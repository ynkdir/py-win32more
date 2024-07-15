from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Adc
import win32more.Windows.Devices.Adc.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class AdcChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Adc.IAdcChannel
    _classid_ = 'Windows.Devices.Adc.AdcChannel'
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.Devices.Adc.IAdcChannel) -> win32more.Windows.Devices.Adc.AdcController: ...
    @winrt_mixinmethod
    def ReadValue(self: win32more.Windows.Devices.Adc.IAdcChannel) -> Int32: ...
    @winrt_mixinmethod
    def ReadRatio(self: win32more.Windows.Devices.Adc.IAdcChannel) -> Double: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Controller = property(get_Controller, None)
class AdcChannelMode(Enum, Int32):
    SingleEnded = 0
    Differential = 1
class AdcController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Adc.IAdcController
    _classid_ = 'Windows.Devices.Adc.AdcController'
    @winrt_mixinmethod
    def get_ChannelCount(self: win32more.Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_ResolutionInBits(self: win32more.Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_MinValue(self: win32more.Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxValue(self: win32more.Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_ChannelMode(self: win32more.Windows.Devices.Adc.IAdcController) -> win32more.Windows.Devices.Adc.AdcChannelMode: ...
    @winrt_mixinmethod
    def put_ChannelMode(self: win32more.Windows.Devices.Adc.IAdcController, value: win32more.Windows.Devices.Adc.AdcChannelMode) -> Void: ...
    @winrt_mixinmethod
    def IsChannelModeSupported(self: win32more.Windows.Devices.Adc.IAdcController, channelMode: win32more.Windows.Devices.Adc.AdcChannelMode) -> Boolean: ...
    @winrt_mixinmethod
    def OpenChannel(self: win32more.Windows.Devices.Adc.IAdcController, channelNumber: Int32) -> win32more.Windows.Devices.Adc.AdcChannel: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Adc.IAdcControllerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Adc.AdcController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: win32more.Windows.Devices.Adc.IAdcControllerStatics, provider: win32more.Windows.Devices.Adc.Provider.IAdcProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Adc.AdcController]]: ...
    ChannelCount = property(get_ChannelCount, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
    MaxValue = property(get_MaxValue, None)
    MinValue = property(get_MinValue, None)
    ResolutionInBits = property(get_ResolutionInBits, None)
class IAdcChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Adc.IAdcChannel'
    _iid_ = Guid('{040bf414-2588-4a56-abef-73a260acc60a}')
    @winrt_commethod(6)
    def get_Controller(self) -> win32more.Windows.Devices.Adc.AdcController: ...
    @winrt_commethod(7)
    def ReadValue(self) -> Int32: ...
    @winrt_commethod(8)
    def ReadRatio(self) -> Double: ...
    Controller = property(get_Controller, None)
class IAdcController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Adc.IAdcController'
    _iid_ = Guid('{2a76e4b0-a896-4219-86b6-ea8cdce98f56}')
    @winrt_commethod(6)
    def get_ChannelCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ResolutionInBits(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MinValue(self) -> Int32: ...
    @winrt_commethod(9)
    def get_MaxValue(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ChannelMode(self) -> win32more.Windows.Devices.Adc.AdcChannelMode: ...
    @winrt_commethod(11)
    def put_ChannelMode(self, value: win32more.Windows.Devices.Adc.AdcChannelMode) -> Void: ...
    @winrt_commethod(12)
    def IsChannelModeSupported(self, channelMode: win32more.Windows.Devices.Adc.AdcChannelMode) -> Boolean: ...
    @winrt_commethod(13)
    def OpenChannel(self, channelNumber: Int32) -> win32more.Windows.Devices.Adc.AdcChannel: ...
    ChannelCount = property(get_ChannelCount, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
    MaxValue = property(get_MaxValue, None)
    MinValue = property(get_MinValue, None)
    ResolutionInBits = property(get_ResolutionInBits, None)
class IAdcControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Adc.IAdcControllerStatics'
    _iid_ = Guid('{cce98e0c-01f8-4891-bc3b-be53ef279ca4}')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: win32more.Windows.Devices.Adc.Provider.IAdcProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Adc.AdcController]]: ...
class IAdcControllerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Adc.IAdcControllerStatics2'
    _iid_ = Guid('{a2b93b1d-977b-4f5a-a5fe-a6abaffe6484}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Adc.AdcController]: ...


make_ready(__name__)
