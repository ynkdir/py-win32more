from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.UI.Text
import win32more.Windows.UI.Text.Core
import win32more.Windows.UI.ViewManagement
import win32more.Windows.Win32.System.WinRT
class CoreTextCompositionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextCompositionCompletedEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextCompositionCompletedEventArgs'
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_CompositionSegments(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionCompletedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Text.Core.CoreTextCompositionSegment]: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionCompletedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    CompositionSegments = property(get_CompositionSegments, None)
    IsCanceled = property(get_IsCanceled, None)
class CoreTextCompositionSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextCompositionSegment
    _classid_ = 'Windows.UI.Text.Core.CoreTextCompositionSegment'
    @winrt_mixinmethod
    def get_PreconversionString(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionSegment) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    PreconversionString = property(get_PreconversionString, None)
    Range = property(get_Range, None)
class CoreTextCompositionStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextCompositionStartedEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextCompositionStartedEventArgs'
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionStartedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextCompositionStartedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
class CoreTextEditContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextEditContext
    _classid_ = 'Windows.UI.Text.Core.CoreTextEditContext'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_InputScope(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> win32more.Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_mixinmethod
    def put_InputScope(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, value: win32more.Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsReadOnly(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputPaneDisplayPolicy(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> win32more.Windows.UI.Text.Core.CoreTextInputPaneDisplayPolicy: ...
    @winrt_mixinmethod
    def put_InputPaneDisplayPolicy(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, value: win32more.Windows.UI.Text.Core.CoreTextInputPaneDisplayPolicy) -> Void: ...
    @winrt_mixinmethod
    def add_TextRequested(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextTextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextRequested(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SelectionRequested(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextSelectionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionRequested(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LayoutRequested(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextLayoutRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LayoutRequested(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TextUpdating(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextTextUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextUpdating(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SelectionUpdating(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextSelectionUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionUpdating(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FormatUpdating(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FormatUpdating(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CompositionStarted(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextCompositionStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CompositionStarted(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CompositionCompleted(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextCompositionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CompositionCompleted(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FocusRemoved(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusRemoved(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyFocusEnter(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> Void: ...
    @winrt_mixinmethod
    def NotifyFocusLeave(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> Void: ...
    @winrt_mixinmethod
    def NotifyTextChanged(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, modifiedRange: win32more.Windows.UI.Text.Core.CoreTextRange, newLength: Int32, newSelection: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_mixinmethod
    def NotifySelectionChanged(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext, selection: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_mixinmethod
    def NotifyLayoutChanged(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext) -> Void: ...
    @winrt_mixinmethod
    def add_NotifyFocusLeaveCompleted(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotifyFocusLeaveCompleted(self: win32more.Windows.UI.Text.Core.ICoreTextEditContext2, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    InputPaneDisplayPolicy = property(get_InputPaneDisplayPolicy, put_InputPaneDisplayPolicy)
    InputScope = property(get_InputScope, put_InputScope)
    IsReadOnly = property(get_IsReadOnly, put_IsReadOnly)
    Name = property(get_Name, put_Name)
    TextRequested = event()
    SelectionRequested = event()
    LayoutRequested = event()
    TextUpdating = event()
    SelectionUpdating = event()
    FormatUpdating = event()
    CompositionStarted = event()
    CompositionCompleted = event()
    FocusRemoved = event()
    NotifyFocusLeaveCompleted = event()
class CoreTextFormatUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextFormatUpdatingEventArgs'
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_TextColor(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.ViewManagement.UIElementType]: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.ViewManagement.UIElementType]: ...
    @winrt_mixinmethod
    def get_UnderlineColor(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.ViewManagement.UIElementType]: ...
    @winrt_mixinmethod
    def get_UnderlineType(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Text.UnderlineType]: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingReason: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingResult: ...
    @winrt_mixinmethod
    def put_Result(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs, value: win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingResult) -> Void: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    BackgroundColor = property(get_BackgroundColor, None)
    IsCanceled = property(get_IsCanceled, None)
    Range = property(get_Range, None)
    Reason = property(get_Reason, None)
    Result = property(get_Result, put_Result)
    TextColor = property(get_TextColor, None)
    UnderlineColor = property(get_UnderlineColor, None)
    UnderlineType = property(get_UnderlineType, None)
class CoreTextFormatUpdatingReason(Enum, Int32):
    None_ = 0
    CompositionUnconverted = 1
    CompositionConverted = 2
    CompositionTargetUnconverted = 3
    CompositionTargetConverted = 4
class CoreTextFormatUpdatingResult(Enum, Int32):
    Succeeded = 0
    Failed = 1
class CoreTextInputPaneDisplayPolicy(Enum, Int32):
    Automatic = 0
    Manual = 1
class CoreTextInputScope(Enum, Int32):
    Default = 0
    Url = 1
    FilePath = 2
    FileName = 3
    EmailUserName = 4
    EmailAddress = 5
    UserName = 6
    PersonalFullName = 7
    PersonalNamePrefix = 8
    PersonalGivenName = 9
    PersonalMiddleName = 10
    PersonalSurname = 11
    PersonalNameSuffix = 12
    Address = 13
    AddressPostalCode = 14
    AddressStreet = 15
    AddressStateOrProvince = 16
    AddressCity = 17
    AddressCountryName = 18
    AddressCountryShortName = 19
    CurrencyAmountAndSymbol = 20
    CurrencyAmount = 21
    Date = 22
    DateMonth = 23
    DateDay = 24
    DateYear = 25
    DateMonthName = 26
    DateDayName = 27
    Number = 29
    SingleCharacter = 30
    Password = 31
    TelephoneNumber = 32
    TelephoneCountryCode = 33
    TelephoneAreaCode = 34
    TelephoneLocalNumber = 35
    Time = 36
    TimeHour = 37
    TimeMinuteOrSecond = 38
    NumberFullWidth = 39
    AlphanumericHalfWidth = 40
    AlphanumericFullWidth = 41
    CurrencyChinese = 42
    Bopomofo = 43
    Hiragana = 44
    KatakanaHalfWidth = 45
    KatakanaFullWidth = 46
    Hanja = 47
    HangulHalfWidth = 48
    HangulFullWidth = 49
    Search = 50
    Formula = 51
    SearchIncremental = 52
    ChineseHalfWidth = 53
    ChineseFullWidth = 54
    NativeScript = 55
    Text = 57
    Chat = 58
    NameOrPhoneNumber = 59
    EmailUserNameOrAddress = 60
    Private = 61
    Maps = 62
    PasswordNumeric = 63
    FormulaNumber = 67
    ChatWithoutEmoji = 68
    Digits = 28
    PinNumeric = 64
    PinAlphanumeric = 65
class CoreTextLayoutBounds(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextLayoutBounds
    _classid_ = 'Windows.UI.Text.Core.CoreTextLayoutBounds'
    @winrt_mixinmethod
    def get_TextBounds(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutBounds) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_TextBounds(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutBounds, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_ControlBounds(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutBounds) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_ControlBounds(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutBounds, value: win32more.Windows.Foundation.Rect) -> Void: ...
    ControlBounds = property(get_ControlBounds, put_ControlBounds)
    TextBounds = property(get_TextBounds, put_TextBounds)
class CoreTextLayoutRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequest
    _classid_ = 'Windows.UI.Text.Core.CoreTextLayoutRequest'
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequest) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_LayoutBounds(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequest) -> win32more.Windows.UI.Text.Core.CoreTextLayoutBounds: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequest) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequest) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_LayoutBoundsVisualPixels(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequest2) -> win32more.Windows.UI.Text.Core.CoreTextLayoutBounds: ...
    IsCanceled = property(get_IsCanceled, None)
    LayoutBounds = property(get_LayoutBounds, None)
    LayoutBoundsVisualPixels = property(get_LayoutBoundsVisualPixels, None)
    Range = property(get_Range, None)
class CoreTextLayoutRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequestedEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextLayoutRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequestedEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextLayoutRequest: ...
    Request = property(get_Request, None)
class CoreTextRange(Structure):
    StartCaretPosition: Int32
    EndCaretPosition: Int32
class CoreTextSelectionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequest
    _classid_ = 'Windows.UI.Text.Core.CoreTextSelectionRequest'
    @winrt_mixinmethod
    def get_Selection(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequest) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def put_Selection(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequest, value: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequest) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequest) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    Selection = property(get_Selection, put_Selection)
class CoreTextSelectionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequestedEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextSelectionRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionRequestedEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextSelectionRequest: ...
    Request = property(get_Request, None)
class CoreTextSelectionUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextSelectionUpdatingEventArgs'
    @winrt_mixinmethod
    def get_Selection(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextSelectionUpdatingResult: ...
    @winrt_mixinmethod
    def put_Result(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs, value: win32more.Windows.UI.Text.Core.CoreTextSelectionUpdatingResult) -> Void: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    Result = property(get_Result, put_Result)
    Selection = property(get_Selection, None)
class CoreTextSelectionUpdatingResult(Enum, Int32):
    Succeeded = 0
    Failed = 1
class _CoreTextServicesConstants_Meta_(ComPtr.__class__):
    pass
class CoreTextServicesConstants(ComPtr, metaclass=_CoreTextServicesConstants_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.CoreTextServicesConstants'
    @winrt_classmethod
    def get_HiddenCharacter(cls: win32more.Windows.UI.Text.Core.ICoreTextServicesStatics) -> Char: ...
    _CoreTextServicesConstants_Meta_.HiddenCharacter = property(get_HiddenCharacter, None)
class CoreTextServicesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextServicesManager
    _classid_ = 'Windows.UI.Text.Core.CoreTextServicesManager'
    @winrt_mixinmethod
    def get_InputLanguage(self: win32more.Windows.UI.Text.Core.ICoreTextServicesManager) -> win32more.Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def add_InputLanguageChanged(self: win32more.Windows.UI.Text.Core.ICoreTextServicesManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextServicesManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputLanguageChanged(self: win32more.Windows.UI.Text.Core.ICoreTextServicesManager, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateEditContext(self: win32more.Windows.UI.Text.Core.ICoreTextServicesManager) -> win32more.Windows.UI.Text.Core.CoreTextEditContext: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Text.Core.ICoreTextServicesManagerStatics) -> win32more.Windows.UI.Text.Core.CoreTextServicesManager: ...
    InputLanguage = property(get_InputLanguage, None)
    InputLanguageChanged = event()
class CoreTextTextRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextTextRequest
    _classid_ = 'Windows.UI.Text.Core.CoreTextTextRequest'
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Text.Core.ICoreTextTextRequest) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Text.Core.ICoreTextTextRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.Text.Core.ICoreTextTextRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextTextRequest) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextTextRequest) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    Range = property(get_Range, None)
    Text = property(get_Text, put_Text)
class CoreTextTextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextTextRequestedEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextTextRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Text.Core.ICoreTextTextRequestedEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextTextRequest: ...
    Request = property(get_Request, None)
class CoreTextTextUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextTextUpdatingEventArgs'
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewSelection(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_InputLanguage(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> win32more.Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextTextUpdatingResult: ...
    @winrt_mixinmethod
    def put_Result(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs, value: win32more.Windows.UI.Text.Core.CoreTextTextUpdatingResult) -> Void: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    InputLanguage = property(get_InputLanguage, None)
    IsCanceled = property(get_IsCanceled, None)
    NewSelection = property(get_NewSelection, None)
    Range = property(get_Range, None)
    Result = property(get_Result, put_Result)
    Text = property(get_Text, None)
class CoreTextTextUpdatingResult(Enum, Int32):
    Succeeded = 0
    Failed = 1
class ICoreTextCompositionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextCompositionCompletedEventArgs'
    _iid_ = Guid('{1f34ebb6-b79f-4121-a5e7-fda9b8616e30}')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CompositionSegments(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Text.Core.CoreTextCompositionSegment]: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    CompositionSegments = property(get_CompositionSegments, None)
    IsCanceled = property(get_IsCanceled, None)
class ICoreTextCompositionSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextCompositionSegment'
    _iid_ = Guid('{776c6bd9-4ead-4da7-8f47-3a88b523cc34}')
    @winrt_commethod(6)
    def get_PreconversionString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    PreconversionString = property(get_PreconversionString, None)
    Range = property(get_Range, None)
class ICoreTextCompositionStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextCompositionStartedEventArgs'
    _iid_ = Guid('{276b16a9-64e7-4ab0-bc4b-a02d73835bfb}')
    @winrt_commethod(6)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
class ICoreTextEditContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextEditContext'
    _iid_ = Guid('{bf6608af-4041-47c3-b263-a918eb5eaef2}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_InputScope(self) -> win32more.Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_commethod(9)
    def put_InputScope(self, value: win32more.Windows.UI.Text.Core.CoreTextInputScope) -> Void: ...
    @winrt_commethod(10)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsReadOnly(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_InputPaneDisplayPolicy(self) -> win32more.Windows.UI.Text.Core.CoreTextInputPaneDisplayPolicy: ...
    @winrt_commethod(13)
    def put_InputPaneDisplayPolicy(self, value: win32more.Windows.UI.Text.Core.CoreTextInputPaneDisplayPolicy) -> Void: ...
    @winrt_commethod(14)
    def add_TextRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextTextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_TextRequested(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_SelectionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextSelectionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SelectionRequested(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_LayoutRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextLayoutRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_LayoutRequested(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_TextUpdating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextTextUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_TextUpdating(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_SelectionUpdating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextSelectionUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_SelectionUpdating(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_FormatUpdating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_FormatUpdating(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_CompositionStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextCompositionStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_CompositionStarted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_CompositionCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.UI.Text.Core.CoreTextCompositionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_CompositionCompleted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_FocusRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_FocusRemoved(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def NotifyFocusEnter(self) -> Void: ...
    @winrt_commethod(33)
    def NotifyFocusLeave(self) -> Void: ...
    @winrt_commethod(34)
    def NotifyTextChanged(self, modifiedRange: win32more.Windows.UI.Text.Core.CoreTextRange, newLength: Int32, newSelection: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_commethod(35)
    def NotifySelectionChanged(self, selection: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_commethod(36)
    def NotifyLayoutChanged(self) -> Void: ...
    InputPaneDisplayPolicy = property(get_InputPaneDisplayPolicy, put_InputPaneDisplayPolicy)
    InputScope = property(get_InputScope, put_InputScope)
    IsReadOnly = property(get_IsReadOnly, put_IsReadOnly)
    Name = property(get_Name, put_Name)
    TextRequested = event()
    SelectionRequested = event()
    LayoutRequested = event()
    TextUpdating = event()
    SelectionUpdating = event()
    FormatUpdating = event()
    CompositionStarted = event()
    CompositionCompleted = event()
    FocusRemoved = event()
class ICoreTextEditContext2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextEditContext2'
    _iid_ = Guid('{b1867dbb-083b-49e1-b281-2b35d62bf466}')
    @winrt_commethod(6)
    def add_NotifyFocusLeaveCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NotifyFocusLeaveCompleted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    NotifyFocusLeaveCompleted = event()
class ICoreTextFormatUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextFormatUpdatingEventArgs'
    _iid_ = Guid('{7310bd33-b4a8-43b1-b37b-0724d4aca7ab}')
    @winrt_commethod(6)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(7)
    def get_TextColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.ViewManagement.UIElementType]: ...
    @winrt_commethod(8)
    def get_BackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.ViewManagement.UIElementType]: ...
    @winrt_commethod(9)
    def get_UnderlineColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.ViewManagement.UIElementType]: ...
    @winrt_commethod(10)
    def get_UnderlineType(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Text.UnderlineType]: ...
    @winrt_commethod(11)
    def get_Reason(self) -> win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingReason: ...
    @winrt_commethod(12)
    def get_Result(self) -> win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingResult: ...
    @winrt_commethod(13)
    def put_Result(self, value: win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingResult) -> Void: ...
    @winrt_commethod(14)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(15)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    BackgroundColor = property(get_BackgroundColor, None)
    IsCanceled = property(get_IsCanceled, None)
    Range = property(get_Range, None)
    Reason = property(get_Reason, None)
    Result = property(get_Result, put_Result)
    TextColor = property(get_TextColor, None)
    UnderlineColor = property(get_UnderlineColor, None)
    UnderlineType = property(get_UnderlineType, None)
class ICoreTextLayoutBounds(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextLayoutBounds'
    _iid_ = Guid('{e972c974-4436-4917-80d0-a525e4ca6780}')
    @winrt_commethod(6)
    def get_TextBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_TextBounds(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(8)
    def get_ControlBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_ControlBounds(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    ControlBounds = property(get_ControlBounds, put_ControlBounds)
    TextBounds = property(get_TextBounds, put_TextBounds)
class ICoreTextLayoutRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextLayoutRequest'
    _iid_ = Guid('{2555a8cc-51fd-4f03-98bf-ac78174d68e0}')
    @winrt_commethod(6)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(7)
    def get_LayoutBounds(self) -> win32more.Windows.UI.Text.Core.CoreTextLayoutBounds: ...
    @winrt_commethod(8)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    LayoutBounds = property(get_LayoutBounds, None)
    Range = property(get_Range, None)
class ICoreTextLayoutRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextLayoutRequest2'
    _iid_ = Guid('{676de624-cd3d-4bcd-bf01-7f7110954511}')
    @winrt_commethod(6)
    def get_LayoutBoundsVisualPixels(self) -> win32more.Windows.UI.Text.Core.CoreTextLayoutBounds: ...
    LayoutBoundsVisualPixels = property(get_LayoutBoundsVisualPixels, None)
class ICoreTextLayoutRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextLayoutRequestedEventArgs'
    _iid_ = Guid('{b1dc6ae0-9a7b-4e9e-a566-4a6b5f8ad676}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.Text.Core.CoreTextLayoutRequest: ...
    Request = property(get_Request, None)
class ICoreTextSelectionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextSelectionRequest'
    _iid_ = Guid('{f0a70403-208b-4301-883c-74ca7485fd8d}')
    @winrt_commethod(6)
    def get_Selection(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(7)
    def put_Selection(self, value: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_commethod(8)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    Selection = property(get_Selection, put_Selection)
class ICoreTextSelectionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextSelectionRequestedEventArgs'
    _iid_ = Guid('{13c6682b-f614-421a-8f4b-9ec8a5a37fcd}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.Text.Core.CoreTextSelectionRequest: ...
    Request = property(get_Request, None)
class ICoreTextSelectionUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextSelectionUpdatingEventArgs'
    _iid_ = Guid('{d445839f-fe7f-4bd5-8a26-0922c1b3e639}')
    @winrt_commethod(6)
    def get_Selection(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(7)
    def get_Result(self) -> win32more.Windows.UI.Text.Core.CoreTextSelectionUpdatingResult: ...
    @winrt_commethod(8)
    def put_Result(self, value: win32more.Windows.UI.Text.Core.CoreTextSelectionUpdatingResult) -> Void: ...
    @winrt_commethod(9)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    Result = property(get_Result, put_Result)
    Selection = property(get_Selection, None)
class ICoreTextServicesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextServicesManager'
    _iid_ = Guid('{c2507d83-6e0a-4a8a-bdf8-1948874854ba}')
    @winrt_commethod(6)
    def get_InputLanguage(self) -> win32more.Windows.Globalization.Language: ...
    @winrt_commethod(7)
    def add_InputLanguageChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextServicesManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_InputLanguageChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def CreateEditContext(self) -> win32more.Windows.UI.Text.Core.CoreTextEditContext: ...
    InputLanguage = property(get_InputLanguage, None)
    InputLanguageChanged = event()
class ICoreTextServicesManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextServicesManagerStatics'
    _iid_ = Guid('{1520a388-e2cf-4d65-aeb9-b32d86fe39b9}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Text.Core.CoreTextServicesManager: ...
class ICoreTextServicesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextServicesStatics'
    _iid_ = Guid('{91859a46-eccf-47a4-8ae7-098a9c6fbb15}')
    @winrt_commethod(6)
    def get_HiddenCharacter(self) -> Char: ...
    HiddenCharacter = property(get_HiddenCharacter, None)
class ICoreTextTextRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextTextRequest'
    _iid_ = Guid('{50d950a9-f51e-4cc1-8ca1-e6346d1a61be}')
    @winrt_commethod(6)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsCanceled = property(get_IsCanceled, None)
    Range = property(get_Range, None)
    Text = property(get_Text, put_Text)
class ICoreTextTextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextTextRequestedEventArgs'
    _iid_ = Guid('{f096a2d0-41c6-4c02-8b1a-d953b00cabb3}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.Text.Core.CoreTextTextRequest: ...
    Request = property(get_Request, None)
class ICoreTextTextUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextTextUpdatingEventArgs'
    _iid_ = Guid('{eea7918d-cc2b-4f03-8ff6-02fd217db450}')
    @winrt_commethod(6)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NewSelection(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(9)
    def get_InputLanguage(self) -> win32more.Windows.Globalization.Language: ...
    @winrt_commethod(10)
    def get_Result(self) -> win32more.Windows.UI.Text.Core.CoreTextTextUpdatingResult: ...
    @winrt_commethod(11)
    def put_Result(self, value: win32more.Windows.UI.Text.Core.CoreTextTextUpdatingResult) -> Void: ...
    @winrt_commethod(12)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    InputLanguage = property(get_InputLanguage, None)
    IsCanceled = property(get_IsCanceled, None)
    NewSelection = property(get_NewSelection, None)
    Range = property(get_Range, None)
    Result = property(get_Result, put_Result)
    Text = property(get_Text, None)


make_ready(__name__)
