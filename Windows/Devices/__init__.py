from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Devices
import Windows.Devices.Adc.Provider
import Windows.Devices.Gpio.Provider
import Windows.Devices.I2c.Provider
import Windows.Devices.Pwm.Provider
import Windows.Devices.Spi.Provider
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DevicesLowLevelContract: UInt32 = 196608
class ILowLevelDevicesAggregateProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.ILowLevelDevicesAggregateProvider'
    _iid_ = Guid('{a73e561c-aac1-4ec7-a852-479f7060d01f}')
    @winrt_commethod(6)
    def get_AdcControllerProvider(self) -> Windows.Devices.Adc.Provider.IAdcControllerProvider: ...
    @winrt_commethod(7)
    def get_PwmControllerProvider(self) -> Windows.Devices.Pwm.Provider.IPwmControllerProvider: ...
    @winrt_commethod(8)
    def get_GpioControllerProvider(self) -> Windows.Devices.Gpio.Provider.IGpioControllerProvider: ...
    @winrt_commethod(9)
    def get_I2cControllerProvider(self) -> Windows.Devices.I2c.Provider.II2cControllerProvider: ...
    @winrt_commethod(10)
    def get_SpiControllerProvider(self) -> Windows.Devices.Spi.Provider.ISpiControllerProvider: ...
    AdcControllerProvider = property(get_AdcControllerProvider, None)
    PwmControllerProvider = property(get_PwmControllerProvider, None)
    GpioControllerProvider = property(get_GpioControllerProvider, None)
    I2cControllerProvider = property(get_I2cControllerProvider, None)
    SpiControllerProvider = property(get_SpiControllerProvider, None)
class ILowLevelDevicesAggregateProviderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.ILowLevelDevicesAggregateProviderFactory'
    _iid_ = Guid('{9ac4aaf6-3473-465e-96d5-36281a2c57af}')
    @winrt_commethod(6)
    def Create(self, adc: Windows.Devices.Adc.Provider.IAdcControllerProvider, pwm: Windows.Devices.Pwm.Provider.IPwmControllerProvider, gpio: Windows.Devices.Gpio.Provider.IGpioControllerProvider, i2c: Windows.Devices.I2c.Provider.II2cControllerProvider, spi: Windows.Devices.Spi.Provider.ISpiControllerProvider) -> Windows.Devices.LowLevelDevicesAggregateProvider: ...
class ILowLevelDevicesController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.ILowLevelDevicesController'
    _iid_ = Guid('{2ec23dd4-179b-45de-9b39-3ae02527de52}')
class ILowLevelDevicesControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.ILowLevelDevicesControllerStatics'
    _iid_ = Guid('{093e926a-fccb-4394-a697-19de637c2db3}')
    @winrt_commethod(6)
    def get_DefaultProvider(self) -> Windows.Devices.ILowLevelDevicesAggregateProvider: ...
    @winrt_commethod(7)
    def put_DefaultProvider(self, value: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Void: ...
    DefaultProvider = property(get_DefaultProvider, put_DefaultProvider)
class LowLevelDevicesAggregateProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.ILowLevelDevicesAggregateProvider
    _classid_ = 'Windows.Devices.LowLevelDevicesAggregateProvider'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.ILowLevelDevicesAggregateProviderFactory, adc: Windows.Devices.Adc.Provider.IAdcControllerProvider, pwm: Windows.Devices.Pwm.Provider.IPwmControllerProvider, gpio: Windows.Devices.Gpio.Provider.IGpioControllerProvider, i2c: Windows.Devices.I2c.Provider.II2cControllerProvider, spi: Windows.Devices.Spi.Provider.ISpiControllerProvider) -> Windows.Devices.LowLevelDevicesAggregateProvider: ...
    @winrt_mixinmethod
    def get_AdcControllerProvider(self: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Windows.Devices.Adc.Provider.IAdcControllerProvider: ...
    @winrt_mixinmethod
    def get_PwmControllerProvider(self: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Windows.Devices.Pwm.Provider.IPwmControllerProvider: ...
    @winrt_mixinmethod
    def get_GpioControllerProvider(self: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Windows.Devices.Gpio.Provider.IGpioControllerProvider: ...
    @winrt_mixinmethod
    def get_I2cControllerProvider(self: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Windows.Devices.I2c.Provider.II2cControllerProvider: ...
    @winrt_mixinmethod
    def get_SpiControllerProvider(self: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Windows.Devices.Spi.Provider.ISpiControllerProvider: ...
    AdcControllerProvider = property(get_AdcControllerProvider, None)
    PwmControllerProvider = property(get_PwmControllerProvider, None)
    GpioControllerProvider = property(get_GpioControllerProvider, None)
    I2cControllerProvider = property(get_I2cControllerProvider, None)
    SpiControllerProvider = property(get_SpiControllerProvider, None)
class _LowLevelDevicesController_Meta_(ComPtr.__class__):
    pass
class LowLevelDevicesController(ComPtr, metaclass=_LowLevelDevicesController_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.ILowLevelDevicesController
    _classid_ = 'Windows.Devices.LowLevelDevicesController'
    @winrt_classmethod
    def get_DefaultProvider(cls: Windows.Devices.ILowLevelDevicesControllerStatics) -> Windows.Devices.ILowLevelDevicesAggregateProvider: ...
    @winrt_classmethod
    def put_DefaultProvider(cls: Windows.Devices.ILowLevelDevicesControllerStatics, value: Windows.Devices.ILowLevelDevicesAggregateProvider) -> Void: ...
    _LowLevelDevicesController_Meta_.DefaultProvider = property(get_DefaultProvider.__wrapped__, put_DefaultProvider.__wrapped__)
make_head(_module, 'ILowLevelDevicesAggregateProvider')
make_head(_module, 'ILowLevelDevicesAggregateProviderFactory')
make_head(_module, 'ILowLevelDevicesController')
make_head(_module, 'ILowLevelDevicesControllerStatics')
make_head(_module, 'LowLevelDevicesAggregateProvider')
make_head(_module, 'LowLevelDevicesController')
