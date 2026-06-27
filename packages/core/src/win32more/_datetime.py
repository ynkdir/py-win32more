from __future__ import annotations

from datetime import datetime, timedelta, timezone

from win32more.Windows.Foundation import DateTime, TimeSpan

from ._winzoneinfo import WinZoneInfo, current_timezone

# FILETIME: 100-nanosecond intervals since January 1, 1601 (UTC)
FILETIME_EPOCH = datetime(1601, 1, 1, tzinfo=timezone.utc)


def datetime_to_winrt(value: datetime) -> DateTime:
    # ensure aware datetime
    if value.tzinfo is None:
        value = value.replace(tzinfo=local_timezone(value))
    return DateTime((value - FILETIME_EPOCH) // timedelta(microseconds=1) * 10)


# nanoseconds are dropped
# FIXME: should return utc?
def datetime_from_winrt(value: DateTime) -> datetime:
    utc = FILETIME_EPOCH + timedelta(microseconds=value.UniversalTime // 10)
    return utc.astimezone(local_timezone(utc))


def local_timezone(dt: datetime) -> timezone:
    try:
        return dt.astimezone().tzinfo
    except OSError:
        # <3.15: astimezone() fails for pre-EPOCH(1970) datetime.  Falls back to custom implementation.
        return WinZoneInfo(current_timezone())


def timedelta_to_winrt(value: timedelta) -> TimeSpan:
    return TimeSpan(value // timedelta(microseconds=1) * 10)


def timedelta_from_winrt(value: TimeSpan) -> timedelta:
    return timedelta(microseconds=value.Duration // 10)
