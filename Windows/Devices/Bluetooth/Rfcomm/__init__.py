from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Bluetooth
import Windows.Devices.Bluetooth.Rfcomm
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
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
class IRfcommDeviceService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae81ff1f-c5a1-4c40-8c-28-f3-ef-d6-90-62-f3')
    @winrt_commethod(6)
    def get_ConnectionHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_ConnectionServiceName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ServiceId(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(9)
    def get_ProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(10)
    def get_MaxProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(11)
    def GetSdpRawAttributesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[UInt32, Windows.Storage.Streams.IBuffer]]: ...
    @winrt_commethod(12)
    def GetSdpRawAttributesWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[UInt32, Windows.Storage.Streams.IBuffer]]: ...
    ConnectionHostName = property(get_ConnectionHostName, None)
    ConnectionServiceName = property(get_ConnectionServiceName, None)
    ServiceId = property(get_ServiceId, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    MaxProtectionLevel = property(get_MaxProtectionLevel, None)
class IRfcommDeviceService2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('536ced14-ebcd-49fe-bf-9f-40-ef-c6-89-b2-0d')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Devices.Bluetooth.BluetoothDevice: ...
    Device = property(get_Device, None)
class IRfcommDeviceService3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1c22ace6-dd44-4d23-86-6d-8f-34-86-ee-64-90')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class IRfcommDeviceServiceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a4a149ef-626d-41ac-b2-53-87-ac-5c-27-e2-8a')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
class IRfcommDeviceServiceStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa8cb1c9-e78d-4be4-80-76-0a-3d-87-a0-a0-5f')
    @winrt_commethod(6)
    def GetDeviceSelectorForBluetoothDevice(self, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorForBluetoothDeviceWithCacheMode(self, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorForBluetoothDeviceAndServiceId(self, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorForBluetoothDeviceAndServiceIdWithCacheMode(self, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
class IRfcommDeviceServicesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3b48388c-7ccf-488e-96-25-d2-59-a5-73-2d-55')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Services(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    Error = property(get_Error, None)
    Services = property(get_Services, None)
class IRfcommServiceId(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('22629204-7e02-4017-81-36-da-1b-6a-1b-9b-bf')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def AsShortId(self) -> UInt32: ...
    @winrt_commethod(8)
    def AsString(self) -> WinRT_String: ...
    Uuid = property(get_Uuid, None)
class IRfcommServiceIdStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2a179eba-a975-46e3-b5-6b-08-ff-d7-83-a5-fe')
    @winrt_commethod(6)
    def FromUuid(self, uuid: Guid) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(7)
    def FromShortId(self, shortId: UInt32) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(8)
    def get_SerialPort(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(9)
    def get_ObexObjectPush(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(10)
    def get_ObexFileTransfer(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(11)
    def get_PhoneBookAccessPce(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(12)
    def get_PhoneBookAccessPse(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(13)
    def get_GenericFileTransfer(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    SerialPort = property(get_SerialPort, None)
    ObexObjectPush = property(get_ObexObjectPush, None)
    ObexFileTransfer = property(get_ObexFileTransfer, None)
    PhoneBookAccessPce = property(get_PhoneBookAccessPce, None)
    PhoneBookAccessPse = property(get_PhoneBookAccessPse, None)
    GenericFileTransfer = property(get_GenericFileTransfer, None)
class IRfcommServiceProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eadbfdc4-b1f6-44ff-9f-7c-e7-a8-2a-b8-68-21')
    @winrt_commethod(6)
    def get_ServiceId(self) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_commethod(7)
    def get_SdpRawAttributes(self) -> Windows.Foundation.Collections.IMap[UInt32, Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(8)
    def StartAdvertising(self, listener: Windows.Networking.Sockets.StreamSocketListener) -> Void: ...
    @winrt_commethod(9)
    def StopAdvertising(self) -> Void: ...
    ServiceId = property(get_ServiceId, None)
    SdpRawAttributes = property(get_SdpRawAttributes, None)
class IRfcommServiceProvider2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('736bdfc6-3c81-4d1e-ba-f2-dd-bb-81-28-45-12')
    @winrt_commethod(6)
    def StartAdvertisingWithRadioDiscoverability(self, listener: Windows.Networking.Sockets.StreamSocketListener, radioDiscoverable: Boolean) -> Void: ...
class IRfcommServiceProviderStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('98888303-69ca-413a-84-f7-43-44-c7-29-29-97')
    @winrt_commethod(6)
    def CreateAsync(self, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommServiceProvider]: ...
class RfcommDeviceService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService'
    @winrt_mixinmethod
    def get_ConnectionHostName(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_ConnectionServiceName(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def get_MaxProtectionLevel(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def GetSdpRawAttributesAsync(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[UInt32, Windows.Storage.Streams.IBuffer]]: ...
    @winrt_mixinmethod
    def GetSdpRawAttributesWithCacheModeAsync(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[UInt32, Windows.Storage.Streams.IBuffer]]: ...
    @winrt_mixinmethod
    def get_Device(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService2) -> Windows.Devices.Bluetooth.BluetoothDevice: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService3) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceService3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDevice(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceWithCacheMode(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceAndServiceId(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceAndServiceIdWithCacheMode(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics2, bluetoothDevice: Windows.Devices.Bluetooth.BluetoothDevice, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServiceStatics, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> WinRT_String: ...
    ConnectionHostName = property(get_ConnectionHostName, None)
    ConnectionServiceName = property(get_ConnectionServiceName, None)
    ServiceId = property(get_ServiceId, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    MaxProtectionLevel = property(get_MaxProtectionLevel, None)
    Device = property(get_Device, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class RfcommDeviceServicesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult'
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServicesResult) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Services(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommDeviceServicesResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    Error = property(get_Error, None)
    Services = property(get_Services, None)
class RfcommServiceId(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId'
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId) -> Guid: ...
    @winrt_mixinmethod
    def AsShortId(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId) -> UInt32: ...
    @winrt_mixinmethod
    def AsString(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceId) -> WinRT_String: ...
    @winrt_classmethod
    def FromUuid(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics, uuid: Guid) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def FromShortId(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics, shortId: UInt32) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_SerialPort(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_ObexObjectPush(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_ObexFileTransfer(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_PhoneBookAccessPce(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_PhoneBookAccessPse(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_classmethod
    def get_GenericFileTransfer(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceIdStatics) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    Uuid = property(get_Uuid, None)
    SerialPort = property(get_SerialPort, None)
    ObexObjectPush = property(get_ObexObjectPush, None)
    ObexFileTransfer = property(get_ObexFileTransfer, None)
    PhoneBookAccessPce = property(get_PhoneBookAccessPce, None)
    PhoneBookAccessPse = property(get_PhoneBookAccessPse, None)
    GenericFileTransfer = property(get_GenericFileTransfer, None)
class RfcommServiceProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Rfcomm.RfcommServiceProvider'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider) -> Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId: ...
    @winrt_mixinmethod
    def get_SdpRawAttributes(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider) -> Windows.Foundation.Collections.IMap[UInt32, Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def StartAdvertising(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider, listener: Windows.Networking.Sockets.StreamSocketListener) -> Void: ...
    @winrt_mixinmethod
    def StopAdvertising(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider) -> Void: ...
    @winrt_mixinmethod
    def StartAdvertisingWithRadioDiscoverability(self: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProvider2, listener: Windows.Networking.Sockets.StreamSocketListener, radioDiscoverable: Boolean) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Devices.Bluetooth.Rfcomm.IRfcommServiceProviderStatics, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommServiceProvider]: ...
    ServiceId = property(get_ServiceId, None)
    SdpRawAttributes = property(get_SdpRawAttributes, None)
make_head(_module, 'IRfcommDeviceService')
make_head(_module, 'IRfcommDeviceService2')
make_head(_module, 'IRfcommDeviceService3')
make_head(_module, 'IRfcommDeviceServiceStatics')
make_head(_module, 'IRfcommDeviceServiceStatics2')
make_head(_module, 'IRfcommDeviceServicesResult')
make_head(_module, 'IRfcommServiceId')
make_head(_module, 'IRfcommServiceIdStatics')
make_head(_module, 'IRfcommServiceProvider')
make_head(_module, 'IRfcommServiceProvider2')
make_head(_module, 'IRfcommServiceProviderStatics')
make_head(_module, 'RfcommDeviceService')
make_head(_module, 'RfcommDeviceServicesResult')
make_head(_module, 'RfcommServiceId')
make_head(_module, 'RfcommServiceProvider')
