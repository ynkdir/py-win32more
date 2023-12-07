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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Calls.Background
import win32more.Windows.Foundation
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
    PhoneNumber = property(get_PhoneNumber, None)
    LineId = property(get_LineId, None)
    CallBlockedReason = property(get_CallBlockedReason, None)
class IPhoneCallOriginDataRequestTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails'
    _iid_ = Guid('{6e9b5b3f-c54b-4e82-4cc9-e329a4184592}')
    @winrt_commethod(6)
    def get_RequestId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_PhoneNumber(self) -> WinRT_String: ...
    RequestId = property(get_RequestId, None)
    PhoneNumber = property(get_PhoneNumber, None)
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
    LineId = property(get_LineId, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DisplayName = property(get_DisplayName, None)
    DismissalTime = property(get_DismissalTime, None)
    TextReplyMessage = property(get_TextReplyMessage, None)
    Reason = property(get_Reason, None)
class IPhoneIncomingCallNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails'
    _iid_ = Guid('{2b0e6044-9b32-5d42-8222-d2812e39fb21}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_CallId(self) -> WinRT_String: ...
    LineId = property(get_LineId, None)
    CallId = property(get_CallId, None)
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
    LineId = property(get_LineId, None)
    ChangeType = property(get_ChangeType, None)
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
    VoicemailCount = property(get_VoicemailCount, None)
    OperatorMessage = property(get_OperatorMessage, None)
PhoneCallBlockedReason = Int32
PhoneCallBlockedReason_InCallBlockingList: PhoneCallBlockedReason = 0
PhoneCallBlockedReason_PrivateNumber: PhoneCallBlockedReason = 1
PhoneCallBlockedReason_UnknownNumber: PhoneCallBlockedReason = 2
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
    PhoneNumber = property(get_PhoneNumber, None)
    LineId = property(get_LineId, None)
    CallBlockedReason = property(get_CallBlockedReason, None)
class PhoneCallOriginDataRequestTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneCallOriginDataRequestTriggerDetails'
    @winrt_mixinmethod
    def get_RequestId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneCallOriginDataRequestTriggerDetails) -> WinRT_String: ...
    RequestId = property(get_RequestId, None)
    PhoneNumber = property(get_PhoneNumber, None)
PhoneIncomingCallDismissedReason = Int32
PhoneIncomingCallDismissedReason_Unknown: PhoneIncomingCallDismissedReason = 0
PhoneIncomingCallDismissedReason_CallRejected: PhoneIncomingCallDismissedReason = 1
PhoneIncomingCallDismissedReason_TextReply: PhoneIncomingCallDismissedReason = 2
PhoneIncomingCallDismissedReason_ConnectionLost: PhoneIncomingCallDismissedReason = 3
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
    LineId = property(get_LineId, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DisplayName = property(get_DisplayName, None)
    DismissalTime = property(get_DismissalTime, None)
    TextReplyMessage = property(get_TextReplyMessage, None)
    Reason = property(get_Reason, None)
class PhoneIncomingCallNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Calls.Background.PhoneIncomingCallNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_CallId(self: win32more.Windows.ApplicationModel.Calls.Background.IPhoneIncomingCallNotificationTriggerDetails) -> WinRT_String: ...
    LineId = property(get_LineId, None)
    CallId = property(get_CallId, None)
PhoneLineChangeKind = Int32
PhoneLineChangeKind_Added: PhoneLineChangeKind = 0
PhoneLineChangeKind_Removed: PhoneLineChangeKind = 1
PhoneLineChangeKind_PropertiesChanged: PhoneLineChangeKind = 2
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
    LineId = property(get_LineId, None)
    ChangeType = property(get_ChangeType, None)
PhoneLineProperties = UInt32
PhoneLineProperties_None: PhoneLineProperties = 0
PhoneLineProperties_BrandingOptions: PhoneLineProperties = 1
PhoneLineProperties_CanDial: PhoneLineProperties = 2
PhoneLineProperties_CellularDetails: PhoneLineProperties = 4
PhoneLineProperties_DisplayColor: PhoneLineProperties = 8
PhoneLineProperties_DisplayName: PhoneLineProperties = 16
PhoneLineProperties_NetworkName: PhoneLineProperties = 32
PhoneLineProperties_NetworkState: PhoneLineProperties = 64
PhoneLineProperties_Transport: PhoneLineProperties = 128
PhoneLineProperties_Voicemail: PhoneLineProperties = 256
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
    VoicemailCount = property(get_VoicemailCount, None)
    OperatorMessage = property(get_OperatorMessage, None)
PhoneTriggerType = Int32
PhoneTriggerType_NewVoicemailMessage: PhoneTriggerType = 0
PhoneTriggerType_CallHistoryChanged: PhoneTriggerType = 1
PhoneTriggerType_LineChanged: PhoneTriggerType = 2
PhoneTriggerType_AirplaneModeDisabledForEmergencyCall: PhoneTriggerType = 3
PhoneTriggerType_CallOriginDataRequest: PhoneTriggerType = 4
PhoneTriggerType_CallBlocked: PhoneTriggerType = 5
PhoneTriggerType_IncomingCallDismissed: PhoneTriggerType = 6
PhoneTriggerType_IncomingCallNotification: PhoneTriggerType = 7
make_ready(__name__)
