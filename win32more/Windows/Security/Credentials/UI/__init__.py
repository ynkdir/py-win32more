from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Security.Credentials.UI
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class AuthenticationProtocol(Enum, Int32):
    Basic = 0
    Digest = 1
    Ntlm = 2
    Kerberos = 3
    Negotiate = 4
    CredSsp = 5
    Custom = 6
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Credentials.UI.CredentialPickerOptions.CreateInstance(*args))
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
    AlwaysDisplayDialog = property(get_AlwaysDisplayDialog, put_AlwaysDisplayDialog)
    AuthenticationProtocol = property(get_AuthenticationProtocol, put_AuthenticationProtocol)
    CallerSavesCredential = property(get_CallerSavesCredential, put_CallerSavesCredential)
    Caption = property(get_Caption, put_Caption)
    CredentialSaveOption = property(get_CredentialSaveOption, put_CredentialSaveOption)
    CustomAuthenticationProtocol = property(get_CustomAuthenticationProtocol, put_CustomAuthenticationProtocol)
    ErrorCode = property(get_ErrorCode, put_ErrorCode)
    Message = property(get_Message, put_Message)
    PreviousCredential = property(get_PreviousCredential, put_PreviousCredential)
    TargetName = property(get_TargetName, put_TargetName)
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
    Credential = property(get_Credential, None)
    CredentialDomainName = property(get_CredentialDomainName, None)
    CredentialPassword = property(get_CredentialPassword, None)
    CredentialSaveOption = property(get_CredentialSaveOption, None)
    CredentialSaved = property(get_CredentialSaved, None)
    CredentialUserName = property(get_CredentialUserName, None)
    ErrorCode = property(get_ErrorCode, None)
class CredentialSaveOption(Enum, Int32):
    Unselected = 0
    Selected = 1
    Hidden = 2
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
    AlwaysDisplayDialog = property(get_AlwaysDisplayDialog, put_AlwaysDisplayDialog)
    AuthenticationProtocol = property(get_AuthenticationProtocol, put_AuthenticationProtocol)
    CallerSavesCredential = property(get_CallerSavesCredential, put_CallerSavesCredential)
    Caption = property(get_Caption, put_Caption)
    CredentialSaveOption = property(get_CredentialSaveOption, put_CredentialSaveOption)
    CustomAuthenticationProtocol = property(get_CustomAuthenticationProtocol, put_CustomAuthenticationProtocol)
    ErrorCode = property(get_ErrorCode, put_ErrorCode)
    Message = property(get_Message, put_Message)
    PreviousCredential = property(get_PreviousCredential, put_PreviousCredential)
    TargetName = property(get_TargetName, put_TargetName)
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
    Credential = property(get_Credential, None)
    CredentialDomainName = property(get_CredentialDomainName, None)
    CredentialPassword = property(get_CredentialPassword, None)
    CredentialSaveOption = property(get_CredentialSaveOption, None)
    CredentialSaved = property(get_CredentialSaved, None)
    CredentialUserName = property(get_CredentialUserName, None)
    ErrorCode = property(get_ErrorCode, None)
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
class UserConsentVerificationResult(Enum, Int32):
    Verified = 0
    DeviceNotPresent = 1
    NotConfiguredForUser = 2
    DisabledByPolicy = 3
    DeviceBusy = 4
    RetriesExhausted = 5
    Canceled = 6
class UserConsentVerifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.UI.UserConsentVerifier'
    @winrt_classmethod
    def CheckAvailabilityAsync(cls: win32more.Windows.Security.Credentials.UI.IUserConsentVerifierStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.UserConsentVerifierAvailability]: ...
    @winrt_classmethod
    def RequestVerificationAsync(cls: win32more.Windows.Security.Credentials.UI.IUserConsentVerifierStatics, message: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.UI.UserConsentVerificationResult]: ...
class UserConsentVerifierAvailability(Enum, Int32):
    Available = 0
    DeviceNotPresent = 1
    NotConfiguredForUser = 2
    DisabledByPolicy = 3
    DeviceBusy = 4


make_ready(__name__)
