from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Adc.Provider
import win32more.Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    ResolutionInBits = property(get_ResolutionInBits, None)
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
class IAdcProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Adc.Provider.IAdcProvider'
    _iid_ = Guid('{28953668-9359-4c57-bc88-e275e81638c9}')
    @winrt_commethod(6)
    def GetControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Adc.Provider.IAdcControllerProvider]: ...
ProviderAdcChannelMode = Int32
ProviderAdcChannelMode_SingleEnded: ProviderAdcChannelMode = 0
ProviderAdcChannelMode_Differential: ProviderAdcChannelMode = 1
make_head(_module, 'IAdcControllerProvider')
make_head(_module, 'IAdcProvider')
