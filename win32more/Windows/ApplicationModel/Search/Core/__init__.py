from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Search
import win32more.Windows.ApplicationModel.Search.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IRequestingFocusOnKeyboardInputEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.Core.IRequestingFocusOnKeyboardInputEventArgs'
    _iid_ = Guid('{a1195f27-b1a7-41a2-879d-6a68687e5985}')
class ISearchSuggestion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.Core.ISearchSuggestion'
    _iid_ = Guid('{5b5554b0-1527-437b-95c5-8d18d2b8af55}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionKind: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DetailText(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Image(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def get_ImageAlternateText(self) -> WinRT_String: ...
    Kind = property(get_Kind, None)
    Text = property(get_Text, None)
    Tag = property(get_Tag, None)
    DetailText = property(get_DetailText, None)
    Image = property(get_Image, None)
    ImageAlternateText = property(get_ImageAlternateText, None)
class ISearchSuggestionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.Core.ISearchSuggestionManager'
    _iid_ = Guid('{3f0c50a1-cb9d-497b-b500-3c04ac959ad2}')
    @winrt_commethod(6)
    def get_SearchHistoryEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SearchHistoryEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SearchHistoryContext(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_SearchHistoryContext(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def SetLocalContentSuggestionSettings(self, settings: win32more.Windows.ApplicationModel.Search.LocalContentSuggestionSettings) -> Void: ...
    @winrt_commethod(11)
    def SetQuery(self, queryText: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetQueryWithLanguage(self, queryText: WinRT_String, language: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def SetQueryWithSearchQueryLinguisticDetails(self, queryText: WinRT_String, language: WinRT_String, linguisticDetails: win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails) -> Void: ...
    @winrt_commethod(14)
    def get_Suggestions(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.ApplicationModel.Search.Core.SearchSuggestion]: ...
    @winrt_commethod(15)
    def AddToHistory(self, queryText: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def AddToHistoryWithLanguage(self, queryText: WinRT_String, language: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def ClearHistory(self) -> Void: ...
    @winrt_commethod(18)
    def add_SuggestionsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionManager, win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_SuggestionsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_RequestingFocusOnKeyboardInput(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionManager, win32more.Windows.ApplicationModel.Search.Core.RequestingFocusOnKeyboardInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_RequestingFocusOnKeyboardInput(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    Suggestions = property(get_Suggestions, None)
class ISearchSuggestionsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.Core.ISearchSuggestionsRequestedEventArgs'
    _iid_ = Guid('{6fd519e5-9e7e-4ab4-8be3-c76b1bd4344a}')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LinguisticDetails(self) -> win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
    @winrt_commethod(9)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionsRequest: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    Request = property(get_Request, None)
class RequestingFocusOnKeyboardInputEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.Core.IRequestingFocusOnKeyboardInputEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.Core.RequestingFocusOnKeyboardInputEventArgs'
SearchCoreContract: UInt32 = 65536
class SearchSuggestion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion
    _classid_ = 'Windows.ApplicationModel.Search.Core.SearchSuggestion'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion) -> win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionKind: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DetailText(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ImageAlternateText(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestion) -> WinRT_String: ...
    Kind = property(get_Kind, None)
    Text = property(get_Text, None)
    Tag = property(get_Tag, None)
    DetailText = property(get_DetailText, None)
    Image = property(get_Image, None)
    ImageAlternateText = property(get_ImageAlternateText, None)
SearchSuggestionKind = Int32
SearchSuggestionKind_Query: SearchSuggestionKind = 0
SearchSuggestionKind_Result: SearchSuggestionKind = 1
SearchSuggestionKind_Separator: SearchSuggestionKind = 2
class SearchSuggestionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager
    _classid_ = 'Windows.ApplicationModel.Search.Core.SearchSuggestionManager'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionManager: ...
    @winrt_mixinmethod
    def get_SearchHistoryEnabled(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager) -> Boolean: ...
    @winrt_mixinmethod
    def put_SearchHistoryEnabled(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SearchHistoryContext(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SearchHistoryContext(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetLocalContentSuggestionSettings(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, settings: win32more.Windows.ApplicationModel.Search.LocalContentSuggestionSettings) -> Void: ...
    @winrt_mixinmethod
    def SetQuery(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, queryText: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetQueryWithLanguage(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, queryText: WinRT_String, language: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetQueryWithSearchQueryLinguisticDetails(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, queryText: WinRT_String, language: WinRT_String, linguisticDetails: win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails) -> Void: ...
    @winrt_mixinmethod
    def get_Suggestions(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.ApplicationModel.Search.Core.SearchSuggestion]: ...
    @winrt_mixinmethod
    def AddToHistory(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, queryText: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddToHistoryWithLanguage(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, queryText: WinRT_String, language: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ClearHistory(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager) -> Void: ...
    @winrt_mixinmethod
    def add_SuggestionsRequested(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionManager, win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SuggestionsRequested(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RequestingFocusOnKeyboardInput(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionManager, win32more.Windows.ApplicationModel.Search.Core.RequestingFocusOnKeyboardInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RequestingFocusOnKeyboardInput(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    Suggestions = property(get_Suggestions, None)
class SearchSuggestionsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionsRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.Core.SearchSuggestionsRequestedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionsRequestedEventArgs) -> win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionsRequestedEventArgs) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionsRequest: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    Request = property(get_Request, None)
make_head(_module, 'IRequestingFocusOnKeyboardInputEventArgs')
make_head(_module, 'ISearchSuggestion')
make_head(_module, 'ISearchSuggestionManager')
make_head(_module, 'ISearchSuggestionsRequestedEventArgs')
make_head(_module, 'RequestingFocusOnKeyboardInputEventArgs')
make_head(_module, 'SearchSuggestion')
make_head(_module, 'SearchSuggestionManager')
make_head(_module, 'SearchSuggestionsRequestedEventArgs')
