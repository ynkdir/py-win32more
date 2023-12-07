from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.I2c
import win32more.Windows.Devices.I2c.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
I2cBusSpeed = Int32
I2cBusSpeed_StandardMode: I2cBusSpeed = 0
I2cBusSpeed_FastMode: I2cBusSpeed = 1
class I2cConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.I2c.II2cConnectionSettings
    _classid_ = 'Windows.Devices.I2c.I2cConnectionSettings'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Devices.I2c.I2cConnectionSettings.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
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
    default_interface: win32more.Windows.Devices.I2c.II2cDevice
    _classid_ = 'Windows.Devices.I2c.I2cDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.I2c.II2cDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionSettings(self: win32more.Windows.Devices.I2c.II2cDevice) -> win32more.Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_mixinmethod
    def Write(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def WritePartial(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def Read(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def ReadPartial(self: win32more.Windows.Devices.I2c.II2cDevice, buffer: Annotated[SZArray[Byte], 'Out']) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def WriteRead(self: win32more.Windows.Devices.I2c.II2cDevice, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def WriteReadPartial(self: win32more.Windows.Devices.I2c.II2cDevice, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.I2c.II2cDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: win32more.Windows.Devices.I2c.II2cDeviceStatics, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.I2c.II2cDeviceStatics, deviceId: WinRT_String, settings: win32more.Windows.Devices.I2c.I2cConnectionSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.I2c.I2cDevice]: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
I2cSharingMode = Int32
I2cSharingMode_Exclusive: I2cSharingMode = 0
I2cSharingMode_Shared: I2cSharingMode = 1
class I2cTransferResult(EasyCastStructure):
    Status: win32more.Windows.Devices.I2c.I2cTransferStatus
    BytesTransferred: UInt32
I2cTransferStatus = Int32
I2cTransferStatus_FullTransfer: I2cTransferStatus = 0
I2cTransferStatus_PartialTransfer: I2cTransferStatus = 1
I2cTransferStatus_SlaveAddressNotAcknowledged: I2cTransferStatus = 2
I2cTransferStatus_ClockStretchTimeout: I2cTransferStatus = 3
I2cTransferStatus_UnknownError: I2cTransferStatus = 4
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
    SlaveAddress = property(get_SlaveAddress, put_SlaveAddress)
    BusSpeed = property(get_BusSpeed, put_BusSpeed)
    SharingMode = property(get_SharingMode, put_SharingMode)
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
    _classid_ = 'Windows.Devices.I2c.II2cDevice'
    _iid_ = Guid('{8636c136-b9c5-4f70-9449-cc46dc6f57eb}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> win32more.Windows.Devices.I2c.I2cConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(9)
    def WritePartial(self, buffer: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_commethod(10)
    def Read(self, buffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(11)
    def ReadPartial(self, buffer: Annotated[SZArray[Byte], 'Out']) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    @winrt_commethod(12)
    def WriteRead(self, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(13)
    def WriteReadPartial(self, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> win32more.Windows.Devices.I2c.I2cTransferResult: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
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
