from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Security.Credentials.UI
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AuthenticationProtocol = Int32
AuthenticationProtocol_Basic: AuthenticationProtocol = 0
AuthenticationProtocol_Digest: AuthenticationProtocol = 1
AuthenticationProtocol_Ntlm: AuthenticationProtocol = 2
AuthenticationProtocol_Kerberos: AuthenticationProtocol = 3
AuthenticationProtocol_Negotiate: AuthenticationProtocol = 4
AuthenticationProtocol_CredSsp: AuthenticationProtocol = 5
AuthenticationProtocol_Custom: AuthenticationProtocol = 6
class CredentialPicker(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Credentials.UI.CredentialPicker'
    @winrt_classmethod
    def PickWithOptionsAsync(cls: Windows.Security.Credentials.UI.ICredentialPickerStatics, options: Windows.Security.Credentials.UI.CredentialPickerOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_classmethod
    def PickWithMessageAsync(cls: Windows.Security.Credentials.UI.ICredentialPickerStatics, targetName: WinRT_String, message: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_classmethod
    def PickWithCaptionAsync(cls: Windows.Security.Credentials.UI.ICredentialPickerStatics, targetName: WinRT_String, message: WinRT_String, caption: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.CredentialPickerResults]: ...
class CredentialPickerOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Credentials.UI.CredentialPickerOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Credentials.UI.CredentialPickerOptions: ...
    @winrt_mixinmethod
    def put_Caption(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Caption(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ErrorCode(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_TargetName(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetName(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AuthenticationProtocol(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Windows.Security.Credentials.UI.AuthenticationProtocol) -> Void: ...
    @winrt_mixinmethod
    def get_AuthenticationProtocol(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Windows.Security.Credentials.UI.AuthenticationProtocol: ...
    @winrt_mixinmethod
    def put_CustomAuthenticationProtocol(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CustomAuthenticationProtocol(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PreviousCredential(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_PreviousCredential(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_AlwaysDisplayDialog(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysDisplayDialog(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_CallerSavesCredential(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CallerSavesCredential(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_CredentialSaveOption(self: Windows.Security.Credentials.UI.ICredentialPickerOptions, value: Windows.Security.Credentials.UI.CredentialSaveOption) -> Void: ...
    @winrt_mixinmethod
    def get_CredentialSaveOption(self: Windows.Security.Credentials.UI.ICredentialPickerOptions) -> Windows.Security.Credentials.UI.CredentialSaveOption: ...
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
class CredentialPickerResults(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Credentials.UI.CredentialPickerResults'
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> UInt32: ...
    @winrt_mixinmethod
    def get_CredentialSaveOption(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> Windows.Security.Credentials.UI.CredentialSaveOption: ...
    @winrt_mixinmethod
    def get_CredentialSaved(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> Boolean: ...
    @winrt_mixinmethod
    def get_Credential(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_CredentialDomainName(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CredentialUserName(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CredentialPassword(self: Windows.Security.Credentials.UI.ICredentialPickerResults) -> WinRT_String: ...
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
class ICredentialPickerOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('965a0b4c-95fa-467f-99-2b-0b-22-e5-85-9b-f6')
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
    def put_AuthenticationProtocol(self, value: Windows.Security.Credentials.UI.AuthenticationProtocol) -> Void: ...
    @winrt_commethod(15)
    def get_AuthenticationProtocol(self) -> Windows.Security.Credentials.UI.AuthenticationProtocol: ...
    @winrt_commethod(16)
    def put_CustomAuthenticationProtocol(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def get_CustomAuthenticationProtocol(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_PreviousCredential(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(19)
    def get_PreviousCredential(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(20)
    def put_AlwaysDisplayDialog(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_AlwaysDisplayDialog(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_CallerSavesCredential(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_CallerSavesCredential(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_CredentialSaveOption(self, value: Windows.Security.Credentials.UI.CredentialSaveOption) -> Void: ...
    @winrt_commethod(25)
    def get_CredentialSaveOption(self) -> Windows.Security.Credentials.UI.CredentialSaveOption: ...
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
class ICredentialPickerResults(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1948f99a-cc30-410c-9c-38-cc-08-84-c5-b3-d7')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CredentialSaveOption(self) -> Windows.Security.Credentials.UI.CredentialSaveOption: ...
    @winrt_commethod(8)
    def get_CredentialSaved(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Credential(self) -> Windows.Storage.Streams.IBuffer: ...
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
class ICredentialPickerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa3a5c73-c9ea-4782-99-fb-e6-d7-e9-38-e1-2d')
    @winrt_commethod(6)
    def PickWithOptionsAsync(self, options: Windows.Security.Credentials.UI.CredentialPickerOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_commethod(7)
    def PickWithMessageAsync(self, targetName: WinRT_String, message: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.CredentialPickerResults]: ...
    @winrt_commethod(8)
    def PickWithCaptionAsync(self, targetName: WinRT_String, message: WinRT_String, caption: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.CredentialPickerResults]: ...
class IUserConsentVerifierStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('af4f3f91-564c-4ddc-b8-b5-97-34-47-62-7c-65')
    @winrt_commethod(6)
    def CheckAvailabilityAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.UserConsentVerifierAvailability]: ...
    @winrt_commethod(7)
    def RequestVerificationAsync(self, message: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.UserConsentVerificationResult]: ...
UserConsentVerificationResult = Int32
UserConsentVerificationResult_Verified: UserConsentVerificationResult = 0
UserConsentVerificationResult_DeviceNotPresent: UserConsentVerificationResult = 1
UserConsentVerificationResult_NotConfiguredForUser: UserConsentVerificationResult = 2
UserConsentVerificationResult_DisabledByPolicy: UserConsentVerificationResult = 3
UserConsentVerificationResult_DeviceBusy: UserConsentVerificationResult = 4
UserConsentVerificationResult_RetriesExhausted: UserConsentVerificationResult = 5
UserConsentVerificationResult_Canceled: UserConsentVerificationResult = 6
class UserConsentVerifier(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Credentials.UI.UserConsentVerifier'
    @winrt_classmethod
    def CheckAvailabilityAsync(cls: Windows.Security.Credentials.UI.IUserConsentVerifierStatics) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.UserConsentVerifierAvailability]: ...
    @winrt_classmethod
    def RequestVerificationAsync(cls: Windows.Security.Credentials.UI.IUserConsentVerifierStatics, message: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.UI.UserConsentVerificationResult]: ...
UserConsentVerifierAvailability = Int32
UserConsentVerifierAvailability_Available: UserConsentVerifierAvailability = 0
UserConsentVerifierAvailability_DeviceNotPresent: UserConsentVerifierAvailability = 1
UserConsentVerifierAvailability_NotConfiguredForUser: UserConsentVerifierAvailability = 2
UserConsentVerifierAvailability_DisabledByPolicy: UserConsentVerifierAvailability = 3
UserConsentVerifierAvailability_DeviceBusy: UserConsentVerifierAvailability = 4
make_head(_module, 'CredentialPicker')
make_head(_module, 'CredentialPickerOptions')
make_head(_module, 'CredentialPickerResults')
make_head(_module, 'ICredentialPickerOptions')
make_head(_module, 'ICredentialPickerResults')
make_head(_module, 'ICredentialPickerStatics')
make_head(_module, 'IUserConsentVerifierStatics')
make_head(_module, 'UserConsentVerifier')
