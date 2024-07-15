from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.Advertisement
import win32more.Windows.Devices.Bluetooth.Background
import win32more.Windows.Devices.Bluetooth.GenericAttributeProfile
import win32more.Windows.Devices.Bluetooth.Rfcomm
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Sockets
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class BluetoothEventTriggeringMode(Enum, Int32):
    Serial = 0
    Batch = 1
    KeepLatest = 2
class BluetoothLEAdvertisementPublisherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.BluetoothLEAdvertisementPublisherTriggerDetails'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_SelectedTransmitPowerLevelInDBm(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails2) -> win32more.Windows.Foundation.IReference[Int16]: ...
    Error = property(get_Error, None)
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
    Status = property(get_Status, None)
class BluetoothLEAdvertisementWatcherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.BluetoothLEAdvertisementWatcherTriggerDetails'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Advertisements(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]: ...
    @winrt_mixinmethod
    def get_SignalStrengthFilter(self: win32more.Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    Advertisements = property(get_Advertisements, None)
    Error = property(get_Error, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, None)
class GattCharacteristicNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.GattCharacteristicNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_Characteristic(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_EventTriggeringMode(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2) -> win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    @winrt_mixinmethod
    def get_ValueChangedEvents(self: win32more.Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]: ...
    Characteristic = property(get_Characteristic, None)
    Error = property(get_Error, None)
    EventTriggeringMode = property(get_EventTriggeringMode, None)
    Value = property(get_Value, None)
    ValueChangedEvents = property(get_ValueChangedEvents, None)
class _GattServiceProviderConnection_Meta_(ComPtr.__class__):
    pass
class GattServiceProviderConnection(ComPtr, metaclass=_GattServiceProviderConnection_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection
    _classid_ = 'Windows.Devices.Bluetooth.Background.GattServiceProviderConnection'
    @winrt_mixinmethod
    def get_TriggerId(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection) -> Void: ...
    @winrt_classmethod
    def get_AllServices(cls: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderConnectionStatics) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection]: ...
    Service = property(get_Service, None)
    TriggerId = property(get_TriggerId, None)
    _GattServiceProviderConnection_Meta_.AllServices = property(get_AllServices, None)
class GattServiceProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.GattServiceProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Devices.Bluetooth.Background.IGattServiceProviderTriggerDetails) -> win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection: ...
    Connection = property(get_Connection, None)
class IBluetoothLEAdvertisementPublisherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails'
    _iid_ = Guid('{610eca86-3480-41c9-a918-7ddadf207e00}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class IBluetoothLEAdvertisementPublisherTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementPublisherTriggerDetails2'
    _iid_ = Guid('{d4a3d025-c601-42d6-9829-4ccb3f5cd77f}')
    @winrt_commethod(6)
    def get_SelectedTransmitPowerLevelInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
class IBluetoothLEAdvertisementWatcherTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IBluetoothLEAdvertisementWatcherTriggerDetails'
    _iid_ = Guid('{a7db5ad7-2257-4e69-9784-fee645c1dce0}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Advertisements(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]: ...
    @winrt_commethod(8)
    def get_SignalStrengthFilter(self) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    Advertisements = property(get_Advertisements, None)
    Error = property(get_Error, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, None)
class IGattCharacteristicNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails'
    _iid_ = Guid('{9ba03b18-0fec-436a-93b1-f46c697532a2}')
    @winrt_commethod(6)
    def get_Characteristic(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Characteristic = property(get_Characteristic, None)
    Value = property(get_Value, None)
class IGattCharacteristicNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattCharacteristicNotificationTriggerDetails2'
    _iid_ = Guid('{727a50dc-949d-454a-b192-983467e3d50f}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_EventTriggeringMode(self) -> win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    @winrt_commethod(8)
    def get_ValueChangedEvents(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]: ...
    Error = property(get_Error, None)
    EventTriggeringMode = property(get_EventTriggeringMode, None)
    ValueChangedEvents = property(get_ValueChangedEvents, None)
class IGattServiceProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattServiceProviderConnection'
    _iid_ = Guid('{7fa1b9b9-2f13-40b5-9582-8eb78e98ef13}')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Service(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    Service = property(get_Service, None)
    TriggerId = property(get_TriggerId, None)
class IGattServiceProviderConnectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattServiceProviderConnectionStatics'
    _iid_ = Guid('{3d509f4b-0b0e-4466-b8cd-6ebdda1fa17d}')
    @winrt_commethod(6)
    def get_AllServices(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection]: ...
    AllServices = property(get_AllServices, None)
class IGattServiceProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IGattServiceProviderTriggerDetails'
    _iid_ = Guid('{ae8c0625-05ff-4afb-b16a-de95f3cf0158}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Devices.Bluetooth.Background.GattServiceProviderConnection: ...
    Connection = property(get_Connection, None)
class IRfcommConnectionTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails'
    _iid_ = Guid('{f922734d-2e3c-4efc-ab59-fc5cf96f97e3}')
    @winrt_commethod(6)
    def get_Socket(self) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_commethod(7)
    def get_Incoming(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_RemoteDevice(self) -> win32more.Windows.Devices.Bluetooth.BluetoothDevice: ...
    Incoming = property(get_Incoming, None)
    RemoteDevice = property(get_RemoteDevice, None)
    Socket = property(get_Socket, None)
class IRfcommInboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation'
    _iid_ = Guid('{6d3e75a8-5429-4059-92e3-1e8b65528707}')
    @winrt_commethod(6)
    def get_SdpRecord(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_SdpRecord(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_LocalServiceId(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(9)
    def put_LocalServiceId(self, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    @winrt_commethod(10)
    def get_ServiceCapabilities(self) -> win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    @winrt_commethod(11)
    def put_ServiceCapabilities(self, value: win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> Void: ...
    LocalServiceId = property(get_LocalServiceId, put_LocalServiceId)
    SdpRecord = property(get_SdpRecord, put_SdpRecord)
    ServiceCapabilities = property(get_ServiceCapabilities, put_ServiceCapabilities)
class IRfcommOutboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation'
    _iid_ = Guid('{b091227b-f434-4cb0-99b1-4ab8cedaedd7}')
    @winrt_commethod(6)
    def get_RemoteServiceId(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(7)
    def put_RemoteServiceId(self, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    RemoteServiceId = property(get_RemoteServiceId, put_RemoteServiceId)
class RfcommConnectionTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails
    _classid_ = 'Windows.Devices.Bluetooth.Background.RfcommConnectionTriggerDetails'
    @winrt_mixinmethod
    def get_Socket(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_Incoming(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_RemoteDevice(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommConnectionTriggerDetails) -> win32more.Windows.Devices.Bluetooth.BluetoothDevice: ...
    Incoming = property(get_Incoming, None)
    RemoteDevice = property(get_RemoteDevice, None)
    Socket = property(get_Socket, None)
class RfcommInboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation
    _classid_ = 'Windows.Devices.Bluetooth.Background.RfcommInboundConnectionInformation'
    @winrt_mixinmethod
    def get_SdpRecord(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_SdpRecord(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_LocalServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def put_LocalServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceCapabilities(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation) -> win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    @winrt_mixinmethod
    def put_ServiceCapabilities(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommInboundConnectionInformation, value: win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> Void: ...
    LocalServiceId = property(get_LocalServiceId, put_LocalServiceId)
    SdpRecord = property(get_SdpRecord, put_SdpRecord)
    ServiceCapabilities = property(get_ServiceCapabilities, put_ServiceCapabilities)
class RfcommOutboundConnectionInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation
    _classid_ = 'Windows.Devices.Bluetooth.Background.RfcommOutboundConnectionInformation'
    @winrt_mixinmethod
    def get_RemoteServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def put_RemoteServiceId(self: win32more.Windows.Devices.Bluetooth.Background.IRfcommOutboundConnectionInformation, value: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Void: ...
    RemoteServiceId = property(get_RemoteServiceId, put_RemoteServiceId)


make_ready(__name__)
