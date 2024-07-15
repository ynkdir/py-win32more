from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization.DateTimeFormatting
import win32more.Windows.Win32.System.WinRT
class _DateTimeFormatter_Meta_(ComPtr.__class__):
    pass
class DateTimeFormatter(ComPtr, metaclass=_DateTimeFormatter_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatter
    _classid_ = 'Windows.Globalization.DateTimeFormatting.DateTimeFormatter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatter(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatterLanguages(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatterTime(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatterDate(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatterContext(*args))
        elif len(args) == 8:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatterDateTimeLanguages(*args))
        elif len(args) == 11:
            super().__init__(move=win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter.CreateDateTimeFormatterDateTimeContext(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateDateTimeFormatter(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterLanguages(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterTime(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDate(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterContext(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, formatTemplate: WinRT_String, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDateTimeLanguages(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_factorymethod
    def CreateDateTimeFormatterDateTimeContext(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterFactory, yearFormat: win32more.Windows.Globalization.DateTimeFormatting.YearFormat, monthFormat: win32more.Windows.Globalization.DateTimeFormatting.MonthFormat, dayFormat: win32more.Windows.Globalization.DateTimeFormatting.DayFormat, dayOfWeekFormat: win32more.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat, hourFormat: win32more.Windows.Globalization.DateTimeFormatting.HourFormat, minuteFormat: win32more.Windows.Globalization.DateTimeFormatting.MinuteFormat, secondFormat: win32more.Windows.Globalization.DateTimeFormatting.SecondFormat, languages: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], geographicRegion: WinRT_String, calendar: WinRT_String, clock: WinRT_String) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
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
    def get_LongDate(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_LongTime(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_ShortDate(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    @winrt_classmethod
    def get_ShortTime(cls: win32more.Windows.Globalization.DateTimeFormatting.IDateTimeFormatterStatics) -> win32more.Windows.Globalization.DateTimeFormatting.DateTimeFormatter: ...
    Calendar = property(get_Calendar, None)
    Clock = property(get_Clock, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IncludeDay = property(get_IncludeDay, None)
    IncludeDayOfWeek = property(get_IncludeDayOfWeek, None)
    IncludeHour = property(get_IncludeHour, None)
    IncludeMinute = property(get_IncludeMinute, None)
    IncludeMonth = property(get_IncludeMonth, None)
    IncludeSecond = property(get_IncludeSecond, None)
    IncludeYear = property(get_IncludeYear, None)
    Languages = property(get_Languages, None)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    Patterns = property(get_Patterns, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    Template = property(get_Template, None)
    _DateTimeFormatter_Meta_.LongDate = property(get_LongDate, None)
    _DateTimeFormatter_Meta_.LongTime = property(get_LongTime, None)
    _DateTimeFormatter_Meta_.ShortDate = property(get_ShortDate, None)
    _DateTimeFormatter_Meta_.ShortTime = property(get_ShortTime, None)
class DayFormat(Enum, Int32):
    None_ = 0
    Default = 1
class DayOfWeekFormat(Enum, Int32):
    None_ = 0
    Default = 1
    Abbreviated = 2
    Full = 3
class HourFormat(Enum, Int32):
    None_ = 0
    Default = 1
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
    Calendar = property(get_Calendar, None)
    Clock = property(get_Clock, None)
    GeographicRegion = property(get_GeographicRegion, None)
    IncludeDay = property(get_IncludeDay, None)
    IncludeDayOfWeek = property(get_IncludeDayOfWeek, None)
    IncludeHour = property(get_IncludeHour, None)
    IncludeMinute = property(get_IncludeMinute, None)
    IncludeMonth = property(get_IncludeMonth, None)
    IncludeSecond = property(get_IncludeSecond, None)
    IncludeYear = property(get_IncludeYear, None)
    Languages = property(get_Languages, None)
    NumeralSystem = property(get_NumeralSystem, put_NumeralSystem)
    Patterns = property(get_Patterns, None)
    ResolvedGeographicRegion = property(get_ResolvedGeographicRegion, None)
    ResolvedLanguage = property(get_ResolvedLanguage, None)
    Template = property(get_Template, None)
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
class MinuteFormat(Enum, Int32):
    None_ = 0
    Default = 1
class MonthFormat(Enum, Int32):
    None_ = 0
    Default = 1
    Abbreviated = 2
    Full = 3
    Numeric = 4
class SecondFormat(Enum, Int32):
    None_ = 0
    Default = 1
class YearFormat(Enum, Int32):
    None_ = 0
    Default = 1
    Abbreviated = 2
    Full = 3


make_ready(__name__)
