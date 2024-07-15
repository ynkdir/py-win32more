from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Search
import win32more.Windows.ApplicationModel.Search.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
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
    DetailText = property(get_DetailText, None)
    Image = property(get_Image, None)
    ImageAlternateText = property(get_ImageAlternateText, None)
    Kind = property(get_Kind, None)
    Tag = property(get_Tag, None)
    Text = property(get_Text, None)
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
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    Suggestions = property(get_Suggestions, None)
    SuggestionsRequested = event()
    RequestingFocusOnKeyboardInput = event()
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
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    QueryText = property(get_QueryText, None)
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
    DetailText = property(get_DetailText, None)
    Image = property(get_Image, None)
    ImageAlternateText = property(get_ImageAlternateText, None)
    Kind = property(get_Kind, None)
    Tag = property(get_Tag, None)
    Text = property(get_Text, None)
class SearchSuggestionKind(Enum, Int32):
    Query = 0
    Result = 1
    Separator = 2
class SearchSuggestionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.Core.ISearchSuggestionManager
    _classid_ = 'Windows.ApplicationModel.Search.Core.SearchSuggestionManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Search.Core.SearchSuggestionManager.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    Suggestions = property(get_Suggestions, None)
    SuggestionsRequested = event()
    RequestingFocusOnKeyboardInput = event()
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
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    QueryText = property(get_QueryText, None)
    Request = property(get_Request, None)


make_ready(__name__)
