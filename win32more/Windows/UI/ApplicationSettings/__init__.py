from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Credentials
import win32more.Windows.System
import win32more.Windows.UI.ApplicationSettings
import win32more.Windows.UI.Popups
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AccountsSettingsPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPane
    _classid_ = 'Windows.UI.ApplicationSettings.AccountsSettingsPane'
    @winrt_mixinmethod
    def add_AccountCommandsRequested(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ApplicationSettings.AccountsSettingsPane, win32more.Windows.UI.ApplicationSettings.AccountsSettingsPaneCommandsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountCommandsRequested(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPane, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ShowManageAccountsForUserAsync(cls: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics3, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowAddAccountForUserAsync(cls: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics3, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowManageAccountsAsync(cls: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowAddAccountAsync(cls: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics) -> win32more.Windows.UI.ApplicationSettings.AccountsSettingsPane: ...
    @winrt_classmethod
    def Show(cls: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics) -> Void: ...
    AccountCommandsRequested = event()
class AccountsSettingsPaneCommandsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs
    _classid_ = 'Windows.UI.ApplicationSettings.AccountsSettingsPaneCommandsRequestedEventArgs'
    @winrt_mixinmethod
    def get_WebAccountProviderCommands(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommand]: ...
    @winrt_mixinmethod
    def get_WebAccountCommands(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.WebAccountCommand]: ...
    @winrt_mixinmethod
    def get_CredentialCommands(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.CredentialCommand]: ...
    @winrt_mixinmethod
    def get_Commands(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.SettingsCommand]: ...
    @winrt_mixinmethod
    def get_HeaderText(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HeaderText(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> win32more.Windows.UI.ApplicationSettings.AccountsSettingsPaneEventDeferral: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs2) -> win32more.Windows.System.User: ...
    Commands = property(get_Commands, None)
    CredentialCommands = property(get_CredentialCommands, None)
    HeaderText = property(get_HeaderText, put_HeaderText)
    User = property(get_User, None)
    WebAccountCommands = property(get_WebAccountCommands, None)
    WebAccountProviderCommands = property(get_WebAccountProviderCommands, None)
class AccountsSettingsPaneEventDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneEventDeferral
    _classid_ = 'Windows.UI.ApplicationSettings.AccountsSettingsPaneEventDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.ApplicationSettings.IAccountsSettingsPaneEventDeferral) -> Void: ...
ApplicationsSettingsContract: UInt32 = 65536
class CredentialCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.ICredentialCommand
    _classid_ = 'Windows.UI.ApplicationSettings.CredentialCommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.ApplicationSettings.CredentialCommand.CreateCredentialCommand(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.ApplicationSettings.CredentialCommand.CreateCredentialCommandWithHandler(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateCredentialCommand(cls: win32more.Windows.UI.ApplicationSettings.ICredentialCommandFactory, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.UI.ApplicationSettings.CredentialCommand: ...
    @winrt_factorymethod
    def CreateCredentialCommandWithHandler(cls: win32more.Windows.UI.ApplicationSettings.ICredentialCommandFactory, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential, deleted: win32more.Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler) -> win32more.Windows.UI.ApplicationSettings.CredentialCommand: ...
    @winrt_mixinmethod
    def get_PasswordCredential(self: win32more.Windows.UI.ApplicationSettings.ICredentialCommand) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_CredentialDeleted(self: win32more.Windows.UI.ApplicationSettings.ICredentialCommand) -> win32more.Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler: ...
    CredentialDeleted = property(get_CredentialDeleted, None)
    PasswordCredential = property(get_PasswordCredential, None)
class CredentialCommandCredentialDeletedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61c0e185-0977-4678-b4e2-98727afbeed9}')
    @winrt_commethod(3)
    def Invoke(self, command: win32more.Windows.UI.ApplicationSettings.CredentialCommand) -> Void: ...
class IAccountsSettingsPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPane'
    _iid_ = Guid('{81ea942c-4f09-4406-a538-838d9b14b7e6}')
    @winrt_commethod(6)
    def add_AccountCommandsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ApplicationSettings.AccountsSettingsPane, win32more.Windows.UI.ApplicationSettings.AccountsSettingsPaneCommandsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccountCommandsRequested(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AccountCommandsRequested = event()
class IAccountsSettingsPaneCommandsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs'
    _iid_ = Guid('{3b68c099-db19-45d0-9abf-95d3773c9330}')
    @winrt_commethod(6)
    def get_WebAccountProviderCommands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommand]: ...
    @winrt_commethod(7)
    def get_WebAccountCommands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.WebAccountCommand]: ...
    @winrt_commethod(8)
    def get_CredentialCommands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.CredentialCommand]: ...
    @winrt_commethod(9)
    def get_Commands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.SettingsCommand]: ...
    @winrt_commethod(10)
    def get_HeaderText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_HeaderText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def GetDeferral(self) -> win32more.Windows.UI.ApplicationSettings.AccountsSettingsPaneEventDeferral: ...
    Commands = property(get_Commands, None)
    CredentialCommands = property(get_CredentialCommands, None)
    HeaderText = property(get_HeaderText, put_HeaderText)
    WebAccountCommands = property(get_WebAccountCommands, None)
    WebAccountProviderCommands = property(get_WebAccountProviderCommands, None)
class IAccountsSettingsPaneCommandsRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs2'
    _iid_ = Guid('{362f7bad-4e37-4967-8c40-e78ee7a1e5bb}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IAccountsSettingsPaneEventDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPaneEventDeferral'
    _iid_ = Guid('{cbf25d3f-e5ba-40ef-93da-65e096e5fb04}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IAccountsSettingsPaneStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics'
    _iid_ = Guid('{561f8b60-b0ec-4150-a8dc-208ee44b068a}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ApplicationSettings.AccountsSettingsPane: ...
    @winrt_commethod(7)
    def Show(self) -> Void: ...
class IAccountsSettingsPaneStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics2'
    _iid_ = Guid('{d21df7c2-ce0d-484f-b8e8-e823c215765e}')
    @winrt_commethod(6)
    def ShowManageAccountsAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ShowAddAccountAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IAccountsSettingsPaneStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics3'
    _iid_ = Guid('{08410458-a2ba-4c6f-b4ac-48f514331216}')
    @winrt_commethod(6)
    def ShowManageAccountsForUserAsync(self, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ShowAddAccountForUserAsync(self, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICredentialCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ICredentialCommand'
    _iid_ = Guid('{a5f665e6-6143-4a7a-a971-b017ba978ce2}')
    @winrt_commethod(6)
    def get_PasswordCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def get_CredentialDeleted(self) -> win32more.Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler: ...
    CredentialDeleted = property(get_CredentialDeleted, None)
    PasswordCredential = property(get_PasswordCredential, None)
class ICredentialCommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ICredentialCommandFactory'
    _iid_ = Guid('{27e88c17-bc3e-4b80-9495-4ed720e48a91}')
    @winrt_commethod(6)
    def CreateCredentialCommand(self, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.UI.ApplicationSettings.CredentialCommand: ...
    @winrt_commethod(7)
    def CreateCredentialCommandWithHandler(self, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential, deleted: win32more.Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler) -> win32more.Windows.UI.ApplicationSettings.CredentialCommand: ...
class ISettingsCommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ISettingsCommandFactory'
    _iid_ = Guid('{68e15b33-1c83-433a-aa5a-ceeea5bd4764}')
    @winrt_commethod(6)
    def CreateSettingsCommand(self, settingsCommandId: win32more.Windows.Win32.System.WinRT.IInspectable, label: WinRT_String, handler: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> win32more.Windows.UI.ApplicationSettings.SettingsCommand: ...
class ISettingsCommandStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ISettingsCommandStatics'
    _iid_ = Guid('{749ae954-2f69-4b17-8aba-d05ce5778e46}')
    @winrt_commethod(6)
    def get_AccountsCommand(self) -> win32more.Windows.UI.ApplicationSettings.SettingsCommand: ...
    AccountsCommand = property(get_AccountsCommand, None)
class ISettingsPane(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ISettingsPane'
    _iid_ = Guid('{b1cd0932-4570-4c69-8d38-89446561ace0}')
    @winrt_commethod(6)
    def add_CommandsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ApplicationSettings.SettingsPane, win32more.Windows.UI.ApplicationSettings.SettingsPaneCommandsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CommandsRequested(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CommandsRequested = event()
class ISettingsPaneCommandsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ISettingsPaneCommandsRequest'
    _iid_ = Guid('{44df23ae-5d6e-4068-a168-f47643182114}')
    @winrt_commethod(6)
    def get_ApplicationCommands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.SettingsCommand]: ...
    ApplicationCommands = property(get_ApplicationCommands, None)
class ISettingsPaneCommandsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ISettingsPaneCommandsRequestedEventArgs'
    _iid_ = Guid('{205f5d24-1b48-4629-a6ca-2fdfedafb75d}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.UI.ApplicationSettings.SettingsPaneCommandsRequest: ...
    Request = property(get_Request, None)
class ISettingsPaneStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.ISettingsPaneStatics'
    _iid_ = Guid('{1c6a52c5-ff19-471b-ba6b-f8f35694ad9a}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ApplicationSettings.SettingsPane: ...
    @winrt_commethod(7)
    def Show(self) -> Void: ...
    @winrt_commethod(8)
    def get_Edge(self) -> win32more.Windows.UI.ApplicationSettings.SettingsEdgeLocation: ...
    Edge = property(get_Edge, None)
class IWebAccountCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IWebAccountCommand'
    _iid_ = Guid('{caa39398-9cfa-4246-b0c4-a913a3896541}')
    @winrt_commethod(6)
    def get_WebAccount(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(7)
    def get_Invoked(self) -> win32more.Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler: ...
    @winrt_commethod(8)
    def get_Actions(self) -> win32more.Windows.UI.ApplicationSettings.SupportedWebAccountActions: ...
    Actions = property(get_Actions, None)
    Invoked = property(get_Invoked, None)
    WebAccount = property(get_WebAccount, None)
class IWebAccountCommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IWebAccountCommandFactory'
    _iid_ = Guid('{bfa6cdff-2f2d-42f5-81de-1d56bafc496d}')
    @winrt_commethod(6)
    def CreateWebAccountCommand(self, webAccount: win32more.Windows.Security.Credentials.WebAccount, invoked: win32more.Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler, actions: win32more.Windows.UI.ApplicationSettings.SupportedWebAccountActions) -> win32more.Windows.UI.ApplicationSettings.WebAccountCommand: ...
class IWebAccountInvokedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IWebAccountInvokedArgs'
    _iid_ = Guid('{e7abcc40-a1d8-4c5d-9a7f-1d34b2f90ad2}')
    @winrt_commethod(6)
    def get_Action(self) -> win32more.Windows.UI.ApplicationSettings.WebAccountAction: ...
    Action = property(get_Action, None)
class IWebAccountProviderCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IWebAccountProviderCommand'
    _iid_ = Guid('{d69bdd9a-a0a6-4e9b-88dc-c71e757a3501}')
    @winrt_commethod(6)
    def get_WebAccountProvider(self) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_Invoked(self) -> win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler: ...
    Invoked = property(get_Invoked, None)
    WebAccountProvider = property(get_WebAccountProvider, None)
class IWebAccountProviderCommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ApplicationSettings.IWebAccountProviderCommandFactory'
    _iid_ = Guid('{d5658a1b-b176-4776-8469-a9d3ff0b3f59}')
    @winrt_commethod(6)
    def CreateWebAccountProviderCommand(self, webAccountProvider: win32more.Windows.Security.Credentials.WebAccountProvider, invoked: win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler) -> win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommand: ...
class _SettingsCommand_Meta_(ComPtr.__class__):
    pass
class SettingsCommand(ComPtr, metaclass=_SettingsCommand_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IUICommand
    _classid_ = 'Windows.UI.ApplicationSettings.SettingsCommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.ApplicationSettings.SettingsCommand.CreateSettingsCommand(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateSettingsCommand(cls: win32more.Windows.UI.ApplicationSettings.ISettingsCommandFactory, settingsCommandId: win32more.Windows.Win32.System.WinRT.IInspectable, label: WinRT_String, handler: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> win32more.Windows.UI.ApplicationSettings.SettingsCommand: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.Popups.IUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.Popups.IUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_Invoked(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_classmethod
    def get_AccountsCommand(cls: win32more.Windows.UI.ApplicationSettings.ISettingsCommandStatics) -> win32more.Windows.UI.ApplicationSettings.SettingsCommand: ...
    Id = property(get_Id, put_Id)
    Invoked = property(get_Invoked, put_Invoked)
    Label = property(get_Label, put_Label)
    _SettingsCommand_Meta_.AccountsCommand = property(get_AccountsCommand, None)
class SettingsEdgeLocation(Enum, Int32):
    Right = 0
    Left = 1
class _SettingsPane_Meta_(ComPtr.__class__):
    pass
class SettingsPane(ComPtr, metaclass=_SettingsPane_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.ISettingsPane
    _classid_ = 'Windows.UI.ApplicationSettings.SettingsPane'
    @winrt_mixinmethod
    def add_CommandsRequested(self: win32more.Windows.UI.ApplicationSettings.ISettingsPane, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ApplicationSettings.SettingsPane, win32more.Windows.UI.ApplicationSettings.SettingsPaneCommandsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandsRequested(self: win32more.Windows.UI.ApplicationSettings.ISettingsPane, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ApplicationSettings.ISettingsPaneStatics) -> win32more.Windows.UI.ApplicationSettings.SettingsPane: ...
    @winrt_classmethod
    def Show(cls: win32more.Windows.UI.ApplicationSettings.ISettingsPaneStatics) -> Void: ...
    @winrt_classmethod
    def get_Edge(cls: win32more.Windows.UI.ApplicationSettings.ISettingsPaneStatics) -> win32more.Windows.UI.ApplicationSettings.SettingsEdgeLocation: ...
    _SettingsPane_Meta_.Edge = property(get_Edge, None)
    CommandsRequested = event()
class SettingsPaneCommandsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.ISettingsPaneCommandsRequest
    _classid_ = 'Windows.UI.ApplicationSettings.SettingsPaneCommandsRequest'
    @winrt_mixinmethod
    def get_ApplicationCommands(self: win32more.Windows.UI.ApplicationSettings.ISettingsPaneCommandsRequest) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.ApplicationSettings.SettingsCommand]: ...
    ApplicationCommands = property(get_ApplicationCommands, None)
class SettingsPaneCommandsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.ISettingsPaneCommandsRequestedEventArgs
    _classid_ = 'Windows.UI.ApplicationSettings.SettingsPaneCommandsRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.ApplicationSettings.ISettingsPaneCommandsRequestedEventArgs) -> win32more.Windows.UI.ApplicationSettings.SettingsPaneCommandsRequest: ...
    Request = property(get_Request, None)
class SupportedWebAccountActions(Enum, UInt32):
    None_ = 0
    Reconnect = 1
    Remove = 2
    ViewDetails = 4
    Manage = 8
    More = 16
class WebAccountAction(Enum, Int32):
    Reconnect = 0
    Remove = 1
    ViewDetails = 2
    Manage = 3
    More = 4
class WebAccountCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.IWebAccountCommand
    _classid_ = 'Windows.UI.ApplicationSettings.WebAccountCommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.ApplicationSettings.WebAccountCommand.CreateWebAccountCommand(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWebAccountCommand(cls: win32more.Windows.UI.ApplicationSettings.IWebAccountCommandFactory, webAccount: win32more.Windows.Security.Credentials.WebAccount, invoked: win32more.Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler, actions: win32more.Windows.UI.ApplicationSettings.SupportedWebAccountActions) -> win32more.Windows.UI.ApplicationSettings.WebAccountCommand: ...
    @winrt_mixinmethod
    def get_WebAccount(self: win32more.Windows.UI.ApplicationSettings.IWebAccountCommand) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.ApplicationSettings.IWebAccountCommand) -> win32more.Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler: ...
    @winrt_mixinmethod
    def get_Actions(self: win32more.Windows.UI.ApplicationSettings.IWebAccountCommand) -> win32more.Windows.UI.ApplicationSettings.SupportedWebAccountActions: ...
    Actions = property(get_Actions, None)
    Invoked = property(get_Invoked, None)
    WebAccount = property(get_WebAccount, None)
class WebAccountCommandInvokedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1ee6e459-1705-4a9a-b599-a0c3d6921973}')
    @winrt_commethod(3)
    def Invoke(self, command: win32more.Windows.UI.ApplicationSettings.WebAccountCommand, args: win32more.Windows.UI.ApplicationSettings.WebAccountInvokedArgs) -> Void: ...
class WebAccountInvokedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.IWebAccountInvokedArgs
    _classid_ = 'Windows.UI.ApplicationSettings.WebAccountInvokedArgs'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.UI.ApplicationSettings.IWebAccountInvokedArgs) -> win32more.Windows.UI.ApplicationSettings.WebAccountAction: ...
    Action = property(get_Action, None)
class WebAccountProviderCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ApplicationSettings.IWebAccountProviderCommand
    _classid_ = 'Windows.UI.ApplicationSettings.WebAccountProviderCommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommand.CreateWebAccountProviderCommand(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWebAccountProviderCommand(cls: win32more.Windows.UI.ApplicationSettings.IWebAccountProviderCommandFactory, webAccountProvider: win32more.Windows.Security.Credentials.WebAccountProvider, invoked: win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler) -> win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommand: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: win32more.Windows.UI.ApplicationSettings.IWebAccountProviderCommand) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.ApplicationSettings.IWebAccountProviderCommand) -> win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler: ...
    Invoked = property(get_Invoked, None)
    WebAccountProvider = property(get_WebAccountProvider, None)
class WebAccountProviderCommandInvokedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7de5527-4c8f-42dd-84da-5ec493abdb9a}')
    @winrt_commethod(3)
    def Invoke(self, command: win32more.Windows.UI.ApplicationSettings.WebAccountProviderCommand) -> Void: ...


make_ready(__name__)
