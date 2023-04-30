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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Authentication.OnlineId
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
CredentialPromptType = Int32
CredentialPromptType_PromptIfNeeded: CredentialPromptType = 0
CredentialPromptType_RetypeCredentials: CredentialPromptType = 1
CredentialPromptType_DoNotPrompt: CredentialPromptType = 2
class IOnlineIdAuthenticator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a003f58a-29ab-4817-b8-84-d7-51-6d-ad-18-b9')
    @winrt_commethod(6)
    def AuthenticateUserAsync(self, request: Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_commethod(7)
    def AuthenticateUserAsyncAdvanced(self, requests: Windows.Foundation.Collections.IIterable[Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest], credentialPromptType: Windows.Security.Authentication.OnlineId.CredentialPromptType) -> Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_commethod(8)
    def SignOutUserAsync(self) -> Windows.Security.Authentication.OnlineId.SignOutUserOperation: ...
    @winrt_commethod(9)
    def put_ApplicationId(self, value: Guid) -> Void: ...
    @winrt_commethod(10)
    def get_ApplicationId(self) -> Guid: ...
    @winrt_commethod(11)
    def get_CanSignOut(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_AuthenticatedSafeCustomerId(self) -> WinRT_String: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    CanSignOut = property(get_CanSignOut, None)
    AuthenticatedSafeCustomerId = property(get_AuthenticatedSafeCustomerId, None)
class IOnlineIdServiceTicket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c95c547f-d781-4a94-ac-b8-c5-98-74-23-8c-26')
    @winrt_commethod(6)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Request(self) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> Int32: ...
    Value = property(get_Value, None)
    Request = property(get_Request, None)
    ErrorCode = property(get_ErrorCode, None)
class IOnlineIdServiceTicketRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('297445d3-fb63-4135-89-09-4e-35-4c-06-14-66')
    @winrt_commethod(6)
    def get_Service(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Policy(self) -> WinRT_String: ...
    Service = property(get_Service, None)
    Policy = property(get_Policy, None)
class IOnlineIdServiceTicketRequestFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bebb0a08-9e73-4077-96-14-08-61-4c-0b-c2-45')
    @winrt_commethod(6)
    def CreateOnlineIdServiceTicketRequest(self, service: WinRT_String, policy: WinRT_String) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_commethod(7)
    def CreateOnlineIdServiceTicketRequestAdvanced(self, service: WinRT_String) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
class IOnlineIdSystemAuthenticatorForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5798befb-1de4-4186-a2-e6-b5-63-f8-6a-af-44')
    @winrt_commethod(6)
    def GetTicketAsync(self, request: Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketResult]: ...
    @winrt_commethod(7)
    def put_ApplicationId(self, value: Guid) -> Void: ...
    @winrt_commethod(8)
    def get_ApplicationId(self) -> Guid: ...
    @winrt_commethod(9)
    def get_User(self) -> Windows.System.User: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    User = property(get_User, None)
class IOnlineIdSystemAuthenticatorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('85047792-f634-41e3-96-a4-51-64-e9-02-c7-40')
    @winrt_commethod(6)
    def get_Default(self) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    Default = property(get_Default, None)
class IOnlineIdSystemIdentity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('743cd20d-b6ca-434d-81-24-53-ea-12-68-53-07')
    @winrt_commethod(6)
    def get_Ticket(self) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    Ticket = property(get_Ticket, None)
    Id = property(get_Id, None)
class IOnlineIdSystemTicketResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('db0a5ff8-b098-4acd-9d-13-9e-64-06-52-b5-b6')
    @winrt_commethod(6)
    def get_Identity(self) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemIdentity: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Identity = property(get_Identity, None)
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IUserIdentity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2146d9cd-0742-4be3-8a-1c-7c-7a-e6-79-aa-88')
    @winrt_commethod(6)
    def get_Tickets(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket]: ...
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
    Tickets = property(get_Tickets, None)
    Id = property(get_Id, None)
    SafeCustomerId = property(get_SafeCustomerId, None)
    SignInName = property(get_SignInName, None)
    FirstName = property(get_FirstName, None)
    LastName = property(get_LastName, None)
    IsBetaAccount = property(get_IsBetaAccount, None)
    IsConfirmedPC = property(get_IsConfirmedPC, None)
class OnlineIdAuthenticator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdAuthenticator'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Authentication.OnlineId.OnlineIdAuthenticator: ...
    @winrt_mixinmethod
    def AuthenticateUserAsync(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator, request: Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_mixinmethod
    def AuthenticateUserAsyncAdvanced(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator, requests: Windows.Foundation.Collections.IIterable[Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest], credentialPromptType: Windows.Security.Authentication.OnlineId.CredentialPromptType) -> Windows.Security.Authentication.OnlineId.UserAuthenticationOperation: ...
    @winrt_mixinmethod
    def SignOutUserAsync(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> Windows.Security.Authentication.OnlineId.SignOutUserOperation: ...
    @winrt_mixinmethod
    def put_ApplicationId(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> Guid: ...
    @winrt_mixinmethod
    def get_CanSignOut(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> Boolean: ...
    @winrt_mixinmethod
    def get_AuthenticatedSafeCustomerId(self: Windows.Security.Authentication.OnlineId.IOnlineIdAuthenticator) -> WinRT_String: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    CanSignOut = property(get_CanSignOut, None)
    AuthenticatedSafeCustomerId = property(get_AuthenticatedSafeCustomerId, None)
class OnlineIdServiceTicket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket'
    @winrt_mixinmethod
    def get_Value(self: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Request(self: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicket) -> Int32: ...
    Value = property(get_Value, None)
    Request = property(get_Request, None)
    ErrorCode = property(get_ErrorCode, None)
class OnlineIdServiceTicketRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest'
    @winrt_factorymethod
    def CreateOnlineIdServiceTicketRequest(cls: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequestFactory, service: WinRT_String, policy: WinRT_String) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_factorymethod
    def CreateOnlineIdServiceTicketRequestAdvanced(cls: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequestFactory, service: WinRT_String) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest: ...
    @winrt_mixinmethod
    def get_Service(self: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Policy(self: Windows.Security.Authentication.OnlineId.IOnlineIdServiceTicketRequest) -> WinRT_String: ...
    Service = property(get_Service, None)
    Policy = property(get_Policy, None)
class OnlineIdSystemAuthenticator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticator'
    @winrt_classmethod
    def get_Default(cls: Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorStatics) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorStatics, user: Windows.System.User) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser: ...
    Default = property(get_Default, None)
class OnlineIdSystemAuthenticatorForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemAuthenticatorForUser'
    @winrt_mixinmethod
    def GetTicketAsync(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser, request: Windows.Security.Authentication.OnlineId.OnlineIdServiceTicketRequest) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketResult]: ...
    @winrt_mixinmethod
    def put_ApplicationId(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser) -> Guid: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemAuthenticatorForUser) -> Windows.System.User: ...
    ApplicationId = property(get_ApplicationId, put_ApplicationId)
    User = property(get_User, None)
class OnlineIdSystemIdentity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemIdentity'
    @winrt_mixinmethod
    def get_Ticket(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemIdentity) -> Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemIdentity) -> WinRT_String: ...
    Ticket = property(get_Ticket, None)
    Id = property(get_Id, None)
class OnlineIdSystemTicketResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketResult'
    @winrt_mixinmethod
    def get_Identity(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemIdentity: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult) -> Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Authentication.OnlineId.IOnlineIdSystemTicketResult) -> Windows.Foundation.HResult: ...
    Identity = property(get_Identity, None)
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
OnlineIdSystemTicketStatus = Int32
OnlineIdSystemTicketStatus_Success: OnlineIdSystemTicketStatus = 0
OnlineIdSystemTicketStatus_Error: OnlineIdSystemTicketStatus = 1
OnlineIdSystemTicketStatus_ServiceConnectionError: OnlineIdSystemTicketStatus = 2
class SignOutUserOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.SignOutUserOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncAction, handler: Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncAction) -> Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class UserAuthenticationOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.UserAuthenticationOperation'
    @winrt_mixinmethod
    def put_Completed(self: Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.OnlineId.UserIdentity], handler: Windows.Foundation.AsyncOperationCompletedHandler[Windows.Security.Authentication.OnlineId.UserIdentity]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.OnlineId.UserIdentity]) -> Windows.Foundation.AsyncOperationCompletedHandler[Windows.Security.Authentication.OnlineId.UserIdentity]: ...
    @winrt_mixinmethod
    def GetResults(self: Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.OnlineId.UserIdentity]) -> Windows.Security.Authentication.OnlineId.UserIdentity: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Foundation.IAsyncInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class UserIdentity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.OnlineId.UserIdentity'
    @winrt_mixinmethod
    def get_Tickets(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.OnlineId.OnlineIdServiceTicket]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SafeCustomerId(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SignInName(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirstName(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastName(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsBetaAccount(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsConfirmedPC(self: Windows.Security.Authentication.OnlineId.IUserIdentity) -> Boolean: ...
    Tickets = property(get_Tickets, None)
    Id = property(get_Id, None)
    SafeCustomerId = property(get_SafeCustomerId, None)
    SignInName = property(get_SignInName, None)
    FirstName = property(get_FirstName, None)
    LastName = property(get_LastName, None)
    IsBetaAccount = property(get_IsBetaAccount, None)
    IsConfirmedPC = property(get_IsConfirmedPC, None)
make_head(_module, 'IOnlineIdAuthenticator')
make_head(_module, 'IOnlineIdServiceTicket')
make_head(_module, 'IOnlineIdServiceTicketRequest')
make_head(_module, 'IOnlineIdServiceTicketRequestFactory')
make_head(_module, 'IOnlineIdSystemAuthenticatorForUser')
make_head(_module, 'IOnlineIdSystemAuthenticatorStatics')
make_head(_module, 'IOnlineIdSystemIdentity')
make_head(_module, 'IOnlineIdSystemTicketResult')
make_head(_module, 'IUserIdentity')
make_head(_module, 'OnlineIdAuthenticator')
make_head(_module, 'OnlineIdServiceTicket')
make_head(_module, 'OnlineIdServiceTicketRequest')
make_head(_module, 'OnlineIdSystemAuthenticator')
make_head(_module, 'OnlineIdSystemAuthenticatorForUser')
make_head(_module, 'OnlineIdSystemIdentity')
make_head(_module, 'OnlineIdSystemTicketResult')
make_head(_module, 'SignOutUserOperation')
make_head(_module, 'UserAuthenticationOperation')
make_head(_module, 'UserIdentity')
