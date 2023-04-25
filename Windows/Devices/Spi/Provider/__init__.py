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
import Windows.Devices.Spi.Provider
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
class IProviderSpiConnectionSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f6034550-a542-4ec0-96-01-a4-dd-68-f8-69-7b')
    @winrt_commethod(6)
    def get_ChipSelectLine(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ChipSelectLine(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.Devices.Spi.Provider.ProviderSpiMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: Windows.Devices.Spi.Provider.ProviderSpiMode) -> Void: ...
    @winrt_commethod(10)
    def get_DataBitLength(self) -> Int32: ...
    @winrt_commethod(11)
    def put_DataBitLength(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_ClockFrequency(self) -> Int32: ...
    @winrt_commethod(13)
    def put_ClockFrequency(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_SharingMode(self) -> Windows.Devices.Spi.Provider.ProviderSpiSharingMode: ...
    @winrt_commethod(15)
    def put_SharingMode(self, value: Windows.Devices.Spi.Provider.ProviderSpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    Mode = property(get_Mode, put_Mode)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    SharingMode = property(get_SharingMode, put_SharingMode)
class IProviderSpiConnectionSettingsFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('66456b5a-0c79-43e3-9f-3c-e5-97-80-ac-18-fa')
    @winrt_commethod(6)
    def Create(self, chipSelectLine: Int32) -> Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
class ISpiControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c1686504-02ce-4226-a3-85-4f-11-fb-04-b4-1b')
    @winrt_commethod(6)
    def GetDeviceProvider(self, settings: Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings) -> Windows.Devices.Spi.Provider.ISpiDeviceProvider: ...
class ISpiDeviceProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0d1c3443-304b-405c-b4-f7-f5-ab-10-74-46-1e')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(9)
    def Read(self, buffer: c_char_p_no) -> Void: ...
    @winrt_commethod(10)
    def TransferSequential(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(11)
    def TransferFullDuplex(self, writeBuffer: c_char_p_no, readBuffer: c_char_p_no) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
class ISpiProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96b461e2-77d4-48ce-aa-a0-75-71-5a-83-62-cf')
    @winrt_commethod(6)
    def GetControllersAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Spi.Provider.ISpiControllerProvider]]: ...
class ProviderSpiConnectionSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettingsFactory, chipSelectLine: Int32) -> Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
    @winrt_mixinmethod
    def get_ChipSelectLine(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ChipSelectLine(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Windows.Devices.Spi.Provider.ProviderSpiMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Windows.Devices.Spi.Provider.ProviderSpiMode) -> Void: ...
    @winrt_mixinmethod
    def get_DataBitLength(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_DataBitLength(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ClockFrequency(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ClockFrequency(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Windows.Devices.Spi.Provider.ProviderSpiSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Windows.Devices.Spi.Provider.ProviderSpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    Mode = property(get_Mode, put_Mode)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    SharingMode = property(get_SharingMode, put_SharingMode)
ProviderSpiMode = Int32
ProviderSpiMode_Mode0: ProviderSpiMode = 0
ProviderSpiMode_Mode1: ProviderSpiMode = 1
ProviderSpiMode_Mode2: ProviderSpiMode = 2
ProviderSpiMode_Mode3: ProviderSpiMode = 3
ProviderSpiSharingMode = Int32
ProviderSpiSharingMode_Exclusive: ProviderSpiSharingMode = 0
ProviderSpiSharingMode_Shared: ProviderSpiSharingMode = 1
make_head(_module, 'IProviderSpiConnectionSettings')
make_head(_module, 'IProviderSpiConnectionSettingsFactory')
make_head(_module, 'ISpiControllerProvider')
make_head(_module, 'ISpiDeviceProvider')
make_head(_module, 'ISpiProvider')
make_head(_module, 'ProviderSpiConnectionSettings')
