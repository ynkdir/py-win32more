from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.I2c
import win32more.Windows.Devices.I2c.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class I2cBusSpeed(Enum, Int32):
    StandardMode = 0
    FastMode = 1
class I2cConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.I2c.II2cConnectionSettings
    _classid_ = 'Windows.Devices.I2c.I2cConnectionSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.I2c.I2cConnectionSettings.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.I2c.II2cConnectionSettingsFactory, slaveAddress: Int32) -> win32more.Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_mixinmethod
    def get_SlaveAddress(self: win32more.Windows.Devices.I2c.II2cConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_SlaveAddress(self: win32more.Windows.Devices.I2c.II2cConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BusSpeed(self: win32more.Windows.Devices.I2c.II2cConnectionSettings) -> win32more.Windows.Devices.I2c.I2cBusSpeed: ...
    @winrt_mixinmethod
    def put_BusSpeed(self: win32more.Windows.Devices.I2c.II2cConnectionSettings, value: win32more.Windows.Devices.I2c.I2cBusSpeed) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Devices.I2c.II2cConnectionSettings) -> win32more.Windows.Devices.I2c.I2cSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: win32more.Windows.Devices.I2c.II2cConnectionSettings, value: win32more.Windows.Devices.I2c.I2cSharingMode) -> Void: ...
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
class I2cController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.I2c.II2cController
    _classid_ = 'Windows.Devices.I2c.I2cController'
    @winrt_mixinmethod
    def GetDevice(self: win32more.Windows.Devices.I2c.II2cController, settings: win32more.Windows.Devices.I2c.I2cConnectionSettings) -> win32more.Windows.Devices.I2c.I2cDevice: ...
    @winrt_classmethod
    def GetControllersAsync(cls: win32more.Windows.Devices.I2c.II2cControllerStatics, provider: win32more.Windows.Devices.I2c.Provider.II2cProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.I2c.I2cController]]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.I2c.II2cControllerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.I2c.I2cController]: ...
class I2cDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.I2c.II2cDevice
    _classid_ = 'Windows.Devices.I2c.I2cDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.I2c.II2cDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionSettings(self: win32more.Windows.Devices.I2c.II2cDevice) -> win32more.Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_mixinmethod
    def Write(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def WritePartial(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: PassArray[Byte]) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def Read(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: FillArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def ReadPartial(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: FillArray[Byte]) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def WriteRead(self: win32more.Windows.Devices.I2c.II2cDevice, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def WriteReadPartial(self: win32more.Windows.Devices.I2c.II2cDevice, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.I2c.II2cDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: win32more.Windows.Devices.I2c.II2cDeviceStatics, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.I2c.II2cDeviceStatics, deviceId: WinRT_String, settings: win32more.Windows.Devices.I2c.I2cConnectionSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.I2c.I2cDevice]: ...
    ConnectionSettings = property(get_ConnectionSettings, None)
    DeviceId = property(get_DeviceId, None)
class I2cSharingMode(Enum, Int32):
    Exclusive = 0
    Shared = 1
class I2cTransferResult(Structure):
    Status: win32more.Windows.Devices.I2c.I2cTransferStatus
    BytesTransferred: UInt32
class I2cTransferStatus(Enum, Int32):
    FullTransfer = 0
    PartialTransfer = 1
    SlaveAddressNotAcknowledged = 2
    ClockStretchTimeout = 3
    UnknownError = 4
class II2cConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.II2cConnectionSettings'
    _iid_ = Guid('{f2db1307-ab6f-4639-a767-54536dc3460f}')
    @winrt_commethod(6)
    def get_SlaveAddress(self) -> Int32: ...
    @winrt_commethod(7)
    def put_SlaveAddress(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_BusSpeed(self) -> win32more.Windows.Devices.I2c.I2cBusSpeed: ...
    @winrt_commethod(9)
    def put_BusSpeed(self, value: win32more.Windows.Devices.I2c.I2cBusSpeed) -> Void: ...
    @winrt_commethod(10)
    def get_SharingMode(self) -> win32more.Windows.Devices.I2c.I2cSharingMode: ...
    @winrt_commethod(11)
    def put_SharingMode(self, value: win32more.Windows.Devices.I2c.I2cSharingMode) -> Void: ...
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
class II2cConnectionSettingsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.II2cConnectionSettingsFactory'
    _iid_ = Guid('{81b586b3-9693-41b1-a243-ded4f6e66926}')
    @winrt_commethod(6)
    def Create(self, slaveAddress: Int32) -> win32more.Windows.Devices.I2c.I2cConnectionSettings: ...
class II2cController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.II2cController'
    _iid_ = Guid('{c48ab1b2-87a0-4166-8e3e-b4b8f97cd729}')
    @winrt_commethod(6)
    def GetDevice(self, settings: win32more.Windows.Devices.I2c.I2cConnectionSettings) -> win32more.Windows.Devices.I2c.I2cDevice: ...
class II2cControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.II2cControllerStatics'
    _iid_ = Guid('{40fc0365-5f05-4e7e-84bd-100db8e0aec5}')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: win32more.Windows.Devices.I2c.Provider.II2cProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.I2c.I2cController]]: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.I2c.I2cController]: ...
class II2cDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.I2c.II2cDevice'
    _iid_ = Guid('{8636c136-b9c5-4f70-9449-cc46dc6f57eb}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> win32more.Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: PassArray[Byte]) -> Void: ...
    @winrt_commethod(9)
    def WritePartial(self, buffer: PassArray[Byte]) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_commethod(10)
    def Read(self, buffer: FillArray[Byte]) -> Void: ...
    @winrt_commethod(11)
    def ReadPartial(self, buffer: FillArray[Byte]) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_commethod(12)
    def WriteRead(self, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    @winrt_commethod(13)
    def WriteReadPartial(self, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    ConnectionSettings = property(get_ConnectionSettings, None)
    DeviceId = property(get_DeviceId, None)
class II2cDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.II2cDeviceStatics'
    _iid_ = Guid('{91a33be3-7334-4512-96bc-fbae9459f5f6}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String, settings: win32more.Windows.Devices.I2c.I2cConnectionSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.I2c.I2cDevice]: ...


make_ready(__name__)
