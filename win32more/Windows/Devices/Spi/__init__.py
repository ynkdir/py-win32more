from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Spi
import win32more.Windows.Devices.Spi.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class ISpiBusInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.ISpiBusInfo'
    _iid_ = Guid('{9929444a-54f2-48c6-b952-9c32fc02c669}')
    @winrt_commethod(6)
    def get_ChipSelectLineCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_MinClockFrequency(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MaxClockFrequency(self) -> Int32: ...
    @winrt_commethod(9)
    def get_SupportedDataBitLengths(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int32]: ...
    ChipSelectLineCount = property(get_ChipSelectLineCount, None)
    MaxClockFrequency = property(get_MaxClockFrequency, None)
    MinClockFrequency = property(get_MinClockFrequency, None)
    SupportedDataBitLengths = property(get_SupportedDataBitLengths, None)
class ISpiConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.ISpiConnectionSettings'
    _iid_ = Guid('{5283a37f-f935-4b9f-a7a7-3a7890afa5ce}')
    @winrt_commethod(6)
    def get_ChipSelectLine(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ChipSelectLine(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.Devices.Spi.SpiMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Windows.Devices.Spi.SpiMode) -> Void: ...
    @winrt_commethod(10)
    def get_DataBitLength(self) -> Int32: ...
    @winrt_commethod(11)
    def put_DataBitLength(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_ClockFrequency(self) -> Int32: ...
    @winrt_commethod(13)
    def put_ClockFrequency(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_SharingMode(self) -> win32more.Windows.Devices.Spi.SpiSharingMode: ...
    @winrt_commethod(15)
    def put_SharingMode(self, value: win32more.Windows.Devices.Spi.SpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    Mode = property(get_Mode, put_Mode)
    SharingMode = property(get_SharingMode, put_SharingMode)
class ISpiConnectionSettingsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.ISpiConnectionSettingsFactory'
    _iid_ = Guid('{ff99081e-10c4-44b7-9fea-a748b5a46f31}')
    @winrt_commethod(6)
    def Create(self, chipSelectLine: Int32) -> win32more.Windows.Devices.Spi.SpiConnectionSettings: ...
class ISpiController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.ISpiController'
    _iid_ = Guid('{a8d3c829-9895-4159-a934-8741f1ee6d27}')
    @winrt_commethod(6)
    def GetDevice(self, settings: win32more.Windows.Devices.Spi.SpiConnectionSettings) -> win32more.Windows.Devices.Spi.SpiDevice: ...
class ISpiControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.ISpiControllerStatics'
    _iid_ = Guid('{0d5229e2-138b-4e48-b964-4f2f79b9c5a2}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Spi.SpiController]: ...
    @winrt_commethod(7)
    def GetControllersAsync(self, provider: win32more.Windows.Devices.Spi.Provider.ISpiProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Spi.SpiController]]: ...
class ISpiDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Spi.ISpiDevice'
    _iid_ = Guid('{05d5356d-11b6-4d39-84d5-95dfb4c9f2ce}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ConnectionSettings(self) -> win32more.Windows.Devices.Spi.SpiConnectionSettings: ...
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
class ISpiDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Spi.ISpiDeviceStatics'
    _iid_ = Guid('{a278e559-5720-4d3f-bd93-56f5ff5a5879}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetBusInfo(self, busId: WinRT_String) -> win32more.Windows.Devices.Spi.SpiBusInfo: ...
    @winrt_commethod(9)
    def FromIdAsync(self, busId: WinRT_String, settings: win32more.Windows.Devices.Spi.SpiConnectionSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Spi.SpiDevice]: ...
class SpiBusInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Spi.ISpiBusInfo
    _classid_ = 'Windows.Devices.Spi.SpiBusInfo'
    @winrt_mixinmethod
    def get_ChipSelectLineCount(self: win32more.Windows.Devices.Spi.ISpiBusInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_MinClockFrequency(self: win32more.Windows.Devices.Spi.ISpiBusInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxClockFrequency(self: win32more.Windows.Devices.Spi.ISpiBusInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_SupportedDataBitLengths(self: win32more.Windows.Devices.Spi.ISpiBusInfo) -> win32more.Windows.Foundation.Collections.IVectorView[Int32]: ...
    ChipSelectLineCount = property(get_ChipSelectLineCount, None)
    MaxClockFrequency = property(get_MaxClockFrequency, None)
    MinClockFrequency = property(get_MinClockFrequency, None)
    SupportedDataBitLengths = property(get_SupportedDataBitLengths, None)
class SpiConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Spi.ISpiConnectionSettings
    _classid_ = 'Windows.Devices.Spi.SpiConnectionSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Spi.SpiConnectionSettings.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Spi.ISpiConnectionSettingsFactory, chipSelectLine: Int32) -> win32more.Windows.Devices.Spi.SpiConnectionSettings: ...
    @winrt_mixinmethod
    def get_ChipSelectLine(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ChipSelectLine(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings) -> win32more.Windows.Devices.Spi.SpiMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings, value: win32more.Windows.Devices.Spi.SpiMode) -> Void: ...
    @winrt_mixinmethod
    def get_DataBitLength(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_DataBitLength(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ClockFrequency(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings) -> Int32: ...
    @winrt_mixinmethod
    def put_ClockFrequency(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings) -> win32more.Windows.Devices.Spi.SpiSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: win32more.Windows.Devices.Spi.ISpiConnectionSettings, value: win32more.Windows.Devices.Spi.SpiSharingMode) -> Void: ...
    ChipSelectLine = property(get_ChipSelectLine, put_ChipSelectLine)
    ClockFrequency = property(get_ClockFrequency, put_ClockFrequency)
    DataBitLength = property(get_DataBitLength, put_DataBitLength)
    Mode = property(get_Mode, put_Mode)
    SharingMode = property(get_SharingMode, put_SharingMode)
class SpiController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Spi.ISpiController
    _classid_ = 'Windows.Devices.Spi.SpiController'
    @winrt_mixinmethod
    def GetDevice(self: win32more.Windows.Devices.Spi.ISpiController, settings: win32more.Windows.Devices.Spi.SpiConnectionSettings) -> win32more.Windows.Devices.Spi.SpiDevice: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Spi.ISpiControllerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Spi.SpiController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: win32more.Windows.Devices.Spi.ISpiControllerStatics, provider: win32more.Windows.Devices.Spi.Provider.ISpiProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Spi.SpiController]]: ...
class SpiDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Spi.ISpiDevice
    _classid_ = 'Windows.Devices.Spi.SpiDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Spi.ISpiDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionSettings(self: win32more.Windows.Devices.Spi.ISpiDevice) -> win32more.Windows.Devices.Spi.SpiConnectionSettings: ...
    @winrt_mixinmethod
    def Write(self: win32more.Windows.Devices.Spi.ISpiDevice, buffer: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def Read(self: win32more.Windows.Devices.Spi.ISpiDevice, buffer: FillArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def TransferSequential(self: win32more.Windows.Devices.Spi.ISpiDevice, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def TransferFullDuplex(self: win32more.Windows.Devices.Spi.ISpiDevice, writeBuffer: PassArray[Byte], readBuffer: FillArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Spi.ISpiDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: win32more.Windows.Devices.Spi.ISpiDeviceStatics, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetBusInfo(cls: win32more.Windows.Devices.Spi.ISpiDeviceStatics, busId: WinRT_String) -> win32more.Windows.Devices.Spi.SpiBusInfo: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Spi.ISpiDeviceStatics, busId: WinRT_String, settings: win32more.Windows.Devices.Spi.SpiConnectionSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Spi.SpiDevice]: ...
    ConnectionSettings = property(get_ConnectionSettings, None)
    DeviceId = property(get_DeviceId, None)
class SpiMode(Enum, Int32):
    Mode0 = 0
    Mode1 = 1
    Mode2 = 2
    Mode3 = 3
class SpiSharingMode(Enum, Int32):
    Exclusive = 0
    Shared = 1


make_ready(__name__)
