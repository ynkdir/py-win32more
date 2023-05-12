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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Chat
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.MediaProperties
import Windows.Security.Credentials
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
class ChatCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatCapabilities
    _classid_ = 'Windows.ApplicationModel.Chat.ChatCapabilities'
    @winrt_mixinmethod
    def get_IsOnline(self: Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsChatCapable(self: Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFileTransferCapable(self: Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGeoLocationPushCapable(self: Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsIntegratedMessagingCapable(self: Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    IsOnline = property(get_IsOnline, None)
    IsChatCapable = property(get_IsChatCapable, None)
    IsFileTransferCapable = property(get_IsFileTransferCapable, None)
    IsGeoLocationPushCapable = property(get_IsGeoLocationPushCapable, None)
    IsIntegratedMessagingCapable = property(get_IsIntegratedMessagingCapable, None)
class ChatCapabilitiesManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.ChatCapabilitiesManager'
    @winrt_classmethod
    def GetCachedCapabilitiesForTransportAsync(cls: Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics2, address: WinRT_String, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_classmethod
    def GetCapabilitiesFromNetworkForTransportAsync(cls: Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics2, address: WinRT_String, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_classmethod
    def GetCachedCapabilitiesAsync(cls: Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics, address: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_classmethod
    def GetCapabilitiesFromNetworkAsync(cls: Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics, address: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
class ChatConversation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatConversation
    _classid_ = 'Windows.ApplicationModel.Chat.ChatConversation'
    @winrt_mixinmethod
    def get_HasUnreadMessages(self: Windows.ApplicationModel.Chat.IChatConversation) -> Boolean: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.Chat.IChatConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.ApplicationModel.Chat.IChatConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: Windows.ApplicationModel.Chat.IChatConversation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsConversationMuted(self: Windows.ApplicationModel.Chat.IChatConversation) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsConversationMuted(self: Windows.ApplicationModel.Chat.IChatConversation, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MostRecentMessageId(self: Windows.ApplicationModel.Chat.IChatConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Participants(self: Windows.ApplicationModel.Chat.IChatConversation) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ThreadingInfo(self: Windows.ApplicationModel.Chat.IChatConversation) -> Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.ApplicationModel.Chat.IChatConversation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMessageReader(self: Windows.ApplicationModel.Chat.IChatConversation) -> Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_mixinmethod
    def MarkAllMessagesAsReadAsync(self: Windows.ApplicationModel.Chat.IChatConversation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkMessagesAsReadAsync(self: Windows.ApplicationModel.Chat.IChatConversation, value: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.ApplicationModel.Chat.IChatConversation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NotifyLocalParticipantComposing(self: Windows.ApplicationModel.Chat.IChatConversation, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_mixinmethod
    def NotifyRemoteParticipantComposing(self: Windows.ApplicationModel.Chat.IChatConversation, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteParticipantComposingChanged(self: Windows.ApplicationModel.Chat.IChatConversation, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.ChatConversation, Windows.ApplicationModel.Chat.RemoteParticipantComposingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteParticipantComposingChanged(self: Windows.ApplicationModel.Chat.IChatConversation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CanModifyParticipants(self: Windows.ApplicationModel.Chat.IChatConversation2) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanModifyParticipants(self: Windows.ApplicationModel.Chat.IChatConversation2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ItemKind(self: Windows.ApplicationModel.Chat.IChatItem) -> Windows.ApplicationModel.Chat.ChatItemKind: ...
    HasUnreadMessages = property(get_HasUnreadMessages, None)
    Id = property(get_Id, None)
    Subject = property(get_Subject, put_Subject)
    IsConversationMuted = property(get_IsConversationMuted, put_IsConversationMuted)
    MostRecentMessageId = property(get_MostRecentMessageId, None)
    Participants = property(get_Participants, None)
    ThreadingInfo = property(get_ThreadingInfo, None)
    CanModifyParticipants = property(get_CanModifyParticipants, put_CanModifyParticipants)
    ItemKind = property(get_ItemKind, None)
class ChatConversationReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatConversationReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatConversationReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: Windows.ApplicationModel.Chat.IChatConversationReader) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatConversation]]: ...
    @winrt_mixinmethod
    def ReadBatchWithCountAsync(self: Windows.ApplicationModel.Chat.IChatConversationReader, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatConversation]]: ...
class ChatConversationThreadingInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo
    _classid_ = 'Windows.ApplicationModel.Chat.ChatConversationThreadingInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_mixinmethod
    def get_ContactId(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContactId(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Custom(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Custom(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ConversationId(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ConversationId(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Participants(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> Windows.ApplicationModel.Chat.ChatConversationThreadingKind: ...
    @winrt_mixinmethod
    def put_Kind(self: Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: Windows.ApplicationModel.Chat.ChatConversationThreadingKind) -> Void: ...
    ContactId = property(get_ContactId, put_ContactId)
    Custom = property(get_Custom, put_Custom)
    ConversationId = property(get_ConversationId, put_ConversationId)
    Participants = property(get_Participants, None)
    Kind = property(get_Kind, put_Kind)
ChatConversationThreadingKind = Int32
ChatConversationThreadingKind_Participants: ChatConversationThreadingKind = 0
ChatConversationThreadingKind_ContactId: ChatConversationThreadingKind = 1
ChatConversationThreadingKind_ConversationId: ChatConversationThreadingKind = 2
ChatConversationThreadingKind_Custom: ChatConversationThreadingKind = 3
ChatItemKind = Int32
ChatItemKind_Message: ChatItemKind = 0
ChatItemKind_Conversation: ChatItemKind = 1
class ChatMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessage
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessage'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Chat.ChatMessage: ...
    @winrt_mixinmethod
    def get_Attachments(self: Windows.ApplicationModel.Chat.IChatMessage) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Chat.ChatMessageAttachment]: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: Windows.ApplicationModel.Chat.IChatMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsForwardingDisabled(self: Windows.ApplicationModel.Chat.IChatMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsIncoming(self: Windows.ApplicationModel.Chat.IChatMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRead(self: Windows.ApplicationModel.Chat.IChatMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_LocalTimestamp(self: Windows.ApplicationModel.Chat.IChatMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NetworkTimestamp(self: Windows.ApplicationModel.Chat.IChatMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Recipients(self: Windows.ApplicationModel.Chat.IChatMessage) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RecipientSendStatuses(self: Windows.ApplicationModel.Chat.IChatMessage) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Chat.ChatMessageStatus]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Chat.IChatMessage) -> Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportFriendlyName(self: Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportId(self: Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TransportId(self: Windows.ApplicationModel.Chat.IChatMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EstimatedDownloadSize(self: Windows.ApplicationModel.Chat.IChatMessage2) -> UInt64: ...
    @winrt_mixinmethod
    def put_EstimatedDownloadSize(self: Windows.ApplicationModel.Chat.IChatMessage2, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def put_From(self: Windows.ApplicationModel.Chat.IChatMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsAutoReply(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAutoReply(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_IsForwardingDisabled(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsReplyDisabled(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIncoming(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_IsRead(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSeen(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSeen(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSimMessage(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_LocalTimestamp(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_MessageKind(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Windows.ApplicationModel.Chat.ChatMessageKind: ...
    @winrt_mixinmethod
    def put_MessageKind(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Windows.ApplicationModel.Chat.ChatMessageKind) -> Void: ...
    @winrt_mixinmethod
    def get_MessageOperatorKind(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Windows.ApplicationModel.Chat.ChatMessageOperatorKind: ...
    @winrt_mixinmethod
    def put_MessageOperatorKind(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Windows.ApplicationModel.Chat.ChatMessageOperatorKind) -> Void: ...
    @winrt_mixinmethod
    def put_NetworkTimestamp(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_IsReceivedDuringQuietHours(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsReceivedDuringQuietHours(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_RemoteId(self: Windows.ApplicationModel.Chat.IChatMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Windows.ApplicationModel.Chat.ChatMessageStatus) -> Void: ...
    @winrt_mixinmethod
    def put_Subject(self: Windows.ApplicationModel.Chat.IChatMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldSuppressNotification(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldSuppressNotification(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ThreadingInfo(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_mixinmethod
    def put_ThreadingInfo(self: Windows.ApplicationModel.Chat.IChatMessage2, value: Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> Void: ...
    @winrt_mixinmethod
    def get_RecipientsDeliveryInfos(self: Windows.ApplicationModel.Chat.IChatMessage2) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo]: ...
    @winrt_mixinmethod
    def get_RemoteId(self: Windows.ApplicationModel.Chat.IChatMessage3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SyncId(self: Windows.ApplicationModel.Chat.IChatMessage4) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SyncId(self: Windows.ApplicationModel.Chat.IChatMessage4, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ItemKind(self: Windows.ApplicationModel.Chat.IChatItem) -> Windows.ApplicationModel.Chat.ChatItemKind: ...
    Attachments = property(get_Attachments, None)
    Body = property(get_Body, put_Body)
    From = property(get_From, put_From)
    Id = property(get_Id, None)
    IsForwardingDisabled = property(get_IsForwardingDisabled, put_IsForwardingDisabled)
    IsIncoming = property(get_IsIncoming, put_IsIncoming)
    IsRead = property(get_IsRead, put_IsRead)
    LocalTimestamp = property(get_LocalTimestamp, put_LocalTimestamp)
    NetworkTimestamp = property(get_NetworkTimestamp, put_NetworkTimestamp)
    Recipients = property(get_Recipients, None)
    RecipientSendStatuses = property(get_RecipientSendStatuses, None)
    Status = property(get_Status, put_Status)
    Subject = property(get_Subject, put_Subject)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, put_TransportId)
    EstimatedDownloadSize = property(get_EstimatedDownloadSize, put_EstimatedDownloadSize)
    IsAutoReply = property(get_IsAutoReply, put_IsAutoReply)
    IsReplyDisabled = property(get_IsReplyDisabled, None)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsSimMessage = property(get_IsSimMessage, None)
    MessageKind = property(get_MessageKind, put_MessageKind)
    MessageOperatorKind = property(get_MessageOperatorKind, put_MessageOperatorKind)
    IsReceivedDuringQuietHours = property(get_IsReceivedDuringQuietHours, put_IsReceivedDuringQuietHours)
    RemoteId = property(get_RemoteId, put_RemoteId)
    ShouldSuppressNotification = property(get_ShouldSuppressNotification, put_ShouldSuppressNotification)
    ThreadingInfo = property(get_ThreadingInfo, put_ThreadingInfo)
    RecipientsDeliveryInfos = property(get_RecipientsDeliveryInfos, None)
    SyncId = property(get_SyncId, put_SyncId)
    ItemKind = property(get_ItemKind, None)
class ChatMessageAttachment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageAttachment
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageAttachment'
    @winrt_factorymethod
    def CreateChatMessageAttachment(cls: Windows.ApplicationModel.Chat.IChatMessageAttachmentFactory, mimeType: WinRT_String, dataStreamReference: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.ApplicationModel.Chat.ChatMessageAttachment: ...
    @winrt_mixinmethod
    def get_DataStreamReference(self: Windows.ApplicationModel.Chat.IChatMessageAttachment) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_DataStreamReference(self: Windows.ApplicationModel.Chat.IChatMessageAttachment, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_GroupId(self: Windows.ApplicationModel.Chat.IChatMessageAttachment) -> UInt32: ...
    @winrt_mixinmethod
    def put_GroupId(self: Windows.ApplicationModel.Chat.IChatMessageAttachment, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MimeType(self: Windows.ApplicationModel.Chat.IChatMessageAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MimeType(self: Windows.ApplicationModel.Chat.IChatMessageAttachment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.ApplicationModel.Chat.IChatMessageAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.ApplicationModel.Chat.IChatMessageAttachment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.ApplicationModel.Chat.IChatMessageAttachment2) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: Windows.ApplicationModel.Chat.IChatMessageAttachment2, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_TransferProgress(self: Windows.ApplicationModel.Chat.IChatMessageAttachment2) -> Double: ...
    @winrt_mixinmethod
    def put_TransferProgress(self: Windows.ApplicationModel.Chat.IChatMessageAttachment2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalFileName(self: Windows.ApplicationModel.Chat.IChatMessageAttachment2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OriginalFileName(self: Windows.ApplicationModel.Chat.IChatMessageAttachment2, value: WinRT_String) -> Void: ...
    DataStreamReference = property(get_DataStreamReference, put_DataStreamReference)
    GroupId = property(get_GroupId, put_GroupId)
    MimeType = property(get_MimeType, put_MimeType)
    Text = property(get_Text, put_Text)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TransferProgress = property(get_TransferProgress, put_TransferProgress)
    OriginalFileName = property(get_OriginalFileName, put_OriginalFileName)
class ChatMessageBlocking(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageBlocking'
    @winrt_classmethod
    def MarkMessageAsBlockedAsync(cls: Windows.ApplicationModel.Chat.IChatMessageBlockingStatic, localChatMessageId: WinRT_String, blocked: Boolean) -> Windows.Foundation.IAsyncAction: ...
class ChatMessageChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageChange
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChange'
    @winrt_mixinmethod
    def get_ChangeType(self: Windows.ApplicationModel.Chat.IChatMessageChange) -> Windows.ApplicationModel.Chat.ChatMessageChangeType: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.Chat.IChatMessageChange) -> Windows.ApplicationModel.Chat.ChatMessage: ...
    ChangeType = property(get_ChangeType, None)
    Message = property(get_Message, None)
class ChatMessageChangeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageChangeReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangeReader'
    @winrt_mixinmethod
    def AcceptChanges(self: Windows.ApplicationModel.Chat.IChatMessageChangeReader) -> Void: ...
    @winrt_mixinmethod
    def AcceptChangesThrough(self: Windows.ApplicationModel.Chat.IChatMessageChangeReader, lastChangeToAcknowledge: Windows.ApplicationModel.Chat.ChatMessageChange) -> Void: ...
    @winrt_mixinmethod
    def ReadBatchAsync(self: Windows.ApplicationModel.Chat.IChatMessageChangeReader) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessageChange]]: ...
class ChatMessageChangeTracker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageChangeTracker
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangeTracker'
    @winrt_mixinmethod
    def Enable(self: Windows.ApplicationModel.Chat.IChatMessageChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def GetChangeReader(self: Windows.ApplicationModel.Chat.IChatMessageChangeTracker) -> Windows.ApplicationModel.Chat.ChatMessageChangeReader: ...
    @winrt_mixinmethod
    def Reset(self: Windows.ApplicationModel.Chat.IChatMessageChangeTracker) -> Void: ...
ChatMessageChangeType = Int32
ChatMessageChangeType_MessageCreated: ChatMessageChangeType = 0
ChatMessageChangeType_MessageModified: ChatMessageChangeType = 1
ChatMessageChangeType_MessageDeleted: ChatMessageChangeType = 2
ChatMessageChangeType_ChangeTrackingLost: ChatMessageChangeType = 3
class ChatMessageChangedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageChangedDeferral
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.Chat.IChatMessageChangedDeferral) -> Void: ...
class ChatMessageChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Chat.IChatMessageChangedEventArgs) -> Windows.ApplicationModel.Chat.ChatMessageChangedDeferral: ...
ChatMessageKind = Int32
ChatMessageKind_Standard: ChatMessageKind = 0
ChatMessageKind_FileTransferRequest: ChatMessageKind = 1
ChatMessageKind_TransportCustom: ChatMessageKind = 2
ChatMessageKind_JoinedConversation: ChatMessageKind = 3
ChatMessageKind_LeftConversation: ChatMessageKind = 4
ChatMessageKind_OtherParticipantJoinedConversation: ChatMessageKind = 5
ChatMessageKind_OtherParticipantLeftConversation: ChatMessageKind = 6
class ChatMessageManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageManager'
    @winrt_classmethod
    def RequestSyncManagerAsync(cls: Windows.ApplicationModel.Chat.IChatMessageManagerStatics3) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatSyncManager]: ...
    @winrt_classmethod
    def RegisterTransportAsync(cls: Windows.ApplicationModel.Chat.IChatMessageManager2Statics) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetTransportAsync(cls: Windows.ApplicationModel.Chat.IChatMessageManager2Statics, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessageTransport]: ...
    @winrt_classmethod
    def GetTransportsAsync(cls: Windows.ApplicationModel.Chat.IChatMessageManagerStatic) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessageTransport]]: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: Windows.ApplicationModel.Chat.IChatMessageManagerStatic) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessageStore]: ...
    @winrt_classmethod
    def ShowComposeSmsMessageAsync(cls: Windows.ApplicationModel.Chat.IChatMessageManagerStatic, message: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowSmsSettings(cls: Windows.ApplicationModel.Chat.IChatMessageManagerStatic) -> Void: ...
class ChatMessageNotificationTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_ChatMessage(self: Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails) -> Windows.ApplicationModel.Chat.ChatMessage: ...
    @winrt_mixinmethod
    def get_ShouldDisplayToast(self: Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldUpdateDetailText(self: Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldUpdateBadge(self: Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldUpdateActionCenter(self: Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    ChatMessage = property(get_ChatMessage, None)
    ShouldDisplayToast = property(get_ShouldDisplayToast, None)
    ShouldUpdateDetailText = property(get_ShouldUpdateDetailText, None)
    ShouldUpdateBadge = property(get_ShouldUpdateBadge, None)
    ShouldUpdateActionCenter = property(get_ShouldUpdateActionCenter, None)
ChatMessageOperatorKind = Int32
ChatMessageOperatorKind_Unspecified: ChatMessageOperatorKind = 0
ChatMessageOperatorKind_Sms: ChatMessageOperatorKind = 1
ChatMessageOperatorKind_Mms: ChatMessageOperatorKind = 2
ChatMessageOperatorKind_Rcs: ChatMessageOperatorKind = 3
class ChatMessageReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: Windows.ApplicationModel.Chat.IChatMessageReader) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessage]]: ...
    @winrt_mixinmethod
    def ReadBatchWithCountAsync(self: Windows.ApplicationModel.Chat.IChatMessageReader2, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessage]]: ...
ChatMessageStatus = Int32
ChatMessageStatus_Draft: ChatMessageStatus = 0
ChatMessageStatus_Sending: ChatMessageStatus = 1
ChatMessageStatus_Sent: ChatMessageStatus = 2
ChatMessageStatus_SendRetryNeeded: ChatMessageStatus = 3
ChatMessageStatus_SendFailed: ChatMessageStatus = 4
ChatMessageStatus_Received: ChatMessageStatus = 5
ChatMessageStatus_ReceiveDownloadNeeded: ChatMessageStatus = 6
ChatMessageStatus_ReceiveDownloadFailed: ChatMessageStatus = 7
ChatMessageStatus_ReceiveDownloading: ChatMessageStatus = 8
ChatMessageStatus_Deleted: ChatMessageStatus = 9
ChatMessageStatus_Declined: ChatMessageStatus = 10
ChatMessageStatus_Cancelled: ChatMessageStatus = 11
ChatMessageStatus_Recalled: ChatMessageStatus = 12
ChatMessageStatus_ReceiveRetryNeeded: ChatMessageStatus = 13
class ChatMessageStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageStore
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageStore'
    @winrt_mixinmethod
    def get_ChangeTracker(self: Windows.ApplicationModel.Chat.IChatMessageStore) -> Windows.ApplicationModel.Chat.ChatMessageChangeTracker: ...
    @winrt_mixinmethod
    def DeleteMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore, localMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DownloadMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_mixinmethod
    def GetMessageReader1(self: Windows.ApplicationModel.Chat.IChatMessageStore) -> Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_mixinmethod
    def GetMessageReader2(self: Windows.ApplicationModel.Chat.IChatMessageStore, recentTimeLimit: Windows.Foundation.TimeSpan) -> Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_mixinmethod
    def MarkMessageReadAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RetrySendMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore, chatMessage: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ValidateMessage(self: Windows.ApplicationModel.Chat.IChatMessageStore, chatMessage: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.ApplicationModel.Chat.ChatMessageValidationResult: ...
    @winrt_mixinmethod
    def add_MessageChanged(self: Windows.ApplicationModel.Chat.IChatMessageStore, value: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.ChatMessageStore, Windows.ApplicationModel.Chat.ChatMessageChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageChanged(self: Windows.ApplicationModel.Chat.IChatMessageStore, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ForwardMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, localChatMessageId: WinRT_String, addresses: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_mixinmethod
    def GetConversationAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, conversationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_mixinmethod
    def GetConversationForTransportsAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, conversationId: WinRT_String, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_mixinmethod
    def GetConversationFromThreadingInfoAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, threadingInfo: Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_mixinmethod
    def GetConversationReader(self: Windows.ApplicationModel.Chat.IChatMessageStore2) -> Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_mixinmethod
    def GetConversationForTransportsReader(self: Windows.ApplicationModel.Chat.IChatMessageStore2, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_mixinmethod
    def GetMessageByRemoteIdAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, transportId: WinRT_String, remoteId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_mixinmethod
    def GetUnseenCountAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def GetUnseenCountForTransportsReaderAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def MarkAsSeenAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkAsSeenForTransportsAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetSearchReader(self: Windows.ApplicationModel.Chat.IChatMessageStore2, value: Windows.ApplicationModel.Chat.ChatQueryOptions) -> Windows.ApplicationModel.Chat.ChatSearchReader: ...
    @winrt_mixinmethod
    def SaveMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, chatMessage: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TryCancelDownloadMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryCancelSendMessageAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore2, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_StoreChanged(self: Windows.ApplicationModel.Chat.IChatMessageStore2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.ChatMessageStore, Windows.ApplicationModel.Chat.ChatMessageStoreChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StoreChanged(self: Windows.ApplicationModel.Chat.IChatMessageStore2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetMessageBySyncIdAsync(self: Windows.ApplicationModel.Chat.IChatMessageStore3, syncId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    ChangeTracker = property(get_ChangeTracker, None)
class ChatMessageStoreChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageStoreChangedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs) -> Windows.ApplicationModel.Chat.ChatStoreChangedEventKind: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class ChatMessageTransport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageTransport
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageTransport'
    @winrt_mixinmethod
    def get_IsAppSetAsNotificationProvider(self: Windows.ApplicationModel.Chat.IChatMessageTransport) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.ApplicationModel.Chat.IChatMessageTransport) -> Boolean: ...
    @winrt_mixinmethod
    def get_TransportFriendlyName(self: Windows.ApplicationModel.Chat.IChatMessageTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportId(self: Windows.ApplicationModel.Chat.IChatMessageTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestSetAsNotificationProviderAsync(self: Windows.ApplicationModel.Chat.IChatMessageTransport) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Configuration(self: Windows.ApplicationModel.Chat.IChatMessageTransport2) -> Windows.ApplicationModel.Chat.ChatMessageTransportConfiguration: ...
    @winrt_mixinmethod
    def get_TransportKind(self: Windows.ApplicationModel.Chat.IChatMessageTransport2) -> Windows.ApplicationModel.Chat.ChatMessageTransportKind: ...
    IsAppSetAsNotificationProvider = property(get_IsAppSetAsNotificationProvider, None)
    IsActive = property(get_IsActive, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
    Configuration = property(get_Configuration, None)
    TransportKind = property(get_TransportKind, None)
class ChatMessageTransportConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageTransportConfiguration'
    @winrt_mixinmethod
    def get_MaxAttachmentCount(self: Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxMessageSizeInKilobytes(self: Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxRecipientCount(self: Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_SupportedVideoFormat(self: Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    SupportedVideoFormat = property(get_SupportedVideoFormat, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
ChatMessageTransportKind = Int32
ChatMessageTransportKind_Text: ChatMessageTransportKind = 0
ChatMessageTransportKind_Untriaged: ChatMessageTransportKind = 1
ChatMessageTransportKind_Blocked: ChatMessageTransportKind = 2
ChatMessageTransportKind_Custom: ChatMessageTransportKind = 3
class ChatMessageValidationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatMessageValidationResult
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageValidationResult'
    @winrt_mixinmethod
    def get_MaxPartCount(self: Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_PartCount(self: Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_RemainingCharacterCountInPart(self: Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> Windows.ApplicationModel.Chat.ChatMessageValidationStatus: ...
    MaxPartCount = property(get_MaxPartCount, None)
    PartCount = property(get_PartCount, None)
    RemainingCharacterCountInPart = property(get_RemainingCharacterCountInPart, None)
    Status = property(get_Status, None)
ChatMessageValidationStatus = Int32
ChatMessageValidationStatus_Valid: ChatMessageValidationStatus = 0
ChatMessageValidationStatus_NoRecipients: ChatMessageValidationStatus = 1
ChatMessageValidationStatus_InvalidData: ChatMessageValidationStatus = 2
ChatMessageValidationStatus_MessageTooLarge: ChatMessageValidationStatus = 3
ChatMessageValidationStatus_TooManyRecipients: ChatMessageValidationStatus = 4
ChatMessageValidationStatus_TransportInactive: ChatMessageValidationStatus = 5
ChatMessageValidationStatus_TransportNotFound: ChatMessageValidationStatus = 6
ChatMessageValidationStatus_TooManyAttachments: ChatMessageValidationStatus = 7
ChatMessageValidationStatus_InvalidRecipients: ChatMessageValidationStatus = 8
ChatMessageValidationStatus_InvalidBody: ChatMessageValidationStatus = 9
ChatMessageValidationStatus_InvalidOther: ChatMessageValidationStatus = 10
ChatMessageValidationStatus_ValidWithLargeMessage: ChatMessageValidationStatus = 11
ChatMessageValidationStatus_VoiceRoamingRestriction: ChatMessageValidationStatus = 12
ChatMessageValidationStatus_DataRoamingRestriction: ChatMessageValidationStatus = 13
class ChatQueryOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatQueryOptions
    _classid_ = 'Windows.ApplicationModel.Chat.ChatQueryOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Chat.ChatQueryOptions: ...
    @winrt_mixinmethod
    def get_SearchString(self: Windows.ApplicationModel.Chat.IChatQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SearchString(self: Windows.ApplicationModel.Chat.IChatQueryOptions, value: WinRT_String) -> Void: ...
    SearchString = property(get_SearchString, put_SearchString)
class ChatRecipientDeliveryInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo
    _classid_ = 'Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo: ...
    @winrt_mixinmethod
    def get_TransportAddress(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TransportAddress(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeliveryTime(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DeliveryTime(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ReadTime(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ReadTime(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_TransportErrorCodeCategory(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Windows.ApplicationModel.Chat.ChatTransportErrorCodeCategory: ...
    @winrt_mixinmethod
    def get_TransportInterpretedErrorCode(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Windows.ApplicationModel.Chat.ChatTransportInterpretedErrorCode: ...
    @winrt_mixinmethod
    def get_TransportErrorCode(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_IsErrorPermanent(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    TransportAddress = property(get_TransportAddress, put_TransportAddress)
    DeliveryTime = property(get_DeliveryTime, put_DeliveryTime)
    ReadTime = property(get_ReadTime, put_ReadTime)
    TransportErrorCodeCategory = property(get_TransportErrorCodeCategory, None)
    TransportInterpretedErrorCode = property(get_TransportInterpretedErrorCode, None)
    TransportErrorCode = property(get_TransportErrorCode, None)
    IsErrorPermanent = property(get_IsErrorPermanent, None)
    Status = property(get_Status, None)
ChatRestoreHistorySpan = Int32
ChatRestoreHistorySpan_LastMonth: ChatRestoreHistorySpan = 0
ChatRestoreHistorySpan_LastYear: ChatRestoreHistorySpan = 1
ChatRestoreHistorySpan_AnyTime: ChatRestoreHistorySpan = 2
class ChatSearchReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatSearchReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatSearchReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: Windows.ApplicationModel.Chat.IChatSearchReader) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.IChatItem]]: ...
    @winrt_mixinmethod
    def ReadBatchWithCountAsync(self: Windows.ApplicationModel.Chat.IChatSearchReader, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.IChatItem]]: ...
ChatStoreChangedEventKind = Int32
ChatStoreChangedEventKind_NotificationsMissed: ChatStoreChangedEventKind = 0
ChatStoreChangedEventKind_StoreModified: ChatStoreChangedEventKind = 1
ChatStoreChangedEventKind_MessageCreated: ChatStoreChangedEventKind = 2
ChatStoreChangedEventKind_MessageModified: ChatStoreChangedEventKind = 3
ChatStoreChangedEventKind_MessageDeleted: ChatStoreChangedEventKind = 4
ChatStoreChangedEventKind_ConversationModified: ChatStoreChangedEventKind = 5
ChatStoreChangedEventKind_ConversationDeleted: ChatStoreChangedEventKind = 6
ChatStoreChangedEventKind_ConversationTransportDeleted: ChatStoreChangedEventKind = 7
class ChatSyncConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatSyncConfiguration
    _classid_ = 'Windows.ApplicationModel.Chat.ChatSyncConfiguration'
    @winrt_mixinmethod
    def get_IsSyncEnabled(self: Windows.ApplicationModel.Chat.IChatSyncConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSyncEnabled(self: Windows.ApplicationModel.Chat.IChatSyncConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RestoreHistorySpan(self: Windows.ApplicationModel.Chat.IChatSyncConfiguration) -> Windows.ApplicationModel.Chat.ChatRestoreHistorySpan: ...
    @winrt_mixinmethod
    def put_RestoreHistorySpan(self: Windows.ApplicationModel.Chat.IChatSyncConfiguration, value: Windows.ApplicationModel.Chat.ChatRestoreHistorySpan) -> Void: ...
    IsSyncEnabled = property(get_IsSyncEnabled, put_IsSyncEnabled)
    RestoreHistorySpan = property(get_RestoreHistorySpan, put_RestoreHistorySpan)
class ChatSyncManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IChatSyncManager
    _classid_ = 'Windows.ApplicationModel.Chat.ChatSyncManager'
    @winrt_mixinmethod
    def get_Configuration(self: Windows.ApplicationModel.Chat.IChatSyncManager) -> Windows.ApplicationModel.Chat.ChatSyncConfiguration: ...
    @winrt_mixinmethod
    def AssociateAccountAsync(self: Windows.ApplicationModel.Chat.IChatSyncManager, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnassociateAccountAsync(self: Windows.ApplicationModel.Chat.IChatSyncManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def IsAccountAssociated(self: Windows.ApplicationModel.Chat.IChatSyncManager, webAccount: Windows.Security.Credentials.WebAccount) -> Boolean: ...
    @winrt_mixinmethod
    def StartSync(self: Windows.ApplicationModel.Chat.IChatSyncManager) -> Void: ...
    @winrt_mixinmethod
    def SetConfigurationAsync(self: Windows.ApplicationModel.Chat.IChatSyncManager, configuration: Windows.ApplicationModel.Chat.ChatSyncConfiguration) -> Windows.Foundation.IAsyncAction: ...
    Configuration = property(get_Configuration, None)
ChatTransportErrorCodeCategory = Int32
ChatTransportErrorCodeCategory_None: ChatTransportErrorCodeCategory = 0
ChatTransportErrorCodeCategory_Http: ChatTransportErrorCodeCategory = 1
ChatTransportErrorCodeCategory_Network: ChatTransportErrorCodeCategory = 2
ChatTransportErrorCodeCategory_MmsServer: ChatTransportErrorCodeCategory = 3
ChatTransportInterpretedErrorCode = Int32
ChatTransportInterpretedErrorCode_None: ChatTransportInterpretedErrorCode = 0
ChatTransportInterpretedErrorCode_Unknown: ChatTransportInterpretedErrorCode = 1
ChatTransportInterpretedErrorCode_InvalidRecipientAddress: ChatTransportInterpretedErrorCode = 2
ChatTransportInterpretedErrorCode_NetworkConnectivity: ChatTransportInterpretedErrorCode = 3
ChatTransportInterpretedErrorCode_ServiceDenied: ChatTransportInterpretedErrorCode = 4
ChatTransportInterpretedErrorCode_Timeout: ChatTransportInterpretedErrorCode = 5
class IChatCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatCapabilities'
    _iid_ = Guid('{3aff77bc-39c9-4dd1-ad2d-3964dd9d403f}')
    @winrt_commethod(6)
    def get_IsOnline(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsChatCapable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsFileTransferCapable(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsGeoLocationPushCapable(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsIntegratedMessagingCapable(self) -> Boolean: ...
    IsOnline = property(get_IsOnline, None)
    IsChatCapable = property(get_IsChatCapable, None)
    IsFileTransferCapable = property(get_IsFileTransferCapable, None)
    IsGeoLocationPushCapable = property(get_IsGeoLocationPushCapable, None)
    IsIntegratedMessagingCapable = property(get_IsIntegratedMessagingCapable, None)
class IChatCapabilitiesManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics'
    _iid_ = Guid('{b57a2f30-7041-458e-b0cf-7c0d9fea333a}')
    @winrt_commethod(6)
    def GetCachedCapabilitiesAsync(self, address: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_commethod(7)
    def GetCapabilitiesFromNetworkAsync(self, address: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
class IChatCapabilitiesManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics2'
    _iid_ = Guid('{e30d4274-d5c1-4ac9-9ffc-40e69184fec8}')
    @winrt_commethod(6)
    def GetCachedCapabilitiesForTransportAsync(self, address: WinRT_String, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_commethod(7)
    def GetCapabilitiesFromNetworkForTransportAsync(self, address: WinRT_String, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatCapabilities]: ...
class IChatConversation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatConversation'
    _iid_ = Guid('{a58c080d-1a6f-46dc-8f3d-f5028660b6ee}')
    @winrt_commethod(6)
    def get_HasUnreadMessages(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Subject(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_IsConversationMuted(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsConversationMuted(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_MostRecentMessageId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Participants(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(14)
    def get_ThreadingInfo(self) -> Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_commethod(15)
    def DeleteAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def GetMessageReader(self) -> Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_commethod(17)
    def MarkAllMessagesAsReadAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def MarkMessagesAsReadAsync(self, value: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def SaveAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def NotifyLocalParticipantComposing(self, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_commethod(21)
    def NotifyRemoteParticipantComposing(self, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_commethod(22)
    def add_RemoteParticipantComposingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.ChatConversation, Windows.ApplicationModel.Chat.RemoteParticipantComposingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_RemoteParticipantComposingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HasUnreadMessages = property(get_HasUnreadMessages, None)
    Id = property(get_Id, None)
    Subject = property(get_Subject, put_Subject)
    IsConversationMuted = property(get_IsConversationMuted, put_IsConversationMuted)
    MostRecentMessageId = property(get_MostRecentMessageId, None)
    Participants = property(get_Participants, None)
    ThreadingInfo = property(get_ThreadingInfo, None)
class IChatConversation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatConversation2'
    _iid_ = Guid('{0a030cd1-983a-47aa-9a90-ee48ee997b59}')
    @winrt_commethod(6)
    def get_CanModifyParticipants(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanModifyParticipants(self, value: Boolean) -> Void: ...
    CanModifyParticipants = property(get_CanModifyParticipants, put_CanModifyParticipants)
class IChatConversationReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatConversationReader'
    _iid_ = Guid('{055136d2-de32-4a47-a93a-b3dc0833852b}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatConversation]]: ...
    @winrt_commethod(7)
    def ReadBatchWithCountAsync(self, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatConversation]]: ...
class IChatConversationThreadingInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatConversationThreadingInfo'
    _iid_ = Guid('{331c21dc-7a07-4422-a32c-24be7c6dab24}')
    @winrt_commethod(6)
    def get_ContactId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ContactId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Custom(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Custom(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ConversationId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ConversationId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Participants(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Kind(self) -> Windows.ApplicationModel.Chat.ChatConversationThreadingKind: ...
    @winrt_commethod(14)
    def put_Kind(self, value: Windows.ApplicationModel.Chat.ChatConversationThreadingKind) -> Void: ...
    ContactId = property(get_ContactId, put_ContactId)
    Custom = property(get_Custom, put_Custom)
    ConversationId = property(get_ConversationId, put_ConversationId)
    Participants = property(get_Participants, None)
    Kind = property(get_Kind, put_Kind)
class IChatItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatItem'
    _iid_ = Guid('{8751d000-ceb1-4243-b803-15d45a1dd428}')
    @winrt_commethod(6)
    def get_ItemKind(self) -> Windows.ApplicationModel.Chat.ChatItemKind: ...
    ItemKind = property(get_ItemKind, None)
class IChatMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage'
    _iid_ = Guid('{4b39052a-1142-5089-76da-f2db3d17cd05}')
    @winrt_commethod(6)
    def get_Attachments(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Chat.ChatMessageAttachment]: ...
    @winrt_commethod(7)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_IsForwardingDisabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsIncoming(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsRead(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_LocalTimestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def get_NetworkTimestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(16)
    def get_Recipients(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(17)
    def get_RecipientSendStatuses(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Chat.ChatMessageStatus]: ...
    @winrt_commethod(18)
    def get_Status(self) -> Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    @winrt_commethod(19)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_TransportFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def put_TransportId(self, value: WinRT_String) -> Void: ...
    Attachments = property(get_Attachments, None)
    Body = property(get_Body, put_Body)
    From = property(get_From, None)
    Id = property(get_Id, None)
    IsForwardingDisabled = property(get_IsForwardingDisabled, None)
    IsIncoming = property(get_IsIncoming, None)
    IsRead = property(get_IsRead, None)
    LocalTimestamp = property(get_LocalTimestamp, None)
    NetworkTimestamp = property(get_NetworkTimestamp, None)
    Recipients = property(get_Recipients, None)
    RecipientSendStatuses = property(get_RecipientSendStatuses, None)
    Status = property(get_Status, None)
    Subject = property(get_Subject, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, put_TransportId)
class IChatMessage2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage2'
    _iid_ = Guid('{86668332-543f-49f5-ac71-6c2afc6565fd}')
    @winrt_commethod(6)
    def get_EstimatedDownloadSize(self) -> UInt64: ...
    @winrt_commethod(7)
    def put_EstimatedDownloadSize(self, value: UInt64) -> Void: ...
    @winrt_commethod(8)
    def put_From(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_IsAutoReply(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsAutoReply(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def put_IsForwardingDisabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsReplyDisabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsIncoming(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def put_IsRead(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_IsSeen(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_IsSeen(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_IsSimMessage(self) -> Boolean: ...
    @winrt_commethod(18)
    def put_LocalTimestamp(self, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(19)
    def get_MessageKind(self) -> Windows.ApplicationModel.Chat.ChatMessageKind: ...
    @winrt_commethod(20)
    def put_MessageKind(self, value: Windows.ApplicationModel.Chat.ChatMessageKind) -> Void: ...
    @winrt_commethod(21)
    def get_MessageOperatorKind(self) -> Windows.ApplicationModel.Chat.ChatMessageOperatorKind: ...
    @winrt_commethod(22)
    def put_MessageOperatorKind(self, value: Windows.ApplicationModel.Chat.ChatMessageOperatorKind) -> Void: ...
    @winrt_commethod(23)
    def put_NetworkTimestamp(self, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(24)
    def get_IsReceivedDuringQuietHours(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_IsReceivedDuringQuietHours(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(27)
    def put_Status(self, value: Windows.ApplicationModel.Chat.ChatMessageStatus) -> Void: ...
    @winrt_commethod(28)
    def put_Subject(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(29)
    def get_ShouldSuppressNotification(self) -> Boolean: ...
    @winrt_commethod(30)
    def put_ShouldSuppressNotification(self, value: Boolean) -> Void: ...
    @winrt_commethod(31)
    def get_ThreadingInfo(self) -> Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_commethod(32)
    def put_ThreadingInfo(self, value: Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> Void: ...
    @winrt_commethod(33)
    def get_RecipientsDeliveryInfos(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo]: ...
    EstimatedDownloadSize = property(get_EstimatedDownloadSize, put_EstimatedDownloadSize)
    From = property(None, put_From)
    IsAutoReply = property(get_IsAutoReply, put_IsAutoReply)
    IsForwardingDisabled = property(None, put_IsForwardingDisabled)
    IsReplyDisabled = property(get_IsReplyDisabled, None)
    IsIncoming = property(None, put_IsIncoming)
    IsRead = property(None, put_IsRead)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsSimMessage = property(get_IsSimMessage, None)
    LocalTimestamp = property(None, put_LocalTimestamp)
    MessageKind = property(get_MessageKind, put_MessageKind)
    MessageOperatorKind = property(get_MessageOperatorKind, put_MessageOperatorKind)
    NetworkTimestamp = property(None, put_NetworkTimestamp)
    IsReceivedDuringQuietHours = property(get_IsReceivedDuringQuietHours, put_IsReceivedDuringQuietHours)
    RemoteId = property(None, put_RemoteId)
    Status = property(None, put_Status)
    Subject = property(None, put_Subject)
    ShouldSuppressNotification = property(get_ShouldSuppressNotification, put_ShouldSuppressNotification)
    ThreadingInfo = property(get_ThreadingInfo, put_ThreadingInfo)
    RecipientsDeliveryInfos = property(get_RecipientsDeliveryInfos, None)
class IChatMessage3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage3'
    _iid_ = Guid('{74eb2fb0-3ba7-459f-8e0b-e8af0febd9ad}')
    @winrt_commethod(6)
    def get_RemoteId(self) -> WinRT_String: ...
    RemoteId = property(get_RemoteId, None)
class IChatMessage4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage4'
    _iid_ = Guid('{2d144b0f-d2bf-460c-aa68-6d3f8483c9bf}')
    @winrt_commethod(6)
    def get_SyncId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SyncId(self, value: WinRT_String) -> Void: ...
    SyncId = property(get_SyncId, put_SyncId)
class IChatMessageAttachment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageAttachment'
    _iid_ = Guid('{c7c4fd74-bf63-58eb-508c-8b863ff16b67}')
    @winrt_commethod(6)
    def get_DataStreamReference(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_DataStreamReference(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def get_GroupId(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_GroupId(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_MimeType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_MimeType(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Text(self, value: WinRT_String) -> Void: ...
    DataStreamReference = property(get_DataStreamReference, put_DataStreamReference)
    GroupId = property(get_GroupId, put_GroupId)
    MimeType = property(get_MimeType, put_MimeType)
    Text = property(get_Text, put_Text)
class IChatMessageAttachment2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageAttachment2'
    _iid_ = Guid('{5ed99270-7dd1-4a87-a8ce-acdd87d80dc8}')
    @winrt_commethod(6)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_Thumbnail(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def get_TransferProgress(self) -> Double: ...
    @winrt_commethod(9)
    def put_TransferProgress(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_OriginalFileName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_OriginalFileName(self, value: WinRT_String) -> Void: ...
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TransferProgress = property(get_TransferProgress, put_TransferProgress)
    OriginalFileName = property(get_OriginalFileName, put_OriginalFileName)
class IChatMessageAttachmentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageAttachmentFactory'
    _iid_ = Guid('{205852a2-a356-5b71-6ca9-66c985b7d0d5}')
    @winrt_commethod(6)
    def CreateChatMessageAttachment(self, mimeType: WinRT_String, dataStreamReference: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.ApplicationModel.Chat.ChatMessageAttachment: ...
class IChatMessageBlockingStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageBlockingStatic'
    _iid_ = Guid('{f6b9a380-cdea-11e4-8830-0800200c9a66}')
    @winrt_commethod(6)
    def MarkMessageAsBlockedAsync(self, localChatMessageId: WinRT_String, blocked: Boolean) -> Windows.Foundation.IAsyncAction: ...
class IChatMessageChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChange'
    _iid_ = Guid('{1c18c355-421e-54b8-6d38-6b3a6c82fccc}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> Windows.ApplicationModel.Chat.ChatMessageChangeType: ...
    @winrt_commethod(7)
    def get_Message(self) -> Windows.ApplicationModel.Chat.ChatMessage: ...
    ChangeType = property(get_ChangeType, None)
    Message = property(get_Message, None)
class IChatMessageChangeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangeReader'
    _iid_ = Guid('{14267020-28ce-5f26-7b05-9a5c7cce87ca}')
    @winrt_commethod(6)
    def AcceptChanges(self) -> Void: ...
    @winrt_commethod(7)
    def AcceptChangesThrough(self, lastChangeToAcknowledge: Windows.ApplicationModel.Chat.ChatMessageChange) -> Void: ...
    @winrt_commethod(8)
    def ReadBatchAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessageChange]]: ...
class IChatMessageChangeTracker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangeTracker'
    _iid_ = Guid('{60b7f066-70a0-5224-508c-242ef7c1d06f}')
    @winrt_commethod(6)
    def Enable(self) -> Void: ...
    @winrt_commethod(7)
    def GetChangeReader(self) -> Windows.ApplicationModel.Chat.ChatMessageChangeReader: ...
    @winrt_commethod(8)
    def Reset(self) -> Void: ...
class IChatMessageChangedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangedDeferral'
    _iid_ = Guid('{fbc6b30c-788c-4dcc-ace7-6282382968cf}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IChatMessageChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangedEventArgs'
    _iid_ = Guid('{b6b73e2d-691c-4edf-8660-6eb9896892e3}')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.ApplicationModel.Chat.ChatMessageChangedDeferral: ...
class IChatMessageManager2Statics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageManager2Statics'
    _iid_ = Guid('{1d45390f-9f4f-4e35-964e-1b9ca61ac044}')
    @winrt_commethod(6)
    def RegisterTransportAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def GetTransportAsync(self, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessageTransport]: ...
class IChatMessageManagerStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageManagerStatic'
    _iid_ = Guid('{f15c60f7-d5e8-5e92-556d-e03b60253104}')
    @winrt_commethod(6)
    def GetTransportsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessageTransport]]: ...
    @winrt_commethod(7)
    def RequestStoreAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessageStore]: ...
    @winrt_commethod(8)
    def ShowComposeSmsMessageAsync(self, message: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ShowSmsSettings(self) -> Void: ...
class IChatMessageManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageManagerStatics3'
    _iid_ = Guid('{208b830d-6755-48cc-9ab3-fd03c463fc92}')
    @winrt_commethod(6)
    def RequestSyncManagerAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatSyncManager]: ...
class IChatMessageNotificationTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails'
    _iid_ = Guid('{fd344dfb-3063-4e17-8586-c6c08262e6c0}')
    @winrt_commethod(6)
    def get_ChatMessage(self) -> Windows.ApplicationModel.Chat.ChatMessage: ...
    ChatMessage = property(get_ChatMessage, None)
class IChatMessageNotificationTriggerDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2'
    _iid_ = Guid('{6bb522e0-aa07-4fd1-9471-77934fb75ee6}')
    @winrt_commethod(6)
    def get_ShouldDisplayToast(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ShouldUpdateDetailText(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ShouldUpdateBadge(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ShouldUpdateActionCenter(self) -> Boolean: ...
    ShouldDisplayToast = property(get_ShouldDisplayToast, None)
    ShouldUpdateDetailText = property(get_ShouldUpdateDetailText, None)
    ShouldUpdateBadge = property(get_ShouldUpdateBadge, None)
    ShouldUpdateActionCenter = property(get_ShouldUpdateActionCenter, None)
class IChatMessageReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageReader'
    _iid_ = Guid('{b6ea78ce-4489-56f9-76aa-e204682514cf}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessage]]: ...
class IChatMessageReader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageReader2'
    _iid_ = Guid('{89643683-64bb-470d-9df4-0de8be1a05bf}')
    @winrt_commethod(6)
    def ReadBatchWithCountAsync(self, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.ChatMessage]]: ...
class IChatMessageStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStore'
    _iid_ = Guid('{31f2fd01-ccf6-580b-4976-0a07dd5d3b47}')
    @winrt_commethod(6)
    def get_ChangeTracker(self) -> Windows.ApplicationModel.Chat.ChatMessageChangeTracker: ...
    @winrt_commethod(7)
    def DeleteMessageAsync(self, localMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DownloadMessageAsync(self, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def GetMessageAsync(self, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_commethod(10)
    def GetMessageReader1(self) -> Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_commethod(11)
    def GetMessageReader2(self, recentTimeLimit: Windows.Foundation.TimeSpan) -> Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_commethod(12)
    def MarkMessageReadAsync(self, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def RetrySendMessageAsync(self, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def SendMessageAsync(self, chatMessage: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def ValidateMessage(self, chatMessage: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.ApplicationModel.Chat.ChatMessageValidationResult: ...
    @winrt_commethod(16)
    def add_MessageChanged(self, value: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.ChatMessageStore, Windows.ApplicationModel.Chat.ChatMessageChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MessageChanged(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ChangeTracker = property(get_ChangeTracker, None)
class IChatMessageStore2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStore2'
    _iid_ = Guid('{ad4dc4ee-3ad4-491b-b311-abdf9bb22768}')
    @winrt_commethod(6)
    def ForwardMessageAsync(self, localChatMessageId: WinRT_String, addresses: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_commethod(7)
    def GetConversationAsync(self, conversationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_commethod(8)
    def GetConversationForTransportsAsync(self, conversationId: WinRT_String, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_commethod(9)
    def GetConversationFromThreadingInfoAsync(self, threadingInfo: Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_commethod(10)
    def GetConversationReader(self) -> Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_commethod(11)
    def GetConversationForTransportsReader(self, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_commethod(12)
    def GetMessageByRemoteIdAsync(self, transportId: WinRT_String, remoteId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_commethod(13)
    def GetUnseenCountAsync(self) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(14)
    def GetUnseenCountForTransportsReaderAsync(self, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(15)
    def MarkAsSeenAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def MarkAsSeenForTransportsAsync(self, transportIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def GetSearchReader(self, value: Windows.ApplicationModel.Chat.ChatQueryOptions) -> Windows.ApplicationModel.Chat.ChatSearchReader: ...
    @winrt_commethod(18)
    def SaveMessageAsync(self, chatMessage: Windows.ApplicationModel.Chat.ChatMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def TryCancelDownloadMessageAsync(self, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(20)
    def TryCancelSendMessageAsync(self, localChatMessageId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def add_StoreChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.ChatMessageStore, Windows.ApplicationModel.Chat.ChatMessageStoreChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_StoreChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IChatMessageStore3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStore3'
    _iid_ = Guid('{9adbbb09-4345-4ec1-8b74-b7338243719c}')
    @winrt_commethod(6)
    def GetMessageBySyncIdAsync(self, syncId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.ChatMessage]: ...
class IChatMessageStoreChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs'
    _iid_ = Guid('{65c66fac-fe8c-46d4-9119-57b8410311d5}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.ApplicationModel.Chat.ChatStoreChangedEventKind: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class IChatMessageTransport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageTransport'
    _iid_ = Guid('{63a9dbf8-e6b3-5c9a-5f85-d47925b9bd18}')
    @winrt_commethod(6)
    def get_IsAppSetAsNotificationProvider(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_TransportFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def RequestSetAsNotificationProviderAsync(self) -> Windows.Foundation.IAsyncAction: ...
    IsAppSetAsNotificationProvider = property(get_IsAppSetAsNotificationProvider, None)
    IsActive = property(get_IsActive, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
class IChatMessageTransport2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageTransport2'
    _iid_ = Guid('{90a75622-d84a-4c22-a94d-544444edc8a1}')
    @winrt_commethod(6)
    def get_Configuration(self) -> Windows.ApplicationModel.Chat.ChatMessageTransportConfiguration: ...
    @winrt_commethod(7)
    def get_TransportKind(self) -> Windows.ApplicationModel.Chat.ChatMessageTransportKind: ...
    Configuration = property(get_Configuration, None)
    TransportKind = property(get_TransportKind, None)
class IChatMessageTransportConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration'
    _iid_ = Guid('{879ff725-1a08-4aca-a075-3355126312e6}')
    @winrt_commethod(6)
    def get_MaxAttachmentCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_MaxMessageSizeInKilobytes(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MaxRecipientCount(self) -> Int32: ...
    @winrt_commethod(9)
    def get_SupportedVideoFormat(self) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(10)
    def get_ExtendedProperties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    SupportedVideoFormat = property(get_SupportedVideoFormat, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
class IChatMessageValidationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageValidationResult'
    _iid_ = Guid('{25e93a03-28ec-5889-569b-7e486b126f18}')
    @winrt_commethod(6)
    def get_MaxPartCount(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def get_PartCount(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_RemainingCharacterCountInPart(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_Status(self) -> Windows.ApplicationModel.Chat.ChatMessageValidationStatus: ...
    MaxPartCount = property(get_MaxPartCount, None)
    PartCount = property(get_PartCount, None)
    RemainingCharacterCountInPart = property(get_RemainingCharacterCountInPart, None)
    Status = property(get_Status, None)
class IChatQueryOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatQueryOptions'
    _iid_ = Guid('{2fd364a6-bf36-42f7-b7e7-923c0aabfe16}')
    @winrt_commethod(6)
    def get_SearchString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SearchString(self, value: WinRT_String) -> Void: ...
    SearchString = property(get_SearchString, put_SearchString)
class IChatRecipientDeliveryInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo'
    _iid_ = Guid('{ffc7b2a2-283c-4c0a-8a0e-8c33bdbf0545}')
    @winrt_commethod(6)
    def get_TransportAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TransportAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DeliveryTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def put_DeliveryTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(10)
    def get_ReadTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_ReadTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_TransportErrorCodeCategory(self) -> Windows.ApplicationModel.Chat.ChatTransportErrorCodeCategory: ...
    @winrt_commethod(13)
    def get_TransportInterpretedErrorCode(self) -> Windows.ApplicationModel.Chat.ChatTransportInterpretedErrorCode: ...
    @winrt_commethod(14)
    def get_TransportErrorCode(self) -> Int32: ...
    @winrt_commethod(15)
    def get_IsErrorPermanent(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_Status(self) -> Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    TransportAddress = property(get_TransportAddress, put_TransportAddress)
    DeliveryTime = property(get_DeliveryTime, put_DeliveryTime)
    ReadTime = property(get_ReadTime, put_ReadTime)
    TransportErrorCodeCategory = property(get_TransportErrorCodeCategory, None)
    TransportInterpretedErrorCode = property(get_TransportInterpretedErrorCode, None)
    TransportErrorCode = property(get_TransportErrorCode, None)
    IsErrorPermanent = property(get_IsErrorPermanent, None)
    Status = property(get_Status, None)
class IChatSearchReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatSearchReader'
    _iid_ = Guid('{4665fe49-9020-4752-980d-39612325f589}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.IChatItem]]: ...
    @winrt_commethod(7)
    def ReadBatchWithCountAsync(self, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.IChatItem]]: ...
class IChatSyncConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatSyncConfiguration'
    _iid_ = Guid('{09f869b2-69f4-4aff-82b6-06992ff402d2}')
    @winrt_commethod(6)
    def get_IsSyncEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsSyncEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_RestoreHistorySpan(self) -> Windows.ApplicationModel.Chat.ChatRestoreHistorySpan: ...
    @winrt_commethod(9)
    def put_RestoreHistorySpan(self, value: Windows.ApplicationModel.Chat.ChatRestoreHistorySpan) -> Void: ...
    IsSyncEnabled = property(get_IsSyncEnabled, put_IsSyncEnabled)
    RestoreHistorySpan = property(get_RestoreHistorySpan, put_RestoreHistorySpan)
class IChatSyncManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatSyncManager'
    _iid_ = Guid('{7ba52c63-2650-486f-b4b4-6bd9d3d63c84}')
    @winrt_commethod(6)
    def get_Configuration(self) -> Windows.ApplicationModel.Chat.ChatSyncConfiguration: ...
    @winrt_commethod(7)
    def AssociateAccountAsync(self, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def UnassociateAccountAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def IsAccountAssociated(self, webAccount: Windows.Security.Credentials.WebAccount) -> Boolean: ...
    @winrt_commethod(10)
    def StartSync(self) -> Void: ...
    @winrt_commethod(11)
    def SetConfigurationAsync(self, configuration: Windows.ApplicationModel.Chat.ChatSyncConfiguration) -> Windows.Foundation.IAsyncAction: ...
    Configuration = property(get_Configuration, None)
class IRcsEndUserMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessage'
    _iid_ = Guid('{d7cda5eb-cbd7-4f3b-8526-b506dec35c53}')
    @winrt_commethod(6)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_IsPinRequired(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Actions(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.RcsEndUserMessageAction]: ...
    @winrt_commethod(11)
    def SendResponseAsync(self, action: Windows.ApplicationModel.Chat.RcsEndUserMessageAction) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def SendResponseWithPinAsync(self, action: Windows.ApplicationModel.Chat.RcsEndUserMessageAction, pin: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    TransportId = property(get_TransportId, None)
    Title = property(get_Title, None)
    Text = property(get_Text, None)
    IsPinRequired = property(get_IsPinRequired, None)
    Actions = property(get_Actions, None)
class IRcsEndUserMessageAction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageAction'
    _iid_ = Guid('{92378737-9b42-46d3-9d5e-3c1b2dae7cb8}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    Label = property(get_Label, None)
class IRcsEndUserMessageAvailableEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs'
    _iid_ = Guid('{2d45ae01-3f89-41ea-9702-9e9ed411aa98}')
    @winrt_commethod(6)
    def get_IsMessageAvailable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Message(self) -> Windows.ApplicationModel.Chat.RcsEndUserMessage: ...
    IsMessageAvailable = property(get_IsMessageAvailable, None)
    Message = property(get_Message, None)
class IRcsEndUserMessageAvailableTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails'
    _iid_ = Guid('{5b97742d-351f-4692-b41e-1b035dc18986}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    Title = property(get_Title, None)
    Text = property(get_Text, None)
class IRcsEndUserMessageManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageManager'
    _iid_ = Guid('{3054ae5a-4d1f-4b59-9433-126c734e86a6}')
    @winrt_commethod(6)
    def add_MessageAvailableChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.RcsEndUserMessageManager, Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageAvailableChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRcsManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsManagerStatics'
    _iid_ = Guid('{7d270ac5-0abd-4f31-9b99-a59e71a7b731}')
    @winrt_commethod(6)
    def GetEndUserMessageManager(self) -> Windows.ApplicationModel.Chat.RcsEndUserMessageManager: ...
    @winrt_commethod(7)
    def GetTransportsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.RcsTransport]]: ...
    @winrt_commethod(8)
    def GetTransportAsync(self, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.RcsTransport]: ...
    @winrt_commethod(9)
    def LeaveConversationAsync(self, conversation: Windows.ApplicationModel.Chat.ChatConversation) -> Windows.Foundation.IAsyncAction: ...
class IRcsManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsManagerStatics2'
    _iid_ = Guid('{cd49ad18-ad8a-42aa-8eeb-a798a8808959}')
    @winrt_commethod(6)
    def add_TransportListChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_TransportListChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRcsServiceKindSupportedChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsServiceKindSupportedChangedEventArgs'
    _iid_ = Guid('{f47ea244-e783-4866-b3a7-4e5ccf023070}')
    @winrt_commethod(6)
    def get_ServiceKind(self) -> Windows.ApplicationModel.Chat.RcsServiceKind: ...
    ServiceKind = property(get_ServiceKind, None)
class IRcsTransport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsTransport'
    _iid_ = Guid('{fea34759-f37c-4319-8546-ec84d21d30ff}')
    @winrt_commethod(6)
    def get_ExtendedProperties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_TransportFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Configuration(self) -> Windows.ApplicationModel.Chat.RcsTransportConfiguration: ...
    @winrt_commethod(11)
    def IsStoreAndForwardEnabled(self, serviceKind: Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_commethod(12)
    def IsServiceKindSupported(self, serviceKind: Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_commethod(13)
    def add_ServiceKindSupportedChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.RcsTransport, Windows.ApplicationModel.Chat.RcsServiceKindSupportedChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_ServiceKindSupportedChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExtendedProperties = property(get_ExtendedProperties, None)
    IsActive = property(get_IsActive, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
    Configuration = property(get_Configuration, None)
class IRcsTransportConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsTransportConfiguration'
    _iid_ = Guid('{1fccb102-2472-4bb9-9988-c1211c83e8a9}')
    @winrt_commethod(6)
    def get_MaxAttachmentCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_MaxMessageSizeInKilobytes(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MaxGroupMessageSizeInKilobytes(self) -> Int32: ...
    @winrt_commethod(9)
    def get_MaxRecipientCount(self) -> Int32: ...
    @winrt_commethod(10)
    def get_MaxFileSizeInKilobytes(self) -> Int32: ...
    @winrt_commethod(11)
    def get_WarningFileSizeInKilobytes(self) -> Int32: ...
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxGroupMessageSizeInKilobytes = property(get_MaxGroupMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    MaxFileSizeInKilobytes = property(get_MaxFileSizeInKilobytes, None)
    WarningFileSizeInKilobytes = property(get_WarningFileSizeInKilobytes, None)
class IRemoteParticipantComposingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs'
    _iid_ = Guid('{1ec045a7-cfc9-45c9-9876-449f2bc180f5}')
    @winrt_commethod(6)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ParticipantAddress(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsComposing(self) -> Boolean: ...
    TransportId = property(get_TransportId, None)
    ParticipantAddress = property(get_ParticipantAddress, None)
    IsComposing = property(get_IsComposing, None)
class RcsEndUserMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsEndUserMessage
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessage'
    @winrt_mixinmethod
    def get_TransportId(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsPinRequired(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_Actions(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.RcsEndUserMessageAction]: ...
    @winrt_mixinmethod
    def SendResponseAsync(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage, action: Windows.ApplicationModel.Chat.RcsEndUserMessageAction) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SendResponseWithPinAsync(self: Windows.ApplicationModel.Chat.IRcsEndUserMessage, action: Windows.ApplicationModel.Chat.RcsEndUserMessageAction, pin: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    TransportId = property(get_TransportId, None)
    Title = property(get_Title, None)
    Text = property(get_Text, None)
    IsPinRequired = property(get_IsPinRequired, None)
    Actions = property(get_Actions, None)
class RcsEndUserMessageAction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsEndUserMessageAction
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageAction'
    @winrt_mixinmethod
    def get_Label(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageAction) -> WinRT_String: ...
    Label = property(get_Label, None)
class RcsEndUserMessageAvailableEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableEventArgs'
    @winrt_mixinmethod
    def get_IsMessageAvailable(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs) -> Windows.ApplicationModel.Chat.RcsEndUserMessage: ...
    IsMessageAvailable = property(get_IsMessageAvailable, None)
    Message = property(get_Message, None)
class RcsEndUserMessageAvailableTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableTriggerDetails'
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails) -> WinRT_String: ...
    Title = property(get_Title, None)
    Text = property(get_Text, None)
class RcsEndUserMessageManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsEndUserMessageManager
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageManager'
    @winrt_mixinmethod
    def add_MessageAvailableChanged(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.RcsEndUserMessageManager, Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageAvailableChanged(self: Windows.ApplicationModel.Chat.IRcsEndUserMessageManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class RcsManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.RcsManager'
    @winrt_classmethod
    def add_TransportListChanged(cls: Windows.ApplicationModel.Chat.IRcsManagerStatics2, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_TransportListChanged(cls: Windows.ApplicationModel.Chat.IRcsManagerStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetEndUserMessageManager(cls: Windows.ApplicationModel.Chat.IRcsManagerStatics) -> Windows.ApplicationModel.Chat.RcsEndUserMessageManager: ...
    @winrt_classmethod
    def GetTransportsAsync(cls: Windows.ApplicationModel.Chat.IRcsManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Chat.RcsTransport]]: ...
    @winrt_classmethod
    def GetTransportAsync(cls: Windows.ApplicationModel.Chat.IRcsManagerStatics, transportId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Chat.RcsTransport]: ...
    @winrt_classmethod
    def LeaveConversationAsync(cls: Windows.ApplicationModel.Chat.IRcsManagerStatics, conversation: Windows.ApplicationModel.Chat.ChatConversation) -> Windows.Foundation.IAsyncAction: ...
RcsServiceKind = Int32
RcsServiceKind_Chat: RcsServiceKind = 0
RcsServiceKind_GroupChat: RcsServiceKind = 1
RcsServiceKind_FileTransfer: RcsServiceKind = 2
RcsServiceKind_Capability: RcsServiceKind = 3
class RcsServiceKindSupportedChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsServiceKindSupportedChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.RcsServiceKindSupportedChangedEventArgs'
    @winrt_mixinmethod
    def get_ServiceKind(self: Windows.ApplicationModel.Chat.IRcsServiceKindSupportedChangedEventArgs) -> Windows.ApplicationModel.Chat.RcsServiceKind: ...
    ServiceKind = property(get_ServiceKind, None)
class RcsTransport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsTransport
    _classid_ = 'Windows.ApplicationModel.Chat.RcsTransport'
    @winrt_mixinmethod
    def get_ExtendedProperties(self: Windows.ApplicationModel.Chat.IRcsTransport) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.ApplicationModel.Chat.IRcsTransport) -> Boolean: ...
    @winrt_mixinmethod
    def get_TransportFriendlyName(self: Windows.ApplicationModel.Chat.IRcsTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportId(self: Windows.ApplicationModel.Chat.IRcsTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Configuration(self: Windows.ApplicationModel.Chat.IRcsTransport) -> Windows.ApplicationModel.Chat.RcsTransportConfiguration: ...
    @winrt_mixinmethod
    def IsStoreAndForwardEnabled(self: Windows.ApplicationModel.Chat.IRcsTransport, serviceKind: Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_mixinmethod
    def IsServiceKindSupported(self: Windows.ApplicationModel.Chat.IRcsTransport, serviceKind: Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_mixinmethod
    def add_ServiceKindSupportedChanged(self: Windows.ApplicationModel.Chat.IRcsTransport, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Chat.RcsTransport, Windows.ApplicationModel.Chat.RcsServiceKindSupportedChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServiceKindSupportedChanged(self: Windows.ApplicationModel.Chat.IRcsTransport, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExtendedProperties = property(get_ExtendedProperties, None)
    IsActive = property(get_IsActive, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
    Configuration = property(get_Configuration, None)
class RcsTransportConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRcsTransportConfiguration
    _classid_ = 'Windows.ApplicationModel.Chat.RcsTransportConfiguration'
    @winrt_mixinmethod
    def get_MaxAttachmentCount(self: Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxMessageSizeInKilobytes(self: Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxGroupMessageSizeInKilobytes(self: Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxRecipientCount(self: Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxFileSizeInKilobytes(self: Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_WarningFileSizeInKilobytes(self: Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxGroupMessageSizeInKilobytes = property(get_MaxGroupMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    MaxFileSizeInKilobytes = property(get_MaxFileSizeInKilobytes, None)
    WarningFileSizeInKilobytes = property(get_WarningFileSizeInKilobytes, None)
class RemoteParticipantComposingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.RemoteParticipantComposingChangedEventArgs'
    @winrt_mixinmethod
    def get_TransportId(self: Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParticipantAddress(self: Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsComposing(self: Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs) -> Boolean: ...
    TransportId = property(get_TransportId, None)
    ParticipantAddress = property(get_ParticipantAddress, None)
    IsComposing = property(get_IsComposing, None)
make_head(_module, 'ChatCapabilities')
make_head(_module, 'ChatCapabilitiesManager')
make_head(_module, 'ChatConversation')
make_head(_module, 'ChatConversationReader')
make_head(_module, 'ChatConversationThreadingInfo')
make_head(_module, 'ChatMessage')
make_head(_module, 'ChatMessageAttachment')
make_head(_module, 'ChatMessageBlocking')
make_head(_module, 'ChatMessageChange')
make_head(_module, 'ChatMessageChangeReader')
make_head(_module, 'ChatMessageChangeTracker')
make_head(_module, 'ChatMessageChangedDeferral')
make_head(_module, 'ChatMessageChangedEventArgs')
make_head(_module, 'ChatMessageManager')
make_head(_module, 'ChatMessageNotificationTriggerDetails')
make_head(_module, 'ChatMessageReader')
make_head(_module, 'ChatMessageStore')
make_head(_module, 'ChatMessageStoreChangedEventArgs')
make_head(_module, 'ChatMessageTransport')
make_head(_module, 'ChatMessageTransportConfiguration')
make_head(_module, 'ChatMessageValidationResult')
make_head(_module, 'ChatQueryOptions')
make_head(_module, 'ChatRecipientDeliveryInfo')
make_head(_module, 'ChatSearchReader')
make_head(_module, 'ChatSyncConfiguration')
make_head(_module, 'ChatSyncManager')
make_head(_module, 'IChatCapabilities')
make_head(_module, 'IChatCapabilitiesManagerStatics')
make_head(_module, 'IChatCapabilitiesManagerStatics2')
make_head(_module, 'IChatConversation')
make_head(_module, 'IChatConversation2')
make_head(_module, 'IChatConversationReader')
make_head(_module, 'IChatConversationThreadingInfo')
make_head(_module, 'IChatItem')
make_head(_module, 'IChatMessage')
make_head(_module, 'IChatMessage2')
make_head(_module, 'IChatMessage3')
make_head(_module, 'IChatMessage4')
make_head(_module, 'IChatMessageAttachment')
make_head(_module, 'IChatMessageAttachment2')
make_head(_module, 'IChatMessageAttachmentFactory')
make_head(_module, 'IChatMessageBlockingStatic')
make_head(_module, 'IChatMessageChange')
make_head(_module, 'IChatMessageChangeReader')
make_head(_module, 'IChatMessageChangeTracker')
make_head(_module, 'IChatMessageChangedDeferral')
make_head(_module, 'IChatMessageChangedEventArgs')
make_head(_module, 'IChatMessageManager2Statics')
make_head(_module, 'IChatMessageManagerStatic')
make_head(_module, 'IChatMessageManagerStatics3')
make_head(_module, 'IChatMessageNotificationTriggerDetails')
make_head(_module, 'IChatMessageNotificationTriggerDetails2')
make_head(_module, 'IChatMessageReader')
make_head(_module, 'IChatMessageReader2')
make_head(_module, 'IChatMessageStore')
make_head(_module, 'IChatMessageStore2')
make_head(_module, 'IChatMessageStore3')
make_head(_module, 'IChatMessageStoreChangedEventArgs')
make_head(_module, 'IChatMessageTransport')
make_head(_module, 'IChatMessageTransport2')
make_head(_module, 'IChatMessageTransportConfiguration')
make_head(_module, 'IChatMessageValidationResult')
make_head(_module, 'IChatQueryOptions')
make_head(_module, 'IChatRecipientDeliveryInfo')
make_head(_module, 'IChatSearchReader')
make_head(_module, 'IChatSyncConfiguration')
make_head(_module, 'IChatSyncManager')
make_head(_module, 'IRcsEndUserMessage')
make_head(_module, 'IRcsEndUserMessageAction')
make_head(_module, 'IRcsEndUserMessageAvailableEventArgs')
make_head(_module, 'IRcsEndUserMessageAvailableTriggerDetails')
make_head(_module, 'IRcsEndUserMessageManager')
make_head(_module, 'IRcsManagerStatics')
make_head(_module, 'IRcsManagerStatics2')
make_head(_module, 'IRcsServiceKindSupportedChangedEventArgs')
make_head(_module, 'IRcsTransport')
make_head(_module, 'IRcsTransportConfiguration')
make_head(_module, 'IRemoteParticipantComposingChangedEventArgs')
make_head(_module, 'RcsEndUserMessage')
make_head(_module, 'RcsEndUserMessageAction')
make_head(_module, 'RcsEndUserMessageAvailableEventArgs')
make_head(_module, 'RcsEndUserMessageAvailableTriggerDetails')
make_head(_module, 'RcsEndUserMessageManager')
make_head(_module, 'RcsManager')
make_head(_module, 'RcsServiceKindSupportedChangedEventArgs')
make_head(_module, 'RcsTransport')
make_head(_module, 'RcsTransportConfiguration')
make_head(_module, 'RemoteParticipantComposingChangedEventArgs')
