from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Phone.Devices.Power
class Battery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Devices.Power.IBattery
    _classid_ = 'Windows.Phone.Devices.Power.Battery'
    @winrt_mixinmethod
    def get_RemainingChargePercent(self: win32more.Windows.Phone.Devices.Power.IBattery) -> Int32: ...
    @winrt_mixinmethod
    def get_RemainingDischargeTime(self: win32more.Windows.Phone.Devices.Power.IBattery) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_RemainingChargePercentChanged(self: win32more.Windows.Phone.Devices.Power.IBattery, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemainingChargePercentChanged(self: win32more.Windows.Phone.Devices.Power.IBattery, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Phone.Devices.Power.IBatteryStatics) -> win32more.Windows.Phone.Devices.Power.Battery: ...
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
class IBattery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Power.IBattery'
    _iid_ = Guid('{972adbdd-6720-4702-a476-b9d38a0070e3}')
    @winrt_commethod(6)
    def get_RemainingChargePercent(self) -> Int32: ...
    @winrt_commethod(7)
    def get_RemainingDischargeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def add_RemainingChargePercentChanged(self, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RemainingChargePercentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
class IBatteryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Power.IBatteryStatics'
    _iid_ = Guid('{faf5bc70-6369-11e1-b86c-0800200c9a66}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Phone.Devices.Power.Battery: ...


make_ready(__name__)
