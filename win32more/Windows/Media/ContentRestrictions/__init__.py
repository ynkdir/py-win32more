from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.ContentRestrictions
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ContentAccessRestrictionLevel(Enum, Int32):
    Allow = 0
    Warn = 1
    Block = 2
    Hide = 3
class ContentRestrictionsBrowsePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy
    _classid_ = 'Windows.Media.ContentRestrictions.ContentRestrictionsBrowsePolicy'
    @winrt_mixinmethod
    def get_GeographicRegion(self: win32more.Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MaxBrowsableAgeRating(self: win32more.Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_PreferredAgeRating(self: win32more.Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    GeographicRegion = property(get_GeographicRegion, None)
    MaxBrowsableAgeRating = property(get_MaxBrowsableAgeRating, None)
    PreferredAgeRating = property(get_PreferredAgeRating, None)
class IContentRestrictionsBrowsePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IContentRestrictionsBrowsePolicy'
    _iid_ = Guid('{8c0133a4-442e-461a-8757-fad2f5bd37e4}')
    @winrt_commethod(6)
    def get_GeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxBrowsableAgeRating(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_PreferredAgeRating(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    GeographicRegion = property(get_GeographicRegion, None)
    MaxBrowsableAgeRating = property(get_MaxBrowsableAgeRating, None)
    PreferredAgeRating = property(get_PreferredAgeRating, None)
class IRatedContentDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Image(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def put_Image(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(12)
    def get_Category(self) -> win32more.Windows.Media.ContentRestrictions.RatedContentCategory: ...
    @winrt_commethod(13)
    def put_Category(self, value: win32more.Windows.Media.ContentRestrictions.RatedContentCategory) -> Void: ...
    @winrt_commethod(14)
    def get_Ratings(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(15)
    def put_Ratings(self, value: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> Void: ...
    Category = property(get_Category, put_Category)
    Id = property(get_Id, put_Id)
    Image = property(get_Image, put_Image)
    Ratings = property(get_Ratings, put_Ratings)
    Title = property(get_Title, put_Title)
class IRatedContentDescriptionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentDescriptionFactory'
    _iid_ = Guid('{2e38df62-9b90-4fa6-89c1-4b8d2ffb3573}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, title: WinRT_String, category: win32more.Windows.Media.ContentRestrictions.RatedContentCategory) -> win32more.Windows.Media.ContentRestrictions.RatedContentDescription: ...
class IRatedContentRestrictions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentRestrictions'
    _iid_ = Guid('{3f7f23cb-ba07-4401-a49d-8b9222205723}')
    @winrt_commethod(6)
    def GetBrowsePolicyAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.ContentRestrictions.ContentRestrictionsBrowsePolicy]: ...
    @winrt_commethod(7)
    def GetRestrictionLevelAsync(self, RatedContentDescription: win32more.Windows.Media.ContentRestrictions.RatedContentDescription) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.ContentRestrictions.ContentAccessRestrictionLevel]: ...
    @winrt_commethod(8)
    def RequestContentAccessAsync(self, RatedContentDescription: win32more.Windows.Media.ContentRestrictions.RatedContentDescription) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def add_RestrictionsChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_RestrictionsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    RestrictionsChanged = event()
class IRatedContentRestrictionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.ContentRestrictions.IRatedContentRestrictionsFactory'
    _iid_ = Guid('{fb4b2996-c3bd-4910-9619-97cfd0694d56}')
    @winrt_commethod(6)
    def CreateWithMaxAgeRating(self, maxAgeRating: UInt32) -> win32more.Windows.Media.ContentRestrictions.RatedContentRestrictions: ...
class RatedContentCategory(Enum, Int32):
    General = 0
    Application = 1
    Game = 2
    Movie = 3
    Television = 4
    Music = 5
class RatedContentDescription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription
    _classid_ = 'Windows.Media.ContentRestrictions.RatedContentDescription'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Media.ContentRestrictions.RatedContentDescription.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.ContentRestrictions.IRatedContentDescriptionFactory, id: WinRT_String, title: WinRT_String, category: win32more.Windows.Media.ContentRestrictions.RatedContentCategory) -> win32more.Windows.Media.ContentRestrictions.RatedContentDescription: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription) -> win32more.Windows.Media.ContentRestrictions.RatedContentCategory: ...
    @winrt_mixinmethod
    def put_Category(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription, value: win32more.Windows.Media.ContentRestrictions.RatedContentCategory) -> Void: ...
    @winrt_mixinmethod
    def get_Ratings(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def put_Ratings(self: win32more.Windows.Media.ContentRestrictions.IRatedContentDescription, value: win32more.Windows.Foundation.Collections.IVector[WinRT_String]) -> Void: ...
    Category = property(get_Category, put_Category)
    Id = property(get_Id, put_Id)
    Image = property(get_Image, put_Image)
    Ratings = property(get_Ratings, put_Ratings)
    Title = property(get_Title, put_Title)
class RatedContentRestrictions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictions
    _classid_ = 'Windows.Media.ContentRestrictions.RatedContentRestrictions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.ContentRestrictions.RatedContentRestrictions.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.ContentRestrictions.RatedContentRestrictions.CreateWithMaxAgeRating(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.ContentRestrictions.RatedContentRestrictions: ...
    @winrt_factorymethod
    def CreateWithMaxAgeRating(cls: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictionsFactory, maxAgeRating: UInt32) -> win32more.Windows.Media.ContentRestrictions.RatedContentRestrictions: ...
    @winrt_mixinmethod
    def GetBrowsePolicyAsync(self: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.ContentRestrictions.ContentRestrictionsBrowsePolicy]: ...
    @winrt_mixinmethod
    def GetRestrictionLevelAsync(self: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictions, RatedContentDescription: win32more.Windows.Media.ContentRestrictions.RatedContentDescription) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.ContentRestrictions.ContentAccessRestrictionLevel]: ...
    @winrt_mixinmethod
    def RequestContentAccessAsync(self: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictions, RatedContentDescription: win32more.Windows.Media.ContentRestrictions.RatedContentDescription) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_RestrictionsChanged(self: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictions, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RestrictionsChanged(self: win32more.Windows.Media.ContentRestrictions.IRatedContentRestrictions, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    RestrictionsChanged = event()


make_ready(__name__)
