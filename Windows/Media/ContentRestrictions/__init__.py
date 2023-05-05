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
import Windows.Foundation.Collections
import Windows.Media.ContentRestrictions
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ContentAccessRestrictionLevel = Int32
ContentAccessRestrictionLevel_Allow: ContentAccessRestrictionLevel = 0
ContentAccessRestrictionLevel_Warn: ContentAccessRestrictionLevel = 1
ContentAccessRestrictionLevel_Block: ContentAccessRestrictionLevel = 2
ContentAccessRestrictionLevel_Hide: ContentAccessRestrictionLevel = 3
class ContentRestrictionsBrowsePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy
    _classid_ = 'Windows.Media.ContentRestrictions.ContentRestrictionsBrowsePolicy'
    @winrt_mixinmethod
    def get_GeographicRegion(self: Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MaxBrowsableAgeRating(self: Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_PreferredAgeRating(self: Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy) -> Windows.Foundation.IReference[UInt32]: ...
    GeographicRegion = property(get_GeographicRegion, None)
    MaxBrowsableAgeRating = property(get_MaxBrowsableAgeRating, None)
    PreferredAgeRating = property(get_PreferredAgeRating, None)
class IContentRestrictionsBrowsePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy'
    _iid_ = Guid('{8c0133a4-442e-461a-8757-fad2f5bd37e4}')
    @winrt_commethod(6)
    def get_GeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxBrowsableAgeRating(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_PreferredAgeRating(self) -> Windows.Foundation.IReference[UInt32]: ...
    GeographicRegion = property(get_GeographicRegion, None)
    MaxBrowsableAgeRating = property(get_MaxBrowsableAgeRating, None)
    PreferredAgeRating = property(get_PreferredAgeRating, None)
class IRatedContentDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentDescription'
    _iid_ = Guid('{694866df-66b2-4dc3-96b1-f090eedee255}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Image(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def put_Image(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(12)
    def get_Category(self) -> Windows.Media.ContentRestrictions.RatedContentCategory: ...
    @winrt_commethod(13)
    def put_Category(self, value: Windows.Media.ContentRestrictions.RatedContentCategory) -> Void: ...
    @winrt_commethod(14)
    def get_Ratings(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(15)
    def put_Ratings(self, value: Windows.Foundation.Collections.IVector[WinRT_String]) -> Void: ...
    Id = property(get_Id, put_Id)
    Title = property(get_Title, put_Title)
    Image = property(get_Image, put_Image)
    Category = property(get_Category, put_Category)
    Ratings = property(get_Ratings, put_Ratings)
class IRatedContentDescriptionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentDescriptionFactory'
    _iid_ = Guid('{2e38df62-9b90-4fa6-89c1-4b8d2ffb3573}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, title: WinRT_String, category: Windows.Media.ContentRestrictions.RatedContentCategory) -> Windows.Media.ContentRestrictions.RatedContentDescription: ...
class IRatedContentRestrictions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentRestrictions'
    _iid_ = Guid('{3f7f23cb-ba07-4401-a49d-8b9222205723}')
    @winrt_commethod(6)
    def GetBrowsePolicyAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.ContentRestrictions.ContentRestrictionsBrowsePolicy]: ...
    @winrt_commethod(7)
    def GetRestrictionLevelAsync(self, RatedContentDescription: Windows.Media.ContentRestrictions.RatedContentDescription) -> Windows.Foundation.IAsyncOperation[Windows.Media.ContentRestrictions.ContentAccessRestrictionLevel]: ...
    @winrt_commethod(8)
    def RequestContentAccessAsync(self, RatedContentDescription: Windows.Media.ContentRestrictions.RatedContentDescription) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def add_RestrictionsChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_RestrictionsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRatedContentRestrictionsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentRestrictionsFactory'
    _iid_ = Guid('{fb4b2996-c3bd-4910-9619-97cfd0694d56}')
    @winrt_commethod(6)
    def CreateWithMaxAgeRating(self, maxAgeRating: UInt32) -> Windows.Media.ContentRestrictions.RatedContentRestrictions: ...
RatedContentCategory = Int32
RatedContentCategory_General: RatedContentCategory = 0
RatedContentCategory_Application: RatedContentCategory = 1
RatedContentCategory_Game: RatedContentCategory = 2
RatedContentCategory_Movie: RatedContentCategory = 3
RatedContentCategory_Television: RatedContentCategory = 4
RatedContentCategory_Music: RatedContentCategory = 5
class RatedContentDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.ContentRestrictions.IRatedContentDescription
    _classid_ = 'Windows.Media.ContentRestrictions.RatedContentDescription'
    @winrt_factorymethod
    def Create(cls: Windows.Media.ContentRestrictions.IRatedContentDescriptionFactory, id: WinRT_String, title: WinRT_String, category: Windows.Media.ContentRestrictions.RatedContentCategory) -> Windows.Media.ContentRestrictions.RatedContentDescription: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.ContentRestrictions.IRatedContentDescription) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Media.ContentRestrictions.IRatedContentDescription, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Media.ContentRestrictions.IRatedContentDescription) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Media.ContentRestrictions.IRatedContentDescription, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: Windows.Media.ContentRestrictions.IRatedContentDescription) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: Windows.Media.ContentRestrictions.IRatedContentDescription, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.Media.ContentRestrictions.IRatedContentDescription) -> Windows.Media.ContentRestrictions.RatedContentCategory: ...
    @winrt_mixinmethod
    def put_Category(self: Windows.Media.ContentRestrictions.IRatedContentDescription, value: Windows.Media.ContentRestrictions.RatedContentCategory) -> Void: ...
    @winrt_mixinmethod
    def get_Ratings(self: Windows.Media.ContentRestrictions.IRatedContentDescription) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def put_Ratings(self: Windows.Media.ContentRestrictions.IRatedContentDescription, value: Windows.Foundation.Collections.IVector[WinRT_String]) -> Void: ...
    Id = property(get_Id, put_Id)
    Title = property(get_Title, put_Title)
    Image = property(get_Image, put_Image)
    Category = property(get_Category, put_Category)
    Ratings = property(get_Ratings, put_Ratings)
class RatedContentRestrictions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.ContentRestrictions.IRatedContentRestrictions
    _classid_ = 'Windows.Media.ContentRestrictions.RatedContentRestrictions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.ContentRestrictions.RatedContentRestrictions: ...
    @winrt_factorymethod
    def CreateWithMaxAgeRating(cls: Windows.Media.ContentRestrictions.IRatedContentRestrictionsFactory, maxAgeRating: UInt32) -> Windows.Media.ContentRestrictions.RatedContentRestrictions: ...
    @winrt_mixinmethod
    def GetBrowsePolicyAsync(self: Windows.Media.ContentRestrictions.IRatedContentRestrictions) -> Windows.Foundation.IAsyncOperation[Windows.Media.ContentRestrictions.ContentRestrictionsBrowsePolicy]: ...
    @winrt_mixinmethod
    def GetRestrictionLevelAsync(self: Windows.Media.ContentRestrictions.IRatedContentRestrictions, RatedContentDescription: Windows.Media.ContentRestrictions.RatedContentDescription) -> Windows.Foundation.IAsyncOperation[Windows.Media.ContentRestrictions.ContentAccessRestrictionLevel]: ...
    @winrt_mixinmethod
    def RequestContentAccessAsync(self: Windows.Media.ContentRestrictions.IRatedContentRestrictions, RatedContentDescription: Windows.Media.ContentRestrictions.RatedContentDescription) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_RestrictionsChanged(self: Windows.Media.ContentRestrictions.IRatedContentRestrictions, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RestrictionsChanged(self: Windows.Media.ContentRestrictions.IRatedContentRestrictions, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
make_head(_module, 'ContentRestrictionsBrowsePolicy')
make_head(_module, 'IContentRestrictionsBrowsePolicy')
make_head(_module, 'IRatedContentDescription')
make_head(_module, 'IRatedContentDescriptionFactory')
make_head(_module, 'IRatedContentRestrictions')
make_head(_module, 'IRatedContentRestrictionsFactory')
make_head(_module, 'RatedContentDescription')
make_head(_module, 'RatedContentRestrictions')
