from __future__ import annotations

from datetime import datetime, timedelta, timezone

from win32more.Windows.Foundation import DateTime, TimeSpan

# FILETIME: 100-nanosecond intervals since January 1, 1601 (UTC)
FILETIME_EPOCH = datetime(1601, 1, 1, tzinfo=timezone.utc)


def datetime_to_winrt(value: datetime) -> DateTime:
    # ensure aware datetime
    if value.tzinfo is None:
        value = value.replace(tzinfo=localtzinfo())
    return DateTime((value - FILETIME_EPOCH) // timedelta(microseconds=1) * 10)


# nanoseconds are dropped
def datetime_from_winrt(value: DateTime) -> datetime:
    utc = FILETIME_EPOCH + timedelta(microseconds=value.UniversalTime // 10)
    local = localtzinfo()
    return (utc + local.utcoffset(None)).replace(tzinfo=local)


# <3.15: astimezone() raises OSError for pre-EPOCH datetime
def localtzinfo():
    return datetime(2006, 1, 2).astimezone().tzinfo


def timedelta_to_winrt(value: timedelta) -> TimeSpan:
    return TimeSpan(value // timedelta(microseconds=1) * 10)


def timedelta_from_winrt(value: TimeSpan) -> timedelta:
    return timedelta(microseconds=value.Duration // 10)
