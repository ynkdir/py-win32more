from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Chat
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ChatCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatCapabilities
    _classid_ = 'Windows.ApplicationModel.Chat.ChatCapabilities'
    @winrt_mixinmethod
    def get_IsOnline(self: win32more.Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsChatCapable(self: win32more.Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsFileTransferCapable(self: win32more.Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGeoLocationPushCapable(self: win32more.Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsIntegratedMessagingCapable(self: win32more.Windows.ApplicationModel.Chat.IChatCapabilities) -> Boolean: ...
    IsChatCapable = property(get_IsChatCapable, None)
    IsFileTransferCapable = property(get_IsFileTransferCapable, None)
    IsGeoLocationPushCapable = property(get_IsGeoLocationPushCapable, None)
    IsIntegratedMessagingCapable = property(get_IsIntegratedMessagingCapable, None)
    IsOnline = property(get_IsOnline, None)
class ChatCapabilitiesManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.ChatCapabilitiesManager'
    @winrt_classmethod
    def GetCachedCapabilitiesForTransportAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics2, address: WinRT_String, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_classmethod
    def GetCapabilitiesFromNetworkForTransportAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics2, address: WinRT_String, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_classmethod
    def GetCachedCapabilitiesAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics, address: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_classmethod
    def GetCapabilitiesFromNetworkAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics, address: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
class ChatConversation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatConversation
    _classid_ = 'Windows.ApplicationModel.Chat.ChatConversation'
    @winrt_mixinmethod
    def get_HasUnreadMessages(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> Boolean: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsConversationMuted(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsConversationMuted(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MostRecentMessageId(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Participants(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ThreadingInfo(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMessageReader(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> win32more.Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_mixinmethod
    def MarkAllMessagesAsReadAsync(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkMessagesAsReadAsync(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, value: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.ApplicationModel.Chat.IChatConversation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def NotifyLocalParticipantComposing(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_mixinmethod
    def NotifyRemoteParticipantComposing(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteParticipantComposingChanged(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.ChatConversation, win32more.Windows.ApplicationModel.Chat.RemoteParticipantComposingChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteParticipantComposingChanged(self: win32more.Windows.ApplicationModel.Chat.IChatConversation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CanModifyParticipants(self: win32more.Windows.ApplicationModel.Chat.IChatConversation2) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanModifyParticipants(self: win32more.Windows.ApplicationModel.Chat.IChatConversation2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ItemKind(self: win32more.Windows.ApplicationModel.Chat.IChatItem) -> win32more.Windows.ApplicationModel.Chat.ChatItemKind: ...
    CanModifyParticipants = property(get_CanModifyParticipants, put_CanModifyParticipants)
    HasUnreadMessages = property(get_HasUnreadMessages, None)
    Id = property(get_Id, None)
    IsConversationMuted = property(get_IsConversationMuted, put_IsConversationMuted)
    ItemKind = property(get_ItemKind, None)
    MostRecentMessageId = property(get_MostRecentMessageId, None)
    Participants = property(get_Participants, None)
    Subject = property(get_Subject, put_Subject)
    ThreadingInfo = property(get_ThreadingInfo, None)
    RemoteParticipantComposingChanged = event()
class ChatConversationReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatConversationReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatConversationReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Chat.IChatConversationReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatConversation]]: ...
    @winrt_mixinmethod
    def ReadBatchWithCountAsync(self: win32more.Windows.ApplicationModel.Chat.IChatConversationReader, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatConversation]]: ...
class ChatConversationThreadingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo
    _classid_ = 'Windows.ApplicationModel.Chat.ChatConversationThreadingInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_mixinmethod
    def get_ContactId(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContactId(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Custom(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Custom(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ConversationId(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ConversationId(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Participants(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.Chat.IChatConversationThreadingInfo, value: win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingKind) -> Void: ...
    ContactId = property(get_ContactId, put_ContactId)
    ConversationId = property(get_ConversationId, put_ConversationId)
    Custom = property(get_Custom, put_Custom)
    Kind = property(get_Kind, put_Kind)
    Participants = property(get_Participants, None)
class ChatConversationThreadingKind(Enum, Int32):
    Participants = 0
    ContactId = 1
    ConversationId = 2
    Custom = 3
class ChatItemKind(Enum, Int32):
    Message = 0
    Conversation = 1
class ChatMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessage
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Chat.ChatMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Chat.ChatMessage: ...
    @winrt_mixinmethod
    def get_Attachments(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Chat.ChatMessageAttachment]: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: win32more.Windows.ApplicationModel.Chat.IChatMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsForwardingDisabled(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsIncoming(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRead(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_LocalTimestamp(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NetworkTimestamp(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Recipients(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RecipientSendStatuses(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Chat.ChatMessageStatus]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> win32more.Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportFriendlyName(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportId(self: win32more.Windows.ApplicationModel.Chat.IChatMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TransportId(self: win32more.Windows.ApplicationModel.Chat.IChatMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EstimatedDownloadSize(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> UInt64: ...
    @winrt_mixinmethod
    def put_EstimatedDownloadSize(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsAutoReply(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAutoReply(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_IsForwardingDisabled(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsReplyDisabled(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIncoming(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_IsRead(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSeen(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSeen(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSimMessage(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_LocalTimestamp(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_MessageKind(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> win32more.Windows.ApplicationModel.Chat.ChatMessageKind: ...
    @winrt_mixinmethod
    def put_MessageKind(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: win32more.Windows.ApplicationModel.Chat.ChatMessageKind) -> Void: ...
    @winrt_mixinmethod
    def get_MessageOperatorKind(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> win32more.Windows.ApplicationModel.Chat.ChatMessageOperatorKind: ...
    @winrt_mixinmethod
    def put_MessageOperatorKind(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: win32more.Windows.ApplicationModel.Chat.ChatMessageOperatorKind) -> Void: ...
    @winrt_mixinmethod
    def put_NetworkTimestamp(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_IsReceivedDuringQuietHours(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsReceivedDuringQuietHours(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: win32more.Windows.ApplicationModel.Chat.ChatMessageStatus) -> Void: ...
    @winrt_mixinmethod
    def put_Subject(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldSuppressNotification(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldSuppressNotification(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ThreadingInfo(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_mixinmethod
    def put_ThreadingInfo(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2, value: win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> Void: ...
    @winrt_mixinmethod
    def get_RecipientsDeliveryInfos(self: win32more.Windows.ApplicationModel.Chat.IChatMessage2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo]: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.Chat.IChatMessage3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SyncId(self: win32more.Windows.ApplicationModel.Chat.IChatMessage4) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SyncId(self: win32more.Windows.ApplicationModel.Chat.IChatMessage4, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ItemKind(self: win32more.Windows.ApplicationModel.Chat.IChatItem) -> win32more.Windows.ApplicationModel.Chat.ChatItemKind: ...
    Attachments = property(get_Attachments, None)
    Body = property(get_Body, put_Body)
    EstimatedDownloadSize = property(get_EstimatedDownloadSize, put_EstimatedDownloadSize)
    From = property(get_From, put_From)
    Id = property(get_Id, None)
    IsAutoReply = property(get_IsAutoReply, put_IsAutoReply)
    IsForwardingDisabled = property(get_IsForwardingDisabled, put_IsForwardingDisabled)
    IsIncoming = property(get_IsIncoming, put_IsIncoming)
    IsRead = property(get_IsRead, put_IsRead)
    IsReceivedDuringQuietHours = property(get_IsReceivedDuringQuietHours, put_IsReceivedDuringQuietHours)
    IsReplyDisabled = property(get_IsReplyDisabled, None)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsSimMessage = property(get_IsSimMessage, None)
    ItemKind = property(get_ItemKind, None)
    LocalTimestamp = property(get_LocalTimestamp, put_LocalTimestamp)
    MessageKind = property(get_MessageKind, put_MessageKind)
    MessageOperatorKind = property(get_MessageOperatorKind, put_MessageOperatorKind)
    NetworkTimestamp = property(get_NetworkTimestamp, put_NetworkTimestamp)
    RecipientSendStatuses = property(get_RecipientSendStatuses, None)
    Recipients = property(get_Recipients, None)
    RecipientsDeliveryInfos = property(get_RecipientsDeliveryInfos, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    ShouldSuppressNotification = property(get_ShouldSuppressNotification, put_ShouldSuppressNotification)
    Status = property(get_Status, put_Status)
    Subject = property(get_Subject, put_Subject)
    SyncId = property(get_SyncId, put_SyncId)
    ThreadingInfo = property(get_ThreadingInfo, put_ThreadingInfo)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, put_TransportId)
class ChatMessageAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageAttachment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Chat.ChatMessageAttachment.CreateChatMessageAttachment(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateChatMessageAttachment(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachmentFactory, mimeType: WinRT_String, dataStreamReference: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.ApplicationModel.Chat.ChatMessageAttachment: ...
    @winrt_mixinmethod
    def get_DataStreamReference(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_DataStreamReference(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_GroupId(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment) -> UInt32: ...
    @winrt_mixinmethod
    def put_GroupId(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MimeType(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MimeType(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment2) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment2, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_TransferProgress(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment2) -> Double: ...
    @winrt_mixinmethod
    def put_TransferProgress(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalFileName(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OriginalFileName(self: win32more.Windows.ApplicationModel.Chat.IChatMessageAttachment2, value: WinRT_String) -> Void: ...
    DataStreamReference = property(get_DataStreamReference, put_DataStreamReference)
    GroupId = property(get_GroupId, put_GroupId)
    MimeType = property(get_MimeType, put_MimeType)
    OriginalFileName = property(get_OriginalFileName, put_OriginalFileName)
    Text = property(get_Text, put_Text)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TransferProgress = property(get_TransferProgress, put_TransferProgress)
class ChatMessageBlocking(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageBlocking'
    @winrt_classmethod
    def MarkMessageAsBlockedAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageBlockingStatic, localChatMessageId: WinRT_String, blocked: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
class ChatMessageChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageChange
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChange'
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChange) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangeType: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChange) -> win32more.Windows.ApplicationModel.Chat.ChatMessage: ...
    ChangeType = property(get_ChangeType, None)
    Message = property(get_Message, None)
class ChatMessageChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangeReader'
    @winrt_mixinmethod
    def AcceptChanges(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeReader) -> Void: ...
    @winrt_mixinmethod
    def AcceptChangesThrough(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeReader, lastChangeToAcknowledge: win32more.Windows.ApplicationModel.Chat.ChatMessageChange) -> Void: ...
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessageChange]]: ...
class ChatMessageChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeTracker
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangeTracker'
    @winrt_mixinmethod
    def Enable(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def GetChangeReader(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeTracker) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangeReader: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangeTracker) -> Void: ...
class ChatMessageChangeType(Enum, Int32):
    MessageCreated = 0
    MessageModified = 1
    MessageDeleted = 2
    ChangeTrackingLost = 3
class ChatMessageChangedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageChangedDeferral
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangedDeferral) -> Void: ...
class ChatMessageChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Chat.IChatMessageChangedEventArgs) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangedDeferral: ...
class ChatMessageKind(Enum, Int32):
    Standard = 0
    FileTransferRequest = 1
    TransportCustom = 2
    JoinedConversation = 3
    LeftConversation = 4
    OtherParticipantJoinedConversation = 5
    OtherParticipantLeftConversation = 6
class ChatMessageManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageManager'
    @winrt_classmethod
    def RequestSyncManagerAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManagerStatics3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatSyncManager]: ...
    @winrt_classmethod
    def RegisterTransportAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManager2Statics) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetTransportAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManager2Statics, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessageTransport]: ...
    @winrt_classmethod
    def GetTransportsAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManagerStatic) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessageTransport]]: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManagerStatic) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessageStore]: ...
    @winrt_classmethod
    def ShowComposeSmsMessageAsync(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManagerStatic, message: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowSmsSettings(cls: win32more.Windows.ApplicationModel.Chat.IChatMessageManagerStatic) -> Void: ...
class ChatMessageNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_ChatMessage(self: win32more.Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails) -> win32more.Windows.ApplicationModel.Chat.ChatMessage: ...
    @winrt_mixinmethod
    def get_ShouldDisplayToast(self: win32more.Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldUpdateDetailText(self: win32more.Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldUpdateBadge(self: win32more.Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldUpdateActionCenter(self: win32more.Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails2) -> Boolean: ...
    ChatMessage = property(get_ChatMessage, None)
    ShouldDisplayToast = property(get_ShouldDisplayToast, None)
    ShouldUpdateActionCenter = property(get_ShouldUpdateActionCenter, None)
    ShouldUpdateBadge = property(get_ShouldUpdateBadge, None)
    ShouldUpdateDetailText = property(get_ShouldUpdateDetailText, None)
class ChatMessageOperatorKind(Enum, Int32):
    Unspecified = 0
    Sms = 1
    Mms = 2
    Rcs = 3
class ChatMessageReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessage]]: ...
    @winrt_mixinmethod
    def ReadBatchWithCountAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageReader2, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessage]]: ...
class ChatMessageStatus(Enum, Int32):
    Draft = 0
    Sending = 1
    Sent = 2
    SendRetryNeeded = 3
    SendFailed = 4
    Received = 5
    ReceiveDownloadNeeded = 6
    ReceiveDownloadFailed = 7
    ReceiveDownloading = 8
    Deleted = 9
    Declined = 10
    Cancelled = 11
    Recalled = 12
    ReceiveRetryNeeded = 13
class ChatMessageStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageStore
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageStore'
    @winrt_mixinmethod
    def get_ChangeTracker(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangeTracker: ...
    @winrt_mixinmethod
    def DeleteMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, localMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DownloadMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_mixinmethod
    def GetMessageReader1(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore) -> win32more.Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_mixinmethod
    def GetMessageReader2(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, recentTimeLimit: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_mixinmethod
    def MarkMessageReadAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RetrySendMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, chatMessage: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ValidateMessage(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, chatMessage: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.ApplicationModel.Chat.ChatMessageValidationResult: ...
    @winrt_mixinmethod
    def add_MessageChanged(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.ChatMessageStore, win32more.Windows.ApplicationModel.Chat.ChatMessageChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageChanged(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ForwardMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, localChatMessageId: WinRT_String, addresses: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_mixinmethod
    def GetConversationAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, conversationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_mixinmethod
    def GetConversationForTransportsAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, conversationId: WinRT_String, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_mixinmethod
    def GetConversationFromThreadingInfoAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, threadingInfo: win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_mixinmethod
    def GetConversationReader(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2) -> win32more.Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_mixinmethod
    def GetConversationForTransportsReader(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_mixinmethod
    def GetMessageByRemoteIdAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, transportId: WinRT_String, remoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_mixinmethod
    def GetUnseenCountAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def GetUnseenCountForTransportsReaderAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def MarkAsSeenAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MarkAsSeenForTransportsAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetSearchReader(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, value: win32more.Windows.ApplicationModel.Chat.ChatQueryOptions) -> win32more.Windows.ApplicationModel.Chat.ChatSearchReader: ...
    @winrt_mixinmethod
    def SaveMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, chatMessage: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TryCancelDownloadMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryCancelSendMessageAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_StoreChanged(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.ChatMessageStore, win32more.Windows.ApplicationModel.Chat.ChatMessageStoreChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StoreChanged(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetMessageBySyncIdAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStore3, syncId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    ChangeTracker = property(get_ChangeTracker, None)
    MessageChanged = event()
    StoreChanged = event()
class ChatMessageStoreChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageStoreChangedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs) -> win32more.Windows.ApplicationModel.Chat.ChatStoreChangedEventKind: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class ChatMessageTransport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageTransport'
    @winrt_mixinmethod
    def get_IsAppSetAsNotificationProvider(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport) -> Boolean: ...
    @winrt_mixinmethod
    def get_TransportFriendlyName(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportId(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestSetAsNotificationProviderAsync(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport2) -> win32more.Windows.ApplicationModel.Chat.ChatMessageTransportConfiguration: ...
    @winrt_mixinmethod
    def get_TransportKind(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransport2) -> win32more.Windows.ApplicationModel.Chat.ChatMessageTransportKind: ...
    Configuration = property(get_Configuration, None)
    IsActive = property(get_IsActive, None)
    IsAppSetAsNotificationProvider = property(get_IsAppSetAsNotificationProvider, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
    TransportKind = property(get_TransportKind, None)
class ChatMessageTransportConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageTransportConfiguration'
    @winrt_mixinmethod
    def get_MaxAttachmentCount(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxMessageSizeInKilobytes(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxRecipientCount(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_SupportedVideoFormat(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> win32more.Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: win32more.Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    ExtendedProperties = property(get_ExtendedProperties, None)
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    SupportedVideoFormat = property(get_SupportedVideoFormat, None)
class ChatMessageTransportKind(Enum, Int32):
    Text = 0
    Untriaged = 1
    Blocked = 2
    Custom = 3
class ChatMessageValidationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatMessageValidationResult
    _classid_ = 'Windows.ApplicationModel.Chat.ChatMessageValidationResult'
    @winrt_mixinmethod
    def get_MaxPartCount(self: win32more.Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_PartCount(self: win32more.Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_RemainingCharacterCountInPart(self: win32more.Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Chat.IChatMessageValidationResult) -> win32more.Windows.ApplicationModel.Chat.ChatMessageValidationStatus: ...
    MaxPartCount = property(get_MaxPartCount, None)
    PartCount = property(get_PartCount, None)
    RemainingCharacterCountInPart = property(get_RemainingCharacterCountInPart, None)
    Status = property(get_Status, None)
class ChatMessageValidationStatus(Enum, Int32):
    Valid = 0
    NoRecipients = 1
    InvalidData = 2
    MessageTooLarge = 3
    TooManyRecipients = 4
    TransportInactive = 5
    TransportNotFound = 6
    TooManyAttachments = 7
    InvalidRecipients = 8
    InvalidBody = 9
    InvalidOther = 10
    ValidWithLargeMessage = 11
    VoiceRoamingRestriction = 12
    DataRoamingRestriction = 13
class ChatQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatQueryOptions
    _classid_ = 'Windows.ApplicationModel.Chat.ChatQueryOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Chat.ChatQueryOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Chat.ChatQueryOptions: ...
    @winrt_mixinmethod
    def get_SearchString(self: win32more.Windows.ApplicationModel.Chat.IChatQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SearchString(self: win32more.Windows.ApplicationModel.Chat.IChatQueryOptions, value: WinRT_String) -> Void: ...
    SearchString = property(get_SearchString, put_SearchString)
class ChatRecipientDeliveryInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo
    _classid_ = 'Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo: ...
    @winrt_mixinmethod
    def get_TransportAddress(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TransportAddress(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeliveryTime(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DeliveryTime(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ReadTime(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ReadTime(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_TransportErrorCodeCategory(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> win32more.Windows.ApplicationModel.Chat.ChatTransportErrorCodeCategory: ...
    @winrt_mixinmethod
    def get_TransportInterpretedErrorCode(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> win32more.Windows.ApplicationModel.Chat.ChatTransportInterpretedErrorCode: ...
    @winrt_mixinmethod
    def get_TransportErrorCode(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_IsErrorPermanent(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo) -> win32more.Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    DeliveryTime = property(get_DeliveryTime, put_DeliveryTime)
    IsErrorPermanent = property(get_IsErrorPermanent, None)
    ReadTime = property(get_ReadTime, put_ReadTime)
    Status = property(get_Status, None)
    TransportAddress = property(get_TransportAddress, put_TransportAddress)
    TransportErrorCode = property(get_TransportErrorCode, None)
    TransportErrorCodeCategory = property(get_TransportErrorCodeCategory, None)
    TransportInterpretedErrorCode = property(get_TransportInterpretedErrorCode, None)
class ChatRestoreHistorySpan(Enum, Int32):
    LastMonth = 0
    LastYear = 1
    AnyTime = 2
class ChatSearchReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatSearchReader
    _classid_ = 'Windows.ApplicationModel.Chat.ChatSearchReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.Chat.IChatSearchReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.IChatItem]]: ...
    @winrt_mixinmethod
    def ReadBatchWithCountAsync(self: win32more.Windows.ApplicationModel.Chat.IChatSearchReader, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.IChatItem]]: ...
class ChatStoreChangedEventKind(Enum, Int32):
    NotificationsMissed = 0
    StoreModified = 1
    MessageCreated = 2
    MessageModified = 3
    MessageDeleted = 4
    ConversationModified = 5
    ConversationDeleted = 6
    ConversationTransportDeleted = 7
class ChatSyncConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatSyncConfiguration
    _classid_ = 'Windows.ApplicationModel.Chat.ChatSyncConfiguration'
    @winrt_mixinmethod
    def get_IsSyncEnabled(self: win32more.Windows.ApplicationModel.Chat.IChatSyncConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSyncEnabled(self: win32more.Windows.ApplicationModel.Chat.IChatSyncConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RestoreHistorySpan(self: win32more.Windows.ApplicationModel.Chat.IChatSyncConfiguration) -> win32more.Windows.ApplicationModel.Chat.ChatRestoreHistorySpan: ...
    @winrt_mixinmethod
    def put_RestoreHistorySpan(self: win32more.Windows.ApplicationModel.Chat.IChatSyncConfiguration, value: win32more.Windows.ApplicationModel.Chat.ChatRestoreHistorySpan) -> Void: ...
    IsSyncEnabled = property(get_IsSyncEnabled, put_IsSyncEnabled)
    RestoreHistorySpan = property(get_RestoreHistorySpan, put_RestoreHistorySpan)
class ChatSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IChatSyncManager
    _classid_ = 'Windows.ApplicationModel.Chat.ChatSyncManager'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.Chat.IChatSyncManager) -> win32more.Windows.ApplicationModel.Chat.ChatSyncConfiguration: ...
    @winrt_mixinmethod
    def AssociateAccountAsync(self: win32more.Windows.ApplicationModel.Chat.IChatSyncManager, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnassociateAccountAsync(self: win32more.Windows.ApplicationModel.Chat.IChatSyncManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def IsAccountAssociated(self: win32more.Windows.ApplicationModel.Chat.IChatSyncManager, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> Boolean: ...
    @winrt_mixinmethod
    def StartSync(self: win32more.Windows.ApplicationModel.Chat.IChatSyncManager) -> Void: ...
    @winrt_mixinmethod
    def SetConfigurationAsync(self: win32more.Windows.ApplicationModel.Chat.IChatSyncManager, configuration: win32more.Windows.ApplicationModel.Chat.ChatSyncConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    Configuration = property(get_Configuration, None)
class ChatTransportErrorCodeCategory(Enum, Int32):
    None_ = 0
    Http = 1
    Network = 2
    MmsServer = 3
class ChatTransportInterpretedErrorCode(Enum, Int32):
    None_ = 0
    Unknown = 1
    InvalidRecipientAddress = 2
    NetworkConnectivity = 3
    ServiceDenied = 4
    Timeout = 5
class IChatCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    IsChatCapable = property(get_IsChatCapable, None)
    IsFileTransferCapable = property(get_IsFileTransferCapable, None)
    IsGeoLocationPushCapable = property(get_IsGeoLocationPushCapable, None)
    IsIntegratedMessagingCapable = property(get_IsIntegratedMessagingCapable, None)
    IsOnline = property(get_IsOnline, None)
class IChatCapabilitiesManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics'
    _iid_ = Guid('{b57a2f30-7041-458e-b0cf-7c0d9fea333a}')
    @winrt_commethod(6)
    def GetCachedCapabilitiesAsync(self, address: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_commethod(7)
    def GetCapabilitiesFromNetworkAsync(self, address: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
class IChatCapabilitiesManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatCapabilitiesManagerStatics2'
    _iid_ = Guid('{e30d4274-d5c1-4ac9-9ffc-40e69184fec8}')
    @winrt_commethod(6)
    def GetCachedCapabilitiesForTransportAsync(self, address: WinRT_String, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
    @winrt_commethod(7)
    def GetCapabilitiesFromNetworkForTransportAsync(self, address: WinRT_String, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatCapabilities]: ...
class IChatConversation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Participants(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(14)
    def get_ThreadingInfo(self) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_commethod(15)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def GetMessageReader(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_commethod(17)
    def MarkAllMessagesAsReadAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def MarkMessagesAsReadAsync(self, value: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def NotifyLocalParticipantComposing(self, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_commethod(21)
    def NotifyRemoteParticipantComposing(self, transportId: WinRT_String, participantAddress: WinRT_String, isComposing: Boolean) -> Void: ...
    @winrt_commethod(22)
    def add_RemoteParticipantComposingChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.ChatConversation, win32more.Windows.ApplicationModel.Chat.RemoteParticipantComposingChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_RemoteParticipantComposingChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HasUnreadMessages = property(get_HasUnreadMessages, None)
    Id = property(get_Id, None)
    IsConversationMuted = property(get_IsConversationMuted, put_IsConversationMuted)
    MostRecentMessageId = property(get_MostRecentMessageId, None)
    Participants = property(get_Participants, None)
    Subject = property(get_Subject, put_Subject)
    ThreadingInfo = property(get_ThreadingInfo, None)
    RemoteParticipantComposingChanged = event()
class IChatConversation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatConversation2'
    _iid_ = Guid('{0a030cd1-983a-47aa-9a90-ee48ee997b59}')
    @winrt_commethod(6)
    def get_CanModifyParticipants(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanModifyParticipants(self, value: Boolean) -> Void: ...
    CanModifyParticipants = property(get_CanModifyParticipants, put_CanModifyParticipants)
class IChatConversationReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatConversationReader'
    _iid_ = Guid('{055136d2-de32-4a47-a93a-b3dc0833852b}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatConversation]]: ...
    @winrt_commethod(7)
    def ReadBatchWithCountAsync(self, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatConversation]]: ...
class IChatConversationThreadingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Participants(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingKind: ...
    @winrt_commethod(14)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingKind) -> Void: ...
    ContactId = property(get_ContactId, put_ContactId)
    ConversationId = property(get_ConversationId, put_ConversationId)
    Custom = property(get_Custom, put_Custom)
    Kind = property(get_Kind, put_Kind)
    Participants = property(get_Participants, None)
class IChatItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatItem'
    _iid_ = Guid('{8751d000-ceb1-4243-b803-15d45a1dd428}')
    @winrt_commethod(6)
    def get_ItemKind(self) -> win32more.Windows.ApplicationModel.Chat.ChatItemKind: ...
    ItemKind = property(get_ItemKind, None)
class IChatMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage'
    _iid_ = Guid('{4b39052a-1142-5089-76da-f2db3d17cd05}')
    @winrt_commethod(6)
    def get_Attachments(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Chat.ChatMessageAttachment]: ...
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
    def get_LocalTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def get_NetworkTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(16)
    def get_Recipients(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(17)
    def get_RecipientSendStatuses(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Chat.ChatMessageStatus]: ...
    @winrt_commethod(18)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageStatus: ...
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
    RecipientSendStatuses = property(get_RecipientSendStatuses, None)
    Recipients = property(get_Recipients, None)
    Status = property(get_Status, None)
    Subject = property(get_Subject, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, put_TransportId)
class IChatMessage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def put_LocalTimestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(19)
    def get_MessageKind(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageKind: ...
    @winrt_commethod(20)
    def put_MessageKind(self, value: win32more.Windows.ApplicationModel.Chat.ChatMessageKind) -> Void: ...
    @winrt_commethod(21)
    def get_MessageOperatorKind(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageOperatorKind: ...
    @winrt_commethod(22)
    def put_MessageOperatorKind(self, value: win32more.Windows.ApplicationModel.Chat.ChatMessageOperatorKind) -> Void: ...
    @winrt_commethod(23)
    def put_NetworkTimestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(24)
    def get_IsReceivedDuringQuietHours(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_IsReceivedDuringQuietHours(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(27)
    def put_Status(self, value: win32more.Windows.ApplicationModel.Chat.ChatMessageStatus) -> Void: ...
    @winrt_commethod(28)
    def put_Subject(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(29)
    def get_ShouldSuppressNotification(self) -> Boolean: ...
    @winrt_commethod(30)
    def put_ShouldSuppressNotification(self, value: Boolean) -> Void: ...
    @winrt_commethod(31)
    def get_ThreadingInfo(self) -> win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo: ...
    @winrt_commethod(32)
    def put_ThreadingInfo(self, value: win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> Void: ...
    @winrt_commethod(33)
    def get_RecipientsDeliveryInfos(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Chat.ChatRecipientDeliveryInfo]: ...
    EstimatedDownloadSize = property(get_EstimatedDownloadSize, put_EstimatedDownloadSize)
    From = property(None, put_From)
    IsAutoReply = property(get_IsAutoReply, put_IsAutoReply)
    IsForwardingDisabled = property(None, put_IsForwardingDisabled)
    IsIncoming = property(None, put_IsIncoming)
    IsRead = property(None, put_IsRead)
    IsReceivedDuringQuietHours = property(get_IsReceivedDuringQuietHours, put_IsReceivedDuringQuietHours)
    IsReplyDisabled = property(get_IsReplyDisabled, None)
    IsSeen = property(get_IsSeen, put_IsSeen)
    IsSimMessage = property(get_IsSimMessage, None)
    LocalTimestamp = property(None, put_LocalTimestamp)
    MessageKind = property(get_MessageKind, put_MessageKind)
    MessageOperatorKind = property(get_MessageOperatorKind, put_MessageOperatorKind)
    NetworkTimestamp = property(None, put_NetworkTimestamp)
    RecipientsDeliveryInfos = property(get_RecipientsDeliveryInfos, None)
    RemoteId = property(None, put_RemoteId)
    ShouldSuppressNotification = property(get_ShouldSuppressNotification, put_ShouldSuppressNotification)
    Status = property(None, put_Status)
    Subject = property(None, put_Subject)
    ThreadingInfo = property(get_ThreadingInfo, put_ThreadingInfo)
class IChatMessage3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage3'
    _iid_ = Guid('{74eb2fb0-3ba7-459f-8e0b-e8af0febd9ad}')
    @winrt_commethod(6)
    def get_RemoteId(self) -> WinRT_String: ...
    RemoteId = property(get_RemoteId, None)
class IChatMessage4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessage4'
    _iid_ = Guid('{2d144b0f-d2bf-460c-aa68-6d3f8483c9bf}')
    @winrt_commethod(6)
    def get_SyncId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SyncId(self, value: WinRT_String) -> Void: ...
    SyncId = property(get_SyncId, put_SyncId)
class IChatMessageAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageAttachment'
    _iid_ = Guid('{c7c4fd74-bf63-58eb-508c-8b863ff16b67}')
    @winrt_commethod(6)
    def get_DataStreamReference(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_DataStreamReference(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageAttachment2'
    _iid_ = Guid('{5ed99270-7dd1-4a87-a8ce-acdd87d80dc8}')
    @winrt_commethod(6)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_Thumbnail(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def get_TransferProgress(self) -> Double: ...
    @winrt_commethod(9)
    def put_TransferProgress(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_OriginalFileName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_OriginalFileName(self, value: WinRT_String) -> Void: ...
    OriginalFileName = property(get_OriginalFileName, put_OriginalFileName)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TransferProgress = property(get_TransferProgress, put_TransferProgress)
class IChatMessageAttachmentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageAttachmentFactory'
    _iid_ = Guid('{205852a2-a356-5b71-6ca9-66c985b7d0d5}')
    @winrt_commethod(6)
    def CreateChatMessageAttachment(self, mimeType: WinRT_String, dataStreamReference: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.ApplicationModel.Chat.ChatMessageAttachment: ...
class IChatMessageBlockingStatic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageBlockingStatic'
    _iid_ = Guid('{f6b9a380-cdea-11e4-8830-0800200c9a66}')
    @winrt_commethod(6)
    def MarkMessageAsBlockedAsync(self, localChatMessageId: WinRT_String, blocked: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
class IChatMessageChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChange'
    _iid_ = Guid('{1c18c355-421e-54b8-6d38-6b3a6c82fccc}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangeType: ...
    @winrt_commethod(7)
    def get_Message(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessage: ...
    ChangeType = property(get_ChangeType, None)
    Message = property(get_Message, None)
class IChatMessageChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangeReader'
    _iid_ = Guid('{14267020-28ce-5f26-7b05-9a5c7cce87ca}')
    @winrt_commethod(6)
    def AcceptChanges(self) -> Void: ...
    @winrt_commethod(7)
    def AcceptChangesThrough(self, lastChangeToAcknowledge: win32more.Windows.ApplicationModel.Chat.ChatMessageChange) -> Void: ...
    @winrt_commethod(8)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessageChange]]: ...
class IChatMessageChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangeTracker'
    _iid_ = Guid('{60b7f066-70a0-5224-508c-242ef7c1d06f}')
    @winrt_commethod(6)
    def Enable(self) -> Void: ...
    @winrt_commethod(7)
    def GetChangeReader(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangeReader: ...
    @winrt_commethod(8)
    def Reset(self) -> Void: ...
class IChatMessageChangedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangedDeferral'
    _iid_ = Guid('{fbc6b30c-788c-4dcc-ace7-6282382968cf}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IChatMessageChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageChangedEventArgs'
    _iid_ = Guid('{b6b73e2d-691c-4edf-8660-6eb9896892e3}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangedDeferral: ...
class IChatMessageManager2Statics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageManager2Statics'
    _iid_ = Guid('{1d45390f-9f4f-4e35-964e-1b9ca61ac044}')
    @winrt_commethod(6)
    def RegisterTransportAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def GetTransportAsync(self, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessageTransport]: ...
class IChatMessageManagerStatic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageManagerStatic'
    _iid_ = Guid('{f15c60f7-d5e8-5e92-556d-e03b60253104}')
    @winrt_commethod(6)
    def GetTransportsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessageTransport]]: ...
    @winrt_commethod(7)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessageStore]: ...
    @winrt_commethod(8)
    def ShowComposeSmsMessageAsync(self, message: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ShowSmsSettings(self) -> Void: ...
class IChatMessageManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageManagerStatics3'
    _iid_ = Guid('{208b830d-6755-48cc-9ab3-fd03c463fc92}')
    @winrt_commethod(6)
    def RequestSyncManagerAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatSyncManager]: ...
class IChatMessageNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageNotificationTriggerDetails'
    _iid_ = Guid('{fd344dfb-3063-4e17-8586-c6c08262e6c0}')
    @winrt_commethod(6)
    def get_ChatMessage(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessage: ...
    ChatMessage = property(get_ChatMessage, None)
class IChatMessageNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    ShouldUpdateActionCenter = property(get_ShouldUpdateActionCenter, None)
    ShouldUpdateBadge = property(get_ShouldUpdateBadge, None)
    ShouldUpdateDetailText = property(get_ShouldUpdateDetailText, None)
class IChatMessageReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageReader'
    _iid_ = Guid('{b6ea78ce-4489-56f9-76aa-e204682514cf}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessage]]: ...
class IChatMessageReader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageReader2'
    _iid_ = Guid('{89643683-64bb-470d-9df4-0de8be1a05bf}')
    @winrt_commethod(6)
    def ReadBatchWithCountAsync(self, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.ChatMessage]]: ...
class IChatMessageStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStore'
    _iid_ = Guid('{31f2fd01-ccf6-580b-4976-0a07dd5d3b47}')
    @winrt_commethod(6)
    def get_ChangeTracker(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageChangeTracker: ...
    @winrt_commethod(7)
    def DeleteMessageAsync(self, localMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DownloadMessageAsync(self, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def GetMessageAsync(self, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_commethod(10)
    def GetMessageReader1(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_commethod(11)
    def GetMessageReader2(self, recentTimeLimit: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Chat.ChatMessageReader: ...
    @winrt_commethod(12)
    def MarkMessageReadAsync(self, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def RetrySendMessageAsync(self, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def SendMessageAsync(self, chatMessage: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def ValidateMessage(self, chatMessage: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.ApplicationModel.Chat.ChatMessageValidationResult: ...
    @winrt_commethod(16)
    def add_MessageChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.ChatMessageStore, win32more.Windows.ApplicationModel.Chat.ChatMessageChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MessageChanged(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ChangeTracker = property(get_ChangeTracker, None)
    MessageChanged = event()
class IChatMessageStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStore2'
    _iid_ = Guid('{ad4dc4ee-3ad4-491b-b311-abdf9bb22768}')
    @winrt_commethod(6)
    def ForwardMessageAsync(self, localChatMessageId: WinRT_String, addresses: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_commethod(7)
    def GetConversationAsync(self, conversationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_commethod(8)
    def GetConversationForTransportsAsync(self, conversationId: WinRT_String, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_commethod(9)
    def GetConversationFromThreadingInfoAsync(self, threadingInfo: win32more.Windows.ApplicationModel.Chat.ChatConversationThreadingInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatConversation]: ...
    @winrt_commethod(10)
    def GetConversationReader(self) -> win32more.Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_commethod(11)
    def GetConversationForTransportsReader(self, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.ApplicationModel.Chat.ChatConversationReader: ...
    @winrt_commethod(12)
    def GetMessageByRemoteIdAsync(self, transportId: WinRT_String, remoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
    @winrt_commethod(13)
    def GetUnseenCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(14)
    def GetUnseenCountForTransportsReaderAsync(self, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(15)
    def MarkAsSeenAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def MarkAsSeenForTransportsAsync(self, transportIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def GetSearchReader(self, value: win32more.Windows.ApplicationModel.Chat.ChatQueryOptions) -> win32more.Windows.ApplicationModel.Chat.ChatSearchReader: ...
    @winrt_commethod(18)
    def SaveMessageAsync(self, chatMessage: win32more.Windows.ApplicationModel.Chat.ChatMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def TryCancelDownloadMessageAsync(self, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(20)
    def TryCancelSendMessageAsync(self, localChatMessageId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def add_StoreChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.ChatMessageStore, win32more.Windows.ApplicationModel.Chat.ChatMessageStoreChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_StoreChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    StoreChanged = event()
class IChatMessageStore3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStore3'
    _iid_ = Guid('{9adbbb09-4345-4ec1-8b74-b7338243719c}')
    @winrt_commethod(6)
    def GetMessageBySyncIdAsync(self, syncId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.ChatMessage]: ...
class IChatMessageStoreChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageStoreChangedEventArgs'
    _iid_ = Guid('{65c66fac-fe8c-46d4-9119-57b8410311d5}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Chat.ChatStoreChangedEventKind: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class IChatMessageTransport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def RequestSetAsNotificationProviderAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    IsActive = property(get_IsActive, None)
    IsAppSetAsNotificationProvider = property(get_IsAppSetAsNotificationProvider, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
class IChatMessageTransport2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageTransport2'
    _iid_ = Guid('{90a75622-d84a-4c22-a94d-544444edc8a1}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageTransportConfiguration: ...
    @winrt_commethod(7)
    def get_TransportKind(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageTransportKind: ...
    Configuration = property(get_Configuration, None)
    TransportKind = property(get_TransportKind, None)
class IChatMessageTransportConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageTransportConfiguration'
    _iid_ = Guid('{879ff725-1a08-4aca-a075-3355126312e6}')
    @winrt_commethod(6)
    def get_MaxAttachmentCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_MaxMessageSizeInKilobytes(self) -> Int32: ...
    @winrt_commethod(8)
    def get_MaxRecipientCount(self) -> Int32: ...
    @winrt_commethod(9)
    def get_SupportedVideoFormat(self) -> win32more.Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(10)
    def get_ExtendedProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    ExtendedProperties = property(get_ExtendedProperties, None)
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    SupportedVideoFormat = property(get_SupportedVideoFormat, None)
class IChatMessageValidationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatMessageValidationResult'
    _iid_ = Guid('{25e93a03-28ec-5889-569b-7e486b126f18}')
    @winrt_commethod(6)
    def get_MaxPartCount(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def get_PartCount(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_RemainingCharacterCountInPart(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageValidationStatus: ...
    MaxPartCount = property(get_MaxPartCount, None)
    PartCount = property(get_PartCount, None)
    RemainingCharacterCountInPart = property(get_RemainingCharacterCountInPart, None)
    Status = property(get_Status, None)
class IChatQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatQueryOptions'
    _iid_ = Guid('{2fd364a6-bf36-42f7-b7e7-923c0aabfe16}')
    @winrt_commethod(6)
    def get_SearchString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SearchString(self, value: WinRT_String) -> Void: ...
    SearchString = property(get_SearchString, put_SearchString)
class IChatRecipientDeliveryInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatRecipientDeliveryInfo'
    _iid_ = Guid('{ffc7b2a2-283c-4c0a-8a0e-8c33bdbf0545}')
    @winrt_commethod(6)
    def get_TransportAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TransportAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DeliveryTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def put_DeliveryTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(10)
    def get_ReadTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_ReadTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_TransportErrorCodeCategory(self) -> win32more.Windows.ApplicationModel.Chat.ChatTransportErrorCodeCategory: ...
    @winrt_commethod(13)
    def get_TransportInterpretedErrorCode(self) -> win32more.Windows.ApplicationModel.Chat.ChatTransportInterpretedErrorCode: ...
    @winrt_commethod(14)
    def get_TransportErrorCode(self) -> Int32: ...
    @winrt_commethod(15)
    def get_IsErrorPermanent(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Chat.ChatMessageStatus: ...
    DeliveryTime = property(get_DeliveryTime, put_DeliveryTime)
    IsErrorPermanent = property(get_IsErrorPermanent, None)
    ReadTime = property(get_ReadTime, put_ReadTime)
    Status = property(get_Status, None)
    TransportAddress = property(get_TransportAddress, put_TransportAddress)
    TransportErrorCode = property(get_TransportErrorCode, None)
    TransportErrorCodeCategory = property(get_TransportErrorCodeCategory, None)
    TransportInterpretedErrorCode = property(get_TransportInterpretedErrorCode, None)
class IChatSearchReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatSearchReader'
    _iid_ = Guid('{4665fe49-9020-4752-980d-39612325f589}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.IChatItem]]: ...
    @winrt_commethod(7)
    def ReadBatchWithCountAsync(self, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.IChatItem]]: ...
class IChatSyncConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatSyncConfiguration'
    _iid_ = Guid('{09f869b2-69f4-4aff-82b6-06992ff402d2}')
    @winrt_commethod(6)
    def get_IsSyncEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsSyncEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_RestoreHistorySpan(self) -> win32more.Windows.ApplicationModel.Chat.ChatRestoreHistorySpan: ...
    @winrt_commethod(9)
    def put_RestoreHistorySpan(self, value: win32more.Windows.ApplicationModel.Chat.ChatRestoreHistorySpan) -> Void: ...
    IsSyncEnabled = property(get_IsSyncEnabled, put_IsSyncEnabled)
    RestoreHistorySpan = property(get_RestoreHistorySpan, put_RestoreHistorySpan)
class IChatSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IChatSyncManager'
    _iid_ = Guid('{7ba52c63-2650-486f-b4b4-6bd9d3d63c84}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.ApplicationModel.Chat.ChatSyncConfiguration: ...
    @winrt_commethod(7)
    def AssociateAccountAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def UnassociateAccountAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def IsAccountAssociated(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> Boolean: ...
    @winrt_commethod(10)
    def StartSync(self) -> Void: ...
    @winrt_commethod(11)
    def SetConfigurationAsync(self, configuration: win32more.Windows.ApplicationModel.Chat.ChatSyncConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    Configuration = property(get_Configuration, None)
class IRcsEndUserMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Actions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAction]: ...
    @winrt_commethod(11)
    def SendResponseAsync(self, action: win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAction) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def SendResponseWithPinAsync(self, action: win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAction, pin: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    Actions = property(get_Actions, None)
    IsPinRequired = property(get_IsPinRequired, None)
    Text = property(get_Text, None)
    Title = property(get_Title, None)
    TransportId = property(get_TransportId, None)
class IRcsEndUserMessageAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageAction'
    _iid_ = Guid('{92378737-9b42-46d3-9d5e-3c1b2dae7cb8}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    Label = property(get_Label, None)
class IRcsEndUserMessageAvailableEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs'
    _iid_ = Guid('{2d45ae01-3f89-41ea-9702-9e9ed411aa98}')
    @winrt_commethod(6)
    def get_IsMessageAvailable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Message(self) -> win32more.Windows.ApplicationModel.Chat.RcsEndUserMessage: ...
    IsMessageAvailable = property(get_IsMessageAvailable, None)
    Message = property(get_Message, None)
class IRcsEndUserMessageAvailableTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails'
    _iid_ = Guid('{5b97742d-351f-4692-b41e-1b035dc18986}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, None)
    Title = property(get_Title, None)
class IRcsEndUserMessageManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsEndUserMessageManager'
    _iid_ = Guid('{3054ae5a-4d1f-4b59-9433-126c734e86a6}')
    @winrt_commethod(6)
    def add_MessageAvailableChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageManager, win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageAvailableChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MessageAvailableChanged = event()
class IRcsManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsManagerStatics'
    _iid_ = Guid('{7d270ac5-0abd-4f31-9b99-a59e71a7b731}')
    @winrt_commethod(6)
    def GetEndUserMessageManager(self) -> win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageManager: ...
    @winrt_commethod(7)
    def GetTransportsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.RcsTransport]]: ...
    @winrt_commethod(8)
    def GetTransportAsync(self, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.RcsTransport]: ...
    @winrt_commethod(9)
    def LeaveConversationAsync(self, conversation: win32more.Windows.ApplicationModel.Chat.ChatConversation) -> win32more.Windows.Foundation.IAsyncAction: ...
class IRcsManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsManagerStatics2'
    _iid_ = Guid('{cd49ad18-ad8a-42aa-8eeb-a798a8808959}')
    @winrt_commethod(6)
    def add_TransportListChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_TransportListChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TransportListChanged = event()
class IRcsServiceKindSupportedChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsServiceKindSupportedChangedEventArgs'
    _iid_ = Guid('{f47ea244-e783-4866-b3a7-4e5ccf023070}')
    @winrt_commethod(6)
    def get_ServiceKind(self) -> win32more.Windows.ApplicationModel.Chat.RcsServiceKind: ...
    ServiceKind = property(get_ServiceKind, None)
class IRcsTransport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRcsTransport'
    _iid_ = Guid('{fea34759-f37c-4319-8546-ec84d21d30ff}')
    @winrt_commethod(6)
    def get_ExtendedProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_TransportFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Configuration(self) -> win32more.Windows.ApplicationModel.Chat.RcsTransportConfiguration: ...
    @winrt_commethod(11)
    def IsStoreAndForwardEnabled(self, serviceKind: win32more.Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_commethod(12)
    def IsServiceKindSupported(self, serviceKind: win32more.Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_commethod(13)
    def add_ServiceKindSupportedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.RcsTransport, win32more.Windows.ApplicationModel.Chat.RcsServiceKindSupportedChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_ServiceKindSupportedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Configuration = property(get_Configuration, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
    IsActive = property(get_IsActive, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
    ServiceKindSupportedChanged = event()
class IRcsTransportConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    MaxFileSizeInKilobytes = property(get_MaxFileSizeInKilobytes, None)
    MaxGroupMessageSizeInKilobytes = property(get_MaxGroupMessageSizeInKilobytes, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    WarningFileSizeInKilobytes = property(get_WarningFileSizeInKilobytes, None)
class IRemoteParticipantComposingChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs'
    _iid_ = Guid('{1ec045a7-cfc9-45c9-9876-449f2bc180f5}')
    @winrt_commethod(6)
    def get_TransportId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ParticipantAddress(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsComposing(self) -> Boolean: ...
    IsComposing = property(get_IsComposing, None)
    ParticipantAddress = property(get_ParticipantAddress, None)
    TransportId = property(get_TransportId, None)
class RcsEndUserMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessage'
    @winrt_mixinmethod
    def get_TransportId(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsPinRequired(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_Actions(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAction]: ...
    @winrt_mixinmethod
    def SendResponseAsync(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage, action: win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAction) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SendResponseWithPinAsync(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessage, action: win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAction, pin: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    Actions = property(get_Actions, None)
    IsPinRequired = property(get_IsPinRequired, None)
    Text = property(get_Text, None)
    Title = property(get_Title, None)
    TransportId = property(get_TransportId, None)
class RcsEndUserMessageAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAction
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageAction'
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAction) -> WinRT_String: ...
    Label = property(get_Label, None)
class RcsEndUserMessageAvailableEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableEventArgs'
    @winrt_mixinmethod
    def get_IsMessageAvailable(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableEventArgs) -> win32more.Windows.ApplicationModel.Chat.RcsEndUserMessage: ...
    IsMessageAvailable = property(get_IsMessageAvailable, None)
    Message = property(get_Message, None)
class RcsEndUserMessageAvailableTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableTriggerDetails'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageAvailableTriggerDetails) -> WinRT_String: ...
    Text = property(get_Text, None)
    Title = property(get_Title, None)
class RcsEndUserMessageManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageManager
    _classid_ = 'Windows.ApplicationModel.Chat.RcsEndUserMessageManager'
    @winrt_mixinmethod
    def add_MessageAvailableChanged(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageManager, win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageAvailableEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageAvailableChanged(self: win32more.Windows.ApplicationModel.Chat.IRcsEndUserMessageManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MessageAvailableChanged = event()
class RcsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Chat.RcsManager'
    @winrt_classmethod
    def add_TransportListChanged(cls: win32more.Windows.ApplicationModel.Chat.IRcsManagerStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_TransportListChanged(cls: win32more.Windows.ApplicationModel.Chat.IRcsManagerStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetEndUserMessageManager(cls: win32more.Windows.ApplicationModel.Chat.IRcsManagerStatics) -> win32more.Windows.ApplicationModel.Chat.RcsEndUserMessageManager: ...
    @winrt_classmethod
    def GetTransportsAsync(cls: win32more.Windows.ApplicationModel.Chat.IRcsManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Chat.RcsTransport]]: ...
    @winrt_classmethod
    def GetTransportAsync(cls: win32more.Windows.ApplicationModel.Chat.IRcsManagerStatics, transportId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Chat.RcsTransport]: ...
    @winrt_classmethod
    def LeaveConversationAsync(cls: win32more.Windows.ApplicationModel.Chat.IRcsManagerStatics, conversation: win32more.Windows.ApplicationModel.Chat.ChatConversation) -> win32more.Windows.Foundation.IAsyncAction: ...
class RcsServiceKind(Enum, Int32):
    Chat = 0
    GroupChat = 1
    FileTransfer = 2
    Capability = 3
class RcsServiceKindSupportedChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsServiceKindSupportedChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.RcsServiceKindSupportedChangedEventArgs'
    @winrt_mixinmethod
    def get_ServiceKind(self: win32more.Windows.ApplicationModel.Chat.IRcsServiceKindSupportedChangedEventArgs) -> win32more.Windows.ApplicationModel.Chat.RcsServiceKind: ...
    ServiceKind = property(get_ServiceKind, None)
class RcsTransport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsTransport
    _classid_ = 'Windows.ApplicationModel.Chat.RcsTransport'
    @winrt_mixinmethod
    def get_ExtendedProperties(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport) -> Boolean: ...
    @winrt_mixinmethod
    def get_TransportFriendlyName(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransportId(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport) -> win32more.Windows.ApplicationModel.Chat.RcsTransportConfiguration: ...
    @winrt_mixinmethod
    def IsStoreAndForwardEnabled(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport, serviceKind: win32more.Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_mixinmethod
    def IsServiceKindSupported(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport, serviceKind: win32more.Windows.ApplicationModel.Chat.RcsServiceKind) -> Boolean: ...
    @winrt_mixinmethod
    def add_ServiceKindSupportedChanged(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Chat.RcsTransport, win32more.Windows.ApplicationModel.Chat.RcsServiceKindSupportedChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServiceKindSupportedChanged(self: win32more.Windows.ApplicationModel.Chat.IRcsTransport, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Configuration = property(get_Configuration, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
    IsActive = property(get_IsActive, None)
    TransportFriendlyName = property(get_TransportFriendlyName, None)
    TransportId = property(get_TransportId, None)
    ServiceKindSupportedChanged = event()
class RcsTransportConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration
    _classid_ = 'Windows.ApplicationModel.Chat.RcsTransportConfiguration'
    @winrt_mixinmethod
    def get_MaxAttachmentCount(self: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxMessageSizeInKilobytes(self: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxGroupMessageSizeInKilobytes(self: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxRecipientCount(self: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxFileSizeInKilobytes(self: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_WarningFileSizeInKilobytes(self: win32more.Windows.ApplicationModel.Chat.IRcsTransportConfiguration) -> Int32: ...
    MaxAttachmentCount = property(get_MaxAttachmentCount, None)
    MaxFileSizeInKilobytes = property(get_MaxFileSizeInKilobytes, None)
    MaxGroupMessageSizeInKilobytes = property(get_MaxGroupMessageSizeInKilobytes, None)
    MaxMessageSizeInKilobytes = property(get_MaxMessageSizeInKilobytes, None)
    MaxRecipientCount = property(get_MaxRecipientCount, None)
    WarningFileSizeInKilobytes = property(get_WarningFileSizeInKilobytes, None)
class RemoteParticipantComposingChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.Chat.RemoteParticipantComposingChangedEventArgs'
    @winrt_mixinmethod
    def get_TransportId(self: win32more.Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParticipantAddress(self: win32more.Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsComposing(self: win32more.Windows.ApplicationModel.Chat.IRemoteParticipantComposingChangedEventArgs) -> Boolean: ...
    IsComposing = property(get_IsComposing, None)
    ParticipantAddress = property(get_ParticipantAddress, None)
    TransportId = property(get_TransportId, None)


make_ready(__name__)
