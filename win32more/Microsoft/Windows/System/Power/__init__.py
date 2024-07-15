from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.System.Power
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class BatteryStatus(Enum, Int32):
    NotPresent = 0
    Discharging = 1
    Idle = 2
    Charging = 3
class DisplayStatus(Enum, Int32):
    Off = 0
    On = 1
    Dimmed = 2
class EffectivePowerMode(Enum, Int32):
    BatterySaver = 0
    BetterBattery = 1
    Balanced = 2
    HighPerformance = 3
    MaxPerformance = 4
    GameMode = 5
    MixedReality = 6
class EnergySaverStatus(Enum, Int32):
    Uninitialized = 0
    Disabled = 1
    Off = 2
    On = 3
class IPowerManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.System.Power.IPowerManagerStatics'
    _iid_ = Guid('{fa3554cc-be1c-534c-bff8-72df78e9f4a4}')
    @winrt_commethod(6)
    def get_EnergySaverStatus(self) -> win32more.Microsoft.Windows.System.Power.EnergySaverStatus: ...
    @winrt_commethod(7)
    def add_EnergySaverStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_EnergySaverStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_BatteryStatus(self) -> win32more.Microsoft.Windows.System.Power.BatteryStatus: ...
    @winrt_commethod(10)
    def add_BatteryStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BatteryStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_PowerSupplyStatus(self) -> win32more.Microsoft.Windows.System.Power.PowerSupplyStatus: ...
    @winrt_commethod(13)
    def add_PowerSupplyStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PowerSupplyStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def get_RemainingChargePercent(self) -> Int32: ...
    @winrt_commethod(16)
    def add_RemainingChargePercentChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_RemainingChargePercentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def get_RemainingDischargeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(19)
    def add_RemainingDischargeTimeChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_RemainingDischargeTimeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def get_PowerSourceKind(self) -> win32more.Microsoft.Windows.System.Power.PowerSourceKind: ...
    @winrt_commethod(22)
    def add_PowerSourceKindChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_PowerSourceKindChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def get_DisplayStatus(self) -> win32more.Microsoft.Windows.System.Power.DisplayStatus: ...
    @winrt_commethod(25)
    def add_DisplayStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_DisplayStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_SystemIdleStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_SystemIdleStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def get_EffectivePowerMode(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.System.Power.EffectivePowerMode]: ...
    @winrt_commethod(30)
    def add_EffectivePowerModeChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_EffectivePowerModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def get_UserPresenceStatus(self) -> win32more.Microsoft.Windows.System.Power.UserPresenceStatus: ...
    @winrt_commethod(33)
    def add_UserPresenceStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_UserPresenceStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(35)
    def get_SystemSuspendStatus(self) -> win32more.Microsoft.Windows.System.Power.SystemSuspendStatus: ...
    @winrt_commethod(36)
    def add_SystemSuspendStatusChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(37)
    def remove_SystemSuspendStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BatteryStatus = property(get_BatteryStatus, None)
    DisplayStatus = property(get_DisplayStatus, None)
    EffectivePowerMode = property(get_EffectivePowerMode, None)
    EnergySaverStatus = property(get_EnergySaverStatus, None)
    PowerSourceKind = property(get_PowerSourceKind, None)
    PowerSupplyStatus = property(get_PowerSupplyStatus, None)
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
    SystemSuspendStatus = property(get_SystemSuspendStatus, None)
    UserPresenceStatus = property(get_UserPresenceStatus, None)
    EnergySaverStatusChanged = event()
    BatteryStatusChanged = event()
    PowerSupplyStatusChanged = event()
    RemainingChargePercentChanged = event()
    RemainingDischargeTimeChanged = event()
    PowerSourceKindChanged = event()
    DisplayStatusChanged = event()
    SystemIdleStatusChanged = event()
    EffectivePowerModeChanged = event()
    UserPresenceStatusChanged = event()
    SystemSuspendStatusChanged = event()
class IPowerManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.System.Power.IPowerManagerStatics2'
    _iid_ = Guid('{61f3cc25-65b4-5def-9c9b-990cef3b0833}')
    @winrt_commethod(6)
    def get_EffectivePowerMode2(self) -> win32more.Microsoft.Windows.System.Power.EffectivePowerMode: ...
    EffectivePowerMode2 = property(get_EffectivePowerMode2, None)
class _PowerManager_Meta_(ComPtr.__class__):
    pass
class PowerManager(ComPtr, metaclass=_PowerManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.System.Power.PowerManager'
    @winrt_classmethod
    def get_EffectivePowerMode2(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics2) -> win32more.Microsoft.Windows.System.Power.EffectivePowerMode: ...
    @winrt_classmethod
    def get_EnergySaverStatus(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.EnergySaverStatus: ...
    @winrt_classmethod
    def add_EnergySaverStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnergySaverStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_BatteryStatus(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.BatteryStatus: ...
    @winrt_classmethod
    def add_BatteryStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BatteryStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PowerSupplyStatus(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.PowerSupplyStatus: ...
    @winrt_classmethod
    def add_PowerSupplyStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PowerSupplyStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RemainingChargePercent(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> Int32: ...
    @winrt_classmethod
    def add_RemainingChargePercentChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RemainingChargePercentChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RemainingDischargeTime(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_classmethod
    def add_RemainingDischargeTimeChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RemainingDischargeTimeChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PowerSourceKind(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.PowerSourceKind: ...
    @winrt_classmethod
    def add_PowerSourceKindChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PowerSourceKindChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_DisplayStatus(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.DisplayStatus: ...
    @winrt_classmethod
    def add_DisplayStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DisplayStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_SystemIdleStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SystemIdleStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_EffectivePowerMode(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.System.Power.EffectivePowerMode]: ...
    @winrt_classmethod
    def add_EffectivePowerModeChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EffectivePowerModeChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_UserPresenceStatus(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.UserPresenceStatus: ...
    @winrt_classmethod
    def add_UserPresenceStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UserPresenceStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_SystemSuspendStatus(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics) -> win32more.Microsoft.Windows.System.Power.SystemSuspendStatus: ...
    @winrt_classmethod
    def add_SystemSuspendStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SystemSuspendStatusChanged(cls: win32more.Microsoft.Windows.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _PowerManager_Meta_.BatteryStatus = property(get_BatteryStatus, None)
    _PowerManager_Meta_.DisplayStatus = property(get_DisplayStatus, None)
    _PowerManager_Meta_.EffectivePowerMode = property(get_EffectivePowerMode, None)
    _PowerManager_Meta_.EffectivePowerMode2 = property(get_EffectivePowerMode2, None)
    _PowerManager_Meta_.EnergySaverStatus = property(get_EnergySaverStatus, None)
    _PowerManager_Meta_.PowerSourceKind = property(get_PowerSourceKind, None)
    _PowerManager_Meta_.PowerSupplyStatus = property(get_PowerSupplyStatus, None)
    _PowerManager_Meta_.RemainingChargePercent = property(get_RemainingChargePercent, None)
    _PowerManager_Meta_.RemainingDischargeTime = property(get_RemainingDischargeTime, None)
    _PowerManager_Meta_.SystemSuspendStatus = property(get_SystemSuspendStatus, None)
    _PowerManager_Meta_.UserPresenceStatus = property(get_UserPresenceStatus, None)
PowerNotificationsContract: UInt32 = 131072
class PowerSourceKind(Enum, Int32):
    AC = 0
    DC = 1
class PowerSupplyStatus(Enum, Int32):
    NotPresent = 0
    Inadequate = 1
    Adequate = 2
class SystemSuspendStatus(Enum, Int32):
    Uninitialized = 0
    Entering = 1
    AutoResume = 2
    ManualResume = 3
class UserPresenceStatus(Enum, Int32):
    Present = 0
    Absent = 1


make_ready(__name__)
