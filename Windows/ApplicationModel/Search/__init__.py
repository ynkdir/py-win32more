from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Search
import Windows.Foundation.Collections
import Windows.Storage
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
class ILocalContentSuggestionSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eeaeb062-743d-456e-84-a3-23-f0-6f-2d-15-d7')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Locations(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(9)
    def put_AqsFilter(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AqsFilter(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PropertiesToMatch(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Enabled = property(get_Enabled, put_Enabled)
    Locations = property(get_Locations, None)
    AqsFilter = property(get_AqsFilter, put_AqsFilter)
    PropertiesToMatch = property(get_PropertiesToMatch, None)
class ISearchPaneQueryLinguisticDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('82fb460e-0940-4b6d-b8-d0-64-2b-30-98-9e-15')
    @winrt_commethod(6)
    def get_QueryTextAlternatives(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_QueryTextCompositionStart(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_QueryTextCompositionLength(self) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class ISearchQueryLinguisticDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('46a1205b-69c9-4745-b7-2f-a8-a4-fc-8f-24-ae')
    @winrt_commethod(6)
    def get_QueryTextAlternatives(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_QueryTextCompositionStart(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_QueryTextCompositionLength(self) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class ISearchQueryLinguisticDetailsFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cac6c3b8-3c64-4dfd-ad-9f-47-9e-4d-40-65-a4')
    @winrt_commethod(6)
    def CreateInstance(self, queryTextAlternatives: Windows.Foundation.Collections.IIterable[WinRT_String], queryTextCompositionStart: UInt32, queryTextCompositionLength: UInt32) -> Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
class ISearchSuggestionCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('323a8a4b-fbea-4446-ab-bc-3d-a7-91-5f-dd-3a')
    @winrt_commethod(6)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(7)
    def AppendQuerySuggestion(self, text: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def AppendQuerySuggestions(self, suggestions: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(9)
    def AppendResultSuggestion(self, text: WinRT_String, detailText: WinRT_String, tag: WinRT_String, image: Windows.Storage.Streams.IRandomAccessStreamReference, imageAlternateText: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def AppendSearchSeparator(self, label: WinRT_String) -> Void: ...
    Size = property(get_Size, None)
class ISearchSuggestionsRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e4e26a7-44e5-4039-90-99-60-00-ea-d1-f0-c6')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SearchSuggestionCollection(self) -> Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class ISearchSuggestionsRequestDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b71598a9-c065-456d-a8-45-1e-cc-ec-5d-c2-8b')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class LocalContentSuggestionSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Search.LocalContentSuggestionSettings'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Search.LocalContentSuggestionSettings: ...
    @winrt_mixinmethod
    def put_Enabled(self: Windows.ApplicationModel.Search.ILocalContentSuggestionSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_Locations(self: Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> Windows.Foundation.Collections.IVector[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def put_AqsFilter(self: Windows.ApplicationModel.Search.ILocalContentSuggestionSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AqsFilter(self: Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PropertiesToMatch(self: Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Enabled = property(get_Enabled, put_Enabled)
    Locations = property(get_Locations, None)
    AqsFilter = property(get_AqsFilter, put_AqsFilter)
    PropertiesToMatch = property(get_PropertiesToMatch, None)
class SearchPaneQueryLinguisticDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails'
    @winrt_mixinmethod
    def get_QueryTextAlternatives(self: Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionStart(self: Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionLength(self: Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class SearchQueryLinguisticDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Search.SearchQueryLinguisticDetails'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.ApplicationModel.Search.ISearchQueryLinguisticDetailsFactory, queryTextAlternatives: Windows.Foundation.Collections.IIterable[WinRT_String], queryTextCompositionStart: UInt32, queryTextCompositionLength: UInt32) -> Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_QueryTextAlternatives(self: Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionStart(self: Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionLength(self: Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class SearchSuggestionCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Search.SearchSuggestionCollection'
    @winrt_mixinmethod
    def get_Size(self: Windows.ApplicationModel.Search.ISearchSuggestionCollection) -> UInt32: ...
    @winrt_mixinmethod
    def AppendQuerySuggestion(self: Windows.ApplicationModel.Search.ISearchSuggestionCollection, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AppendQuerySuggestions(self: Windows.ApplicationModel.Search.ISearchSuggestionCollection, suggestions: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def AppendResultSuggestion(self: Windows.ApplicationModel.Search.ISearchSuggestionCollection, text: WinRT_String, detailText: WinRT_String, tag: WinRT_String, image: Windows.Storage.Streams.IRandomAccessStreamReference, imageAlternateText: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AppendSearchSeparator(self: Windows.ApplicationModel.Search.ISearchSuggestionCollection, label: WinRT_String) -> Void: ...
    Size = property(get_Size, None)
class SearchSuggestionsRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Search.SearchSuggestionsRequest'
    @winrt_mixinmethod
    def get_IsCanceled(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_SearchSuggestionCollection(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class SearchSuggestionsRequestDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequestDeferral) -> Void: ...
make_head(_module, 'ILocalContentSuggestionSettings')
make_head(_module, 'ISearchPaneQueryLinguisticDetails')
make_head(_module, 'ISearchQueryLinguisticDetails')
make_head(_module, 'ISearchQueryLinguisticDetailsFactory')
make_head(_module, 'ISearchSuggestionCollection')
make_head(_module, 'ISearchSuggestionsRequest')
make_head(_module, 'ISearchSuggestionsRequestDeferral')
make_head(_module, 'LocalContentSuggestionSettings')
make_head(_module, 'SearchPaneQueryLinguisticDetails')
make_head(_module, 'SearchQueryLinguisticDetails')
make_head(_module, 'SearchSuggestionCollection')
make_head(_module, 'SearchSuggestionsRequest')
make_head(_module, 'SearchSuggestionsRequestDeferral')
