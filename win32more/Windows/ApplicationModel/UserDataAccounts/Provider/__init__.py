from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.UserDataAccounts
import win32more.Windows.ApplicationModel.UserDataAccounts.Provider
import win32more.Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    DisplayName = property(get_DisplayName, None)
    Priority = property(get_Priority, None)
    AccountKind = property(get_AccountKind, None)
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
    DisplayName = property(get_DisplayName, None)
    Priority = property(get_Priority, None)
    AccountKind = property(get_AccountKind, None)
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
    PartnerAccountInfos = property(get_PartnerAccountInfos, None)
    Kind = property(get_Kind, None)
UserDataAccountProviderOperationKind = Int32
UserDataAccountProviderOperationKind_AddAccount: UserDataAccountProviderOperationKind = 0
UserDataAccountProviderOperationKind_Settings: UserDataAccountProviderOperationKind = 1
UserDataAccountProviderOperationKind_ResolveErrors: UserDataAccountProviderOperationKind = 2
UserDataAccountProviderPartnerAccountKind = Int32
UserDataAccountProviderPartnerAccountKind_Exchange: UserDataAccountProviderPartnerAccountKind = 0
UserDataAccountProviderPartnerAccountKind_PopOrImap: UserDataAccountProviderPartnerAccountKind = 1
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
    UserDataAccountId = property(get_UserDataAccountId, None)
    Kind = property(get_Kind, None)
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
    UserDataAccountId = property(get_UserDataAccountId, None)
    Kind = property(get_Kind, None)
make_head(_module, 'IUserDataAccountPartnerAccountInfo')
make_head(_module, 'IUserDataAccountProviderAddAccountOperation')
make_head(_module, 'IUserDataAccountProviderOperation')
make_head(_module, 'IUserDataAccountProviderResolveErrorsOperation')
make_head(_module, 'IUserDataAccountProviderSettingsOperation')
make_head(_module, 'UserDataAccountPartnerAccountInfo')
make_head(_module, 'UserDataAccountProviderAddAccountOperation')
make_head(_module, 'UserDataAccountProviderResolveErrorsOperation')
make_head(_module, 'UserDataAccountProviderSettingsOperation')
