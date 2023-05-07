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
import Windows.Devices.Pwm.Provider
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
class IPwmControllerProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.Provider.IPwmControllerProvider'
    _iid_ = Guid('{1300593b-e2e3-40a4-b7d9-48dff0377a52}')
    @winrt_commethod(6)
    def get_PinCount(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider) -> Int32: ...
    @winrt_commethod(7)
    def get_ActualFrequency(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider) -> Double: ...
    @winrt_commethod(8)
    def SetDesiredFrequency(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider, frequency: Double) -> Double: ...
    @winrt_commethod(9)
    def get_MaxFrequency(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider) -> Double: ...
    @winrt_commethod(10)
    def get_MinFrequency(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider) -> Double: ...
    @winrt_commethod(11)
    def AcquirePin(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider, pin: Int32) -> Void: ...
    @winrt_commethod(12)
    def ReleasePin(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider, pin: Int32) -> Void: ...
    @winrt_commethod(13)
    def EnablePin(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider, pin: Int32) -> Void: ...
    @winrt_commethod(14)
    def DisablePin(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider, pin: Int32) -> Void: ...
    @winrt_commethod(15)
    def SetPulseParameters(self: Windows.Devices.Pwm.Provider.IPwmControllerProvider, pin: Int32, dutyCycle: Double, invertPolarity: Boolean) -> Void: ...
    PinCount = property(get_PinCount, None)
    ActualFrequency = property(get_ActualFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
class IPwmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.Provider.IPwmProvider'
    _iid_ = Guid('{a3301228-52f1-47b0-9349-66ba43d25902}')
    @winrt_commethod(6)
    def GetControllers(self: Windows.Devices.Pwm.Provider.IPwmProvider) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Pwm.Provider.IPwmControllerProvider]: ...
make_head(_module, 'IPwmControllerProvider')
make_head(_module, 'IPwmProvider')
