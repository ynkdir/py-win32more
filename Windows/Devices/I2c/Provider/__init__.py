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
import Windows.Devices.I2c.Provider
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class II2cControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('61c2bb82-4510-4163-a8-7c-4e-15-a9-55-89-80')
    @winrt_commethod(6)
    def GetDeviceProvider(self, settings: Windows.Devices.I2c.Provider.ProviderI2cConnectionSettings) -> Windows.Devices.I2c.Provider.II2cDeviceProvider: ...
class II2cDeviceProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ad342654-57e8-453e-83-29-d1-e4-47-d1-03-a9')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Write(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(8)
    def WritePartial(self, buffer: c_char_p_no) -> Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    @winrt_commethod(9)
    def Read(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(10)
    def ReadPartial(self, buffer: c_char_p_no) -> Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    @winrt_commethod(11)
    def WriteRead(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(12)
    def WriteReadPartial(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Windows.Devices.I2c.Provider.ProviderI2cTransferResult: ...
    DeviceId = property(get_DeviceId, None)
class II2cProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f13083e-bf62-4fe2-a9-5a-f0-89-99-66-98-18')
    @winrt_commethod(6)
    def GetControllersAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.I2c.Provider.II2cControllerProvider]]: ...
class IProviderI2cConnectionSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e9db4e34-e510-44b7-80-9d-f2-f8-5b-55-53-39')
    @winrt_commethod(6)
    def get_SlaveAddress(self) -> Int32: ...
    @winrt_commethod(7)
    def put_SlaveAddress(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_BusSpeed(self) -> Windows.Devices.I2c.Provider.ProviderI2cBusSpeed: ...
    @winrt_commethod(9)
    def put_BusSpeed(self, value: Windows.Devices.I2c.Provider.ProviderI2cBusSpeed) -> Void: ...
    @winrt_commethod(10)
    def get_SharingMode(self) -> Windows.Devices.I2c.Provider.ProviderI2cSharingMode: ...
    @winrt_commethod(11)
    def put_SharingMode(self, value: Windows.Devices.I2c.Provider.ProviderI2cSharingMode) -> Void: ...
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
ProviderI2cBusSpeed = Int32
ProviderI2cBusSpeed_StandardMode: ProviderI2cBusSpeed = 0
ProviderI2cBusSpeed_FastMode: ProviderI2cBusSpeed = 1
class ProviderI2cConnectionSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.I2c.Provider.ProviderI2cConnectionSettings'
    @winrt_mixinmethod
    def get_SlaveAddress(self: Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_SlaveAddress(self: Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BusSpeed(self: Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings) -> Windows.Devices.I2c.Provider.ProviderI2cBusSpeed: ...
    @winrt_mixinmethod
    def put_BusSpeed(self: Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings, value: Windows.Devices.I2c.Provider.ProviderI2cBusSpeed) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings) -> Windows.Devices.I2c.Provider.ProviderI2cSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: Windows.Devices.I2c.Provider.IProviderI2cConnectionSettings, value: Windows.Devices.I2c.Provider.ProviderI2cSharingMode) -> Void: ...
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
ProviderI2cSharingMode = Int32
ProviderI2cSharingMode_Exclusive: ProviderI2cSharingMode = 0
ProviderI2cSharingMode_Shared: ProviderI2cSharingMode = 1
class ProviderI2cTransferResult(EasyCastStructure):
    Status: Windows.Devices.I2c.Provider.ProviderI2cTransferStatus
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
