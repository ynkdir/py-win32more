from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.Email
import win32more.Windows.ApplicationModel.UserDataAccounts
import win32more.Windows.ApplicationModel.UserDataTasks
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class IUserDataAccount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount'
    _iid_ = Guid('{b9c4367e-b348-4910-be94-4ad4bba6dea7}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_UserDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_OtherAppReadAccess(self) -> win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess: ...
    @winrt_commethod(10)
    def put_OtherAppReadAccess(self, value: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess) -> Void: ...
    @winrt_commethod(11)
    def get_Icon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(12)
    def get_DeviceAccountTypeId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def FindAppointmentCalendarsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Appointments.AppointmentCalendar]]: ...
    @winrt_commethod(17)
    def FindEmailMailboxesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMailbox]]: ...
    @winrt_commethod(18)
    def FindContactListsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactList]]: ...
    @winrt_commethod(19)
    def FindContactAnnotationListsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]]: ...
    DeviceAccountTypeId = property(get_DeviceAccountTypeId, None)
    Icon = property(get_Icon, None)
    Id = property(get_Id, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    PackageFamilyName = property(get_PackageFamilyName, None)
    UserDisplayName = property(get_UserDisplayName, put_UserDisplayName)
class IUserDataAccount2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount2'
    _iid_ = Guid('{078cd89f-de82-404b-8195-c8a3ac198f60}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsProtectedUnderLock(self) -> Boolean: ...
    EnterpriseId = property(get_EnterpriseId, None)
    IsProtectedUnderLock = property(get_IsProtectedUnderLock, None)
class IUserDataAccount3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3'
    _iid_ = Guid('{01533845-6c43-4286-9d69-3e1709a1f266}')
    @winrt_commethod(6)
    def get_ExplictReadAccessPackageFamilyNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    ExplictReadAccessPackageFamilyNames = property(get_ExplictReadAccessPackageFamilyNames, None)
class IUserDataAccount4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4'
    _iid_ = Guid('{c4315210-eae5-4f0a-a8b2-1cca115e008f}')
    @winrt_commethod(6)
    def get_CanShowCreateContactGroup(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CanShowCreateContactGroup(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ProviderProperties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def FindUserDataTaskListsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_commethod(10)
    def FindContactGroupsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactGroup]]: ...
    @winrt_commethod(11)
    def TryShowCreateContactGroupAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(12)
    def put_IsProtectedUnderLock(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def put_Icon(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    CanShowCreateContactGroup = property(get_CanShowCreateContactGroup, put_CanShowCreateContactGroup)
    Icon = property(None, put_Icon)
    IsProtectedUnderLock = property(None, put_IsProtectedUnderLock)
    ProviderProperties = property(get_ProviderProperties, None)
class IUserDataAccountManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser'
    _iid_ = Guid('{56a6e8db-db8f-41ab-a65f-8c5971aac982}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, storeAccessType: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IUserDataAccountManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics'
    _iid_ = Guid('{0d9b89ea-1928-4a20-86d5-3c737f7dc3b0}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, storeAccessType: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_commethod(7)
    def ShowAddAccountAsync(self, contentKinds: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def ShowAccountSettingsAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ShowAccountErrorResolverAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IUserDataAccountManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics2'
    _iid_ = Guid('{6a3ded88-316b-435e-b534-f7d4b4b7dba6}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountManagerForUser: ...
class IUserDataAccountStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore'
    _iid_ = Guid('{2073b0ad-7d0a-4e76-bf45-2368f978a59a}')
    @winrt_commethod(6)
    def FindAccountsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]]: ...
    @winrt_commethod(7)
    def GetAccountAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_commethod(8)
    def CreateAccountAsync(self, userDisplayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
class IUserDataAccountStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2'
    _iid_ = Guid('{b1e0aef7-9560-4631-8af0-061d30161469}')
    @winrt_commethod(6)
    def CreateAccountWithPackageRelativeAppIdAsync(self, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_commethod(7)
    def add_StoreChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore, win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StoreChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    StoreChanged = event()
class IUserDataAccountStore3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore3'
    _iid_ = Guid('{8142c094-f3c9-478b-b117-6585bebb6789}')
    @winrt_commethod(6)
    def CreateAccountWithPackageRelativeAppIdAndEnterpriseIdAsync(self, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String, enterpriseId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
class IUserDataAccountStoreChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStoreChangedEventArgs'
    _iid_ = Guid('{84e3e2e5-8820-4512-b1f6-2e035be1072c}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class UserDataAccount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccount'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserDisplayName(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserDisplayName(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount, value: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_DeviceAccountTypeId(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FindAppointmentCalendarsAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Appointments.AppointmentCalendar]]: ...
    @winrt_mixinmethod
    def FindEmailMailboxesAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Email.EmailMailbox]]: ...
    @winrt_mixinmethod
    def FindContactListsAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactList]]: ...
    @winrt_mixinmethod
    def FindContactAnnotationListsAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactAnnotationList]]: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsProtectedUnderLock(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExplictReadAccessPackageFamilyNames(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CanShowCreateContactGroup(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> Boolean: ...
    @winrt_mixinmethod
    def put_CanShowCreateContactGroup(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderProperties(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def FindUserDataTaskListsAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_mixinmethod
    def FindContactGroupsAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.ContactGroup]]: ...
    @winrt_mixinmethod
    def TryShowCreateContactGroupAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def put_IsProtectedUnderLock(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccount4, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    CanShowCreateContactGroup = property(get_CanShowCreateContactGroup, put_CanShowCreateContactGroup)
    DeviceAccountTypeId = property(get_DeviceAccountTypeId, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    EnterpriseId = property(get_EnterpriseId, None)
    ExplictReadAccessPackageFamilyNames = property(get_ExplictReadAccessPackageFamilyNames, None)
    Icon = property(get_Icon, put_Icon)
    Id = property(get_Id, None)
    IsProtectedUnderLock = property(get_IsProtectedUnderLock, put_IsProtectedUnderLock)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    PackageFamilyName = property(get_PackageFamilyName, None)
    ProviderProperties = property(get_ProviderProperties, None)
    UserDisplayName = property(get_UserDisplayName, put_UserDisplayName)
class UserDataAccountContentKinds(Enum, UInt32):
    Email = 1
    Contact = 2
    Appointment = 4
class UserDataAccountManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountManager'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountManagerForUser: ...
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, storeAccessType: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_classmethod
    def ShowAddAccountAsync(cls: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, contentKinds: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ShowAccountSettingsAsync(cls: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowAccountErrorResolverAsync(cls: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class UserDataAccountManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountManagerForUser'
    @winrt_mixinmethod
    def RequestStoreAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser, storeAccessType: win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountManagerForUser) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class UserDataAccountOtherAppReadAccess(Enum, Int32):
    SystemOnly = 0
    Full = 1
    None_ = 2
class UserDataAccountStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore'
    @winrt_mixinmethod
    def FindAccountsAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]]: ...
    @winrt_mixinmethod
    def GetAccountAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_mixinmethod
    def CreateAccountAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore, userDisplayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_mixinmethod
    def CreateAccountWithPackageRelativeAppIdAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    @winrt_mixinmethod
    def add_StoreChanged(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStore, win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StoreChanged(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateAccountWithPackageRelativeAppIdAndEnterpriseIdAsync(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStore3, userDisplayName: WinRT_String, packageRelativeAppId: WinRT_String, enterpriseId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccount]: ...
    StoreChanged = event()
class UserDataAccountStoreAccessType(Enum, Int32):
    AllAccountsReadOnly = 0
    AppAccountsReadWrite = 1
class UserDataAccountStoreChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStoreChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserDataAccounts.IUserDataAccountStoreChangedEventArgs) -> win32more.Windows.Foundation.Deferral: ...


make_ready(__name__)
