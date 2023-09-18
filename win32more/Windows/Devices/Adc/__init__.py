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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Adc
import win32more.Windows.Devices.Adc.Provider
import win32more.Windows.Foundation
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
class AdcChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
AdcChannelMode = Int32
AdcChannelMode_SingleEnded: AdcChannelMode = 0
AdcChannelMode_Differential: AdcChannelMode = 1
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
    ResolutionInBits = property(get_ResolutionInBits, None)
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
class IAdcChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    ResolutionInBits = property(get_ResolutionInBits, None)
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
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
make_head(_module, 'AdcChannel')
make_head(_module, 'AdcController')
make_head(_module, 'IAdcChannel')
make_head(_module, 'IAdcController')
make_head(_module, 'IAdcControllerStatics')
make_head(_module, 'IAdcControllerStatics2')
