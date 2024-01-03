from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.UI.Text
import win32more.Windows.UI.Text.Core
import win32more.Windows.UI.ViewManagement
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
    IsCanceled = property(get_IsCanceled, None)
    CompositionSegments = property(get_CompositionSegments, None)
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
    Name = property(get_Name, put_Name)
    InputScope = property(get_InputScope, put_InputScope)
    IsReadOnly = property(get_IsReadOnly, put_IsReadOnly)
    InputPaneDisplayPolicy = property(get_InputPaneDisplayPolicy, put_InputPaneDisplayPolicy)
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
    Range = property(get_Range, None)
    TextColor = property(get_TextColor, None)
    BackgroundColor = property(get_BackgroundColor, None)
    UnderlineColor = property(get_UnderlineColor, None)
    UnderlineType = property(get_UnderlineType, None)
    Reason = property(get_Reason, None)
    Result = property(get_Result, put_Result)
    IsCanceled = property(get_IsCanceled, None)
CoreTextFormatUpdatingReason = Int32
CoreTextFormatUpdatingReason_None: CoreTextFormatUpdatingReason = 0
CoreTextFormatUpdatingReason_CompositionUnconverted: CoreTextFormatUpdatingReason = 1
CoreTextFormatUpdatingReason_CompositionConverted: CoreTextFormatUpdatingReason = 2
CoreTextFormatUpdatingReason_CompositionTargetUnconverted: CoreTextFormatUpdatingReason = 3
CoreTextFormatUpdatingReason_CompositionTargetConverted: CoreTextFormatUpdatingReason = 4
CoreTextFormatUpdatingResult = Int32
CoreTextFormatUpdatingResult_Succeeded: CoreTextFormatUpdatingResult = 0
CoreTextFormatUpdatingResult_Failed: CoreTextFormatUpdatingResult = 1
CoreTextInputPaneDisplayPolicy = Int32
CoreTextInputPaneDisplayPolicy_Automatic: CoreTextInputPaneDisplayPolicy = 0
CoreTextInputPaneDisplayPolicy_Manual: CoreTextInputPaneDisplayPolicy = 1
CoreTextInputScope = Int32
CoreTextInputScope_Default: CoreTextInputScope = 0
CoreTextInputScope_Url: CoreTextInputScope = 1
CoreTextInputScope_FilePath: CoreTextInputScope = 2
CoreTextInputScope_FileName: CoreTextInputScope = 3
CoreTextInputScope_EmailUserName: CoreTextInputScope = 4
CoreTextInputScope_EmailAddress: CoreTextInputScope = 5
CoreTextInputScope_UserName: CoreTextInputScope = 6
CoreTextInputScope_PersonalFullName: CoreTextInputScope = 7
CoreTextInputScope_PersonalNamePrefix: CoreTextInputScope = 8
CoreTextInputScope_PersonalGivenName: CoreTextInputScope = 9
CoreTextInputScope_PersonalMiddleName: CoreTextInputScope = 10
CoreTextInputScope_PersonalSurname: CoreTextInputScope = 11
CoreTextInputScope_PersonalNameSuffix: CoreTextInputScope = 12
CoreTextInputScope_Address: CoreTextInputScope = 13
CoreTextInputScope_AddressPostalCode: CoreTextInputScope = 14
CoreTextInputScope_AddressStreet: CoreTextInputScope = 15
CoreTextInputScope_AddressStateOrProvince: CoreTextInputScope = 16
CoreTextInputScope_AddressCity: CoreTextInputScope = 17
CoreTextInputScope_AddressCountryName: CoreTextInputScope = 18
CoreTextInputScope_AddressCountryShortName: CoreTextInputScope = 19
CoreTextInputScope_CurrencyAmountAndSymbol: CoreTextInputScope = 20
CoreTextInputScope_CurrencyAmount: CoreTextInputScope = 21
CoreTextInputScope_Date: CoreTextInputScope = 22
CoreTextInputScope_DateMonth: CoreTextInputScope = 23
CoreTextInputScope_DateDay: CoreTextInputScope = 24
CoreTextInputScope_DateYear: CoreTextInputScope = 25
CoreTextInputScope_DateMonthName: CoreTextInputScope = 26
CoreTextInputScope_DateDayName: CoreTextInputScope = 27
CoreTextInputScope_Number: CoreTextInputScope = 29
CoreTextInputScope_SingleCharacter: CoreTextInputScope = 30
CoreTextInputScope_Password: CoreTextInputScope = 31
CoreTextInputScope_TelephoneNumber: CoreTextInputScope = 32
CoreTextInputScope_TelephoneCountryCode: CoreTextInputScope = 33
CoreTextInputScope_TelephoneAreaCode: CoreTextInputScope = 34
CoreTextInputScope_TelephoneLocalNumber: CoreTextInputScope = 35
CoreTextInputScope_Time: CoreTextInputScope = 36
CoreTextInputScope_TimeHour: CoreTextInputScope = 37
CoreTextInputScope_TimeMinuteOrSecond: CoreTextInputScope = 38
CoreTextInputScope_NumberFullWidth: CoreTextInputScope = 39
CoreTextInputScope_AlphanumericHalfWidth: CoreTextInputScope = 40
CoreTextInputScope_AlphanumericFullWidth: CoreTextInputScope = 41
CoreTextInputScope_CurrencyChinese: CoreTextInputScope = 42
CoreTextInputScope_Bopomofo: CoreTextInputScope = 43
CoreTextInputScope_Hiragana: CoreTextInputScope = 44
CoreTextInputScope_KatakanaHalfWidth: CoreTextInputScope = 45
CoreTextInputScope_KatakanaFullWidth: CoreTextInputScope = 46
CoreTextInputScope_Hanja: CoreTextInputScope = 47
CoreTextInputScope_HangulHalfWidth: CoreTextInputScope = 48
CoreTextInputScope_HangulFullWidth: CoreTextInputScope = 49
CoreTextInputScope_Search: CoreTextInputScope = 50
CoreTextInputScope_Formula: CoreTextInputScope = 51
CoreTextInputScope_SearchIncremental: CoreTextInputScope = 52
CoreTextInputScope_ChineseHalfWidth: CoreTextInputScope = 53
CoreTextInputScope_ChineseFullWidth: CoreTextInputScope = 54
CoreTextInputScope_NativeScript: CoreTextInputScope = 55
CoreTextInputScope_Text: CoreTextInputScope = 57
CoreTextInputScope_Chat: CoreTextInputScope = 58
CoreTextInputScope_NameOrPhoneNumber: CoreTextInputScope = 59
CoreTextInputScope_EmailUserNameOrAddress: CoreTextInputScope = 60
CoreTextInputScope_Private: CoreTextInputScope = 61
CoreTextInputScope_Maps: CoreTextInputScope = 62
CoreTextInputScope_PasswordNumeric: CoreTextInputScope = 63
CoreTextInputScope_FormulaNumber: CoreTextInputScope = 67
CoreTextInputScope_ChatWithoutEmoji: CoreTextInputScope = 68
CoreTextInputScope_Digits: CoreTextInputScope = 28
CoreTextInputScope_PinNumeric: CoreTextInputScope = 64
CoreTextInputScope_PinAlphanumeric: CoreTextInputScope = 65
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
    TextBounds = property(get_TextBounds, put_TextBounds)
    ControlBounds = property(get_ControlBounds, put_ControlBounds)
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
    Range = property(get_Range, None)
    LayoutBounds = property(get_LayoutBounds, None)
    IsCanceled = property(get_IsCanceled, None)
    LayoutBoundsVisualPixels = property(get_LayoutBoundsVisualPixels, None)
class CoreTextLayoutRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequestedEventArgs
    _classid_ = 'Windows.UI.Text.Core.CoreTextLayoutRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Text.Core.ICoreTextLayoutRequestedEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextLayoutRequest: ...
    Request = property(get_Request, None)
class CoreTextRange(EasyCastStructure):
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
    Selection = property(get_Selection, put_Selection)
    IsCanceled = property(get_IsCanceled, None)
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
    Selection = property(get_Selection, None)
    Result = property(get_Result, put_Result)
    IsCanceled = property(get_IsCanceled, None)
CoreTextSelectionUpdatingResult = Int32
CoreTextSelectionUpdatingResult_Succeeded: CoreTextSelectionUpdatingResult = 0
CoreTextSelectionUpdatingResult_Failed: CoreTextSelectionUpdatingResult = 1
class _CoreTextServicesConstants_Meta_(ComPtr.__class__):
    pass
class CoreTextServicesConstants(ComPtr, metaclass=_CoreTextServicesConstants_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.CoreTextServicesConstants'
    @winrt_classmethod
    def get_HiddenCharacter(cls: win32more.Windows.UI.Text.Core.ICoreTextServicesStatics) -> Char: ...
    _CoreTextServicesConstants_Meta_.HiddenCharacter = property(get_HiddenCharacter.__wrapped__, None)
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
    Range = property(get_Range, None)
    Text = property(get_Text, put_Text)
    IsCanceled = property(get_IsCanceled, None)
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
    Range = property(get_Range, None)
    Text = property(get_Text, None)
    NewSelection = property(get_NewSelection, None)
    InputLanguage = property(get_InputLanguage, None)
    Result = property(get_Result, put_Result)
    IsCanceled = property(get_IsCanceled, None)
CoreTextTextUpdatingResult = Int32
CoreTextTextUpdatingResult_Succeeded: CoreTextTextUpdatingResult = 0
CoreTextTextUpdatingResult_Failed: CoreTextTextUpdatingResult = 1
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
    IsCanceled = property(get_IsCanceled, None)
    CompositionSegments = property(get_CompositionSegments, None)
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
    Name = property(get_Name, put_Name)
    InputScope = property(get_InputScope, put_InputScope)
    IsReadOnly = property(get_IsReadOnly, put_IsReadOnly)
    InputPaneDisplayPolicy = property(get_InputPaneDisplayPolicy, put_InputPaneDisplayPolicy)
class ICoreTextEditContext2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Text.Core.ICoreTextEditContext2'
    _iid_ = Guid('{b1867dbb-083b-49e1-b281-2b35d62bf466}')
    @winrt_commethod(6)
    def add_NotifyFocusLeaveCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Text.Core.CoreTextEditContext, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NotifyFocusLeaveCompleted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    Range = property(get_Range, None)
    TextColor = property(get_TextColor, None)
    BackgroundColor = property(get_BackgroundColor, None)
    UnderlineColor = property(get_UnderlineColor, None)
    UnderlineType = property(get_UnderlineType, None)
    Reason = property(get_Reason, None)
    Result = property(get_Result, put_Result)
    IsCanceled = property(get_IsCanceled, None)
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
    TextBounds = property(get_TextBounds, put_TextBounds)
    ControlBounds = property(get_ControlBounds, put_ControlBounds)
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
    Range = property(get_Range, None)
    LayoutBounds = property(get_LayoutBounds, None)
    IsCanceled = property(get_IsCanceled, None)
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
    Selection = property(get_Selection, put_Selection)
    IsCanceled = property(get_IsCanceled, None)
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
    Selection = property(get_Selection, None)
    Result = property(get_Result, put_Result)
    IsCanceled = property(get_IsCanceled, None)
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
    Range = property(get_Range, None)
    Text = property(get_Text, put_Text)
    IsCanceled = property(get_IsCanceled, None)
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
    Range = property(get_Range, None)
    Text = property(get_Text, None)
    NewSelection = property(get_NewSelection, None)
    InputLanguage = property(get_InputLanguage, None)
    Result = property(get_Result, put_Result)
    IsCanceled = property(get_IsCanceled, None)


make_ready(__name__)
