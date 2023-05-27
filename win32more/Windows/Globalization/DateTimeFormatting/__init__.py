from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization.DateTimeFormatting
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _DateTimeFormatter_Meta_(ComPtr.__class__):
    pass
class DateTimeFormatter(ComPtr, metaclass=_DateTimeFormatter_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter
    _classid_ = 'Windows.Globalization.DateTimeFormatting.DateTimeFormatter'
    @winrt_factorymethod
    def CreateDateTimeFormatter(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterLanguages(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterContext(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDate(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterTime(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDateTimeLanguages(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDateTimeContext(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_GeographicRegion(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Calendar(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Clock(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NumeralSystem(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NumeralSystem(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Patterns(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Template(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def Format(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter, value: win32more.Windows.Foundation.DateTime) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IncludeYear(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.YearFormat: ...
    @winrt_mixinmethod
    def get_IncludeMonth(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.MonthFormat: ...
    @winrt_mixinmethod
    def get_IncludeDayOfWeek(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat: ...
    @winrt_mixinmethod
    def get_IncludeDay(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.DayFormat: ...
    @winrt_mixinmethod
    def get_IncludeHour(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.HourFormat: ...
    @winrt_mixinmethod
    def get_IncludeMinute(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat: ...
    @winrt_mixinmethod
    def get_IncludeSecond(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> win32more.Windows.Globalization.DateTimeFormatting.SecondFormat: ...
    @winrt_mixinmethod
    def get_ResolvedLanguage(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResolvedGeographicRegion(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatUsingTimeZone(self: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter2, datetime: win32more.Windows.Foundation.DateTime, timeZoneId: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def get_LongDate(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_LongTime(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_ShortDate(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_ShortTime(cls: Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
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
    _DateTimeFormatter_Meta_.LongDate = property(get_LongDate.__wrapped__, None)
    _DateTimeFormatter_Meta_.LongTime = property(get_LongTime.__wrapped__, None)
    _DateTimeFormatter_Meta_.ShortDate = property(get_ShortDate.__wrapped__, None)
    _DateTimeFormatter_Meta_.ShortTime = property(get_ShortTime.__wrapped__, None)
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
class IDateTimeFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.DateTimeFormatting.IDateTimeFormatter'
    _iid_ = Guid('{95eeca10-73e0-4e4b-a183-3d6ad0ba35ec}')
    @winrt_commethod(6)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
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
    def get_Patterns(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Template(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def Format(self, value: win32more.Windows.Foundation.DateTime) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_IncludeYear(self) -> win32more.Windows.Globalization.DateTimeFormatting.YearFormat: ...
    @winrt_commethod(16)
    def get_IncludeMonth(self) -> win32more.Windows.Globalization.DateTimeFormatting.MonthFormat: ...
    @winrt_commethod(17)
    def get_IncludeDayOfWeek(self) -> win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat: ...
    @winrt_commethod(18)
    def get_IncludeDay(self) -> win32more.Windows.Globalization.DateTimeFormatting.DayFormat: ...
    @winrt_commethod(19)
    def get_IncludeHour(self) -> win32more.Windows.Globalization.DateTimeFormatting.HourFormat: ...
    @winrt_commethod(20)
    def get_IncludeMinute(self) -> win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat: ...
    @winrt_commethod(21)
    def get_IncludeSecond(self) -> win32more.Windows.Globalization.DateTimeFormatting.SecondFormat: ...
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
class IDateTimeFormatter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.DateTimeFormatting.IDateTimeFormatter2'
    _iid_ = Guid('{27c91a86-bdaa-4fd0-9e36-671d5aa5ee03}')
    @winrt_commethod(6)
    def FormatUsingTimeZone(self, datetime: win32more.Windows.Foundation.DateTime, timeZoneId: WinRT_String) -> WinRT_String: ...
class IDateTimeFormatterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory'
    _iid_ = Guid('{ec8d8a53-1a2e-412d-8815-3b745fb1a2a0}')
    @winrt_commethod(6)
    def CreateDateTimeFormatter(self, formatTemplate: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(7)
    def CreateDateTimeFormatterLanguages(self, formatTemplate: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(8)
    def CreateDateTimeFormatterContext(self, formatTemplate: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(9)
    def CreateDateTimeFormatterDate(self, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(10)
    def CreateDateTimeFormatterTime(self, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(11)
    def CreateDateTimeFormatterDateTimeLanguages(self, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(12)
    def CreateDateTimeFormatterDateTimeContext(self, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
class IDateTimeFormatterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics'
    _iid_ = Guid('{bfcde7c0-df4c-4a2e-9012-f47daf3f1212}')
    @winrt_commethod(6)
    def get_LongDate(self) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(7)
    def get_LongTime(self) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(8)
    def get_ShortDate(self) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_commethod(9)
    def get_ShortTime(self) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
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
