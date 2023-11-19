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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.Windows.System.Power
import win32more.Windows.Foundation
BatteryStatus = Int32
BatteryStatus_NotPresent: BatteryStatus = 0
BatteryStatus_Discharging: BatteryStatus = 1
BatteryStatus_Idle: BatteryStatus = 2
BatteryStatus_Charging: BatteryStatus = 3
DisplayStatus = Int32
DisplayStatus_Off: DisplayStatus = 0
DisplayStatus_On: DisplayStatus = 1
DisplayStatus_Dimmed: DisplayStatus = 2
EffectivePowerMode = Int32
EffectivePowerMode_BatterySaver: EffectivePowerMode = 0
EffectivePowerMode_BetterBattery: EffectivePowerMode = 1
EffectivePowerMode_Balanced: EffectivePowerMode = 2
EffectivePowerMode_HighPerformance: EffectivePowerMode = 3
EffectivePowerMode_MaxPerformance: EffectivePowerMode = 4
EffectivePowerMode_GameMode: EffectivePowerMode = 5
EffectivePowerMode_MixedReality: EffectivePowerMode = 6
EnergySaverStatus = Int32
EnergySaverStatus_Uninitialized: EnergySaverStatus = 0
EnergySaverStatus_Disabled: EnergySaverStatus = 1
EnergySaverStatus_Off: EnergySaverStatus = 2
EnergySaverStatus_On: EnergySaverStatus = 3
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
    EnergySaverStatus = property(get_EnergySaverStatus, None)
    BatteryStatus = property(get_BatteryStatus, None)
    PowerSupplyStatus = property(get_PowerSupplyStatus, None)
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
    PowerSourceKind = property(get_PowerSourceKind, None)
    DisplayStatus = property(get_DisplayStatus, None)
    EffectivePowerMode = property(get_EffectivePowerMode, None)
    UserPresenceStatus = property(get_UserPresenceStatus, None)
    SystemSuspendStatus = property(get_SystemSuspendStatus, None)
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
    _PowerManager_Meta_.EffectivePowerMode2 = property(get_EffectivePowerMode2.__wrapped__, None)
    _PowerManager_Meta_.EnergySaverStatus = property(get_EnergySaverStatus.__wrapped__, None)
    _PowerManager_Meta_.BatteryStatus = property(get_BatteryStatus.__wrapped__, None)
    _PowerManager_Meta_.PowerSupplyStatus = property(get_PowerSupplyStatus.__wrapped__, None)
    _PowerManager_Meta_.RemainingChargePercent = property(get_RemainingChargePercent.__wrapped__, None)
    _PowerManager_Meta_.RemainingDischargeTime = property(get_RemainingDischargeTime.__wrapped__, None)
    _PowerManager_Meta_.PowerSourceKind = property(get_PowerSourceKind.__wrapped__, None)
    _PowerManager_Meta_.DisplayStatus = property(get_DisplayStatus.__wrapped__, None)
    _PowerManager_Meta_.EffectivePowerMode = property(get_EffectivePowerMode.__wrapped__, None)
    _PowerManager_Meta_.UserPresenceStatus = property(get_UserPresenceStatus.__wrapped__, None)
    _PowerManager_Meta_.SystemSuspendStatus = property(get_SystemSuspendStatus.__wrapped__, None)
PowerNotificationsContract: UInt32 = 131072
PowerSourceKind = Int32
AC: PowerSourceKind = 0
DC: PowerSourceKind = 1
PowerSupplyStatus = Int32
PowerSupplyStatus_NotPresent: PowerSupplyStatus = 0
PowerSupplyStatus_Inadequate: PowerSupplyStatus = 1
PowerSupplyStatus_Adequate: PowerSupplyStatus = 2
SystemSuspendStatus = Int32
SystemSuspendStatus_Uninitialized: SystemSuspendStatus = 0
SystemSuspendStatus_Entering: SystemSuspendStatus = 1
SystemSuspendStatus_AutoResume: SystemSuspendStatus = 2
SystemSuspendStatus_ManualResume: SystemSuspendStatus = 3
UserPresenceStatus = Int32
UserPresenceStatus_Present: UserPresenceStatus = 0
UserPresenceStatus_Absent: UserPresenceStatus = 1
make_ready(__name__)
