from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Identity.Core
class IMicrosoftAccountMultiFactorAuthenticationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager'
    _iid_ = Guid('{0fd340a5-f574-4320-a08e-0a19a82322aa}')
    @winrt_commethod(6)
    def GetOneTimePassCodeAsync(self, userAccountId: WinRT_String, codeLength: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorOneTimeCodedInfo]: ...
    @winrt_commethod(7)
    def AddDeviceAsync(self, userAccountId: WinRT_String, authenticationToken: WinRT_String, wnsChannelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_commethod(8)
    def RemoveDeviceAsync(self, userAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_commethod(9)
    def UpdateWnsChannelAsync(self, userAccountId: WinRT_String, channelUri: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_commethod(10)
    def GetSessionsAsync(self, userAccountIdList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorGetSessionsResult]: ...
    @winrt_commethod(11)
    def GetSessionsAndUnregisteredAccountsAsync(self, userAccountIdList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo]: ...
    @winrt_commethod(12)
    def ApproveSessionUsingAuthSessionInfoAsync(self, sessionAuthentictionStatus: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionAuthenticationStatus, authenticationSessionInfo: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_commethod(13)
    def ApproveSessionAsync(self, sessionAuthentictionStatus: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionAuthenticationStatus, userAccountId: WinRT_String, sessionId: WinRT_String, sessionAuthenticationType: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_commethod(14)
    def DenySessionUsingAuthSessionInfoAsync(self, authenticationSessionInfo: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_commethod(15)
    def DenySessionAsync(self, userAccountId: WinRT_String, sessionId: WinRT_String, sessionAuthenticationType: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
class IMicrosoftAccountMultiFactorAuthenticatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticatorStatics'
    _iid_ = Guid('{d964c2e6-f446-4c71-8b79-6ea4024aa9b8}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationManager: ...
    Current = property(get_Current, None)
class IMicrosoftAccountMultiFactorGetSessionsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorGetSessionsResult'
    _iid_ = Guid('{4e23a9a0-e9fa-497a-95de-6d5747bf974c}')
    @winrt_commethod(6)
    def get_Sessions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo]: ...
    @winrt_commethod(7)
    def get_ServiceResponse(self) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse: ...
    Sessions = property(get_Sessions, None)
    ServiceResponse = property(get_ServiceResponse, None)
class IMicrosoftAccountMultiFactorOneTimeCodedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorOneTimeCodedInfo'
    _iid_ = Guid('{82ba264b-d87c-4668-a976-40cfae547d08}')
    @winrt_commethod(6)
    def get_Code(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TimeInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_TimeToLive(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ServiceResponse(self) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse: ...
    Code = property(get_Code, None)
    TimeInterval = property(get_TimeInterval, None)
    TimeToLive = property(get_TimeToLive, None)
    ServiceResponse = property(get_ServiceResponse, None)
class IMicrosoftAccountMultiFactorSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo'
    _iid_ = Guid('{5f7eabb4-a278-4635-b765-b494eb260af4}')
    @winrt_commethod(6)
    def get_UserAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplaySessionId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ApprovalStatus(self) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionApprovalStatus: ...
    @winrt_commethod(10)
    def get_AuthenticationType(self) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType: ...
    @winrt_commethod(11)
    def get_RequestTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    UserAccountId = property(get_UserAccountId, None)
    SessionId = property(get_SessionId, None)
    DisplaySessionId = property(get_DisplaySessionId, None)
    ApprovalStatus = property(get_ApprovalStatus, None)
    AuthenticationType = property(get_AuthenticationType, None)
    RequestTime = property(get_RequestTime, None)
    ExpirationTime = property(get_ExpirationTime, None)
class IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo'
    _iid_ = Guid('{aa7ec5fb-da3f-4088-a20d-5618afadb2e5}')
    @winrt_commethod(6)
    def get_Sessions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo]: ...
    @winrt_commethod(7)
    def get_UnregisteredAccounts(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ServiceResponse(self) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse: ...
    Sessions = property(get_Sessions, None)
    UnregisteredAccounts = property(get_UnregisteredAccounts, None)
    ServiceResponse = property(get_ServiceResponse, None)
class _MicrosoftAccountMultiFactorAuthenticationManager_Meta_(ComPtr.__class__):
    pass
class MicrosoftAccountMultiFactorAuthenticationManager(ComPtr, metaclass=_MicrosoftAccountMultiFactorAuthenticationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager
    _classid_ = 'Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationManager'
    @winrt_mixinmethod
    def GetOneTimePassCodeAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountId: WinRT_String, codeLength: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorOneTimeCodedInfo]: ...
    @winrt_mixinmethod
    def AddDeviceAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountId: WinRT_String, authenticationToken: WinRT_String, wnsChannelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_mixinmethod
    def RemoveDeviceAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_mixinmethod
    def UpdateWnsChannelAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountId: WinRT_String, channelUri: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_mixinmethod
    def GetSessionsAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountIdList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorGetSessionsResult]: ...
    @winrt_mixinmethod
    def GetSessionsAndUnregisteredAccountsAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountIdList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo]: ...
    @winrt_mixinmethod
    def ApproveSessionUsingAuthSessionInfoAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, sessionAuthentictionStatus: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionAuthenticationStatus, authenticationSessionInfo: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_mixinmethod
    def ApproveSessionAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, sessionAuthentictionStatus: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionAuthenticationStatus, userAccountId: WinRT_String, sessionId: WinRT_String, sessionAuthenticationType: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_mixinmethod
    def DenySessionUsingAuthSessionInfoAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, authenticationSessionInfo: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_mixinmethod
    def DenySessionAsync(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticationManager, userAccountId: WinRT_String, sessionId: WinRT_String, sessionAuthenticationType: win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorAuthenticatorStatics) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationManager: ...
    _MicrosoftAccountMultiFactorAuthenticationManager_Meta_.Current = property(get_Current.__wrapped__, None)
MicrosoftAccountMultiFactorAuthenticationType = Int32
MicrosoftAccountMultiFactorAuthenticationType_User: MicrosoftAccountMultiFactorAuthenticationType = 0
MicrosoftAccountMultiFactorAuthenticationType_Device: MicrosoftAccountMultiFactorAuthenticationType = 1
class MicrosoftAccountMultiFactorGetSessionsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorGetSessionsResult
    _classid_ = 'Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorGetSessionsResult'
    @winrt_mixinmethod
    def get_Sessions(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorGetSessionsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo]: ...
    @winrt_mixinmethod
    def get_ServiceResponse(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorGetSessionsResult) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse: ...
    Sessions = property(get_Sessions, None)
    ServiceResponse = property(get_ServiceResponse, None)
class MicrosoftAccountMultiFactorOneTimeCodedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorOneTimeCodedInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorOneTimeCodedInfo'
    @winrt_mixinmethod
    def get_Code(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorOneTimeCodedInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TimeInterval(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorOneTimeCodedInfo) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TimeToLive(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorOneTimeCodedInfo) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ServiceResponse(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorOneTimeCodedInfo) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse: ...
    Code = property(get_Code, None)
    TimeInterval = property(get_TimeInterval, None)
    TimeToLive = property(get_TimeToLive, None)
    ServiceResponse = property(get_ServiceResponse, None)
MicrosoftAccountMultiFactorServiceResponse = Int32
MicrosoftAccountMultiFactorServiceResponse_Success: MicrosoftAccountMultiFactorServiceResponse = 0
MicrosoftAccountMultiFactorServiceResponse_Error: MicrosoftAccountMultiFactorServiceResponse = 1
MicrosoftAccountMultiFactorServiceResponse_NoNetworkConnection: MicrosoftAccountMultiFactorServiceResponse = 2
MicrosoftAccountMultiFactorServiceResponse_ServiceUnavailable: MicrosoftAccountMultiFactorServiceResponse = 3
MicrosoftAccountMultiFactorServiceResponse_TotpSetupDenied: MicrosoftAccountMultiFactorServiceResponse = 4
MicrosoftAccountMultiFactorServiceResponse_NgcNotSetup: MicrosoftAccountMultiFactorServiceResponse = 5
MicrosoftAccountMultiFactorServiceResponse_SessionAlreadyDenied: MicrosoftAccountMultiFactorServiceResponse = 6
MicrosoftAccountMultiFactorServiceResponse_SessionAlreadyApproved: MicrosoftAccountMultiFactorServiceResponse = 7
MicrosoftAccountMultiFactorServiceResponse_SessionExpired: MicrosoftAccountMultiFactorServiceResponse = 8
MicrosoftAccountMultiFactorServiceResponse_NgcNonceExpired: MicrosoftAccountMultiFactorServiceResponse = 9
MicrosoftAccountMultiFactorServiceResponse_InvalidSessionId: MicrosoftAccountMultiFactorServiceResponse = 10
MicrosoftAccountMultiFactorServiceResponse_InvalidSessionType: MicrosoftAccountMultiFactorServiceResponse = 11
MicrosoftAccountMultiFactorServiceResponse_InvalidOperation: MicrosoftAccountMultiFactorServiceResponse = 12
MicrosoftAccountMultiFactorServiceResponse_InvalidStateTransition: MicrosoftAccountMultiFactorServiceResponse = 13
MicrosoftAccountMultiFactorServiceResponse_DeviceNotFound: MicrosoftAccountMultiFactorServiceResponse = 14
MicrosoftAccountMultiFactorServiceResponse_FlowDisabled: MicrosoftAccountMultiFactorServiceResponse = 15
MicrosoftAccountMultiFactorServiceResponse_SessionNotApproved: MicrosoftAccountMultiFactorServiceResponse = 16
MicrosoftAccountMultiFactorServiceResponse_OperationCanceledByUser: MicrosoftAccountMultiFactorServiceResponse = 17
MicrosoftAccountMultiFactorServiceResponse_NgcDisabledByServer: MicrosoftAccountMultiFactorServiceResponse = 18
MicrosoftAccountMultiFactorServiceResponse_NgcKeyNotFoundOnServer: MicrosoftAccountMultiFactorServiceResponse = 19
MicrosoftAccountMultiFactorServiceResponse_UIRequired: MicrosoftAccountMultiFactorServiceResponse = 20
MicrosoftAccountMultiFactorServiceResponse_DeviceIdChanged: MicrosoftAccountMultiFactorServiceResponse = 21
MicrosoftAccountMultiFactorSessionApprovalStatus = Int32
MicrosoftAccountMultiFactorSessionApprovalStatus_Pending: MicrosoftAccountMultiFactorSessionApprovalStatus = 0
MicrosoftAccountMultiFactorSessionApprovalStatus_Approved: MicrosoftAccountMultiFactorSessionApprovalStatus = 1
MicrosoftAccountMultiFactorSessionApprovalStatus_Denied: MicrosoftAccountMultiFactorSessionApprovalStatus = 2
MicrosoftAccountMultiFactorSessionAuthenticationStatus = Int32
MicrosoftAccountMultiFactorSessionAuthenticationStatus_Authenticated: MicrosoftAccountMultiFactorSessionAuthenticationStatus = 0
MicrosoftAccountMultiFactorSessionAuthenticationStatus_Unauthenticated: MicrosoftAccountMultiFactorSessionAuthenticationStatus = 1
class MicrosoftAccountMultiFactorSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo'
    @winrt_mixinmethod
    def get_UserAccountId(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplaySessionId(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApprovalStatus(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionApprovalStatus: ...
    @winrt_mixinmethod
    def get_AuthenticationType(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType: ...
    @winrt_mixinmethod
    def get_RequestTime(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorSessionInfo) -> win32more.Windows.Foundation.DateTime: ...
    UserAccountId = property(get_UserAccountId, None)
    SessionId = property(get_SessionId, None)
    DisplaySessionId = property(get_DisplaySessionId, None)
    ApprovalStatus = property(get_ApprovalStatus, None)
    AuthenticationType = property(get_AuthenticationType, None)
    RequestTime = property(get_RequestTime, None)
    ExpirationTime = property(get_ExpirationTime, None)
class MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo'
    @winrt_mixinmethod
    def get_Sessions(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionInfo]: ...
    @winrt_mixinmethod
    def get_UnregisteredAccounts(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ServiceResponse(self: win32more.Windows.Security.Authentication.Identity.Core.IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo) -> win32more.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse: ...
    Sessions = property(get_Sessions, None)
    UnregisteredAccounts = property(get_UnregisteredAccounts, None)
    ServiceResponse = property(get_ServiceResponse, None)


make_ready(__name__)
