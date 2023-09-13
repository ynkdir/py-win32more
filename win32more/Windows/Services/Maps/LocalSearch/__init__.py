from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.Services.Maps
import win32more.Windows.Services.Maps.LocalSearch
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILocalCategoriesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics'
    _iid_ = Guid('{f49399f5-8261-4321-9974-ef92d49a8dca}')
    @winrt_commethod(6)
    def get_BankAndCreditUnions(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EatDrink(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Hospitals(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_HotelsAndMotels(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_All(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Parking(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_SeeDo(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Shop(self) -> WinRT_String: ...
    BankAndCreditUnions = property(get_BankAndCreditUnions, None)
    EatDrink = property(get_EatDrink, None)
    Hospitals = property(get_Hospitals, None)
    HotelsAndMotels = property(get_HotelsAndMotels, None)
    All = property(get_All, None)
    Parking = property(get_Parking, None)
    SeeDo = property(get_SeeDo, None)
    Shop = property(get_Shop, None)
class ILocalLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocation'
    _iid_ = Guid('{bb0fe9ab-4502-4f2c-94a9-0d60de0e2163}')
    @winrt_commethod(6)
    def get_Address(self) -> win32more.Windows.Services.Maps.MapAddress: ...
    @winrt_commethod(7)
    def get_Identifier(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Point(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(11)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_DataAttribution(self) -> WinRT_String: ...
    Address = property(get_Address, None)
    Identifier = property(get_Identifier, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Point = property(get_Point, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DataAttribution = property(get_DataAttribution, None)
class ILocalLocation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocation2'
    _iid_ = Guid('{6e9e307c-ecb5-4ffc-bb8c-ba50ba8c2dc6}')
    @winrt_commethod(6)
    def get_Category(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RatingInfo(self) -> win32more.Windows.Services.Maps.LocalSearch.LocalLocationRatingInfo: ...
    @winrt_commethod(8)
    def get_HoursOfOperation(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocationHoursOfOperationItem]: ...
    Category = property(get_Category, None)
    RatingInfo = property(get_RatingInfo, None)
    HoursOfOperation = property(get_HoursOfOperation, None)
class ILocalLocationFinderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult'
    _iid_ = Guid('{d09b6cc6-f338-4191-9fd8-5440b9a68f52}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Services.Maps.LocalSearch.LocalLocationFinderStatus: ...
    LocalLocations = property(get_LocalLocations, None)
    Status = property(get_Status, None)
class ILocalLocationFinderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationFinderStatics'
    _iid_ = Guid('{d2ef7344-a0de-48ca-81a8-07c7dcfd37ab}')
    @winrt_commethod(6)
    def FindLocalLocationsAsync(self, searchTerm: WinRT_String, searchArea: win32more.Windows.Devices.Geolocation.Geocircle, localCategory: WinRT_String, maxResults: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.LocalSearch.LocalLocationFinderResult]: ...
class ILocalLocationHoursOfOperationItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem'
    _iid_ = Guid('{23548c72-a1c7-43f1-a4f0-1091c39ec640}')
    @winrt_commethod(6)
    def get_Day(self) -> win32more.Windows.Globalization.DayOfWeek: ...
    @winrt_commethod(7)
    def get_Start(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Span(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Day = property(get_Day, None)
    Start = property(get_Start, None)
    Span = property(get_Span, None)
class ILocalLocationRatingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo'
    _iid_ = Guid('{cb1dab56-3354-4311-8bc0-a2d4d5eb806e}')
    @winrt_commethod(6)
    def get_AggregateRating(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def get_RatingCount(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ProviderIdentifier(self) -> WinRT_String: ...
    AggregateRating = property(get_AggregateRating, None)
    RatingCount = property(get_RatingCount, None)
    ProviderIdentifier = property(get_ProviderIdentifier, None)
class IPlaceInfoHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.IPlaceInfoHelperStatics'
    _iid_ = Guid('{dd1ca9a7-a9c6-491b-bc09-e80fcea48ee6}')
    @winrt_commethod(6)
    def CreateFromLocalLocation(self, location: win32more.Windows.Services.Maps.LocalSearch.LocalLocation) -> win32more.Windows.Services.Maps.PlaceInfo: ...
class _LocalCategories_Meta_(ComPtr.__class__):
    pass
class LocalCategories(ComPtr, metaclass=_LocalCategories_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalCategories'
    @winrt_classmethod
    def get_BankAndCreditUnions(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EatDrink(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Hospitals(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HotelsAndMotels(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_All(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Parking(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SeeDo(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Shop(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalCategoriesStatics) -> WinRT_String: ...
    _LocalCategories_Meta_.BankAndCreditUnions = property(get_BankAndCreditUnions.__wrapped__, None)
    _LocalCategories_Meta_.EatDrink = property(get_EatDrink.__wrapped__, None)
    _LocalCategories_Meta_.Hospitals = property(get_Hospitals.__wrapped__, None)
    _LocalCategories_Meta_.HotelsAndMotels = property(get_HotelsAndMotels.__wrapped__, None)
    _LocalCategories_Meta_.All = property(get_All.__wrapped__, None)
    _LocalCategories_Meta_.Parking = property(get_Parking.__wrapped__, None)
    _LocalCategories_Meta_.SeeDo = property(get_SeeDo.__wrapped__, None)
    _LocalCategories_Meta_.Shop = property(get_Shop.__wrapped__, None)
class LocalLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocation'
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> win32more.Windows.Services.Maps.MapAddress: ...
    @winrt_mixinmethod
    def get_Identifier(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DataAttribution(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RatingInfo(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation2) -> win32more.Windows.Services.Maps.LocalSearch.LocalLocationRatingInfo: ...
    @winrt_mixinmethod
    def get_HoursOfOperation(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocationHoursOfOperationItem]: ...
    Address = property(get_Address, None)
    Identifier = property(get_Identifier, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Point = property(get_Point, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DataAttribution = property(get_DataAttribution, None)
    Category = property(get_Category, None)
    RatingInfo = property(get_RatingInfo, None)
    HoursOfOperation = property(get_HoursOfOperation, None)
class LocalLocationFinder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationFinder'
    @winrt_classmethod
    def FindLocalLocationsAsync(cls: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationFinderStatics, searchTerm: WinRT_String, searchArea: win32more.Windows.Devices.Geolocation.Geocircle, localCategory: WinRT_String, maxResults: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.LocalSearch.LocalLocationFinderResult]: ...
class LocalLocationFinderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationFinderResult'
    @winrt_mixinmethod
    def get_LocalLocations(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationFinderResult) -> win32more.Windows.Services.Maps.LocalSearch.LocalLocationFinderStatus: ...
    LocalLocations = property(get_LocalLocations, None)
    Status = property(get_Status, None)
LocalLocationFinderStatus = Int32
LocalLocationFinderStatus_Success: LocalLocationFinderStatus = 0
LocalLocationFinderStatus_UnknownError: LocalLocationFinderStatus = 1
LocalLocationFinderStatus_InvalidCredentials: LocalLocationFinderStatus = 2
LocalLocationFinderStatus_InvalidCategory: LocalLocationFinderStatus = 3
LocalLocationFinderStatus_InvalidSearchTerm: LocalLocationFinderStatus = 4
LocalLocationFinderStatus_InvalidSearchArea: LocalLocationFinderStatus = 5
LocalLocationFinderStatus_NetworkFailure: LocalLocationFinderStatus = 6
LocalLocationFinderStatus_NotSupported: LocalLocationFinderStatus = 7
class LocalLocationHoursOfOperationItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationHoursOfOperationItem'
    @winrt_mixinmethod
    def get_Day(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> win32more.Windows.Globalization.DayOfWeek: ...
    @winrt_mixinmethod
    def get_Start(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Span(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationHoursOfOperationItem) -> win32more.Windows.Foundation.TimeSpan: ...
    Day = property(get_Day, None)
    Start = property(get_Start, None)
    Span = property(get_Span, None)
class LocalLocationRatingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo
    _classid_ = 'Windows.Services.Maps.LocalSearch.LocalLocationRatingInfo'
    @winrt_mixinmethod
    def get_AggregateRating(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_RatingCount(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderIdentifier(self: win32more.Windows.Services.Maps.LocalSearch.ILocalLocationRatingInfo) -> WinRT_String: ...
    AggregateRating = property(get_AggregateRating, None)
    RatingCount = property(get_RatingCount, None)
    ProviderIdentifier = property(get_ProviderIdentifier, None)
class PlaceInfoHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.LocalSearch.PlaceInfoHelper'
    @winrt_classmethod
    def CreateFromLocalLocation(cls: win32more.Windows.Services.Maps.LocalSearch.IPlaceInfoHelperStatics, location: win32more.Windows.Services.Maps.LocalSearch.LocalLocation) -> win32more.Windows.Services.Maps.PlaceInfo: ...
make_head(_module, 'ILocalCategoriesStatics')
make_head(_module, 'ILocalLocation')
make_head(_module, 'ILocalLocation2')
make_head(_module, 'ILocalLocationFinderResult')
make_head(_module, 'ILocalLocationFinderStatics')
make_head(_module, 'ILocalLocationHoursOfOperationItem')
make_head(_module, 'ILocalLocationRatingInfo')
make_head(_module, 'IPlaceInfoHelperStatics')
make_head(_module, 'LocalCategories')
make_head(_module, 'LocalLocation')
make_head(_module, 'LocalLocationFinder')
make_head(_module, 'LocalLocationFinderResult')
make_head(_module, 'LocalLocationHoursOfOperationItem')
make_head(_module, 'LocalLocationRatingInfo')
make_head(_module, 'PlaceInfoHelper')
