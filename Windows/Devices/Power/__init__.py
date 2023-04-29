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
import Windows.Devices.Power
import Windows.Foundation
import Windows.System.Power
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
    ClassId = 'Windows.Devices.Power.Battery'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Power.IBattery) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetReport(self: Windows.Devices.Power.IBattery) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_mixinmethod
    def add_ReportUpdated(self: Windows.Devices.Power.IBattery, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Power.Battery, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReportUpdated(self: Windows.Devices.Power.IBattery, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AggregateBattery(cls: Windows.Devices.Power.IBatteryStatics) -> Windows.Devices.Power.Battery: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Power.IBatteryStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Power.Battery]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Power.IBatteryStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    AggregateBattery = property(get_AggregateBattery, None)
class BatteryReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Power.BatteryReport'
    @winrt_mixinmethod
    def get_ChargeRateInMilliwatts(self: Windows.Devices.Power.IBatteryReport) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_DesignCapacityInMilliwattHours(self: Windows.Devices.Power.IBatteryReport) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_FullChargeCapacityInMilliwattHours(self: Windows.Devices.Power.IBatteryReport) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_RemainingCapacityInMilliwattHours(self: Windows.Devices.Power.IBatteryReport) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Power.IBatteryReport) -> Windows.System.Power.BatteryStatus: ...
    ChargeRateInMilliwatts = property(get_ChargeRateInMilliwatts, None)
    DesignCapacityInMilliwattHours = property(get_DesignCapacityInMilliwattHours, None)
    FullChargeCapacityInMilliwattHours = property(get_FullChargeCapacityInMilliwattHours, None)
    RemainingCapacityInMilliwattHours = property(get_RemainingCapacityInMilliwattHours, None)
    Status = property(get_Status, None)
class IBattery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bc894fc6-0072-47c8-8b-5d-61-4a-aa-7a-43-7e')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetReport(self) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_commethod(8)
    def add_ReportUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Power.Battery, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ReportUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
class IBatteryReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c9858c3a-4e13-420a-a8-d0-24-f1-8f-39-54-01')
    @winrt_commethod(6)
    def get_ChargeRateInMilliwatts(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_DesignCapacityInMilliwattHours(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_FullChargeCapacityInMilliwattHours(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_RemainingCapacityInMilliwattHours(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def get_Status(self) -> Windows.System.Power.BatteryStatus: ...
    ChargeRateInMilliwatts = property(get_ChargeRateInMilliwatts, None)
    DesignCapacityInMilliwattHours = property(get_DesignCapacityInMilliwattHours, None)
    FullChargeCapacityInMilliwattHours = property(get_FullChargeCapacityInMilliwattHours, None)
    RemainingCapacityInMilliwattHours = property(get_RemainingCapacityInMilliwattHours, None)
    Status = property(get_Status, None)
class IBatteryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('79cd72b6-9e5e-4452-be-a6-df-cd-54-1e-59-7f')
    @winrt_commethod(6)
    def get_AggregateBattery(self) -> Windows.Devices.Power.Battery: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Power.Battery]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
    AggregateBattery = property(get_AggregateBattery, None)
make_head(_module, 'Battery')
make_head(_module, 'BatteryReport')
make_head(_module, 'IBattery')
make_head(_module, 'IBatteryReport')
make_head(_module, 'IBatteryStatics')
