from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.UserDataAccounts
import win32more.Windows.ApplicationModel.UserDataAccounts.Provider
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IUserDataAccountPartnerAccountInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountPartnerAccountInfo'
    _iid_ = Guid('{5f200037-f6ef-4ec3-8630-012c59c1149f}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Priority(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_AccountKind(self) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderPartnerAccountKind: ...
    AccountKind = property(get_AccountKind, None)
    DisplayName = property(get_DisplayName, None)
    Priority = property(get_Priority, None)
class IUserDataAccountProviderAddAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderAddAccountOperation'
    _iid_ = Guid('{b9c72530-3f84-4b5d-8eaa-45e97aa842ed}')
    @winrt_commethod(6)
    def get_ContentKinds(self) -> win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds: ...
    @winrt_commethod(7)
    def get_PartnerAccountInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountPartnerAccountInfo]: ...
    @winrt_commethod(8)
    def ReportCompleted(self, userDataAccountId: WinRT_String) -> Void: ...
    ContentKinds = property(get_ContentKinds, None)
    PartnerAccountInfos = property(get_PartnerAccountInfos, None)
class IUserDataAccountProviderOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation'
    _iid_ = Guid('{a20aad63-888c-4a62-a3dd-34d07a802b2b}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderOperationKind: ...
    Kind = property(get_Kind, None)
class IUserDataAccountProviderResolveErrorsOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderResolveErrorsOperation'
    _iid_ = Guid('{6235dc15-bfcb-41e1-9957-9759a28846cc}')
    @winrt_commethod(6)
    def get_UserDataAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompleted(self) -> Void: ...
    UserDataAccountId = property(get_UserDataAccountId, None)
class IUserDataAccountProviderSettingsOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderSettingsOperation'
    _iid_ = Guid('{92034db7-8648-4f30-acfa-3002658ca80d}')
    @winrt_commethod(6)
    def get_UserDataAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompleted(self) -> Void: ...
    UserDataAccountId = property(get_UserDataAccountId, None)
class UserDataAccountPartnerAccountInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountPartnerAccountInfo
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountPartnerAccountInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountPartnerAccountInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountPartnerAccountInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_AccountKind(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountPartnerAccountInfo) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderPartnerAccountKind: ...
    AccountKind = property(get_AccountKind, None)
    DisplayName = property(get_DisplayName, None)
    Priority = property(get_Priority, None)
class UserDataAccountProviderAddAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderAddAccountOperation
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderAddAccountOperation'
    @winrt_mixinmethod
    def get_ContentKinds(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderAddAccountOperation) -> win32more.Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds: ...
    @winrt_mixinmethod
    def get_PartnerAccountInfos(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderAddAccountOperation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountPartnerAccountInfo]: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderAddAccountOperation, userDataAccountId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderOperationKind: ...
    ContentKinds = property(get_ContentKinds, None)
    Kind = property(get_Kind, None)
    PartnerAccountInfos = property(get_PartnerAccountInfos, None)
class UserDataAccountProviderOperationKind(Enum, Int32):
    AddAccount = 0
    Settings = 1
    ResolveErrors = 2
class UserDataAccountProviderPartnerAccountKind(Enum, Int32):
    Exchange = 0
    PopOrImap = 1
class UserDataAccountProviderResolveErrorsOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderResolveErrorsOperation
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderResolveErrorsOperation'
    @winrt_mixinmethod
    def get_UserDataAccountId(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderResolveErrorsOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderResolveErrorsOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderOperationKind: ...
    Kind = property(get_Kind, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
class UserDataAccountProviderSettingsOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderSettingsOperation
    _classid_ = 'Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderSettingsOperation'
    @winrt_mixinmethod
    def get_UserDataAccountId(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderSettingsOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderSettingsOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderOperationKind: ...
    Kind = property(get_Kind, None)
    UserDataAccountId = property(get_UserDataAccountId, None)


make_ready(__name__)
