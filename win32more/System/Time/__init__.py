from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Time
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
wszW32TimeRegKeyTimeProviders = 'System\\CurrentControlSet\\Services\\W32Time\\TimeProviders'
wszW32TimeRegKeyPolicyTimeProviders = 'Software\\Policies\\Microsoft\\W32Time\\TimeProviders'
wszW32TimeRegValueEnabled = 'Enabled'
wszW32TimeRegValueDllName = 'DllName'
wszW32TimeRegValueInputProvider = 'InputProvider'
wszW32TimeRegValueMetaDataProvider = 'MetaDataProvider'
TSF_Hardware = 1
TSF_Authenticated = 2
TSF_IPv6 = 4
TSF_SignatureAuthenticated = 8
def _define_SystemTimeToTzSpecificLocalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('SystemTimeToTzSpecificLocalTime', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),(1, 'lpUniversalTime'),(1, 'lpLocalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TzSpecificLocalTimeToSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('TzSpecificLocalTimeToSystemTime', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),(1, 'lpLocalTime'),(1, 'lpUniversalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileTimeToSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('FileTimeToSystemTime', windll['KERNEL32.dll']), ((1, 'lpFileTime'),(1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemTimeToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.FILETIME_head))(('SystemTimeToFileTime', windll['KERNEL32.dll']), ((1, 'lpSystemTime'),(1, 'lpFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTimeZoneInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head))(('GetTimeZoneInformation', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTimeZoneInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head))(('SetTimeZoneInformation', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDynamicTimeZoneInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head))(('SetDynamicTimeZoneInformation', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDynamicTimeZoneInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head))(('GetDynamicTimeZoneInformation', windll['KERNEL32.dll']), ((1, 'pTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTimeZoneInformationForYear():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head))(('GetTimeZoneInformationForYear', windll['KERNEL32.dll']), ((1, 'wYear'),(1, 'pdtzi'),(1, 'ptzi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDynamicTimeZoneInformation():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head))(('EnumDynamicTimeZoneInformation', windll['ADVAPI32.dll']), ((1, 'dwIndex'),(1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDynamicTimeZoneInformationEffectiveYears():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(UInt32),POINTER(UInt32))(('GetDynamicTimeZoneInformationEffectiveYears', windll['ADVAPI32.dll']), ((1, 'lpTimeZoneInformation'),(1, 'FirstYear'),(1, 'LastYear'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemTimeToTzSpecificLocalTimeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('SystemTimeToTzSpecificLocalTimeEx', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),(1, 'lpUniversalTime'),(1, 'lpLocalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TzSpecificLocalTimeToSystemTimeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('TzSpecificLocalTimeToSystemTimeEx', windll['KERNEL32.dll']), ((1, 'lpTimeZoneInformation'),(1, 'lpLocalTime'),(1, 'lpUniversalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalFileTimeToLocalSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head))(('LocalFileTimeToLocalSystemTime', windll['KERNEL32.dll']), ((1, 'timeZoneInformation'),(1, 'localFileTime'),(1, 'localSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalSystemTimeToLocalFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.FILETIME_head))(('LocalSystemTimeToLocalFileTime', windll['KERNEL32.dll']), ((1, 'timeZoneInformation'),(1, 'localSystemTime'),(1, 'localFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DYNAMIC_TIME_ZONE_INFORMATION_head():
    class DYNAMIC_TIME_ZONE_INFORMATION(Structure):
        pass
    return DYNAMIC_TIME_ZONE_INFORMATION
def _define_DYNAMIC_TIME_ZONE_INFORMATION():
    DYNAMIC_TIME_ZONE_INFORMATION = win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head
    DYNAMIC_TIME_ZONE_INFORMATION._fields_ = [
        ('Bias', Int32),
        ('StandardName', Char * 32),
        ('StandardDate', win32more.Foundation.SYSTEMTIME),
        ('StandardBias', Int32),
        ('DaylightName', Char * 32),
        ('DaylightDate', win32more.Foundation.SYSTEMTIME),
        ('DaylightBias', Int32),
        ('TimeZoneKeyName', Char * 128),
        ('DynamicDaylightTimeDisabled', win32more.Foundation.BOOLEAN),
    ]
    return DYNAMIC_TIME_ZONE_INFORMATION
def _define_TIME_ZONE_INFORMATION_head():
    class TIME_ZONE_INFORMATION(Structure):
        pass
    return TIME_ZONE_INFORMATION
def _define_TIME_ZONE_INFORMATION():
    TIME_ZONE_INFORMATION = win32more.System.Time.TIME_ZONE_INFORMATION_head
    TIME_ZONE_INFORMATION._fields_ = [
        ('Bias', Int32),
        ('StandardName', Char * 32),
        ('StandardDate', win32more.Foundation.SYSTEMTIME),
        ('StandardBias', Int32),
        ('DaylightName', Char * 32),
        ('DaylightDate', win32more.Foundation.SYSTEMTIME),
        ('DaylightBias', Int32),
    ]
    return TIME_ZONE_INFORMATION
__all__ = [
    "DYNAMIC_TIME_ZONE_INFORMATION",
    "EnumDynamicTimeZoneInformation",
    "FileTimeToSystemTime",
    "GetDynamicTimeZoneInformation",
    "GetDynamicTimeZoneInformationEffectiveYears",
    "GetTimeZoneInformation",
    "GetTimeZoneInformationForYear",
    "LocalFileTimeToLocalSystemTime",
    "LocalSystemTimeToLocalFileTime",
    "SetDynamicTimeZoneInformation",
    "SetTimeZoneInformation",
    "SystemTimeToFileTime",
    "SystemTimeToTzSpecificLocalTime",
    "SystemTimeToTzSpecificLocalTimeEx",
    "TIME_ZONE_INFORMATION",
    "TSF_Authenticated",
    "TSF_Hardware",
    "TSF_IPv6",
    "TSF_SignatureAuthenticated",
    "TzSpecificLocalTimeToSystemTime",
    "TzSpecificLocalTimeToSystemTimeEx",
    "wszW32TimeRegKeyPolicyTimeProviders",
    "wszW32TimeRegKeyTimeProviders",
    "wszW32TimeRegValueDllName",
    "wszW32TimeRegValueEnabled",
    "wszW32TimeRegValueInputProvider",
    "wszW32TimeRegValueMetaDataProvider",
]
