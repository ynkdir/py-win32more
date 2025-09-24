from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input.Preview.Text
import win32more.Windows.UI.Text
import win32more.Windows.UI.Text.Core
class ConversionModeChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.IConversionModeChangedEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.ConversionModeChangedEventArgs'
    @winrt_mixinmethod
    def get_NewConversionMode(self: win32more.Windows.UI.Input.Preview.Text.IConversionModeChangedEventArgs) -> win32more.Windows.UI.Input.Preview.Text.TextConversionMode: ...
    NewConversionMode = property(get_NewConversionMode, None)
class FocusEnteredEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.IFocusEnteredEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.FocusEnteredEventArgs'
    @winrt_mixinmethod
    def get_FocusedTextBoxInfo(self: win32more.Windows.UI.Input.Preview.Text.IFocusEnteredEventArgs) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    FocusedTextBoxInfo = property(get_FocusedTextBoxInfo, None)
class IConversionModeChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.IConversionModeChangedEventArgs'
    _iid_ = Guid('{b49761f9-5b21-513c-b6c0-78f27d26b010}')
    @winrt_commethod(6)
    def get_NewConversionMode(self) -> win32more.Windows.UI.Input.Preview.Text.TextConversionMode: ...
    NewConversionMode = property(get_NewConversionMode, None)
class IFocusEnteredEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.IFocusEnteredEventArgs'
    _iid_ = Guid('{ca4dc200-875f-501d-af14-413a0aa1ed5f}')
    @winrt_commethod(6)
    def get_FocusedTextBoxInfo(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    FocusedTextBoxInfo = property(get_FocusedTextBoxInfo, None)
class IInputDelegationModeChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.IInputDelegationModeChangedEventArgs'
    _iid_ = Guid('{4bb448b2-67ba-5215-8783-b444bd28eed3}')
    @winrt_commethod(6)
    def get_DelegationOn(self) -> Boolean: ...
    DelegationOn = property(get_DelegationOn, None)
class IKeyEventReceivedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs'
    _iid_ = Guid('{0c30f686-a058-5ecc-abd2-9cc861c1185b}')
    @winrt_commethod(6)
    def get_VirtualKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(7)
    def get_KeyStatus(self) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(8)
    def get_Unicode(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Source(self) -> win32more.Windows.UI.Input.Preview.Text.KeyEventDeviceType: ...
    @winrt_commethod(10)
    def IsKeyPressed(self, vkey: win32more.Windows.System.VirtualKey) -> Boolean: ...
    @winrt_commethod(11)
    def IsToggleKeyOn(self, vkey: win32more.Windows.System.VirtualKey) -> Boolean: ...
    @winrt_commethod(12)
    def get_EditSession(self) -> win32more.Windows.UI.Input.Preview.Text.TextEditSession: ...
    @winrt_commethod(13)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_Handled(self, value: Boolean) -> Void: ...
    EditSession = property(get_EditSession, None)
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
    Source = property(get_Source, None)
    Unicode = property(get_Unicode, None)
    VirtualKey = property(get_VirtualKey, None)
class IKeyboardInputProcessor(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.IKeyboardInputProcessor'
    _iid_ = Guid('{2afe79b6-5818-50e0-8fa8-81bc96428c46}')
    @winrt_commethod(6)
    def get_InputProfile(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HasFocusedTextBox(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_FocusedTextBoxId(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_commethod(10)
    def get_FocusedTextBoxInfo(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    @winrt_commethod(11)
    def get_FocusedTextBoxBounds(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(12)
    def get_SelectionBounds(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(13)
    def get_ConversionMode(self) -> win32more.Windows.UI.Input.Preview.Text.TextConversionMode: ...
    @winrt_commethod(14)
    def put_ConversionMode(self, value: win32more.Windows.UI.Input.Preview.Text.TextConversionMode) -> Void: ...
    @winrt_commethod(15)
    def CreateEditSession(self) -> win32more.Windows.UI.Input.Preview.Text.TextEditSession: ...
    @winrt_commethod(16)
    def add_Activated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_Deactivated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_Deactivated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_KeyEventReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.KeyEventReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_KeyEventReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_FocusEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.FocusEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_FocusEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_FocusRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_FocusRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_ConversionModeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.ConversionModeChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_ConversionModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_TextBoxInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.TextBoxInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_TextBoxInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_TextBoxContentChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.TextBoxContentChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_TextBoxContentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_CompositionTerminated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_CompositionTerminated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_ReconversionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.ReconversionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_ReconversionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ConversionMode = property(get_ConversionMode, put_ConversionMode)
    FocusedTextBoxBounds = property(get_FocusedTextBoxBounds, None)
    FocusedTextBoxId = property(get_FocusedTextBoxId, None)
    FocusedTextBoxInfo = property(get_FocusedTextBoxInfo, None)
    HasFocusedTextBox = property(get_HasFocusedTextBox, None)
    InputProfile = property(get_InputProfile, None)
    IsActive = property(get_IsActive, None)
    SelectionBounds = property(get_SelectionBounds, None)
    Activated = event()
    Deactivated = event()
    KeyEventReceived = event()
    FocusEntered = event()
    FocusRemoved = event()
    ConversionModeChanged = event()
    TextBoxInfoChanged = event()
    TextBoxContentChanged = event()
    CompositionTerminated = event()
    ReconversionRequested = event()
class IReconversionRequestedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.IReconversionRequestedEventArgs'
    _iid_ = Guid('{73852244-d202-55fe-9edf-beb7ec19f937}')
    @winrt_commethod(6)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    Range = property(get_Range, None)
class ITextBoxContentChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextBoxContentChangedEventArgs'
    _iid_ = Guid('{2cb70a41-5aed-58c5-b4c1-8ee4e1492f9e}')
    @winrt_commethod(6)
    def get_TextBoxId(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_commethod(7)
    def get_Source(self) -> win32more.Windows.UI.Input.Preview.Text.TextChangeSource: ...
    @winrt_commethod(8)
    def get_SelectionBounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def IsContentAttributeChanged(self, value: win32more.Windows.UI.Input.Preview.Text.TextBoxContentAttribute) -> Boolean: ...
    SelectionBounds = property(get_SelectionBounds, None)
    Source = property(get_Source, None)
    TextBoxId = property(get_TextBoxId, None)
class ITextBoxInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextBoxInfo'
    _iid_ = Guid('{b122443d-e8f7-5f8b-813d-aaa0941d5fa0}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_commethod(7)
    def get_InputScope(self) -> win32more.Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_commethod(8)
    def get_AppName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Url(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Settings(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxSettings: ...
    @winrt_commethod(11)
    def get_DisabledFeatures(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxFeatures: ...
    AppName = property(get_AppName, None)
    DisabledFeatures = property(get_DisabledFeatures, None)
    Id = property(get_Id, None)
    InputScope = property(get_InputScope, None)
    Settings = property(get_Settings, None)
    Url = property(get_Url, None)
class ITextBoxInfoChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextBoxInfoChangedEventArgs'
    _iid_ = Guid('{ac1275af-648c-5bac-b29f-d1ea17e9e6d6}')
    @winrt_commethod(6)
    def get_TextBoxInfo(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    TextBoxInfo = property(get_TextBoxInfo, None)
class ITextComposition(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextComposition'
    _iid_ = Guid('{5cea9aea-524d-50a4-b08a-c83d8d25ec6e}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FirstSegment(self) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_commethod(8)
    def get_SelectedSegment(self) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_commethod(9)
    def get_CaretPosition(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_CaretPosition(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def InsertText(self, text: WinRT_String) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_commethod(12)
    def Complete(self) -> Void: ...
    @winrt_commethod(13)
    def CompleteUnconverted(self) -> Void: ...
    @winrt_commethod(14)
    def CompleteFirstSegment(self) -> Void: ...
    CaretPosition = property(get_CaretPosition, put_CaretPosition)
    FirstSegment = property(get_FirstSegment, None)
    SelectedSegment = property(get_SelectedSegment, None)
    Text = property(get_Text, None)
class ITextCompositionSegment(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextCompositionSegment'
    _iid_ = Guid('{0543f6c6-eb98-56d6-8808-2eca6d02f6a5}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ConvertedText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ConvertedText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_UnconvertedText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_UnconvertedText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Range(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(13)
    def get_ConversionState(self) -> win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingReason: ...
    @winrt_commethod(14)
    def put_ConversionState(self, value: win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingReason) -> Void: ...
    @winrt_commethod(15)
    def get_Next(self) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_commethod(16)
    def get_Previous(self) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_commethod(17)
    def GetTextStyle(self) -> win32more.Windows.UI.Input.Preview.Text.TextStyle: ...
    @winrt_commethod(18)
    def SetTextStyle(self, value: win32more.Windows.UI.Input.Preview.Text.TextStyle) -> Void: ...
    ConversionState = property(get_ConversionState, put_ConversionState)
    ConvertedText = property(get_ConvertedText, put_ConvertedText)
    Next = property(get_Next, None)
    Previous = property(get_Previous, None)
    Range = property(get_Range, None)
    Text = property(get_Text, put_Text)
    UnconvertedText = property(get_UnconvertedText, put_UnconvertedText)
class ITextEditSession(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextEditSession'
    _iid_ = Guid('{0bcad18a-d31b-5787-aff9-995ee743aea8}')
    @winrt_commethod(6)
    def get_TextBoxId(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_commethod(7)
    def get_TextLength(self) -> Int32: ...
    @winrt_commethod(8)
    def get_PopulatedRange(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(9)
    def PopulateAsync(self, range: win32more.Windows.UI.Text.Core.CoreTextRange) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def GetText(self, range: win32more.Windows.UI.Text.Core.CoreTextRange) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetSelectedRange(self) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(12)
    def SetSelectedRange(self, value: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_commethod(13)
    def ReplaceText(self, replaceRange: win32more.Windows.UI.Text.Core.CoreTextRange, text: WinRT_String) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_commethod(14)
    def get_Composition(self) -> win32more.Windows.UI.Input.Preview.Text.TextComposition: ...
    @winrt_commethod(15)
    def StartComposition(self) -> win32more.Windows.UI.Input.Preview.Text.TextComposition: ...
    @winrt_commethod(16)
    def StartReconversion(self, range: win32more.Windows.UI.Text.Core.CoreTextRange) -> win32more.Windows.UI.Input.Preview.Text.TextComposition: ...
    @winrt_commethod(17)
    def SubmitPayload(self) -> Boolean: ...
    @winrt_commethod(18)
    def SubmitPayloadAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Input.Preview.Text.PayloadResult]: ...
    Composition = property(get_Composition, None)
    PopulatedRange = property(get_PopulatedRange, None)
    TextBoxId = property(get_TextBoxId, None)
    TextLength = property(get_TextLength, None)
class ITextInputProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextInputProvider'
    _iid_ = Guid('{b0885fb7-e9f8-5849-b0ef-f8155ecf60d1}')
    @winrt_commethod(6)
    def GetSubscription(self) -> win32more.Windows.UI.Input.Preview.Text.TextInputServiceSubscription: ...
    @winrt_commethod(7)
    def SetSubscription(self, subscription: win32more.Windows.UI.Input.Preview.Text.TextInputServiceSubscription) -> Void: ...
    @winrt_commethod(8)
    def get_HasFocusedTextBox(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_FocusedTextBoxId(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_commethod(10)
    def get_FocusedTextBoxInfo(self) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    @winrt_commethod(11)
    def get_FocusedTextBoxBounds(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(12)
    def get_SelectionBounds(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(13)
    def CreateEditSession(self) -> win32more.Windows.UI.Input.Preview.Text.TextEditSession: ...
    @winrt_commethod(14)
    def TryStartDelegation(self) -> Boolean: ...
    @winrt_commethod(15)
    def StopDelegation(self) -> Void: ...
    @winrt_commethod(16)
    def add_FocusEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.FocusEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_FocusEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_FocusRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_FocusRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_TextBoxInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.TextBoxInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_TextBoxInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_TextBoxContentChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.TextBoxContentChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_TextBoxContentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_CompositionTerminated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_CompositionTerminated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_ReconversionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.ReconversionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_ReconversionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_InputDelegationModeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.InputDelegationModeChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_InputDelegationModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    FocusedTextBoxBounds = property(get_FocusedTextBoxBounds, None)
    FocusedTextBoxId = property(get_FocusedTextBoxId, None)
    FocusedTextBoxInfo = property(get_FocusedTextBoxInfo, None)
    HasFocusedTextBox = property(get_HasFocusedTextBox, None)
    SelectionBounds = property(get_SelectionBounds, None)
    FocusEntered = event()
    FocusRemoved = event()
    TextBoxInfoChanged = event()
    TextBoxContentChanged = event()
    CompositionTerminated = event()
    ReconversionRequested = event()
    InputDelegationModeChanged = event()
class ITextInputService(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextInputService'
    _iid_ = Guid('{8e23f89c-ab1f-551a-8751-7d4f29e34d88}')
    @winrt_commethod(6)
    def CreateKeyboardInputProcessor(self, inputProfile: WinRT_String) -> win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor: ...
    @winrt_commethod(7)
    def CreateTextInputProvider(self, inputProfile: WinRT_String) -> win32more.Windows.UI.Input.Preview.Text.TextInputProvider: ...
class ITextInputServiceStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Text.ITextInputServiceStatics'
    _iid_ = Guid('{91b68f5e-02ed-4e09-ae89-dfd735cf10bc}')
    @winrt_commethod(6)
    def GetForCurrentThread(self) -> win32more.Windows.UI.Input.Preview.Text.TextInputService: ...
class InputDelegationModeChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.IInputDelegationModeChangedEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.InputDelegationModeChangedEventArgs'
    @winrt_mixinmethod
    def get_DelegationOn(self: win32more.Windows.UI.Input.Preview.Text.IInputDelegationModeChangedEventArgs) -> Boolean: ...
    DelegationOn = property(get_DelegationOn, None)
class KeyEventDeviceType(Enum, Int32):
    Undefined = 0
    HardwareKeyboard = 1
    SoftwareKeyboard = 2
    Gamepad = 3
    Injection = 4
class KeyEventReceivedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.KeyEventReceivedEventArgs'
    @winrt_mixinmethod
    def get_VirtualKey(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Unicode(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs) -> win32more.Windows.UI.Input.Preview.Text.KeyEventDeviceType: ...
    @winrt_mixinmethod
    def IsKeyPressed(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs, vkey: win32more.Windows.System.VirtualKey) -> Boolean: ...
    @winrt_mixinmethod
    def IsToggleKeyOn(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs, vkey: win32more.Windows.System.VirtualKey) -> Boolean: ...
    @winrt_mixinmethod
    def get_EditSession(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs) -> win32more.Windows.UI.Input.Preview.Text.TextEditSession: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Input.Preview.Text.IKeyEventReceivedEventArgs, value: Boolean) -> Void: ...
    EditSession = property(get_EditSession, None)
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
    Source = property(get_Source, None)
    Unicode = property(get_Unicode, None)
    VirtualKey = property(get_VirtualKey, None)
class KeyboardInputProcessor(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor
    _classid_ = 'Windows.UI.Input.Preview.Text.KeyboardInputProcessor'
    @winrt_mixinmethod
    def get_InputProfile(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasFocusedTextBox(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> Boolean: ...
    @winrt_mixinmethod
    def get_FocusedTextBoxId(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_mixinmethod
    def get_FocusedTextBoxInfo(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    @winrt_mixinmethod
    def get_FocusedTextBoxBounds(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def get_SelectionBounds(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def get_ConversionMode(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> win32more.Windows.UI.Input.Preview.Text.TextConversionMode: ...
    @winrt_mixinmethod
    def put_ConversionMode(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, value: win32more.Windows.UI.Input.Preview.Text.TextConversionMode) -> Void: ...
    @winrt_mixinmethod
    def CreateEditSession(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor) -> win32more.Windows.UI.Input.Preview.Text.TextEditSession: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Deactivated(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Deactivated(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyEventReceived(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.KeyEventReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyEventReceived(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FocusEntered(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.FocusEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusEntered(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FocusRemoved(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusRemoved(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConversionModeChanged(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.ConversionModeChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConversionModeChanged(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TextBoxInfoChanged(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.TextBoxInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextBoxInfoChanged(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TextBoxContentChanged(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.TextBoxContentChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextBoxContentChanged(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CompositionTerminated(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CompositionTerminated(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReconversionRequested(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor, win32more.Windows.UI.Input.Preview.Text.ReconversionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReconversionRequested(self: win32more.Windows.UI.Input.Preview.Text.IKeyboardInputProcessor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ConversionMode = property(get_ConversionMode, put_ConversionMode)
    FocusedTextBoxBounds = property(get_FocusedTextBoxBounds, None)
    FocusedTextBoxId = property(get_FocusedTextBoxId, None)
    FocusedTextBoxInfo = property(get_FocusedTextBoxInfo, None)
    HasFocusedTextBox = property(get_HasFocusedTextBox, None)
    InputProfile = property(get_InputProfile, None)
    IsActive = property(get_IsActive, None)
    SelectionBounds = property(get_SelectionBounds, None)
    Activated = event()
    Deactivated = event()
    KeyEventReceived = event()
    FocusEntered = event()
    FocusRemoved = event()
    ConversionModeChanged = event()
    TextBoxInfoChanged = event()
    TextBoxContentChanged = event()
    CompositionTerminated = event()
    ReconversionRequested = event()
class PayloadResult(Enum, Int32):
    InEditing = 0
    Pending = 1
    Completed = 2
    Overridden = 3
    Outrun = 4
    Rejected = 5
    Canceled = 6
PreviewTextContract: UInt32 = 65536
class ReconversionRequestedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.IReconversionRequestedEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.ReconversionRequestedEventArgs'
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Input.Preview.Text.IReconversionRequestedEventArgs) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    Range = property(get_Range, None)
class TextBoxContentAttribute(Enum, Int32):
    None_ = 0
    Selection = 1
    Text = 2
    Property = 3
    Layout = 4
class TextBoxContentChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextBoxContentChangedEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.TextBoxContentChangedEventArgs'
    @winrt_mixinmethod
    def get_TextBoxId(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxContentChangedEventArgs) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxContentChangedEventArgs) -> win32more.Windows.UI.Input.Preview.Text.TextChangeSource: ...
    @winrt_mixinmethod
    def get_SelectionBounds(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxContentChangedEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def IsContentAttributeChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxContentChangedEventArgs, value: win32more.Windows.UI.Input.Preview.Text.TextBoxContentAttribute) -> Boolean: ...
    SelectionBounds = property(get_SelectionBounds, None)
    Source = property(get_Source, None)
    TextBoxId = property(get_TextBoxId, None)
class TextBoxFeatures(Enum, UInt32):
    None_ = 0
    ReadText = 1
    WriteText = 2
    AugmentText = 4
class TextBoxId(Structure):
    Value: UInt32
class TextBoxInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo
    _classid_ = 'Windows.UI.Input.Preview.Text.TextBoxInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_mixinmethod
    def get_InputScope(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo) -> win32more.Windows.UI.Text.Core.CoreTextInputScope: ...
    @winrt_mixinmethod
    def get_AppName(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Url(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Settings(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo) -> win32more.Windows.UI.Input.Preview.Text.TextBoxSettings: ...
    @winrt_mixinmethod
    def get_DisabledFeatures(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfo) -> win32more.Windows.UI.Input.Preview.Text.TextBoxFeatures: ...
    AppName = property(get_AppName, None)
    DisabledFeatures = property(get_DisabledFeatures, None)
    Id = property(get_Id, None)
    InputScope = property(get_InputScope, None)
    Settings = property(get_Settings, None)
    Url = property(get_Url, None)
class TextBoxInfoChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfoChangedEventArgs
    _classid_ = 'Windows.UI.Input.Preview.Text.TextBoxInfoChangedEventArgs'
    @winrt_mixinmethod
    def get_TextBoxInfo(self: win32more.Windows.UI.Input.Preview.Text.ITextBoxInfoChangedEventArgs) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    TextBoxInfo = property(get_TextBoxInfo, None)
class TextBoxSettings(Enum, UInt32):
    None_ = 0
    Private = 1
    Multiline = 2
    VerticalWriting = 4
class TextChangeSource(Enum, Int32):
    External = 0
    HardwareKeyTyped = 1
    SoftwareKeyTyped = 2
    KeyboardImeInsertion = 3
    OtherImeInsertion = 4
    Reconversion = 5
    AutoCompletion = 6
    Mixed = 7
class TextComposition(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextComposition
    _classid_ = 'Windows.UI.Input.Preview.Text.TextComposition'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirstSegment(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_mixinmethod
    def get_SelectedSegment(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_mixinmethod
    def get_CaretPosition(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> UInt32: ...
    @winrt_mixinmethod
    def put_CaretPosition(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def InsertText(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition, text: WinRT_String) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> Void: ...
    @winrt_mixinmethod
    def CompleteUnconverted(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> Void: ...
    @winrt_mixinmethod
    def CompleteFirstSegment(self: win32more.Windows.UI.Input.Preview.Text.ITextComposition) -> Void: ...
    CaretPosition = property(get_CaretPosition, put_CaretPosition)
    FirstSegment = property(get_FirstSegment, None)
    SelectedSegment = property(get_SelectedSegment, None)
    Text = property(get_Text, None)
class TextCompositionSegment(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment
    _classid_ = 'Windows.UI.Input.Preview.Text.TextCompositionSegment'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ConvertedText(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ConvertedText(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UnconvertedText(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UnconvertedText(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Range(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_ConversionState(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingReason: ...
    @winrt_mixinmethod
    def put_ConversionState(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment, value: win32more.Windows.UI.Text.Core.CoreTextFormatUpdatingReason) -> Void: ...
    @winrt_mixinmethod
    def get_Next(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_mixinmethod
    def get_Previous(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> win32more.Windows.UI.Input.Preview.Text.TextCompositionSegment: ...
    @winrt_mixinmethod
    def GetTextStyle(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment) -> win32more.Windows.UI.Input.Preview.Text.TextStyle: ...
    @winrt_mixinmethod
    def SetTextStyle(self: win32more.Windows.UI.Input.Preview.Text.ITextCompositionSegment, value: win32more.Windows.UI.Input.Preview.Text.TextStyle) -> Void: ...
    ConversionState = property(get_ConversionState, put_ConversionState)
    ConvertedText = property(get_ConvertedText, put_ConvertedText)
    Next = property(get_Next, None)
    Previous = property(get_Previous, None)
    Range = property(get_Range, None)
    Text = property(get_Text, put_Text)
    UnconvertedText = property(get_UnconvertedText, put_UnconvertedText)
class TextConversionMode(Enum, Int32):
    Undefined = 0
    AlphanumericHalfWidth = 1
    AlphanumericFullWidth = 2
    NativeHalfWidth = 3
    NativeFullWidth = 4
    KatakanaHalfWidth = 5
    KatakanaFullWidth = 6
    NativeHalfWidthNativeSymbol = 7
    NativeFullWidthNativeSymbol = 8
    NoConversion = 9
    RequestConversion = 10
    NativeEudc = 11
class TextEditSession(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextEditSession
    _classid_ = 'Windows.UI.Input.Preview.Text.TextEditSession'
    @winrt_mixinmethod
    def get_TextBoxId(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_mixinmethod
    def get_TextLength(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> Int32: ...
    @winrt_mixinmethod
    def get_PopulatedRange(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def PopulateAsync(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession, range: win32more.Windows.UI.Text.Core.CoreTextRange) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetText(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession, range: win32more.Windows.UI.Text.Core.CoreTextRange) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetSelectedRange(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def SetSelectedRange(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession, value: win32more.Windows.UI.Text.Core.CoreTextRange) -> Void: ...
    @winrt_mixinmethod
    def ReplaceText(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession, replaceRange: win32more.Windows.UI.Text.Core.CoreTextRange, text: WinRT_String) -> win32more.Windows.UI.Text.Core.CoreTextRange: ...
    @winrt_mixinmethod
    def get_Composition(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> win32more.Windows.UI.Input.Preview.Text.TextComposition: ...
    @winrt_mixinmethod
    def StartComposition(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> win32more.Windows.UI.Input.Preview.Text.TextComposition: ...
    @winrt_mixinmethod
    def StartReconversion(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession, range: win32more.Windows.UI.Text.Core.CoreTextRange) -> win32more.Windows.UI.Input.Preview.Text.TextComposition: ...
    @winrt_mixinmethod
    def SubmitPayload(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> Boolean: ...
    @winrt_mixinmethod
    def SubmitPayloadAsync(self: win32more.Windows.UI.Input.Preview.Text.ITextEditSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Input.Preview.Text.PayloadResult]: ...
    Composition = property(get_Composition, None)
    PopulatedRange = property(get_PopulatedRange, None)
    TextBoxId = property(get_TextBoxId, None)
    TextLength = property(get_TextLength, None)
class TextInputProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider
    _classid_ = 'Windows.UI.Input.Preview.Text.TextInputProvider'
    @winrt_mixinmethod
    def GetSubscription(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> win32more.Windows.UI.Input.Preview.Text.TextInputServiceSubscription: ...
    @winrt_mixinmethod
    def SetSubscription(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, subscription: win32more.Windows.UI.Input.Preview.Text.TextInputServiceSubscription) -> Void: ...
    @winrt_mixinmethod
    def get_HasFocusedTextBox(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_FocusedTextBoxId(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> win32more.Windows.UI.Input.Preview.Text.TextBoxId: ...
    @winrt_mixinmethod
    def get_FocusedTextBoxInfo(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> win32more.Windows.UI.Input.Preview.Text.TextBoxInfo: ...
    @winrt_mixinmethod
    def get_FocusedTextBoxBounds(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def get_SelectionBounds(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def CreateEditSession(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> win32more.Windows.UI.Input.Preview.Text.TextEditSession: ...
    @winrt_mixinmethod
    def TryStartDelegation(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> Boolean: ...
    @winrt_mixinmethod
    def StopDelegation(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider) -> Void: ...
    @winrt_mixinmethod
    def add_FocusEntered(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.FocusEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusEntered(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FocusRemoved(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusRemoved(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TextBoxInfoChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.TextBoxInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextBoxInfoChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TextBoxContentChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.TextBoxContentChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextBoxContentChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CompositionTerminated(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CompositionTerminated(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReconversionRequested(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.ReconversionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReconversionRequested(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_InputDelegationModeChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Preview.Text.TextInputProvider, win32more.Windows.UI.Input.Preview.Text.InputDelegationModeChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputDelegationModeChanged(self: win32more.Windows.UI.Input.Preview.Text.ITextInputProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    FocusedTextBoxBounds = property(get_FocusedTextBoxBounds, None)
    FocusedTextBoxId = property(get_FocusedTextBoxId, None)
    FocusedTextBoxInfo = property(get_FocusedTextBoxInfo, None)
    HasFocusedTextBox = property(get_HasFocusedTextBox, None)
    SelectionBounds = property(get_SelectionBounds, None)
    FocusEntered = event()
    FocusRemoved = event()
    TextBoxInfoChanged = event()
    TextBoxContentChanged = event()
    CompositionTerminated = event()
    ReconversionRequested = event()
    InputDelegationModeChanged = event()
class TextInputService(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Text.ITextInputService
    _classid_ = 'Windows.UI.Input.Preview.Text.TextInputService'
    @winrt_mixinmethod
    def CreateKeyboardInputProcessor(self: win32more.Windows.UI.Input.Preview.Text.ITextInputService, inputProfile: WinRT_String) -> win32more.Windows.UI.Input.Preview.Text.KeyboardInputProcessor: ...
    @winrt_mixinmethod
    def CreateTextInputProvider(self: win32more.Windows.UI.Input.Preview.Text.ITextInputService, inputProfile: WinRT_String) -> win32more.Windows.UI.Input.Preview.Text.TextInputProvider: ...
    @winrt_classmethod
    def GetForCurrentThread(cls: win32more.Windows.UI.Input.Preview.Text.ITextInputServiceStatics) -> win32more.Windows.UI.Input.Preview.Text.TextInputService: ...
class TextInputServiceSubscription(Structure):
    requiredEnabledFeatures: win32more.Windows.UI.Input.Preview.Text.TextBoxFeatures
    requiredDisabledFeatures: win32more.Windows.UI.Input.Preview.Text.TextBoxFeatures
class TextStyle(Structure):
    mask: win32more.Windows.UI.Input.Preview.Text.TextStyleAttributes
    textColor: win32more.Windows.UI.Color
    backgroundColor: win32more.Windows.UI.Color
    underlineColor: win32more.Windows.UI.Color
    underlineType: win32more.Windows.UI.Text.UnderlineType
class TextStyleAttributes(Enum, UInt32):
    None_ = 0
    TextColor = 1
    BackgroundColor = 2
    UnderlineColor = 4
    UnderlineType = 8


make_ready(__name__)
