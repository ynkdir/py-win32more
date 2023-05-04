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
import Windows.Networking
import Windows.Networking.Proximity
import Windows.Networking.Sockets
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
class ConnectionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Proximity.IConnectionRequestedEventArgs
    _classid_ = 'Windows.Networking.Proximity.ConnectionRequestedEventArgs'
    @winrt_mixinmethod
    def get_PeerInformation(self: Windows.Networking.Proximity.IConnectionRequestedEventArgs) -> Windows.Networking.Proximity.PeerInformation: ...
    PeerInformation = property(get_PeerInformation, None)
class DeviceArrivedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.Networking.Proximity.DeviceArrivedEventHandler'
    _iid_ = Guid('{efa9da69-f6e1-49c9-a49e-8e0fc58fb911}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Networking.Proximity.ProximityDevice) -> Void: ...
class DeviceDepartedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.Networking.Proximity.DeviceDepartedEventHandler'
    _iid_ = Guid('{efa9da69-f6e2-49c9-a49e-8e0fc58fb911}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Networking.Proximity.ProximityDevice) -> Void: ...
class IConnectionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IConnectionRequestedEventArgs'
    _iid_ = Guid('{eb6891ae-4f1e-4c66-bd0d-46924a942e08}')
    @winrt_commethod(6)
    def get_PeerInformation(self) -> Windows.Networking.Proximity.PeerInformation: ...
    PeerInformation = property(get_PeerInformation, None)
class IPeerFinderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IPeerFinderStatics'
    _iid_ = Guid('{914b3b61-f6e1-47c4-a14c-148a1903d0c6}')
    @winrt_commethod(6)
    def get_AllowBluetooth(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowBluetooth(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AllowInfrastructure(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AllowInfrastructure(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_AllowWiFiDirect(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AllowWiFiDirect(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_SupportedDiscoveryTypes(self) -> Windows.Networking.Proximity.PeerDiscoveryTypes: ...
    @winrt_commethod(15)
    def get_AlternateIdentities(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(16)
    def Start(self) -> Void: ...
    @winrt_commethod(17)
    def StartWithMessage(self, peerMessage: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    @winrt_commethod(19)
    def add_TriggeredConnectionStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Networking.Proximity.TriggeredConnectionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_TriggeredConnectionStateChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_ConnectionRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Networking.Proximity.ConnectionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_ConnectionRequested(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def FindAllPeersAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Proximity.PeerInformation]]: ...
    @winrt_commethod(24)
    def ConnectAsync(self, peerInformation: Windows.Networking.Proximity.PeerInformation) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Sockets.StreamSocket]: ...
    AllowBluetooth = property(get_AllowBluetooth, put_AllowBluetooth)
    AllowInfrastructure = property(get_AllowInfrastructure, put_AllowInfrastructure)
    AllowWiFiDirect = property(get_AllowWiFiDirect, put_AllowWiFiDirect)
    DisplayName = property(get_DisplayName, put_DisplayName)
    SupportedDiscoveryTypes = property(get_SupportedDiscoveryTypes, None)
    AlternateIdentities = property(get_AlternateIdentities, None)
class IPeerFinderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IPeerFinderStatics2'
    _iid_ = Guid('{d6e73c65-fdd0-4b0b-9312-866408935d82}')
    @winrt_commethod(6)
    def get_Role(self) -> Windows.Networking.Proximity.PeerRole: ...
    @winrt_commethod(7)
    def put_Role(self, value: Windows.Networking.Proximity.PeerRole) -> Void: ...
    @winrt_commethod(8)
    def get_DiscoveryData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_DiscoveryData(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def CreateWatcher(self) -> Windows.Networking.Proximity.PeerWatcher: ...
    Role = property(get_Role, put_Role)
    DiscoveryData = property(get_DiscoveryData, put_DiscoveryData)
class IPeerInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IPeerInformation'
    _iid_ = Guid('{20024f08-9fff-45f4-b6e9-408b2ebef373}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
class IPeerInformation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IPeerInformation3'
    _iid_ = Guid('{b20f612a-dbd0-40f8-95bd-2d4209c7836f}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DiscoveryData(self) -> Windows.Storage.Streams.IBuffer: ...
    Id = property(get_Id, None)
    DiscoveryData = property(get_DiscoveryData, None)
class IPeerInformationWithHostAndService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IPeerInformationWithHostAndService'
    _iid_ = Guid('{ecc7ccad-1b70-4e8b-92db-bbe781419308}')
    @winrt_commethod(6)
    def get_HostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_ServiceName(self) -> WinRT_String: ...
    HostName = property(get_HostName, None)
    ServiceName = property(get_ServiceName, None)
class IPeerWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IPeerWatcher'
    _iid_ = Guid('{3cee21f8-2fa6-4679-9691-03c94a420f34}')
    @winrt_commethod(6)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Networking.Proximity.PeerInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Networking.Proximity.PeerInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Networking.Proximity.PeerInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> Windows.Networking.Proximity.PeerWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IProximityDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IProximityDevice'
    _iid_ = Guid('{efa8a552-f6e1-4329-a0fc-ab6b0fd28262}')
    @winrt_commethod(6)
    def SubscribeForMessage(self, messageType: WinRT_String, messageReceivedHandler: Windows.Networking.Proximity.MessageReceivedHandler) -> Int64: ...
    @winrt_commethod(7)
    def PublishMessage(self, messageType: WinRT_String, message: WinRT_String) -> Int64: ...
    @winrt_commethod(8)
    def PublishMessageWithCallback(self, messageType: WinRT_String, message: WinRT_String, messageTransmittedHandler: Windows.Networking.Proximity.MessageTransmittedHandler) -> Int64: ...
    @winrt_commethod(9)
    def PublishBinaryMessage(self, messageType: WinRT_String, message: Windows.Storage.Streams.IBuffer) -> Int64: ...
    @winrt_commethod(10)
    def PublishBinaryMessageWithCallback(self, messageType: WinRT_String, message: Windows.Storage.Streams.IBuffer, messageTransmittedHandler: Windows.Networking.Proximity.MessageTransmittedHandler) -> Int64: ...
    @winrt_commethod(11)
    def PublishUriMessage(self, message: Windows.Foundation.Uri) -> Int64: ...
    @winrt_commethod(12)
    def PublishUriMessageWithCallback(self, message: Windows.Foundation.Uri, messageTransmittedHandler: Windows.Networking.Proximity.MessageTransmittedHandler) -> Int64: ...
    @winrt_commethod(13)
    def StopSubscribingForMessage(self, subscriptionId: Int64) -> Void: ...
    @winrt_commethod(14)
    def StopPublishingMessage(self, messageId: Int64) -> Void: ...
    @winrt_commethod(15)
    def add_DeviceArrived(self, arrivedHandler: Windows.Networking.Proximity.DeviceArrivedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DeviceArrived(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_DeviceDeparted(self, departedHandler: Windows.Networking.Proximity.DeviceDepartedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_DeviceDeparted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def get_MaxMessageBytes(self) -> UInt32: ...
    @winrt_commethod(20)
    def get_BitsPerSecond(self) -> UInt64: ...
    @winrt_commethod(21)
    def get_DeviceId(self) -> WinRT_String: ...
    MaxMessageBytes = property(get_MaxMessageBytes, None)
    BitsPerSecond = property(get_BitsPerSecond, None)
    DeviceId = property(get_DeviceId, None)
class IProximityDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IProximityDeviceStatics'
    _iid_ = Guid('{914ba01d-f6e1-47c4-a14c-148a1903d0c6}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDefault(self) -> Windows.Networking.Proximity.ProximityDevice: ...
    @winrt_commethod(8)
    def FromId(self, deviceId: WinRT_String) -> Windows.Networking.Proximity.ProximityDevice: ...
class IProximityMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.IProximityMessage'
    _iid_ = Guid('{efab0782-f6e1-4675-a045-d8e320c24808}')
    @winrt_commethod(6)
    def get_MessageType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SubscriptionId(self) -> Int64: ...
    @winrt_commethod(8)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def get_DataAsString(self) -> WinRT_String: ...
    MessageType = property(get_MessageType, None)
    SubscriptionId = property(get_SubscriptionId, None)
    Data = property(get_Data, None)
    DataAsString = property(get_DataAsString, None)
class ITriggeredConnectionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.ITriggeredConnectionStateChangedEventArgs'
    _iid_ = Guid('{c6a780ad-f6e1-4d54-96e2-33f620bca88a}')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Networking.Proximity.TriggeredConnectState: ...
    @winrt_commethod(7)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Socket(self) -> Windows.Networking.Sockets.StreamSocket: ...
    State = property(get_State, None)
    Id = property(get_Id, None)
    Socket = property(get_Socket, None)
class MessageReceivedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.Networking.Proximity.MessageReceivedHandler'
    _iid_ = Guid('{efab0782-f6e2-4675-a045-d8e320c24808}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Networking.Proximity.ProximityDevice, message: Windows.Networking.Proximity.ProximityMessage) -> Void: ...
class MessageTransmittedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.Networking.Proximity.MessageTransmittedHandler'
    _iid_ = Guid('{efaa0b4a-f6e2-4d7d-856c-78fc8efc021e}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Networking.Proximity.ProximityDevice, messageId: Int64) -> Void: ...
PeerDiscoveryTypes = UInt32
PeerDiscoveryTypes_None: PeerDiscoveryTypes = 0
PeerDiscoveryTypes_Browse: PeerDiscoveryTypes = 1
PeerDiscoveryTypes_Triggered: PeerDiscoveryTypes = 2
class PeerFinder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Proximity.PeerFinder'
    @winrt_classmethod
    def get_Role(cls: Windows.Networking.Proximity.IPeerFinderStatics2) -> Windows.Networking.Proximity.PeerRole: ...
    @winrt_classmethod
    def put_Role(cls: Windows.Networking.Proximity.IPeerFinderStatics2, value: Windows.Networking.Proximity.PeerRole) -> Void: ...
    @winrt_classmethod
    def get_DiscoveryData(cls: Windows.Networking.Proximity.IPeerFinderStatics2) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def put_DiscoveryData(cls: Windows.Networking.Proximity.IPeerFinderStatics2, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Networking.Proximity.IPeerFinderStatics2) -> Windows.Networking.Proximity.PeerWatcher: ...
    @winrt_classmethod
    def get_AllowBluetooth(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AllowBluetooth(cls: Windows.Networking.Proximity.IPeerFinderStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_AllowInfrastructure(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AllowInfrastructure(cls: Windows.Networking.Proximity.IPeerFinderStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_AllowWiFiDirect(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Boolean: ...
    @winrt_classmethod
    def put_AllowWiFiDirect(cls: Windows.Networking.Proximity.IPeerFinderStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_DisplayName(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> WinRT_String: ...
    @winrt_classmethod
    def put_DisplayName(cls: Windows.Networking.Proximity.IPeerFinderStatics, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_SupportedDiscoveryTypes(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Windows.Networking.Proximity.PeerDiscoveryTypes: ...
    @winrt_classmethod
    def get_AlternateIdentities(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_classmethod
    def Start(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Void: ...
    @winrt_classmethod
    def StartWithMessage(cls: Windows.Networking.Proximity.IPeerFinderStatics, peerMessage: WinRT_String) -> Void: ...
    @winrt_classmethod
    def Stop(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Void: ...
    @winrt_classmethod
    def add_TriggeredConnectionStateChanged(cls: Windows.Networking.Proximity.IPeerFinderStatics, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Networking.Proximity.TriggeredConnectionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_TriggeredConnectionStateChanged(cls: Windows.Networking.Proximity.IPeerFinderStatics, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ConnectionRequested(cls: Windows.Networking.Proximity.IPeerFinderStatics, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.Networking.Proximity.ConnectionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ConnectionRequested(cls: Windows.Networking.Proximity.IPeerFinderStatics, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FindAllPeersAsync(cls: Windows.Networking.Proximity.IPeerFinderStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Proximity.PeerInformation]]: ...
    @winrt_classmethod
    def ConnectAsync(cls: Windows.Networking.Proximity.IPeerFinderStatics, peerInformation: Windows.Networking.Proximity.PeerInformation) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Sockets.StreamSocket]: ...
    Role = property(get_Role, put_Role)
    DiscoveryData = property(get_DiscoveryData, put_DiscoveryData)
    AllowBluetooth = property(get_AllowBluetooth, put_AllowBluetooth)
    AllowInfrastructure = property(get_AllowInfrastructure, put_AllowInfrastructure)
    AllowWiFiDirect = property(get_AllowWiFiDirect, put_AllowWiFiDirect)
    DisplayName = property(get_DisplayName, put_DisplayName)
    SupportedDiscoveryTypes = property(get_SupportedDiscoveryTypes, None)
    AlternateIdentities = property(get_AlternateIdentities, None)
class PeerInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Proximity.IPeerInformation
    _classid_ = 'Windows.Networking.Proximity.PeerInformation'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Networking.Proximity.IPeerInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.Proximity.IPeerInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DiscoveryData(self: Windows.Networking.Proximity.IPeerInformation3) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_HostName(self: Windows.Networking.Proximity.IPeerInformationWithHostAndService) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_ServiceName(self: Windows.Networking.Proximity.IPeerInformationWithHostAndService) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    DiscoveryData = property(get_DiscoveryData, None)
    HostName = property(get_HostName, None)
    ServiceName = property(get_ServiceName, None)
PeerRole = Int32
PeerRole_Peer: PeerRole = 0
PeerRole_Host: PeerRole = 1
PeerRole_Client: PeerRole = 2
class PeerWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Proximity.IPeerWatcher
    _classid_ = 'Windows.Networking.Proximity.PeerWatcher'
    @winrt_mixinmethod
    def add_Added(self: Windows.Networking.Proximity.IPeerWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Networking.Proximity.PeerInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Networking.Proximity.IPeerWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Networking.Proximity.IPeerWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Networking.Proximity.PeerInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Networking.Proximity.IPeerWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Networking.Proximity.IPeerWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Networking.Proximity.PeerInformation]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Networking.Proximity.IPeerWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Networking.Proximity.IPeerWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Networking.Proximity.IPeerWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Networking.Proximity.IPeerWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Proximity.PeerWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Networking.Proximity.IPeerWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.Proximity.IPeerWatcher) -> Windows.Networking.Proximity.PeerWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Networking.Proximity.IPeerWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Networking.Proximity.IPeerWatcher) -> Void: ...
    Status = property(get_Status, None)
PeerWatcherStatus = Int32
PeerWatcherStatus_Created: PeerWatcherStatus = 0
PeerWatcherStatus_Started: PeerWatcherStatus = 1
PeerWatcherStatus_EnumerationCompleted: PeerWatcherStatus = 2
PeerWatcherStatus_Stopping: PeerWatcherStatus = 3
PeerWatcherStatus_Stopped: PeerWatcherStatus = 4
PeerWatcherStatus_Aborted: PeerWatcherStatus = 5
class ProximityDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Proximity.IProximityDevice
    _classid_ = 'Windows.Networking.Proximity.ProximityDevice'
    @winrt_mixinmethod
    def SubscribeForMessage(self: Windows.Networking.Proximity.IProximityDevice, messageType: WinRT_String, messageReceivedHandler: Windows.Networking.Proximity.MessageReceivedHandler) -> Int64: ...
    @winrt_mixinmethod
    def PublishMessage(self: Windows.Networking.Proximity.IProximityDevice, messageType: WinRT_String, message: WinRT_String) -> Int64: ...
    @winrt_mixinmethod
    def PublishMessageWithCallback(self: Windows.Networking.Proximity.IProximityDevice, messageType: WinRT_String, message: WinRT_String, messageTransmittedHandler: Windows.Networking.Proximity.MessageTransmittedHandler) -> Int64: ...
    @winrt_mixinmethod
    def PublishBinaryMessage(self: Windows.Networking.Proximity.IProximityDevice, messageType: WinRT_String, message: Windows.Storage.Streams.IBuffer) -> Int64: ...
    @winrt_mixinmethod
    def PublishBinaryMessageWithCallback(self: Windows.Networking.Proximity.IProximityDevice, messageType: WinRT_String, message: Windows.Storage.Streams.IBuffer, messageTransmittedHandler: Windows.Networking.Proximity.MessageTransmittedHandler) -> Int64: ...
    @winrt_mixinmethod
    def PublishUriMessage(self: Windows.Networking.Proximity.IProximityDevice, message: Windows.Foundation.Uri) -> Int64: ...
    @winrt_mixinmethod
    def PublishUriMessageWithCallback(self: Windows.Networking.Proximity.IProximityDevice, message: Windows.Foundation.Uri, messageTransmittedHandler: Windows.Networking.Proximity.MessageTransmittedHandler) -> Int64: ...
    @winrt_mixinmethod
    def StopSubscribingForMessage(self: Windows.Networking.Proximity.IProximityDevice, subscriptionId: Int64) -> Void: ...
    @winrt_mixinmethod
    def StopPublishingMessage(self: Windows.Networking.Proximity.IProximityDevice, messageId: Int64) -> Void: ...
    @winrt_mixinmethod
    def add_DeviceArrived(self: Windows.Networking.Proximity.IProximityDevice, arrivedHandler: Windows.Networking.Proximity.DeviceArrivedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceArrived(self: Windows.Networking.Proximity.IProximityDevice, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeviceDeparted(self: Windows.Networking.Proximity.IProximityDevice, departedHandler: Windows.Networking.Proximity.DeviceDepartedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceDeparted(self: Windows.Networking.Proximity.IProximityDevice, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MaxMessageBytes(self: Windows.Networking.Proximity.IProximityDevice) -> UInt32: ...
    @winrt_mixinmethod
    def get_BitsPerSecond(self: Windows.Networking.Proximity.IProximityDevice) -> UInt64: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.Proximity.IProximityDevice) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Networking.Proximity.IProximityDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Networking.Proximity.IProximityDeviceStatics) -> Windows.Networking.Proximity.ProximityDevice: ...
    @winrt_classmethod
    def FromId(cls: Windows.Networking.Proximity.IProximityDeviceStatics, deviceId: WinRT_String) -> Windows.Networking.Proximity.ProximityDevice: ...
    MaxMessageBytes = property(get_MaxMessageBytes, None)
    BitsPerSecond = property(get_BitsPerSecond, None)
    DeviceId = property(get_DeviceId, None)
class ProximityMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Proximity.IProximityMessage
    _classid_ = 'Windows.Networking.Proximity.ProximityMessage'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Proximity.IProximityMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SubscriptionId(self: Windows.Networking.Proximity.IProximityMessage) -> Int64: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Networking.Proximity.IProximityMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_DataAsString(self: Windows.Networking.Proximity.IProximityMessage) -> WinRT_String: ...
    MessageType = property(get_MessageType, None)
    SubscriptionId = property(get_SubscriptionId, None)
    Data = property(get_Data, None)
    DataAsString = property(get_DataAsString, None)
TriggeredConnectState = Int32
TriggeredConnectState_PeerFound: TriggeredConnectState = 0
TriggeredConnectState_Listening: TriggeredConnectState = 1
TriggeredConnectState_Connecting: TriggeredConnectState = 2
TriggeredConnectState_Completed: TriggeredConnectState = 3
TriggeredConnectState_Canceled: TriggeredConnectState = 4
TriggeredConnectState_Failed: TriggeredConnectState = 5
class TriggeredConnectionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Proximity.ITriggeredConnectionStateChangedEventArgs
    _classid_ = 'Windows.Networking.Proximity.TriggeredConnectionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.Networking.Proximity.ITriggeredConnectionStateChangedEventArgs) -> Windows.Networking.Proximity.TriggeredConnectState: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.Proximity.ITriggeredConnectionStateChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_Socket(self: Windows.Networking.Proximity.ITriggeredConnectionStateChangedEventArgs) -> Windows.Networking.Sockets.StreamSocket: ...
    State = property(get_State, None)
    Id = property(get_Id, None)
    Socket = property(get_Socket, None)
make_head(_module, 'ConnectionRequestedEventArgs')
make_head(_module, 'DeviceArrivedEventHandler')
make_head(_module, 'DeviceDepartedEventHandler')
make_head(_module, 'IConnectionRequestedEventArgs')
make_head(_module, 'IPeerFinderStatics')
make_head(_module, 'IPeerFinderStatics2')
make_head(_module, 'IPeerInformation')
make_head(_module, 'IPeerInformation3')
make_head(_module, 'IPeerInformationWithHostAndService')
make_head(_module, 'IPeerWatcher')
make_head(_module, 'IProximityDevice')
make_head(_module, 'IProximityDeviceStatics')
make_head(_module, 'IProximityMessage')
make_head(_module, 'ITriggeredConnectionStateChangedEventArgs')
make_head(_module, 'MessageReceivedHandler')
make_head(_module, 'MessageTransmittedHandler')
make_head(_module, 'PeerFinder')
make_head(_module, 'PeerInformation')
make_head(_module, 'PeerWatcher')
make_head(_module, 'ProximityDevice')
make_head(_module, 'ProximityMessage')
make_head(_module, 'TriggeredConnectionStateChangedEventArgs')
