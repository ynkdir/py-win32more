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
import Windows.Devices.Pwm
import Windows.Devices.Pwm.Provider
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
class IPwmController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c45f5c85-d2e8-42cf-9b-d6-cf-5e-d0-29-e6-a7')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ActualFrequency(self) -> Double: ...
    @winrt_commethod(8)
    def SetDesiredFrequency(self, desiredFrequency: Double) -> Double: ...
    @winrt_commethod(9)
    def get_MinFrequency(self) -> Double: ...
    @winrt_commethod(10)
    def get_MaxFrequency(self) -> Double: ...
    @winrt_commethod(11)
    def OpenPin(self, pinNumber: Int32) -> Windows.Devices.Pwm.PwmPin: ...
    PinCount = property(get_PinCount, None)
    ActualFrequency = property(get_ActualFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
class IPwmControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4263bda1-8946-4404-bd-48-81-dd-12-4a-f4-d9')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: Windows.Devices.Pwm.Provider.IPwmProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Pwm.PwmController]]: ...
class IPwmControllerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('44fc5b1f-f119-4bdd-97-ad-f7-6e-f9-86-73-6d')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Pwm.PwmController]: ...
class IPwmControllerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b2581871-0229-4344-ae-3f-9b-7c-d0-e6-6b-94')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Pwm.PwmController]: ...
class IPwmPin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('22972dc8-c6cf-4821-b7-f9-c6-45-4f-b6-af-79')
    @winrt_commethod(6)
    def get_Controller(self) -> Windows.Devices.Pwm.PwmController: ...
    @winrt_commethod(7)
    def GetActiveDutyCyclePercentage(self) -> Double: ...
    @winrt_commethod(8)
    def SetActiveDutyCyclePercentage(self, dutyCyclePercentage: Double) -> Void: ...
    @winrt_commethod(9)
    def get_Polarity(self) -> Windows.Devices.Pwm.PwmPulsePolarity: ...
    @winrt_commethod(10)
    def put_Polarity(self, value: Windows.Devices.Pwm.PwmPulsePolarity) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    @winrt_commethod(13)
    def get_IsStarted(self) -> Boolean: ...
    Controller = property(get_Controller, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class PwmController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.PwmController'
    @winrt_mixinmethod
    def get_PinCount(self: Windows.Devices.Pwm.IPwmController) -> Int32: ...
    @winrt_mixinmethod
    def get_ActualFrequency(self: Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def SetDesiredFrequency(self: Windows.Devices.Pwm.IPwmController, desiredFrequency: Double) -> Double: ...
    @winrt_mixinmethod
    def get_MinFrequency(self: Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def get_MaxFrequency(self: Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def OpenPin(self: Windows.Devices.Pwm.IPwmController, pinNumber: Int32) -> Windows.Devices.Pwm.PwmPin: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Pwm.IPwmControllerStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: Windows.Devices.Pwm.IPwmControllerStatics3, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Pwm.IPwmControllerStatics3, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Pwm.PwmController]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Pwm.IPwmControllerStatics2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Pwm.PwmController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: Windows.Devices.Pwm.IPwmControllerStatics, provider: Windows.Devices.Pwm.Provider.IPwmProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Pwm.PwmController]]: ...
    PinCount = property(get_PinCount, None)
    ActualFrequency = property(get_ActualFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
class PwmPin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.PwmPin'
    @winrt_mixinmethod
    def get_Controller(self: Windows.Devices.Pwm.IPwmPin) -> Windows.Devices.Pwm.PwmController: ...
    @winrt_mixinmethod
    def GetActiveDutyCyclePercentage(self: Windows.Devices.Pwm.IPwmPin) -> Double: ...
    @winrt_mixinmethod
    def SetActiveDutyCyclePercentage(self: Windows.Devices.Pwm.IPwmPin, dutyCyclePercentage: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: Windows.Devices.Pwm.IPwmPin) -> Windows.Devices.Pwm.PwmPulsePolarity: ...
    @winrt_mixinmethod
    def put_Polarity(self: Windows.Devices.Pwm.IPwmPin, value: Windows.Devices.Pwm.PwmPulsePolarity) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Pwm.IPwmPin) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Pwm.IPwmPin) -> Void: ...
    @winrt_mixinmethod
    def get_IsStarted(self: Windows.Devices.Pwm.IPwmPin) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Controller = property(get_Controller, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
PwmPulsePolarity = Int32
PwmPulsePolarity_ActiveHigh: PwmPulsePolarity = 0
PwmPulsePolarity_ActiveLow: PwmPulsePolarity = 1
make_head(_module, 'IPwmController')
make_head(_module, 'IPwmControllerStatics')
make_head(_module, 'IPwmControllerStatics2')
make_head(_module, 'IPwmControllerStatics3')
make_head(_module, 'IPwmPin')
make_head(_module, 'PwmController')
make_head(_module, 'PwmPin')
