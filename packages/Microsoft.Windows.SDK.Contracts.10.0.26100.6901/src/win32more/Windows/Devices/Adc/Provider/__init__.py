from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Devices.Adc.Provider
import win32more.Windows.Foundation.Collections
class IAdcControllerProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Adc.Provider.IAdcControllerProvider'
    _iid_ = Guid('{be545828-816d-4de5-a048-aba06958aaa8}')
    @winrt_commethod(6)
    def get_ChannelCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ResolutionInBits(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MinValue(self) -> Int32: ...
    @winrt_commethod(9)
    def get_MaxValue(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ChannelMode(self) -> win32more.Windows.Devices.Adc.Provider.ProviderAdcChannelMode: ...
    @winrt_commethod(11)
    def put_ChannelMode(self, value: win32more.Windows.Devices.Adc.Provider.ProviderAdcChannelMode) -> Void: ...
    @winrt_commethod(12)
    def IsChannelModeSupported(self, channelMode: win32more.Windows.Devices.Adc.Provider.ProviderAdcChannelMode) -> Boolean: ...
    @winrt_commethod(13)
    def AcquireChannel(self, channel: Int32) -> Void: ...
    @winrt_commethod(14)
    def ReleaseChannel(self, channel: Int32) -> Void: ...
    @winrt_commethod(15)
    def ReadValue(self, channelNumber: Int32) -> Int32: ...
    ChannelCount = property(get_ChannelCount, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
    MaxValue = property(get_MaxValue, None)
    MinValue = property(get_MinValue, None)
    ResolutionInBits = property(get_ResolutionInBits, None)
class IAdcProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Adc.Provider.IAdcProvider'
    _iid_ = Guid('{28953668-9359-4c57-bc88-e275e81638c9}')
    @winrt_commethod(6)
    def GetControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Adc.Provider.IAdcControllerProvider]: ...
class ProviderAdcChannelMode(Enum, Int32):
    SingleEnded = 0
    Differential = 1


make_ready(__name__)
