from win32more import *
import win32more.Foundation
import win32more.System.Power
import win32more.System.Registry
import win32more.System.Threading
import win32more.UI.Shell.PropertiesSystem

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
PROCESSOR_NUMBER_PKEY = PROPERTYKEY(Fmtid='5724c81d-d5af-4c1f-a103-a06e28f204c6', Pid=1)
GUID_DEVICE_BATTERY = '72631e54-78a4-11d0-bcf7-00aa00b7b32a'
GUID_DEVICE_APPLICATIONLAUNCH_BUTTON = '629758ee-986e-4d9e-8e47-de27f8ab054d'
GUID_DEVICE_SYS_BUTTON = '4afa3d53-74a7-11d0-be5e-00a0c9062857'
GUID_DEVICE_LID = '4afa3d52-74a7-11d0-be5e-00a0c9062857'
GUID_DEVICE_THERMAL_ZONE = '4afa3d51-74a7-11d0-be5e-00a0c9062857'
GUID_DEVICE_FAN = '05ecd13d-81da-4a2a-8a4c-524f23dd4dc9'
GUID_DEVICE_PROCESSOR = '97fadb10-4e33-40ae-359c-8bef029dbdd0'
GUID_DEVICE_MEMORY = '3fd0f03d-92e0-45fb-b75c-5ed8ffb01021'
GUID_DEVICE_ACPI_TIME = '97f99bf6-4497-4f18-bb22-4b9fb2fbef9c'
GUID_DEVICE_MESSAGE_INDICATOR = 'cd48a365-fa94-4ce2-a232-a1b764e5d8b4'
GUID_CLASS_INPUT = '4d1e55b2-f16f-11cf-88cb-001111000030'
GUID_DEVINTERFACE_THERMAL_COOLING = 'dbe4373d-3c81-40cb-ace4-e0e5d05f0c9f'
GUID_DEVINTERFACE_THERMAL_MANAGER = '927ec093-69a4-4bc0-bd02-711664714463'
BATTERY_UNKNOWN_CAPACITY = 4294967295
UNKNOWN_CAPACITY = 4294967295
BATTERY_SYSTEM_BATTERY = 2147483648
BATTERY_CAPACITY_RELATIVE = 1073741824
BATTERY_IS_SHORT_TERM = 536870912
BATTERY_SEALED = 268435456
BATTERY_SET_CHARGE_SUPPORTED = 1
BATTERY_SET_DISCHARGE_SUPPORTED = 2
BATTERY_SET_CHARGINGSOURCE_SUPPORTED = 4
BATTERY_SET_CHARGER_ID_SUPPORTED = 8
BATTERY_UNKNOWN_TIME = 4294967295
BATTERY_UNKNOWN_CURRENT = 4294967295
UNKNOWN_CURRENT = 4294967295
BATTERY_USB_CHARGER_STATUS_FN_DEFAULT_USB = 1
BATTERY_USB_CHARGER_STATUS_UCM_PD = 2
BATTERY_UNKNOWN_VOLTAGE = 4294967295
BATTERY_UNKNOWN_RATE = 2147483648
UNKNOWN_RATE = 2147483648
UNKNOWN_VOLTAGE = 4294967295
BATTERY_POWER_ON_LINE = 1
BATTERY_DISCHARGING = 2
BATTERY_CHARGING = 4
BATTERY_CRITICAL = 8
MAX_BATTERY_STRING_SIZE = 128
IOCTL_BATTERY_QUERY_TAG = 2703424
IOCTL_BATTERY_QUERY_INFORMATION = 2703428
IOCTL_BATTERY_SET_INFORMATION = 2719816
IOCTL_BATTERY_QUERY_STATUS = 2703436
IOCTL_BATTERY_CHARGING_SOURCE_CHANGE = 2703440
BATTERY_TAG_INVALID = 0
MAX_ACTIVE_COOLING_LEVELS = 10
ACTIVE_COOLING = 0
PASSIVE_COOLING = 1
TZ_ACTIVATION_REASON_THERMAL = 1
TZ_ACTIVATION_REASON_CURRENT = 2
THERMAL_POLICY_VERSION_1 = 1
THERMAL_POLICY_VERSION_2 = 2
IOCTL_THERMAL_QUERY_INFORMATION = 2703488
IOCTL_THERMAL_SET_COOLING_POLICY = 2719876
IOCTL_RUN_ACTIVE_COOLING_METHOD = 2719880
IOCTL_THERMAL_SET_PASSIVE_LIMIT = 2719884
IOCTL_THERMAL_READ_TEMPERATURE = 2703504
IOCTL_THERMAL_READ_POLICY = 2703508
IOCTL_QUERY_LID = 2703552
IOCTL_NOTIFY_SWITCH_EVENT = 2703616
IOCTL_GET_SYS_BUTTON_CAPS = 2703680
IOCTL_GET_SYS_BUTTON_EVENT = 2703684
SYS_BUTTON_POWER = 1
SYS_BUTTON_SLEEP = 2
SYS_BUTTON_LID = 4
SYS_BUTTON_WAKE = 2147483648
SYS_BUTTON_LID_STATE_MASK = 196608
SYS_BUTTON_LID_OPEN = 65536
SYS_BUTTON_LID_CLOSED = 131072
SYS_BUTTON_LID_INITIAL = 262144
SYS_BUTTON_LID_CHANGED = 524288
IOCTL_GET_PROCESSOR_OBJ_INFO = 2703744
THERMAL_COOLING_INTERFACE_VERSION = 1
THERMAL_DEVICE_INTERFACE_VERSION = 1
IOCTL_SET_SYS_MESSAGE_INDICATOR = 2720192
IOCTL_SET_WAKE_ALARM_VALUE = 2720256
IOCTL_SET_WAKE_ALARM_POLICY = 2720260
IOCTL_GET_WAKE_ALARM_VALUE = 2736648
IOCTL_GET_WAKE_ALARM_POLICY = 2736652
ACPI_TIME_ADJUST_DAYLIGHT = 1
ACPI_TIME_IN_DAYLIGHT = 2
ACPI_TIME_ZONE_UNKNOWN = 2047
IOCTL_ACPI_GET_REAL_TIME = 2703888
IOCTL_ACPI_SET_REAL_TIME = 2720276
IOCTL_GET_WAKE_ALARM_SYSTEM_POWERSTATE = 2703896
BATTERY_STATUS_WMI_GUID = 'fc4670d1-ebbf-416e-87ce-374a4ebc111a'
BATTERY_RUNTIME_WMI_GUID = '535a3767-1ac2-49bc-a077-3f7a02e40aec'
BATTERY_TEMPERATURE_WMI_GUID = '1a52a14d-adce-4a44-9a3e-c8d8f15ff2c2'
BATTERY_FULL_CHARGED_CAPACITY_WMI_GUID = '40b40565-96f7-4435-8694-97e0e4395905'
BATTERY_CYCLE_COUNT_WMI_GUID = 'ef98db24-0014-4c25-a50b-c724ae5cd371'
BATTERY_STATIC_DATA_WMI_GUID = '05e1e463-e4e2-4ea9-80cb-9bd4b3ca0655'
BATTERY_STATUS_CHANGE_WMI_GUID = 'cddfa0c3-7c5b-4e43-a034-059fa5b84364'
BATTERY_TAG_CHANGE_WMI_GUID = '5e1f6e19-8786-4d23-94fc-9e746bd5d888'
BATTERY_MINIPORT_UPDATE_DATA_VER_1 = 1
BATTERY_MINIPORT_UPDATE_DATA_VER_2 = 2
BATTERY_CLASS_MAJOR_VERSION = 1
BATTERY_CLASS_MINOR_VERSION = 0
BATTERY_CLASS_MINOR_VERSION_1 = 1
GUID_DEVICE_ENERGY_METER = '45bd8344-7ed6-49cf-a440-c276c933b053'
IOCTL_EMI_GET_VERSION = 2244608
IOCTL_EMI_GET_METADATA_SIZE = 2244612
IOCTL_EMI_GET_METADATA = 2244616
IOCTL_EMI_GET_MEASUREMENT = 2244620
EMI_NAME_MAX = 16
EMI_VERSION_V1 = 1
EMI_VERSION_V2 = 2
EFFECTIVE_POWER_MODE_V1 = 1
EFFECTIVE_POWER_MODE_V2 = 2
EnableSysTrayBatteryMeter = 1
EnableMultiBatteryDisplay = 2
EnablePasswordLogon = 4
EnableWakeOnRing = 8
EnableVideoDimDisplay = 16
POWER_ATTRIBUTE_HIDE = 1
POWER_ATTRIBUTE_SHOW_AOAC = 2
DEVICEPOWER_HARDWAREID = 2147483648
DEVICEPOWER_AND_OPERATION = 1073741824
DEVICEPOWER_FILTER_DEVICES_PRESENT = 536870912
DEVICEPOWER_FILTER_HARDWARE = 268435456
DEVICEPOWER_FILTER_WAKEENABLED = 134217728
DEVICEPOWER_FILTER_WAKEPROGRAMMABLE = 67108864
DEVICEPOWER_FILTER_ON_NAME = 33554432
DEVICEPOWER_SET_WAKEENABLED = 1
DEVICEPOWER_CLEAR_WAKEENABLED = 2
PDCAP_S0_SUPPORTED = 65536
PDCAP_S1_SUPPORTED = 131072
PDCAP_S2_SUPPORTED = 262144
PDCAP_S3_SUPPORTED = 524288
PDCAP_WAKE_FROM_S0_SUPPORTED = 1048576
PDCAP_WAKE_FROM_S1_SUPPORTED = 2097152
PDCAP_WAKE_FROM_S2_SUPPORTED = 4194304
PDCAP_WAKE_FROM_S3_SUPPORTED = 8388608
PDCAP_S4_SUPPORTED = 16777216
PDCAP_S5_SUPPORTED = 33554432
THERMAL_EVENT_VERSION = 1
POWER_PLATFORM_ROLE_VERSION = UInt32
POWER_PLATFORM_ROLE_V1 = 1
POWER_PLATFORM_ROLE_V2 = 2
POWER_SETTING_REGISTER_NOTIFICATION_FLAGS = UInt32
DEVICE_NOTIFY_SERVICE_HANDLE = 1
DEVICE_NOTIFY_CALLBACK = 2
DEVICE_NOTIFY_WINDOW_HANDLE = 0
EXECUTION_STATE = UInt32
ES_AWAYMODE_REQUIRED = 64
ES_CONTINUOUS = 2147483648
ES_DISPLAY_REQUIRED = 2
ES_SYSTEM_REQUIRED = 1
ES_USER_PRESENT = 4
POWER_ACTION_POLICY_EVENT_CODE = UInt32
POWER_FORCE_TRIGGER_RESET = 2147483648
POWER_LEVEL_USER_NOTIFY_EXEC = 4
POWER_LEVEL_USER_NOTIFY_SOUND = 2
POWER_LEVEL_USER_NOTIFY_TEXT = 1
POWER_USER_NOTIFY_BUTTON = 8
POWER_USER_NOTIFY_SHUTDOWN = 16
HPOWERNOTIFY = IntPtr
EFFECTIVE_POWER_MODE = Int32
EFFECTIVE_POWER_MODE_EffectivePowerModeBatterySaver = 0
EFFECTIVE_POWER_MODE_EffectivePowerModeBetterBattery = 1
EFFECTIVE_POWER_MODE_EffectivePowerModeBalanced = 2
EFFECTIVE_POWER_MODE_EffectivePowerModeHighPerformance = 3
EFFECTIVE_POWER_MODE_EffectivePowerModeMaxPerformance = 4
EFFECTIVE_POWER_MODE_EffectivePowerModeGameMode = 5
EFFECTIVE_POWER_MODE_EffectivePowerModeMixedReality = 6
def _define_EFFECTIVE_POWER_MODE_CALLBACK():
    return CFUNCTYPE(Void,win32more.System.Power.EFFECTIVE_POWER_MODE,c_void_p, use_last_error=False)
def _define_GLOBAL_MACHINE_POWER_POLICY_head():
    class GLOBAL_MACHINE_POWER_POLICY(Structure):
        pass
    return GLOBAL_MACHINE_POWER_POLICY
def _define_GLOBAL_MACHINE_POWER_POLICY():
    GLOBAL_MACHINE_POWER_POLICY = win32more.System.Power.GLOBAL_MACHINE_POWER_POLICY_head
    GLOBAL_MACHINE_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("LidOpenWakeAc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("LidOpenWakeDc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("BroadcastCapacityResolution", UInt32),
    ]
    return GLOBAL_MACHINE_POWER_POLICY
def _define_GLOBAL_USER_POWER_POLICY_head():
    class GLOBAL_USER_POWER_POLICY(Structure):
        pass
    return GLOBAL_USER_POWER_POLICY
def _define_GLOBAL_USER_POWER_POLICY():
    GLOBAL_USER_POWER_POLICY = win32more.System.Power.GLOBAL_USER_POWER_POLICY_head
    GLOBAL_USER_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("PowerButtonAc", win32more.System.Power.POWER_ACTION_POLICY),
        ("PowerButtonDc", win32more.System.Power.POWER_ACTION_POLICY),
        ("SleepButtonAc", win32more.System.Power.POWER_ACTION_POLICY),
        ("SleepButtonDc", win32more.System.Power.POWER_ACTION_POLICY),
        ("LidCloseAc", win32more.System.Power.POWER_ACTION_POLICY),
        ("LidCloseDc", win32more.System.Power.POWER_ACTION_POLICY),
        ("DischargePolicy", win32more.System.Power.SYSTEM_POWER_LEVEL * 4),
        ("GlobalFlags", UInt32),
    ]
    return GLOBAL_USER_POWER_POLICY
def _define_GLOBAL_POWER_POLICY_head():
    class GLOBAL_POWER_POLICY(Structure):
        pass
    return GLOBAL_POWER_POLICY
def _define_GLOBAL_POWER_POLICY():
    GLOBAL_POWER_POLICY = win32more.System.Power.GLOBAL_POWER_POLICY_head
    GLOBAL_POWER_POLICY._fields_ = [
        ("user", win32more.System.Power.GLOBAL_USER_POWER_POLICY),
        ("mach", win32more.System.Power.GLOBAL_MACHINE_POWER_POLICY),
    ]
    return GLOBAL_POWER_POLICY
def _define_MACHINE_POWER_POLICY_head():
    class MACHINE_POWER_POLICY(Structure):
        pass
    return MACHINE_POWER_POLICY
def _define_MACHINE_POWER_POLICY():
    MACHINE_POWER_POLICY = win32more.System.Power.MACHINE_POWER_POLICY_head
    MACHINE_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("MinSleepAc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("MinSleepDc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("ReducedLatencySleepAc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("ReducedLatencySleepDc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("DozeTimeoutAc", UInt32),
        ("DozeTimeoutDc", UInt32),
        ("DozeS4TimeoutAc", UInt32),
        ("DozeS4TimeoutDc", UInt32),
        ("MinThrottleAc", Byte),
        ("MinThrottleDc", Byte),
        ("pad1", Byte * 2),
        ("OverThrottledAc", win32more.System.Power.POWER_ACTION_POLICY),
        ("OverThrottledDc", win32more.System.Power.POWER_ACTION_POLICY),
    ]
    return MACHINE_POWER_POLICY
def _define_MACHINE_PROCESSOR_POWER_POLICY_head():
    class MACHINE_PROCESSOR_POWER_POLICY(Structure):
        pass
    return MACHINE_PROCESSOR_POWER_POLICY
def _define_MACHINE_PROCESSOR_POWER_POLICY():
    MACHINE_PROCESSOR_POWER_POLICY = win32more.System.Power.MACHINE_PROCESSOR_POWER_POLICY_head
    MACHINE_PROCESSOR_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("ProcessorPolicyAc", win32more.System.Power.PROCESSOR_POWER_POLICY),
        ("ProcessorPolicyDc", win32more.System.Power.PROCESSOR_POWER_POLICY),
    ]
    return MACHINE_PROCESSOR_POWER_POLICY
def _define_USER_POWER_POLICY_head():
    class USER_POWER_POLICY(Structure):
        pass
    return USER_POWER_POLICY
def _define_USER_POWER_POLICY():
    USER_POWER_POLICY = win32more.System.Power.USER_POWER_POLICY_head
    USER_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("IdleAc", win32more.System.Power.POWER_ACTION_POLICY),
        ("IdleDc", win32more.System.Power.POWER_ACTION_POLICY),
        ("IdleTimeoutAc", UInt32),
        ("IdleTimeoutDc", UInt32),
        ("IdleSensitivityAc", Byte),
        ("IdleSensitivityDc", Byte),
        ("ThrottlePolicyAc", Byte),
        ("ThrottlePolicyDc", Byte),
        ("MaxSleepAc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("MaxSleepDc", win32more.System.Power.SYSTEM_POWER_STATE),
        ("Reserved", UInt32 * 2),
        ("VideoTimeoutAc", UInt32),
        ("VideoTimeoutDc", UInt32),
        ("SpindownTimeoutAc", UInt32),
        ("SpindownTimeoutDc", UInt32),
        ("OptimizeForPowerAc", win32more.Foundation.BOOLEAN),
        ("OptimizeForPowerDc", win32more.Foundation.BOOLEAN),
        ("FanThrottleToleranceAc", Byte),
        ("FanThrottleToleranceDc", Byte),
        ("ForcedThrottleAc", Byte),
        ("ForcedThrottleDc", Byte),
    ]
    return USER_POWER_POLICY
def _define_POWER_POLICY_head():
    class POWER_POLICY(Structure):
        pass
    return POWER_POLICY
def _define_POWER_POLICY():
    POWER_POLICY = win32more.System.Power.POWER_POLICY_head
    POWER_POLICY._fields_ = [
        ("user", win32more.System.Power.USER_POWER_POLICY),
        ("mach", win32more.System.Power.MACHINE_POWER_POLICY),
    ]
    return POWER_POLICY
def _define_PWRSCHEMESENUMPROC_V1():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,UInt32,POINTER(SByte),UInt32,POINTER(SByte),POINTER(win32more.System.Power.POWER_POLICY_head),win32more.Foundation.LPARAM, use_last_error=False)
def _define_PWRSCHEMESENUMPROC():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.Power.POWER_POLICY_head),win32more.Foundation.LPARAM, use_last_error=False)
POWER_DATA_ACCESSOR = Int32
ACCESS_AC_POWER_SETTING_INDEX = 0
ACCESS_DC_POWER_SETTING_INDEX = 1
ACCESS_FRIENDLY_NAME = 2
ACCESS_DESCRIPTION = 3
ACCESS_POSSIBLE_POWER_SETTING = 4
ACCESS_POSSIBLE_POWER_SETTING_FRIENDLY_NAME = 5
ACCESS_POSSIBLE_POWER_SETTING_DESCRIPTION = 6
ACCESS_DEFAULT_AC_POWER_SETTING = 7
ACCESS_DEFAULT_DC_POWER_SETTING = 8
ACCESS_POSSIBLE_VALUE_MIN = 9
ACCESS_POSSIBLE_VALUE_MAX = 10
ACCESS_POSSIBLE_VALUE_INCREMENT = 11
ACCESS_POSSIBLE_VALUE_UNITS = 12
ACCESS_ICON_RESOURCE = 13
ACCESS_DEFAULT_SECURITY_DESCRIPTOR = 14
ACCESS_ATTRIBUTES = 15
ACCESS_SCHEME = 16
ACCESS_SUBGROUP = 17
ACCESS_INDIVIDUAL_SETTING = 18
ACCESS_ACTIVE_SCHEME = 19
ACCESS_CREATE_SCHEME = 20
ACCESS_AC_POWER_SETTING_MAX = 21
ACCESS_DC_POWER_SETTING_MAX = 22
ACCESS_AC_POWER_SETTING_MIN = 23
ACCESS_DC_POWER_SETTING_MIN = 24
ACCESS_PROFILE = 25
ACCESS_OVERLAY_SCHEME = 26
ACCESS_ACTIVE_OVERLAY_SCHEME = 27
def _define_PDEVICE_NOTIFY_CALLBACK_ROUTINE():
    return CFUNCTYPE(UInt32,c_void_p,UInt32,c_void_p, use_last_error=False)
def _define_DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS_head():
    class DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS(Structure):
        pass
    return DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS
def _define_DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS():
    DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS = win32more.System.Power.DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS_head
    DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS._fields_ = [
        ("Callback", win32more.System.Power.PDEVICE_NOTIFY_CALLBACK_ROUTINE),
        ("Context", c_void_p),
    ]
    return DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS
def _define_THERMAL_EVENT_head():
    class THERMAL_EVENT(Structure):
        pass
    return THERMAL_EVENT
def _define_THERMAL_EVENT():
    THERMAL_EVENT = win32more.System.Power.THERMAL_EVENT_head
    THERMAL_EVENT._fields_ = [
        ("Version", UInt32),
        ("Size", UInt32),
        ("Type", UInt32),
        ("Temperature", UInt32),
        ("TripPointTemperature", UInt32),
        ("Initiator", win32more.Foundation.PWSTR),
    ]
    return THERMAL_EVENT
BATTERY_QUERY_INFORMATION_LEVEL = Int32
BATTERY_QUERY_INFORMATION_LEVEL_BatteryInformation = 0
BATTERY_QUERY_INFORMATION_LEVEL_BatteryGranularityInformation = 1
BATTERY_QUERY_INFORMATION_LEVEL_BatteryTemperature = 2
BATTERY_QUERY_INFORMATION_LEVEL_BatteryEstimatedTime = 3
BATTERY_QUERY_INFORMATION_LEVEL_BatteryDeviceName = 4
BATTERY_QUERY_INFORMATION_LEVEL_BatteryManufactureDate = 5
BATTERY_QUERY_INFORMATION_LEVEL_BatteryManufactureName = 6
BATTERY_QUERY_INFORMATION_LEVEL_BatteryUniqueID = 7
BATTERY_QUERY_INFORMATION_LEVEL_BatterySerialNumber = 8
def _define_BATTERY_QUERY_INFORMATION_head():
    class BATTERY_QUERY_INFORMATION(Structure):
        pass
    return BATTERY_QUERY_INFORMATION
def _define_BATTERY_QUERY_INFORMATION():
    BATTERY_QUERY_INFORMATION = win32more.System.Power.BATTERY_QUERY_INFORMATION_head
    BATTERY_QUERY_INFORMATION._fields_ = [
        ("BatteryTag", UInt32),
        ("InformationLevel", win32more.System.Power.BATTERY_QUERY_INFORMATION_LEVEL),
        ("AtRate", UInt32),
    ]
    return BATTERY_QUERY_INFORMATION
def _define_BATTERY_INFORMATION_head():
    class BATTERY_INFORMATION(Structure):
        pass
    return BATTERY_INFORMATION
def _define_BATTERY_INFORMATION():
    BATTERY_INFORMATION = win32more.System.Power.BATTERY_INFORMATION_head
    BATTERY_INFORMATION._fields_ = [
        ("Capabilities", UInt32),
        ("Technology", Byte),
        ("Reserved", Byte * 3),
        ("Chemistry", Byte * 4),
        ("DesignedCapacity", UInt32),
        ("FullChargedCapacity", UInt32),
        ("DefaultAlert1", UInt32),
        ("DefaultAlert2", UInt32),
        ("CriticalBias", UInt32),
        ("CycleCount", UInt32),
    ]
    return BATTERY_INFORMATION
BATTERY_CHARGING_SOURCE_TYPE = Int32
BatteryChargingSourceType_AC = 1
BatteryChargingSourceType_USB = 2
BatteryChargingSourceType_Wireless = 3
BatteryChargingSourceType_Max = 4
def _define_BATTERY_CHARGING_SOURCE_head():
    class BATTERY_CHARGING_SOURCE(Structure):
        pass
    return BATTERY_CHARGING_SOURCE
def _define_BATTERY_CHARGING_SOURCE():
    BATTERY_CHARGING_SOURCE = win32more.System.Power.BATTERY_CHARGING_SOURCE_head
    BATTERY_CHARGING_SOURCE._fields_ = [
        ("Type", win32more.System.Power.BATTERY_CHARGING_SOURCE_TYPE),
        ("MaxCurrent", UInt32),
    ]
    return BATTERY_CHARGING_SOURCE
def _define_BATTERY_CHARGING_SOURCE_INFORMATION_head():
    class BATTERY_CHARGING_SOURCE_INFORMATION(Structure):
        pass
    return BATTERY_CHARGING_SOURCE_INFORMATION
def _define_BATTERY_CHARGING_SOURCE_INFORMATION():
    BATTERY_CHARGING_SOURCE_INFORMATION = win32more.System.Power.BATTERY_CHARGING_SOURCE_INFORMATION_head
    BATTERY_CHARGING_SOURCE_INFORMATION._fields_ = [
        ("Type", win32more.System.Power.BATTERY_CHARGING_SOURCE_TYPE),
        ("SourceOnline", win32more.Foundation.BOOLEAN),
    ]
    return BATTERY_CHARGING_SOURCE_INFORMATION
USB_CHARGER_PORT = Int32
UsbChargerPort_Legacy = 0
UsbChargerPort_TypeC = 1
UsbChargerPort_Max = 2
BATTERY_SET_INFORMATION_LEVEL = Int32
BATTERY_SET_INFORMATION_LEVEL_BatteryCriticalBias = 0
BATTERY_SET_INFORMATION_LEVEL_BatteryCharge = 1
BATTERY_SET_INFORMATION_LEVEL_BatteryDischarge = 2
BATTERY_SET_INFORMATION_LEVEL_BatteryChargingSource = 3
BATTERY_SET_INFORMATION_LEVEL_BatteryChargerId = 4
BATTERY_SET_INFORMATION_LEVEL_BatteryChargerStatus = 5
def _define_BATTERY_SET_INFORMATION_head():
    class BATTERY_SET_INFORMATION(Structure):
        pass
    return BATTERY_SET_INFORMATION
def _define_BATTERY_SET_INFORMATION():
    BATTERY_SET_INFORMATION = win32more.System.Power.BATTERY_SET_INFORMATION_head
    BATTERY_SET_INFORMATION._fields_ = [
        ("BatteryTag", UInt32),
        ("InformationLevel", win32more.System.Power.BATTERY_SET_INFORMATION_LEVEL),
        ("Buffer", Byte * 0),
    ]
    return BATTERY_SET_INFORMATION
def _define_BATTERY_CHARGER_STATUS_head():
    class BATTERY_CHARGER_STATUS(Structure):
        pass
    return BATTERY_CHARGER_STATUS
def _define_BATTERY_CHARGER_STATUS():
    BATTERY_CHARGER_STATUS = win32more.System.Power.BATTERY_CHARGER_STATUS_head
    BATTERY_CHARGER_STATUS._fields_ = [
        ("Type", win32more.System.Power.BATTERY_CHARGING_SOURCE_TYPE),
        ("VaData", UInt32 * 0),
    ]
    return BATTERY_CHARGER_STATUS
def _define_BATTERY_USB_CHARGER_STATUS_head():
    class BATTERY_USB_CHARGER_STATUS(Structure):
        pass
    return BATTERY_USB_CHARGER_STATUS
def _define_BATTERY_USB_CHARGER_STATUS():
    BATTERY_USB_CHARGER_STATUS = win32more.System.Power.BATTERY_USB_CHARGER_STATUS_head
    BATTERY_USB_CHARGER_STATUS._fields_ = [
        ("Type", win32more.System.Power.BATTERY_CHARGING_SOURCE_TYPE),
        ("Reserved", UInt32),
        ("Flags", UInt32),
        ("MaxCurrent", UInt32),
        ("Voltage", UInt32),
        ("PortType", win32more.System.Power.USB_CHARGER_PORT),
        ("PortId", UInt64),
        ("PowerSourceInformation", c_void_p),
        ("OemCharger", Guid),
    ]
    return BATTERY_USB_CHARGER_STATUS
def _define_BATTERY_WAIT_STATUS_head():
    class BATTERY_WAIT_STATUS(Structure):
        pass
    return BATTERY_WAIT_STATUS
def _define_BATTERY_WAIT_STATUS():
    BATTERY_WAIT_STATUS = win32more.System.Power.BATTERY_WAIT_STATUS_head
    BATTERY_WAIT_STATUS._fields_ = [
        ("BatteryTag", UInt32),
        ("Timeout", UInt32),
        ("PowerState", UInt32),
        ("LowCapacity", UInt32),
        ("HighCapacity", UInt32),
    ]
    return BATTERY_WAIT_STATUS
def _define_BATTERY_STATUS_head():
    class BATTERY_STATUS(Structure):
        pass
    return BATTERY_STATUS
def _define_BATTERY_STATUS():
    BATTERY_STATUS = win32more.System.Power.BATTERY_STATUS_head
    BATTERY_STATUS._fields_ = [
        ("PowerState", UInt32),
        ("Capacity", UInt32),
        ("Voltage", UInt32),
        ("Rate", Int32),
    ]
    return BATTERY_STATUS
def _define_BATTERY_MANUFACTURE_DATE_head():
    class BATTERY_MANUFACTURE_DATE(Structure):
        pass
    return BATTERY_MANUFACTURE_DATE
def _define_BATTERY_MANUFACTURE_DATE():
    BATTERY_MANUFACTURE_DATE = win32more.System.Power.BATTERY_MANUFACTURE_DATE_head
    BATTERY_MANUFACTURE_DATE._fields_ = [
        ("Day", Byte),
        ("Month", Byte),
        ("Year", UInt16),
    ]
    return BATTERY_MANUFACTURE_DATE
def _define_THERMAL_INFORMATION_head():
    class THERMAL_INFORMATION(Structure):
        pass
    return THERMAL_INFORMATION
def _define_THERMAL_INFORMATION():
    THERMAL_INFORMATION = win32more.System.Power.THERMAL_INFORMATION_head
    THERMAL_INFORMATION._fields_ = [
        ("ThermalStamp", UInt32),
        ("ThermalConstant1", UInt32),
        ("ThermalConstant2", UInt32),
        ("Processors", UIntPtr),
        ("SamplingPeriod", UInt32),
        ("CurrentTemperature", UInt32),
        ("PassiveTripPoint", UInt32),
        ("CriticalTripPoint", UInt32),
        ("ActiveTripPointCount", Byte),
        ("ActiveTripPoint", UInt32 * 10),
    ]
    return THERMAL_INFORMATION
def _define_THERMAL_WAIT_READ_head():
    class THERMAL_WAIT_READ(Structure):
        pass
    return THERMAL_WAIT_READ
def _define_THERMAL_WAIT_READ():
    THERMAL_WAIT_READ = win32more.System.Power.THERMAL_WAIT_READ_head
    THERMAL_WAIT_READ._fields_ = [
        ("Timeout", UInt32),
        ("LowTemperature", UInt32),
        ("HighTemperature", UInt32),
    ]
    return THERMAL_WAIT_READ
def _define_THERMAL_POLICY_head():
    class THERMAL_POLICY(Structure):
        pass
    return THERMAL_POLICY
def _define_THERMAL_POLICY():
    THERMAL_POLICY = win32more.System.Power.THERMAL_POLICY_head
    THERMAL_POLICY._fields_ = [
        ("Version", UInt32),
        ("WaitForUpdate", win32more.Foundation.BOOLEAN),
        ("Hibernate", win32more.Foundation.BOOLEAN),
        ("Critical", win32more.Foundation.BOOLEAN),
        ("ThermalStandby", win32more.Foundation.BOOLEAN),
        ("ActivationReasons", UInt32),
        ("PassiveLimit", UInt32),
        ("ActiveLevel", UInt32),
        ("OverThrottled", win32more.Foundation.BOOLEAN),
    ]
    return THERMAL_POLICY
def _define_PROCESSOR_OBJECT_INFO_head():
    class PROCESSOR_OBJECT_INFO(Structure):
        pass
    return PROCESSOR_OBJECT_INFO
def _define_PROCESSOR_OBJECT_INFO():
    PROCESSOR_OBJECT_INFO = win32more.System.Power.PROCESSOR_OBJECT_INFO_head
    PROCESSOR_OBJECT_INFO._fields_ = [
        ("PhysicalID", UInt32),
        ("PBlkAddress", UInt32),
        ("PBlkLength", Byte),
    ]
    return PROCESSOR_OBJECT_INFO
def _define_PROCESSOR_OBJECT_INFO_EX_head():
    class PROCESSOR_OBJECT_INFO_EX(Structure):
        pass
    return PROCESSOR_OBJECT_INFO_EX
def _define_PROCESSOR_OBJECT_INFO_EX():
    PROCESSOR_OBJECT_INFO_EX = win32more.System.Power.PROCESSOR_OBJECT_INFO_EX_head
    PROCESSOR_OBJECT_INFO_EX._fields_ = [
        ("PhysicalID", UInt32),
        ("PBlkAddress", UInt32),
        ("PBlkLength", Byte),
        ("InitialApicId", UInt32),
    ]
    return PROCESSOR_OBJECT_INFO_EX
def _define_WAKE_ALARM_INFORMATION_head():
    class WAKE_ALARM_INFORMATION(Structure):
        pass
    return WAKE_ALARM_INFORMATION
def _define_WAKE_ALARM_INFORMATION():
    WAKE_ALARM_INFORMATION = win32more.System.Power.WAKE_ALARM_INFORMATION_head
    WAKE_ALARM_INFORMATION._fields_ = [
        ("TimerIdentifier", UInt32),
        ("Timeout", UInt32),
    ]
    return WAKE_ALARM_INFORMATION
def _define_ACPI_REAL_TIME_head():
    class ACPI_REAL_TIME(Structure):
        pass
    return ACPI_REAL_TIME
def _define_ACPI_REAL_TIME():
    ACPI_REAL_TIME = win32more.System.Power.ACPI_REAL_TIME_head
    ACPI_REAL_TIME._fields_ = [
        ("Year", UInt16),
        ("Month", Byte),
        ("Day", Byte),
        ("Hour", Byte),
        ("Minute", Byte),
        ("Second", Byte),
        ("Valid", Byte),
        ("Milliseconds", UInt16),
        ("TimeZone", Int16),
        ("DayLight", Byte),
        ("Reserved1", Byte * 3),
    ]
    return ACPI_REAL_TIME
EMI_MEASUREMENT_UNIT = Int32
EMI_MEASUREMENT_UNIT_EmiMeasurementUnitPicowattHours = 0
def _define_EMI_VERSION_head():
    class EMI_VERSION(Structure):
        pass
    return EMI_VERSION
def _define_EMI_VERSION():
    EMI_VERSION = win32more.System.Power.EMI_VERSION_head
    EMI_VERSION._fields_ = [
        ("EmiVersion", UInt16),
    ]
    return EMI_VERSION
def _define_EMI_METADATA_SIZE_head():
    class EMI_METADATA_SIZE(Structure):
        pass
    return EMI_METADATA_SIZE
def _define_EMI_METADATA_SIZE():
    EMI_METADATA_SIZE = win32more.System.Power.EMI_METADATA_SIZE_head
    EMI_METADATA_SIZE._fields_ = [
        ("MetadataSize", UInt32),
    ]
    return EMI_METADATA_SIZE
def _define_EMI_CHANNEL_MEASUREMENT_DATA_head():
    class EMI_CHANNEL_MEASUREMENT_DATA(Structure):
        pass
    return EMI_CHANNEL_MEASUREMENT_DATA
def _define_EMI_CHANNEL_MEASUREMENT_DATA():
    EMI_CHANNEL_MEASUREMENT_DATA = win32more.System.Power.EMI_CHANNEL_MEASUREMENT_DATA_head
    EMI_CHANNEL_MEASUREMENT_DATA._fields_ = [
        ("AbsoluteEnergy", UInt64),
        ("AbsoluteTime", UInt64),
    ]
    return EMI_CHANNEL_MEASUREMENT_DATA
def _define_EMI_METADATA_V1_head():
    class EMI_METADATA_V1(Structure):
        pass
    return EMI_METADATA_V1
def _define_EMI_METADATA_V1():
    EMI_METADATA_V1 = win32more.System.Power.EMI_METADATA_V1_head
    EMI_METADATA_V1._fields_ = [
        ("MeasurementUnit", win32more.System.Power.EMI_MEASUREMENT_UNIT),
        ("HardwareOEM", Char * 16),
        ("HardwareModel", Char * 16),
        ("HardwareRevision", UInt16),
        ("MeteredHardwareNameSize", UInt16),
        ("MeteredHardwareName", Char * 0),
    ]
    return EMI_METADATA_V1
def _define_EMI_CHANNEL_V2_head():
    class EMI_CHANNEL_V2(Structure):
        pass
    return EMI_CHANNEL_V2
def _define_EMI_CHANNEL_V2():
    EMI_CHANNEL_V2 = win32more.System.Power.EMI_CHANNEL_V2_head
    EMI_CHANNEL_V2._fields_ = [
        ("MeasurementUnit", win32more.System.Power.EMI_MEASUREMENT_UNIT),
        ("ChannelNameSize", UInt16),
        ("ChannelName", Char * 0),
    ]
    return EMI_CHANNEL_V2
def _define_EMI_METADATA_V2_head():
    class EMI_METADATA_V2(Structure):
        pass
    return EMI_METADATA_V2
def _define_EMI_METADATA_V2():
    EMI_METADATA_V2 = win32more.System.Power.EMI_METADATA_V2_head
    EMI_METADATA_V2._fields_ = [
        ("HardwareOEM", Char * 16),
        ("HardwareModel", Char * 16),
        ("HardwareRevision", UInt16),
        ("ChannelCount", UInt16),
        ("Channels", win32more.System.Power.EMI_CHANNEL_V2 * 0),
    ]
    return EMI_METADATA_V2
def _define_EMI_MEASUREMENT_DATA_V2_head():
    class EMI_MEASUREMENT_DATA_V2(Structure):
        pass
    return EMI_MEASUREMENT_DATA_V2
def _define_EMI_MEASUREMENT_DATA_V2():
    EMI_MEASUREMENT_DATA_V2 = win32more.System.Power.EMI_MEASUREMENT_DATA_V2_head
    EMI_MEASUREMENT_DATA_V2._fields_ = [
        ("ChannelData", win32more.System.Power.EMI_CHANNEL_MEASUREMENT_DATA * 0),
    ]
    return EMI_MEASUREMENT_DATA_V2
SYSTEM_POWER_STATE = Int32
SYSTEM_POWER_STATE_PowerSystemUnspecified = 0
SYSTEM_POWER_STATE_PowerSystemWorking = 1
SYSTEM_POWER_STATE_PowerSystemSleeping1 = 2
SYSTEM_POWER_STATE_PowerSystemSleeping2 = 3
SYSTEM_POWER_STATE_PowerSystemSleeping3 = 4
SYSTEM_POWER_STATE_PowerSystemHibernate = 5
SYSTEM_POWER_STATE_PowerSystemShutdown = 6
SYSTEM_POWER_STATE_PowerSystemMaximum = 7
POWER_ACTION = Int32
POWER_ACTION_PowerActionNone = 0
POWER_ACTION_PowerActionReserved = 1
POWER_ACTION_PowerActionSleep = 2
POWER_ACTION_PowerActionHibernate = 3
POWER_ACTION_PowerActionShutdown = 4
POWER_ACTION_PowerActionShutdownReset = 5
POWER_ACTION_PowerActionShutdownOff = 6
POWER_ACTION_PowerActionWarmEject = 7
POWER_ACTION_PowerActionDisplayOff = 8
DEVICE_POWER_STATE = Int32
DEVICE_POWER_STATE_PowerDeviceUnspecified = 0
DEVICE_POWER_STATE_PowerDeviceD0 = 1
DEVICE_POWER_STATE_PowerDeviceD1 = 2
DEVICE_POWER_STATE_PowerDeviceD2 = 3
DEVICE_POWER_STATE_PowerDeviceD3 = 4
DEVICE_POWER_STATE_PowerDeviceMaximum = 5
LATENCY_TIME = Int32
LT_DONT_CARE = 0
LT_LOWEST_LATENCY = 1
POWER_REQUEST_TYPE = Int32
POWER_REQUEST_TYPE_PowerRequestDisplayRequired = 0
POWER_REQUEST_TYPE_PowerRequestSystemRequired = 1
POWER_REQUEST_TYPE_PowerRequestAwayModeRequired = 2
POWER_REQUEST_TYPE_PowerRequestExecutionRequired = 3
def _define_CM_POWER_DATA_head():
    class CM_POWER_DATA(Structure):
        pass
    return CM_POWER_DATA
def _define_CM_POWER_DATA():
    CM_POWER_DATA = win32more.System.Power.CM_POWER_DATA_head
    CM_POWER_DATA._fields_ = [
        ("PD_Size", UInt32),
        ("PD_MostRecentPowerState", win32more.System.Power.DEVICE_POWER_STATE),
        ("PD_Capabilities", UInt32),
        ("PD_D1Latency", UInt32),
        ("PD_D2Latency", UInt32),
        ("PD_D3Latency", UInt32),
        ("PD_PowerStateMapping", win32more.System.Power.DEVICE_POWER_STATE * 7),
        ("PD_DeepestSystemWake", win32more.System.Power.SYSTEM_POWER_STATE),
    ]
    return CM_POWER_DATA
POWER_INFORMATION_LEVEL = Int32
POWER_INFORMATION_LEVEL_SystemPowerPolicyAc = 0
POWER_INFORMATION_LEVEL_SystemPowerPolicyDc = 1
POWER_INFORMATION_LEVEL_VerifySystemPolicyAc = 2
POWER_INFORMATION_LEVEL_VerifySystemPolicyDc = 3
POWER_INFORMATION_LEVEL_SystemPowerCapabilities = 4
POWER_INFORMATION_LEVEL_SystemBatteryState = 5
POWER_INFORMATION_LEVEL_SystemPowerStateHandler = 6
POWER_INFORMATION_LEVEL_ProcessorStateHandler = 7
POWER_INFORMATION_LEVEL_SystemPowerPolicyCurrent = 8
POWER_INFORMATION_LEVEL_AdministratorPowerPolicy = 9
POWER_INFORMATION_LEVEL_SystemReserveHiberFile = 10
POWER_INFORMATION_LEVEL_ProcessorInformation = 11
POWER_INFORMATION_LEVEL_SystemPowerInformation = 12
POWER_INFORMATION_LEVEL_ProcessorStateHandler2 = 13
POWER_INFORMATION_LEVEL_LastWakeTime = 14
POWER_INFORMATION_LEVEL_LastSleepTime = 15
POWER_INFORMATION_LEVEL_SystemExecutionState = 16
POWER_INFORMATION_LEVEL_SystemPowerStateNotifyHandler = 17
POWER_INFORMATION_LEVEL_ProcessorPowerPolicyAc = 18
POWER_INFORMATION_LEVEL_ProcessorPowerPolicyDc = 19
POWER_INFORMATION_LEVEL_VerifyProcessorPowerPolicyAc = 20
POWER_INFORMATION_LEVEL_VerifyProcessorPowerPolicyDc = 21
POWER_INFORMATION_LEVEL_ProcessorPowerPolicyCurrent = 22
POWER_INFORMATION_LEVEL_SystemPowerStateLogging = 23
POWER_INFORMATION_LEVEL_SystemPowerLoggingEntry = 24
POWER_INFORMATION_LEVEL_SetPowerSettingValue = 25
POWER_INFORMATION_LEVEL_NotifyUserPowerSetting = 26
POWER_INFORMATION_LEVEL_PowerInformationLevelUnused0 = 27
POWER_INFORMATION_LEVEL_SystemMonitorHiberBootPowerOff = 28
POWER_INFORMATION_LEVEL_SystemVideoState = 29
POWER_INFORMATION_LEVEL_TraceApplicationPowerMessage = 30
POWER_INFORMATION_LEVEL_TraceApplicationPowerMessageEnd = 31
POWER_INFORMATION_LEVEL_ProcessorPerfStates = 32
POWER_INFORMATION_LEVEL_ProcessorIdleStates = 33
POWER_INFORMATION_LEVEL_ProcessorCap = 34
POWER_INFORMATION_LEVEL_SystemWakeSource = 35
POWER_INFORMATION_LEVEL_SystemHiberFileInformation = 36
POWER_INFORMATION_LEVEL_TraceServicePowerMessage = 37
POWER_INFORMATION_LEVEL_ProcessorLoad = 38
POWER_INFORMATION_LEVEL_PowerShutdownNotification = 39
POWER_INFORMATION_LEVEL_MonitorCapabilities = 40
POWER_INFORMATION_LEVEL_SessionPowerInit = 41
POWER_INFORMATION_LEVEL_SessionDisplayState = 42
POWER_INFORMATION_LEVEL_PowerRequestCreate = 43
POWER_INFORMATION_LEVEL_PowerRequestAction = 44
POWER_INFORMATION_LEVEL_GetPowerRequestList = 45
POWER_INFORMATION_LEVEL_ProcessorInformationEx = 46
POWER_INFORMATION_LEVEL_NotifyUserModeLegacyPowerEvent = 47
POWER_INFORMATION_LEVEL_GroupPark = 48
POWER_INFORMATION_LEVEL_ProcessorIdleDomains = 49
POWER_INFORMATION_LEVEL_WakeTimerList = 50
POWER_INFORMATION_LEVEL_SystemHiberFileSize = 51
POWER_INFORMATION_LEVEL_ProcessorIdleStatesHv = 52
POWER_INFORMATION_LEVEL_ProcessorPerfStatesHv = 53
POWER_INFORMATION_LEVEL_ProcessorPerfCapHv = 54
POWER_INFORMATION_LEVEL_ProcessorSetIdle = 55
POWER_INFORMATION_LEVEL_LogicalProcessorIdling = 56
POWER_INFORMATION_LEVEL_UserPresence = 57
POWER_INFORMATION_LEVEL_PowerSettingNotificationName = 58
POWER_INFORMATION_LEVEL_GetPowerSettingValue = 59
POWER_INFORMATION_LEVEL_IdleResiliency = 60
POWER_INFORMATION_LEVEL_SessionRITState = 61
POWER_INFORMATION_LEVEL_SessionConnectNotification = 62
POWER_INFORMATION_LEVEL_SessionPowerCleanup = 63
POWER_INFORMATION_LEVEL_SessionLockState = 64
POWER_INFORMATION_LEVEL_SystemHiberbootState = 65
POWER_INFORMATION_LEVEL_PlatformInformation = 66
POWER_INFORMATION_LEVEL_PdcInvocation = 67
POWER_INFORMATION_LEVEL_MonitorInvocation = 68
POWER_INFORMATION_LEVEL_FirmwareTableInformationRegistered = 69
POWER_INFORMATION_LEVEL_SetShutdownSelectedTime = 70
POWER_INFORMATION_LEVEL_SuspendResumeInvocation = 71
POWER_INFORMATION_LEVEL_PlmPowerRequestCreate = 72
POWER_INFORMATION_LEVEL_ScreenOff = 73
POWER_INFORMATION_LEVEL_CsDeviceNotification = 74
POWER_INFORMATION_LEVEL_PlatformRole = 75
POWER_INFORMATION_LEVEL_LastResumePerformance = 76
POWER_INFORMATION_LEVEL_DisplayBurst = 77
POWER_INFORMATION_LEVEL_ExitLatencySamplingPercentage = 78
POWER_INFORMATION_LEVEL_RegisterSpmPowerSettings = 79
POWER_INFORMATION_LEVEL_PlatformIdleStates = 80
POWER_INFORMATION_LEVEL_ProcessorIdleVeto = 81
POWER_INFORMATION_LEVEL_PlatformIdleVeto = 82
POWER_INFORMATION_LEVEL_SystemBatteryStatePrecise = 83
POWER_INFORMATION_LEVEL_ThermalEvent = 84
POWER_INFORMATION_LEVEL_PowerRequestActionInternal = 85
POWER_INFORMATION_LEVEL_BatteryDeviceState = 86
POWER_INFORMATION_LEVEL_PowerInformationInternal = 87
POWER_INFORMATION_LEVEL_ThermalStandby = 88
POWER_INFORMATION_LEVEL_SystemHiberFileType = 89
POWER_INFORMATION_LEVEL_PhysicalPowerButtonPress = 90
POWER_INFORMATION_LEVEL_QueryPotentialDripsConstraint = 91
POWER_INFORMATION_LEVEL_EnergyTrackerCreate = 92
POWER_INFORMATION_LEVEL_EnergyTrackerQuery = 93
POWER_INFORMATION_LEVEL_UpdateBlackBoxRecorder = 94
POWER_INFORMATION_LEVEL_SessionAllowExternalDmaDevices = 95
POWER_INFORMATION_LEVEL_SendSuspendResumeNotification = 96
POWER_INFORMATION_LEVEL_PowerInformationLevelMaximum = 97
SYSTEM_POWER_CONDITION = Int32
SYSTEM_POWER_CONDITION_PoAc = 0
SYSTEM_POWER_CONDITION_PoDc = 1
SYSTEM_POWER_CONDITION_PoHot = 2
SYSTEM_POWER_CONDITION_PoConditionMaximum = 3
def _define_SET_POWER_SETTING_VALUE_head():
    class SET_POWER_SETTING_VALUE(Structure):
        pass
    return SET_POWER_SETTING_VALUE
def _define_SET_POWER_SETTING_VALUE():
    SET_POWER_SETTING_VALUE = win32more.System.Power.SET_POWER_SETTING_VALUE_head
    SET_POWER_SETTING_VALUE._fields_ = [
        ("Version", UInt32),
        ("Guid", Guid),
        ("PowerCondition", win32more.System.Power.SYSTEM_POWER_CONDITION),
        ("DataLength", UInt32),
        ("Data", Byte * 0),
    ]
    return SET_POWER_SETTING_VALUE
POWER_PLATFORM_ROLE = Int32
POWER_PLATFORM_ROLE_PlatformRoleUnspecified = 0
POWER_PLATFORM_ROLE_PlatformRoleDesktop = 1
POWER_PLATFORM_ROLE_PlatformRoleMobile = 2
POWER_PLATFORM_ROLE_PlatformRoleWorkstation = 3
POWER_PLATFORM_ROLE_PlatformRoleEnterpriseServer = 4
POWER_PLATFORM_ROLE_PlatformRoleSOHOServer = 5
POWER_PLATFORM_ROLE_PlatformRoleAppliancePC = 6
POWER_PLATFORM_ROLE_PlatformRolePerformanceServer = 7
POWER_PLATFORM_ROLE_PlatformRoleSlate = 8
POWER_PLATFORM_ROLE_PlatformRoleMaximum = 9
def _define_BATTERY_REPORTING_SCALE_head():
    class BATTERY_REPORTING_SCALE(Structure):
        pass
    return BATTERY_REPORTING_SCALE
def _define_BATTERY_REPORTING_SCALE():
    BATTERY_REPORTING_SCALE = win32more.System.Power.BATTERY_REPORTING_SCALE_head
    BATTERY_REPORTING_SCALE._fields_ = [
        ("Granularity", UInt32),
        ("Capacity", UInt32),
    ]
    return BATTERY_REPORTING_SCALE
def _define_POWER_ACTION_POLICY_head():
    class POWER_ACTION_POLICY(Structure):
        pass
    return POWER_ACTION_POLICY
def _define_POWER_ACTION_POLICY():
    POWER_ACTION_POLICY = win32more.System.Power.POWER_ACTION_POLICY_head
    POWER_ACTION_POLICY._fields_ = [
        ("Action", win32more.System.Power.POWER_ACTION),
        ("Flags", UInt32),
        ("EventCode", win32more.System.Power.POWER_ACTION_POLICY_EVENT_CODE),
    ]
    return POWER_ACTION_POLICY
def _define_SYSTEM_POWER_LEVEL_head():
    class SYSTEM_POWER_LEVEL(Structure):
        pass
    return SYSTEM_POWER_LEVEL
def _define_SYSTEM_POWER_LEVEL():
    SYSTEM_POWER_LEVEL = win32more.System.Power.SYSTEM_POWER_LEVEL_head
    SYSTEM_POWER_LEVEL._fields_ = [
        ("Enable", win32more.Foundation.BOOLEAN),
        ("Spare", Byte * 3),
        ("BatteryLevel", UInt32),
        ("PowerPolicy", win32more.System.Power.POWER_ACTION_POLICY),
        ("MinSystemState", win32more.System.Power.SYSTEM_POWER_STATE),
    ]
    return SYSTEM_POWER_LEVEL
def _define_SYSTEM_POWER_POLICY_head():
    class SYSTEM_POWER_POLICY(Structure):
        pass
    return SYSTEM_POWER_POLICY
def _define_SYSTEM_POWER_POLICY():
    SYSTEM_POWER_POLICY = win32more.System.Power.SYSTEM_POWER_POLICY_head
    SYSTEM_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("PowerButton", win32more.System.Power.POWER_ACTION_POLICY),
        ("SleepButton", win32more.System.Power.POWER_ACTION_POLICY),
        ("LidClose", win32more.System.Power.POWER_ACTION_POLICY),
        ("LidOpenWake", win32more.System.Power.SYSTEM_POWER_STATE),
        ("Reserved", UInt32),
        ("Idle", win32more.System.Power.POWER_ACTION_POLICY),
        ("IdleTimeout", UInt32),
        ("IdleSensitivity", Byte),
        ("DynamicThrottle", Byte),
        ("Spare2", Byte * 2),
        ("MinSleep", win32more.System.Power.SYSTEM_POWER_STATE),
        ("MaxSleep", win32more.System.Power.SYSTEM_POWER_STATE),
        ("ReducedLatencySleep", win32more.System.Power.SYSTEM_POWER_STATE),
        ("WinLogonFlags", UInt32),
        ("Spare3", UInt32),
        ("DozeS4Timeout", UInt32),
        ("BroadcastCapacityResolution", UInt32),
        ("DischargePolicy", win32more.System.Power.SYSTEM_POWER_LEVEL * 4),
        ("VideoTimeout", UInt32),
        ("VideoDimDisplay", win32more.Foundation.BOOLEAN),
        ("VideoReserved", UInt32 * 3),
        ("SpindownTimeout", UInt32),
        ("OptimizeForPower", win32more.Foundation.BOOLEAN),
        ("FanThrottleTolerance", Byte),
        ("ForcedThrottle", Byte),
        ("MinThrottle", Byte),
        ("OverThrottled", win32more.System.Power.POWER_ACTION_POLICY),
    ]
    return SYSTEM_POWER_POLICY
def _define_PROCESSOR_POWER_POLICY_INFO_head():
    class PROCESSOR_POWER_POLICY_INFO(Structure):
        pass
    return PROCESSOR_POWER_POLICY_INFO
def _define_PROCESSOR_POWER_POLICY_INFO():
    PROCESSOR_POWER_POLICY_INFO = win32more.System.Power.PROCESSOR_POWER_POLICY_INFO_head
    PROCESSOR_POWER_POLICY_INFO._fields_ = [
        ("TimeCheck", UInt32),
        ("DemoteLimit", UInt32),
        ("PromoteLimit", UInt32),
        ("DemotePercent", Byte),
        ("PromotePercent", Byte),
        ("Spare", Byte * 2),
        ("_bitfield", UInt32),
    ]
    return PROCESSOR_POWER_POLICY_INFO
def _define_PROCESSOR_POWER_POLICY_head():
    class PROCESSOR_POWER_POLICY(Structure):
        pass
    return PROCESSOR_POWER_POLICY
def _define_PROCESSOR_POWER_POLICY():
    PROCESSOR_POWER_POLICY = win32more.System.Power.PROCESSOR_POWER_POLICY_head
    PROCESSOR_POWER_POLICY._fields_ = [
        ("Revision", UInt32),
        ("DynamicThrottle", Byte),
        ("Spare", Byte * 3),
        ("_bitfield", UInt32),
        ("PolicyCount", UInt32),
        ("Policy", win32more.System.Power.PROCESSOR_POWER_POLICY_INFO * 3),
    ]
    return PROCESSOR_POWER_POLICY
def _define_ADMINISTRATOR_POWER_POLICY_head():
    class ADMINISTRATOR_POWER_POLICY(Structure):
        pass
    return ADMINISTRATOR_POWER_POLICY
def _define_ADMINISTRATOR_POWER_POLICY():
    ADMINISTRATOR_POWER_POLICY = win32more.System.Power.ADMINISTRATOR_POWER_POLICY_head
    ADMINISTRATOR_POWER_POLICY._fields_ = [
        ("MinSleep", win32more.System.Power.SYSTEM_POWER_STATE),
        ("MaxSleep", win32more.System.Power.SYSTEM_POWER_STATE),
        ("MinVideoTimeout", UInt32),
        ("MaxVideoTimeout", UInt32),
        ("MinSpindownTimeout", UInt32),
        ("MaxSpindownTimeout", UInt32),
    ]
    return ADMINISTRATOR_POWER_POLICY
def _define_SYSTEM_POWER_CAPABILITIES_head():
    class SYSTEM_POWER_CAPABILITIES(Structure):
        pass
    return SYSTEM_POWER_CAPABILITIES
def _define_SYSTEM_POWER_CAPABILITIES():
    SYSTEM_POWER_CAPABILITIES = win32more.System.Power.SYSTEM_POWER_CAPABILITIES_head
    SYSTEM_POWER_CAPABILITIES._fields_ = [
        ("PowerButtonPresent", win32more.Foundation.BOOLEAN),
        ("SleepButtonPresent", win32more.Foundation.BOOLEAN),
        ("LidPresent", win32more.Foundation.BOOLEAN),
        ("SystemS1", win32more.Foundation.BOOLEAN),
        ("SystemS2", win32more.Foundation.BOOLEAN),
        ("SystemS3", win32more.Foundation.BOOLEAN),
        ("SystemS4", win32more.Foundation.BOOLEAN),
        ("SystemS5", win32more.Foundation.BOOLEAN),
        ("HiberFilePresent", win32more.Foundation.BOOLEAN),
        ("FullWake", win32more.Foundation.BOOLEAN),
        ("VideoDimPresent", win32more.Foundation.BOOLEAN),
        ("ApmPresent", win32more.Foundation.BOOLEAN),
        ("UpsPresent", win32more.Foundation.BOOLEAN),
        ("ThermalControl", win32more.Foundation.BOOLEAN),
        ("ProcessorThrottle", win32more.Foundation.BOOLEAN),
        ("ProcessorMinThrottle", Byte),
        ("ProcessorMaxThrottle", Byte),
        ("FastSystemS4", win32more.Foundation.BOOLEAN),
        ("Hiberboot", win32more.Foundation.BOOLEAN),
        ("WakeAlarmPresent", win32more.Foundation.BOOLEAN),
        ("AoAc", win32more.Foundation.BOOLEAN),
        ("DiskSpinDown", win32more.Foundation.BOOLEAN),
        ("HiberFileType", Byte),
        ("AoAcConnectivitySupported", win32more.Foundation.BOOLEAN),
        ("spare3", Byte * 6),
        ("SystemBatteriesPresent", win32more.Foundation.BOOLEAN),
        ("BatteriesAreShortTerm", win32more.Foundation.BOOLEAN),
        ("BatteryScale", win32more.System.Power.BATTERY_REPORTING_SCALE * 3),
        ("AcOnLineWake", win32more.System.Power.SYSTEM_POWER_STATE),
        ("SoftLidWake", win32more.System.Power.SYSTEM_POWER_STATE),
        ("RtcWake", win32more.System.Power.SYSTEM_POWER_STATE),
        ("MinDeviceWakeState", win32more.System.Power.SYSTEM_POWER_STATE),
        ("DefaultLowLatencyWake", win32more.System.Power.SYSTEM_POWER_STATE),
    ]
    return SYSTEM_POWER_CAPABILITIES
def _define_SYSTEM_BATTERY_STATE_head():
    class SYSTEM_BATTERY_STATE(Structure):
        pass
    return SYSTEM_BATTERY_STATE
def _define_SYSTEM_BATTERY_STATE():
    SYSTEM_BATTERY_STATE = win32more.System.Power.SYSTEM_BATTERY_STATE_head
    SYSTEM_BATTERY_STATE._fields_ = [
        ("AcOnLine", win32more.Foundation.BOOLEAN),
        ("BatteryPresent", win32more.Foundation.BOOLEAN),
        ("Charging", win32more.Foundation.BOOLEAN),
        ("Discharging", win32more.Foundation.BOOLEAN),
        ("Spare1", win32more.Foundation.BOOLEAN * 3),
        ("Tag", Byte),
        ("MaxCapacity", UInt32),
        ("RemainingCapacity", UInt32),
        ("Rate", UInt32),
        ("EstimatedTime", UInt32),
        ("DefaultAlert1", UInt32),
        ("DefaultAlert2", UInt32),
    ]
    return SYSTEM_BATTERY_STATE
def _define_POWERBROADCAST_SETTING_head():
    class POWERBROADCAST_SETTING(Structure):
        pass
    return POWERBROADCAST_SETTING
def _define_POWERBROADCAST_SETTING():
    POWERBROADCAST_SETTING = win32more.System.Power.POWERBROADCAST_SETTING_head
    POWERBROADCAST_SETTING._fields_ = [
        ("PowerSetting", Guid),
        ("DataLength", UInt32),
        ("Data", Byte * 0),
    ]
    return POWERBROADCAST_SETTING
def _define_SYSTEM_POWER_STATUS_head():
    class SYSTEM_POWER_STATUS(Structure):
        pass
    return SYSTEM_POWER_STATUS
def _define_SYSTEM_POWER_STATUS():
    SYSTEM_POWER_STATUS = win32more.System.Power.SYSTEM_POWER_STATUS_head
    SYSTEM_POWER_STATUS._fields_ = [
        ("ACLineStatus", Byte),
        ("BatteryFlag", Byte),
        ("BatteryLifePercent", Byte),
        ("SystemStatusFlag", Byte),
        ("BatteryLifeTime", UInt32),
        ("BatteryFullLifeTime", UInt32),
    ]
    return SYSTEM_POWER_STATUS
def _define_CallNtPowerInformation():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Power.POWER_INFORMATION_LEVEL,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(("CallNtPowerInformation", windll["POWRPROF"]), ((1, 'InformationLevel'),(1, 'InputBuffer'),(1, 'InputBufferLength'),(1, 'OutputBuffer'),(1, 'OutputBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPwrCapabilities():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Power.SYSTEM_POWER_CAPABILITIES_head), use_last_error=True)(("GetPwrCapabilities", windll["POWRPROF"]), ((1, 'lpspc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerDeterminePlatformRoleEx():
    try:
        return WINFUNCTYPE(win32more.System.Power.POWER_PLATFORM_ROLE,win32more.System.Power.POWER_PLATFORM_ROLE_VERSION, use_last_error=False)(("PowerDeterminePlatformRoleEx", windll["POWRPROF"]), ((1, 'Version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerRegisterSuspendResumeNotification():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.HANDLE,POINTER(c_void_p), use_last_error=False)(("PowerRegisterSuspendResumeNotification", windll["POWRPROF"]), ((1, 'Flags'),(1, 'Recipient'),(1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerUnregisterSuspendResumeNotification():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Power.HPOWERNOTIFY, use_last_error=False)(("PowerUnregisterSuspendResumeNotification", windll["POWRPROF"]), ((1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadACValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadACValue", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Type'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadDCValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadDCValue", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Type'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteACValueIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteACValueIndex", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'AcValueIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteDCValueIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteDCValueIndex", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'DcValueIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerGetActiveScheme():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(POINTER(Guid)), use_last_error=False)(("PowerGetActiveScheme", windll["POWRPROF"]), ((1, 'UserRootPowerKey'),(1, 'ActivePolicyGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerSetActiveScheme():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid), use_last_error=False)(("PowerSetActiveScheme", windll["POWRPROF"]), ((1, 'UserRootPowerKey'),(1, 'SchemeGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerSettingRegisterNotification():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.System.Power.POWER_SETTING_REGISTER_NOTIFICATION_FLAGS,win32more.Foundation.HANDLE,POINTER(c_void_p), use_last_error=False)(("PowerSettingRegisterNotification", windll["POWRPROF"]), ((1, 'SettingGuid'),(1, 'Flags'),(1, 'Recipient'),(1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerSettingUnregisterNotification():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Power.HPOWERNOTIFY, use_last_error=False)(("PowerSettingUnregisterNotification", windll["POWRPROF"]), ((1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerRegisterForEffectivePowerModeNotifications():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Power.EFFECTIVE_POWER_MODE_CALLBACK,c_void_p,POINTER(c_void_p), use_last_error=False)(("PowerRegisterForEffectivePowerModeNotifications", windll["POWRPROF"]), ((1, 'Version'),(1, 'Callback'),(1, 'Context'),(1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerUnregisterFromEffectivePowerModeNotifications():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PowerUnregisterFromEffectivePowerModeNotifications", windll["POWRPROF"]), ((1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPwrDiskSpindownRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("GetPwrDiskSpindownRange", windll["POWRPROF"]), ((1, 'puiMax'),(1, 'puiMin'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumPwrSchemes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.System.Power.PWRSCHEMESENUMPROC,win32more.Foundation.LPARAM, use_last_error=True)(("EnumPwrSchemes", windll["POWRPROF"]), ((1, 'lpfn'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadGlobalPwrPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Power.GLOBAL_POWER_POLICY_head), use_last_error=True)(("ReadGlobalPwrPolicy", windll["POWRPROF"]), ((1, 'pGlobalPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadPwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,POINTER(win32more.System.Power.POWER_POLICY_head), use_last_error=True)(("ReadPwrScheme", windll["POWRPROF"]), ((1, 'uiID'),(1, 'pPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WritePwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Power.POWER_POLICY_head), use_last_error=True)(("WritePwrScheme", windll["POWRPROF"]), ((1, 'puiID'),(1, 'lpszSchemeName'),(1, 'lpszDescription'),(1, 'lpScheme'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteGlobalPwrPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Power.GLOBAL_POWER_POLICY_head), use_last_error=True)(("WriteGlobalPwrPolicy", windll["POWRPROF"]), ((1, 'pGlobalPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeletePwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32, use_last_error=True)(("DeletePwrScheme", windll["POWRPROF"]), ((1, 'uiID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetActivePwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(UInt32), use_last_error=True)(("GetActivePwrScheme", windll["POWRPROF"]), ((1, 'puiID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetActivePwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,POINTER(win32more.System.Power.GLOBAL_POWER_POLICY_head),POINTER(win32more.System.Power.POWER_POLICY_head), use_last_error=True)(("SetActivePwrScheme", windll["POWRPROF"]), ((1, 'uiID'),(1, 'pGlobalPowerPolicy'),(1, 'pPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsPwrSuspendAllowed():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN, use_last_error=False)(("IsPwrSuspendAllowed", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsPwrHibernateAllowed():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN, use_last_error=False)(("IsPwrHibernateAllowed", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsPwrShutdownAllowed():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN, use_last_error=False)(("IsPwrShutdownAllowed", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsAdminOverrideActive():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Power.ADMINISTRATOR_POWER_POLICY_head), use_last_error=False)(("IsAdminOverrideActive", windll["POWRPROF"]), ((1, 'papp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSuspendState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.BOOLEAN,win32more.Foundation.BOOLEAN,win32more.Foundation.BOOLEAN, use_last_error=True)(("SetSuspendState", windll["POWRPROF"]), ((1, 'bHibernate'),(1, 'bForce'),(1, 'bWakeupEventsDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPowerPolicies():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Power.GLOBAL_POWER_POLICY_head),POINTER(win32more.System.Power.POWER_POLICY_head), use_last_error=True)(("GetCurrentPowerPolicies", windll["POWRPROF"]), ((1, 'pGlobalPowerPolicy'),(1, 'pPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CanUserWritePwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN, use_last_error=True)(("CanUserWritePwrScheme", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadProcessorPwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,POINTER(win32more.System.Power.MACHINE_PROCESSOR_POWER_POLICY_head), use_last_error=True)(("ReadProcessorPwrScheme", windll["POWRPROF"]), ((1, 'uiID'),(1, 'pMachineProcessorPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteProcessorPwrScheme():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,POINTER(win32more.System.Power.MACHINE_PROCESSOR_POWER_POLICY_head), use_last_error=True)(("WriteProcessorPwrScheme", windll["POWRPROF"]), ((1, 'uiID'),(1, 'pMachineProcessorPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValidatePowerPolicies():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Power.GLOBAL_POWER_POLICY_head),POINTER(win32more.System.Power.POWER_POLICY_head), use_last_error=False)(("ValidatePowerPolicies", windll["POWRPROF"]), ((1, 'pGlobalPowerPolicy'),(1, 'pPowerPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerIsSettingRangeDefined():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(Guid),POINTER(Guid), use_last_error=False)(("PowerIsSettingRangeDefined", windll["POWRPROF"]), ((1, 'SubKeyGuid'),(1, 'SettingGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerSettingAccessCheckEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Power.POWER_DATA_ACCESSOR,POINTER(Guid),win32more.System.Registry.REG_SAM_FLAGS, use_last_error=False)(("PowerSettingAccessCheckEx", windll["POWRPROF"]), ((1, 'AccessFlags'),(1, 'PowerGuid'),(1, 'AccessType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerSettingAccessCheck():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Power.POWER_DATA_ACCESSOR,POINTER(Guid), use_last_error=False)(("PowerSettingAccessCheck", windll["POWRPROF"]), ((1, 'AccessFlags'),(1, 'PowerGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadACValueIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadACValueIndex", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'AcValueIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadDCValueIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadDCValueIndex", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'DcValueIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadFriendlyName():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadFriendlyName", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadDescription():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadDescription", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadPossibleValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(UInt32),UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadPossibleValue", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Type'),(1, 'PossibleSettingIndex'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadPossibleFriendlyName():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadPossibleFriendlyName", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'PossibleSettingIndex'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadPossibleDescription():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadPossibleDescription", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'PossibleSettingIndex'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadValueMin():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadValueMin", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'ValueMinimum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadValueMax():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadValueMax", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'ValueMaximum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadValueIncrement():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadValueIncrement", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'ValueIncrement'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadValueUnitsSpecifier():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadValueUnitsSpecifier", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadACDefaultIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadACDefaultIndex", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemePersonalityGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'AcDefaultIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadDCDefaultIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),POINTER(UInt32), use_last_error=False)(("PowerReadDCDefaultIndex", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemePersonalityGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'DcDefaultIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadIconResourceSpecifier():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerReadIconResourceSpecifier", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReadSettingAttributes():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(Guid), use_last_error=False)(("PowerReadSettingAttributes", windll["POWRPROF"]), ((1, 'SubGroupGuid'),(1, 'PowerSettingGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteFriendlyName():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),c_char_p_no,UInt32, use_last_error=False)(("PowerWriteFriendlyName", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteDescription():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),c_char_p_no,UInt32, use_last_error=False)(("PowerWriteDescription", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWritePossibleValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32,UInt32,c_char_p_no,UInt32, use_last_error=False)(("PowerWritePossibleValue", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Type'),(1, 'PossibleSettingIndex'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWritePossibleFriendlyName():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32,c_char_p_no,UInt32, use_last_error=False)(("PowerWritePossibleFriendlyName", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'PossibleSettingIndex'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWritePossibleDescription():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32,c_char_p_no,UInt32, use_last_error=False)(("PowerWritePossibleDescription", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'PossibleSettingIndex'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteValueMin():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteValueMin", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'ValueMinimum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteValueMax():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteValueMax", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'ValueMaximum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteValueIncrement():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteValueIncrement", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'ValueIncrement'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteValueUnitsSpecifier():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),c_char_p_no,UInt32, use_last_error=False)(("PowerWriteValueUnitsSpecifier", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteACDefaultIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteACDefaultIndex", windll["POWRPROF"]), ((1, 'RootSystemPowerKey'),(1, 'SchemePersonalityGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'DefaultAcIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteDCDefaultIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteDCDefaultIndex", windll["POWRPROF"]), ((1, 'RootSystemPowerKey'),(1, 'SchemePersonalityGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'DefaultDcIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteIconResourceSpecifier():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),POINTER(Guid),c_char_p_no,UInt32, use_last_error=False)(("PowerWriteIconResourceSpecifier", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerWriteSettingAttributes():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerWriteSettingAttributes", windll["POWRPROF"]), ((1, 'SubGroupGuid'),(1, 'PowerSettingGuid'),(1, 'Attributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerDuplicateScheme():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(POINTER(Guid)), use_last_error=False)(("PowerDuplicateScheme", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SourceSchemeGuid'),(1, 'DestinationSchemeGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerImportPowerScheme():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(POINTER(Guid)), use_last_error=False)(("PowerImportPowerScheme", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'ImportFileNamePath'),(1, 'DestinationSchemeGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerDeleteScheme():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid), use_last_error=False)(("PowerDeleteScheme", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerRemovePowerSetting():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(Guid), use_last_error=False)(("PowerRemovePowerSetting", windll["POWRPROF"]), ((1, 'PowerSettingSubKeyGuid'),(1, 'PowerSettingGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerCreateSetting():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid), use_last_error=False)(("PowerCreateSetting", windll["POWRPROF"]), ((1, 'RootSystemPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerCreatePossibleSetting():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(("PowerCreatePossibleSetting", windll["POWRPROF"]), ((1, 'RootSystemPowerKey'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'PowerSettingGuid'),(1, 'PossibleSettingIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerEnumerate():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Registry.HKEY,POINTER(Guid),POINTER(Guid),win32more.System.Power.POWER_DATA_ACCESSOR,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("PowerEnumerate", windll["POWRPROF"]), ((1, 'RootPowerKey'),(1, 'SchemeGuid'),(1, 'SubGroupOfPowerSettingsGuid'),(1, 'AccessFlags'),(1, 'Index'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerOpenUserPowerKey():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Registry.HKEY),UInt32,win32more.Foundation.BOOL, use_last_error=False)(("PowerOpenUserPowerKey", windll["POWRPROF"]), ((1, 'phUserPowerKey'),(1, 'Access'),(1, 'OpenExisting'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerOpenSystemPowerKey():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Registry.HKEY),UInt32,win32more.Foundation.BOOL, use_last_error=False)(("PowerOpenSystemPowerKey", windll["POWRPROF"]), ((1, 'phSystemPowerKey'),(1, 'Access'),(1, 'OpenExisting'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerCanRestoreIndividualDefaultPowerScheme():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid), use_last_error=False)(("PowerCanRestoreIndividualDefaultPowerScheme", windll["POWRPROF"]), ((1, 'SchemeGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerRestoreIndividualDefaultPowerScheme():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid), use_last_error=False)(("PowerRestoreIndividualDefaultPowerScheme", windll["POWRPROF"]), ((1, 'SchemeGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerRestoreDefaultPowerSchemes():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("PowerRestoreDefaultPowerSchemes", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReplaceDefaultPowerSchemes():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("PowerReplaceDefaultPowerSchemes", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerDeterminePlatformRole():
    try:
        return WINFUNCTYPE(win32more.System.Power.POWER_PLATFORM_ROLE, use_last_error=False)(("PowerDeterminePlatformRole", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevicePowerEnumDevices():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32,UInt32,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("DevicePowerEnumDevices", windll["POWRPROF"]), ((1, 'QueryIndex'),(1, 'QueryInterpretationFlags'),(1, 'QueryFlags'),(1, 'pReturnBuffer'),(1, 'pBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevicePowerSetDeviceState():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_void_p, use_last_error=True)(("DevicePowerSetDeviceState", windll["POWRPROF"]), ((1, 'DeviceDescription'),(1, 'SetFlags'),(1, 'SetData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevicePowerOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,UInt32, use_last_error=False)(("DevicePowerOpen", windll["POWRPROF"]), ((1, 'DebugMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevicePowerClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN, use_last_error=False)(("DevicePowerClose", windll["POWRPROF"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerReportThermalEvent():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Power.THERMAL_EVENT_head), use_last_error=False)(("PowerReportThermalEvent", windll["POWRPROF"]), ((1, 'Event'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterPowerSettingNotification():
    try:
        return WINFUNCTYPE(win32more.System.Power.HPOWERNOTIFY,win32more.Foundation.HANDLE,POINTER(Guid),UInt32, use_last_error=True)(("RegisterPowerSettingNotification", windll["USER32"]), ((1, 'hRecipient'),(1, 'PowerSettingGuid'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterPowerSettingNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Power.HPOWERNOTIFY, use_last_error=True)(("UnregisterPowerSettingNotification", windll["USER32"]), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterSuspendResumeNotification():
    try:
        return WINFUNCTYPE(win32more.System.Power.HPOWERNOTIFY,win32more.Foundation.HANDLE,UInt32, use_last_error=True)(("RegisterSuspendResumeNotification", windll["USER32"]), ((1, 'hRecipient'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterSuspendResumeNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Power.HPOWERNOTIFY, use_last_error=True)(("UnregisterSuspendResumeNotification", windll["USER32"]), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RequestWakeupLatency():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Power.LATENCY_TIME, use_last_error=False)(("RequestWakeupLatency", windll["KERNEL32"]), ((1, 'latency'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsSystemResumeAutomatic():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("IsSystemResumeAutomatic", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadExecutionState():
    try:
        return WINFUNCTYPE(win32more.System.Power.EXECUTION_STATE,win32more.System.Power.EXECUTION_STATE, use_last_error=False)(("SetThreadExecutionState", windll["KERNEL32"]), ((1, 'esFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerCreateRequest():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.System.Threading.REASON_CONTEXT_head), use_last_error=True)(("PowerCreateRequest", windll["KERNEL32"]), ((1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerSetRequest():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Power.POWER_REQUEST_TYPE, use_last_error=True)(("PowerSetRequest", windll["KERNEL32"]), ((1, 'PowerRequest'),(1, 'RequestType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PowerClearRequest():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Power.POWER_REQUEST_TYPE, use_last_error=True)(("PowerClearRequest", windll["KERNEL32"]), ((1, 'PowerRequest'),(1, 'RequestType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDevicePowerState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("GetDevicePowerState", windll["KERNEL32"]), ((1, 'hDevice'),(1, 'pfOn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSystemPowerState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=True)(("SetSystemPowerState", windll["KERNEL32"]), ((1, 'fSuspend'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemPowerStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Power.SYSTEM_POWER_STATUS_head), use_last_error=True)(("GetSystemPowerStatus", windll["KERNEL32"]), ((1, 'lpSystemPowerStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PROCESSOR_NUMBER_PKEY",
    "GUID_DEVICE_BATTERY",
    "GUID_DEVICE_APPLICATIONLAUNCH_BUTTON",
    "GUID_DEVICE_SYS_BUTTON",
    "GUID_DEVICE_LID",
    "GUID_DEVICE_THERMAL_ZONE",
    "GUID_DEVICE_FAN",
    "GUID_DEVICE_PROCESSOR",
    "GUID_DEVICE_MEMORY",
    "GUID_DEVICE_ACPI_TIME",
    "GUID_DEVICE_MESSAGE_INDICATOR",
    "GUID_CLASS_INPUT",
    "GUID_DEVINTERFACE_THERMAL_COOLING",
    "GUID_DEVINTERFACE_THERMAL_MANAGER",
    "BATTERY_UNKNOWN_CAPACITY",
    "UNKNOWN_CAPACITY",
    "BATTERY_SYSTEM_BATTERY",
    "BATTERY_CAPACITY_RELATIVE",
    "BATTERY_IS_SHORT_TERM",
    "BATTERY_SEALED",
    "BATTERY_SET_CHARGE_SUPPORTED",
    "BATTERY_SET_DISCHARGE_SUPPORTED",
    "BATTERY_SET_CHARGINGSOURCE_SUPPORTED",
    "BATTERY_SET_CHARGER_ID_SUPPORTED",
    "BATTERY_UNKNOWN_TIME",
    "BATTERY_UNKNOWN_CURRENT",
    "UNKNOWN_CURRENT",
    "BATTERY_USB_CHARGER_STATUS_FN_DEFAULT_USB",
    "BATTERY_USB_CHARGER_STATUS_UCM_PD",
    "BATTERY_UNKNOWN_VOLTAGE",
    "BATTERY_UNKNOWN_RATE",
    "UNKNOWN_RATE",
    "UNKNOWN_VOLTAGE",
    "BATTERY_POWER_ON_LINE",
    "BATTERY_DISCHARGING",
    "BATTERY_CHARGING",
    "BATTERY_CRITICAL",
    "MAX_BATTERY_STRING_SIZE",
    "IOCTL_BATTERY_QUERY_TAG",
    "IOCTL_BATTERY_QUERY_INFORMATION",
    "IOCTL_BATTERY_SET_INFORMATION",
    "IOCTL_BATTERY_QUERY_STATUS",
    "IOCTL_BATTERY_CHARGING_SOURCE_CHANGE",
    "BATTERY_TAG_INVALID",
    "MAX_ACTIVE_COOLING_LEVELS",
    "ACTIVE_COOLING",
    "PASSIVE_COOLING",
    "TZ_ACTIVATION_REASON_THERMAL",
    "TZ_ACTIVATION_REASON_CURRENT",
    "THERMAL_POLICY_VERSION_1",
    "THERMAL_POLICY_VERSION_2",
    "IOCTL_THERMAL_QUERY_INFORMATION",
    "IOCTL_THERMAL_SET_COOLING_POLICY",
    "IOCTL_RUN_ACTIVE_COOLING_METHOD",
    "IOCTL_THERMAL_SET_PASSIVE_LIMIT",
    "IOCTL_THERMAL_READ_TEMPERATURE",
    "IOCTL_THERMAL_READ_POLICY",
    "IOCTL_QUERY_LID",
    "IOCTL_NOTIFY_SWITCH_EVENT",
    "IOCTL_GET_SYS_BUTTON_CAPS",
    "IOCTL_GET_SYS_BUTTON_EVENT",
    "SYS_BUTTON_POWER",
    "SYS_BUTTON_SLEEP",
    "SYS_BUTTON_LID",
    "SYS_BUTTON_WAKE",
    "SYS_BUTTON_LID_STATE_MASK",
    "SYS_BUTTON_LID_OPEN",
    "SYS_BUTTON_LID_CLOSED",
    "SYS_BUTTON_LID_INITIAL",
    "SYS_BUTTON_LID_CHANGED",
    "IOCTL_GET_PROCESSOR_OBJ_INFO",
    "THERMAL_COOLING_INTERFACE_VERSION",
    "THERMAL_DEVICE_INTERFACE_VERSION",
    "IOCTL_SET_SYS_MESSAGE_INDICATOR",
    "IOCTL_SET_WAKE_ALARM_VALUE",
    "IOCTL_SET_WAKE_ALARM_POLICY",
    "IOCTL_GET_WAKE_ALARM_VALUE",
    "IOCTL_GET_WAKE_ALARM_POLICY",
    "ACPI_TIME_ADJUST_DAYLIGHT",
    "ACPI_TIME_IN_DAYLIGHT",
    "ACPI_TIME_ZONE_UNKNOWN",
    "IOCTL_ACPI_GET_REAL_TIME",
    "IOCTL_ACPI_SET_REAL_TIME",
    "IOCTL_GET_WAKE_ALARM_SYSTEM_POWERSTATE",
    "BATTERY_STATUS_WMI_GUID",
    "BATTERY_RUNTIME_WMI_GUID",
    "BATTERY_TEMPERATURE_WMI_GUID",
    "BATTERY_FULL_CHARGED_CAPACITY_WMI_GUID",
    "BATTERY_CYCLE_COUNT_WMI_GUID",
    "BATTERY_STATIC_DATA_WMI_GUID",
    "BATTERY_STATUS_CHANGE_WMI_GUID",
    "BATTERY_TAG_CHANGE_WMI_GUID",
    "BATTERY_MINIPORT_UPDATE_DATA_VER_1",
    "BATTERY_MINIPORT_UPDATE_DATA_VER_2",
    "BATTERY_CLASS_MAJOR_VERSION",
    "BATTERY_CLASS_MINOR_VERSION",
    "BATTERY_CLASS_MINOR_VERSION_1",
    "GUID_DEVICE_ENERGY_METER",
    "IOCTL_EMI_GET_VERSION",
    "IOCTL_EMI_GET_METADATA_SIZE",
    "IOCTL_EMI_GET_METADATA",
    "IOCTL_EMI_GET_MEASUREMENT",
    "EMI_NAME_MAX",
    "EMI_VERSION_V1",
    "EMI_VERSION_V2",
    "EFFECTIVE_POWER_MODE_V1",
    "EFFECTIVE_POWER_MODE_V2",
    "EnableSysTrayBatteryMeter",
    "EnableMultiBatteryDisplay",
    "EnablePasswordLogon",
    "EnableWakeOnRing",
    "EnableVideoDimDisplay",
    "POWER_ATTRIBUTE_HIDE",
    "POWER_ATTRIBUTE_SHOW_AOAC",
    "DEVICEPOWER_HARDWAREID",
    "DEVICEPOWER_AND_OPERATION",
    "DEVICEPOWER_FILTER_DEVICES_PRESENT",
    "DEVICEPOWER_FILTER_HARDWARE",
    "DEVICEPOWER_FILTER_WAKEENABLED",
    "DEVICEPOWER_FILTER_WAKEPROGRAMMABLE",
    "DEVICEPOWER_FILTER_ON_NAME",
    "DEVICEPOWER_SET_WAKEENABLED",
    "DEVICEPOWER_CLEAR_WAKEENABLED",
    "PDCAP_S0_SUPPORTED",
    "PDCAP_S1_SUPPORTED",
    "PDCAP_S2_SUPPORTED",
    "PDCAP_S3_SUPPORTED",
    "PDCAP_WAKE_FROM_S0_SUPPORTED",
    "PDCAP_WAKE_FROM_S1_SUPPORTED",
    "PDCAP_WAKE_FROM_S2_SUPPORTED",
    "PDCAP_WAKE_FROM_S3_SUPPORTED",
    "PDCAP_S4_SUPPORTED",
    "PDCAP_S5_SUPPORTED",
    "THERMAL_EVENT_VERSION",
    "POWER_PLATFORM_ROLE_VERSION",
    "POWER_PLATFORM_ROLE_V1",
    "POWER_PLATFORM_ROLE_V2",
    "POWER_SETTING_REGISTER_NOTIFICATION_FLAGS",
    "DEVICE_NOTIFY_SERVICE_HANDLE",
    "DEVICE_NOTIFY_CALLBACK",
    "DEVICE_NOTIFY_WINDOW_HANDLE",
    "EXECUTION_STATE",
    "ES_AWAYMODE_REQUIRED",
    "ES_CONTINUOUS",
    "ES_DISPLAY_REQUIRED",
    "ES_SYSTEM_REQUIRED",
    "ES_USER_PRESENT",
    "POWER_ACTION_POLICY_EVENT_CODE",
    "POWER_FORCE_TRIGGER_RESET",
    "POWER_LEVEL_USER_NOTIFY_EXEC",
    "POWER_LEVEL_USER_NOTIFY_SOUND",
    "POWER_LEVEL_USER_NOTIFY_TEXT",
    "POWER_USER_NOTIFY_BUTTON",
    "POWER_USER_NOTIFY_SHUTDOWN",
    "HPOWERNOTIFY",
    "EFFECTIVE_POWER_MODE",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeBatterySaver",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeBetterBattery",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeBalanced",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeHighPerformance",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeMaxPerformance",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeGameMode",
    "EFFECTIVE_POWER_MODE_EffectivePowerModeMixedReality",
    "EFFECTIVE_POWER_MODE_CALLBACK",
    "GLOBAL_MACHINE_POWER_POLICY",
    "GLOBAL_USER_POWER_POLICY",
    "GLOBAL_POWER_POLICY",
    "MACHINE_POWER_POLICY",
    "MACHINE_PROCESSOR_POWER_POLICY",
    "USER_POWER_POLICY",
    "POWER_POLICY",
    "PWRSCHEMESENUMPROC_V1",
    "PWRSCHEMESENUMPROC",
    "POWER_DATA_ACCESSOR",
    "ACCESS_AC_POWER_SETTING_INDEX",
    "ACCESS_DC_POWER_SETTING_INDEX",
    "ACCESS_FRIENDLY_NAME",
    "ACCESS_DESCRIPTION",
    "ACCESS_POSSIBLE_POWER_SETTING",
    "ACCESS_POSSIBLE_POWER_SETTING_FRIENDLY_NAME",
    "ACCESS_POSSIBLE_POWER_SETTING_DESCRIPTION",
    "ACCESS_DEFAULT_AC_POWER_SETTING",
    "ACCESS_DEFAULT_DC_POWER_SETTING",
    "ACCESS_POSSIBLE_VALUE_MIN",
    "ACCESS_POSSIBLE_VALUE_MAX",
    "ACCESS_POSSIBLE_VALUE_INCREMENT",
    "ACCESS_POSSIBLE_VALUE_UNITS",
    "ACCESS_ICON_RESOURCE",
    "ACCESS_DEFAULT_SECURITY_DESCRIPTOR",
    "ACCESS_ATTRIBUTES",
    "ACCESS_SCHEME",
    "ACCESS_SUBGROUP",
    "ACCESS_INDIVIDUAL_SETTING",
    "ACCESS_ACTIVE_SCHEME",
    "ACCESS_CREATE_SCHEME",
    "ACCESS_AC_POWER_SETTING_MAX",
    "ACCESS_DC_POWER_SETTING_MAX",
    "ACCESS_AC_POWER_SETTING_MIN",
    "ACCESS_DC_POWER_SETTING_MIN",
    "ACCESS_PROFILE",
    "ACCESS_OVERLAY_SCHEME",
    "ACCESS_ACTIVE_OVERLAY_SCHEME",
    "PDEVICE_NOTIFY_CALLBACK_ROUTINE",
    "DEVICE_NOTIFY_SUBSCRIBE_PARAMETERS",
    "THERMAL_EVENT",
    "BATTERY_QUERY_INFORMATION_LEVEL",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryInformation",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryGranularityInformation",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryTemperature",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryEstimatedTime",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryDeviceName",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryManufactureDate",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryManufactureName",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatteryUniqueID",
    "BATTERY_QUERY_INFORMATION_LEVEL_BatterySerialNumber",
    "BATTERY_QUERY_INFORMATION",
    "BATTERY_INFORMATION",
    "BATTERY_CHARGING_SOURCE_TYPE",
    "BatteryChargingSourceType_AC",
    "BatteryChargingSourceType_USB",
    "BatteryChargingSourceType_Wireless",
    "BatteryChargingSourceType_Max",
    "BATTERY_CHARGING_SOURCE",
    "BATTERY_CHARGING_SOURCE_INFORMATION",
    "USB_CHARGER_PORT",
    "UsbChargerPort_Legacy",
    "UsbChargerPort_TypeC",
    "UsbChargerPort_Max",
    "BATTERY_SET_INFORMATION_LEVEL",
    "BATTERY_SET_INFORMATION_LEVEL_BatteryCriticalBias",
    "BATTERY_SET_INFORMATION_LEVEL_BatteryCharge",
    "BATTERY_SET_INFORMATION_LEVEL_BatteryDischarge",
    "BATTERY_SET_INFORMATION_LEVEL_BatteryChargingSource",
    "BATTERY_SET_INFORMATION_LEVEL_BatteryChargerId",
    "BATTERY_SET_INFORMATION_LEVEL_BatteryChargerStatus",
    "BATTERY_SET_INFORMATION",
    "BATTERY_CHARGER_STATUS",
    "BATTERY_USB_CHARGER_STATUS",
    "BATTERY_WAIT_STATUS",
    "BATTERY_STATUS",
    "BATTERY_MANUFACTURE_DATE",
    "THERMAL_INFORMATION",
    "THERMAL_WAIT_READ",
    "THERMAL_POLICY",
    "PROCESSOR_OBJECT_INFO",
    "PROCESSOR_OBJECT_INFO_EX",
    "WAKE_ALARM_INFORMATION",
    "ACPI_REAL_TIME",
    "EMI_MEASUREMENT_UNIT",
    "EMI_MEASUREMENT_UNIT_EmiMeasurementUnitPicowattHours",
    "EMI_VERSION",
    "EMI_METADATA_SIZE",
    "EMI_CHANNEL_MEASUREMENT_DATA",
    "EMI_METADATA_V1",
    "EMI_CHANNEL_V2",
    "EMI_METADATA_V2",
    "EMI_MEASUREMENT_DATA_V2",
    "SYSTEM_POWER_STATE",
    "SYSTEM_POWER_STATE_PowerSystemUnspecified",
    "SYSTEM_POWER_STATE_PowerSystemWorking",
    "SYSTEM_POWER_STATE_PowerSystemSleeping1",
    "SYSTEM_POWER_STATE_PowerSystemSleeping2",
    "SYSTEM_POWER_STATE_PowerSystemSleeping3",
    "SYSTEM_POWER_STATE_PowerSystemHibernate",
    "SYSTEM_POWER_STATE_PowerSystemShutdown",
    "SYSTEM_POWER_STATE_PowerSystemMaximum",
    "POWER_ACTION",
    "POWER_ACTION_PowerActionNone",
    "POWER_ACTION_PowerActionReserved",
    "POWER_ACTION_PowerActionSleep",
    "POWER_ACTION_PowerActionHibernate",
    "POWER_ACTION_PowerActionShutdown",
    "POWER_ACTION_PowerActionShutdownReset",
    "POWER_ACTION_PowerActionShutdownOff",
    "POWER_ACTION_PowerActionWarmEject",
    "POWER_ACTION_PowerActionDisplayOff",
    "DEVICE_POWER_STATE",
    "DEVICE_POWER_STATE_PowerDeviceUnspecified",
    "DEVICE_POWER_STATE_PowerDeviceD0",
    "DEVICE_POWER_STATE_PowerDeviceD1",
    "DEVICE_POWER_STATE_PowerDeviceD2",
    "DEVICE_POWER_STATE_PowerDeviceD3",
    "DEVICE_POWER_STATE_PowerDeviceMaximum",
    "LATENCY_TIME",
    "LT_DONT_CARE",
    "LT_LOWEST_LATENCY",
    "POWER_REQUEST_TYPE",
    "POWER_REQUEST_TYPE_PowerRequestDisplayRequired",
    "POWER_REQUEST_TYPE_PowerRequestSystemRequired",
    "POWER_REQUEST_TYPE_PowerRequestAwayModeRequired",
    "POWER_REQUEST_TYPE_PowerRequestExecutionRequired",
    "CM_POWER_DATA",
    "POWER_INFORMATION_LEVEL",
    "POWER_INFORMATION_LEVEL_SystemPowerPolicyAc",
    "POWER_INFORMATION_LEVEL_SystemPowerPolicyDc",
    "POWER_INFORMATION_LEVEL_VerifySystemPolicyAc",
    "POWER_INFORMATION_LEVEL_VerifySystemPolicyDc",
    "POWER_INFORMATION_LEVEL_SystemPowerCapabilities",
    "POWER_INFORMATION_LEVEL_SystemBatteryState",
    "POWER_INFORMATION_LEVEL_SystemPowerStateHandler",
    "POWER_INFORMATION_LEVEL_ProcessorStateHandler",
    "POWER_INFORMATION_LEVEL_SystemPowerPolicyCurrent",
    "POWER_INFORMATION_LEVEL_AdministratorPowerPolicy",
    "POWER_INFORMATION_LEVEL_SystemReserveHiberFile",
    "POWER_INFORMATION_LEVEL_ProcessorInformation",
    "POWER_INFORMATION_LEVEL_SystemPowerInformation",
    "POWER_INFORMATION_LEVEL_ProcessorStateHandler2",
    "POWER_INFORMATION_LEVEL_LastWakeTime",
    "POWER_INFORMATION_LEVEL_LastSleepTime",
    "POWER_INFORMATION_LEVEL_SystemExecutionState",
    "POWER_INFORMATION_LEVEL_SystemPowerStateNotifyHandler",
    "POWER_INFORMATION_LEVEL_ProcessorPowerPolicyAc",
    "POWER_INFORMATION_LEVEL_ProcessorPowerPolicyDc",
    "POWER_INFORMATION_LEVEL_VerifyProcessorPowerPolicyAc",
    "POWER_INFORMATION_LEVEL_VerifyProcessorPowerPolicyDc",
    "POWER_INFORMATION_LEVEL_ProcessorPowerPolicyCurrent",
    "POWER_INFORMATION_LEVEL_SystemPowerStateLogging",
    "POWER_INFORMATION_LEVEL_SystemPowerLoggingEntry",
    "POWER_INFORMATION_LEVEL_SetPowerSettingValue",
    "POWER_INFORMATION_LEVEL_NotifyUserPowerSetting",
    "POWER_INFORMATION_LEVEL_PowerInformationLevelUnused0",
    "POWER_INFORMATION_LEVEL_SystemMonitorHiberBootPowerOff",
    "POWER_INFORMATION_LEVEL_SystemVideoState",
    "POWER_INFORMATION_LEVEL_TraceApplicationPowerMessage",
    "POWER_INFORMATION_LEVEL_TraceApplicationPowerMessageEnd",
    "POWER_INFORMATION_LEVEL_ProcessorPerfStates",
    "POWER_INFORMATION_LEVEL_ProcessorIdleStates",
    "POWER_INFORMATION_LEVEL_ProcessorCap",
    "POWER_INFORMATION_LEVEL_SystemWakeSource",
    "POWER_INFORMATION_LEVEL_SystemHiberFileInformation",
    "POWER_INFORMATION_LEVEL_TraceServicePowerMessage",
    "POWER_INFORMATION_LEVEL_ProcessorLoad",
    "POWER_INFORMATION_LEVEL_PowerShutdownNotification",
    "POWER_INFORMATION_LEVEL_MonitorCapabilities",
    "POWER_INFORMATION_LEVEL_SessionPowerInit",
    "POWER_INFORMATION_LEVEL_SessionDisplayState",
    "POWER_INFORMATION_LEVEL_PowerRequestCreate",
    "POWER_INFORMATION_LEVEL_PowerRequestAction",
    "POWER_INFORMATION_LEVEL_GetPowerRequestList",
    "POWER_INFORMATION_LEVEL_ProcessorInformationEx",
    "POWER_INFORMATION_LEVEL_NotifyUserModeLegacyPowerEvent",
    "POWER_INFORMATION_LEVEL_GroupPark",
    "POWER_INFORMATION_LEVEL_ProcessorIdleDomains",
    "POWER_INFORMATION_LEVEL_WakeTimerList",
    "POWER_INFORMATION_LEVEL_SystemHiberFileSize",
    "POWER_INFORMATION_LEVEL_ProcessorIdleStatesHv",
    "POWER_INFORMATION_LEVEL_ProcessorPerfStatesHv",
    "POWER_INFORMATION_LEVEL_ProcessorPerfCapHv",
    "POWER_INFORMATION_LEVEL_ProcessorSetIdle",
    "POWER_INFORMATION_LEVEL_LogicalProcessorIdling",
    "POWER_INFORMATION_LEVEL_UserPresence",
    "POWER_INFORMATION_LEVEL_PowerSettingNotificationName",
    "POWER_INFORMATION_LEVEL_GetPowerSettingValue",
    "POWER_INFORMATION_LEVEL_IdleResiliency",
    "POWER_INFORMATION_LEVEL_SessionRITState",
    "POWER_INFORMATION_LEVEL_SessionConnectNotification",
    "POWER_INFORMATION_LEVEL_SessionPowerCleanup",
    "POWER_INFORMATION_LEVEL_SessionLockState",
    "POWER_INFORMATION_LEVEL_SystemHiberbootState",
    "POWER_INFORMATION_LEVEL_PlatformInformation",
    "POWER_INFORMATION_LEVEL_PdcInvocation",
    "POWER_INFORMATION_LEVEL_MonitorInvocation",
    "POWER_INFORMATION_LEVEL_FirmwareTableInformationRegistered",
    "POWER_INFORMATION_LEVEL_SetShutdownSelectedTime",
    "POWER_INFORMATION_LEVEL_SuspendResumeInvocation",
    "POWER_INFORMATION_LEVEL_PlmPowerRequestCreate",
    "POWER_INFORMATION_LEVEL_ScreenOff",
    "POWER_INFORMATION_LEVEL_CsDeviceNotification",
    "POWER_INFORMATION_LEVEL_PlatformRole",
    "POWER_INFORMATION_LEVEL_LastResumePerformance",
    "POWER_INFORMATION_LEVEL_DisplayBurst",
    "POWER_INFORMATION_LEVEL_ExitLatencySamplingPercentage",
    "POWER_INFORMATION_LEVEL_RegisterSpmPowerSettings",
    "POWER_INFORMATION_LEVEL_PlatformIdleStates",
    "POWER_INFORMATION_LEVEL_ProcessorIdleVeto",
    "POWER_INFORMATION_LEVEL_PlatformIdleVeto",
    "POWER_INFORMATION_LEVEL_SystemBatteryStatePrecise",
    "POWER_INFORMATION_LEVEL_ThermalEvent",
    "POWER_INFORMATION_LEVEL_PowerRequestActionInternal",
    "POWER_INFORMATION_LEVEL_BatteryDeviceState",
    "POWER_INFORMATION_LEVEL_PowerInformationInternal",
    "POWER_INFORMATION_LEVEL_ThermalStandby",
    "POWER_INFORMATION_LEVEL_SystemHiberFileType",
    "POWER_INFORMATION_LEVEL_PhysicalPowerButtonPress",
    "POWER_INFORMATION_LEVEL_QueryPotentialDripsConstraint",
    "POWER_INFORMATION_LEVEL_EnergyTrackerCreate",
    "POWER_INFORMATION_LEVEL_EnergyTrackerQuery",
    "POWER_INFORMATION_LEVEL_UpdateBlackBoxRecorder",
    "POWER_INFORMATION_LEVEL_SessionAllowExternalDmaDevices",
    "POWER_INFORMATION_LEVEL_SendSuspendResumeNotification",
    "POWER_INFORMATION_LEVEL_PowerInformationLevelMaximum",
    "SYSTEM_POWER_CONDITION",
    "SYSTEM_POWER_CONDITION_PoAc",
    "SYSTEM_POWER_CONDITION_PoDc",
    "SYSTEM_POWER_CONDITION_PoHot",
    "SYSTEM_POWER_CONDITION_PoConditionMaximum",
    "SET_POWER_SETTING_VALUE",
    "POWER_PLATFORM_ROLE",
    "POWER_PLATFORM_ROLE_PlatformRoleUnspecified",
    "POWER_PLATFORM_ROLE_PlatformRoleDesktop",
    "POWER_PLATFORM_ROLE_PlatformRoleMobile",
    "POWER_PLATFORM_ROLE_PlatformRoleWorkstation",
    "POWER_PLATFORM_ROLE_PlatformRoleEnterpriseServer",
    "POWER_PLATFORM_ROLE_PlatformRoleSOHOServer",
    "POWER_PLATFORM_ROLE_PlatformRoleAppliancePC",
    "POWER_PLATFORM_ROLE_PlatformRolePerformanceServer",
    "POWER_PLATFORM_ROLE_PlatformRoleSlate",
    "POWER_PLATFORM_ROLE_PlatformRoleMaximum",
    "BATTERY_REPORTING_SCALE",
    "POWER_ACTION_POLICY",
    "SYSTEM_POWER_LEVEL",
    "SYSTEM_POWER_POLICY",
    "PROCESSOR_POWER_POLICY_INFO",
    "PROCESSOR_POWER_POLICY",
    "ADMINISTRATOR_POWER_POLICY",
    "SYSTEM_POWER_CAPABILITIES",
    "SYSTEM_BATTERY_STATE",
    "POWERBROADCAST_SETTING",
    "SYSTEM_POWER_STATUS",
    "CallNtPowerInformation",
    "GetPwrCapabilities",
    "PowerDeterminePlatformRoleEx",
    "PowerRegisterSuspendResumeNotification",
    "PowerUnregisterSuspendResumeNotification",
    "PowerReadACValue",
    "PowerReadDCValue",
    "PowerWriteACValueIndex",
    "PowerWriteDCValueIndex",
    "PowerGetActiveScheme",
    "PowerSetActiveScheme",
    "PowerSettingRegisterNotification",
    "PowerSettingUnregisterNotification",
    "PowerRegisterForEffectivePowerModeNotifications",
    "PowerUnregisterFromEffectivePowerModeNotifications",
    "GetPwrDiskSpindownRange",
    "EnumPwrSchemes",
    "ReadGlobalPwrPolicy",
    "ReadPwrScheme",
    "WritePwrScheme",
    "WriteGlobalPwrPolicy",
    "DeletePwrScheme",
    "GetActivePwrScheme",
    "SetActivePwrScheme",
    "IsPwrSuspendAllowed",
    "IsPwrHibernateAllowed",
    "IsPwrShutdownAllowed",
    "IsAdminOverrideActive",
    "SetSuspendState",
    "GetCurrentPowerPolicies",
    "CanUserWritePwrScheme",
    "ReadProcessorPwrScheme",
    "WriteProcessorPwrScheme",
    "ValidatePowerPolicies",
    "PowerIsSettingRangeDefined",
    "PowerSettingAccessCheckEx",
    "PowerSettingAccessCheck",
    "PowerReadACValueIndex",
    "PowerReadDCValueIndex",
    "PowerReadFriendlyName",
    "PowerReadDescription",
    "PowerReadPossibleValue",
    "PowerReadPossibleFriendlyName",
    "PowerReadPossibleDescription",
    "PowerReadValueMin",
    "PowerReadValueMax",
    "PowerReadValueIncrement",
    "PowerReadValueUnitsSpecifier",
    "PowerReadACDefaultIndex",
    "PowerReadDCDefaultIndex",
    "PowerReadIconResourceSpecifier",
    "PowerReadSettingAttributes",
    "PowerWriteFriendlyName",
    "PowerWriteDescription",
    "PowerWritePossibleValue",
    "PowerWritePossibleFriendlyName",
    "PowerWritePossibleDescription",
    "PowerWriteValueMin",
    "PowerWriteValueMax",
    "PowerWriteValueIncrement",
    "PowerWriteValueUnitsSpecifier",
    "PowerWriteACDefaultIndex",
    "PowerWriteDCDefaultIndex",
    "PowerWriteIconResourceSpecifier",
    "PowerWriteSettingAttributes",
    "PowerDuplicateScheme",
    "PowerImportPowerScheme",
    "PowerDeleteScheme",
    "PowerRemovePowerSetting",
    "PowerCreateSetting",
    "PowerCreatePossibleSetting",
    "PowerEnumerate",
    "PowerOpenUserPowerKey",
    "PowerOpenSystemPowerKey",
    "PowerCanRestoreIndividualDefaultPowerScheme",
    "PowerRestoreIndividualDefaultPowerScheme",
    "PowerRestoreDefaultPowerSchemes",
    "PowerReplaceDefaultPowerSchemes",
    "PowerDeterminePlatformRole",
    "DevicePowerEnumDevices",
    "DevicePowerSetDeviceState",
    "DevicePowerOpen",
    "DevicePowerClose",
    "PowerReportThermalEvent",
    "RegisterPowerSettingNotification",
    "UnregisterPowerSettingNotification",
    "RegisterSuspendResumeNotification",
    "UnregisterSuspendResumeNotification",
    "RequestWakeupLatency",
    "IsSystemResumeAutomatic",
    "SetThreadExecutionState",
    "PowerCreateRequest",
    "PowerSetRequest",
    "PowerClearRequest",
    "GetDevicePowerState",
    "SetSystemPowerState",
    "GetSystemPowerStatus",
]
