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
import Windows.ApplicationModel.Contacts.Provider
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AddContactResult = Int32
AddContactResult_Added: AddContactResult = 0
AddContactResult_AlreadyAdded: AddContactResult = 1
AddContactResult_Unavailable: AddContactResult = 2
class ContactPickerUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.ContactPickerUI'
    @winrt_mixinmethod
    def AddContact(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, id: WinRT_String, contact: Windows.ApplicationModel.Contacts.Contact) -> Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_mixinmethod
    def RemoveContact(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsContact(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, id: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def get_DesiredFields(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SelectionMode(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI) -> Windows.ApplicationModel.Contacts.ContactSelectionMode: ...
    @winrt_mixinmethod
    def add_ContactRemoved(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.Provider.ContactPickerUI, Windows.ApplicationModel.Contacts.Provider.ContactRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContactRemoved(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddContact(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI, contact: Windows.ApplicationModel.Contacts.Contact) -> Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_mixinmethod
    def get_DesiredFieldsWithContactFieldType(self: Windows.ApplicationModel.Contacts.Provider.IContactPickerUI2) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Contacts.ContactFieldType]: ...
    DesiredFields = property(get_DesiredFields, None)
    SelectionMode = property(get_SelectionMode, None)
    DesiredFieldsWithContactFieldType = property(get_DesiredFieldsWithContactFieldType, None)
class ContactRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Contacts.Provider.IContactRemovedEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.ContactRemovedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.Contacts.Provider.IContactRemovedEventArgs) -> WinRT_String: ...
    Id = property(get_Id, None)
class IContactPickerUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.IContactPickerUI'
    _iid_ = Guid('{e2cc1366-cf66-43c4-a96a-a5a112db4746}')
    @winrt_commethod(6)
    def AddContact(self, id: WinRT_String, contact: Windows.ApplicationModel.Contacts.Contact) -> Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_commethod(7)
    def RemoveContact(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def ContainsContact(self, id: WinRT_String) -> Boolean: ...
    @winrt_commethod(9)
    def get_DesiredFields(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_SelectionMode(self) -> Windows.ApplicationModel.Contacts.ContactSelectionMode: ...
    @winrt_commethod(11)
    def add_ContactRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Contacts.Provider.ContactPickerUI, Windows.ApplicationModel.Contacts.Provider.ContactRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ContactRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredFields = property(get_DesiredFields, None)
    SelectionMode = property(get_SelectionMode, None)
class IContactPickerUI2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.IContactPickerUI2'
    _iid_ = Guid('{6e449e28-7b25-4999-9b0b-875400a1e8c8}')
    @winrt_commethod(6)
    def AddContact(self, contact: Windows.ApplicationModel.Contacts.Contact) -> Windows.ApplicationModel.Contacts.Provider.AddContactResult: ...
    @winrt_commethod(7)
    def get_DesiredFieldsWithContactFieldType(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Contacts.ContactFieldType]: ...
    DesiredFieldsWithContactFieldType = property(get_DesiredFieldsWithContactFieldType, None)
class IContactRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.Provider.IContactRemovedEventArgs'
    _iid_ = Guid('{6f354338-3302-4d13-ad8d-adcc0ff9e47c}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
make_head(_module, 'ContactPickerUI')
make_head(_module, 'ContactRemovedEventArgs')
make_head(_module, 'IContactPickerUI')
make_head(_module, 'IContactPickerUI2')
make_head(_module, 'IContactRemovedEventArgs')
