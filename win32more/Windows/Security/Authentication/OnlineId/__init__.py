from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.OnlineId
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class CredentialPromptType(Enum, Int32):
    PromptIfNeeded = 0
    RetypeCredentials = 1
    DoNotPrompt = 2
class IOnlineIdAuthenticator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator'
    _iid_ = Guid('{a003f58a-29ab-4817-b884-d7516dad18b9}')
    @winrt_commethod(6)
    def AuthenticateUserAsync(self, request: win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> win32more.Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_commethod(7)
    def AuthenticateUserAsyncAdvanced(self, requests: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest], credentialPromptType: win32more.Windows.Security.Authentication.OnlineId.CredentialPromptType) -> win32more.Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_commethod(8)
    def SignOutUserAsync(self) -> win32more.Windows.Security.Authentication.OnlineId.SignOutUserOperation: ...
    @winrt_commethod(9)
    def put_ApplicationId(self, value: Guid) -> Void: ...
    @winrt_commethod(10)
    def get_ApplicationId(self) -> Guid: ...
    @winrt_commethod(11)
    def get_CanSignOut(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_AuthenticatedSafeCustomerId(self) -> WinRT_String: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    AuthenticatedSafeCustomerId = property(get_AuthenticatedSafeCustomerId, None)
    CanSignOut = property(get_CanSignOut, None)
class IOnlineIdServiceTicket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket'
    _iid_ = Guid('{c95c547f-d781-4a94-acb8-c59874238c26}')
    @winrt_commethod(6)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Request(self) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> Int32: ...
    ErrorCode = property(get_ErrorCode, None)
    Request = property(get_Request, None)
    Value = property(get_Value, None)
class IOnlineIdServiceTicketRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequest'
    _iid_ = Guid('{297445d3-fb63-4135-8909-4e354c061466}')
    @winrt_commethod(6)
    def get_Service(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Policy(self) -> WinRT_String: ...
    Policy = property(get_Policy, None)
    Service = property(get_Service, None)
class IOnlineIdServiceTicketRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequestFactory'
    _iid_ = Guid('{bebb0a08-9e73-4077-9614-08614c0bc245}')
    @winrt_commethod(6)
    def CreateOnlineIdServiceTicketRequest(self, service: WinRT_String, policy: WinRT_String) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_commethod(7)
    def CreateOnlineIdServiceTicketRequestAdvanced(self, service: WinRT_String) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
class IOnlineIdSystemAuthenticatorForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser'
    _iid_ = Guid('{5798befb-1de4-4186-a2e6-b563f86aaf44}')
    @winrt_commethod(6)
    def GetTicketAsync(self, request: win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketResult]: ...
    @winrt_commethod(7)
    def put_ApplicationId(self, value: Guid) -> Void: ...
    @winrt_commethod(8)
    def get_ApplicationId(self) -> Guid: ...
    @winrt_commethod(9)
    def get_User(self) -> win32more.Windows.System.User: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    User = property(get_User, None)
class IOnlineIdSystemAuthenticatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorStatics'
    _iid_ = Guid('{85047792-f634-41e3-96a4-5164e902c740}')
    @winrt_commethod(6)
    def get_Default(self) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    Default = property(get_Default, None)
class IOnlineIdSystemIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdSystemIdentity'
    _iid_ = Guid('{743cd20d-b6ca-434d-8124-53ea12685307}')
    @winrt_commethod(6)
    def get_Ticket(self) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    Ticket = property(get_Ticket, None)
class IOnlineIdSystemTicketResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult'
    _iid_ = Guid('{db0a5ff8-b098-4acd-9d13-9e640652b5b6}')
    @winrt_commethod(6)
    def get_Identity(self) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemIdentity: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Identity = property(get_Identity, None)
    Status = property(get_Status, None)
class IUserIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.IUserIdentity'
    _iid_ = Guid('{2146d9cd-0742-4be3-8a1c-7c7ae679aa88}')
    @winrt_commethod(6)
    def get_Tickets(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket]: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SafeCustomerId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SignInName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_FirstName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_LastName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_IsBetaAccount(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsConfirmedPC(self) -> Boolean: ...
    FirstName = property(get_FirstName, None)
    Id = property(get_Id, None)
    IsBetaAccount = property(get_IsBetaAccount, None)
    IsConfirmedPC = property(get_IsConfirmedPC, None)
    LastName = property(get_LastName, None)
    SafeCustomerId = property(get_SafeCustomerId, None)
    SignInName = property(get_SignInName, None)
    Tickets = property(get_Tickets, None)
class OnlineIdAuthenticator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdAuthenticator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Authentication.OnlineId.OnlineIdAuthenticator.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdAuthenticator: ...
    @winrt_mixinmethod
    def AuthenticateUserAsync(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator, request: win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> win32more.Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_mixinmethod
    def AuthenticateUserAsyncAdvanced(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator, requests: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest], credentialPromptType: win32more.Windows.Security.Authentication.OnlineId.CredentialPromptType) -> win32more.Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_mixinmethod
    def SignOutUserAsync(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> win32more.Windows.Security.Authentication.OnlineId.SignOutUserOperation: ...
    @winrt_mixinmethod
    def put_ApplicationId(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> Guid: ...
    @winrt_mixinmethod
    def get_CanSignOut(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> Boolean: ...
    @winrt_mixinmethod
    def get_AuthenticatedSafeCustomerId(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> WinRT_String: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    AuthenticatedSafeCustomerId = property(get_AuthenticatedSafeCustomerId, None)
    CanSignOut = property(get_CanSignOut, None)
class OnlineIdServiceTicket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket'
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket) -> Int32: ...
    ErrorCode = property(get_ErrorCode, None)
    Request = property(get_Request, None)
    Value = property(get_Value, None)
class OnlineIdServiceTicketRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequest
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest.CreateOnlineIdServiceTicketRequestAdvanced(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest.CreateOnlineIdServiceTicketRequest(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateOnlineIdServiceTicketRequestAdvanced(cls: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequestFactory, service: WinRT_String) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_factorymethod
    def CreateOnlineIdServiceTicketRequest(cls: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequestFactory, service: WinRT_String, policy: WinRT_String) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Policy(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequest) -> WinRT_String: ...
    Policy = property(get_Policy, None)
    Service = property(get_Service, None)
class _OnlineIdSystemAuthenticator_Meta_(ComPtr.__class__):
    pass
class OnlineIdSystemAuthenticator(ComPtr, metaclass=_OnlineIdSystemAuthenticator_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticator'
    @winrt_classmethod
    def get_Default(cls: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorStatics) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorStatics, user: win32more.Windows.System.User) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    _OnlineIdSystemAuthenticator_Meta_.Default = property(get_Default, None)
class OnlineIdSystemAuthenticatorForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser'
    @winrt_mixinmethod
    def GetTicketAsync(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser, request: win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketResult]: ...
    @winrt_mixinmethod
    def put_ApplicationId(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser) -> Guid: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser) -> win32more.Windows.System.User: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    User = property(get_User, None)
class OnlineIdSystemIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemIdentity
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemIdentity'
    @winrt_mixinmethod
    def get_Ticket(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemIdentity) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemIdentity) -> WinRT_String: ...
    Id = property(get_Id, None)
    Ticket = property(get_Ticket, None)
class OnlineIdSystemTicketResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketResult'
    @winrt_mixinmethod
    def get_Identity(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemIdentity: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult) -> win32more.Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Identity = property(get_Identity, None)
    Status = property(get_Status, None)
class OnlineIdSystemTicketStatus(Enum, Int32):
    Success = 0
    Error = 1
    ServiceConnectionError = 2
class SignOutUserOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Security.Authentication.OnlineId.SignOutUserOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncAction, handler: win32more.Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncAction) -> win32more.Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class UserAuthenticationOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.OnlineId.UserIdentity]
    _classid_ = 'Windows.Security.Authentication.OnlineId.UserAuthenticationOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.OnlineId.UserIdentity], handler: win32more.Windows.Foundation.AsyncOperationCompletedHandler[win32more.Windows.Security.Authentication.OnlineId.UserIdentity]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.OnlineId.UserIdentity]) -> win32more.Windows.Foundation.AsyncOperationCompletedHandler[win32more.Windows.Security.Authentication.OnlineId.UserIdentity]: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.OnlineId.UserIdentity]) -> win32more.Windows.Security.Authentication.OnlineId.UserIdentity: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class UserIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity
    _classid_ = 'Windows.Security.Authentication.OnlineId.UserIdentity'
    @winrt_mixinmethod
    def get_Tickets(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SafeCustomerId(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SignInName(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirstName(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastName(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsBetaAccount(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsConfirmedPC(self: win32more.Windows.Security.Authentication.OnlineId.IUserIdentity) -> Boolean: ...
    FirstName = property(get_FirstName, None)
    Id = property(get_Id, None)
    IsBetaAccount = property(get_IsBetaAccount, None)
    IsConfirmedPC = property(get_IsConfirmedPC, None)
    LastName = property(get_LastName, None)
    SafeCustomerId = property(get_SafeCustomerId, None)
    SignInName = property(get_SignInName, None)
    Tickets = property(get_Tickets, None)


make_ready(__name__)
