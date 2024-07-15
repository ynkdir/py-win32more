from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.Rfcomm
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Sockets
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class IRfcommDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService'
    _iid_ = Guid('{ae81ff1f-c5a1-4c40-8c28-f3efd69062f3}')
    @winrt_commethod(6)
    def get_ConnectionHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_ConnectionServiceName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ServiceId(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(9)
    def get_ProtectionLevel(self) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(10)
    def get_MaxProtectionLevel(self) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(11)
    def GetSdpRawAttributesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[UInt32, win32more.Windows.Storage.Streams.IBuffer]]: ...
    @winrt_commethod(12)
    def GetSdpRawAttributesWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[UInt32, win32more.Windows.Storage.Streams.IBuffer]]: ...
    ConnectionHostName = property(get_ConnectionHostName, None)
    ConnectionServiceName = property(get_ConnectionServiceName, None)
    MaxProtectionLevel = property(get_MaxProtectionLevel, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    ServiceId = property(get_ServiceId, None)
class IRfcommDeviceService2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService2'
    _iid_ = Guid('{536ced14-ebcd-49fe-bf9f-40efc689b20d}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Bluetooth.BluetoothDevice: ...
    Device = property(get_Device, None)
class IRfcommDeviceService3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService3'
    _iid_ = Guid('{1c22ace6-dd44-4d23-866d-8f3486ee6490}')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class IRfcommDeviceServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics'
    _iid_ = Guid('{a4a149ef-626d-41ac-b253-87ac5c27e28a}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
class IRfcommDeviceServiceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2'
    _iid_ = Guid('{aa8cb1c9-e78d-4be4-8076-0a3d87a0a05f}')
    @winrt_commethod(6)
    def GetDeviceSelectorForBluetoothDevice(self, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorForBluetoothDeviceWithCacheMode(self, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorForBluetoothDeviceAndServiceId(self, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorForBluetoothDeviceAndServiceIdWithCacheMode(self, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
class IRfcommDeviceServicesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServicesResult'
    _iid_ = Guid('{3b48388c-7ccf-488e-9625-d259a5732d55}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Services(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    Error = property(get_Error, None)
    Services = property(get_Services, None)
class IRfcommServiceId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId'
    _iid_ = Guid('{22629204-7e02-4017-8136-da1b6a1b9bbf}')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def AsShortId(self) -> UInt32: ...
    @winrt_commethod(8)
    def AsString(self) -> WinRT_String: ...
    Uuid = property(get_Uuid, None)
class IRfcommServiceIdStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics'
    _iid_ = Guid('{2a179eba-a975-46e3-b56b-08ffd783a5fe}')
    @winrt_commethod(6)
    def FromUuid(self, uuid: Guid) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(7)
    def FromShortId(self, shortId: UInt32) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(8)
    def get_SerialPort(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(9)
    def get_ObexObjectPush(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(10)
    def get_ObexFileTransfer(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(11)
    def get_PhoneBookAccessPce(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(12)
    def get_PhoneBookAccessPse(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(13)
    def get_GenericFileTransfer(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    GenericFileTransfer = property(get_GenericFileTransfer, None)
    ObexFileTransfer = property(get_ObexFileTransfer, None)
    ObexObjectPush = property(get_ObexObjectPush, None)
    PhoneBookAccessPce = property(get_PhoneBookAccessPce, None)
    PhoneBookAccessPse = property(get_PhoneBookAccessPse, None)
    SerialPort = property(get_SerialPort, None)
class IRfcommServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider'
    _iid_ = Guid('{eadbfdc4-b1f6-44ff-9f7c-e7a82ab86821}')
    @winrt_commethod(6)
    def get_ServiceId(self) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(7)
    def get_SdpRawAttributes(self) -> win32more.Windows.Foundation.Collections.IMap[UInt32, win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(8)
    def StartAdvertising(self, listener: win32more.Windows.Networking.Sockets.StreamSocketListener) -> Void: ...
    @winrt_commethod(9)
    def StopAdvertising(self) -> Void: ...
    SdpRawAttributes = property(get_SdpRawAttributes, None)
    ServiceId = property(get_ServiceId, None)
class IRfcommServiceProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider2'
    _iid_ = Guid('{736bdfc6-3c81-4d1e-baf2-ddbb81284512}')
    @winrt_commethod(6)
    def StartAdvertisingWithRadioDiscoverability(self, listener: win32more.Windows.Networking.Sockets.StreamSocketListener, radioDiscoverable: Boolean) -> Void: ...
class IRfcommServiceProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProviderStatics'
    _iid_ = Guid('{98888303-69ca-413a-84f7-4344c7292997}')
    @winrt_commethod(6)
    def CreateAsync(self, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceProvider]: ...
class RfcommDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService'
    @winrt_mixinmethod
    def get_ConnectionHostName(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_ConnectionServiceName(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def get_MaxProtectionLevel(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def GetSdpRawAttributesAsync(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[UInt32, win32more.Windows.Storage.Streams.IBuffer]]: ...
    @winrt_mixinmethod
    def GetSdpRawAttributesWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[UInt32, win32more.Windows.Storage.Streams.IBuffer]]: ...
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService2) -> win32more.Windows.Devices.Bluetooth.BluetoothDevice: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService3) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDevice(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceWithCacheMode(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceAndServiceId(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceAndServiceIdWithCacheMode(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: win32more.Windows.Devices.Bluetooth.BluetoothDevice, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
    ConnectionHostName = property(get_ConnectionHostName, None)
    ConnectionServiceName = property(get_ConnectionServiceName, None)
    Device = property(get_Device, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    MaxProtectionLevel = property(get_MaxProtectionLevel, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    ServiceId = property(get_ServiceId, None)
class RfcommDeviceServicesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServicesResult
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServicesResult) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Services(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServicesResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    Error = property(get_Error, None)
    Services = property(get_Services, None)
class _RfcommServiceId_Meta_(ComPtr.__class__):
    pass
class RfcommServiceId(ComPtr, metaclass=_RfcommServiceId_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId'
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId) -> Guid: ...
    @winrt_mixinmethod
    def AsShortId(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId) -> UInt32: ...
    @winrt_mixinmethod
    def AsString(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId) -> WinRT_String: ...
    @winrt_classmethod
    def FromUuid(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics, uuid: Guid) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def FromShortId(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics, shortId: UInt32) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_SerialPort(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_ObexObjectPush(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_ObexFileTransfer(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_PhoneBookAccessPce(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_PhoneBookAccessPse(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_GenericFileTransfer(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    Uuid = property(get_Uuid, None)
    _RfcommServiceId_Meta_.GenericFileTransfer = property(get_GenericFileTransfer, None)
    _RfcommServiceId_Meta_.ObexFileTransfer = property(get_ObexFileTransfer, None)
    _RfcommServiceId_Meta_.ObexObjectPush = property(get_ObexObjectPush, None)
    _RfcommServiceId_Meta_.PhoneBookAccessPce = property(get_PhoneBookAccessPce, None)
    _RfcommServiceId_Meta_.PhoneBookAccessPse = property(get_PhoneBookAccessPse, None)
    _RfcommServiceId_Meta_.SerialPort = property(get_SerialPort, None)
class RfcommServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider
    _classid_ = 'Windows.Devices.Bluetooth.Rfcomm.RfcommServiceProvider'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider) -> win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def get_SdpRawAttributes(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider) -> win32more.Windows.Foundation.Collections.IMap[UInt32, win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def StartAdvertising(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider, listener: win32more.Windows.Networking.Sockets.StreamSocketListener) -> Void: ...
    @winrt_mixinmethod
    def StopAdvertising(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider) -> Void: ...
    @winrt_mixinmethod
    def StartAdvertisingWithRadioDiscoverability(self: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider2, listener: win32more.Windows.Networking.Sockets.StreamSocketListener, radioDiscoverable: Boolean) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProviderStatics, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceProvider]: ...
    SdpRawAttributes = property(get_SdpRawAttributes, None)
    ServiceId = property(get_ServiceId, None)


make_ready(__name__)
