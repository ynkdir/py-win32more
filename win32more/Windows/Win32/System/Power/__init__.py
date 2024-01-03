from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Power
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Threading
import win32more.Windows.Win32.UI.WindowsAndMessaging
class ACPI_REAL_TIME(EasyCastStructure):
    Year: UInt16
    Month: Byte
    Day: Byte
    Hour: Byte
    Minute: Byte
    Second: Byte
    Valid: Byte
    Milliseconds: UInt16
    TimeZone: Int16
    DayLight: Byte
    Reserved1: Byte * 3
class ACPI_TIME_AND_ALARM_CAPABILITIES(EasyCastStructure):
    AcWakeSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    DcWakeSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    S4AcWakeSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    S4DcWakeSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    S5AcWakeSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    S5DcWakeSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    S4S5WakeStatusSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    DeepestWakeSystemState: UInt32
    RealTimeFeaturesSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    RealTimeResolution: win32more.Windows.Win32.System.Power.ACPI_TIME_RESOLUTION
ACPI_TIME_RESOLUTION = Int32
ACPI_TIME_RESOLUTION_AcpiTimeResolutionMilliseconds: win32more.Windows.Win32.System.Power.ACPI_TIME_RESOLUTION = 0
ACPI_TIME_RESOLUTION_AcpiTimeResolutionSeconds: win32more.Windows.Win32.System.Power.ACPI_TIME_RESOLUTION = 1
ACPI_TIME_RESOLUTION_AcpiTimeResolutionMax: win32more.Windows.Win32.System.Power.ACPI_TIME_RESOLUTION = 2
class ADMINISTRATOR_POWER_POLICY(EasyCastStructure):
    MinSleep: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    MaxSleep: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    MinVideoTimeout: UInt32
    MaxVideoTimeout: UInt32
    MinSpindownTimeout: UInt32
    MaxSpindownTimeout: UInt32
PPM_FIRMWARE_ACPI1C2: UInt32 = 1
PPM_FIRMWARE_ACPI1C3: UInt32 = 2
PPM_FIRMWARE_ACPI1TSTATES: UInt32 = 4
PPM_FIRMWARE_CST: UInt32 = 8
PPM_FIRMWARE_CSD: UInt32 = 16
PPM_FIRMWARE_PCT: UInt32 = 32
PPM_FIRMWARE_PSS: UInt32 = 64
PPM_FIRMWARE_XPSS: UInt32 = 128
PPM_FIRMWARE_PPC: UInt32 = 256
PPM_FIRMWARE_PSD: UInt32 = 512
PPM_FIRMWARE_PTC: UInt32 = 1024
PPM_FIRMWARE_TSS: UInt32 = 2048
PPM_FIRMWARE_TPC: UInt32 = 4096
PPM_FIRMWARE_TSD: UInt32 = 8192
PPM_FIRMWARE_PCCH: UInt32 = 16384
PPM_FIRMWARE_PCCP: UInt32 = 32768
PPM_FIRMWARE_OSC: UInt32 = 65536
PPM_FIRMWARE_PDC: UInt32 = 131072
PPM_FIRMWARE_CPC: UInt32 = 262144
PPM_FIRMWARE_LPI: UInt32 = 524288
PPM_PERFORMANCE_IMPLEMENTATION_NONE: UInt32 = 0
PPM_PERFORMANCE_IMPLEMENTATION_PSTATES: UInt32 = 1
PPM_PERFORMANCE_IMPLEMENTATION_PCCV1: UInt32 = 2
PPM_PERFORMANCE_IMPLEMENTATION_CPPC: UInt32 = 3
PPM_PERFORMANCE_IMPLEMENTATION_PEP: UInt32 = 4
PPM_IDLE_IMPLEMENTATION_NONE: UInt32 = 0
PPM_IDLE_IMPLEMENTATION_CSTATES: UInt32 = 1
PPM_IDLE_IMPLEMENTATION_PEP: UInt32 = 2
PPM_IDLE_IMPLEMENTATION_MICROPEP: UInt32 = 3
PPM_IDLE_IMPLEMENTATION_LPISTATES: UInt32 = 4
PPM_PERFSTATE_CHANGE_GUID: Guid = Guid('{a5b32ddd-7f39-4abc-b892-900e43b59ebb}')
PPM_PERFSTATE_DOMAIN_CHANGE_GUID: Guid = Guid('{995e6b7f-d653-497a-b978-36a30c29bf01}')
PPM_IDLESTATE_CHANGE_GUID: Guid = Guid('{4838fe4f-f71c-4e51-9ecc-8430a7ac4c6c}')
PPM_PERFSTATES_DATA_GUID: Guid = Guid('{5708cc20-7d40-4bf4-b4aa-2b01338d0126}')
PPM_IDLESTATES_DATA_GUID: Guid = Guid('{ba138e10-e250-4ad7-8616-cf1a7ad410e7}')
PPM_IDLE_ACCOUNTING_GUID: Guid = Guid('{e2a26f78-ae07-4ee0-a30f-ce54f55a94cd}')
PPM_IDLE_ACCOUNTING_EX_GUID: Guid = Guid('{d67abd39-81f8-4a5e-8152-72e31ec912ee}')
PPM_THERMALCONSTRAINT_GUID: Guid = Guid('{a852c2c8-1a4c-423b-8c2c-f30d82931a88}')
PPM_PERFMON_PERFSTATE_GUID: Guid = Guid('{7fd18652-0cfe-40d2-b0a1-0b066a87759e}')
PPM_THERMAL_POLICY_CHANGE_GUID: Guid = Guid('{48f377b8-6880-4c7b-8bdc-380176c6654d}')
PROCESSOR_NUMBER_PKEY: win32more.Windows.Win32.Devices.Properties.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{5724c81d-d5af-4c1f-a103-a06e28f204c6}'), pid=1)
GUID_DEVICE_BATTERY: Guid = Guid('{72631e54-78a4-11d0-bcf7-00aa00b7b32a}')
GUID_DEVICE_APPLICATIONLAUNCH_BUTTON: Guid = Guid('{629758ee-986e-4d9e-8e47-de27f8ab054d}')
GUID_DEVICE_SYS_BUTTON: Guid = Guid('{4afa3d53-74a7-11d0-be5e-00a0c9062857}')
GUID_DEVICE_LID: Guid = Guid('{4afa3d52-74a7-11d0-be5e-00a0c9062857}')
GUID_DEVICE_THERMAL_ZONE: Guid = Guid('{4afa3d51-74a7-11d0-be5e-00a0c9062857}')
GUID_DEVICE_FAN: Guid = Guid('{05ecd13d-81da-4a2a-8a4c-524f23dd4dc9}')
GUID_DEVICE_PROCESSOR: Guid = Guid('{97fadb10-4e33-40ae-359c-8bef029dbdd0}')
GUID_DEVICE_MEMORY: Guid = Guid('{3fd0f03d-92e0-45fb-b75c-5ed8ffb01021}')
GUID_DEVICE_ACPI_TIME: Guid = Guid('{97f99bf6-4497-4f18-bb22-4b9fb2fbef9c}')
GUID_DEVICE_MESSAGE_INDICATOR: Guid = Guid('{cd48a365-fa94-4ce2-a232-a1b764e5d8b4}')
GUID_CLASS_INPUT: Guid = Guid('{4d1e55b2-f16f-11cf-88cb-001111000030}')
GUID_DEVINTERFACE_THERMAL_COOLING: Guid = Guid('{dbe4373d-3c81-40cb-ace4-e0e5d05f0c9f}')
GUID_DEVINTERFACE_THERMAL_MANAGER: Guid = Guid('{927ec093-69a4-4bc0-bd02-711664714463}')
BATTERY_UNKNOWN_CAPACITY: UInt32 = 4294967295
UNKNOWN_CAPACITY: UInt32 = 4294967295
BATTERY_SYSTEM_BATTERY: UInt32 = 2147483648
BATTERY_CAPACITY_RELATIVE: UInt32 = 1073741824
BATTERY_IS_SHORT_TERM: UInt32 = 536870912
BATTERY_SEALED: UInt32 = 268435456
BATTERY_SET_CHARGE_SUPPORTED: UInt32 = 1
BATTERY_SET_DISCHARGE_SUPPORTED: UInt32 = 2
BATTERY_SET_CHARGINGSOURCE_SUPPORTED: UInt32 = 4
BATTERY_SET_CHARGER_ID_SUPPORTED: UInt32 = 8
BATTERY_UNKNOWN_TIME: UInt32 = 4294967295
BATTERY_UNKNOWN_CURRENT: UInt32 = 4294967295
UNKNOWN_CURRENT: UInt32 = 4294967295
BATTERY_USB_CHARGER_STATUS_FN_DEFAULT_USB: UInt32 = 1
BATTERY_USB_CHARGER_STATUS_UCM_PD: UInt32 = 2
BATTERY_UNKNOWN_VOLTAGE: UInt32 = 4294967295
BATTERY_UNKNOWN_RATE: UInt32 = 2147483648
UNKNOWN_RATE: UInt32 = 2147483648
UNKNOWN_VOLTAGE: UInt32 = 4294967295
BATTERY_POWER_ON_LINE: UInt32 = 1
BATTERY_DISCHARGING: UInt32 = 2
BATTERY_CHARGING: UInt32 = 4
BATTERY_CRITICAL: UInt32 = 8
MAX_BATTERY_STRING_SIZE: UInt32 = 128
IOCTL_BATTERY_QUERY_TAG: UInt32 = 2703424
IOCTL_BATTERY_QUERY_INFORMATION: UInt32 = 2703428
IOCTL_BATTERY_SET_INFORMATION: UInt32 = 2719816
IOCTL_BATTERY_QUERY_STATUS: UInt32 = 2703436
IOCTL_BATTERY_CHARGING_SOURCE_CHANGE: UInt32 = 2703440
BATTERY_TAG_INVALID: UInt32 = 0
MAX_ACTIVE_COOLING_LEVELS: UInt32 = 10
ACTIVE_COOLING: UInt32 = 0
PASSIVE_COOLING: UInt32 = 1
TZ_ACTIVATION_REASON_THERMAL: UInt32 = 1
TZ_ACTIVATION_REASON_CURRENT: UInt32 = 2
THERMAL_POLICY_VERSION_1: UInt32 = 1
THERMAL_POLICY_VERSION_2: UInt32 = 2
IOCTL_THERMAL_QUERY_INFORMATION: UInt32 = 2703488
IOCTL_THERMAL_SET_COOLING_POLICY: UInt32 = 2719876
IOCTL_RUN_ACTIVE_COOLING_METHOD: UInt32 = 2719880
IOCTL_THERMAL_SET_PASSIVE_LIMIT: UInt32 = 2719884
IOCTL_THERMAL_READ_TEMPERATURE: UInt32 = 2703504
IOCTL_THERMAL_READ_POLICY: UInt32 = 2703508
IOCTL_QUERY_LID: UInt32 = 2703552
IOCTL_NOTIFY_SWITCH_EVENT: UInt32 = 2703616
IOCTL_GET_SYS_BUTTON_CAPS: UInt32 = 2703680
IOCTL_GET_SYS_BUTTON_EVENT: UInt32 = 2703684
SYS_BUTTON_POWER: UInt32 = 1
SYS_BUTTON_SLEEP: UInt32 = 2
SYS_BUTTON_LID: UInt32 = 4
SYS_BUTTON_WAKE: UInt32 = 2147483648
SYS_BUTTON_LID_STATE_MASK: UInt32 = 196608
SYS_BUTTON_LID_OPEN: UInt32 = 65536
SYS_BUTTON_LID_CLOSED: UInt32 = 131072
SYS_BUTTON_LID_INITIAL: UInt32 = 262144
SYS_BUTTON_LID_CHANGED: UInt32 = 524288
IOCTL_GET_PROCESSOR_OBJ_INFO: UInt32 = 2703744
THERMAL_COOLING_INTERFACE_VERSION: UInt32 = 1
THERMAL_DEVICE_INTERFACE_VERSION: UInt32 = 1
IOCTL_SET_SYS_MESSAGE_INDICATOR: UInt32 = 2720192
IOCTL_SET_WAKE_ALARM_VALUE: UInt32 = 2720256
IOCTL_SET_WAKE_ALARM_POLICY: UInt32 = 2720260
IOCTL_GET_WAKE_ALARM_VALUE: UInt32 = 2736648
IOCTL_GET_WAKE_ALARM_POLICY: UInt32 = 2736652
ACPI_TIME_ADJUST_DAYLIGHT: UInt32 = 1
ACPI_TIME_IN_DAYLIGHT: UInt32 = 2
ACPI_TIME_ZONE_UNKNOWN: UInt32 = 2047
IOCTL_ACPI_GET_REAL_TIME: UInt32 = 2703888
IOCTL_ACPI_SET_REAL_TIME: UInt32 = 2720276
IOCTL_GET_WAKE_ALARM_SYSTEM_POWERSTATE: UInt32 = 2703896
IOCTL_GET_ACPI_TIME_AND_ALARM_CAPABILITIES: UInt32 = 2703900
BATTERY_STATUS_WMI_GUID: Guid = Guid('{fc4670d1-ebbf-416e-87ce-374a4ebc111a}')
BATTERY_RUNTIME_WMI_GUID: Guid = Guid('{535a3767-1ac2-49bc-a077-3f7a02e40aec}')
BATTERY_TEMPERATURE_WMI_GUID: Guid = Guid('{1a52a14d-adce-4a44-9a3e-c8d8f15ff2c2}')
BATTERY_FULL_CHARGED_CAPACITY_WMI_GUID: Guid = Guid('{40b40565-96f7-4435-8694-97e0e4395905}')
BATTERY_CYCLE_COUNT_WMI_GUID: Guid = Guid('{ef98db24-0014-4c25-a50b-c724ae5cd371}')
BATTERY_STATIC_DATA_WMI_GUID: Guid = Guid('{05e1e463-e4e2-4ea9-80cb-9bd4b3ca0655}')
BATTERY_STATUS_CHANGE_WMI_GUID: Guid = Guid('{cddfa0c3-7c5b-4e43-a034-059fa5b84364}')
BATTERY_TAG_CHANGE_WMI_GUID: Guid = Guid('{5e1f6e19-8786-4d23-94fc-9e746bd5d888}')
BATTERY_MINIPORT_UPDATE_DATA_VER_1: UInt32 = 1
BATTERY_MINIPORT_UPDATE_DATA_VER_2: UInt32 = 2
BATTERY_CLASS_MAJOR_VERSION: UInt32 = 1
BATTERY_CLASS_MINOR_VERSION: UInt32 = 0
BATTERY_CLASS_MINOR_VERSION_1: UInt32 = 1
GUID_DEVICE_ENERGY_METER: Guid = Guid('{45bd8344-7ed6-49cf-a440-c276c933b053}')
IOCTL_EMI_GET_VERSION: UInt32 = 2244608
IOCTL_EMI_GET_METADATA_SIZE: UInt32 = 2244612
IOCTL_EMI_GET_METADATA: UInt32 = 2244616
IOCTL_EMI_GET_MEASUREMENT: UInt32 = 2244620
EMI_NAME_MAX: UInt32 = 16
EMI_VERSION_V1: UInt32 = 1
EMI_VERSION_V2: UInt32 = 2
EFFECTIVE_POWER_MODE_V1: UInt32 = 1
EFFECTIVE_POWER_MODE_V2: UInt32 = 2
EnableSysTrayBatteryMeter: UInt32 = 1
EnableMultiBatteryDisplay: UInt32 = 2
EnablePasswordLogon: UInt32 = 4
EnableWakeOnRing: UInt32 = 8
EnableVideoDimDisplay: UInt32 = 16
POWER_ATTRIBUTE_HIDE: UInt32 = 1
POWER_ATTRIBUTE_SHOW_AOAC: UInt32 = 2
DEVICEPOWER_HARDWAREID: UInt32 = 2147483648
DEVICEPOWER_AND_OPERATION: UInt32 = 1073741824
DEVICEPOWER_FILTER_DEVICES_PRESENT: UInt32 = 536870912
DEVICEPOWER_FILTER_HARDWARE: UInt32 = 268435456
DEVICEPOWER_FILTER_WAKEENABLED: UInt32 = 134217728
DEVICEPOWER_FILTER_WAKEPROGRAMMABLE: UInt32 = 67108864
DEVICEPOWER_FILTER_ON_NAME: UInt32 = 33554432
DEVICEPOWER_SET_WAKEENABLED: UInt32 = 1
DEVICEPOWER_CLEAR_WAKEENABLED: UInt32 = 2
PDCAP_S0_SUPPORTED: UInt32 = 65536
PDCAP_S1_SUPPORTED: UInt32 = 131072
PDCAP_S2_SUPPORTED: UInt32 = 262144
PDCAP_S3_SUPPORTED: UInt32 = 524288
PDCAP_WAKE_FROM_S0_SUPPORTED: UInt32 = 1048576
PDCAP_WAKE_FROM_S1_SUPPORTED: UInt32 = 2097152
PDCAP_WAKE_FROM_S2_SUPPORTED: UInt32 = 4194304
PDCAP_WAKE_FROM_S3_SUPPORTED: UInt32 = 8388608
PDCAP_S4_SUPPORTED: UInt32 = 16777216
PDCAP_S5_SUPPORTED: UInt32 = 33554432
THERMAL_EVENT_VERSION: UInt32 = 1
@winfunctype('POWRPROF.dll')
def CallNtPowerInformation(InformationLevel: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL, InputBuffer: VoidPtr, InputBufferLength: UInt32, OutputBuffer: VoidPtr, OutputBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('POWRPROF.dll')
def GetPwrCapabilities(lpspc: POINTER(win32more.Windows.Win32.System.Power.SYSTEM_POWER_CAPABILITIES)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def PowerDeterminePlatformRoleEx(Version: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE_VERSION) -> win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE: ...
@winfunctype('POWRPROF.dll')
def PowerRegisterSuspendResumeNotification(Flags: win32more.Windows.Win32.UI.WindowsAndMessaging.REGISTER_NOTIFICATION_FLAGS, Recipient: win32more.Windows.Win32.Foundation.HANDLE, RegistrationHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerUnregisterSuspendResumeNotification(RegistrationHandle: win32more.Windows.Win32.System.Power.HPOWERNOTIFY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadACValue(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Type: POINTER(UInt32), Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadDCValue(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Type: POINTER(UInt32), Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteACValueIndex(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), AcValueIndex: UInt32) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerWriteDCValueIndex(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), DcValueIndex: UInt32) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerGetActiveScheme(UserRootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, ActivePolicyGuid: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerSetActiveScheme(UserRootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerSettingRegisterNotification(SettingGuid: POINTER(Guid), Flags: win32more.Windows.Win32.UI.WindowsAndMessaging.REGISTER_NOTIFICATION_FLAGS, Recipient: win32more.Windows.Win32.Foundation.HANDLE, RegistrationHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerSettingUnregisterNotification(RegistrationHandle: win32more.Windows.Win32.System.Power.HPOWERNOTIFY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerRegisterForEffectivePowerModeNotifications(Version: UInt32, Callback: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE_CALLBACK, Context: VoidPtr, RegistrationHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('POWRPROF.dll')
def PowerUnregisterFromEffectivePowerModeNotifications(RegistrationHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('POWRPROF.dll')
def GetPwrDiskSpindownRange(puiMax: POINTER(UInt32), puiMin: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def EnumPwrSchemes(lpfn: win32more.Windows.Win32.System.Power.PWRSCHEMESENUMPROC, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def ReadGlobalPwrPolicy(pGlobalPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.GLOBAL_POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def ReadPwrScheme(uiID: UInt32, pPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def WritePwrScheme(puiID: POINTER(UInt32), lpszSchemeName: win32more.Windows.Win32.Foundation.PWSTR, lpszDescription: win32more.Windows.Win32.Foundation.PWSTR, lpScheme: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def WriteGlobalPwrPolicy(pGlobalPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.GLOBAL_POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def DeletePwrScheme(uiID: UInt32) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def GetActivePwrScheme(puiID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def SetActivePwrScheme(uiID: UInt32, pGlobalPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.GLOBAL_POWER_POLICY), pPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def IsPwrSuspendAllowed() -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def IsPwrHibernateAllowed() -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def IsPwrShutdownAllowed() -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def IsAdminOverrideActive(papp: POINTER(win32more.Windows.Win32.System.Power.ADMINISTRATOR_POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def SetSuspendState(bHibernate: win32more.Windows.Win32.Foundation.BOOLEAN, bForce: win32more.Windows.Win32.Foundation.BOOLEAN, bWakeupEventsDisabled: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def GetCurrentPowerPolicies(pGlobalPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.GLOBAL_POWER_POLICY), pPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def CanUserWritePwrScheme() -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def ReadProcessorPwrScheme(uiID: UInt32, pMachineProcessorPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.MACHINE_PROCESSOR_POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def WriteProcessorPwrScheme(uiID: UInt32, pMachineProcessorPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.MACHINE_PROCESSOR_POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def ValidatePowerPolicies(pGlobalPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.GLOBAL_POWER_POLICY), pPowerPolicy: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def PowerIsSettingRangeDefined(SubKeyGuid: POINTER(Guid), SettingGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def PowerSettingAccessCheckEx(AccessFlags: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR, PowerGuid: POINTER(Guid), AccessType: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerSettingAccessCheck(AccessFlags: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR, PowerGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadACValueIndex(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), AcValueIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerReadDCValueIndex(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), DcValueIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerReadFriendlyName(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadDescription(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadPossibleValue(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Type: POINTER(UInt32), PossibleSettingIndex: UInt32, Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadPossibleFriendlyName(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), PossibleSettingIndex: UInt32, Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadPossibleDescription(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), PossibleSettingIndex: UInt32, Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadValueMin(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), ValueMinimum: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadValueMax(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), ValueMaximum: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadValueIncrement(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), ValueIncrement: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadValueUnitsSpecifier(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadACDefaultIndex(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemePersonalityGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), AcDefaultIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerReadDCDefaultIndex(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemePersonalityGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), DcDefaultIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerReadIconResourceSpecifier(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReadSettingAttributes(SubGroupGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid)) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerWriteFriendlyName(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteDescription(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWritePossibleValue(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Type: UInt32, PossibleSettingIndex: UInt32, Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWritePossibleFriendlyName(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), PossibleSettingIndex: UInt32, Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWritePossibleDescription(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), PossibleSettingIndex: UInt32, Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteValueMin(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), ValueMinimum: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteValueMax(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), ValueMaximum: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteValueIncrement(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), ValueIncrement: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteValueUnitsSpecifier(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteACDefaultIndex(RootSystemPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemePersonalityGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), DefaultAcIndex: UInt32) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerWriteDCDefaultIndex(RootSystemPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemePersonalityGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), DefaultDcIndex: UInt32) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerWriteIconResourceSpecifier(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerWriteSettingAttributes(SubGroupGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), Attributes: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerDuplicateScheme(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SourceSchemeGuid: POINTER(Guid), DestinationSchemeGuid: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerImportPowerScheme(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, ImportFileNamePath: win32more.Windows.Win32.Foundation.PWSTR, DestinationSchemeGuid: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerDeleteScheme(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerRemovePowerSetting(PowerSettingSubKeyGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerCreateSetting(RootSystemPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerCreatePossibleSetting(RootSystemPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SubGroupOfPowerSettingsGuid: POINTER(Guid), PowerSettingGuid: POINTER(Guid), PossibleSettingIndex: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerEnumerate(RootPowerKey: win32more.Windows.Win32.System.Registry.HKEY, SchemeGuid: POINTER(Guid), SubGroupOfPowerSettingsGuid: POINTER(Guid), AccessFlags: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR, Index: UInt32, Buffer: POINTER(Byte), BufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerOpenUserPowerKey(phUserPowerKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY), Access: UInt32, OpenExisting: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerOpenSystemPowerKey(phSystemPowerKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY), Access: UInt32, OpenExisting: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerCanRestoreIndividualDefaultPowerScheme(SchemeGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerRestoreIndividualDefaultPowerScheme(SchemeGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerRestoreDefaultPowerSchemes() -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('POWRPROF.dll')
def PowerReplaceDefaultPowerSchemes() -> UInt32: ...
@winfunctype('POWRPROF.dll')
def PowerDeterminePlatformRole() -> win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE: ...
@winfunctype('POWRPROF.dll')
def DevicePowerEnumDevices(QueryIndex: UInt32, QueryInterpretationFlags: UInt32, QueryFlags: UInt32, pReturnBuffer: POINTER(Byte), pBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def DevicePowerSetDeviceState(DeviceDescription: win32more.Windows.Win32.Foundation.PWSTR, SetFlags: UInt32, SetData: VoidPtr) -> UInt32: ...
@winfunctype('POWRPROF.dll')
def DevicePowerOpen(DebugMask: UInt32) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def DevicePowerClose() -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('POWRPROF.dll')
def PowerReportThermalEvent(Event: POINTER(win32more.Windows.Win32.System.Power.THERMAL_EVENT)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('USER32.dll')
def RegisterPowerSettingNotification(hRecipient: win32more.Windows.Win32.Foundation.HANDLE, PowerSettingGuid: POINTER(Guid), Flags: UInt32) -> win32more.Windows.Win32.System.Power.HPOWERNOTIFY: ...
@winfunctype('USER32.dll')
def UnregisterPowerSettingNotification(Handle: win32more.Windows.Win32.System.Power.HPOWERNOTIFY) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterSuspendResumeNotification(hRecipient: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.UI.WindowsAndMessaging.REGISTER_NOTIFICATION_FLAGS) -> win32more.Windows.Win32.System.Power.HPOWERNOTIFY: ...
@winfunctype('USER32.dll')
def UnregisterSuspendResumeNotification(Handle: win32more.Windows.Win32.System.Power.HPOWERNOTIFY) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RequestWakeupLatency(latency: win32more.Windows.Win32.System.Power.LATENCY_TIME) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsSystemResumeAutomatic() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetThreadExecutionState(esFlags: win32more.Windows.Win32.System.Power.EXECUTION_STATE) -> win32more.Windows.Win32.System.Power.EXECUTION_STATE: ...
@winfunctype('KERNEL32.dll')
def PowerCreateRequest(Context: POINTER(win32more.Windows.Win32.System.Threading.REASON_CONTEXT)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def PowerSetRequest(PowerRequest: win32more.Windows.Win32.Foundation.HANDLE, RequestType: win32more.Windows.Win32.System.Power.POWER_REQUEST_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PowerClearRequest(PowerRequest: win32more.Windows.Win32.Foundation.HANDLE, RequestType: win32more.Windows.Win32.System.Power.POWER_REQUEST_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDevicePowerState(hDevice: win32more.Windows.Win32.Foundation.HANDLE, pfOn: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetSystemPowerState(fSuspend: win32more.Windows.Win32.Foundation.BOOL, fForce: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemPowerStatus(lpSystemPowerStatus: POINTER(win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATUS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class BATTERY_CHARGER_STATUS(EasyCastStructure):
    Type: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE
    VaData: UInt32 * 1
class BATTERY_CHARGING_SOURCE(EasyCastStructure):
    Type: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE
    MaxCurrent: UInt32
class BATTERY_CHARGING_SOURCE_INFORMATION(EasyCastStructure):
    Type: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE
    SourceOnline: win32more.Windows.Win32.Foundation.BOOLEAN
BATTERY_CHARGING_SOURCE_TYPE = Int32
BatteryChargingSourceType_AC: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE = 1
BatteryChargingSourceType_USB: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE = 2
BatteryChargingSourceType_Wireless: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE = 3
BatteryChargingSourceType_Max: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE = 4
class BATTERY_INFORMATION(EasyCastStructure):
    Capabilities: UInt32
    Technology: Byte
    Reserved: Byte * 3
    Chemistry: Byte * 4
    DesignedCapacity: UInt32
    FullChargedCapacity: UInt32
    DefaultAlert1: UInt32
    DefaultAlert2: UInt32
    CriticalBias: UInt32
    CycleCount: UInt32
class BATTERY_MANUFACTURE_DATE(EasyCastStructure):
    Day: Byte
    Month: Byte
    Year: UInt16
class BATTERY_QUERY_INFORMATION(EasyCastStructure):
    BatteryTag: UInt32
    InformationLevel: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL
    AtRate: UInt32
BATTERY_QUERY_INFORMATION_LEVEL = Int32
BATTERY_QUERY_INFORMATION_LEVEL_BatteryInformation: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 0
BATTERY_QUERY_INFORMATION_LEVEL_BatteryGranularityInformation: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 1
BATTERY_QUERY_INFORMATION_LEVEL_BatteryTemperature: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 2
BATTERY_QUERY_INFORMATION_LEVEL_BatteryEstimatedTime: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 3
BATTERY_QUERY_INFORMATION_LEVEL_BatteryDeviceName: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 4
BATTERY_QUERY_INFORMATION_LEVEL_BatteryManufactureDate: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 5
BATTERY_QUERY_INFORMATION_LEVEL_BatteryManufactureName: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 6
BATTERY_QUERY_INFORMATION_LEVEL_BatteryUniqueID: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 7
BATTERY_QUERY_INFORMATION_LEVEL_BatterySerialNumber: win32more.Windows.Win32.System.Power.BATTERY_QUERY_INFORMATION_LEVEL = 8
class BATTERY_REPORTING_SCALE(EasyCastStructure):
    Granularity: UInt32
    Capacity: UInt32
class BATTERY_SET_INFORMATION(EasyCastStructure):
    BatteryTag: UInt32
    InformationLevel: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL
    Buffer: Byte * 1
BATTERY_SET_INFORMATION_LEVEL = Int32
BATTERY_SET_INFORMATION_LEVEL_BatteryCriticalBias: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL = 0
BATTERY_SET_INFORMATION_LEVEL_BatteryCharge: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL = 1
BATTERY_SET_INFORMATION_LEVEL_BatteryDischarge: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL = 2
BATTERY_SET_INFORMATION_LEVEL_BatteryChargingSource: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL = 3
BATTERY_SET_INFORMATION_LEVEL_BatteryChargerId: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL = 4
BATTERY_SET_INFORMATION_LEVEL_BatteryChargerStatus: win32more.Windows.Win32.System.Power.BATTERY_SET_INFORMATION_LEVEL = 5
class BATTERY_STATUS(EasyCastStructure):
    PowerState: UInt32
    Capacity: UInt32
    Voltage: UInt32
    Rate: Int32
class BATTERY_USB_CHARGER_STATUS(EasyCastStructure):
    Type: win32more.Windows.Win32.System.Power.BATTERY_CHARGING_SOURCE_TYPE
    Reserved: UInt32
    Flags: UInt32
    MaxCurrent: UInt32
    Voltage: UInt32
    PortType: win32more.Windows.Win32.System.Power.USB_CHARGER_PORT
    PortId: UInt64
    PowerSourceInformation: VoidPtr
    OemCharger: Guid
class BATTERY_WAIT_STATUS(EasyCastStructure):
    BatteryTag: UInt32
    Timeout: UInt32
    PowerState: UInt32
    LowCapacity: UInt32
    HighCapacity: UInt32
class CM_POWER_DATA(EasyCastStructure):
    PD_Size: UInt32
    PD_MostRecentPowerState: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE
    PD_Capabilities: UInt32
    PD_D1Latency: UInt32
    PD_D2Latency: UInt32
    PD_D3Latency: UInt32
    PD_PowerStateMapping: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE * 7
    PD_DeepestSystemWake: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
class DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS(EasyCastStructure):
    Callback: win32more.Windows.Win32.System.Power.PDEVICE_NOTIFY_CALLBACK_ROUTINE
    Context: VoidPtr
DEVICE_POWER_STATE = Int32
DEVICE_POWER_STATE_PowerDeviceUnspecified: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE = 0
DEVICE_POWER_STATE_PowerDeviceD0: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE = 1
DEVICE_POWER_STATE_PowerDeviceD1: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE = 2
DEVICE_POWER_STATE_PowerDeviceD2: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE = 3
DEVICE_POWER_STATE_PowerDeviceD3: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE = 4
DEVICE_POWER_STATE_PowerDeviceMaximum: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE = 5
EFFECTIVE_POWER_MODE = Int32
EFFECTIVE_POWER_MODE_EffectivePowerModeBatterySaver: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 0
EFFECTIVE_POWER_MODE_EffectivePowerModeBetterBattery: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 1
EFFECTIVE_POWER_MODE_EffectivePowerModeBalanced: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 2
EFFECTIVE_POWER_MODE_EffectivePowerModeHighPerformance: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 3
EFFECTIVE_POWER_MODE_EffectivePowerModeMaxPerformance: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 4
EFFECTIVE_POWER_MODE_EffectivePowerModeGameMode: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 5
EFFECTIVE_POWER_MODE_EffectivePowerModeMixedReality: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE = 6
@winfunctype_pointer
def EFFECTIVE_POWER_MODE_CALLBACK(Mode: win32more.Windows.Win32.System.Power.EFFECTIVE_POWER_MODE, Context: VoidPtr) -> Void: ...
class EMI_CHANNEL_MEASUREMENT_DATA(EasyCastStructure):
    AbsoluteEnergy: UInt64
    AbsoluteTime: UInt64
class EMI_CHANNEL_V2(EasyCastStructure):
    MeasurementUnit: win32more.Windows.Win32.System.Power.EMI_MEASUREMENT_UNIT
    ChannelNameSize: UInt16
    ChannelName: Char * 1
class EMI_MEASUREMENT_DATA_V2(EasyCastStructure):
    ChannelData: win32more.Windows.Win32.System.Power.EMI_CHANNEL_MEASUREMENT_DATA * 1
EMI_MEASUREMENT_UNIT = Int32
EMI_MEASUREMENT_UNIT_EmiMeasurementUnitPicowattHours: win32more.Windows.Win32.System.Power.EMI_MEASUREMENT_UNIT = 0
class EMI_METADATA_SIZE(EasyCastStructure):
    MetadataSize: UInt32
class EMI_METADATA_V1(EasyCastStructure):
    MeasurementUnit: win32more.Windows.Win32.System.Power.EMI_MEASUREMENT_UNIT
    HardwareOEM: Char * 16
    HardwareModel: Char * 16
    HardwareRevision: UInt16
    MeteredHardwareNameSize: UInt16
    MeteredHardwareName: Char * 1
class EMI_METADATA_V2(EasyCastStructure):
    HardwareOEM: Char * 16
    HardwareModel: Char * 16
    HardwareRevision: UInt16
    ChannelCount: UInt16
    Channels: win32more.Windows.Win32.System.Power.EMI_CHANNEL_V2 * 1
class EMI_VERSION(EasyCastStructure):
    EmiVersion: UInt16
EXECUTION_STATE = UInt32
ES_AWAYMODE_REQUIRED: win32more.Windows.Win32.System.Power.EXECUTION_STATE = 64
ES_CONTINUOUS: win32more.Windows.Win32.System.Power.EXECUTION_STATE = 2147483648
ES_DISPLAY_REQUIRED: win32more.Windows.Win32.System.Power.EXECUTION_STATE = 2
ES_SYSTEM_REQUIRED: win32more.Windows.Win32.System.Power.EXECUTION_STATE = 1
ES_USER_PRESENT: win32more.Windows.Win32.System.Power.EXECUTION_STATE = 4
class GLOBAL_MACHINE_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    LidOpenWakeAc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    LidOpenWakeDc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    BroadcastCapacityResolution: UInt32
class GLOBAL_POWER_POLICY(EasyCastStructure):
    user: win32more.Windows.Win32.System.Power.GLOBAL_USER_POWER_POLICY
    mach: win32more.Windows.Win32.System.Power.GLOBAL_MACHINE_POWER_POLICY
class GLOBAL_USER_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    PowerButtonAc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    PowerButtonDc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    SleepButtonAc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    SleepButtonDc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    LidCloseAc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    LidCloseDc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    DischargePolicy: win32more.Windows.Win32.System.Power.SYSTEM_POWER_LEVEL * 4
    GlobalFlags: UInt32
HPOWERNOTIFY = IntPtr
LATENCY_TIME = Int32
LT_DONT_CARE: win32more.Windows.Win32.System.Power.LATENCY_TIME = 0
LT_LOWEST_LATENCY: win32more.Windows.Win32.System.Power.LATENCY_TIME = 1
class MACHINE_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    MinSleepAc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    MinSleepDc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    ReducedLatencySleepAc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    ReducedLatencySleepDc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    DozeTimeoutAc: UInt32
    DozeTimeoutDc: UInt32
    DozeS4TimeoutAc: UInt32
    DozeS4TimeoutDc: UInt32
    MinThrottleAc: Byte
    MinThrottleDc: Byte
    pad1: Byte * 2
    OverThrottledAc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    OverThrottledDc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
class MACHINE_PROCESSOR_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    ProcessorPolicyAc: win32more.Windows.Win32.System.Power.PROCESSOR_POWER_POLICY
    ProcessorPolicyDc: win32more.Windows.Win32.System.Power.PROCESSOR_POWER_POLICY
@winfunctype_pointer
def PDEVICE_NOTIFY_CALLBACK_ROUTINE(Context: VoidPtr, Type: UInt32, Setting: VoidPtr) -> UInt32: ...
class POWERBROADCAST_SETTING(EasyCastStructure):
    PowerSetting: Guid
    DataLength: UInt32
    Data: Byte * 1
POWER_ACTION = Int32
POWER_ACTION_PowerActionNone: win32more.Windows.Win32.System.Power.POWER_ACTION = 0
POWER_ACTION_PowerActionReserved: win32more.Windows.Win32.System.Power.POWER_ACTION = 1
POWER_ACTION_PowerActionSleep: win32more.Windows.Win32.System.Power.POWER_ACTION = 2
POWER_ACTION_PowerActionHibernate: win32more.Windows.Win32.System.Power.POWER_ACTION = 3
POWER_ACTION_PowerActionShutdown: win32more.Windows.Win32.System.Power.POWER_ACTION = 4
POWER_ACTION_PowerActionShutdownReset: win32more.Windows.Win32.System.Power.POWER_ACTION = 5
POWER_ACTION_PowerActionShutdownOff: win32more.Windows.Win32.System.Power.POWER_ACTION = 6
POWER_ACTION_PowerActionWarmEject: win32more.Windows.Win32.System.Power.POWER_ACTION = 7
POWER_ACTION_PowerActionDisplayOff: win32more.Windows.Win32.System.Power.POWER_ACTION = 8
class POWER_ACTION_POLICY(EasyCastStructure):
    Action: win32more.Windows.Win32.System.Power.POWER_ACTION
    Flags: UInt32
    EventCode: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE
POWER_ACTION_POLICY_EVENT_CODE = UInt32
POWER_FORCE_TRIGGER_RESET: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE = 2147483648
POWER_LEVEL_USER_NOTIFY_EXEC: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE = 4
POWER_LEVEL_USER_NOTIFY_SOUND: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE = 2
POWER_LEVEL_USER_NOTIFY_TEXT: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE = 1
POWER_USER_NOTIFY_BUTTON: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE = 8
POWER_USER_NOTIFY_SHUTDOWN: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY_EVENT_CODE = 16
POWER_COOLING_MODE = UInt16
PO_TZ_ACTIVE: win32more.Windows.Win32.System.Power.POWER_COOLING_MODE = 0
PO_TZ_PASSIVE: win32more.Windows.Win32.System.Power.POWER_COOLING_MODE = 1
PO_TZ_INVALID_MODE: win32more.Windows.Win32.System.Power.POWER_COOLING_MODE = 2
POWER_DATA_ACCESSOR = Int32
ACCESS_AC_POWER_SETTING_INDEX: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 0
ACCESS_DC_POWER_SETTING_INDEX: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 1
ACCESS_FRIENDLY_NAME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 2
ACCESS_DESCRIPTION: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 3
ACCESS_POSSIBLE_POWER_SETTING: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 4
ACCESS_POSSIBLE_POWER_SETTING_FRIENDLY_NAME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 5
ACCESS_POSSIBLE_POWER_SETTING_DESCRIPTION: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 6
ACCESS_DEFAULT_AC_POWER_SETTING: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 7
ACCESS_DEFAULT_DC_POWER_SETTING: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 8
ACCESS_POSSIBLE_VALUE_MIN: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 9
ACCESS_POSSIBLE_VALUE_MAX: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 10
ACCESS_POSSIBLE_VALUE_INCREMENT: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 11
ACCESS_POSSIBLE_VALUE_UNITS: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 12
ACCESS_ICON_RESOURCE: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 13
ACCESS_DEFAULT_SECURITY_DESCRIPTOR: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 14
ACCESS_ATTRIBUTES: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 15
ACCESS_SCHEME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 16
ACCESS_SUBGROUP: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 17
ACCESS_INDIVIDUAL_SETTING: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 18
ACCESS_ACTIVE_SCHEME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 19
ACCESS_CREATE_SCHEME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 20
ACCESS_AC_POWER_SETTING_MAX: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 21
ACCESS_DC_POWER_SETTING_MAX: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 22
ACCESS_AC_POWER_SETTING_MIN: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 23
ACCESS_DC_POWER_SETTING_MIN: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 24
ACCESS_PROFILE: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 25
ACCESS_OVERLAY_SCHEME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 26
ACCESS_ACTIVE_OVERLAY_SCHEME: win32more.Windows.Win32.System.Power.POWER_DATA_ACCESSOR = 27
class POWER_IDLE_RESILIENCY(EasyCastStructure):
    CoalescingTimeout: UInt32
    IdleResiliencyPeriod: UInt32
POWER_INFORMATION_LEVEL = Int32
POWER_INFORMATION_LEVEL_SystemPowerPolicyAc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 0
POWER_INFORMATION_LEVEL_SystemPowerPolicyDc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 1
POWER_INFORMATION_LEVEL_VerifySystemPolicyAc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 2
POWER_INFORMATION_LEVEL_VerifySystemPolicyDc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 3
POWER_INFORMATION_LEVEL_SystemPowerCapabilities: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 4
POWER_INFORMATION_LEVEL_SystemBatteryState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 5
POWER_INFORMATION_LEVEL_SystemPowerStateHandler: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 6
POWER_INFORMATION_LEVEL_ProcessorStateHandler: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 7
POWER_INFORMATION_LEVEL_SystemPowerPolicyCurrent: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 8
POWER_INFORMATION_LEVEL_AdministratorPowerPolicy: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 9
POWER_INFORMATION_LEVEL_SystemReserveHiberFile: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 10
POWER_INFORMATION_LEVEL_ProcessorInformation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 11
POWER_INFORMATION_LEVEL_SystemPowerInformation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 12
POWER_INFORMATION_LEVEL_ProcessorStateHandler2: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 13
POWER_INFORMATION_LEVEL_LastWakeTime: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 14
POWER_INFORMATION_LEVEL_LastSleepTime: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 15
POWER_INFORMATION_LEVEL_SystemExecutionState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 16
POWER_INFORMATION_LEVEL_SystemPowerStateNotifyHandler: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 17
POWER_INFORMATION_LEVEL_ProcessorPowerPolicyAc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 18
POWER_INFORMATION_LEVEL_ProcessorPowerPolicyDc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 19
POWER_INFORMATION_LEVEL_VerifyProcessorPowerPolicyAc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 20
POWER_INFORMATION_LEVEL_VerifyProcessorPowerPolicyDc: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 21
POWER_INFORMATION_LEVEL_ProcessorPowerPolicyCurrent: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 22
POWER_INFORMATION_LEVEL_SystemPowerStateLogging: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 23
POWER_INFORMATION_LEVEL_SystemPowerLoggingEntry: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 24
POWER_INFORMATION_LEVEL_SetPowerSettingValue: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 25
POWER_INFORMATION_LEVEL_NotifyUserPowerSetting: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 26
POWER_INFORMATION_LEVEL_PowerInformationLevelUnused0: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 27
POWER_INFORMATION_LEVEL_SystemMonitorHiberBootPowerOff: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 28
POWER_INFORMATION_LEVEL_SystemVideoState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 29
POWER_INFORMATION_LEVEL_TraceApplicationPowerMessage: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 30
POWER_INFORMATION_LEVEL_TraceApplicationPowerMessageEnd: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 31
POWER_INFORMATION_LEVEL_ProcessorPerfStates: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 32
POWER_INFORMATION_LEVEL_ProcessorIdleStates: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 33
POWER_INFORMATION_LEVEL_ProcessorCap: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 34
POWER_INFORMATION_LEVEL_SystemWakeSource: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 35
POWER_INFORMATION_LEVEL_SystemHiberFileInformation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 36
POWER_INFORMATION_LEVEL_TraceServicePowerMessage: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 37
POWER_INFORMATION_LEVEL_ProcessorLoad: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 38
POWER_INFORMATION_LEVEL_PowerShutdownNotification: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 39
POWER_INFORMATION_LEVEL_MonitorCapabilities: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 40
POWER_INFORMATION_LEVEL_SessionPowerInit: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 41
POWER_INFORMATION_LEVEL_SessionDisplayState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 42
POWER_INFORMATION_LEVEL_PowerRequestCreate: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 43
POWER_INFORMATION_LEVEL_PowerRequestAction: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 44
POWER_INFORMATION_LEVEL_GetPowerRequestList: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 45
POWER_INFORMATION_LEVEL_ProcessorInformationEx: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 46
POWER_INFORMATION_LEVEL_NotifyUserModeLegacyPowerEvent: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 47
POWER_INFORMATION_LEVEL_GroupPark: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 48
POWER_INFORMATION_LEVEL_ProcessorIdleDomains: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 49
POWER_INFORMATION_LEVEL_WakeTimerList: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 50
POWER_INFORMATION_LEVEL_SystemHiberFileSize: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 51
POWER_INFORMATION_LEVEL_ProcessorIdleStatesHv: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 52
POWER_INFORMATION_LEVEL_ProcessorPerfStatesHv: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 53
POWER_INFORMATION_LEVEL_ProcessorPerfCapHv: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 54
POWER_INFORMATION_LEVEL_ProcessorSetIdle: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 55
POWER_INFORMATION_LEVEL_LogicalProcessorIdling: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 56
POWER_INFORMATION_LEVEL_UserPresence: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 57
POWER_INFORMATION_LEVEL_PowerSettingNotificationName: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 58
POWER_INFORMATION_LEVEL_GetPowerSettingValue: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 59
POWER_INFORMATION_LEVEL_IdleResiliency: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 60
POWER_INFORMATION_LEVEL_SessionRITState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 61
POWER_INFORMATION_LEVEL_SessionConnectNotification: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 62
POWER_INFORMATION_LEVEL_SessionPowerCleanup: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 63
POWER_INFORMATION_LEVEL_SessionLockState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 64
POWER_INFORMATION_LEVEL_SystemHiberbootState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 65
POWER_INFORMATION_LEVEL_PlatformInformation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 66
POWER_INFORMATION_LEVEL_PdcInvocation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 67
POWER_INFORMATION_LEVEL_MonitorInvocation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 68
POWER_INFORMATION_LEVEL_FirmwareTableInformationRegistered: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 69
POWER_INFORMATION_LEVEL_SetShutdownSelectedTime: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 70
POWER_INFORMATION_LEVEL_SuspendResumeInvocation: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 71
POWER_INFORMATION_LEVEL_PlmPowerRequestCreate: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 72
POWER_INFORMATION_LEVEL_ScreenOff: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 73
POWER_INFORMATION_LEVEL_CsDeviceNotification: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 74
POWER_INFORMATION_LEVEL_PlatformRole: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 75
POWER_INFORMATION_LEVEL_LastResumePerformance: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 76
POWER_INFORMATION_LEVEL_DisplayBurst: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 77
POWER_INFORMATION_LEVEL_ExitLatencySamplingPercentage: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 78
POWER_INFORMATION_LEVEL_RegisterSpmPowerSettings: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 79
POWER_INFORMATION_LEVEL_PlatformIdleStates: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 80
POWER_INFORMATION_LEVEL_ProcessorIdleVeto: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 81
POWER_INFORMATION_LEVEL_PlatformIdleVeto: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 82
POWER_INFORMATION_LEVEL_SystemBatteryStatePrecise: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 83
POWER_INFORMATION_LEVEL_ThermalEvent: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 84
POWER_INFORMATION_LEVEL_PowerRequestActionInternal: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 85
POWER_INFORMATION_LEVEL_BatteryDeviceState: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 86
POWER_INFORMATION_LEVEL_PowerInformationInternal: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 87
POWER_INFORMATION_LEVEL_ThermalStandby: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 88
POWER_INFORMATION_LEVEL_SystemHiberFileType: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 89
POWER_INFORMATION_LEVEL_PhysicalPowerButtonPress: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 90
POWER_INFORMATION_LEVEL_QueryPotentialDripsConstraint: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 91
POWER_INFORMATION_LEVEL_EnergyTrackerCreate: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 92
POWER_INFORMATION_LEVEL_EnergyTrackerQuery: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 93
POWER_INFORMATION_LEVEL_UpdateBlackBoxRecorder: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 94
POWER_INFORMATION_LEVEL_SessionAllowExternalDmaDevices: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 95
POWER_INFORMATION_LEVEL_SendSuspendResumeNotification: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 96
POWER_INFORMATION_LEVEL_BlackBoxRecorderDirectAccessBuffer: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 97
POWER_INFORMATION_LEVEL_PowerInformationLevelMaximum: win32more.Windows.Win32.System.Power.POWER_INFORMATION_LEVEL = 98
class POWER_MONITOR_INVOCATION(EasyCastStructure):
    Console: win32more.Windows.Win32.Foundation.BOOLEAN
    RequestReason: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON
POWER_MONITOR_REQUEST_REASON = Int32
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUnknown: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 0
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPowerButton: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 1
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonRemoteConnection: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 2
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonScMonitorpower: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 3
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInput: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 4
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonAcDcDisplayBurst: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 5
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserDisplayBurst: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 6
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPoSetSystemState: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 7
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonSetThreadExecutionState: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 8
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonFullWake: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 9
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonSessionUnlock: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 10
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonScreenOffRequest: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 11
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonIdleTimeout: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 12
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPolicyChange: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 13
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonSleepButton: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 14
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonLid: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 15
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonBatteryCountChange: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 16
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonGracePeriod: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 17
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPnP: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 18
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonDP: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 19
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonSxTransition: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 20
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonSystemIdle: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 21
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonNearProximity: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 22
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonThermalStandby: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 23
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonResumePdc: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 24
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonResumeS4: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 25
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonTerminal: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 26
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignal: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 27
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonAcDcDisplayBurstSuppressed: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 28
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonSystemStateEntered: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 29
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonWinrt: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 30
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputKeyboard: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 31
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputMouse: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 32
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputTouchpad: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 33
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputPen: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 34
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputAccelerometer: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 35
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputHid: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 36
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputPoUserPresent: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 37
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputSessionSwitch: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 38
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputInitialization: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 39
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignalWindowsMobilePwrNotif: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 40
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignalWindowsMobileShell: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 41
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignalHeyCortana: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 42
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignalHolographicShell: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 43
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignalFingerprint: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 44
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonDirectedDrips: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 45
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonDim: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 46
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonBuiltinPanel: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 47
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonDisplayRequiredUnDim: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 48
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonBatteryCountChangeSuppressed: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 49
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonResumeModernStandby: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 50
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonTerminalInit: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 51
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonPdcSignalSensorsHumanPresence: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 52
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonBatteryPreCritical: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 53
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonUserInputTouch: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 54
POWER_MONITOR_REQUEST_REASON_MonitorRequestReasonMax: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_REASON = 55
POWER_MONITOR_REQUEST_TYPE = Int32
POWER_MONITOR_REQUEST_TYPE_MonitorRequestTypeOff: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_TYPE = 0
POWER_MONITOR_REQUEST_TYPE_MonitorRequestTypeOnAndPresent: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_TYPE = 1
POWER_MONITOR_REQUEST_TYPE_MonitorRequestTypeToggleOn: win32more.Windows.Win32.System.Power.POWER_MONITOR_REQUEST_TYPE = 2
class POWER_PLATFORM_INFORMATION(EasyCastStructure):
    AoAc: win32more.Windows.Win32.Foundation.BOOLEAN
POWER_PLATFORM_ROLE = Int32
POWER_PLATFORM_ROLE_PlatformRoleUnspecified: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 0
POWER_PLATFORM_ROLE_PlatformRoleDesktop: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 1
POWER_PLATFORM_ROLE_PlatformRoleMobile: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 2
POWER_PLATFORM_ROLE_PlatformRoleWorkstation: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 3
POWER_PLATFORM_ROLE_PlatformRoleEnterpriseServer: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 4
POWER_PLATFORM_ROLE_PlatformRoleSOHOServer: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 5
POWER_PLATFORM_ROLE_PlatformRoleAppliancePC: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 6
POWER_PLATFORM_ROLE_PlatformRolePerformanceServer: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 7
POWER_PLATFORM_ROLE_PlatformRoleSlate: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 8
POWER_PLATFORM_ROLE_PlatformRoleMaximum: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE = 9
POWER_PLATFORM_ROLE_VERSION = UInt32
POWER_PLATFORM_ROLE_V1: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE_VERSION = 1
POWER_PLATFORM_ROLE_V2: win32more.Windows.Win32.System.Power.POWER_PLATFORM_ROLE_VERSION = 2
class POWER_POLICY(EasyCastStructure):
    user: win32more.Windows.Win32.System.Power.USER_POWER_POLICY
    mach: win32more.Windows.Win32.System.Power.MACHINE_POWER_POLICY
POWER_REQUEST_TYPE = Int32
POWER_REQUEST_TYPE_PowerRequestDisplayRequired: win32more.Windows.Win32.System.Power.POWER_REQUEST_TYPE = 0
POWER_REQUEST_TYPE_PowerRequestSystemRequired: win32more.Windows.Win32.System.Power.POWER_REQUEST_TYPE = 1
POWER_REQUEST_TYPE_PowerRequestAwayModeRequired: win32more.Windows.Win32.System.Power.POWER_REQUEST_TYPE = 2
POWER_REQUEST_TYPE_PowerRequestExecutionRequired: win32more.Windows.Win32.System.Power.POWER_REQUEST_TYPE = 3
class POWER_SESSION_ALLOW_EXTERNAL_DMA_DEVICES(EasyCastStructure):
    IsAllowed: win32more.Windows.Win32.Foundation.BOOLEAN
class POWER_SESSION_CONNECT(EasyCastStructure):
    Connected: win32more.Windows.Win32.Foundation.BOOLEAN
    Console: win32more.Windows.Win32.Foundation.BOOLEAN
class POWER_SESSION_RIT_STATE(EasyCastStructure):
    Active: win32more.Windows.Win32.Foundation.BOOLEAN
    LastInputTime: UInt64
class POWER_SESSION_TIMEOUTS(EasyCastStructure):
    InputTimeout: UInt32
    DisplayTimeout: UInt32
class POWER_SESSION_WINLOGON(EasyCastStructure):
    SessionId: UInt32
    Console: win32more.Windows.Win32.Foundation.BOOLEAN
    Locked: win32more.Windows.Win32.Foundation.BOOLEAN
POWER_SETTING_ALTITUDE = Int32
ALTITUDE_GROUP_POLICY: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 0
ALTITUDE_USER: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 1
ALTITUDE_RUNTIME_OVERRIDE: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 2
ALTITUDE_PROVISIONING: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 3
ALTITUDE_OEM_CUSTOMIZATION: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 4
ALTITUDE_INTERNAL_OVERRIDE: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 5
ALTITUDE_OS_DEFAULT: win32more.Windows.Win32.System.Power.POWER_SETTING_ALTITUDE = 6
class POWER_USER_PRESENCE(EasyCastStructure):
    UserPresence: win32more.Windows.Win32.System.Power.POWER_USER_PRESENCE_TYPE
POWER_USER_PRESENCE_TYPE = Int32
POWER_USER_PRESENCE_TYPE_UserNotPresent: win32more.Windows.Win32.System.Power.POWER_USER_PRESENCE_TYPE = 0
POWER_USER_PRESENCE_TYPE_UserPresent: win32more.Windows.Win32.System.Power.POWER_USER_PRESENCE_TYPE = 1
POWER_USER_PRESENCE_TYPE_UserUnknown: win32more.Windows.Win32.System.Power.POWER_USER_PRESENCE_TYPE = 255
class PPM_IDLESTATE_EVENT(EasyCastStructure):
    NewState: UInt32
    OldState: UInt32
    Processors: UInt64
class PPM_IDLE_ACCOUNTING(EasyCastStructure):
    StateCount: UInt32
    TotalTransitions: UInt32
    ResetCount: UInt32
    StartTime: UInt64
    State: win32more.Windows.Win32.System.Power.PPM_IDLE_STATE_ACCOUNTING * 1
class PPM_IDLE_ACCOUNTING_EX(EasyCastStructure):
    StateCount: UInt32
    TotalTransitions: UInt32
    ResetCount: UInt32
    AbortCount: UInt32
    StartTime: UInt64
    State: win32more.Windows.Win32.System.Power.PPM_IDLE_STATE_ACCOUNTING_EX * 1
class PPM_IDLE_STATE_ACCOUNTING(EasyCastStructure):
    IdleTransitions: UInt32
    FailedTransitions: UInt32
    InvalidBucketIndex: UInt32
    TotalTime: UInt64
    IdleTimeBuckets: UInt32 * 6
class PPM_IDLE_STATE_ACCOUNTING_EX(EasyCastStructure):
    TotalTime: UInt64
    IdleTransitions: UInt32
    FailedTransitions: UInt32
    InvalidBucketIndex: UInt32
    MinTimeUs: UInt32
    MaxTimeUs: UInt32
    CancelledTransitions: UInt32
    IdleTimeBuckets: win32more.Windows.Win32.System.Power.PPM_IDLE_STATE_BUCKET_EX * 16
class PPM_IDLE_STATE_BUCKET_EX(EasyCastStructure):
    TotalTimeUs: UInt64
    MinTimeUs: UInt32
    MaxTimeUs: UInt32
    Count: UInt32
class PPM_PERFSTATE_DOMAIN_EVENT(EasyCastStructure):
    State: UInt32
    Latency: UInt32
    Speed: UInt32
    Processors: UInt64
class PPM_PERFSTATE_EVENT(EasyCastStructure):
    State: UInt32
    Status: UInt32
    Latency: UInt32
    Speed: UInt32
    Processor: UInt32
class PPM_THERMALCHANGE_EVENT(EasyCastStructure):
    ThermalConstraint: UInt32
    Processors: UInt64
class PPM_THERMAL_POLICY_EVENT(EasyCastStructure):
    Mode: Byte
    Processors: UInt64
class PPM_WMI_IDLE_STATE(EasyCastStructure):
    Latency: UInt32
    Power: UInt32
    TimeCheck: UInt32
    PromotePercent: Byte
    DemotePercent: Byte
    StateType: Byte
    Reserved: Byte
    StateFlags: UInt32
    Context: UInt32
    IdleHandler: UInt32
    Reserved1: UInt32
class PPM_WMI_IDLE_STATES(EasyCastStructure):
    Type: UInt32
    Count: UInt32
    TargetState: UInt32
    OldState: UInt32
    TargetProcessors: UInt64
    State: win32more.Windows.Win32.System.Power.PPM_WMI_IDLE_STATE * 1
class PPM_WMI_IDLE_STATES_EX(EasyCastStructure):
    Type: UInt32
    Count: UInt32
    TargetState: UInt32
    OldState: UInt32
    TargetProcessors: VoidPtr
    State: win32more.Windows.Win32.System.Power.PPM_WMI_IDLE_STATE * 1
class PPM_WMI_LEGACY_PERFSTATE(EasyCastStructure):
    Frequency: UInt32
    Flags: UInt32
    PercentFrequency: UInt32
class PPM_WMI_PERF_STATE(EasyCastStructure):
    Frequency: UInt32
    Power: UInt32
    PercentFrequency: Byte
    IncreaseLevel: Byte
    DecreaseLevel: Byte
    Type: Byte
    IncreaseTime: UInt32
    DecreaseTime: UInt32
    Control: UInt64
    Status: UInt64
    HitCount: UInt32
    Reserved1: UInt32
    Reserved2: UInt64
    Reserved3: UInt64
class PPM_WMI_PERF_STATES(EasyCastStructure):
    Count: UInt32
    MaxFrequency: UInt32
    CurrentState: UInt32
    MaxPerfState: UInt32
    MinPerfState: UInt32
    LowestPerfState: UInt32
    ThermalConstraint: UInt32
    BusyAdjThreshold: Byte
    PolicyType: Byte
    Type: Byte
    Reserved: Byte
    TimerInterval: UInt32
    TargetProcessors: UInt64
    PStateHandler: UInt32
    PStateContext: UInt32
    TStateHandler: UInt32
    TStateContext: UInt32
    FeedbackHandler: UInt32
    Reserved1: UInt32
    Reserved2: UInt64
    State: win32more.Windows.Win32.System.Power.PPM_WMI_PERF_STATE * 1
class PPM_WMI_PERF_STATES_EX(EasyCastStructure):
    Count: UInt32
    MaxFrequency: UInt32
    CurrentState: UInt32
    MaxPerfState: UInt32
    MinPerfState: UInt32
    LowestPerfState: UInt32
    ThermalConstraint: UInt32
    BusyAdjThreshold: Byte
    PolicyType: Byte
    Type: Byte
    Reserved: Byte
    TimerInterval: UInt32
    TargetProcessors: VoidPtr
    PStateHandler: UInt32
    PStateContext: UInt32
    TStateHandler: UInt32
    TStateContext: UInt32
    FeedbackHandler: UInt32
    Reserved1: UInt32
    Reserved2: UInt64
    State: win32more.Windows.Win32.System.Power.PPM_WMI_PERF_STATE * 1
class PROCESSOR_OBJECT_INFO(EasyCastStructure):
    PhysicalID: UInt32
    PBlkAddress: UInt32
    PBlkLength: Byte
class PROCESSOR_OBJECT_INFO_EX(EasyCastStructure):
    PhysicalID: UInt32
    PBlkAddress: UInt32
    PBlkLength: Byte
    InitialApicId: UInt32
class PROCESSOR_POWER_INFORMATION(EasyCastStructure):
    Number: UInt32
    MaxMhz: UInt32
    CurrentMhz: UInt32
    MhzLimit: UInt32
    MaxIdleState: UInt32
    CurrentIdleState: UInt32
class PROCESSOR_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    DynamicThrottle: Byte
    Spare: Byte * 3
    _bitfield: UInt32
    PolicyCount: UInt32
    Policy: win32more.Windows.Win32.System.Power.PROCESSOR_POWER_POLICY_INFO * 3
class PROCESSOR_POWER_POLICY_INFO(EasyCastStructure):
    TimeCheck: UInt32
    DemoteLimit: UInt32
    PromoteLimit: UInt32
    DemotePercent: Byte
    PromotePercent: Byte
    Spare: Byte * 2
    _bitfield: UInt32
@winfunctype_pointer
def PWRSCHEMESENUMPROC(Index: UInt32, NameSize: UInt32, Name: win32more.Windows.Win32.Foundation.PWSTR, DescriptionSize: UInt32, Description: win32more.Windows.Win32.Foundation.PWSTR, Policy: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY), Context: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def PWRSCHEMESENUMPROC_V1(Index: UInt32, NameSize: UInt32, Name: POINTER(SByte), DescriptionSize: UInt32, Description: POINTER(SByte), Policy: POINTER(win32more.Windows.Win32.System.Power.POWER_POLICY), Context: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
class RESUME_PERFORMANCE(EasyCastStructure):
    PostTimeMs: UInt32
    TotalResumeTimeMs: UInt64
    ResumeCompleteTimestamp: UInt64
class SET_POWER_SETTING_VALUE(EasyCastStructure):
    Version: UInt32
    Guid: Guid
    PowerCondition: win32more.Windows.Win32.System.Power.SYSTEM_POWER_CONDITION
    DataLength: UInt32
    Data: Byte * 1
class SYSTEM_BATTERY_STATE(EasyCastStructure):
    AcOnLine: win32more.Windows.Win32.Foundation.BOOLEAN
    BatteryPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    Charging: win32more.Windows.Win32.Foundation.BOOLEAN
    Discharging: win32more.Windows.Win32.Foundation.BOOLEAN
    Spare1: win32more.Windows.Win32.Foundation.BOOLEAN * 3
    Tag: Byte
    MaxCapacity: UInt32
    RemainingCapacity: UInt32
    Rate: UInt32
    EstimatedTime: UInt32
    DefaultAlert1: UInt32
    DefaultAlert2: UInt32
class SYSTEM_POWER_CAPABILITIES(EasyCastStructure):
    PowerButtonPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    SleepButtonPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    LidPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    SystemS1: win32more.Windows.Win32.Foundation.BOOLEAN
    SystemS2: win32more.Windows.Win32.Foundation.BOOLEAN
    SystemS3: win32more.Windows.Win32.Foundation.BOOLEAN
    SystemS4: win32more.Windows.Win32.Foundation.BOOLEAN
    SystemS5: win32more.Windows.Win32.Foundation.BOOLEAN
    HiberFilePresent: win32more.Windows.Win32.Foundation.BOOLEAN
    FullWake: win32more.Windows.Win32.Foundation.BOOLEAN
    VideoDimPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    ApmPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    UpsPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    ThermalControl: win32more.Windows.Win32.Foundation.BOOLEAN
    ProcessorThrottle: win32more.Windows.Win32.Foundation.BOOLEAN
    ProcessorMinThrottle: Byte
    ProcessorMaxThrottle: Byte
    FastSystemS4: win32more.Windows.Win32.Foundation.BOOLEAN
    Hiberboot: win32more.Windows.Win32.Foundation.BOOLEAN
    WakeAlarmPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    AoAc: win32more.Windows.Win32.Foundation.BOOLEAN
    DiskSpinDown: win32more.Windows.Win32.Foundation.BOOLEAN
    HiberFileType: Byte
    AoAcConnectivitySupported: win32more.Windows.Win32.Foundation.BOOLEAN
    spare3: Byte * 6
    SystemBatteriesPresent: win32more.Windows.Win32.Foundation.BOOLEAN
    BatteriesAreShortTerm: win32more.Windows.Win32.Foundation.BOOLEAN
    BatteryScale: win32more.Windows.Win32.System.Power.BATTERY_REPORTING_SCALE * 3
    AcOnLineWake: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    SoftLidWake: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    RtcWake: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    MinDeviceWakeState: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    DefaultLowLatencyWake: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
SYSTEM_POWER_CONDITION = Int32
SYSTEM_POWER_CONDITION_PoAc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_CONDITION = 0
SYSTEM_POWER_CONDITION_PoDc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_CONDITION = 1
SYSTEM_POWER_CONDITION_PoHot: win32more.Windows.Win32.System.Power.SYSTEM_POWER_CONDITION = 2
SYSTEM_POWER_CONDITION_PoConditionMaximum: win32more.Windows.Win32.System.Power.SYSTEM_POWER_CONDITION = 3
class SYSTEM_POWER_INFORMATION(EasyCastStructure):
    MaxIdlenessAllowed: UInt32
    Idleness: UInt32
    TimeRemaining: UInt32
    CoolingMode: win32more.Windows.Win32.System.Power.POWER_COOLING_MODE
class SYSTEM_POWER_LEVEL(EasyCastStructure):
    Enable: win32more.Windows.Win32.Foundation.BOOLEAN
    Spare: Byte * 3
    BatteryLevel: UInt32
    PowerPolicy: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    MinSystemState: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
class SYSTEM_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    PowerButton: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    SleepButton: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    LidClose: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    LidOpenWake: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    Reserved: UInt32
    Idle: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    IdleTimeout: UInt32
    IdleSensitivity: Byte
    DynamicThrottle: Byte
    Spare2: Byte * 2
    MinSleep: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    MaxSleep: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    ReducedLatencySleep: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    WinLogonFlags: UInt32
    Spare3: UInt32
    DozeS4Timeout: UInt32
    BroadcastCapacityResolution: UInt32
    DischargePolicy: win32more.Windows.Win32.System.Power.SYSTEM_POWER_LEVEL * 4
    VideoTimeout: UInt32
    VideoDimDisplay: win32more.Windows.Win32.Foundation.BOOLEAN
    VideoReserved: UInt32 * 3
    SpindownTimeout: UInt32
    OptimizeForPower: win32more.Windows.Win32.Foundation.BOOLEAN
    FanThrottleTolerance: Byte
    ForcedThrottle: Byte
    MinThrottle: Byte
    OverThrottled: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
SYSTEM_POWER_STATE = Int32
SYSTEM_POWER_STATE_PowerSystemUnspecified: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 0
SYSTEM_POWER_STATE_PowerSystemWorking: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 1
SYSTEM_POWER_STATE_PowerSystemSleeping1: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 2
SYSTEM_POWER_STATE_PowerSystemSleeping2: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 3
SYSTEM_POWER_STATE_PowerSystemSleeping3: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 4
SYSTEM_POWER_STATE_PowerSystemHibernate: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 5
SYSTEM_POWER_STATE_PowerSystemShutdown: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 6
SYSTEM_POWER_STATE_PowerSystemMaximum: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE = 7
class SYSTEM_POWER_STATUS(EasyCastStructure):
    ACLineStatus: Byte
    BatteryFlag: Byte
    BatteryLifePercent: Byte
    SystemStatusFlag: Byte
    BatteryLifeTime: UInt32
    BatteryFullLifeTime: UInt32
class THERMAL_EVENT(EasyCastStructure):
    Version: UInt32
    Size: UInt32
    Type: UInt32
    Temperature: UInt32
    TripPointTemperature: UInt32
    Initiator: win32more.Windows.Win32.Foundation.PWSTR
class THERMAL_INFORMATION(EasyCastStructure):
    ThermalStamp: UInt32
    ThermalConstant1: UInt32
    ThermalConstant2: UInt32
    Processors: UIntPtr
    SamplingPeriod: UInt32
    CurrentTemperature: UInt32
    PassiveTripPoint: UInt32
    CriticalTripPoint: UInt32
    ActiveTripPointCount: Byte
    ActiveTripPoint: UInt32 * 10
class THERMAL_POLICY(EasyCastStructure):
    Version: UInt32
    WaitForUpdate: win32more.Windows.Win32.Foundation.BOOLEAN
    Hibernate: win32more.Windows.Win32.Foundation.BOOLEAN
    Critical: win32more.Windows.Win32.Foundation.BOOLEAN
    ThermalStandby: win32more.Windows.Win32.Foundation.BOOLEAN
    ActivationReasons: UInt32
    PassiveLimit: UInt32
    ActiveLevel: UInt32
    OverThrottled: win32more.Windows.Win32.Foundation.BOOLEAN
class THERMAL_WAIT_READ(EasyCastStructure):
    Timeout: UInt32
    LowTemperature: UInt32
    HighTemperature: UInt32
USB_CHARGER_PORT = Int32
UsbChargerPort_Legacy: win32more.Windows.Win32.System.Power.USB_CHARGER_PORT = 0
UsbChargerPort_TypeC: win32more.Windows.Win32.System.Power.USB_CHARGER_PORT = 1
UsbChargerPort_Max: win32more.Windows.Win32.System.Power.USB_CHARGER_PORT = 2
USER_ACTIVITY_PRESENCE = Int32
USER_ACTIVITY_PRESENCE_PowerUserPresent: win32more.Windows.Win32.System.Power.USER_ACTIVITY_PRESENCE = 0
USER_ACTIVITY_PRESENCE_PowerUserNotPresent: win32more.Windows.Win32.System.Power.USER_ACTIVITY_PRESENCE = 1
USER_ACTIVITY_PRESENCE_PowerUserInactive: win32more.Windows.Win32.System.Power.USER_ACTIVITY_PRESENCE = 2
USER_ACTIVITY_PRESENCE_PowerUserMaximum: win32more.Windows.Win32.System.Power.USER_ACTIVITY_PRESENCE = 3
USER_ACTIVITY_PRESENCE_PowerUserInvalid: win32more.Windows.Win32.System.Power.USER_ACTIVITY_PRESENCE = 3
class USER_POWER_POLICY(EasyCastStructure):
    Revision: UInt32
    IdleAc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    IdleDc: win32more.Windows.Win32.System.Power.POWER_ACTION_POLICY
    IdleTimeoutAc: UInt32
    IdleTimeoutDc: UInt32
    IdleSensitivityAc: Byte
    IdleSensitivityDc: Byte
    ThrottlePolicyAc: Byte
    ThrottlePolicyDc: Byte
    MaxSleepAc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    MaxSleepDc: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
    Reserved: UInt32 * 2
    VideoTimeoutAc: UInt32
    VideoTimeoutDc: UInt32
    SpindownTimeoutAc: UInt32
    SpindownTimeoutDc: UInt32
    OptimizeForPowerAc: win32more.Windows.Win32.Foundation.BOOLEAN
    OptimizeForPowerDc: win32more.Windows.Win32.Foundation.BOOLEAN
    FanThrottleToleranceAc: Byte
    FanThrottleToleranceDc: Byte
    ForcedThrottleAc: Byte
    ForcedThrottleDc: Byte
class WAKE_ALARM_INFORMATION(EasyCastStructure):
    TimerIdentifier: UInt32
    Timeout: UInt32


make_ready(__name__)
