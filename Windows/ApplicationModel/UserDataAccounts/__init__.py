from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Appointments
import Windows.ApplicationModel.Contacts
import Windows.ApplicationModel.Email
import Windows.ApplicationModel.UserDataAccounts
import Windows.ApplicationModel.UserDataTasks
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IUserDataAccount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount'
    _iid_ = Guid('{b9c4367e-b348-4910-be94-4ad4bba6dea7}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_UserDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_OtherAppReadAccess(self) -> Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess: ...
    @winrt_commethod(10)
    def put_OtherAppReadAccess(self, value: Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess) -> Void: ...
    @winrt_commethod(11)
    def get_Icon(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(12)
    def get_DeviceAccountTypeId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def SaveAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def DeleteAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def FindAppointmentCalendarsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Appointments.AppointmentCalendar]]: ...
    @winrt_commethod(17)
    def FindEmailMailboxesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Email.EmailMailbox]]: ...
    @winrt_commethod(18)
    def FindContactListsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.ContactList]]: ...
    @winrt_commethod(19)
    def FindContactAnnotationListsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.ContactAnnotationList]]: ...
    Id = property(get_Id, None)
    UserDisplayName = property(get_UserDisplayName, put_UserDisplayName)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    Icon = property(get_Icon, None)
    DeviceAccountTypeId = property(get_DeviceAccountTypeId, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class IUserDataAccount2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount2'
    _iid_ = Guid('{078cd89f-de82-404b-8195-c8a3ac198f60}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsProtectedUnderLock(self) -> Boolean: ...
    EnterpriseId = property(get_EnterpriseId, None)
    IsProtectedUnderLock = property(get_IsProtectedUnderLock, None)
class IUserDataAccount3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3'
    _iid_ = Guid('{01533845-6c43-4286-9d69-3e1709a1f266}')
    @winrt_commethod(6)
    def get_ExplictReadAccessPackageFamilyNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    ExplictReadAccessPackageFamilyNames = property(get_ExplictReadAccessPackageFamilyNames, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
class IUserDataAccount4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4'
    _iid_ = Guid('{c4315210-eae5-4f0a-a8b2-1cca115e008f}')
    @winrt_commethod(6)
    def get_CanShowCreateContactGroup(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanShowCreateContactGroup(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ProviderProperties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def FindUserDataTaskListsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_commethod(10)
    def FindContactGroupsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.ContactGroup]]: ...
    @winrt_commethod(11)
    def TryShowCreateContactGroupAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(12)
    def put_IsProtectedUnderLock(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def put_Icon(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    CanShowCreateContactGroup = property(get_CanShowCreateContactGroup, put_CanShowCreateContactGroup)
    ProviderProperties = property(get_ProviderProperties, None)
    IsProtectedUnderLock = property(None, put_IsProtectedUnderLock)
    Icon = property(None, put_Icon)
class IUserDataAccountManagerForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser'
    _iid_ = Guid('{56a6e8db-db8f-41ab-a65f-8c5971aac982}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, storeAccessType: Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IUserDataAccountManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics'
    _iid_ = Guid('{0d9b89ea-1928-4a20-86d5-3c737f7dc3b0}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, storeAccessType: Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_commethod(7)
    def ShowAddAccountAsync(self, contentKinds: Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def ShowAccountSettingsAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ShowAccountErrorResolverAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IUserDataAccountManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics2'
    _iid_ = Guid('{6a3ded88-316b-435e-b534-f7d4b4b7dba6}')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.ApplicationModel.UserDataAccounts.UserDataAccountManagerForUser: ...
class IUserDataAccountStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore'
    _iid_ = Guid('{2073b0ad-7d0a-4e76-bf45-2368f978a59a}')
    @winrt_commethod(6)
    def FindAccountsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]]: ...
    @winrt_commethod(7)
    def GetAccountAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_commethod(8)
    def CreateAccountAsync(self, userDisplayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
class IUserDataAccountStore2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2'
    _iid_ = Guid('{b1e0aef7-9560-4631-8af0-061d30161469}')
    @winrt_commethod(6)
    def CreateAccountWithPackageRelativeAppIdAsync(self, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_commethod(7)
    def add_StoreChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore, Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StoreChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUserDataAccountStore3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore3'
    _iid_ = Guid('{8142c094-f3c9-478b-b117-6585bebb6789}')
    @winrt_commethod(6)
    def CreateAccountWithPackageRelativeAppIdAndEnterpriseIdAsync(self, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String, enterpriseId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
class IUserDataAccountStoreChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStoreChangedEventArgs'
    _iid_ = Guid('{84e3e2e5-8820-4512-b1f6-2e035be1072c}')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class UserDataAccount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccount'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserDisplayName(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserDisplayName(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount, value: Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_DeviceAccountTypeId(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FindAppointmentCalendarsAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Appointments.AppointmentCalendar]]: ...
    @winrt_mixinmethod
    def FindEmailMailboxesAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Email.EmailMailbox]]: ...
    @winrt_mixinmethod
    def FindContactListsAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.ContactList]]: ...
    @winrt_mixinmethod
    def FindContactAnnotationListsAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.ContactAnnotationList]]: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsProtectedUnderLock(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExplictReadAccessPackageFamilyNames(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CanShowCreateContactGroup(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanShowCreateContactGroup(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderProperties(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def FindUserDataTaskListsAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_mixinmethod
    def FindContactGroupsAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.ContactGroup]]: ...
    @winrt_mixinmethod
    def TryShowCreateContactGroupAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def put_IsProtectedUnderLock(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_Icon(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    Id = property(get_Id, None)
    UserDisplayName = property(get_UserDisplayName, put_UserDisplayName)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    Icon = property(get_Icon, put_Icon)
    DeviceAccountTypeId = property(get_DeviceAccountTypeId, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    IsProtectedUnderLock = property(get_IsProtectedUnderLock, put_IsProtectedUnderLock)
    ExplictReadAccessPackageFamilyNames = property(get_ExplictReadAccessPackageFamilyNames, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    CanShowCreateContactGroup = property(get_CanShowCreateContactGroup, put_CanShowCreateContactGroup)
    ProviderProperties = property(get_ProviderProperties, None)
UserDataAccountContentKinds = UInt32
UserDataAccountContentKinds_Email: UserDataAccountContentKinds = 1
UserDataAccountContentKinds_Contact: UserDataAccountContentKinds = 2
UserDataAccountContentKinds_Appointment: UserDataAccountContentKinds = 4
class UserDataAccountManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountManager'
    @winrt_classmethod
    def GetForUser(cls: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics2, user: Windows.System.User) -> Windows.ApplicationModel.UserDataAccounts.UserDataAccountManagerForUser: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, storeAccessType: Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_classmethod
    def ShowAddAccountAsync(cls: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, contentKinds: Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ShowAccountSettingsAsync(cls: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, id: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowAccountErrorResolverAsync(cls: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, id: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class UserDataAccountManagerForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountManagerForUser'
    @winrt_mixinmethod
    def RequestStoreAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser, storeAccessType: Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser) -> Windows.System.User: ...
    User = property(get_User, None)
UserDataAccountOtherAppReadAccess = Int32
UserDataAccountOtherAppReadAccess_SystemOnly: UserDataAccountOtherAppReadAccess = 0
UserDataAccountOtherAppReadAccess_Full: UserDataAccountOtherAppReadAccess = 1
UserDataAccountOtherAppReadAccess_None: UserDataAccountOtherAppReadAccess = 2
class UserDataAccountStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore'
    @winrt_mixinmethod
    def FindAccountsAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]]: ...
    @winrt_mixinmethod
    def GetAccountAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_mixinmethod
    def CreateAccountAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore, userDisplayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_mixinmethod
    def CreateAccountWithPackageRelativeAppIdAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_mixinmethod
    def add_StoreChanged(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore, Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StoreChanged(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateAccountWithPackageRelativeAppIdAndEnterpriseIdAsync(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore3, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String, enterpriseId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
UserDataAccountStoreAccessType = Int32
UserDataAccountStoreAccessType_AllAccountsReadOnly: UserDataAccountStoreAccessType = 0
UserDataAccountStoreAccessType_AppAccountsReadWrite: UserDataAccountStoreAccessType = 1
class UserDataAccountStoreChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStoreChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStoreChangedEventArgs) -> Windows.Foundation.Deferral: ...
make_head(_module, 'IUserDataAccount')
make_head(_module, 'IUserDataAccount2')
make_head(_module, 'IUserDataAccount3')
make_head(_module, 'IUserDataAccount4')
make_head(_module, 'IUserDataAccountManagerForUser')
make_head(_module, 'IUserDataAccountManagerStatics')
make_head(_module, 'IUserDataAccountManagerStatics2')
make_head(_module, 'IUserDataAccountStore')
make_head(_module, 'IUserDataAccountStore2')
make_head(_module, 'IUserDataAccountStore3')
make_head(_module, 'IUserDataAccountStoreChangedEventArgs')
make_head(_module, 'UserDataAccount')
make_head(_module, 'UserDataAccountManager')
make_head(_module, 'UserDataAccountManagerForUser')
make_head(_module, 'UserDataAccountStore')
make_head(_module, 'UserDataAccountStoreChangedEventArgs')
