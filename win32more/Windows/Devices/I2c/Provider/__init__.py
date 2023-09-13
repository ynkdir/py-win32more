from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.I2c.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class II2cControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.Provider.II2cControllerProvider'
    _iid_ = Guid('{61c2bb82-4510-4163-a87c-4e15a9558980}')
    @winrt_commethod(6)
    def GetDeviceProvider(self, settings: win32more.Windows.Devices.I2c.Provider.ProviderI2cConnectionSettings) -> win32more.Windows.Devices.I2c.Provider.II2cDeviceProvider: ...
class II2cDeviceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.I2c.Provider.II2cDeviceProvider'
    _iid_ = Guid('{ad342654-57e8-453e-8329-d1e447d103a9}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Write(self, buffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(8)
    def WritePartial(self, buffer: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    @winrt_commethod(9)
    def Read(self, buffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(10)
    def ReadPartial(self, buffer: Annotated[SZArray[Byte], 'Out']) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    @winrt_commethod(11)
    def WriteRead(self, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(12)
    def WriteReadPartial(self, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
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
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
ProviderI2cBusSpeed = Int32
ProviderI2cBusSpeed_StandardMode: ProviderI2cBusSpeed = 0
ProviderI2cBusSpeed_FastMode: ProviderI2cBusSpeed = 1
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
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
ProviderI2cSharingMode = Int32
ProviderI2cSharingMode_Exclusive: ProviderI2cSharingMode = 0
ProviderI2cSharingMode_Shared: ProviderI2cSharingMode = 1
class ProviderI2cTransferResult(EasyCastStructure):
    Status: win32more.Windows.Devices.I2c.Provider.ProviderI2cTransferStatus
    BytesTransferred: UInt32
ProviderI2cTransferStatus = Int32
ProviderI2cTransferStatus_FullTransfer: ProviderI2cTransferStatus = 0
ProviderI2cTransferStatus_PartialTransfer: ProviderI2cTransferStatus = 1
ProviderI2cTransferStatus_SlaveAddressNotAcknowledged: ProviderI2cTransferStatus = 2
make_head(_module, 'II2cControllerProvider')
make_head(_module, 'II2cDeviceProvider')
make_head(_module, 'II2cProvider')
make_head(_module, 'IProviderI2cConnectionSettings')
make_head(_module, 'ProviderI2cConnectionSettings')
make_head(_module, 'ProviderI2cTransferResult')
