from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Email
import win32more.Windows.ApplicationModel.Email.DataProvider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Win32.System.WinRT
class EmailDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection'
    @winrt_mixinmethod
    def add_MailboxSyncRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MailboxSyncRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadMessageRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadMessageRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadAttachmentRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadAttachmentRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CreateFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeleteFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeleteFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EmptyFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EmptyFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MoveFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MoveFolderRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateMeetingResponseRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateMeetingResponseRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ForwardMeetingRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ForwardMeetingRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProposeNewTimeForMeetingRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProposeNewTimeForMeetingRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SetAutoReplySettingsRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetAutoReplySettingsRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetAutoReplySettingsRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetAutoReplySettingsRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResolveRecipientsRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResolveRecipientsRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ValidateCertificatesRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValidateCertificatesRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ServerSearchReadBatchRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerSearchReadBatchRequested(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection) -> Void: ...
    MailboxSyncRequested = event()
    DownloadMessageRequested = event()
    DownloadAttachmentRequested = event()
    CreateFolderRequested = event()
    DeleteFolderRequested = event()
    EmptyFolderRequested = event()
    MoveFolderRequested = event()
    UpdateMeetingResponseRequested = event()
    ForwardMeetingRequested = event()
    ProposeNewTimeForMeetingRequested = event()
    SetAutoReplySettingsRequested = event()
    GetAutoReplySettingsRequested = event()
    ResolveRecipientsRequested = event()
    ValidateCertificatesRequested = event()
    ServerSearchReadBatchRequested = event()
class EmailDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderTriggerDetails) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection: ...
    Connection = property(get_Connection, None)
class EmailMailboxCreateFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentFolderId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest, folder: win32more.Windows.ApplicationModel.Email.EmailFolder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest, status: win32more.Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Name = property(get_Name, None)
    ParentFolderId = property(get_ParentFolderId, None)
class EmailMailboxCreateFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxDeleteFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest, status: win32more.Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class EmailMailboxDeleteFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxDownloadAttachmentRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailAttachmentId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailAttachmentId = property(get_EmailAttachmentId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
class EmailMailboxDownloadAttachmentRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxDownloadMessageRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
class EmailMailboxDownloadMessageRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxEmptyFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest, status: win32more.Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class EmailMailboxEmptyFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxForwardMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recipients(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ForwardHeaderType(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind: ...
    @winrt_mixinmethod
    def get_ForwardHeader(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    ForwardHeader = property(get_ForwardHeader, None)
    ForwardHeaderType = property(get_ForwardHeaderType, None)
    Recipients = property(get_Recipients, None)
    Subject = property(get_Subject, None)
class EmailMailboxForwardMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxGetAutoReplySettingsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RequestedFormat(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest, autoReplySettings: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    RequestedFormat = property(get_RequestedFormat, None)
class EmailMailboxGetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxMoveFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewParentFolderId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewFolderName(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    NewFolderName = property(get_NewFolderName, None)
    NewParentFolderId = property(get_NewParentFolderId, None)
class EmailMailboxMoveFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxProposeNewTimeForMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewStartTime(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NewDuration(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    NewDuration = property(get_NewDuration, None)
    NewStartTime = property(get_NewStartTime, None)
    Subject = property(get_Subject, None)
class EmailMailboxProposeNewTimeForMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxResolveRecipientsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recipients(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest, resolutionResults: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionResult]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Recipients = property(get_Recipients, None)
class EmailMailboxResolveRecipientsRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxServerSearchReadBatchRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequest'
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_mixinmethod
    def get_SuggestedBatchSize(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> UInt32: ...
    @winrt_mixinmethod
    def SaveMessageAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest, batchStatus: win32more.Windows.ApplicationModel.Email.EmailBatchStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    Options = property(get_Options, None)
    SessionId = property(get_SessionId, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class EmailMailboxServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxSetAutoReplySettingsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AutoReplySettings(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AutoReplySettings = property(get_AutoReplySettings, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class EmailMailboxSetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
class EmailMailboxSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxUpdateMeetingResponseRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> win32more.Windows.ApplicationModel.Email.EmailMeetingResponseType: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SendUpdate(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> Boolean: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    Response = property(get_Response, None)
    SendUpdate = property(get_SendUpdate, None)
    Subject = property(get_Subject, None)
class EmailMailboxUpdateMeetingResponseRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxValidateCertificatesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Certificates(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest, validationStatuses: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Email.EmailCertificateValidationStatus]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    Certificates = property(get_Certificates, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class EmailMailboxValidateCertificatesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequestEventArgs) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection'
    _iid_ = Guid('{3b9c9dc7-37b2-4bf0-ae30-7b644a1c96e1}')
    @winrt_commethod(6)
    def add_MailboxSyncRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MailboxSyncRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_DownloadMessageRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DownloadMessageRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DownloadAttachmentRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DownloadAttachmentRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CreateFolderRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CreateFolderRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_DeleteFolderRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DeleteFolderRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_EmptyFolderRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_EmptyFolderRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_MoveFolderRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_MoveFolderRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_UpdateMeetingResponseRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_UpdateMeetingResponseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_ForwardMeetingRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_ForwardMeetingRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_ProposeNewTimeForMeetingRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_ProposeNewTimeForMeetingRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_SetAutoReplySettingsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_SetAutoReplySettingsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_GetAutoReplySettingsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_GetAutoReplySettingsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_ResolveRecipientsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_ResolveRecipientsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_ValidateCertificatesRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_ValidateCertificatesRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_ServerSearchReadBatchRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_ServerSearchReadBatchRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def Start(self) -> Void: ...
    MailboxSyncRequested = event()
    DownloadMessageRequested = event()
    DownloadAttachmentRequested = event()
    CreateFolderRequested = event()
    DeleteFolderRequested = event()
    EmptyFolderRequested = event()
    MoveFolderRequested = event()
    UpdateMeetingResponseRequested = event()
    ForwardMeetingRequested = event()
    ProposeNewTimeForMeetingRequested = event()
    SetAutoReplySettingsRequested = event()
    GetAutoReplySettingsRequested = event()
    ResolveRecipientsRequested = event()
    ValidateCertificatesRequested = event()
    ServerSearchReadBatchRequested = event()
class IEmailDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderTriggerDetails'
    _iid_ = Guid('{8f3e4e50-341e-45f3-bba0-84a005e1319a}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IEmailMailboxCreateFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest'
    _iid_ = Guid('{184d3775-c921-4c39-a309-e16c9f22b04b}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ParentFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def ReportCompletedAsync(self, folder: win32more.Windows.ApplicationModel.Email.EmailFolder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ReportFailedAsync(self, status: win32more.Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Name = property(get_Name, None)
    ParentFolderId = property(get_ParentFolderId, None)
class IEmailMailboxCreateFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequestEventArgs'
    _iid_ = Guid('{03e4c02c-241c-4ea9-a68f-ff20bc5afc85}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxDeleteFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest'
    _iid_ = Guid('{9469e88a-a931-4779-923d-09a3ea292e29}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self, status: win32more.Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class IEmailMailboxDeleteFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequestEventArgs'
    _iid_ = Guid('{b4d32d06-2332-4678-8378-28b579336846}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxDownloadAttachmentRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest'
    _iid_ = Guid('{0b1dbbb4-750c-48e1-bce4-8d589684ffbc}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EmailAttachmentId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailAttachmentId = property(get_EmailAttachmentId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
class IEmailMailboxDownloadAttachmentRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequestEventArgs'
    _iid_ = Guid('{ccddc46d-ffa8-4877-9f9d-fed7bcaf4104}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxDownloadMessageRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest'
    _iid_ = Guid('{497b4187-5b4d-4b23-816c-f3842beb753e}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
class IEmailMailboxDownloadMessageRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequestEventArgs'
    _iid_ = Guid('{470409ad-d0a0-4a5b-bb2a-37621039c53e}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxEmptyFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest'
    _iid_ = Guid('{fe4b03ab-f86d-46d9-b4ce-bc8a6d9e9268}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self, status: win32more.Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class IEmailMailboxEmptyFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequestEventArgs'
    _iid_ = Guid('{7183f484-985a-4ac0-b33f-ee0e2627a3c0}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxForwardMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest'
    _iid_ = Guid('{616d6af1-70d4-4832-b869-b80542ae9be8}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Recipients(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_commethod(9)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ForwardHeaderType(self) -> win32more.Windows.ApplicationModel.Email.EmailMessageBodyKind: ...
    @winrt_commethod(11)
    def get_ForwardHeader(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    ForwardHeader = property(get_ForwardHeader, None)
    ForwardHeaderType = property(get_ForwardHeaderType, None)
    Recipients = property(get_Recipients, None)
    Subject = property(get_Subject, None)
class IEmailMailboxForwardMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequestEventArgs'
    _iid_ = Guid('{2bd8f33a-2974-4759-a5a5-58f44d3c0275}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxGetAutoReplySettingsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest'
    _iid_ = Guid('{9b380789-1e88-4e01-84cc-1386ad9a2c2f}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RequestedFormat(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, autoReplySettings: win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    RequestedFormat = property(get_RequestedFormat, None)
class IEmailMailboxGetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequestEventArgs'
    _iid_ = Guid('{d79f55c2-fd45-4004-8a91-9bacf38b7022}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxMoveFolderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest'
    _iid_ = Guid('{10ba2856-4a95-4068-91cc-67cc7acf454f}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NewParentFolderId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_NewFolderName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    NewFolderName = property(get_NewFolderName, None)
    NewParentFolderId = property(get_NewParentFolderId, None)
class IEmailMailboxMoveFolderRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequestEventArgs'
    _iid_ = Guid('{38623020-14ba-4c88-8698-7239e3c8aaa7}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxProposeNewTimeForMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest'
    _iid_ = Guid('{5aeff152-9799-4f9f-a399-ff07f3eef04e}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NewStartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_NewDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    NewDuration = property(get_NewDuration, None)
    NewStartTime = property(get_NewStartTime, None)
    Subject = property(get_Subject, None)
class IEmailMailboxProposeNewTimeForMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequestEventArgs'
    _iid_ = Guid('{fb480b98-33ad-4a67-8251-0f9c249b6a20}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxResolveRecipientsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest'
    _iid_ = Guid('{efa4cf70-7b39-4c9b-811e-41eaf43a332d}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Recipients(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, resolutionResults: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Email.EmailRecipientResolutionResult]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Recipients = property(get_Recipients, None)
class IEmailMailboxResolveRecipientsRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequestEventArgs'
    _iid_ = Guid('{260f9e02-b2cf-40f8-8c28-e3ed43b1e89a}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxServerSearchReadBatchRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest'
    _iid_ = Guid('{090eebdf-5a96-41d3-8ad8-34912f9aa60e}')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Options(self) -> win32more.Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_commethod(10)
    def get_SuggestedBatchSize(self) -> UInt32: ...
    @winrt_commethod(11)
    def SaveMessageAsync(self, message: win32more.Windows.ApplicationModel.Email.EmailMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self, batchStatus: win32more.Windows.ApplicationModel.Email.EmailBatchStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailFolderId = property(get_EmailFolderId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    Options = property(get_Options, None)
    SessionId = property(get_SessionId, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class IEmailMailboxServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequestEventArgs'
    _iid_ = Guid('{14101b4e-ed9e-45d1-ad7a-cc9b7f643ae2}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxSetAutoReplySettingsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest'
    _iid_ = Guid('{75a422d0-a88e-4e54-8dc7-c243186b774e}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AutoReplySettings(self) -> win32more.Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AutoReplySettings = property(get_AutoReplySettings, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class IEmailMailboxSetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequestEventArgs'
    _iid_ = Guid('{09da11ad-d7ca-4087-ac86-53fa67f76246}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest'
    _iid_ = Guid('{4e10e8e4-7e67-405a-b673-dc60c91090fc}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
class IEmailMailboxSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequestEventArgs'
    _iid_ = Guid('{439a031a-8fcc-4ae5-b9b5-d434e0a65aa8}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxUpdateMeetingResponseRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest'
    _iid_ = Guid('{5b99ac93-b2cf-4888-ba4f-306b6b66df30}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Response(self) -> win32more.Windows.ApplicationModel.Email.EmailMeetingResponseType: ...
    @winrt_commethod(9)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SendUpdate(self) -> Boolean: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    Response = property(get_Response, None)
    SendUpdate = property(get_SendUpdate, None)
    Subject = property(get_Subject, None)
class IEmailMailboxUpdateMeetingResponseRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequestEventArgs'
    _iid_ = Guid('{6898d761-56c9-4f17-be31-66fda94ba159}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxValidateCertificatesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest'
    _iid_ = Guid('{a94d3931-e11a-4f97-b81a-187a70a8f41a}')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Certificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, validationStatuses: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Email.EmailCertificateValidationStatus]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Certificates = property(get_Certificates, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
class IEmailMailboxValidateCertificatesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequestEventArgs'
    _iid_ = Guid('{2583bf17-02ff-49fe-a73c-03f37566c691}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)


make_ready(__name__)
