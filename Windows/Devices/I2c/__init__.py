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
import Windows.Devices.I2c
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
I2cBusSpeed = Int32
I2cBusSpeed_StandardMode: I2cBusSpeed = 0
I2cBusSpeed_FastMode: I2cBusSpeed = 1
class I2cConnectionSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.I2c.II2cConnectionSettings
    _classid_ = 'Windows.Devices.I2c.I2cConnectionSettings'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.I2c.II2cConnectionSettingsFactory, slaveAddress: Int32) -> Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_mixinmethod
    def get_SlaveAddress(self: Windows.Devices.I2c.II2cConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_SlaveAddress(self: Windows.Devices.I2c.II2cConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BusSpeed(self: Windows.Devices.I2c.II2cConnectionSettings) -> Windows.Devices.I2c.I2cBusSpeed: ...
    @winrt_mixinmethod
    def put_BusSpeed(self: Windows.Devices.I2c.II2cConnectionSettings, value: Windows.Devices.I2c.I2cBusSpeed) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Devices.I2c.II2cConnectionSettings) -> Windows.Devices.I2c.I2cSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: Windows.Devices.I2c.II2cConnectionSettings, value: Windows.Devices.I2c.I2cSharingMode) -> Void: ...
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
class I2cController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.I2c.II2cController
    _classid_ = 'Windows.Devices.I2c.I2cController'
    @winrt_mixinmethod
    def GetDevice(self: Windows.Devices.I2c.II2cController, settings: Windows.Devices.I2c.I2cConnectionSettings) -> Windows.Devices.I2c.I2cDevice: ...
    @winrt_classmethod
    def GetControllersAsync(cls: Windows.Devices.I2c.II2cControllerStatics, provider: Windows.Devices.I2c.Provider.II2cProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.I2c.I2cController]]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.I2c.II2cControllerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.I2c.I2cController]: ...
class I2cDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.I2c.II2cDevice
    _classid_ = 'Windows.Devices.I2c.I2cDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.I2c.II2cDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionSettings(self: Windows.Devices.I2c.II2cDevice) -> Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_mixinmethod
    def Write(self: Windows.Devices.I2c.II2cDevice, buffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def WritePartial(self: Windows.Devices.I2c.II2cDevice, buffer: c_char_p_no) -> Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def Read(self: Windows.Devices.I2c.II2cDevice, buffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def ReadPartial(self: Windows.Devices.I2c.II2cDevice, buffer: c_char_p_no) -> Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def WriteRead(self: Windows.Devices.I2c.II2cDevice, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def WriteReadPartial(self: Windows.Devices.I2c.II2cDevice, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.I2c.II2cDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: Windows.Devices.I2c.II2cDeviceStatics, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.I2c.II2cDeviceStatics, deviceId: WinRT_String, settings: Windows.Devices.I2c.I2cConnectionSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.I2c.I2cDevice]: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
I2cSharingMode = Int32
I2cSharingMode_Exclusive: I2cSharingMode = 0
I2cSharingMode_Shared: I2cSharingMode = 1
class I2cTransferResult(EasyCastStructure):
    Status: Windows.Devices.I2c.I2cTransferStatus
    BytesTransferred: UInt32
I2cTransferStatus = Int32
I2cTransferStatus_FullTransfer: I2cTransferStatus = 0
I2cTransferStatus_PartialTransfer: I2cTransferStatus = 1
I2cTransferStatus_SlaveAddressNotAcknowledged: I2cTransferStatus = 2
I2cTransferStatus_ClockStretchTimeout: I2cTransferStatus = 3
I2cTransferStatus_UnknownError: I2cTransferStatus = 4
class II2cConnectionSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f2db1307-ab6f-4639-a767-54536dc3460f}')
    @winrt_commethod(6)
    def get_SlaveAddress(self) -> Int32: ...
    @winrt_commethod(7)
    def put_SlaveAddress(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_BusSpeed(self) -> Windows.Devices.I2c.I2cBusSpeed: ...
    @winrt_commethod(9)
    def put_BusSpeed(self, value: Windows.Devices.I2c.I2cBusSpeed) -> Void: ...
    @winrt_commethod(10)
    def get_SharingMode(self) -> Windows.Devices.I2c.I2cSharingMode: ...
    @winrt_commethod(11)
    def put_SharingMode(self, value: Windows.Devices.I2c.I2cSharingMode) -> Void: ...
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
class II2cConnectionSettingsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{81b586b3-9693-41b1-a243-ded4f6e66926}')
    @winrt_commethod(6)
    def Create(self, slaveAddress: Int32) -> Windows.Devices.I2c.I2cConnectionSettings: ...
class II2cController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c48ab1b2-87a0-4166-8e3e-b4b8f97cd729}')
    @winrt_commethod(6)
    def GetDevice(self, settings: Windows.Devices.I2c.I2cConnectionSettings) -> Windows.Devices.I2c.I2cDevice: ...
class II2cControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{40fc0365-5f05-4e7e-84bd-100db8e0aec5}')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: Windows.Devices.I2c.Provider.II2cProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.I2c.I2cController]]: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.I2c.I2cController]: ...
class II2cDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8636c136-b9c5-4f70-9449-cc46dc6f57eb}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(9)
    def WritePartial(self, buffer: c_char_p_no) -> Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_commethod(10)
    def Read(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(11)
    def ReadPartial(self, buffer: c_char_p_no) -> Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_commethod(12)
    def WriteRead(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(13)
    def WriteReadPartial(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Windows.Devices.I2c.I2cTransferResult: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
class II2cDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{91a33be3-7334-4512-96bc-fbae9459f5f6}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String, settings: Windows.Devices.I2c.I2cConnectionSettings) -> Windows.Foundation.IAsyncOperation[Windows.Devices.I2c.I2cDevice]: ...
make_head(_module, 'I2cConnectionSettings')
make_head(_module, 'I2cController')
make_head(_module, 'I2cDevice')
make_head(_module, 'I2cTransferResult')
make_head(_module, 'II2cConnectionSettings')
make_head(_module, 'II2cConnectionSettingsFactory')
make_head(_module, 'II2cController')
make_head(_module, 'II2cControllerStatics')
make_head(_module, 'II2cDevice')
make_head(_module, 'II2cDeviceStatics')
