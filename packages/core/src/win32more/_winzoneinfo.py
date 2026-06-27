from collections.abc import Iterable
from datetime import datetime, timedelta, tzinfo

from win32more import WinError
from win32more.Windows.Win32.Foundation import ERROR_NO_MORE_ITEMS, ERROR_SUCCESS, SYSTEMTIME
from win32more.Windows.Win32.System.Time import (
    DYNAMIC_TIME_ZONE_INFORMATION,
    TIME_ZONE_ID_INVALID,
    TIME_ZONE_INFORMATION,
    EnumDynamicTimeZoneInformation,
    GetDynamicTimeZoneInformation,
    GetTimeZoneInformationForYear,
    SystemTimeToTzSpecificLocalTimeEx,
    TzSpecificLocalTimeToSystemTimeEx,
)


def system_time_to_tz_specific_local_time_ex(dtz: DYNAMIC_TIME_ZONE_INFORMATION, utc: datetime) -> datetime:
    utc_st = datetime_to_systemtime(utc)
    local_st = SYSTEMTIME()
    if not SystemTimeToTzSpecificLocalTimeEx(dtz, utc_st, local_st):
        raise WinError()
    return systemtime_to_datetime(local_st).replace(microsecond=utc.microsecond)


def tz_specific_local_time_to_system_time_ex(dtz: DYNAMIC_TIME_ZONE_INFORMATION, local: datetime) -> datetime:
    local_st = datetime_to_systemtime(local)
    utc_st = SYSTEMTIME()
    if not TzSpecificLocalTimeToSystemTimeEx(dtz, local_st, utc_st):
        raise WinError()
    return systemtime_to_datetime(utc_st).replace(microsecond=local.microsecond)


def get_time_zone_information_for_year(year: int, dtz: DYNAMIC_TIME_ZONE_INFORMATION) -> TIME_ZONE_INFORMATION:
    tz = TIME_ZONE_INFORMATION()
    if not GetTimeZoneInformationForYear(year, dtz, tz):
        raise WinError()
    return tz


def current_timezone() -> str:
    tz = DYNAMIC_TIME_ZONE_INFORMATION()
    if GetDynamicTimeZoneInformation(tz) == TIME_ZONE_ID_INVALID:
        raise WinError()
    return tz.TimeZoneKeyName


def available_timezones() -> set[str]:
    return {tz.TimeZoneKeyName for tz in enum_dynamic_time_zone()}


def find_timezone(key: str) -> DYNAMIC_TIME_ZONE_INFORMATION:
    for tz in enum_dynamic_time_zone():
        if tz.TimeZoneKeyName == key:
            return tz
    raise KeyError(key)


def enum_dynamic_time_zone() -> Iterable[DYNAMIC_TIME_ZONE_INFORMATION]:
    i = 0
    tz = DYNAMIC_TIME_ZONE_INFORMATION()
    while True:
        r = EnumDynamicTimeZoneInformation(i, tz)
        if r == ERROR_SUCCESS:
            yield tz
        elif r == ERROR_NO_MORE_ITEMS:
            break
        else:
            raise WinError()
        i += 1


def datetime_to_systemtime(dt: datetime) -> SYSTEMTIME:
    return SYSTEMTIME(
        dt.year, dt.month, systemtime_weekday(dt), dt.day, dt.hour, dt.minute, dt.second, dt.microsecond // 1000
    )


def systemtime_to_datetime(st: SYSTEMTIME) -> datetime:
    return datetime(st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond, st.wMilliseconds * 1000)


# Monday=1, ..., Sunday=7 to Sunday=0, ..., Saturday=6
def systemtime_weekday(dt: datetime) -> int:
    return dt.isoweekday() % 7


class WinZoneInfo(tzinfo):
    def __init__(self, key: str) -> None:
        super().__init__()
        self._dtz = find_timezone(key)

    def utcoffset(self, local: datetime) -> timedelta:
        return local.replace(tzinfo=None) - tz_specific_local_time_to_system_time_ex(self._dtz, local)

    def dst(self, local: datetime) -> timedelta:
        tz = get_time_zone_information_for_year(local.year, self._dtz)
        return self.utcoffset(local) - timedelta(minutes=-tz.Bias)

    def tzname(self, local: datetime) -> str:
        return self._dtz.TimeZoneKeyName

    def fromutc(self, utc: datetime) -> datetime:
        return system_time_to_tz_specific_local_time_ex(self._dtz, utc).replace(tzinfo=self)

    def __str__(self) -> str:
        return f"WinZoneInfo(key='{self._dtz.TimeZoneKeyName}')"

    def __repr__(self) -> str:
        return str(self)
