from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Adc.Provider
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IAdcControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Adc.Provider.IAdcProvider'
    _iid_ = Guid('{28953668-9359-4c57-bc88-e275e81638c9}')
    @winrt_commethod(6)
    def GetControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Adc.Provider.IAdcControllerProvider]: ...
class ProviderAdcChannelMode(Enum, Int32):
    SingleEnded = 0
    Differential = 1


make_ready(__name__)
