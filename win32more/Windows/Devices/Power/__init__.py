from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Power
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
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
    _Battery_Meta_.AggregateBattery = property(get_AggregateBattery, None)
    ReportUpdated = event()
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
    ReportUpdated = event()
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
class IPowerGridData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Power.IPowerGridData'
    _iid_ = Guid('{c360fb17-fc92-5f6e-999d-16a4cf9d6c40}')
    @winrt_commethod(6)
    def get_Severity(self) -> Double: ...
    @winrt_commethod(7)
    def get_IsLowUserExperienceImpact(self) -> Boolean: ...
    IsLowUserExperienceImpact = property(get_IsLowUserExperienceImpact, None)
    Severity = property(get_Severity, None)
class IPowerGridForecast(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Power.IPowerGridForecast'
    _iid_ = Guid('{077e4de9-ed60-58bb-a850-003c6a138685}')
    @winrt_commethod(6)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_BlockDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Forecast(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Power.PowerGridData]: ...
    BlockDuration = property(get_BlockDuration, None)
    Forecast = property(get_Forecast, None)
    StartTime = property(get_StartTime, None)
class IPowerGridForecastStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Power.IPowerGridForecastStatics'
    _iid_ = Guid('{5b78c806-2e4e-5bcc-bb34-cb81c60f9e12}')
    @winrt_commethod(6)
    def GetForecast(self) -> win32more.Windows.Devices.Power.PowerGridForecast: ...
    @winrt_commethod(7)
    def add_ForecastUpdated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ForecastUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ForecastUpdated = event()
PowerGridApiContract: UInt32 = 65536
class PowerGridData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Power.IPowerGridData
    _classid_ = 'Windows.Devices.Power.PowerGridData'
    @winrt_mixinmethod
    def get_Severity(self: win32more.Windows.Devices.Power.IPowerGridData) -> Double: ...
    @winrt_mixinmethod
    def get_IsLowUserExperienceImpact(self: win32more.Windows.Devices.Power.IPowerGridData) -> Boolean: ...
    IsLowUserExperienceImpact = property(get_IsLowUserExperienceImpact, None)
    Severity = property(get_Severity, None)
class PowerGridForecast(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Power.IPowerGridForecast
    _classid_ = 'Windows.Devices.Power.PowerGridForecast'
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Devices.Power.IPowerGridForecast) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_BlockDuration(self: win32more.Windows.Devices.Power.IPowerGridForecast) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Forecast(self: win32more.Windows.Devices.Power.IPowerGridForecast) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Power.PowerGridData]: ...
    @winrt_classmethod
    def GetForecast(cls: win32more.Windows.Devices.Power.IPowerGridForecastStatics) -> win32more.Windows.Devices.Power.PowerGridForecast: ...
    @winrt_classmethod
    def add_ForecastUpdated(cls: win32more.Windows.Devices.Power.IPowerGridForecastStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ForecastUpdated(cls: win32more.Windows.Devices.Power.IPowerGridForecastStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BlockDuration = property(get_BlockDuration, None)
    Forecast = property(get_Forecast, None)
    StartTime = property(get_StartTime, None)


make_ready(__name__)
