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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Calls
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.UI
class CallAnswerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.ICallAnswerEventArgs
    _classid_ = 'Windows.ApplicationModel.Calls.CallAnswerEventArgs'
    @winrt_mixinmethod
    def get_AcceptedMedia(self: win32more.Windows.ApplicationModel.Calls.ICallAnswerEventArgs) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia: ...
    AcceptedMedia = property(get_AcceptedMedia, None)
class CallRejectEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.ICallRejectEventArgs
    _classid_ = 'Windows.ApplicationModel.Calls.CallRejectEventArgs'
    @winrt_mixinmethod
    def get_RejectReason(self: win32more.Windows.ApplicationModel.Calls.ICallRejectEventArgs) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallRejectReason: ...
    RejectReason = property(get_RejectReason, None)
class CallStateChangeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.ICallStateChangeEventArgs
    _classid_ = 'Windows.ApplicationModel.Calls.CallStateChangeEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.ApplicationModel.Calls.ICallStateChangeEventArgs) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallState: ...
    State = property(get_State, None)
CallsPhoneContract: UInt32 = 458752
CallsVoipContract: UInt32 = 262144
CellularDtmfMode = Int32
CellularDtmfMode_Continuous: CellularDtmfMode = 0
CellularDtmfMode_Burst: CellularDtmfMode = 1
DtmfKey = Int32
DtmfKey_D0: DtmfKey = 0
DtmfKey_D1: DtmfKey = 1
DtmfKey_D2: DtmfKey = 2
DtmfKey_D3: DtmfKey = 3
DtmfKey_D4: DtmfKey = 4
DtmfKey_D5: DtmfKey = 5
DtmfKey_D6: DtmfKey = 6
DtmfKey_D7: DtmfKey = 7
DtmfKey_D8: DtmfKey = 8
DtmfKey_D9: DtmfKey = 9
DtmfKey_Star: DtmfKey = 10
DtmfKey_Pound: DtmfKey = 11
DtmfToneAudioPlayback = Int32
DtmfToneAudioPlayback_Play: DtmfToneAudioPlayback = 0
DtmfToneAudioPlayback_DoNotPlay: DtmfToneAudioPlayback = 1
class ICallAnswerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.ICallAnswerEventArgs'
    _iid_ = Guid('{fd789617-2dd7-4c8c-b2bd-95d17a5bb733}')
    @winrt_commethod(6)
    def get_AcceptedMedia(self) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia: ...
    AcceptedMedia = property(get_AcceptedMedia, None)
class ICallRejectEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.ICallRejectEventArgs'
    _iid_ = Guid('{da47fad7-13d4-4d92-a1c2-b77811ee37ec}')
    @winrt_commethod(6)
    def get_RejectReason(self) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallRejectReason: ...
    RejectReason = property(get_RejectReason, None)
class ICallStateChangeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.ICallStateChangeEventArgs'
    _iid_ = Guid('{eab2349e-66f5-47f9-9fb5-459c5198c720}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallState: ...
    State = property(get_State, None)
class ILockScreenCallEndCallDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.ILockScreenCallEndCallDeferral'
    _iid_ = Guid('{2dd7ed0d-98ed-4041-9632-50ff812b773f}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ILockScreenCallEndRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.ILockScreenCallEndRequestedEventArgs'
    _iid_ = Guid('{8190a363-6f27-46e9-aeb6-c0ae83e47dc7}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Calls.LockScreenCallEndCallDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class ILockScreenCallUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.ILockScreenCallUI'
    _iid_ = Guid('{c596fd8d-73c9-4a14-b021-ec1c50a3b727}')
    @winrt_commethod(6)
    def Dismiss(self) -> Void: ...
    @winrt_commethod(7)
    def add_EndRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.LockScreenCallUI, win32more.Windows.ApplicationModel.Calls.LockScreenCallEndRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_EndRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.LockScreenCallUI, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_CallTitle(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_CallTitle(self, value: WinRT_String) -> Void: ...
    CallTitle = property(get_CallTitle, put_CallTitle)
class IMuteChangeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IMuteChangeEventArgs'
    _iid_ = Guid('{8585e159-0c41-432c-814d-c5f1fdf530be}')
    @winrt_commethod(6)
    def get_Muted(self) -> Boolean: ...
    Muted = property(get_Muted, None)
class IPhoneCall(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCall'
    _iid_ = Guid('{c14ed0f8-c17d-59d2-9628-66e545b6cd21}')
    @winrt_commethod(6)
    def add_StatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneCall, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_AudioDeviceChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneCall, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AudioDeviceChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_IsMutedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneCall, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_IsMutedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_CallId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_IsMuted(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallStatus: ...
    @winrt_commethod(15)
    def get_AudioDevice(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallAudioDevice: ...
    @winrt_commethod(16)
    def GetPhoneCallInfo(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallInfo: ...
    @winrt_commethod(17)
    def GetPhoneCallInfoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallInfo]: ...
    @winrt_commethod(18)
    def End(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(19)
    def EndAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(20)
    def SendDtmfKey(self, key: win32more.Windows.ApplicationModel.Calls.DtmfKey, dtmfToneAudioPlayback: win32more.Windows.ApplicationModel.Calls.DtmfToneAudioPlayback) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(21)
    def SendDtmfKeyAsync(self, key: win32more.Windows.ApplicationModel.Calls.DtmfKey, dtmfToneAudioPlayback: win32more.Windows.ApplicationModel.Calls.DtmfToneAudioPlayback) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(22)
    def AcceptIncoming(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(23)
    def AcceptIncomingAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(24)
    def Hold(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(25)
    def HoldAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(26)
    def ResumeFromHold(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(27)
    def ResumeFromHoldAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(28)
    def Mute(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(29)
    def MuteAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(30)
    def Unmute(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(31)
    def UnmuteAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(32)
    def RejectIncoming(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(33)
    def RejectIncomingAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_commethod(34)
    def ChangeAudioDevice(self, endpoint: win32more.Windows.ApplicationModel.Calls.PhoneCallAudioDevice) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(35)
    def ChangeAudioDeviceAsync(self, endpoint: win32more.Windows.ApplicationModel.Calls.PhoneCallAudioDevice) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    CallId = property(get_CallId, None)
    IsMuted = property(get_IsMuted, None)
    Status = property(get_Status, None)
    AudioDevice = property(get_AudioDevice, None)
class IPhoneCallBlockingStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallBlockingStatics'
    _iid_ = Guid('{19646f84-2b79-26f1-a46f-694be043f313}')
    @winrt_commethod(6)
    def get_BlockUnknownNumbers(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_BlockUnknownNumbers(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_BlockPrivateNumbers(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_BlockPrivateNumbers(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def SetCallBlockingListAsync(self, phoneNumberList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    BlockUnknownNumbers = property(get_BlockUnknownNumbers, put_BlockUnknownNumbers)
    BlockPrivateNumbers = property(get_BlockPrivateNumbers, put_BlockPrivateNumbers)
class IPhoneCallHistoryEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry'
    _iid_ = Guid('{fab0e129-32a4-4b85-83d1-f90d8c23a857}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Address(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress: ...
    @winrt_commethod(8)
    def put_Address(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress) -> Void: ...
    @winrt_commethod(9)
    def get_Duration(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(10)
    def put_Duration(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(11)
    def get_IsCallerIdBlocked(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_IsCallerIdBlocked(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_IsEmergency(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_IsEmergency(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_IsIncoming(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_IsIncoming(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_IsMissed(self) -> Boolean: ...
    @winrt_commethod(18)
    def put_IsMissed(self, value: Boolean) -> Void: ...
    @winrt_commethod(19)
    def get_IsRinging(self) -> Boolean: ...
    @winrt_commethod(20)
    def put_IsRinging(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_IsSeen(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_IsSeen(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_IsSuppressed(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_IsSuppressed(self, value: Boolean) -> Void: ...
    @winrt_commethod(25)
    def get_IsVoicemail(self) -> Boolean: ...
    @winrt_commethod(26)
    def put_IsVoicemail(self, value: Boolean) -> Void: ...
    @winrt_commethod(27)
    def get_Media(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryMedia: ...
    @winrt_commethod(28)
    def put_Media(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryMedia) -> Void: ...
    @winrt_commethod(29)
    def get_OtherAppReadAccess(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryOtherAppReadAccess: ...
    @winrt_commethod(30)
    def put_OtherAppReadAccess(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryOtherAppReadAccess) -> Void: ...
    @winrt_commethod(31)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(33)
    def get_SourceDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_SourceId(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def put_SourceId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(36)
    def get_SourceIdKind(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistorySourceIdKind: ...
    @winrt_commethod(37)
    def put_SourceIdKind(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistorySourceIdKind) -> Void: ...
    @winrt_commethod(38)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(39)
    def put_StartTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    Id = property(get_Id, None)
    Address = property(get_Address, put_Address)
    Duration = property(get_Duration, put_Duration)
    IsCallerIdBlocked = property(get_IsCallerIdBlocked, put_IsCallerIdBlocked)
    IsEmergency = property(get_IsEmergency, put_IsEmergency)
    IsIncoming = property(get_IsIncoming, put_IsIncoming)
    IsMissed = property(get_IsMissed, put_IsMissed)
    IsRinging = property(get_IsRinging, put_IsRinging)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsSuppressed = property(get_IsSuppressed, put_IsSuppressed)
    IsVoicemail = property(get_IsVoicemail, put_IsVoicemail)
    Media = property(get_Media, put_Media)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SourceDisplayName = property(get_SourceDisplayName, None)
    SourceId = property(get_SourceId, put_SourceId)
    SourceIdKind = property(get_SourceIdKind, put_SourceIdKind)
    StartTime = property(get_StartTime, put_StartTime)
class IPhoneCallHistoryEntryAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress'
    _iid_ = Guid('{30f159da-3955-4042-84e6-66eebf82e67f}')
    @winrt_commethod(6)
    def get_ContactId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ContactId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RawAddress(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_RawAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_RawAddressKind(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind: ...
    @winrt_commethod(13)
    def put_RawAddressKind(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind) -> Void: ...
    ContactId = property(get_ContactId, put_ContactId)
    DisplayName = property(get_DisplayName, put_DisplayName)
    RawAddress = property(get_RawAddress, put_RawAddress)
    RawAddressKind = property(get_RawAddressKind, put_RawAddressKind)
class IPhoneCallHistoryEntryAddressFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddressFactory'
    _iid_ = Guid('{fb0fadba-c7f0-4bb6-9f6b-ba5d73209aca}')
    @winrt_commethod(6)
    def Create(self, rawAddress: WinRT_String, rawAddressKind: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress: ...
class IPhoneCallHistoryEntryQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryQueryOptions'
    _iid_ = Guid('{9c5fe15c-8bed-40ca-b06e-c4ca8eae5c87}')
    @winrt_commethod(6)
    def get_DesiredMedia(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryDesiredMedia: ...
    @winrt_commethod(7)
    def put_DesiredMedia(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryDesiredMedia) -> Void: ...
    @winrt_commethod(8)
    def get_SourceIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    DesiredMedia = property(get_DesiredMedia, put_DesiredMedia)
    SourceIds = property(get_SourceIds, None)
class IPhoneCallHistoryEntryReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryReader'
    _iid_ = Guid('{61ece4be-8d86-479f-8404-a9846920fee6}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]]: ...
class IPhoneCallHistoryManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerForUser'
    _iid_ = Guid('{d925c523-f55f-4353-9db4-0205a5265a55}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStore]: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IPhoneCallHistoryManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerStatics'
    _iid_ = Guid('{f5a6da39-b31f-4f45-ac8e-1b08893c1b50}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, accessType: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStore]: ...
class IPhoneCallHistoryManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerStatics2'
    _iid_ = Guid('{efd474f0-a2db-4188-9e92-bc3cfa6813cf}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryManagerForUser: ...
class IPhoneCallHistoryStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallHistoryStore'
    _iid_ = Guid('{2f907db8-b40e-422b-8545-cb1910a61c52}')
    @winrt_commethod(6)
    def GetEntryAsync(self, callHistoryEntryId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]: ...
    @winrt_commethod(7)
    def GetEntryReader(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryReader: ...
    @winrt_commethod(8)
    def GetEntryReaderWithOptions(self, queryOptions: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryOptions) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryReader: ...
    @winrt_commethod(9)
    def SaveEntryAsync(self, callHistoryEntry: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def DeleteEntryAsync(self, callHistoryEntry: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def DeleteEntriesAsync(self, callHistoryEntries: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def MarkEntryAsSeenAsync(self, callHistoryEntry: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def MarkEntriesAsSeenAsync(self, callHistoryEntries: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def GetUnseenCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(15)
    def MarkAllAsSeenAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def GetSourcesUnseenCountAsync(self, sourceIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(17)
    def MarkSourcesAsSeenAsync(self, sourceIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPhoneCallInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallInfo'
    _iid_ = Guid('{22b42577-3e4d-5dc6-89c2-469fe5ffc189}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_IsHoldSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_CallDirection(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallDirection: ...
    LineId = property(get_LineId, None)
    IsHoldSupported = property(get_IsHoldSupported, None)
    StartTime = property(get_StartTime, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DisplayName = property(get_DisplayName, None)
    CallDirection = property(get_CallDirection, None)
class IPhoneCallManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallManagerStatics'
    _iid_ = Guid('{60edac78-78a6-4872-a3ef-98325ec8b843}')
    @winrt_commethod(6)
    def ShowPhoneCallUI(self, phoneNumber: WinRT_String, displayName: WinRT_String) -> Void: ...
class IPhoneCallManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2'
    _iid_ = Guid('{c7e3c8bc-2370-431c-98fd-43be5f03086d}')
    @winrt_commethod(6)
    def add_CallStateChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CallStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_IsCallActive(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsCallIncoming(self) -> Boolean: ...
    @winrt_commethod(10)
    def ShowPhoneCallSettingsUI(self) -> Void: ...
    @winrt_commethod(11)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallStore]: ...
    IsCallActive = property(get_IsCallActive, None)
    IsCallIncoming = property(get_IsCallIncoming, None)
class IPhoneCallStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallStatics'
    _iid_ = Guid('{2218eeab-f60b-53e7-ba13-5aeafbc22957}')
    @winrt_commethod(6)
    def GetFromId(self, callId: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.PhoneCall: ...
class IPhoneCallStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallStore'
    _iid_ = Guid('{5f610748-18a6-4173-86d1-28be9dc62dba}')
    @winrt_commethod(6)
    def IsEmergencyPhoneNumberAsync(self, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def GetDefaultLineAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Guid]: ...
    @winrt_commethod(8)
    def RequestLineWatcher(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher: ...
class IPhoneCallVideoCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallVideoCapabilities'
    _iid_ = Guid('{02382786-b16a-4fdb-be3b-c4240e13ad0d}')
    @winrt_commethod(6)
    def get_IsVideoCallingCapable(self) -> Boolean: ...
    IsVideoCallingCapable = property(get_IsVideoCallingCapable, None)
class IPhoneCallVideoCapabilitiesManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallVideoCapabilitiesManagerStatics'
    _iid_ = Guid('{f3c64b56-f00b-4a1c-a0c6-ee1910749ce7}')
    @winrt_commethod(6)
    def GetCapabilitiesAsync(self, phoneNumber: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallVideoCapabilities]: ...
class IPhoneCallsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneCallsResult'
    _iid_ = Guid('{1bfad365-57cf-57dd-986d-b057c91eac33}')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineOperationStatus: ...
    @winrt_commethod(7)
    def get_AllActivePhoneCalls(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Calls.PhoneCall]: ...
    OperationStatus = property(get_OperationStatus, None)
    AllActivePhoneCalls = property(get_AllActivePhoneCalls, None)
class IPhoneDialOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneDialOptions'
    _iid_ = Guid('{b639c4b8-f06f-36cb-a863-823742b5f2d4}')
    @winrt_commethod(6)
    def get_Number(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Number(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_commethod(11)
    def put_Contact(self, value: win32more.Windows.ApplicationModel.Contacts.Contact) -> Void: ...
    @winrt_commethod(12)
    def get_ContactPhone(self) -> win32more.Windows.ApplicationModel.Contacts.ContactPhone: ...
    @winrt_commethod(13)
    def put_ContactPhone(self, value: win32more.Windows.ApplicationModel.Contacts.ContactPhone) -> Void: ...
    @winrt_commethod(14)
    def get_Media(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallMedia: ...
    @winrt_commethod(15)
    def put_Media(self, value: win32more.Windows.ApplicationModel.Calls.PhoneCallMedia) -> Void: ...
    @winrt_commethod(16)
    def get_AudioEndpoint(self) -> win32more.Windows.ApplicationModel.Calls.PhoneAudioRoutingEndpoint: ...
    @winrt_commethod(17)
    def put_AudioEndpoint(self, value: win32more.Windows.ApplicationModel.Calls.PhoneAudioRoutingEndpoint) -> Void: ...
    Number = property(get_Number, put_Number)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Contact = property(get_Contact, put_Contact)
    ContactPhone = property(get_ContactPhone, put_ContactPhone)
    Media = property(get_Media, put_Media)
    AudioEndpoint = property(get_AudioEndpoint, put_AudioEndpoint)
class IPhoneLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLine'
    _iid_ = Guid('{27c66f30-6a69-34ca-a2ba-65302530c311}')
    @winrt_commethod(6)
    def add_LineChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLine, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LineChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(9)
    def get_DisplayColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(10)
    def get_NetworkState(self) -> win32more.Windows.ApplicationModel.Calls.PhoneNetworkState: ...
    @winrt_commethod(11)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Voicemail(self) -> win32more.Windows.ApplicationModel.Calls.PhoneVoicemail: ...
    @winrt_commethod(13)
    def get_NetworkName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_CellularDetails(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineCellularDetails: ...
    @winrt_commethod(15)
    def get_Transport(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineTransport: ...
    @winrt_commethod(16)
    def get_CanDial(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_SupportsTile(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_VideoCallingCapabilities(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallVideoCapabilities: ...
    @winrt_commethod(19)
    def get_LineConfiguration(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineConfiguration: ...
    @winrt_commethod(20)
    def IsImmediateDialNumberAsync(self, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def Dial(self, number: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def DialWithOptions(self, options: win32more.Windows.ApplicationModel.Calls.PhoneDialOptions) -> Void: ...
    Id = property(get_Id, None)
    DisplayColor = property(get_DisplayColor, None)
    NetworkState = property(get_NetworkState, None)
    DisplayName = property(get_DisplayName, None)
    Voicemail = property(get_Voicemail, None)
    NetworkName = property(get_NetworkName, None)
    CellularDetails = property(get_CellularDetails, None)
    Transport = property(get_Transport, None)
    CanDial = property(get_CanDial, None)
    SupportsTile = property(get_SupportsTile, None)
    VideoCallingCapabilities = property(get_VideoCallingCapabilities, None)
    LineConfiguration = property(get_LineConfiguration, None)
class IPhoneLine2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLine2'
    _iid_ = Guid('{0167f56a-5344-5d64-8af3-a31a950e916a}')
    @winrt_commethod(6)
    def EnableTextReply(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_TransportDeviceId(self) -> WinRT_String: ...
    TransportDeviceId = property(get_TransportDeviceId, None)
class IPhoneLine3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLine3'
    _iid_ = Guid('{e2e33cf7-2406-57f3-826a-e5a5f40d6fb5}')
    @winrt_commethod(6)
    def DialWithResult(self, number: WinRT_String, displayName: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.PhoneLineDialResult: ...
    @winrt_commethod(7)
    def DialWithResultAsync(self, number: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneLineDialResult]: ...
    @winrt_commethod(8)
    def GetAllActivePhoneCalls(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallsResult: ...
    @winrt_commethod(9)
    def GetAllActivePhoneCallsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallsResult]: ...
class IPhoneLineCellularDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineCellularDetails'
    _iid_ = Guid('{192601d5-147c-4769-b673-98a5ec8426cb}')
    @winrt_commethod(6)
    def get_SimState(self) -> win32more.Windows.ApplicationModel.Calls.PhoneSimState: ...
    @winrt_commethod(7)
    def get_SimSlotIndex(self) -> Int32: ...
    @winrt_commethod(8)
    def get_IsModemOn(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_RegistrationRejectCode(self) -> Int32: ...
    @winrt_commethod(10)
    def GetNetworkOperatorDisplayText(self, location: win32more.Windows.ApplicationModel.Calls.PhoneLineNetworkOperatorDisplayTextLocation) -> WinRT_String: ...
    SimState = property(get_SimState, None)
    SimSlotIndex = property(get_SimSlotIndex, None)
    IsModemOn = property(get_IsModemOn, None)
    RegistrationRejectCode = property(get_RegistrationRejectCode, None)
class IPhoneLineConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineConfiguration'
    _iid_ = Guid('{fe265862-f64f-4312-b2a8-4e257721aa95}')
    @winrt_commethod(6)
    def get_IsVideoCallingEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    IsVideoCallingEnabled = property(get_IsVideoCallingEnabled, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
class IPhoneLineDialResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineDialResult'
    _iid_ = Guid('{e825a30a-5c7f-546f-b918-3ad2fe70fb34}')
    @winrt_commethod(6)
    def get_DialCallStatus(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_commethod(7)
    def get_DialedCall(self) -> win32more.Windows.ApplicationModel.Calls.PhoneCall: ...
    DialCallStatus = property(get_DialCallStatus, None)
    DialedCall = property(get_DialedCall, None)
class IPhoneLineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineStatics'
    _iid_ = Guid('{f38b5f23-ceb0-404f-bcf2-ba9f697d8adf}')
    @winrt_commethod(6)
    def FromIdAsync(self, lineId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneLine]: ...
class IPhoneLineTransportDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineTransportDevice'
    _iid_ = Guid('{efa8f889-cffa-59f4-97e4-74705b7dc490}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Transport(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineTransport: ...
    @winrt_commethod(8)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(9)
    def RegisterApp(self) -> Void: ...
    @winrt_commethod(10)
    def RegisterAppForUser(self, user: win32more.Windows.System.User) -> Void: ...
    @winrt_commethod(11)
    def UnregisterApp(self) -> Void: ...
    @winrt_commethod(12)
    def UnregisterAppForUser(self, user: win32more.Windows.System.User) -> Void: ...
    @winrt_commethod(13)
    def IsRegistered(self) -> Boolean: ...
    @winrt_commethod(14)
    def Connect(self) -> Boolean: ...
    @winrt_commethod(15)
    def ConnectAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    DeviceId = property(get_DeviceId, None)
    Transport = property(get_Transport, None)
class IPhoneLineTransportDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2'
    _iid_ = Guid('{64c885f2-ecf4-5761-8c04-3c248ce61690}')
    @winrt_commethod(6)
    def get_AudioRoutingStatus(self) -> win32more.Windows.ApplicationModel.Calls.TransportDeviceAudioRoutingStatus: ...
    @winrt_commethod(7)
    def add_AudioRoutingStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineTransportDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AudioRoutingStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_InBandRingingEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_InBandRingingEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineTransportDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_InBandRingingEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AudioRoutingStatus = property(get_AudioRoutingStatus, None)
    InBandRingingEnabled = property(get_InBandRingingEnabled, None)
class IPhoneLineTransportDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineTransportDeviceStatics'
    _iid_ = Guid('{0f3121ac-d609-51a1-96f3-fb00d1819252}')
    @winrt_commethod(6)
    def FromId(self, id: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.PhoneLineTransportDevice: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorForPhoneLineTransport(self, transport: win32more.Windows.ApplicationModel.Calls.PhoneLineTransport) -> WinRT_String: ...
class IPhoneLineWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineWatcher'
    _iid_ = Guid('{8a45cd0a-6323-44e0-a6f6-9f21f64dc90a}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def add_LineAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LineAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_LineRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LineRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_LineUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_LineUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherStatus: ...
    Status = property(get_Status, None)
class IPhoneLineWatcherEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneLineWatcherEventArgs'
    _iid_ = Guid('{d07c753e-9e12-4a37-82b7-ad535dad6a67}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    LineId = property(get_LineId, None)
class IPhoneVoicemail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IPhoneVoicemail'
    _iid_ = Guid('{c9ce77f6-6e9f-3a8b-b727-6e0cf6998224}')
    @winrt_commethod(6)
    def get_Number(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MessageCount(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Type(self) -> win32more.Windows.ApplicationModel.Calls.PhoneVoicemailType: ...
    @winrt_commethod(9)
    def DialVoicemailAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Number = property(get_Number, None)
    MessageCount = property(get_MessageCount, None)
    Type = property(get_Type, None)
class IVoipCallCoordinator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipCallCoordinator'
    _iid_ = Guid('{4f118bcf-e8ef-4434-9c5f-a8d893fafe79}')
    @winrt_commethod(6)
    def ReserveCallResourcesAsync(self, taskEntryPoint: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.VoipPhoneCallResourceReservationStatus]: ...
    @winrt_commethod(7)
    def add_MuteStateChanged(self, muteChangeHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipCallCoordinator, win32more.Windows.ApplicationModel.Calls.MuteChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_MuteStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def RequestNewIncomingCall(self, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, contactImage: win32more.Windows.Foundation.Uri, serviceName: WinRT_String, brandingImage: win32more.Windows.Foundation.Uri, callDetails: WinRT_String, ringtone: win32more.Windows.Foundation.Uri, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia, ringTimeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_commethod(10)
    def RequestNewOutgoingCall(self, context: WinRT_String, contactName: WinRT_String, serviceName: WinRT_String, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_commethod(11)
    def NotifyMuted(self) -> Void: ...
    @winrt_commethod(12)
    def NotifyUnmuted(self) -> Void: ...
    @winrt_commethod(13)
    def RequestOutgoingUpgradeToVideoCall(self, callUpgradeGuid: Guid, context: WinRT_String, contactName: WinRT_String, serviceName: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_commethod(14)
    def RequestIncomingUpgradeToVideoCall(self, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, contactImage: win32more.Windows.Foundation.Uri, serviceName: WinRT_String, brandingImage: win32more.Windows.Foundation.Uri, callDetails: WinRT_String, ringtone: win32more.Windows.Foundation.Uri, ringTimeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_commethod(15)
    def TerminateCellularCall(self, callUpgradeGuid: Guid) -> Void: ...
    @winrt_commethod(16)
    def CancelUpgrade(self, callUpgradeGuid: Guid) -> Void: ...
class IVoipCallCoordinator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipCallCoordinator2'
    _iid_ = Guid('{beb4a9f3-c704-4234-89ce-e88cc0d28fbe}')
    @winrt_commethod(6)
    def SetupNewAcceptedCall(self, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, serviceName: WinRT_String, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
class IVoipCallCoordinator3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipCallCoordinator3'
    _iid_ = Guid('{338d0cbf-9b55-4021-87ca-e64b9bd666c7}')
    @winrt_commethod(6)
    def RequestNewAppInitiatedCall(self, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, serviceName: WinRT_String, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_commethod(7)
    def RequestNewIncomingCallWithContactRemoteId(self, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, contactImage: win32more.Windows.Foundation.Uri, serviceName: WinRT_String, brandingImage: win32more.Windows.Foundation.Uri, callDetails: WinRT_String, ringtone: win32more.Windows.Foundation.Uri, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia, ringTimeout: win32more.Windows.Foundation.TimeSpan, contactRemoteId: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
class IVoipCallCoordinator4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipCallCoordinator4'
    _iid_ = Guid('{83737239-9311-468f-bb49-47e0dfb5d93e}')
    @winrt_commethod(6)
    def ReserveOneProcessCallResourcesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.VoipPhoneCallResourceReservationStatus]: ...
class IVoipCallCoordinatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipCallCoordinatorStatics'
    _iid_ = Guid('{7f5d1f2b-e04a-4d10-b31a-a55c922cc2fb}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.Calls.VoipCallCoordinator: ...
class IVoipPhoneCall(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipPhoneCall'
    _iid_ = Guid('{6cf1f19a-7794-4a5a-8c68-ae87947a6990}')
    @winrt_commethod(6)
    def add_EndRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallStateChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EndRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_HoldRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallStateChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HoldRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ResumeRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallStateChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ResumeRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_AnswerRequested(self, acceptHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallAnswerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_AnswerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_RejectRequested(self, rejectHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallRejectEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_RejectRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def NotifyCallHeld(self) -> Void: ...
    @winrt_commethod(17)
    def NotifyCallActive(self) -> Void: ...
    @winrt_commethod(18)
    def NotifyCallEnded(self) -> Void: ...
    @winrt_commethod(19)
    def get_ContactName(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_ContactName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(22)
    def put_StartTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(23)
    def get_CallMedia(self) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia: ...
    @winrt_commethod(24)
    def put_CallMedia(self, value: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> Void: ...
    @winrt_commethod(25)
    def NotifyCallReady(self) -> Void: ...
    ContactName = property(get_ContactName, put_ContactName)
    StartTime = property(get_StartTime, put_StartTime)
    CallMedia = property(get_CallMedia, put_CallMedia)
class IVoipPhoneCall2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipPhoneCall2'
    _iid_ = Guid('{741b46e1-245f-41f3-9399-3141d25b52e3}')
    @winrt_commethod(6)
    def TryShowAppUI(self) -> Void: ...
class IVoipPhoneCall3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.IVoipPhoneCall3'
    _iid_ = Guid('{0d891522-e258-4aa9-907a-1aa413c25523}')
    @winrt_commethod(6)
    def NotifyCallAccepted(self, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> Void: ...
LockScreenCallContract: UInt32 = 65536
class LockScreenCallEndCallDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.ILockScreenCallEndCallDeferral
    _classid_ = 'Windows.ApplicationModel.Calls.LockScreenCallEndCallDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallEndCallDeferral) -> Void: ...
class LockScreenCallEndRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.ILockScreenCallEndRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.Calls.LockScreenCallEndRequestedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallEndRequestedEventArgs) -> win32more.Windows.ApplicationModel.Calls.LockScreenCallEndCallDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallEndRequestedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class LockScreenCallUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI
    _classid_ = 'Windows.ApplicationModel.Calls.LockScreenCallUI'
    @winrt_mixinmethod
    def Dismiss(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI) -> Void: ...
    @winrt_mixinmethod
    def add_EndRequested(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.LockScreenCallUI, win32more.Windows.ApplicationModel.Calls.LockScreenCallEndRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EndRequested(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.LockScreenCallUI, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CallTitle(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallTitle(self: win32more.Windows.ApplicationModel.Calls.ILockScreenCallUI, value: WinRT_String) -> Void: ...
    CallTitle = property(get_CallTitle, put_CallTitle)
class MuteChangeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IMuteChangeEventArgs
    _classid_ = 'Windows.ApplicationModel.Calls.MuteChangeEventArgs'
    @winrt_mixinmethod
    def get_Muted(self: win32more.Windows.ApplicationModel.Calls.IMuteChangeEventArgs) -> Boolean: ...
    Muted = property(get_Muted, None)
PhoneAudioRoutingEndpoint = Int32
PhoneAudioRoutingEndpoint_Default: PhoneAudioRoutingEndpoint = 0
PhoneAudioRoutingEndpoint_Bluetooth: PhoneAudioRoutingEndpoint = 1
PhoneAudioRoutingEndpoint_Speakerphone: PhoneAudioRoutingEndpoint = 2
class PhoneCall(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCall
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCall'
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneCall, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AudioDeviceChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneCall, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioDeviceChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsMutedChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneCall, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsMutedChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CallId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsMuted(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallStatus: ...
    @winrt_mixinmethod
    def get_AudioDevice(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallAudioDevice: ...
    @winrt_mixinmethod
    def GetPhoneCallInfo(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallInfo: ...
    @winrt_mixinmethod
    def GetPhoneCallInfoAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallInfo]: ...
    @winrt_mixinmethod
    def End(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def EndAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def SendDtmfKey(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, key: win32more.Windows.ApplicationModel.Calls.DtmfKey, dtmfToneAudioPlayback: win32more.Windows.ApplicationModel.Calls.DtmfToneAudioPlayback) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def SendDtmfKeyAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, key: win32more.Windows.ApplicationModel.Calls.DtmfKey, dtmfToneAudioPlayback: win32more.Windows.ApplicationModel.Calls.DtmfToneAudioPlayback) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def AcceptIncoming(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def AcceptIncomingAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def Hold(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def HoldAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def ResumeFromHold(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def ResumeFromHoldAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def Mute(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def MuteAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def Unmute(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def UnmuteAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def RejectIncoming(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def RejectIncomingAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_mixinmethod
    def ChangeAudioDevice(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, endpoint: win32more.Windows.ApplicationModel.Calls.PhoneCallAudioDevice) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def ChangeAudioDeviceAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCall, endpoint: win32more.Windows.ApplicationModel.Calls.PhoneCallAudioDevice) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]: ...
    @winrt_classmethod
    def GetFromId(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallStatics, callId: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.PhoneCall: ...
    CallId = property(get_CallId, None)
    IsMuted = property(get_IsMuted, None)
    Status = property(get_Status, None)
    AudioDevice = property(get_AudioDevice, None)
PhoneCallAudioDevice = Int32
PhoneCallAudioDevice_Unknown: PhoneCallAudioDevice = 0
PhoneCallAudioDevice_LocalDevice: PhoneCallAudioDevice = 1
PhoneCallAudioDevice_RemoteDevice: PhoneCallAudioDevice = 2
class _PhoneCallBlocking_Meta_(ComPtr.__class__):
    pass
class PhoneCallBlocking(ComPtr, metaclass=_PhoneCallBlocking_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallBlocking'
    @winrt_classmethod
    def get_BlockUnknownNumbers(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallBlockingStatics) -> Boolean: ...
    @winrt_classmethod
    def put_BlockUnknownNumbers(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallBlockingStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_BlockPrivateNumbers(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallBlockingStatics) -> Boolean: ...
    @winrt_classmethod
    def put_BlockPrivateNumbers(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallBlockingStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def SetCallBlockingListAsync(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallBlockingStatics, phoneNumberList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    _PhoneCallBlocking_Meta_.BlockUnknownNumbers = property(get_BlockUnknownNumbers.__wrapped__, put_BlockUnknownNumbers.__wrapped__)
    _PhoneCallBlocking_Meta_.BlockPrivateNumbers = property(get_BlockPrivateNumbers.__wrapped__, put_BlockPrivateNumbers.__wrapped__)
PhoneCallDirection = Int32
PhoneCallDirection_Unknown: PhoneCallDirection = 0
PhoneCallDirection_Incoming: PhoneCallDirection = 1
PhoneCallDirection_Outgoing: PhoneCallDirection = 2
class PhoneCallHistoryEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryEntry'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress: ...
    @winrt_mixinmethod
    def put_Address(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_IsCallerIdBlocked(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCallerIdBlocked(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsEmergency(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEmergency(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsIncoming(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIncoming(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsMissed(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMissed(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRinging(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRinging(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSeen(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSeen(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSuppressed(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSuppressed(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsVoicemail(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVoicemail(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Media(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryMedia: ...
    @winrt_mixinmethod
    def put_Media(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryMedia) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceDisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SourceId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceIdKind(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistorySourceIdKind: ...
    @winrt_mixinmethod
    def put_SourceIdKind(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistorySourceIdKind) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntry, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    Id = property(get_Id, None)
    Address = property(get_Address, put_Address)
    Duration = property(get_Duration, put_Duration)
    IsCallerIdBlocked = property(get_IsCallerIdBlocked, put_IsCallerIdBlocked)
    IsEmergency = property(get_IsEmergency, put_IsEmergency)
    IsIncoming = property(get_IsIncoming, put_IsIncoming)
    IsMissed = property(get_IsMissed, put_IsMissed)
    IsRinging = property(get_IsRinging, put_IsRinging)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsSuppressed = property(get_IsSuppressed, put_IsSuppressed)
    IsVoicemail = property(get_IsVoicemail, put_IsVoicemail)
    Media = property(get_Media, put_Media)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SourceDisplayName = property(get_SourceDisplayName, None)
    SourceId = property(get_SourceId, put_SourceId)
    SourceIdKind = property(get_SourceIdKind, put_SourceIdKind)
    StartTime = property(get_StartTime, put_StartTime)
class PhoneCallHistoryEntryAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress.CreateInstance(*args)
        elif len(args) == 2:
            instance = win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddressFactory, rawAddress: WinRT_String, rawAddressKind: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryAddress: ...
    @winrt_mixinmethod
    def get_ContactId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContactId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RawAddress(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RawAddress(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RawAddressKind(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind: ...
    @winrt_mixinmethod
    def put_RawAddressKind(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryAddress, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind) -> Void: ...
    ContactId = property(get_ContactId, put_ContactId)
    DisplayName = property(get_DisplayName, put_DisplayName)
    RawAddress = property(get_RawAddress, put_RawAddress)
    RawAddressKind = property(get_RawAddressKind, put_RawAddressKind)
PhoneCallHistoryEntryMedia = Int32
PhoneCallHistoryEntryMedia_Audio: PhoneCallHistoryEntryMedia = 0
PhoneCallHistoryEntryMedia_Video: PhoneCallHistoryEntryMedia = 1
PhoneCallHistoryEntryOtherAppReadAccess = Int32
PhoneCallHistoryEntryOtherAppReadAccess_Full: PhoneCallHistoryEntryOtherAppReadAccess = 0
PhoneCallHistoryEntryOtherAppReadAccess_SystemOnly: PhoneCallHistoryEntryOtherAppReadAccess = 1
PhoneCallHistoryEntryQueryDesiredMedia = UInt32
PhoneCallHistoryEntryQueryDesiredMedia_None: PhoneCallHistoryEntryQueryDesiredMedia = 0
PhoneCallHistoryEntryQueryDesiredMedia_Audio: PhoneCallHistoryEntryQueryDesiredMedia = 1
PhoneCallHistoryEntryQueryDesiredMedia_Video: PhoneCallHistoryEntryQueryDesiredMedia = 2
PhoneCallHistoryEntryQueryDesiredMedia_All: PhoneCallHistoryEntryQueryDesiredMedia = 4294967295
class PhoneCallHistoryEntryQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryQueryOptions
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryOptions'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryOptions: ...
    @winrt_mixinmethod
    def get_DesiredMedia(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryQueryOptions) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryDesiredMedia: ...
    @winrt_mixinmethod
    def put_DesiredMedia(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryQueryOptions, value: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryDesiredMedia) -> Void: ...
    @winrt_mixinmethod
    def get_SourceIds(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    DesiredMedia = property(get_DesiredMedia, put_DesiredMedia)
    SourceIds = property(get_SourceIds, None)
PhoneCallHistoryEntryRawAddressKind = Int32
PhoneCallHistoryEntryRawAddressKind_PhoneNumber: PhoneCallHistoryEntryRawAddressKind = 0
PhoneCallHistoryEntryRawAddressKind_Custom: PhoneCallHistoryEntryRawAddressKind = 1
class PhoneCallHistoryEntryReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryReader
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryEntryReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryEntryReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]]: ...
class PhoneCallHistoryManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryManager'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryManagerForUser: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerStatics, accessType: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStore]: ...
class PhoneCallHistoryManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerForUser
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryManagerForUser'
    @winrt_mixinmethod
    def RequestStoreAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerForUser, accessType: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryStore]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryManagerForUser) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
PhoneCallHistorySourceIdKind = Int32
PhoneCallHistorySourceIdKind_CellularPhoneLineId: PhoneCallHistorySourceIdKind = 0
PhoneCallHistorySourceIdKind_PackageFamilyName: PhoneCallHistorySourceIdKind = 1
class PhoneCallHistoryStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallHistoryStore'
    @winrt_mixinmethod
    def GetEntryAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, callHistoryEntryId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]: ...
    @winrt_mixinmethod
    def GetEntryReader(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryReader: ...
    @winrt_mixinmethod
    def GetEntryReaderWithOptions(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, queryOptions: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryOptions) -> win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryReader: ...
    @winrt_mixinmethod
    def SaveEntryAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, callHistoryEntry: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteEntryAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, callHistoryEntry: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteEntriesAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, callHistoryEntries: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkEntryAsSeenAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, callHistoryEntry: win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkEntriesAsSeenAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, callHistoryEntries: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Calls.PhoneCallHistoryEntry]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetUnseenCountAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def MarkAllAsSeenAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetSourcesUnseenCountAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, sourceIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def MarkSourcesAsSeenAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallHistoryStore, sourceIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
PhoneCallHistoryStoreAccessType = Int32
PhoneCallHistoryStoreAccessType_AppEntriesReadWrite: PhoneCallHistoryStoreAccessType = 0
PhoneCallHistoryStoreAccessType_AllEntriesLimitedReadWrite: PhoneCallHistoryStoreAccessType = 1
PhoneCallHistoryStoreAccessType_AllEntriesReadWrite: PhoneCallHistoryStoreAccessType = 2
class PhoneCallInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallInfo'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_IsHoldSupported(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CallDirection(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallInfo) -> win32more.Windows.ApplicationModel.Calls.PhoneCallDirection: ...
    LineId = property(get_LineId, None)
    IsHoldSupported = property(get_IsHoldSupported, None)
    StartTime = property(get_StartTime, None)
    PhoneNumber = property(get_PhoneNumber, None)
    DisplayName = property(get_DisplayName, None)
    CallDirection = property(get_CallDirection, None)
class _PhoneCallManager_Meta_(ComPtr.__class__):
    pass
class PhoneCallManager(ComPtr, metaclass=_PhoneCallManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallManager'
    @winrt_classmethod
    def add_CallStateChanged(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CallStateChanged(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_IsCallActive(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_IsCallIncoming(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def ShowPhoneCallSettingsUI(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2) -> Void: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallStore]: ...
    @winrt_classmethod
    def ShowPhoneCallUI(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallManagerStatics, phoneNumber: WinRT_String, displayName: WinRT_String) -> Void: ...
    _PhoneCallManager_Meta_.IsCallActive = property(get_IsCallActive.__wrapped__, None)
    _PhoneCallManager_Meta_.IsCallIncoming = property(get_IsCallIncoming.__wrapped__, None)
PhoneCallMedia = Int32
PhoneCallMedia_Audio: PhoneCallMedia = 0
PhoneCallMedia_AudioAndVideo: PhoneCallMedia = 1
PhoneCallMedia_AudioAndRealTimeText: PhoneCallMedia = 2
PhoneCallOperationStatus = Int32
PhoneCallOperationStatus_Succeeded: PhoneCallOperationStatus = 0
PhoneCallOperationStatus_OtherFailure: PhoneCallOperationStatus = 1
PhoneCallOperationStatus_TimedOut: PhoneCallOperationStatus = 2
PhoneCallOperationStatus_ConnectionLost: PhoneCallOperationStatus = 3
PhoneCallOperationStatus_InvalidCallState: PhoneCallOperationStatus = 4
PhoneCallStatus = Int32
PhoneCallStatus_Lost: PhoneCallStatus = 0
PhoneCallStatus_Incoming: PhoneCallStatus = 1
PhoneCallStatus_Dialing: PhoneCallStatus = 2
PhoneCallStatus_Talking: PhoneCallStatus = 3
PhoneCallStatus_Held: PhoneCallStatus = 4
PhoneCallStatus_Ended: PhoneCallStatus = 5
class PhoneCallStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallStore
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallStore'
    @winrt_mixinmethod
    def IsEmergencyPhoneNumberAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallStore, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetDefaultLineAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallStore) -> win32more.Windows.Foundation.IAsyncOperation[Guid]: ...
    @winrt_mixinmethod
    def RequestLineWatcher(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallStore) -> win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher: ...
class PhoneCallVideoCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallVideoCapabilities
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallVideoCapabilities'
    @winrt_mixinmethod
    def get_IsVideoCallingCapable(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallVideoCapabilities) -> Boolean: ...
    IsVideoCallingCapable = property(get_IsVideoCallingCapable, None)
class PhoneCallVideoCapabilitiesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallVideoCapabilitiesManager'
    @winrt_classmethod
    def GetCapabilitiesAsync(cls: win32more.Windows.ApplicationModel.Calls.IPhoneCallVideoCapabilitiesManagerStatics, phoneNumber: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallVideoCapabilities]: ...
class PhoneCallsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneCallsResult
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneCallsResult'
    @winrt_mixinmethod
    def get_OperationStatus(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallsResult) -> win32more.Windows.ApplicationModel.Calls.PhoneLineOperationStatus: ...
    @winrt_mixinmethod
    def get_AllActivePhoneCalls(self: win32more.Windows.ApplicationModel.Calls.IPhoneCallsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Calls.PhoneCall]: ...
    OperationStatus = property(get_OperationStatus, None)
    AllActivePhoneCalls = property(get_AllActivePhoneCalls, None)
class PhoneDialOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneDialOptions'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Calls.PhoneDialOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Calls.PhoneDialOptions: ...
    @winrt_mixinmethod
    def get_Number(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Number(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def put_Contact(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions, value: win32more.Windows.ApplicationModel.Contacts.Contact) -> Void: ...
    @winrt_mixinmethod
    def get_ContactPhone(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions) -> win32more.Windows.ApplicationModel.Contacts.ContactPhone: ...
    @winrt_mixinmethod
    def put_ContactPhone(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions, value: win32more.Windows.ApplicationModel.Contacts.ContactPhone) -> Void: ...
    @winrt_mixinmethod
    def get_Media(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions) -> win32more.Windows.ApplicationModel.Calls.PhoneCallMedia: ...
    @winrt_mixinmethod
    def put_Media(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions, value: win32more.Windows.ApplicationModel.Calls.PhoneCallMedia) -> Void: ...
    @winrt_mixinmethod
    def get_AudioEndpoint(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions) -> win32more.Windows.ApplicationModel.Calls.PhoneAudioRoutingEndpoint: ...
    @winrt_mixinmethod
    def put_AudioEndpoint(self: win32more.Windows.ApplicationModel.Calls.IPhoneDialOptions, value: win32more.Windows.ApplicationModel.Calls.PhoneAudioRoutingEndpoint) -> Void: ...
    Number = property(get_Number, put_Number)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Contact = property(get_Contact, put_Contact)
    ContactPhone = property(get_ContactPhone, put_ContactPhone)
    Media = property(get_Media, put_Media)
    AudioEndpoint = property(get_AudioEndpoint, put_AudioEndpoint)
class PhoneLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLine
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLine'
    @winrt_mixinmethod
    def add_LineChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLine, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LineChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> Guid: ...
    @winrt_mixinmethod
    def get_DisplayColor(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_NetworkState(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.ApplicationModel.Calls.PhoneNetworkState: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Voicemail(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.ApplicationModel.Calls.PhoneVoicemail: ...
    @winrt_mixinmethod
    def get_NetworkName(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularDetails(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.ApplicationModel.Calls.PhoneLineCellularDetails: ...
    @winrt_mixinmethod
    def get_Transport(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.ApplicationModel.Calls.PhoneLineTransport: ...
    @winrt_mixinmethod
    def get_CanDial(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsTile(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> Boolean: ...
    @winrt_mixinmethod
    def get_VideoCallingCapabilities(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.ApplicationModel.Calls.PhoneCallVideoCapabilities: ...
    @winrt_mixinmethod
    def get_LineConfiguration(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine) -> win32more.Windows.ApplicationModel.Calls.PhoneLineConfiguration: ...
    @winrt_mixinmethod
    def IsImmediateDialNumberAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Dial(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine, number: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DialWithOptions(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine, options: win32more.Windows.ApplicationModel.Calls.PhoneDialOptions) -> Void: ...
    @winrt_mixinmethod
    def EnableTextReply(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransportDeviceId(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine2) -> WinRT_String: ...
    @winrt_mixinmethod
    def DialWithResult(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine3, number: WinRT_String, displayName: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.PhoneLineDialResult: ...
    @winrt_mixinmethod
    def DialWithResultAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine3, number: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneLineDialResult]: ...
    @winrt_mixinmethod
    def GetAllActivePhoneCalls(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine3) -> win32more.Windows.ApplicationModel.Calls.PhoneCallsResult: ...
    @winrt_mixinmethod
    def GetAllActivePhoneCallsAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneLine3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneCallsResult]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.ApplicationModel.Calls.IPhoneLineStatics, lineId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.PhoneLine]: ...
    Id = property(get_Id, None)
    DisplayColor = property(get_DisplayColor, None)
    NetworkState = property(get_NetworkState, None)
    DisplayName = property(get_DisplayName, None)
    Voicemail = property(get_Voicemail, None)
    NetworkName = property(get_NetworkName, None)
    CellularDetails = property(get_CellularDetails, None)
    Transport = property(get_Transport, None)
    CanDial = property(get_CanDial, None)
    SupportsTile = property(get_SupportsTile, None)
    VideoCallingCapabilities = property(get_VideoCallingCapabilities, None)
    LineConfiguration = property(get_LineConfiguration, None)
    TransportDeviceId = property(get_TransportDeviceId, None)
class PhoneLineCellularDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLineCellularDetails
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLineCellularDetails'
    @winrt_mixinmethod
    def get_SimState(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineCellularDetails) -> win32more.Windows.ApplicationModel.Calls.PhoneSimState: ...
    @winrt_mixinmethod
    def get_SimSlotIndex(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineCellularDetails) -> Int32: ...
    @winrt_mixinmethod
    def get_IsModemOn(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineCellularDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_RegistrationRejectCode(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineCellularDetails) -> Int32: ...
    @winrt_mixinmethod
    def GetNetworkOperatorDisplayText(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineCellularDetails, location: win32more.Windows.ApplicationModel.Calls.PhoneLineNetworkOperatorDisplayTextLocation) -> WinRT_String: ...
    SimState = property(get_SimState, None)
    SimSlotIndex = property(get_SimSlotIndex, None)
    IsModemOn = property(get_IsModemOn, None)
    RegistrationRejectCode = property(get_RegistrationRejectCode, None)
class PhoneLineConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLineConfiguration
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLineConfiguration'
    @winrt_mixinmethod
    def get_IsVideoCallingEnabled(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineConfiguration) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    IsVideoCallingEnabled = property(get_IsVideoCallingEnabled, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
class PhoneLineDialResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLineDialResult
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLineDialResult'
    @winrt_mixinmethod
    def get_DialCallStatus(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineDialResult) -> win32more.Windows.ApplicationModel.Calls.PhoneCallOperationStatus: ...
    @winrt_mixinmethod
    def get_DialedCall(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineDialResult) -> win32more.Windows.ApplicationModel.Calls.PhoneCall: ...
    DialCallStatus = property(get_DialCallStatus, None)
    DialedCall = property(get_DialedCall, None)
PhoneLineNetworkOperatorDisplayTextLocation = Int32
PhoneLineNetworkOperatorDisplayTextLocation_Default: PhoneLineNetworkOperatorDisplayTextLocation = 0
PhoneLineNetworkOperatorDisplayTextLocation_Tile: PhoneLineNetworkOperatorDisplayTextLocation = 1
PhoneLineNetworkOperatorDisplayTextLocation_Dialer: PhoneLineNetworkOperatorDisplayTextLocation = 2
PhoneLineNetworkOperatorDisplayTextLocation_InCallUI: PhoneLineNetworkOperatorDisplayTextLocation = 3
PhoneLineOperationStatus = Int32
PhoneLineOperationStatus_Succeeded: PhoneLineOperationStatus = 0
PhoneLineOperationStatus_OtherFailure: PhoneLineOperationStatus = 1
PhoneLineOperationStatus_TimedOut: PhoneLineOperationStatus = 2
PhoneLineOperationStatus_ConnectionLost: PhoneLineOperationStatus = 3
PhoneLineOperationStatus_InvalidCallState: PhoneLineOperationStatus = 4
PhoneLineTransport = Int32
PhoneLineTransport_Cellular: PhoneLineTransport = 0
PhoneLineTransport_VoipApp: PhoneLineTransport = 1
PhoneLineTransport_Bluetooth: PhoneLineTransport = 2
class PhoneLineTransportDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLineTransportDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Transport(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> win32more.Windows.ApplicationModel.Calls.PhoneLineTransport: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def RegisterApp(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> Void: ...
    @winrt_mixinmethod
    def RegisterAppForUser(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice, user: win32more.Windows.System.User) -> Void: ...
    @winrt_mixinmethod
    def UnregisterApp(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> Void: ...
    @winrt_mixinmethod
    def UnregisterAppForUser(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice, user: win32more.Windows.System.User) -> Void: ...
    @winrt_mixinmethod
    def IsRegistered(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> Boolean: ...
    @winrt_mixinmethod
    def Connect(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> Boolean: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AudioRoutingStatus(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2) -> win32more.Windows.ApplicationModel.Calls.TransportDeviceAudioRoutingStatus: ...
    @winrt_mixinmethod
    def add_AudioRoutingStatusChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineTransportDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioRoutingStatusChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InBandRingingEnabled(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2) -> Boolean: ...
    @winrt_mixinmethod
    def add_InBandRingingEnabledChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineTransportDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InBandRingingEnabledChanged(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDevice2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FromId(cls: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDeviceStatics, id: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.PhoneLineTransportDevice: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForPhoneLineTransport(cls: win32more.Windows.ApplicationModel.Calls.IPhoneLineTransportDeviceStatics, transport: win32more.Windows.ApplicationModel.Calls.PhoneLineTransport) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Transport = property(get_Transport, None)
    AudioRoutingStatus = property(get_AudioRoutingStatus, None)
    InBandRingingEnabled = property(get_InBandRingingEnabled, None)
class PhoneLineWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLineWatcher'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_LineAdded(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LineAdded(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LineRemoved(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LineRemoved(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LineUpdated(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LineUpdated(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.PhoneLineWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcher) -> win32more.Windows.ApplicationModel.Calls.PhoneLineWatcherStatus: ...
    Status = property(get_Status, None)
class PhoneLineWatcherEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcherEventArgs
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneLineWatcherEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Calls.IPhoneLineWatcherEventArgs) -> Guid: ...
    LineId = property(get_LineId, None)
PhoneLineWatcherStatus = Int32
PhoneLineWatcherStatus_Created: PhoneLineWatcherStatus = 0
PhoneLineWatcherStatus_Started: PhoneLineWatcherStatus = 1
PhoneLineWatcherStatus_EnumerationCompleted: PhoneLineWatcherStatus = 2
PhoneLineWatcherStatus_Stopped: PhoneLineWatcherStatus = 3
PhoneNetworkState = Int32
PhoneNetworkState_Unknown: PhoneNetworkState = 0
PhoneNetworkState_NoSignal: PhoneNetworkState = 1
PhoneNetworkState_Deregistered: PhoneNetworkState = 2
PhoneNetworkState_Denied: PhoneNetworkState = 3
PhoneNetworkState_Searching: PhoneNetworkState = 4
PhoneNetworkState_Home: PhoneNetworkState = 5
PhoneNetworkState_RoamingInternational: PhoneNetworkState = 6
PhoneNetworkState_RoamingDomestic: PhoneNetworkState = 7
PhoneSimState = Int32
PhoneSimState_Unknown: PhoneSimState = 0
PhoneSimState_PinNotRequired: PhoneSimState = 1
PhoneSimState_PinUnlocked: PhoneSimState = 2
PhoneSimState_PinLocked: PhoneSimState = 3
PhoneSimState_PukLocked: PhoneSimState = 4
PhoneSimState_NotInserted: PhoneSimState = 5
PhoneSimState_Invalid: PhoneSimState = 6
PhoneSimState_Disabled: PhoneSimState = 7
class PhoneVoicemail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IPhoneVoicemail
    _classid_ = 'Windows.ApplicationModel.Calls.PhoneVoicemail'
    @winrt_mixinmethod
    def get_Number(self: win32more.Windows.ApplicationModel.Calls.IPhoneVoicemail) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageCount(self: win32more.Windows.ApplicationModel.Calls.IPhoneVoicemail) -> Int32: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.ApplicationModel.Calls.IPhoneVoicemail) -> win32more.Windows.ApplicationModel.Calls.PhoneVoicemailType: ...
    @winrt_mixinmethod
    def DialVoicemailAsync(self: win32more.Windows.ApplicationModel.Calls.IPhoneVoicemail) -> win32more.Windows.Foundation.IAsyncAction: ...
    Number = property(get_Number, None)
    MessageCount = property(get_MessageCount, None)
    Type = property(get_Type, None)
PhoneVoicemailType = Int32
PhoneVoicemailType_None: PhoneVoicemailType = 0
PhoneVoicemailType_Traditional: PhoneVoicemailType = 1
PhoneVoicemailType_Visual: PhoneVoicemailType = 2
TransportDeviceAudioRoutingStatus = Int32
TransportDeviceAudioRoutingStatus_Unknown: TransportDeviceAudioRoutingStatus = 0
TransportDeviceAudioRoutingStatus_CanRouteToLocalDevice: TransportDeviceAudioRoutingStatus = 1
TransportDeviceAudioRoutingStatus_CannotRouteToLocalDevice: TransportDeviceAudioRoutingStatus = 2
class VoipCallCoordinator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator
    _classid_ = 'Windows.ApplicationModel.Calls.VoipCallCoordinator'
    @winrt_mixinmethod
    def ReserveCallResourcesAsync(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, taskEntryPoint: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.VoipPhoneCallResourceReservationStatus]: ...
    @winrt_mixinmethod
    def add_MuteStateChanged(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, muteChangeHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipCallCoordinator, win32more.Windows.ApplicationModel.Calls.MuteChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MuteStateChanged(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestNewIncomingCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, contactImage: win32more.Windows.Foundation.Uri, serviceName: WinRT_String, brandingImage: win32more.Windows.Foundation.Uri, callDetails: WinRT_String, ringtone: win32more.Windows.Foundation.Uri, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia, ringTimeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def RequestNewOutgoingCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, context: WinRT_String, contactName: WinRT_String, serviceName: WinRT_String, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def NotifyMuted(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator) -> Void: ...
    @winrt_mixinmethod
    def NotifyUnmuted(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator) -> Void: ...
    @winrt_mixinmethod
    def RequestOutgoingUpgradeToVideoCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, callUpgradeGuid: Guid, context: WinRT_String, contactName: WinRT_String, serviceName: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def RequestIncomingUpgradeToVideoCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, contactImage: win32more.Windows.Foundation.Uri, serviceName: WinRT_String, brandingImage: win32more.Windows.Foundation.Uri, callDetails: WinRT_String, ringtone: win32more.Windows.Foundation.Uri, ringTimeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def TerminateCellularCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, callUpgradeGuid: Guid) -> Void: ...
    @winrt_mixinmethod
    def CancelUpgrade(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator, callUpgradeGuid: Guid) -> Void: ...
    @winrt_mixinmethod
    def SetupNewAcceptedCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator2, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, serviceName: WinRT_String, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def RequestNewAppInitiatedCall(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator3, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, serviceName: WinRT_String, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def RequestNewIncomingCallWithContactRemoteId(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator3, context: WinRT_String, contactName: WinRT_String, contactNumber: WinRT_String, contactImage: win32more.Windows.Foundation.Uri, serviceName: WinRT_String, brandingImage: win32more.Windows.Foundation.Uri, callDetails: WinRT_String, ringtone: win32more.Windows.Foundation.Uri, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia, ringTimeout: win32more.Windows.Foundation.TimeSpan, contactRemoteId: WinRT_String) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCall: ...
    @winrt_mixinmethod
    def ReserveOneProcessCallResourcesAsync(self: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinator4) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Calls.VoipPhoneCallResourceReservationStatus]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.ApplicationModel.Calls.IVoipCallCoordinatorStatics) -> win32more.Windows.ApplicationModel.Calls.VoipCallCoordinator: ...
class VoipPhoneCall(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall
    _classid_ = 'Windows.ApplicationModel.Calls.VoipPhoneCall'
    @winrt_mixinmethod
    def add_EndRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallStateChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EndRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallStateChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResumeRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallStateChangeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResumeRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AnswerRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, acceptHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallAnswerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AnswerRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RejectRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, rejectHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Calls.VoipPhoneCall, win32more.Windows.ApplicationModel.Calls.CallRejectEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RejectRequested(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyCallHeld(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> Void: ...
    @winrt_mixinmethod
    def NotifyCallActive(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> Void: ...
    @winrt_mixinmethod
    def NotifyCallEnded(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> Void: ...
    @winrt_mixinmethod
    def get_ContactName(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContactName(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_CallMedia(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia: ...
    @winrt_mixinmethod
    def put_CallMedia(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall, value: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> Void: ...
    @winrt_mixinmethod
    def NotifyCallReady(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall) -> Void: ...
    @winrt_mixinmethod
    def TryShowAppUI(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall2) -> Void: ...
    @winrt_mixinmethod
    def NotifyCallAccepted(self: win32more.Windows.ApplicationModel.Calls.IVoipPhoneCall3, media: win32more.Windows.ApplicationModel.Calls.VoipPhoneCallMedia) -> Void: ...
    ContactName = property(get_ContactName, put_ContactName)
    StartTime = property(get_StartTime, put_StartTime)
    CallMedia = property(get_CallMedia, put_CallMedia)
VoipPhoneCallMedia = UInt32
VoipPhoneCallMedia_None: VoipPhoneCallMedia = 0
VoipPhoneCallMedia_Audio: VoipPhoneCallMedia = 1
VoipPhoneCallMedia_Video: VoipPhoneCallMedia = 2
VoipPhoneCallRejectReason = Int32
VoipPhoneCallRejectReason_UserIgnored: VoipPhoneCallRejectReason = 0
VoipPhoneCallRejectReason_TimedOut: VoipPhoneCallRejectReason = 1
VoipPhoneCallRejectReason_OtherIncomingCall: VoipPhoneCallRejectReason = 2
VoipPhoneCallRejectReason_EmergencyCallExists: VoipPhoneCallRejectReason = 3
VoipPhoneCallRejectReason_InvalidCallState: VoipPhoneCallRejectReason = 4
VoipPhoneCallResourceReservationStatus = Int32
VoipPhoneCallResourceReservationStatus_Success: VoipPhoneCallResourceReservationStatus = 0
VoipPhoneCallResourceReservationStatus_ResourcesNotAvailable: VoipPhoneCallResourceReservationStatus = 1
VoipPhoneCallState = Int32
VoipPhoneCallState_Ended: VoipPhoneCallState = 0
VoipPhoneCallState_Held: VoipPhoneCallState = 1
VoipPhoneCallState_Active: VoipPhoneCallState = 2
VoipPhoneCallState_Incoming: VoipPhoneCallState = 3
VoipPhoneCallState_Outgoing: VoipPhoneCallState = 4
make_ready(__name__)
