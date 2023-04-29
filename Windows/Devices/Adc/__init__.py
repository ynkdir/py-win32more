from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Adc
import Windows.Devices.Adc.Provider
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
class AdcChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Adc.AdcChannel'
    @winrt_mixinmethod
    def get_Controller(self: Windows.Devices.Adc.IAdcChannel) -> Windows.Devices.Adc.AdcController: ...
    @winrt_mixinmethod
    def ReadValue(self: Windows.Devices.Adc.IAdcChannel) -> Int32: ...
    @winrt_mixinmethod
    def ReadRatio(self: Windows.Devices.Adc.IAdcChannel) -> Double: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Controller = property(get_Controller, None)
AdcChannelMode = Int32
AdcChannelMode_SingleEnded: AdcChannelMode = 0
AdcChannelMode_Differential: AdcChannelMode = 1
class AdcController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Adc.AdcController'
    @winrt_mixinmethod
    def get_ChannelCount(self: Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_ResolutionInBits(self: Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_MinValue(self: Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxValue(self: Windows.Devices.Adc.IAdcController) -> Int32: ...
    @winrt_mixinmethod
    def get_ChannelMode(self: Windows.Devices.Adc.IAdcController) -> Windows.Devices.Adc.AdcChannelMode: ...
    @winrt_mixinmethod
    def put_ChannelMode(self: Windows.Devices.Adc.IAdcController, value: Windows.Devices.Adc.AdcChannelMode) -> Void: ...
    @winrt_mixinmethod
    def IsChannelModeSupported(self: Windows.Devices.Adc.IAdcController, channelMode: Windows.Devices.Adc.AdcChannelMode) -> Boolean: ...
    @winrt_mixinmethod
    def OpenChannel(self: Windows.Devices.Adc.IAdcController, channelNumber: Int32) -> Windows.Devices.Adc.AdcChannel: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Adc.IAdcControllerStatics2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Adc.AdcController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: Windows.Devices.Adc.IAdcControllerStatics, provider: Windows.Devices.Adc.Provider.IAdcProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Adc.AdcController]]: ...
    ChannelCount = property(get_ChannelCount, None)
    ResolutionInBits = property(get_ResolutionInBits, None)
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
class IAdcChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('040bf414-2588-4a56-ab-ef-73-a2-60-ac-c6-0a')
    @winrt_commethod(6)
    def get_Controller(self) -> Windows.Devices.Adc.AdcController: ...
    @winrt_commethod(7)
    def ReadValue(self) -> Int32: ...
    @winrt_commethod(8)
    def ReadRatio(self) -> Double: ...
    Controller = property(get_Controller, None)
class IAdcController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2a76e4b0-a896-4219-86-b6-ea-8c-dc-e9-8f-56')
    @winrt_commethod(6)
    def get_ChannelCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ResolutionInBits(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MinValue(self) -> Int32: ...
    @winrt_commethod(9)
    def get_MaxValue(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ChannelMode(self) -> Windows.Devices.Adc.AdcChannelMode: ...
    @winrt_commethod(11)
    def put_ChannelMode(self, value: Windows.Devices.Adc.AdcChannelMode) -> Void: ...
    @winrt_commethod(12)
    def IsChannelModeSupported(self, channelMode: Windows.Devices.Adc.AdcChannelMode) -> Boolean: ...
    @winrt_commethod(13)
    def OpenChannel(self, channelNumber: Int32) -> Windows.Devices.Adc.AdcChannel: ...
    ChannelCount = property(get_ChannelCount, None)
    ResolutionInBits = property(get_ResolutionInBits, None)
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
    ChannelMode = property(get_ChannelMode, put_ChannelMode)
class IAdcControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cce98e0c-01f8-4891-bc-3b-be-53-ef-27-9c-a4')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: Windows.Devices.Adc.Provider.IAdcProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Adc.AdcController]]: ...
class IAdcControllerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a2b93b1d-977b-4f5a-a5-fe-a6-ab-af-fe-64-84')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Adc.AdcController]: ...
make_head(_module, 'AdcChannel')
make_head(_module, 'AdcController')
make_head(_module, 'IAdcChannel')
make_head(_module, 'IAdcController')
make_head(_module, 'IAdcControllerStatics')
make_head(_module, 'IAdcControllerStatics2')
