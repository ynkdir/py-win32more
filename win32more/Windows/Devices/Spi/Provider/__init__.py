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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Spi.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class IProviderSpiConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings'
    _iid_ = Guid('{f6034550-a542-4ec0-9601-a4dd68f8697b}')
    @winrt_commethod(6)
    def get_ChipSelectLine(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ChipSelectLine(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Windows.Devices.Spi.Provider.ProviderSpiMode) -> Void: ...
    @winrt_commethod(10)
    def get_DataBitLength(self) -> Int32: ...
    @winrt_commethod(11)
    def put_DataBitLength(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_ClockFrequency(self) -> Int32: ...
    @winrt_commethod(13)
    def put_ClockFrequency(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_SharingMode(self) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiSharingMode: ...
    @winrt_commethod(15)
    def put_SharingMode(self, value: win32more.Windows.Devices.Spi.Provider.ProviderSpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    Mode = property(get_Mode, put_Mode)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    SharingMode = property(get_SharingMode, put_SharingMode)
class IProviderSpiConnectionSettingsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.Provider.IProviderSpiConnectionSettingsFactory'
    _iid_ = Guid('{66456b5a-0c79-43e3-9f3c-e59780ac18fa}')
    @winrt_commethod(6)
    def Create(self, chipSelectLine: Int32) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
class ISpiControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.Provider.ISpiControllerProvider'
    _iid_ = Guid('{c1686504-02ce-4226-a385-4f11fb04b41b}')
    @winrt_commethod(6)
    def GetDeviceProvider(self, settings: win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings) -> win32more.Windows.Devices.Spi.Provider.ISpiDeviceProvider: ...
class ISpiDeviceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.Provider.ISpiDeviceProvider'
    _iid_ = Guid('{0d1c3443-304b-405c-b4f7-f5ab1074461e}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(9)
    def Read(self, buffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(10)
    def TransferSequential(self, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(11)
    def TransferFullDuplex(self, writeBuffer: Annotated[SZArray[Byte], 'In'], readBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    ConnectionSettings = property(get_ConnectionSettings, None)
class ISpiProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.Provider.ISpiProvider'
    _iid_ = Guid('{96b461e2-77d4-48ce-aaa0-75715a8362cf}')
    @winrt_commethod(6)
    def GetControllersAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Spi.Provider.ISpiControllerProvider]]: ...
class ProviderSpiConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings
    _classid_ = 'Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettingsFactory, chipSelectLine: Int32) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
    @winrt_mixinmethod
    def get_ChipSelectLine(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ChipSelectLine(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: win32more.Windows.Devices.Spi.Provider.ProviderSpiMode) -> Void: ...
    @winrt_mixinmethod
    def get_DataBitLength(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_DataBitLength(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ClockFrequency(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ClockFrequency(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: win32more.Windows.Devices.Spi.Provider.IProviderSpiConnectionSettings, value: win32more.Windows.Devices.Spi.Provider.ProviderSpiSharingMode) -> Void: ...
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
make_ready(__name__)
