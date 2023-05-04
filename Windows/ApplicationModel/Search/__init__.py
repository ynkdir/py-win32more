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
import Windows.ApplicationModel.Search
import Windows.Foundation
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
class ILocalContentSuggestionSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{eeaeb062-743d-456e-84a3-23f06f2d15d7}')
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
class ISearchPane(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fdacec38-3700-4d73-91a1-2f998674238a}')
    @winrt_commethod(6)
    def put_SearchHistoryEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_SearchHistoryEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_SearchHistoryContext(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_SearchHistoryContext(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_PlaceholderText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_PlaceholderText(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(15)
    def add_VisibilityChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneVisibilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_VisibilityChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_QueryChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneQueryChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_QueryChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_SuggestionsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_SuggestionsRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_QuerySubmitted(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneQuerySubmittedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_QuerySubmitted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_ResultSuggestionChosen(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneResultSuggestionChosenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_ResultSuggestionChosen(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def SetLocalContentSuggestionSettings(self, settings: Windows.ApplicationModel.Search.LocalContentSuggestionSettings) -> Void: ...
    @winrt_commethod(26)
    def ShowOverloadDefault(self) -> Void: ...
    @winrt_commethod(27)
    def ShowOverloadWithQuery(self, query: WinRT_String) -> Void: ...
    @winrt_commethod(28)
    def put_ShowOnKeyboardInput(self, value: Boolean) -> Void: ...
    @winrt_commethod(29)
    def get_ShowOnKeyboardInput(self) -> Boolean: ...
    @winrt_commethod(30)
    def TrySetQueryText(self, query: WinRT_String) -> Boolean: ...
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    Visible = property(get_Visible, None)
    ShowOnKeyboardInput = property(get_ShowOnKeyboardInput, put_ShowOnKeyboardInput)
class ISearchPaneQueryChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3c064fe9-2351-4248-a529-7110f464a785}')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LinguisticDetails(self) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
class ISearchPaneQueryLinguisticDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{82fb460e-0940-4b6d-b8d0-642b30989e15}')
    @winrt_commethod(6)
    def get_QueryTextAlternatives(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_QueryTextCompositionStart(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_QueryTextCompositionLength(self) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class ISearchPaneQuerySubmittedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{143ba4fc-e9c5-4736-91b2-e8eb9cb88356}')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
class ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{460c92e5-4c32-4538-a4d4-b6b4400d140f}')
    @winrt_commethod(6)
    def get_LinguisticDetails(self) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    LinguisticDetails = property(get_LinguisticDetails, None)
class ISearchPaneResultSuggestionChosenEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c8316cc0-aed2-41e0-bce0-c26ca74f85ec}')
    @winrt_commethod(6)
    def get_Tag(self) -> WinRT_String: ...
    Tag = property(get_Tag, None)
class ISearchPaneStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9572adf1-8f1d-481f-a15b-c61655f16a0e}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.Search.SearchPane: ...
class ISearchPaneStaticsWithHideThisApplication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{00732830-50f1-4d03-99ac-c6644c8ed8b5}')
    @winrt_commethod(6)
    def HideThisApplication(self) -> Void: ...
class ISearchPaneSuggestionsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{81b10b1c-e561-4093-9b4d-2ad482794a53}')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SearchSuggestionCollection(self) -> Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class ISearchPaneSuggestionsRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a0d009f7-8748-4ee2-ad44-afa6be997c51}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISearchPaneSuggestionsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c89b8a2f-ac56-4460-8d2f-80023bec4fc5}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Search.SearchPaneSuggestionsRequest: ...
    Request = property(get_Request, None)
class ISearchPaneVisibilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3c4d3046-ac4b-49f2-97d6-020e6182cb9c}')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    Visible = property(get_Visible, None)
class ISearchQueryLinguisticDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{46a1205b-69c9-4745-b72f-a8a4fc8f24ae}')
    @winrt_commethod(6)
    def get_QueryTextAlternatives(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_QueryTextCompositionStart(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_QueryTextCompositionLength(self) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class ISearchQueryLinguisticDetailsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cac6c3b8-3c64-4dfd-ad9f-479e4d4065a4}')
    @winrt_commethod(6)
    def CreateInstance(self, queryTextAlternatives: Windows.Foundation.Collections.IIterable[WinRT_String], queryTextCompositionStart: UInt32, queryTextCompositionLength: UInt32) -> Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
class ISearchSuggestionCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{323a8a4b-fbea-4446-abbc-3da7915fdd3a}')
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
class ISearchSuggestionsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4e4e26a7-44e5-4039-9099-6000ead1f0c6}')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SearchSuggestionCollection(self) -> Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class ISearchSuggestionsRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b71598a9-c065-456d-a845-1eccec5dc28b}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class LocalContentSuggestionSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.LocalContentSuggestionSettings'
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
SearchContract: UInt32 = 65536
class SearchPane(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPane'
    @winrt_mixinmethod
    def put_SearchHistoryEnabled(self: Windows.ApplicationModel.Search.ISearchPane, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SearchHistoryEnabled(self: Windows.ApplicationModel.Search.ISearchPane) -> Boolean: ...
    @winrt_mixinmethod
    def put_SearchHistoryContext(self: Windows.ApplicationModel.Search.ISearchPane, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SearchHistoryContext(self: Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PlaceholderText(self: Windows.ApplicationModel.Search.ISearchPane, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderText(self: Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Visible(self: Windows.ApplicationModel.Search.ISearchPane) -> Boolean: ...
    @winrt_mixinmethod
    def add_VisibilityChanged(self: Windows.ApplicationModel.Search.ISearchPane, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneVisibilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibilityChanged(self: Windows.ApplicationModel.Search.ISearchPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_QueryChanged(self: Windows.ApplicationModel.Search.ISearchPane, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneQueryChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QueryChanged(self: Windows.ApplicationModel.Search.ISearchPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SuggestionsRequested(self: Windows.ApplicationModel.Search.ISearchPane, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SuggestionsRequested(self: Windows.ApplicationModel.Search.ISearchPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_QuerySubmitted(self: Windows.ApplicationModel.Search.ISearchPane, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneQuerySubmittedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QuerySubmitted(self: Windows.ApplicationModel.Search.ISearchPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResultSuggestionChosen(self: Windows.ApplicationModel.Search.ISearchPane, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Search.SearchPane, Windows.ApplicationModel.Search.SearchPaneResultSuggestionChosenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResultSuggestionChosen(self: Windows.ApplicationModel.Search.ISearchPane, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetLocalContentSuggestionSettings(self: Windows.ApplicationModel.Search.ISearchPane, settings: Windows.ApplicationModel.Search.LocalContentSuggestionSettings) -> Void: ...
    @winrt_mixinmethod
    def ShowOverloadDefault(self: Windows.ApplicationModel.Search.ISearchPane) -> Void: ...
    @winrt_mixinmethod
    def ShowOverloadWithQuery(self: Windows.ApplicationModel.Search.ISearchPane, query: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_ShowOnKeyboardInput(self: Windows.ApplicationModel.Search.ISearchPane, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowOnKeyboardInput(self: Windows.ApplicationModel.Search.ISearchPane) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetQueryText(self: Windows.ApplicationModel.Search.ISearchPane, query: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def HideThisApplication(cls: Windows.ApplicationModel.Search.ISearchPaneStaticsWithHideThisApplication) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.Search.ISearchPaneStatics) -> Windows.ApplicationModel.Search.SearchPane: ...
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    Visible = property(get_Visible, None)
    ShowOnKeyboardInput = property(get_ShowOnKeyboardInput, put_ShowOnKeyboardInput)
class SearchPaneQueryChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneQueryChangedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
class SearchPaneQueryLinguisticDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails'
    @winrt_mixinmethod
    def get_QueryTextAlternatives(self: Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionStart(self: Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionLength(self: Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
class SearchPaneQuerySubmittedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneQuerySubmittedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
class SearchPaneResultSuggestionChosenEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneResultSuggestionChosenEventArgs'
    @winrt_mixinmethod
    def get_Tag(self: Windows.ApplicationModel.Search.ISearchPaneResultSuggestionChosenEventArgs) -> WinRT_String: ...
    Tag = property(get_Tag, None)
class SearchPaneSuggestionsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneSuggestionsRequest'
    @winrt_mixinmethod
    def get_IsCanceled(self: Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_SearchSuggestionCollection(self: Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest) -> Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest) -> Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class SearchPaneSuggestionsRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestDeferral) -> Void: ...
class SearchPaneSuggestionsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestedEventArgs) -> Windows.ApplicationModel.Search.SearchPaneSuggestionsRequest: ...
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    Request = property(get_Request, None)
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
class SearchPaneVisibilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneVisibilityChangedEventArgs'
    @winrt_mixinmethod
    def get_Visible(self: Windows.ApplicationModel.Search.ISearchPaneVisibilityChangedEventArgs) -> Boolean: ...
    Visible = property(get_Visible, None)
class SearchQueryLinguisticDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchQueryLinguisticDetails'
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
class SearchSuggestionCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchSuggestionCollection'
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
class SearchSuggestionsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchSuggestionsRequest'
    @winrt_mixinmethod
    def get_IsCanceled(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_SearchSuggestionCollection(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class SearchSuggestionsRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.Search.ISearchSuggestionsRequestDeferral) -> Void: ...
make_head(_module, 'ILocalContentSuggestionSettings')
make_head(_module, 'ISearchPane')
make_head(_module, 'ISearchPaneQueryChangedEventArgs')
make_head(_module, 'ISearchPaneQueryLinguisticDetails')
make_head(_module, 'ISearchPaneQuerySubmittedEventArgs')
make_head(_module, 'ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails')
make_head(_module, 'ISearchPaneResultSuggestionChosenEventArgs')
make_head(_module, 'ISearchPaneStatics')
make_head(_module, 'ISearchPaneStaticsWithHideThisApplication')
make_head(_module, 'ISearchPaneSuggestionsRequest')
make_head(_module, 'ISearchPaneSuggestionsRequestDeferral')
make_head(_module, 'ISearchPaneSuggestionsRequestedEventArgs')
make_head(_module, 'ISearchPaneVisibilityChangedEventArgs')
make_head(_module, 'ISearchQueryLinguisticDetails')
make_head(_module, 'ISearchQueryLinguisticDetailsFactory')
make_head(_module, 'ISearchSuggestionCollection')
make_head(_module, 'ISearchSuggestionsRequest')
make_head(_module, 'ISearchSuggestionsRequestDeferral')
make_head(_module, 'LocalContentSuggestionSettings')
make_head(_module, 'SearchPane')
make_head(_module, 'SearchPaneQueryChangedEventArgs')
make_head(_module, 'SearchPaneQueryLinguisticDetails')
make_head(_module, 'SearchPaneQuerySubmittedEventArgs')
make_head(_module, 'SearchPaneResultSuggestionChosenEventArgs')
make_head(_module, 'SearchPaneSuggestionsRequest')
make_head(_module, 'SearchPaneSuggestionsRequestDeferral')
make_head(_module, 'SearchPaneSuggestionsRequestedEventArgs')
make_head(_module, 'SearchPaneVisibilityChangedEventArgs')
make_head(_module, 'SearchQueryLinguisticDetails')
make_head(_module, 'SearchSuggestionCollection')
make_head(_module, 'SearchSuggestionsRequest')
make_head(_module, 'SearchSuggestionsRequestDeferral')
