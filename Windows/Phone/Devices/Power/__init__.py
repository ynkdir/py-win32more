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
import Windows.Foundation
import Windows.Phone.Devices.Power
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Battery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Power.Battery'
    @winrt_mixinmethod
    def get_RemainingChargePercent(self: Windows.Phone.Devices.Power.IBattery) -> Int32: ...
    @winrt_mixinmethod
    def get_RemainingDischargeTime(self: Windows.Phone.Devices.Power.IBattery) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_RemainingChargePercentChanged(self: Windows.Phone.Devices.Power.IBattery, changeHandler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemainingChargePercentChanged(self: Windows.Phone.Devices.Power.IBattery, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Phone.Devices.Power.IBatteryStatics) -> Windows.Phone.Devices.Power.Battery: ...
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
class IBattery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{972adbdd-6720-4702-a476-b9d38a0070e3}')
    @winrt_commethod(6)
    def get_RemainingChargePercent(self) -> Int32: ...
    @winrt_commethod(7)
    def get_RemainingDischargeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def add_RemainingChargePercentChanged(self, changeHandler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RemainingChargePercentChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
class IBatteryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{faf5bc70-6369-11e1-b86c-0800200c9a66}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Phone.Devices.Power.Battery: ...
make_head(_module, 'Battery')
make_head(_module, 'IBattery')
make_head(_module, 'IBatteryStatics')
