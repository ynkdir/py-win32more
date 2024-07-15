from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.I2c.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class II2cControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.Provider.II2cControllerProvider'
    _iid_ = Guid('{61c2bb82-4510-4163-a87c-4e15a9558980}')
    @winrt_commethod(6)
    def GetDeviceProvider(self, settings: win32more.Windows.Devices.I2c.Provider.ProviderI2cConnectionSettings) -> win32more.Windows.Devices.I2c.Provider.II2cDeviceProvider: ...
class II2cDeviceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.I2c.Provider.II2cDeviceProvider'
    _iid_ = Guid('{ad342654-57e8-453e-8329-d1e447d103a9}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Write(self, buffer: PassArray[Byte]) -> Void: ...
    @winrt_commethod(8)
    def WritePartial(self, buffer: PassArray[Byte]) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    @winrt_commethod(9)
    def Read(self, buffer: FillArray[Byte]) -> Void: ...
    @winrt_commethod(10)
    def ReadPartial(self, buffer: FillArray[Byte]) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    @winrt_commethod(11)
    def WriteRead(self, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    @winrt_commethod(12)
    def WriteReadPartial(self, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    DeviceId = property(get_DeviceId, None)
class II2cProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.Provider.II2cProvider'
    _iid_ = Guid('{6f13083e-bf62-4fe2-a95a-f08999669818}')
    @winrt_commethod(6)
    def GetControllersAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.I2c.Provider.II2cControllerProvider]]: ...
class IProviderI2cConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings'
    _iid_ = Guid('{e9db4e34-e510-44b7-809d-f2f85b555339}')
    @winrt_commethod(6)
    def get_SlaveAddress(self) -> Int32: ...
    @winrt_commethod(7)
    def put_SlaveAddress(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_BusSpeed(self) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cBusSpeed: ...
    @winrt_commethod(9)
    def put_BusSpeed(self, value: win32more.Windows.Devices.I2c.Provider.ProviderI2cBusSpeed) -> Void: ...
    @winrt_commethod(10)
    def get_SharingMode(self) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cSharingMode: ...
    @winrt_commethod(11)
    def put_SharingMode(self, value: win32more.Windows.Devices.I2c.Provider.ProviderI2cSharingMode) -> Void: ...
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
class ProviderI2cBusSpeed(Enum, Int32):
    StandardMode = 0
    FastMode = 1
class ProviderI2cConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings
    _classid_ = 'Windows.Devices.I2c.Provider.ProviderI2cConnectionSettings'
    @winrt_mixinmethod
    def get_SlaveAddress(self: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_SlaveAddress(self: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BusSpeed(self: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cBusSpeed: ...
    @winrt_mixinmethod
    def put_BusSpeed(self: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings, value: win32more.Windows.Devices.I2c.Provider.ProviderI2cBusSpeed) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: win32more.Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings, value: win32more.Windows.Devices.I2c.Provider.ProviderI2cSharingMode) -> Void: ...
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
class ProviderI2cSharingMode(Enum, Int32):
    Exclusive = 0
    Shared = 1
class ProviderI2cTransferResult(Structure):
    Status: win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferStatus
    BytesTransferred: UInt32
class ProviderI2cTransferStatus(Enum, Int32):
    FullTransfer = 0
    PartialTransfer = 1
    SlaveAddressNotAcknowledged = 2


make_ready(__name__)
