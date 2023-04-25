from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization.DateTimeFormatting
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DateTimeFormatter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Globalization.DateTimeFormatting.DateTimeFormatter'
    @winrt_factorymethod
    def CreateDateTimeFormatter(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterLanguages(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String, languages: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterContext(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String, languages: Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDate(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: Windows.Globalization.DateTimeFormatting.DayOfWeekFormat) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterTime(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, hourFormat: Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: Windows.Globalization.DateTimeFormatting.SecondFormat) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDateTimeLanguages(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: Windows.Globalization.DateTimeFormatting.SecondFormat, languages: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDateTimeContext(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: Windows.Globalization.DateTimeFormatting.SecondFormat, languages: Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_mixinmethod
    def get_Languages(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_GeographicRegion(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Calendar(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Clock(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Patterns(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Template(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def Format(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter, value: Windows.Foundation.DateTime) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IncludeYear(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.YearFormat: ...
    @winrt_mixinmethod
    def get_IncludeMonth(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.MonthFormat: ...
    @winrt_mixinmethod
    def get_IncludeDayOfWeek(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.DayOfWeekFormat: ...
    @winrt_mixinmethod
    def get_IncludeDay(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.DayFormat: ...
    @winrt_mixinmethod
    def get_IncludeHour(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.HourFormat: ...
    @winrt_mixinmethod
    def get_IncludeMinute(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.MinuteFormat: ...
    @winrt_mixinmethod
    def get_IncludeSecond(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> Windows.Globalization.DateTimeFormatting.SecondFormat: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResolvedGeographicRegion(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUsingTimeZone(self: Windows.Globalization.DateTimeFormatting.IDateTimeFormatter2, datetime: Windows.Foundation.DateTime, timeZoneId: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def get_LongDate(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_LongTime(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_ShortDate(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_ShortTime(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    Calendar = property(get_Calendar, None)
    Clock = property(get_Clock, None)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    Patterns = property(get_Patterns, None)
    Template = property(get_Template, None)
    IncludeYear = property(get_IncludeYear, None)
    IncludeMonth = property(get_IncludeMonth, None)
    IncludeDayOfWeek = property(get_IncludeDayOfWeek, None)
    IncludeDay = property(get_IncludeDay, None)
    IncludeHour = property(get_IncludeHour, None)
    IncludeMinute = property(get_IncludeMinute, None)
    IncludeSecond = property(get_IncludeSecond, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    LongDate = property(get_LongDate, None)
    LongTime = property(get_LongTime, None)
    ShortDate = property(get_ShortDate, None)
    ShortTime = property(get_ShortTime, None)
DayFormat = Int32
DayFormat_None: DayFormat = 0
DayFormat_Default: DayFormat = 1
DayOfWeekFormat = Int32
DayOfWeekFormat_None: DayOfWeekFormat = 0
DayOfWeekFormat_Default: DayOfWeekFormat = 1
DayOfWeekFormat_Abbreviated: DayOfWeekFormat = 2
DayOfWeekFormat_Full: DayOfWeekFormat = 3
HourFormat = Int32
HourFormat_None: HourFormat = 0
HourFormat_Default: HourFormat = 1
class IDateTimeFormatter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('95eeca10-73e0-4e4b-a1-83-3d-6a-d0-ba-35-ec')
    @winrt_commethod(6)
    def get_Languages(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_GeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Calendar(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Clock(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_NumeralSystem(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_NumeralSystem(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Patterns(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Template(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def Format(self, value: Windows.Foundation.DateTime) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_IncludeYear(self) -> Windows.Globalization.DateTimeFormatting.YearFormat: ...
    @winrt_commethod(16)
    def get_IncludeMonth(self) -> Windows.Globalization.DateTimeFormatting.MonthFormat: ...
    @winrt_commethod(17)
    def get_IncludeDayOfWeek(self) -> Windows.Globalization.DateTimeFormatting.DayOfWeekFormat: ...
    @winrt_commethod(18)
    def get_IncludeDay(self) -> Windows.Globalization.DateTimeFormatting.DayFormat: ...
    @winrt_commethod(19)
    def get_IncludeHour(self) -> Windows.Globalization.DateTimeFormatting.HourFormat: ...
    @winrt_commethod(20)
    def get_IncludeMinute(self) -> Windows.Globalization.DateTimeFormatting.MinuteFormat: ...
    @winrt_commethod(21)
    def get_IncludeSecond(self) -> Windows.Globalization.DateTimeFormatting.SecondFormat: ...
    @winrt_commethod(22)
    def get_ResolvedLanguage(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_ResolvedGeographicRegion(self) -> WinRT_String: ...
    Languages = property(get_Languages, None)
    GeographicRegion = property(get_GeographicRegion, None)
    Calendar = property(get_Calendar, None)
    Clock = property(get_Clock, None)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    Patterns = property(get_Patterns, None)
    Template = property(get_Template, None)
    IncludeYear = property(get_IncludeYear, None)
    IncludeMonth = property(get_IncludeMonth, None)
    IncludeDayOfWeek = property(get_IncludeDayOfWeek, None)
    IncludeDay = property(get_IncludeDay, None)
    IncludeHour = property(get_IncludeHour, None)
    IncludeMinute = property(get_IncludeMinute, None)
    IncludeSecond = property(get_IncludeSecond, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
class IDateTimeFormatter2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('27c91a86-bdaa-4fd0-9e-36-67-1d-5a-a5-ee-03')
    @winrt_commethod(6)
    def FormatUsingTimeZone(self, datetime: Windows.Foundation.DateTime, timeZoneId: WinRT_String) -> WinRT_String: ...
class IDateTimeFormatterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ec8d8a53-1a2e-412d-88-15-3b-74-5f-b1-a2-a0')
    @winrt_commethod(6)
    def CreateDateTimeFormatter(self, formatTemplate: WinRT_String) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(7)
    def CreateDateTimeFormatterLanguages(self, formatTemplate: WinRT_String, languages: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(8)
    def CreateDateTimeFormatterContext(self, formatTemplate: WinRT_String, languages: Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(9)
    def CreateDateTimeFormatterDate(self, yearFormat: Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: Windows.Globalization.DateTimeFormatting.DayOfWeekFormat) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(10)
    def CreateDateTimeFormatterTime(self, hourFormat: Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: Windows.Globalization.DateTimeFormatting.SecondFormat) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(11)
    def CreateDateTimeFormatterDateTimeLanguages(self, yearFormat: Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: Windows.Globalization.DateTimeFormatting.SecondFormat, languages: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(12)
    def CreateDateTimeFormatterDateTimeContext(self, yearFormat: Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: Windows.Globalization.DateTimeFormatting.SecondFormat, languages: Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
class IDateTimeFormatterStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bfcde7c0-df4c-4a2e-90-12-f4-7d-af-3f-12-12')
    @winrt_commethod(6)
    def get_LongDate(self) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(7)
    def get_LongTime(self) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(8)
    def get_ShortDate(self) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(9)
    def get_ShortTime(self) -> Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    LongDate = property(get_LongDate, None)
    LongTime = property(get_LongTime, None)
    ShortDate = property(get_ShortDate, None)
    ShortTime = property(get_ShortTime, None)
MinuteFormat = Int32
MinuteFormat_None: MinuteFormat = 0
MinuteFormat_Default: MinuteFormat = 1
MonthFormat = Int32
MonthFormat_None: MonthFormat = 0
MonthFormat_Default: MonthFormat = 1
MonthFormat_Abbreviated: MonthFormat = 2
MonthFormat_Full: MonthFormat = 3
MonthFormat_Numeric: MonthFormat = 4
SecondFormat = Int32
SecondFormat_None: SecondFormat = 0
SecondFormat_Default: SecondFormat = 1
YearFormat = Int32
YearFormat_None: YearFormat = 0
YearFormat_Default: YearFormat = 1
YearFormat_Abbreviated: YearFormat = 2
YearFormat_Full: YearFormat = 3
make_head(_module, 'DateTimeFormatter')
make_head(_module, 'IDateTimeFormatter')
make_head(_module, 'IDateTimeFormatter2')
make_head(_module, 'IDateTimeFormatterFactory')
make_head(_module, 'IDateTimeFormatterStatics')
