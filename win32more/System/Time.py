from win32more import *
import win32more.System.Time
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Time, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Time, name)
TSF_Hardware = 1
TSF_Authenticated = 2
TSF_IPv6 = 4
TSF_SignatureAuthenticated = 8
def _define_TIME_ZONE_INFORMATION_head():
    class TIME_ZONE_INFORMATION(Structure):
        pass
    return TIME_ZONE_INFORMATION
def _define_TIME_ZONE_INFORMATION():
    TIME_ZONE_INFORMATION = win32more.System.Time.TIME_ZONE_INFORMATION_head
    TIME_ZONE_INFORMATION._fields_ = [
        ("Bias", Int32),
        ("StandardName", Char * 32),
        ("StandardDate", win32more.Foundation.SYSTEMTIME),
        ("StandardBias", Int32),
        ("DaylightName", Char * 32),
        ("DaylightDate", win32more.Foundation.SYSTEMTIME),
        ("DaylightBias", Int32),
    ]
    return TIME_ZONE_INFORMATION
def _define_DYNAMIC_TIME_ZONE_INFORMATION_head():
    class DYNAMIC_TIME_ZONE_INFORMATION(Structure):
        pass
    return DYNAMIC_TIME_ZONE_INFORMATION
def _define_DYNAMIC_TIME_ZONE_INFORMATION():
    DYNAMIC_TIME_ZONE_INFORMATION = win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head
    DYNAMIC_TIME_ZONE_INFORMATION._fields_ = [
        ("Bias", Int32),
        ("StandardName", Char * 32),
        ("StandardDate", win32more.Foundation.SYSTEMTIME),
        ("StandardBias", Int32),
        ("DaylightName", Char * 32),
        ("DaylightDate", win32more.Foundation.SYSTEMTIME),
        ("DaylightBias", Int32),
        ("TimeZoneKeyName", Char * 128),
        ("DynamicDaylightTimeDisabled", win32more.Foundation.BOOLEAN),
    ]
    return DYNAMIC_TIME_ZONE_INFORMATION
def _define_SystemTimeToTzSpecificLocalTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("SystemTimeToTzSpecificLocalTime", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),(1, 'lpUniversalTime'),(1, 'lpLocalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TzSpecificLocalTimeToSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("TzSpecificLocalTimeToSystemTime", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),(1, 'lpLocalTime'),(1, 'lpUniversalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileTimeToSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("FileTimeToSystemTime", windll["KERNEL32"]), ((1, 'lpFileTime'),(1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemTimeToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=True)(("SystemTimeToFileTime", windll["KERNEL32"]), ((1, 'lpSystemTime'),(1, 'lpFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTimeZoneInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head), use_last_error=True)(("GetTimeZoneInformation", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTimeZoneInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head), use_last_error=True)(("SetTimeZoneInformation", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDynamicTimeZoneInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), use_last_error=True)(("SetDynamicTimeZoneInformation", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDynamicTimeZoneInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), use_last_error=True)(("GetDynamicTimeZoneInformation", windll["KERNEL32"]), ((1, 'pTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTimeZoneInformationForYear():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head), use_last_error=True)(("GetTimeZoneInformationForYear", windll["KERNEL32"]), ((1, 'wYear'),(1, 'pdtzi'),(1, 'ptzi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDynamicTimeZoneInformation():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), use_last_error=False)(("EnumDynamicTimeZoneInformation", windll["ADVAPI32"]), ((1, 'dwIndex'),(1, 'lpTimeZoneInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDynamicTimeZoneInformationEffectiveYears():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetDynamicTimeZoneInformationEffectiveYears", windll["ADVAPI32"]), ((1, 'lpTimeZoneInformation'),(1, 'FirstYear'),(1, 'LastYear'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemTimeToTzSpecificLocalTimeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("SystemTimeToTzSpecificLocalTimeEx", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),(1, 'lpUniversalTime'),(1, 'lpLocalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TzSpecificLocalTimeToSystemTimeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=True)(("TzSpecificLocalTimeToSystemTimeEx", windll["KERNEL32"]), ((1, 'lpTimeZoneInformation'),(1, 'lpLocalTime'),(1, 'lpUniversalTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalFileTimeToLocalSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(("LocalFileTimeToLocalSystemTime", windll["KERNEL32"]), ((1, 'timeZoneInformation'),(1, 'localFileTime'),(1, 'localSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalSystemTimeToLocalFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Time.TIME_ZONE_INFORMATION_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("LocalSystemTimeToLocalFileTime", windll["KERNEL32"]), ((1, 'timeZoneInformation'),(1, 'localSystemTime'),(1, 'localFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "TSF_Hardware",
    "TSF_Authenticated",
    "TSF_IPv6",
    "TSF_SignatureAuthenticated",
    "TIME_ZONE_INFORMATION",
    "DYNAMIC_TIME_ZONE_INFORMATION",
    "SystemTimeToTzSpecificLocalTime",
    "TzSpecificLocalTimeToSystemTime",
    "FileTimeToSystemTime",
    "SystemTimeToFileTime",
    "GetTimeZoneInformation",
    "SetTimeZoneInformation",
    "SetDynamicTimeZoneInformation",
    "GetDynamicTimeZoneInformation",
    "GetTimeZoneInformationForYear",
    "EnumDynamicTimeZoneInformation",
    "GetDynamicTimeZoneInformationEffectiveYears",
    "SystemTimeToTzSpecificLocalTimeEx",
    "TzSpecificLocalTimeToSystemTimeEx",
    "LocalFileTimeToLocalSystemTime",
    "LocalSystemTimeToLocalFileTime",
]
