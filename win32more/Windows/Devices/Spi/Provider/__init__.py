from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Spi.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
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
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    Mode = property(get_Mode, put_Mode)
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
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Spi.Provider.ISpiDeviceProvider'
    _iid_ = Guid('{0d1c3443-304b-405c-b4f7-f5ab1074461e}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings: ...
    @winrt_commethod(8)
    def Write(self, buffer: PassArray[Byte]) -> Void: ...
    @winrt_commethod(9)
    def Read(self, buffer: FillArray[Byte]) -> Void: ...
    @winrt_commethod(10)
    def TransferSequential(self, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    @winrt_commethod(11)
    def TransferFullDuplex(self, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    ConnectionSettings = property(get_ConnectionSettings, None)
    DeviceId = property(get_DeviceId, None)
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Spi.Provider.ProviderSpiConnectionSettings.Create(*args))
        else:
            raise ValueError('no matched constructor')
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
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    Mode = property(get_Mode, put_Mode)
    SharingMode = property(get_SharingMode, put_SharingMode)
class ProviderSpiMode(Enum, Int32):
    Mode0 = 0
    Mode1 = 1
    Mode2 = 2
    Mode3 = 3
class ProviderSpiSharingMode(Enum, Int32):
    Exclusive = 0
    Shared = 1


make_ready(__name__)
