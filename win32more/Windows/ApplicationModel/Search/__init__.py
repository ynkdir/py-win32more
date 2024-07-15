from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Search
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ILocalContentSuggestionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ILocalContentSuggestionSettings'
    _iid_ = Guid('{eeaeb062-743d-456e-84a3-23f06f2d15d7}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Locations(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(9)
    def put_AqsFilter(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AqsFilter(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PropertiesToMatch(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    AqsFilter = property(get_AqsFilter, put_AqsFilter)
    Enabled = property(get_Enabled, put_Enabled)
    Locations = property(get_Locations, None)
    PropertiesToMatch = property(get_PropertiesToMatch, None)
class ISearchPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPane'
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
    def add_VisibilityChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneVisibilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_VisibilityChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_QueryChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneQueryChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_QueryChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_SuggestionsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_SuggestionsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_QuerySubmitted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneQuerySubmittedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_QuerySubmitted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_ResultSuggestionChosen(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneResultSuggestionChosenEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_ResultSuggestionChosen(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def SetLocalContentSuggestionSettings(self, settings: win32more.Windows.ApplicationModel.Search.LocalContentSuggestionSettings) -> Void: ...
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
    Language = property(get_Language, None)
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    QueryText = property(get_QueryText, None)
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    ShowOnKeyboardInput = property(get_ShowOnKeyboardInput, put_ShowOnKeyboardInput)
    Visible = property(get_Visible, None)
    VisibilityChanged = event()
    QueryChanged = event()
    SuggestionsRequested = event()
    QuerySubmitted = event()
    ResultSuggestionChosen = event()
class ISearchPaneQueryChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs'
    _iid_ = Guid('{3c064fe9-2351-4248-a529-7110f464a785}')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LinguisticDetails(self) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    QueryText = property(get_QueryText, None)
class ISearchPaneQueryLinguisticDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails'
    _iid_ = Guid('{82fb460e-0940-4b6d-b8d0-642b30989e15}')
    @winrt_commethod(6)
    def get_QueryTextAlternatives(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_QueryTextCompositionStart(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_QueryTextCompositionLength(self) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
class ISearchPaneQuerySubmittedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgs'
    _iid_ = Guid('{143ba4fc-e9c5-4736-91b2-e8eb9cb88356}')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    Language = property(get_Language, None)
    QueryText = property(get_QueryText, None)
class ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails'
    _iid_ = Guid('{460c92e5-4c32-4538-a4d4-b6b4400d140f}')
    @winrt_commethod(6)
    def get_LinguisticDetails(self) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    LinguisticDetails = property(get_LinguisticDetails, None)
class ISearchPaneResultSuggestionChosenEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneResultSuggestionChosenEventArgs'
    _iid_ = Guid('{c8316cc0-aed2-41e0-bce0-c26ca74f85ec}')
    @winrt_commethod(6)
    def get_Tag(self) -> WinRT_String: ...
    Tag = property(get_Tag, None)
class ISearchPaneStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneStatics'
    _iid_ = Guid('{9572adf1-8f1d-481f-a15b-c61655f16a0e}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.Search.SearchPane: ...
class ISearchPaneStaticsWithHideThisApplication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneStaticsWithHideThisApplication'
    _iid_ = Guid('{00732830-50f1-4d03-99ac-c6644c8ed8b5}')
    @winrt_commethod(6)
    def HideThisApplication(self) -> Void: ...
class ISearchPaneSuggestionsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest'
    _iid_ = Guid('{81b10b1c-e561-4093-9b4d-2ad482794a53}')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SearchSuggestionCollection(self) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class ISearchPaneSuggestionsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestDeferral'
    _iid_ = Guid('{a0d009f7-8748-4ee2-ad44-afa6be997c51}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISearchPaneSuggestionsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestedEventArgs'
    _iid_ = Guid('{c89b8a2f-ac56-4460-8d2f-80023bec4fc5}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Search.SearchPaneSuggestionsRequest: ...
    Request = property(get_Request, None)
class ISearchPaneVisibilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchPaneVisibilityChangedEventArgs'
    _iid_ = Guid('{3c4d3046-ac4b-49f2-97d6-020e6182cb9c}')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    Visible = property(get_Visible, None)
class ISearchQueryLinguisticDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails'
    _iid_ = Guid('{46a1205b-69c9-4745-b72f-a8a4fc8f24ae}')
    @winrt_commethod(6)
    def get_QueryTextAlternatives(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_QueryTextCompositionStart(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_QueryTextCompositionLength(self) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
class ISearchQueryLinguisticDetailsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchQueryLinguisticDetailsFactory'
    _iid_ = Guid('{cac6c3b8-3c64-4dfd-ad9f-479e4d4065a4}')
    @winrt_commethod(6)
    def CreateInstance(self, queryTextAlternatives: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], queryTextCompositionStart: UInt32, queryTextCompositionLength: UInt32) -> win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
class ISearchSuggestionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchSuggestionCollection'
    _iid_ = Guid('{323a8a4b-fbea-4446-abbc-3da7915fdd3a}')
    @winrt_commethod(6)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(7)
    def AppendQuerySuggestion(self, text: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def AppendQuerySuggestions(self, suggestions: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(9)
    def AppendResultSuggestion(self, text: WinRT_String, detailText: WinRT_String, tag: WinRT_String, image: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, imageAlternateText: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def AppendSearchSeparator(self, label: WinRT_String) -> Void: ...
    Size = property(get_Size, None)
class ISearchSuggestionsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchSuggestionsRequest'
    _iid_ = Guid('{4e4e26a7-44e5-4039-9099-6000ead1f0c6}')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SearchSuggestionCollection(self) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class ISearchSuggestionsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Search.ISearchSuggestionsRequestDeferral'
    _iid_ = Guid('{b71598a9-c065-456d-a845-1eccec5dc28b}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class LocalContentSuggestionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings
    _classid_ = 'Windows.ApplicationModel.Search.LocalContentSuggestionSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Search.LocalContentSuggestionSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Search.LocalContentSuggestionSettings: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_Locations(self: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def put_AqsFilter(self: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AqsFilter(self: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PropertiesToMatch(self: win32more.Windows.ApplicationModel.Search.ILocalContentSuggestionSettings) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    AqsFilter = property(get_AqsFilter, put_AqsFilter)
    Enabled = property(get_Enabled, put_Enabled)
    Locations = property(get_Locations, None)
    PropertiesToMatch = property(get_PropertiesToMatch, None)
SearchContract: UInt32 = 65536
class SearchPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPane
    _classid_ = 'Windows.ApplicationModel.Search.SearchPane'
    @winrt_mixinmethod
    def put_SearchHistoryEnabled(self: win32more.Windows.ApplicationModel.Search.ISearchPane, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SearchHistoryEnabled(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> Boolean: ...
    @winrt_mixinmethod
    def put_SearchHistoryContext(self: win32more.Windows.ApplicationModel.Search.ISearchPane, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SearchHistoryContext(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PlaceholderText(self: win32more.Windows.ApplicationModel.Search.ISearchPane, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderText(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> Boolean: ...
    @winrt_mixinmethod
    def add_VisibilityChanged(self: win32more.Windows.ApplicationModel.Search.ISearchPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneVisibilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisibilityChanged(self: win32more.Windows.ApplicationModel.Search.ISearchPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_QueryChanged(self: win32more.Windows.ApplicationModel.Search.ISearchPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneQueryChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QueryChanged(self: win32more.Windows.ApplicationModel.Search.ISearchPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SuggestionsRequested(self: win32more.Windows.ApplicationModel.Search.ISearchPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SuggestionsRequested(self: win32more.Windows.ApplicationModel.Search.ISearchPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_QuerySubmitted(self: win32more.Windows.ApplicationModel.Search.ISearchPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneQuerySubmittedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_QuerySubmitted(self: win32more.Windows.ApplicationModel.Search.ISearchPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResultSuggestionChosen(self: win32more.Windows.ApplicationModel.Search.ISearchPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Search.SearchPane, win32more.Windows.ApplicationModel.Search.SearchPaneResultSuggestionChosenEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResultSuggestionChosen(self: win32more.Windows.ApplicationModel.Search.ISearchPane, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetLocalContentSuggestionSettings(self: win32more.Windows.ApplicationModel.Search.ISearchPane, settings: win32more.Windows.ApplicationModel.Search.LocalContentSuggestionSettings) -> Void: ...
    @winrt_mixinmethod
    def ShowOverloadDefault(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> Void: ...
    @winrt_mixinmethod
    def ShowOverloadWithQuery(self: win32more.Windows.ApplicationModel.Search.ISearchPane, query: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_ShowOnKeyboardInput(self: win32more.Windows.ApplicationModel.Search.ISearchPane, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowOnKeyboardInput(self: win32more.Windows.ApplicationModel.Search.ISearchPane) -> Boolean: ...
    @winrt_mixinmethod
    def TrySetQueryText(self: win32more.Windows.ApplicationModel.Search.ISearchPane, query: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def HideThisApplication(cls: win32more.Windows.ApplicationModel.Search.ISearchPaneStaticsWithHideThisApplication) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.Search.ISearchPaneStatics) -> win32more.Windows.ApplicationModel.Search.SearchPane: ...
    Language = property(get_Language, None)
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    QueryText = property(get_QueryText, None)
    SearchHistoryContext = property(get_SearchHistoryContext, put_SearchHistoryContext)
    SearchHistoryEnabled = property(get_SearchHistoryEnabled, put_SearchHistoryEnabled)
    ShowOnKeyboardInput = property(get_ShowOnKeyboardInput, put_ShowOnKeyboardInput)
    Visible = property(get_Visible, None)
    VisibilityChanged = event()
    QueryChanged = event()
    SuggestionsRequested = event()
    QuerySubmitted = event()
    ResultSuggestionChosen = event()
class SearchPaneQueryChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneQueryChangedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    QueryText = property(get_QueryText, None)
class SearchPaneQueryLinguisticDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails'
    @winrt_mixinmethod
    def get_QueryTextAlternatives(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionStart(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionLength(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryLinguisticDetails) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
class SearchPaneQuerySubmittedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneQuerySubmittedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    QueryText = property(get_QueryText, None)
class SearchPaneResultSuggestionChosenEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneResultSuggestionChosenEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneResultSuggestionChosenEventArgs'
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.ApplicationModel.Search.ISearchPaneResultSuggestionChosenEventArgs) -> WinRT_String: ...
    Tag = property(get_Tag, None)
class SearchPaneSuggestionsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneSuggestionsRequest'
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_SearchSuggestionCollection(self: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequest) -> win32more.Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class SearchPaneSuggestionsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestDeferral
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestDeferral) -> Void: ...
class SearchPaneSuggestionsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneSuggestionsRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Search.ISearchPaneSuggestionsRequestedEventArgs) -> win32more.Windows.ApplicationModel.Search.SearchPaneSuggestionsRequest: ...
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Search.ISearchPaneQueryChangedEventArgs) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    QueryText = property(get_QueryText, None)
    Request = property(get_Request, None)
class SearchPaneVisibilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchPaneVisibilityChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Search.SearchPaneVisibilityChangedEventArgs'
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.ApplicationModel.Search.ISearchPaneVisibilityChangedEventArgs) -> Boolean: ...
    Visible = property(get_Visible, None)
class SearchQueryLinguisticDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails
    _classid_ = 'Windows.ApplicationModel.Search.SearchQueryLinguisticDetails'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.ApplicationModel.Search.ISearchQueryLinguisticDetailsFactory, queryTextAlternatives: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], queryTextCompositionStart: UInt32, queryTextCompositionLength: UInt32) -> win32more.Windows.ApplicationModel.Search.SearchQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_QueryTextAlternatives(self: win32more.Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionStart(self: win32more.Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_QueryTextCompositionLength(self: win32more.Windows.ApplicationModel.Search.ISearchQueryLinguisticDetails) -> UInt32: ...
    QueryTextAlternatives = property(get_QueryTextAlternatives, None)
    QueryTextCompositionLength = property(get_QueryTextCompositionLength, None)
    QueryTextCompositionStart = property(get_QueryTextCompositionStart, None)
class SearchSuggestionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchSuggestionCollection
    _classid_ = 'Windows.ApplicationModel.Search.SearchSuggestionCollection'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionCollection) -> UInt32: ...
    @winrt_mixinmethod
    def AppendQuerySuggestion(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionCollection, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AppendQuerySuggestions(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionCollection, suggestions: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def AppendResultSuggestion(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionCollection, text: WinRT_String, detailText: WinRT_String, tag: WinRT_String, image: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, imageAlternateText: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AppendSearchSeparator(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionCollection, label: WinRT_String) -> Void: ...
    Size = property(get_Size, None)
class SearchSuggestionsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchSuggestionsRequest
    _classid_ = 'Windows.ApplicationModel.Search.SearchSuggestionsRequest'
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_SearchSuggestionCollection(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionCollection: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionsRequest) -> win32more.Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral: ...
    IsCanceled = property(get_IsCanceled, None)
    SearchSuggestionCollection = property(get_SearchSuggestionCollection, None)
class SearchSuggestionsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Search.ISearchSuggestionsRequestDeferral
    _classid_ = 'Windows.ApplicationModel.Search.SearchSuggestionsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Search.ISearchSuggestionsRequestDeferral) -> Void: ...


make_ready(__name__)
