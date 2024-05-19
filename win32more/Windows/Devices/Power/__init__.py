from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import FillArray, Generic, K, MulticastDelegate, PassArray, ReceiveArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Power
import win32more.Windows.Foundation
import win32more.Windows.System.Power
import win32more.Windows.Win32.System.WinRT
class _Battery_Meta_(ComPtr.__class__):
    pass
class Battery(ComPtr, metaclass=_Battery_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Power.IBattery
    _classid_ = 'Windows.Devices.Power.Battery'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Power.IBattery) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetReport(self: win32more.Windows.Devices.Power.IBattery) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_mixinmethod
    def add_ReportUpdated(self: win32more.Windows.Devices.Power.IBattery, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Power.Battery, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReportUpdated(self: win32more.Windows.Devices.Power.IBattery, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AggregateBattery(cls: win32more.Windows.Devices.Power.IBatteryStatics) -> win32more.Windows.Devices.Power.Battery: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Power.IBatteryStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Power.Battery]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Power.IBatteryStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    _Battery_Meta_.AggregateBattery = property(get_AggregateBattery.__wrapped__, None)
class BatteryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Power.IBatteryReport
    _classid_ = 'Windows.Devices.Power.BatteryReport'
    @winrt_mixinmethod
    def get_ChargeRateInMilliwatts(self: win32more.Windows.Devices.Power.IBatteryReport) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_DesignCapacityInMilliwattHours(self: win32more.Windows.Devices.Power.IBatteryReport) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_FullChargeCapacityInMilliwattHours(self: win32more.Windows.Devices.Power.IBatteryReport) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_RemainingCapacityInMilliwattHours(self: win32more.Windows.Devices.Power.IBatteryReport) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Power.IBatteryReport) -> win32more.Windows.System.Power.BatteryStatus: ...
    ChargeRateInMilliwatts = property(get_ChargeRateInMilliwatts, None)
    DesignCapacityInMilliwattHours = property(get_DesignCapacityInMilliwattHours, None)
    FullChargeCapacityInMilliwattHours = property(get_FullChargeCapacityInMilliwattHours, None)
    RemainingCapacityInMilliwattHours = property(get_RemainingCapacityInMilliwattHours, None)
    Status = property(get_Status, None)
class IBattery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Power.IBattery'
    _iid_ = Guid('{bc894fc6-0072-47c8-8b5d-614aaa7a437e}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetReport(self) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_commethod(8)
    def add_ReportUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Power.Battery, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ReportUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
class IBatteryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Power.IBatteryReport'
    _iid_ = Guid('{c9858c3a-4e13-420a-a8d0-24f18f395401}')
    @winrt_commethod(6)
    def get_ChargeRateInMilliwatts(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_DesignCapacityInMilliwattHours(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_FullChargeCapacityInMilliwattHours(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_RemainingCapacityInMilliwattHours(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def get_Status(self) -> win32more.Windows.System.Power.BatteryStatus: ...
    ChargeRateInMilliwatts = property(get_ChargeRateInMilliwatts, None)
    DesignCapacityInMilliwattHours = property(get_DesignCapacityInMilliwattHours, None)
    FullChargeCapacityInMilliwattHours = property(get_FullChargeCapacityInMilliwattHours, None)
    RemainingCapacityInMilliwattHours = property(get_RemainingCapacityInMilliwattHours, None)
    Status = property(get_Status, None)
class IBatteryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Power.IBatteryStatics'
    _iid_ = Guid('{79cd72b6-9e5e-4452-bea6-dfcd541e597f}')
    @winrt_commethod(6)
    def get_AggregateBattery(self) -> win32more.Windows.Devices.Power.Battery: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Power.Battery]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
    AggregateBattery = property(get_AggregateBattery, None)


make_ready(__name__)
