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
import Windows.ApplicationModel.Contacts
import Windows.ApplicationModel.Contacts.DataProvider
import Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ContactDataProviderConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection'
    @winrt_mixinmethod
    def add_SyncRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ServerSearchReadBatchRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerSearchReadBatchRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection) -> Void: ...
    @winrt_mixinmethod
    def add_CreateOrUpdateContactRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateOrUpdateContactRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeleteContactRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeleteContactRequested(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ContactDataProviderTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderTriggerDetails) -> Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection: ...
    Connection = property(get_Connection, None)
class ContactListCreateOrUpdateContactRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequest'
    @winrt_mixinmethod
    def get_ContactListId(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest, createdOrUpdatedContact: Windows.ApplicationModel.Contacts.Contact) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest) -> Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    Contact = property(get_Contact, None)
class ContactListCreateOrUpdateContactRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class ContactListDeleteContactRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequest'
    @winrt_mixinmethod
    def get_ContactListId(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactId(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    ContactId = property(get_ContactId, None)
class ContactListDeleteContactRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class ContactListServerSearchReadBatchRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequest'
    @winrt_mixinmethod
    def get_SessionId(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactListId(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_mixinmethod
    def get_SuggestedBatchSize(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> UInt32: ...
    @winrt_mixinmethod
    def SaveContactAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest, contact: Windows.ApplicationModel.Contacts.Contact) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest, batchStatus: Windows.ApplicationModel.Contacts.ContactBatchStatus) -> Windows.Foundation.IAsyncAction: ...
    SessionId = property(get_SessionId, None)
    ContactListId = property(get_ContactListId, None)
    Options = property(get_Options, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class ContactListServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class ContactListSyncManagerSyncRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_ContactListId(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
class ContactListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactDataProviderConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1a398a52-8c9d-4d6f-a4e0-111e9a125a30}')
    @winrt_commethod(6)
    def add_SyncRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SyncRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ServerSearchReadBatchRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ServerSearchReadBatchRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def Start(self) -> Void: ...
class IContactDataProviderConnection2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a1d327b0-196c-4bfd-8f0f-c68d67f249d3}')
    @winrt_commethod(6)
    def add_CreateOrUpdateContactRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CreateOrUpdateContactRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_DeleteContactRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DeleteContactRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IContactDataProviderTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{527104be-3c62-43c8-9ae7-db531685cd99}')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IContactListCreateOrUpdateContactRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b4af411f-c849-47d0-b119-91cf605b2f2a}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, createdOrUpdatedContact: Windows.ApplicationModel.Contacts.Contact) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    Contact = property(get_Contact, None)
class IContactListCreateOrUpdateContactRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{851c1690-1a51-4b0c-aeef-1240ac5bed75}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactListDeleteContactRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5e114687-ce03-4de5-8557-9ccf552d472a}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContactId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    ContactId = property(get_ContactId, None)
class IContactListDeleteContactRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b22054a1-e8fa-4db5-9389-2d12ee7d15ee}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactListServerSearchReadBatchRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ba776a97-4030-4925-9fb4-143b295e653b}')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Options(self) -> Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_commethod(9)
    def get_SuggestedBatchSize(self) -> UInt32: ...
    @winrt_commethod(10)
    def SaveContactAsync(self, contact: Windows.ApplicationModel.Contacts.Contact) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReportFailedAsync(self, batchStatus: Windows.ApplicationModel.Contacts.ContactBatchStatus) -> Windows.Foundation.IAsyncAction: ...
    SessionId = property(get_SessionId, None)
    ContactListId = property(get_ContactListId, None)
    Options = property(get_Options, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class IContactListServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1a27e87b-69d7-4e4e-8042-861cba61471e}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactListSyncManagerSyncRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3c0e57a4-c4e7-4970-9a8f-9a66a2bb6c1a}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
class IContactListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{158e4dac-446d-4f10-afc2-02683ec533a6}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
make_head(_module, 'ContactDataProviderConnection')
make_head(_module, 'ContactDataProviderTriggerDetails')
make_head(_module, 'ContactListCreateOrUpdateContactRequest')
make_head(_module, 'ContactListCreateOrUpdateContactRequestEventArgs')
make_head(_module, 'ContactListDeleteContactRequest')
make_head(_module, 'ContactListDeleteContactRequestEventArgs')
make_head(_module, 'ContactListServerSearchReadBatchRequest')
make_head(_module, 'ContactListServerSearchReadBatchRequestEventArgs')
make_head(_module, 'ContactListSyncManagerSyncRequest')
make_head(_module, 'ContactListSyncManagerSyncRequestEventArgs')
make_head(_module, 'IContactDataProviderConnection')
make_head(_module, 'IContactDataProviderConnection2')
make_head(_module, 'IContactDataProviderTriggerDetails')
make_head(_module, 'IContactListCreateOrUpdateContactRequest')
make_head(_module, 'IContactListCreateOrUpdateContactRequestEventArgs')
make_head(_module, 'IContactListDeleteContactRequest')
make_head(_module, 'IContactListDeleteContactRequestEventArgs')
make_head(_module, 'IContactListServerSearchReadBatchRequest')
make_head(_module, 'IContactListServerSearchReadBatchRequestEventArgs')
make_head(_module, 'IContactListSyncManagerSyncRequest')
make_head(_module, 'IContactListSyncManagerSyncRequestEventArgs')
