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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Email
import Windows.ApplicationModel.Email.DataProvider
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Cryptography.Certificates
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class EmailDataProviderConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection'
    @winrt_mixinmethod
    def add_MailboxSyncRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MailboxSyncRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadMessageRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadMessageRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadAttachmentRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadAttachmentRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CreateFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeleteFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeleteFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EmptyFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EmptyFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MoveFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MoveFolderRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateMeetingResponseRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateMeetingResponseRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ForwardMeetingRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ForwardMeetingRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProposeNewTimeForMeetingRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProposeNewTimeForMeetingRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SetAutoReplySettingsRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetAutoReplySettingsRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetAutoReplySettingsRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetAutoReplySettingsRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResolveRecipientsRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResolveRecipientsRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ValidateCertificatesRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValidateCertificatesRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ServerSearchReadBatchRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerSearchReadBatchRequested(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderConnection) -> Void: ...
class EmailDataProviderTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: Windows.ApplicationModel.Email.DataProvider.IEmailDataProviderTriggerDetails) -> Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection: ...
    Connection = property(get_Connection, None)
class EmailMailboxCreateFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentFolderId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest, folder: Windows.ApplicationModel.Email.EmailFolder) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequest, status: Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    ParentFolderId = property(get_ParentFolderId, None)
    Name = property(get_Name, None)
class EmailMailboxCreateFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxCreateFolderRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxDeleteFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequest, status: Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
class EmailMailboxDeleteFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDeleteFolderRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxDownloadAttachmentRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailAttachmentId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    EmailAttachmentId = property(get_EmailAttachmentId, None)
class EmailMailboxDownloadAttachmentRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadAttachmentRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxDownloadMessageRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
class EmailMailboxDownloadMessageRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxDownloadMessageRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxEmptyFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequest, status: Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
class EmailMailboxEmptyFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxEmptyFolderRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxForwardMeetingRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recipients(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ForwardHeaderType(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> Windows.ApplicationModel.Email.EmailMessageBodyKind: ...
    @winrt_mixinmethod
    def get_ForwardHeader(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    Recipients = property(get_Recipients, None)
    Subject = property(get_Subject, None)
    ForwardHeaderType = property(get_ForwardHeaderType, None)
    ForwardHeader = property(get_ForwardHeader, None)
    Comment = property(get_Comment, None)
class EmailMailboxForwardMeetingRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxForwardMeetingRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxGetAutoReplySettingsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RequestedFormat(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest) -> Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest, autoReplySettings: Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    RequestedFormat = property(get_RequestedFormat, None)
class EmailMailboxGetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxGetAutoReplySettingsRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxMoveFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewParentFolderId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewFolderName(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
    NewParentFolderId = property(get_NewParentFolderId, None)
    NewFolderName = property(get_NewFolderName, None)
class EmailMailboxMoveFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxMoveFolderRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxProposeNewTimeForMeetingRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewStartTime(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NewDuration(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    NewStartTime = property(get_NewStartTime, None)
    NewDuration = property(get_NewDuration, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
class EmailMailboxProposeNewTimeForMeetingRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxProposeNewTimeForMeetingRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxResolveRecipientsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recipients(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest, resolutionResults: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Email.EmailRecipientResolutionResult]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Recipients = property(get_Recipients, None)
class EmailMailboxResolveRecipientsRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxResolveRecipientsRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxServerSearchReadBatchRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequest'
    @winrt_mixinmethod
    def get_SessionId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailFolderId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_mixinmethod
    def get_SuggestedBatchSize(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> UInt32: ...
    @winrt_mixinmethod
    def SaveMessageAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest, message: Windows.ApplicationModel.Email.EmailMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequest, batchStatus: Windows.ApplicationModel.Email.EmailBatchStatus) -> Windows.Foundation.IAsyncAction: ...
    SessionId = property(get_SessionId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
    Options = property(get_Options, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class EmailMailboxServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxServerSearchReadBatchRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxSetAutoReplySettingsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AutoReplySettings(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    AutoReplySettings = property(get_AutoReplySettings, None)
class EmailMailboxSetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSetAutoReplySettingsRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxSyncManagerSyncRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
class EmailMailboxSyncManagerSyncRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxSyncManagerSyncRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxUpdateMeetingResponseRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessageId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Response(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> Windows.ApplicationModel.Email.EmailMeetingResponseType: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SendUpdate(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> Boolean: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    Response = property(get_Response, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
    SendUpdate = property(get_SendUpdate, None)
class EmailMailboxUpdateMeetingResponseRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxUpdateMeetingResponseRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class EmailMailboxValidateCertificatesRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequest'
    @winrt_mixinmethod
    def get_EmailMailboxId(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Certificates(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest, validationStatuses: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Email.EmailCertificateValidationStatus]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequest) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Certificates = property(get_Certificates, None)
class EmailMailboxValidateCertificatesRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequestEventArgs) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Email.DataProvider.IEmailMailboxValidateCertificatesRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailDataProviderConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3b9c9dc7-37b2-4bf0-ae-30-7b-64-4a-1c-96-e1')
    @winrt_commethod(6)
    def add_MailboxSyncRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MailboxSyncRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_DownloadMessageRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DownloadMessageRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DownloadAttachmentRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DownloadAttachmentRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CreateFolderRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CreateFolderRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_DeleteFolderRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DeleteFolderRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_EmptyFolderRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_EmptyFolderRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_MoveFolderRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_MoveFolderRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_UpdateMeetingResponseRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_UpdateMeetingResponseRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_ForwardMeetingRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_ForwardMeetingRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_ProposeNewTimeForMeetingRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_ProposeNewTimeForMeetingRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_SetAutoReplySettingsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_SetAutoReplySettingsRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_GetAutoReplySettingsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_GetAutoReplySettingsRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_ResolveRecipientsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_ResolveRecipientsRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_ValidateCertificatesRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_ValidateCertificatesRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_ServerSearchReadBatchRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection, Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_ServerSearchReadBatchRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def Start(self) -> Void: ...
class IEmailDataProviderTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8f3e4e50-341e-45f3-bb-a0-84-a0-05-e1-31-9a')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.ApplicationModel.Email.DataProvider.EmailDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IEmailMailboxCreateFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('184d3775-c921-4c39-a3-09-e1-6c-9f-22-b0-4b')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ParentFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def ReportCompletedAsync(self, folder: Windows.ApplicationModel.Email.EmailFolder) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ReportFailedAsync(self, status: Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    ParentFolderId = property(get_ParentFolderId, None)
    Name = property(get_Name, None)
class IEmailMailboxCreateFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('03e4c02c-241c-4ea9-a6-8f-ff-20-bc-5a-fc-85')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxCreateFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxDeleteFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9469e88a-a931-4779-92-3d-09-a3-ea-29-2e-29')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self, status: Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
class IEmailMailboxDeleteFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b4d32d06-2332-4678-83-78-28-b5-79-33-68-46')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxDeleteFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxDownloadAttachmentRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0b1dbbb4-750c-48e1-bc-e4-8d-58-96-84-ff-bc')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EmailAttachmentId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    EmailAttachmentId = property(get_EmailAttachmentId, None)
class IEmailMailboxDownloadAttachmentRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ccddc46d-ffa8-4877-9f-9d-fe-d7-bc-af-41-04')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadAttachmentRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxDownloadMessageRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('497b4187-5b4d-4b23-81-6c-f3-84-2b-eb-75-3e')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
class IEmailMailboxDownloadMessageRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('470409ad-d0a0-4a5b-bb-2a-37-62-10-39-c5-3e')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxDownloadMessageRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxEmptyFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fe4b03ab-f86d-46d9-b4-ce-bc-8a-6d-9e-92-68')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self, status: Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
class IEmailMailboxEmptyFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7183f484-985a-4ac0-b3-3f-ee-0e-26-27-a3-c0')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxEmptyFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxForwardMeetingRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('616d6af1-70d4-4832-b8-69-b8-05-42-ae-9b-e8')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Recipients(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Email.EmailRecipient]: ...
    @winrt_commethod(9)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ForwardHeaderType(self) -> Windows.ApplicationModel.Email.EmailMessageBodyKind: ...
    @winrt_commethod(11)
    def get_ForwardHeader(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    Recipients = property(get_Recipients, None)
    Subject = property(get_Subject, None)
    ForwardHeaderType = property(get_ForwardHeaderType, None)
    ForwardHeader = property(get_ForwardHeader, None)
    Comment = property(get_Comment, None)
class IEmailMailboxForwardMeetingRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2bd8f33a-2974-4759-a5-a5-58-f4-4d-3c-02-75')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxForwardMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxGetAutoReplySettingsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9b380789-1e88-4e01-84-cc-13-86-ad-9a-2c-2f')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RequestedFormat(self) -> Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, autoReplySettings: Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    RequestedFormat = property(get_RequestedFormat, None)
class IEmailMailboxGetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d79f55c2-fd45-4004-8a-91-9b-ac-f3-8b-70-22')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxGetAutoReplySettingsRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxMoveFolderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('10ba2856-4a95-4068-91-cc-67-cc-7a-cf-45-4f')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NewParentFolderId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_NewFolderName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
    NewParentFolderId = property(get_NewParentFolderId, None)
    NewFolderName = property(get_NewFolderName, None)
class IEmailMailboxMoveFolderRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38623020-14ba-4c88-86-98-72-39-e3-c8-aa-a7')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxMoveFolderRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxProposeNewTimeForMeetingRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5aeff152-9799-4f9f-a3-99-ff-07-f3-ee-f0-4e')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_NewStartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_NewDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    NewStartTime = property(get_NewStartTime, None)
    NewDuration = property(get_NewDuration, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
class IEmailMailboxProposeNewTimeForMeetingRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fb480b98-33ad-4a67-82-51-0f-9c-24-9b-6a-20')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxProposeNewTimeForMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxResolveRecipientsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('efa4cf70-7b39-4c9b-81-1e-41-ea-f4-3a-33-2d')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Recipients(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, resolutionResults: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Email.EmailRecipientResolutionResult]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Recipients = property(get_Recipients, None)
class IEmailMailboxResolveRecipientsRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('260f9e02-b2cf-40f8-8c-28-e3-ed-43-b1-e8-9a')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxResolveRecipientsRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxServerSearchReadBatchRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('090eebdf-5a96-41d3-8a-d8-34-91-2f-9a-a6-0e')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EmailFolderId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Options(self) -> Windows.ApplicationModel.Email.EmailQueryOptions: ...
    @winrt_commethod(10)
    def get_SuggestedBatchSize(self) -> UInt32: ...
    @winrt_commethod(11)
    def SaveMessageAsync(self, message: Windows.ApplicationModel.Email.EmailMessage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self, batchStatus: Windows.ApplicationModel.Email.EmailBatchStatus) -> Windows.Foundation.IAsyncAction: ...
    SessionId = property(get_SessionId, None)
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailFolderId = property(get_EmailFolderId, None)
    Options = property(get_Options, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class IEmailMailboxServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('14101b4e-ed9e-45d1-ad-7a-cc-9b-7f-64-3a-e2')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxServerSearchReadBatchRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxSetAutoReplySettingsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('75a422d0-a88e-4e54-8d-c7-c2-43-18-6b-77-4e')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AutoReplySettings(self) -> Windows.ApplicationModel.Email.EmailMailboxAutoReplySettings: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    AutoReplySettings = property(get_AutoReplySettings, None)
class IEmailMailboxSetAutoReplySettingsRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('09da11ad-d7ca-4087-ac-86-53-fa-67-f7-62-46')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxSetAutoReplySettingsRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxSyncManagerSyncRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4e10e8e4-7e67-405a-b6-73-dc-60-c9-10-90-fc')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
class IEmailMailboxSyncManagerSyncRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('439a031a-8fcc-4ae5-b9-b5-d4-34-e0-a6-5a-a8')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxUpdateMeetingResponseRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5b99ac93-b2cf-4888-ba-4f-30-6b-6b-66-df-30')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EmailMessageId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Response(self) -> Windows.ApplicationModel.Email.EmailMeetingResponseType: ...
    @winrt_commethod(9)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SendUpdate(self) -> Boolean: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    EmailMessageId = property(get_EmailMessageId, None)
    Response = property(get_Response, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
    SendUpdate = property(get_SendUpdate, None)
class IEmailMailboxUpdateMeetingResponseRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6898d761-56c9-4f17-be-31-66-fd-a9-4b-a1-59')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxUpdateMeetingResponseRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IEmailMailboxValidateCertificatesRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a94d3931-e11a-4f97-b8-1a-18-7a-70-a8-f4-1a')
    @winrt_commethod(6)
    def get_EmailMailboxId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Certificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, validationStatuses: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Email.EmailCertificateValidationStatus]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EmailMailboxId = property(get_EmailMailboxId, None)
    Certificates = property(get_Certificates, None)
class IEmailMailboxValidateCertificatesRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2583bf17-02ff-49fe-a7-3c-03-f3-75-66-c6-91')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Email.DataProvider.EmailMailboxValidateCertificatesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
make_head(_module, 'EmailDataProviderConnection')
make_head(_module, 'EmailDataProviderTriggerDetails')
make_head(_module, 'EmailMailboxCreateFolderRequest')
make_head(_module, 'EmailMailboxCreateFolderRequestEventArgs')
make_head(_module, 'EmailMailboxDeleteFolderRequest')
make_head(_module, 'EmailMailboxDeleteFolderRequestEventArgs')
make_head(_module, 'EmailMailboxDownloadAttachmentRequest')
make_head(_module, 'EmailMailboxDownloadAttachmentRequestEventArgs')
make_head(_module, 'EmailMailboxDownloadMessageRequest')
make_head(_module, 'EmailMailboxDownloadMessageRequestEventArgs')
make_head(_module, 'EmailMailboxEmptyFolderRequest')
make_head(_module, 'EmailMailboxEmptyFolderRequestEventArgs')
make_head(_module, 'EmailMailboxForwardMeetingRequest')
make_head(_module, 'EmailMailboxForwardMeetingRequestEventArgs')
make_head(_module, 'EmailMailboxGetAutoReplySettingsRequest')
make_head(_module, 'EmailMailboxGetAutoReplySettingsRequestEventArgs')
make_head(_module, 'EmailMailboxMoveFolderRequest')
make_head(_module, 'EmailMailboxMoveFolderRequestEventArgs')
make_head(_module, 'EmailMailboxProposeNewTimeForMeetingRequest')
make_head(_module, 'EmailMailboxProposeNewTimeForMeetingRequestEventArgs')
make_head(_module, 'EmailMailboxResolveRecipientsRequest')
make_head(_module, 'EmailMailboxResolveRecipientsRequestEventArgs')
make_head(_module, 'EmailMailboxServerSearchReadBatchRequest')
make_head(_module, 'EmailMailboxServerSearchReadBatchRequestEventArgs')
make_head(_module, 'EmailMailboxSetAutoReplySettingsRequest')
make_head(_module, 'EmailMailboxSetAutoReplySettingsRequestEventArgs')
make_head(_module, 'EmailMailboxSyncManagerSyncRequest')
make_head(_module, 'EmailMailboxSyncManagerSyncRequestEventArgs')
make_head(_module, 'EmailMailboxUpdateMeetingResponseRequest')
make_head(_module, 'EmailMailboxUpdateMeetingResponseRequestEventArgs')
make_head(_module, 'EmailMailboxValidateCertificatesRequest')
make_head(_module, 'EmailMailboxValidateCertificatesRequestEventArgs')
make_head(_module, 'IEmailDataProviderConnection')
make_head(_module, 'IEmailDataProviderTriggerDetails')
make_head(_module, 'IEmailMailboxCreateFolderRequest')
make_head(_module, 'IEmailMailboxCreateFolderRequestEventArgs')
make_head(_module, 'IEmailMailboxDeleteFolderRequest')
make_head(_module, 'IEmailMailboxDeleteFolderRequestEventArgs')
make_head(_module, 'IEmailMailboxDownloadAttachmentRequest')
make_head(_module, 'IEmailMailboxDownloadAttachmentRequestEventArgs')
make_head(_module, 'IEmailMailboxDownloadMessageRequest')
make_head(_module, 'IEmailMailboxDownloadMessageRequestEventArgs')
make_head(_module, 'IEmailMailboxEmptyFolderRequest')
make_head(_module, 'IEmailMailboxEmptyFolderRequestEventArgs')
make_head(_module, 'IEmailMailboxForwardMeetingRequest')
make_head(_module, 'IEmailMailboxForwardMeetingRequestEventArgs')
make_head(_module, 'IEmailMailboxGetAutoReplySettingsRequest')
make_head(_module, 'IEmailMailboxGetAutoReplySettingsRequestEventArgs')
make_head(_module, 'IEmailMailboxMoveFolderRequest')
make_head(_module, 'IEmailMailboxMoveFolderRequestEventArgs')
make_head(_module, 'IEmailMailboxProposeNewTimeForMeetingRequest')
make_head(_module, 'IEmailMailboxProposeNewTimeForMeetingRequestEventArgs')
make_head(_module, 'IEmailMailboxResolveRecipientsRequest')
make_head(_module, 'IEmailMailboxResolveRecipientsRequestEventArgs')
make_head(_module, 'IEmailMailboxServerSearchReadBatchRequest')
make_head(_module, 'IEmailMailboxServerSearchReadBatchRequestEventArgs')
make_head(_module, 'IEmailMailboxSetAutoReplySettingsRequest')
make_head(_module, 'IEmailMailboxSetAutoReplySettingsRequestEventArgs')
make_head(_module, 'IEmailMailboxSyncManagerSyncRequest')
make_head(_module, 'IEmailMailboxSyncManagerSyncRequestEventArgs')
make_head(_module, 'IEmailMailboxUpdateMeetingResponseRequest')
make_head(_module, 'IEmailMailboxUpdateMeetingResponseRequestEventArgs')
make_head(_module, 'IEmailMailboxValidateCertificatesRequest')
make_head(_module, 'IEmailMailboxValidateCertificatesRequestEventArgs')
