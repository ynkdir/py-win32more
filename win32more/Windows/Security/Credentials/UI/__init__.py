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
import win32more.Windows.Foundation
import win32more.Windows.Security.Credentials.UI
import win32more.Windows.Storage.Streams
AuthenticationProtocol = Int32
AuthenticationProtocol_Basic: AuthenticationProtocol = 0
AuthenticationProtocol_Digest: AuthenticationProtocol = 1
AuthenticationProtocol_Ntlm: AuthenticationProtocol = 2
AuthenticationProtocol_Kerberos: AuthenticationProtocol = 3
AuthenticationProtocol_Negotiate: AuthenticationProtocol = 4
AuthenticationProtocol_CredSsp: AuthenticationProtocol = 5
AuthenticationProtocol_Custom: AuthenticationProtocol = 6
class CredentialPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.CredentialPicker'
    @winrt_classmethod
    def PickWithOptionsAsync(cls: win32more.Windows.Security.Credentials.UI.ICredentialPickerStatics, options: win32more.Windows.Security.Credentials.UI.CredentialPickerOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_classmethod
    def PickWithMessageAsync(cls: win32more.Windows.Security.Credentials.UI.ICredentialPickerStatics, targetName: WinRT_String, message: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_classmethod
    def PickWithCaptionAsync(cls: win32more.Windows.Security.Credentials.UI.ICredentialPickerStatics, targetName: WinRT_String, message: WinRT_String, caption: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.CredentialPickerResults]: ...
class CredentialPickerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions
    _classid_ = 'Windows.Security.Credentials.UI.CredentialPickerOptions'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Security.Credentials.UI.CredentialPickerOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Credentials.UI.CredentialPickerOptions: ...
    @winrt_mixinmethod
    def put_Caption(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Caption(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ErrorCode(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_TargetName(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetName(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AuthenticationProtocol(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: win32more.Windows.Security.Credentials.UI.AuthenticationProtocol) -> Void: ...
    @winrt_mixinmethod
    def get_AuthenticationProtocol(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> win32more.Windows.Security.Credentials.UI.AuthenticationProtocol: ...
    @winrt_mixinmethod
    def put_CustomAuthenticationProtocol(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CustomAuthenticationProtocol(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PreviousCredential(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_PreviousCredential(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_AlwaysDisplayDialog(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysDisplayDialog(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_CallerSavesCredential(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CallerSavesCredential(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_CredentialSaveOption(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions, value: win32more.Windows.Security.Credentials.UI.CredentialSaveOption) -> Void: ...
    @winrt_mixinmethod
    def get_CredentialSaveOption(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerOptions) -> win32more.Windows.Security.Credentials.UI.CredentialSaveOption: ...
    Caption = property(get_Caption, put_Caption)
    Message = property(get_Message, put_Message)
    ErrorCode = property(get_ErrorCode, put_ErrorCode)
    TargetName = property(get_TargetName, put_TargetName)
    AuthenticationProtocol = property(get_AuthenticationProtocol, put_AuthenticationProtocol)
    CustomAuthenticationProtocol = property(get_CustomAuthenticationProtocol, put_CustomAuthenticationProtocol)
    PreviousCredential = property(get_PreviousCredential, put_PreviousCredential)
    AlwaysDisplayDialog = property(get_AlwaysDisplayDialog, put_AlwaysDisplayDialog)
    CallerSavesCredential = property(get_CallerSavesCredential, put_CallerSavesCredential)
    CredentialSaveOption = property(get_CredentialSaveOption, put_CredentialSaveOption)
class CredentialPickerResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults
    _classid_ = 'Windows.Security.Credentials.UI.CredentialPickerResults'
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> UInt32: ...
    @winrt_mixinmethod
    def get_CredentialSaveOption(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> win32more.Windows.Security.Credentials.UI.CredentialSaveOption: ...
    @winrt_mixinmethod
    def get_CredentialSaved(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> Boolean: ...
    @winrt_mixinmethod
    def get_Credential(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_CredentialDomainName(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CredentialUserName(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CredentialPassword(self: win32more.Windows.Security.Credentials.UI.ICredentialPickerResults) -> WinRT_String: ...
    ErrorCode = property(get_ErrorCode, None)
    CredentialSaveOption = property(get_CredentialSaveOption, None)
    CredentialSaved = property(get_CredentialSaved, None)
    Credential = property(get_Credential, None)
    CredentialDomainName = property(get_CredentialDomainName, None)
    CredentialUserName = property(get_CredentialUserName, None)
    CredentialPassword = property(get_CredentialPassword, None)
CredentialSaveOption = Int32
CredentialSaveOption_Unselected: CredentialSaveOption = 0
CredentialSaveOption_Selected: CredentialSaveOption = 1
CredentialSaveOption_Hidden: CredentialSaveOption = 2
class ICredentialPickerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.ICredentialPickerOptions'
    _iid_ = Guid('{965a0b4c-95fa-467f-992b-0b22e5859bf6}')
    @winrt_commethod(6)
    def put_Caption(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Message(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ErrorCode(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_ErrorCode(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_TargetName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_TargetName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_AuthenticationProtocol(self, value: win32more.Windows.Security.Credentials.UI.AuthenticationProtocol) -> Void: ...
    @winrt_commethod(15)
    def get_AuthenticationProtocol(self) -> win32more.Windows.Security.Credentials.UI.AuthenticationProtocol: ...
    @winrt_commethod(16)
    def put_CustomAuthenticationProtocol(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def get_CustomAuthenticationProtocol(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_PreviousCredential(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(19)
    def get_PreviousCredential(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(20)
    def put_AlwaysDisplayDialog(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_AlwaysDisplayDialog(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_CallerSavesCredential(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_CallerSavesCredential(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_CredentialSaveOption(self, value: win32more.Windows.Security.Credentials.UI.CredentialSaveOption) -> Void: ...
    @winrt_commethod(25)
    def get_CredentialSaveOption(self) -> win32more.Windows.Security.Credentials.UI.CredentialSaveOption: ...
    Caption = property(get_Caption, put_Caption)
    Message = property(get_Message, put_Message)
    ErrorCode = property(get_ErrorCode, put_ErrorCode)
    TargetName = property(get_TargetName, put_TargetName)
    AuthenticationProtocol = property(get_AuthenticationProtocol, put_AuthenticationProtocol)
    CustomAuthenticationProtocol = property(get_CustomAuthenticationProtocol, put_CustomAuthenticationProtocol)
    PreviousCredential = property(get_PreviousCredential, put_PreviousCredential)
    AlwaysDisplayDialog = property(get_AlwaysDisplayDialog, put_AlwaysDisplayDialog)
    CallerSavesCredential = property(get_CallerSavesCredential, put_CallerSavesCredential)
    CredentialSaveOption = property(get_CredentialSaveOption, put_CredentialSaveOption)
class ICredentialPickerResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.ICredentialPickerResults'
    _iid_ = Guid('{1948f99a-cc30-410c-9c38-cc0884c5b3d7}')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CredentialSaveOption(self) -> win32more.Windows.Security.Credentials.UI.CredentialSaveOption: ...
    @winrt_commethod(8)
    def get_CredentialSaved(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Credential(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def get_CredentialDomainName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_CredentialUserName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_CredentialPassword(self) -> WinRT_String: ...
    ErrorCode = property(get_ErrorCode, None)
    CredentialSaveOption = property(get_CredentialSaveOption, None)
    CredentialSaved = property(get_CredentialSaved, None)
    Credential = property(get_Credential, None)
    CredentialDomainName = property(get_CredentialDomainName, None)
    CredentialUserName = property(get_CredentialUserName, None)
    CredentialPassword = property(get_CredentialPassword, None)
class ICredentialPickerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.ICredentialPickerStatics'
    _iid_ = Guid('{aa3a5c73-c9ea-4782-99fb-e6d7e938e12d}')
    @winrt_commethod(6)
    def PickWithOptionsAsync(self, options: win32more.Windows.Security.Credentials.UI.CredentialPickerOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_commethod(7)
    def PickWithMessageAsync(self, targetName: WinRT_String, message: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_commethod(8)
    def PickWithCaptionAsync(self, targetName: WinRT_String, message: WinRT_String, caption: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.CredentialPickerResults]: ...
class IUserConsentVerifierStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.IUserConsentVerifierStatics'
    _iid_ = Guid('{af4f3f91-564c-4ddc-b8b5-973447627c65}')
    @winrt_commethod(6)
    def CheckAvailabilityAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.UserConsentVerifierAvailability]: ...
    @winrt_commethod(7)
    def RequestVerificationAsync(self, message: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.UserConsentVerificationResult]: ...
UserConsentVerificationResult = Int32
UserConsentVerificationResult_Verified: UserConsentVerificationResult = 0
UserConsentVerificationResult_DeviceNotPresent: UserConsentVerificationResult = 1
UserConsentVerificationResult_NotConfiguredForUser: UserConsentVerificationResult = 2
UserConsentVerificationResult_DisabledByPolicy: UserConsentVerificationResult = 3
UserConsentVerificationResult_DeviceBusy: UserConsentVerificationResult = 4
UserConsentVerificationResult_RetriesExhausted: UserConsentVerificationResult = 5
UserConsentVerificationResult_Canceled: UserConsentVerificationResult = 6
class UserConsentVerifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.UserConsentVerifier'
    @winrt_classmethod
    def CheckAvailabilityAsync(cls: win32more.Windows.Security.Credentials.UI.IUserConsentVerifierStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.UserConsentVerifierAvailability]: ...
    @winrt_classmethod
    def RequestVerificationAsync(cls: win32more.Windows.Security.Credentials.UI.IUserConsentVerifierStatics, message: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.UserConsentVerificationResult]: ...
UserConsentVerifierAvailability = Int32
UserConsentVerifierAvailability_Available: UserConsentVerifierAvailability = 0
UserConsentVerifierAvailability_DeviceNotPresent: UserConsentVerifierAvailability = 1
UserConsentVerifierAvailability_NotConfiguredForUser: UserConsentVerifierAvailability = 2
UserConsentVerifierAvailability_DisabledByPolicy: UserConsentVerifierAvailability = 3
UserConsentVerifierAvailability_DeviceBusy: UserConsentVerifierAvailability = 4
make_ready(__name__)
