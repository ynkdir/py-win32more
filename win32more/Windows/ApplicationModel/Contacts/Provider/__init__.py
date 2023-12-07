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
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.Contacts.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
AddContactResult = Int32
AddContactResult_Added: AddContactResult = 0
AddContactResult_AlreadyAdded: AddContactResult = 1
AddContactResult_Unavailable: AddContactResult = 2
class ContactPickerUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.ContactPickerUI'
    @winrt_overload
    @winrt_mixinmethod
    def AddContact(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, id: WinRT_String, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_mixinmethod
    def RemoveContact(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsContact(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, id: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def get_DesiredFields(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SelectionMode(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI) -> win32more.Windows.ApplicationModel.Contacts.ContactSelectionMode: ...
    @winrt_mixinmethod
    def add_ContactRemoved(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.Provider.ContactPickerUI, win32more.Windows.ApplicationModel.Contacts.Provider.ContactRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContactRemoved(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @AddContact.register
    @winrt_mixinmethod
    def AddContact(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI2, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_mixinmethod
    def get_DesiredFieldsWithContactFieldType(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactPickerUI2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactFieldType]: ...
    DesiredFields = property(get_DesiredFields, None)
    SelectionMode = property(get_SelectionMode, None)
    DesiredFieldsWithContactFieldType = property(get_DesiredFieldsWithContactFieldType, None)
class ContactRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.Provider.IContactRemovedEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.ContactRemovedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Contacts.Provider.IContactRemovedEventArgs) -> WinRT_String: ...
    Id = property(get_Id, None)
class IContactPickerUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.IContactPickerUI'
    _iid_ = Guid('{e2cc1366-cf66-43c4-a96a-a5a112db4746}')
    @winrt_commethod(6)
    def AddContact(self, id: WinRT_String, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_commethod(7)
    def RemoveContact(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def ContainsContact(self, id: WinRT_String) -> Boolean: ...
    @winrt_commethod(9)
    def get_DesiredFields(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_SelectionMode(self) -> win32more.Windows.ApplicationModel.Contacts.ContactSelectionMode: ...
    @winrt_commethod(11)
    def add_ContactRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.Provider.ContactPickerUI, win32more.Windows.ApplicationModel.Contacts.Provider.ContactRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ContactRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredFields = property(get_DesiredFields, None)
    SelectionMode = property(get_SelectionMode, None)
class IContactPickerUI2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.IContactPickerUI2'
    _iid_ = Guid('{6e449e28-7b25-4999-9b0b-875400a1e8c8}')
    @winrt_commethod(6)
    def AddContact(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_commethod(7)
    def get_DesiredFieldsWithContactFieldType(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Contacts.ContactFieldType]: ...
    DesiredFieldsWithContactFieldType = property(get_DesiredFieldsWithContactFieldType, None)
class IContactRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.IContactRemovedEventArgs'
    _iid_ = Guid('{6f354338-3302-4d13-ad8d-adcc0ff9e47c}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
make_ready(__name__)
