from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Globalization.PhoneNumberFormatting
import win32more.Windows.Win32.System.WinRT
class IPhoneNumberFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter'
    _iid_ = Guid('{1556b49e-bad4-4b4a-900d-4407adb7c981}')
    @winrt_commethod(6)
    def Format(self, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> WinRT_String: ...
    @winrt_commethod(7)
    def FormatWithOutputFormat(self, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo, numberFormat: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat) -> WinRT_String: ...
    @winrt_commethod(8)
    def FormatPartialString(self, number: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def FormatString(self, number: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(10)
    def FormatStringWithLeftToRightMarkers(self, number: WinRT_String) -> WinRT_String: ...
class IPhoneNumberFormatterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics'
    _iid_ = Guid('{5ca6f931-84d9-414b-ab4e-a0552c878602}')
    @winrt_commethod(6)
    def TryCreate(self, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter)) -> Void: ...
    @winrt_commethod(7)
    def GetCountryCodeForRegion(self, regionCode: WinRT_String) -> Int32: ...
    @winrt_commethod(8)
    def GetNationalDirectDialingPrefixForRegion(self, regionCode: WinRT_String, stripNonDigit: Boolean) -> WinRT_String: ...
    @winrt_commethod(9)
    def WrapWithLeftToRightMarkers(self, number: WinRT_String) -> WinRT_String: ...
class IPhoneNumberInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo'
    _iid_ = Guid('{1c7ce4dd-c8b4-4ea3-9aef-b342e2c5b417}')
    @winrt_commethod(6)
    def get_CountryCode(self) -> Int32: ...
    @winrt_commethod(7)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetLengthOfGeographicalAreaCode(self) -> Int32: ...
    @winrt_commethod(9)
    def GetNationalSignificantNumber(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetLengthOfNationalDestinationCode(self) -> Int32: ...
    @winrt_commethod(11)
    def PredictNumberKind(self) -> win32more.Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind: ...
    @winrt_commethod(12)
    def GetGeographicRegionCode(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def CheckNumberMatch(self, otherNumber: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult: ...
    CountryCode = property(get_CountryCode, None)
    PhoneNumber = property(get_PhoneNumber, None)
class IPhoneNumberInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoFactory'
    _iid_ = Guid('{8202b964-adaa-4cff-8fcf-17e7516a28ff}')
    @winrt_commethod(6)
    def Create(self, number: WinRT_String) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo: ...
class IPhoneNumberInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics'
    _iid_ = Guid('{5b3f4f6a-86a9-40e9-8649-6d61161928d4}')
    @winrt_commethod(6)
    def TryParse(self, input: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    @winrt_commethod(7)
    def TryParseWithRegion(self, input: WinRT_String, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
class PhoneNumberFormat(Enum, Int32):
    E164 = 0
    International = 1
    National = 2
    Rfc3966 = 3
class PhoneNumberFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter: ...
    @winrt_mixinmethod
    def Format(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatWithOutputFormat(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo, numberFormat: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatPartialString(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatString(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatStringWithLeftToRightMarkers(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def TryCreate(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter)) -> Void: ...
    @winrt_classmethod
    def GetCountryCodeForRegion(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String) -> Int32: ...
    @winrt_classmethod
    def GetNationalDirectDialingPrefixForRegion(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String, stripNonDigit: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def WrapWithLeftToRightMarkers(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, number: WinRT_String) -> WinRT_String: ...
class PhoneNumberInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoFactory, number: WinRT_String) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo: ...
    @winrt_mixinmethod
    def get_CountryCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLengthOfGeographicalAreaCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def GetNationalSignificantNumber(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLengthOfNationalDestinationCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def PredictNumberKind(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> win32more.Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind: ...
    @winrt_mixinmethod
    def GetGeographicRegionCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def CheckNumberMatch(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo, otherNumber: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics, input: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    @winrt_classmethod
    def TryParseWithRegion(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics, input: WinRT_String, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    CountryCode = property(get_CountryCode, None)
    PhoneNumber = property(get_PhoneNumber, None)
class PhoneNumberMatchResult(Enum, Int32):
    NoMatch = 0
    ShortNationalSignificantNumberMatch = 1
    NationalSignificantNumberMatch = 2
    ExactMatch = 3
class PhoneNumberParseResult(Enum, Int32):
    Valid = 0
    NotANumber = 1
    InvalidCountryCode = 2
    TooShort = 3
    TooLong = 4
class PredictedPhoneNumberKind(Enum, Int32):
    FixedLine = 0
    Mobile = 1
    FixedLineOrMobile = 2
    TollFree = 3
    PremiumRate = 4
    SharedCost = 5
    Voip = 6
    PersonalNumber = 7
    Pager = 8
    UniversalAccountNumber = 9
    Voicemail = 10
    Unknown = 11


make_ready(__name__)
