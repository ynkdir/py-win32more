from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Calls.Background
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
CallsBackgroundContract: UInt32 = 262144
class IPhoneCallBlockedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneCallBlockedTriggerDetails'
    _iid_ = Guid('{a4a690a2-e4c1-427f-864e-e470477ddb67}')
    @winrt_commethod(6)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_CallBlockedReason(self) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneCallBlockedReason: ...
    CallBlockedReason = property(get_CallBlockedReason, None)
    LineId = property(get_LineId, None)
    PhoneNumber = property(get_PhoneNumber, None)
class IPhoneCallOriginDataRequestTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails'
    _iid_ = Guid('{6e9b5b3f-c54b-4e82-4cc9-e329a4184592}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_PhoneNumber(self) -> WinRT_String: ...
    PhoneNumber = property(get_PhoneNumber, None)
    RequestId = property(get_RequestId, None)
class IPhoneIncomingCallDismissedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails'
    _iid_ = Guid('{bad30276-83b6-5732-9c38-0c206546196a}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DismissalTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_TextReplyMessage(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneIncomingCallDismissedReason: ...
    DismissalTime = property(get_DismissalTime, None)
    DisplayName = property(get_DisplayName, None)
    LineId = property(get_LineId, None)
    PhoneNumber = property(get_PhoneNumber, None)
    Reason = property(get_Reason, None)
    TextReplyMessage = property(get_TextReplyMessage, None)
class IPhoneIncomingCallNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails'
    _iid_ = Guid('{2b0e6044-9b32-5d42-8222-d2812e39fb21}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_CallId(self) -> WinRT_String: ...
    CallId = property(get_CallId, None)
    LineId = property(get_LineId, None)
class IPhoneLineChangedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneLineChangedTriggerDetails'
    _iid_ = Guid('{c6d321e7-d11d-40d8-b2b7-e40a01d66249}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_ChangeType(self) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneLineChangeKind: ...
    @winrt_commethod(8)
    def HasLinePropertyChanged(self, lineProperty: win32more.Windows.ApplicationModel.Calls.Background.PhoneLineProperties) -> Boolean: ...
    ChangeType = property(get_ChangeType, None)
    LineId = property(get_LineId, None)
class IPhoneNewVoicemailMessageTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneNewVoicemailMessageTriggerDetails'
    _iid_ = Guid('{13a8c01b-b831-48d3-8ba9-8d22a6580dcf}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_VoicemailCount(self) -> Int32: ...
    @winrt_commethod(8)
    def get_OperatorMessage(self) -> WinRT_String: ...
    LineId = property(get_LineId, None)
    OperatorMessage = property(get_OperatorMessage, None)
    VoicemailCount = property(get_VoicemailCount, None)
class PhoneCallBlockedReason(Enum, Int32):
    InCallBlockingList = 0
    PrivateNumber = 1
    UnknownNumber = 2
class PhoneCallBlockedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallBlockedTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneCallBlockedTriggerDetails'
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallBlockedTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallBlockedTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_CallBlockedReason(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallBlockedTriggerDetails) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneCallBlockedReason: ...
    CallBlockedReason = property(get_CallBlockedReason, None)
    LineId = property(get_LineId, None)
    PhoneNumber = property(get_PhoneNumber, None)
class PhoneCallOriginDataRequestTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneCallOriginDataRequestTriggerDetails'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails) -> WinRT_String: ...
    PhoneNumber = property(get_PhoneNumber, None)
    RequestId = property(get_RequestId, None)
class PhoneIncomingCallDismissedReason(Enum, Int32):
    Unknown = 0
    CallRejected = 1
    TextReply = 2
    ConnectionLost = 3
class PhoneIncomingCallDismissedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneIncomingCallDismissedTriggerDetails'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DismissalTime(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_TextReplyMessage(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallDismissedTriggerDetails) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneIncomingCallDismissedReason: ...
    DismissalTime = property(get_DismissalTime, None)
    DisplayName = property(get_DisplayName, None)
    LineId = property(get_LineId, None)
    PhoneNumber = property(get_PhoneNumber, None)
    Reason = property(get_Reason, None)
    TextReplyMessage = property(get_TextReplyMessage, None)
class PhoneIncomingCallNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneIncomingCallNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_CallId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails) -> WinRT_String: ...
    CallId = property(get_CallId, None)
    LineId = property(get_LineId, None)
class PhoneLineChangeKind(Enum, Int32):
    Added = 0
    Removed = 1
    PropertiesChanged = 2
class PhoneLineChangedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneLineChangedTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneLineChangedTriggerDetails'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneLineChangedTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneLineChangedTriggerDetails) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneLineChangeKind: ...
    @winrt_mixinmethod
    def HasLinePropertyChanged(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneLineChangedTriggerDetails, lineProperty: win32more.Windows.ApplicationModel.Calls.Background.PhoneLineProperties) -> Boolean: ...
    ChangeType = property(get_ChangeType, None)
    LineId = property(get_LineId, None)
class PhoneLineProperties(Enum, UInt32):
    None_ = 0
    BrandingOptions = 1
    CanDial = 2
    CellularDetails = 4
    DisplayColor = 8
    DisplayName = 16
    NetworkName = 32
    NetworkState = 64
    Transport = 128
    Voicemail = 256
class PhoneNewVoicemailMessageTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneNewVoicemailMessageTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneNewVoicemailMessageTriggerDetails'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneNewVoicemailMessageTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_VoicemailCount(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneNewVoicemailMessageTriggerDetails) -> Int32: ...
    @winrt_mixinmethod
    def get_OperatorMessage(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneNewVoicemailMessageTriggerDetails) -> WinRT_String: ...
    LineId = property(get_LineId, None)
    OperatorMessage = property(get_OperatorMessage, None)
    VoicemailCount = property(get_VoicemailCount, None)
class PhoneTriggerType(Enum, Int32):
    NewVoicemailMessage = 0
    CallHistoryChanged = 1
    LineChanged = 2
    AirplaneModeDisabledForEmergencyCall = 3
    CallOriginDataRequest = 4
    CallBlocked = 5
    IncomingCallDismissed = 6
    IncomingCallNotification = 7


make_ready(__name__)
