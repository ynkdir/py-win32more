from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Globalization.PhoneNumberFormatting
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPhoneNumberFormatter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1556b49e-bad4-4b4a-90-0d-44-07-ad-b7-c9-81')
    @winrt_commethod(6)
    def Format(self, number: Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> WinRT_String: ...
    @winrt_commethod(7)
    def FormatWithOutputFormat(self, number: Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo, numberFormat: Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat) -> WinRT_String: ...
    @winrt_commethod(8)
    def FormatPartialString(self, number: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def FormatString(self, number: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(10)
    def FormatStringWithLeftToRightMarkers(self, number: WinRT_String) -> WinRT_String: ...
class IPhoneNumberFormatterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5ca6f931-84d9-414b-ab-4e-a0-55-2c-87-86-02')
    @winrt_commethod(6)
    def TryCreate(self, regionCode: WinRT_String, phoneNumber: POINTER(Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter)) -> Void: ...
    @winrt_commethod(7)
    def GetCountryCodeForRegion(self, regionCode: WinRT_String) -> Int32: ...
    @winrt_commethod(8)
    def GetNationalDirectDialingPrefixForRegion(self, regionCode: WinRT_String, stripNonDigit: Boolean) -> WinRT_String: ...
    @winrt_commethod(9)
    def WrapWithLeftToRightMarkers(self, number: WinRT_String) -> WinRT_String: ...
class IPhoneNumberInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1c7ce4dd-c8b4-4ea3-9a-ef-b3-42-e2-c5-b4-17')
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
    def PredictNumberKind(self) -> Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind: ...
    @winrt_commethod(12)
    def GetGeographicRegionCode(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def CheckNumberMatch(self, otherNumber: Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult: ...
    CountryCode = property(get_CountryCode, None)
    PhoneNumber = property(get_PhoneNumber, None)
class IPhoneNumberInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8202b964-adaa-4cff-8f-cf-17-e7-51-6a-28-ff')
    @winrt_commethod(6)
    def Create(self, number: WinRT_String) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo: ...
class IPhoneNumberInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5b3f4f6a-86a9-40e9-86-49-6d-61-16-19-28-d4')
    @winrt_commethod(6)
    def TryParse(self, input: WinRT_String, phoneNumber: POINTER(Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    @winrt_commethod(7)
    def TryParseWithRegion(self, input: WinRT_String, regionCode: WinRT_String, phoneNumber: POINTER(Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
PhoneNumberFormat = Int32
PhoneNumberFormat_E164: PhoneNumberFormat = 0
PhoneNumberFormat_International: PhoneNumberFormat = 1
PhoneNumberFormat_National: PhoneNumberFormat = 2
PhoneNumberFormat_Rfc3966: PhoneNumberFormat = 3
class PhoneNumberFormatter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter'
    @winrt_activatemethod
    def New(cls) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter: ...
    @winrt_mixinmethod
    def Format(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatWithOutputFormat(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo, numberFormat: Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatPartialString(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatString(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatStringWithLeftToRightMarkers(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def TryCreate(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String, phoneNumber: POINTER(Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter)) -> Void: ...
    @winrt_classmethod
    def GetCountryCodeForRegion(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String) -> Int32: ...
    @winrt_classmethod
    def GetNationalDirectDialingPrefixForRegion(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String, stripNonDigit: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def WrapWithLeftToRightMarkers(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, number: WinRT_String) -> WinRT_String: ...
class PhoneNumberInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo'
    @winrt_factorymethod
    def Create(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoFactory, number: WinRT_String) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo: ...
    @winrt_mixinmethod
    def get_CountryCode(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLengthOfGeographicalAreaCode(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def GetNationalSignificantNumber(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLengthOfNationalDestinationCode(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def PredictNumberKind(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind: ...
    @winrt_mixinmethod
    def GetGeographicRegionCode(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def CheckNumberMatch(self: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo, otherNumber: Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics, input: WinRT_String, phoneNumber: POINTER(Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    @winrt_classmethod
    def TryParseWithRegion(cls: Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics, input: WinRT_String, regionCode: WinRT_String, phoneNumber: POINTER(Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    CountryCode = property(get_CountryCode, None)
    PhoneNumber = property(get_PhoneNumber, None)
PhoneNumberMatchResult = Int32
PhoneNumberMatchResult_NoMatch: PhoneNumberMatchResult = 0
PhoneNumberMatchResult_ShortNationalSignificantNumberMatch: PhoneNumberMatchResult = 1
PhoneNumberMatchResult_NationalSignificantNumberMatch: PhoneNumberMatchResult = 2
PhoneNumberMatchResult_ExactMatch: PhoneNumberMatchResult = 3
PhoneNumberParseResult = Int32
PhoneNumberParseResult_Valid: PhoneNumberParseResult = 0
PhoneNumberParseResult_NotANumber: PhoneNumberParseResult = 1
PhoneNumberParseResult_InvalidCountryCode: PhoneNumberParseResult = 2
PhoneNumberParseResult_TooShort: PhoneNumberParseResult = 3
PhoneNumberParseResult_TooLong: PhoneNumberParseResult = 4
PredictedPhoneNumberKind = Int32
PredictedPhoneNumberKind_FixedLine: PredictedPhoneNumberKind = 0
PredictedPhoneNumberKind_Mobile: PredictedPhoneNumberKind = 1
PredictedPhoneNumberKind_FixedLineOrMobile: PredictedPhoneNumberKind = 2
PredictedPhoneNumberKind_TollFree: PredictedPhoneNumberKind = 3
PredictedPhoneNumberKind_PremiumRate: PredictedPhoneNumberKind = 4
PredictedPhoneNumberKind_SharedCost: PredictedPhoneNumberKind = 5
PredictedPhoneNumberKind_Voip: PredictedPhoneNumberKind = 6
PredictedPhoneNumberKind_PersonalNumber: PredictedPhoneNumberKind = 7
PredictedPhoneNumberKind_Pager: PredictedPhoneNumberKind = 8
PredictedPhoneNumberKind_UniversalAccountNumber: PredictedPhoneNumberKind = 9
PredictedPhoneNumberKind_Voicemail: PredictedPhoneNumberKind = 10
PredictedPhoneNumberKind_Unknown: PredictedPhoneNumberKind = 11
make_head(_module, 'IPhoneNumberFormatter')
make_head(_module, 'IPhoneNumberFormatterStatics')
make_head(_module, 'IPhoneNumberInfo')
make_head(_module, 'IPhoneNumberInfoFactory')
make_head(_module, 'IPhoneNumberInfoStatics')
make_head(_module, 'PhoneNumberFormatter')
make_head(_module, 'PhoneNumberInfo')
