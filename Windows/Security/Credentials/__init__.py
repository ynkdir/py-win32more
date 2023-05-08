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
import Windows.Security.Credentials
import Windows.Security.Cryptography.Core
import Windows.Storage.Streams
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
class ICredentialFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.ICredentialFactory'
    _iid_ = Guid('{54ef13a1-bf26-47b5-97dd-de779b7cad58}')
    @winrt_commethod(6)
    def CreatePasswordCredential(self: Windows.Security.Credentials.ICredentialFactory, resource: WinRT_String, userName: WinRT_String, password: WinRT_String) -> Windows.Security.Credentials.PasswordCredential: ...
class IKeyCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredential'
    _iid_ = Guid('{9585ef8d-457b-4847-b11a-fa960bbdb138}')
    @winrt_commethod(6)
    def get_Name(self: Windows.Security.Credentials.IKeyCredential) -> WinRT_String: ...
    @winrt_commethod(7)
    def RetrievePublicKeyWithDefaultBlobType(self: Windows.Security.Credentials.IKeyCredential) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def RetrievePublicKeyWithBlobType(self: Windows.Security.Credentials.IKeyCredential, blobType: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def RequestSignAsync(self: Windows.Security.Credentials.IKeyCredential, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialOperationResult]: ...
    @winrt_commethod(10)
    def GetAttestationAsync(self: Windows.Security.Credentials.IKeyCredential) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialAttestationResult]: ...
    Name = property(get_Name, None)
class IKeyCredentialAttestationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialAttestationResult'
    _iid_ = Guid('{78aab3a1-a3c1-4103-b6cc-472c44171cbb}')
    @winrt_commethod(6)
    def get_CertificateChainBuffer(self: Windows.Security.Credentials.IKeyCredentialAttestationResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_AttestationBuffer(self: Windows.Security.Credentials.IKeyCredentialAttestationResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_Status(self: Windows.Security.Credentials.IKeyCredentialAttestationResult) -> Windows.Security.Credentials.KeyCredentialAttestationStatus: ...
    CertificateChainBuffer = property(get_CertificateChainBuffer, None)
    AttestationBuffer = property(get_AttestationBuffer, None)
    Status = property(get_Status, None)
class IKeyCredentialManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialManagerStatics'
    _iid_ = Guid('{6aac468b-0ef1-4ce0-8290-4106da6a63b5}')
    @winrt_commethod(6)
    def IsSupportedAsync(self: Windows.Security.Credentials.IKeyCredentialManagerStatics) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RenewAttestationAsync(self: Windows.Security.Credentials.IKeyCredentialManagerStatics) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def RequestCreateAsync(self: Windows.Security.Credentials.IKeyCredentialManagerStatics, name: WinRT_String, option: Windows.Security.Credentials.KeyCredentialCreationOption) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_commethod(9)
    def OpenAsync(self: Windows.Security.Credentials.IKeyCredentialManagerStatics, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_commethod(10)
    def DeleteAsync(self: Windows.Security.Credentials.IKeyCredentialManagerStatics, name: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IKeyCredentialOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialOperationResult'
    _iid_ = Guid('{f53786c1-5261-4cdd-976d-cc909ac71620}')
    @winrt_commethod(6)
    def get_Result(self: Windows.Security.Credentials.IKeyCredentialOperationResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Status(self: Windows.Security.Credentials.IKeyCredentialOperationResult) -> Windows.Security.Credentials.KeyCredentialStatus: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class IKeyCredentialRetrievalResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialRetrievalResult'
    _iid_ = Guid('{58cd7703-8d87-4249-9b58-f6598cc9644e}')
    @winrt_commethod(6)
    def get_Credential(self: Windows.Security.Credentials.IKeyCredentialRetrievalResult) -> Windows.Security.Credentials.KeyCredential: ...
    @winrt_commethod(7)
    def get_Status(self: Windows.Security.Credentials.IKeyCredentialRetrievalResult) -> Windows.Security.Credentials.KeyCredentialStatus: ...
    Credential = property(get_Credential, None)
    Status = property(get_Status, None)
class IPasswordCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IPasswordCredential'
    _iid_ = Guid('{6ab18989-c720-41a7-a6c1-feadb36329a0}')
    @winrt_commethod(6)
    def get_Resource(self: Windows.Security.Credentials.IPasswordCredential) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Resource(self: Windows.Security.Credentials.IPasswordCredential, resource: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_UserName(self: Windows.Security.Credentials.IPasswordCredential) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_UserName(self: Windows.Security.Credentials.IPasswordCredential, userName: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Password(self: Windows.Security.Credentials.IPasswordCredential) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Password(self: Windows.Security.Credentials.IPasswordCredential, password: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def RetrievePassword(self: Windows.Security.Credentials.IPasswordCredential) -> Void: ...
    @winrt_commethod(13)
    def get_Properties(self: Windows.Security.Credentials.IPasswordCredential) -> Windows.Foundation.Collections.IPropertySet: ...
    Resource = property(get_Resource, put_Resource)
    UserName = property(get_UserName, put_UserName)
    Password = property(get_Password, put_Password)
    Properties = property(get_Properties, None)
class IPasswordVault(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IPasswordVault'
    _iid_ = Guid('{61fd2c0b-c8d4-48c1-a54f-bc5a64205af2}')
    @winrt_commethod(6)
    def Add(self: Windows.Security.Credentials.IPasswordVault, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(7)
    def Remove(self: Windows.Security.Credentials.IPasswordVault, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(8)
    def Retrieve(self: Windows.Security.Credentials.IPasswordVault, resource: WinRT_String, userName: WinRT_String) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(9)
    def FindAllByResource(self: Windows.Security.Credentials.IPasswordVault, resource: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_commethod(10)
    def FindAllByUserName(self: Windows.Security.Credentials.IPasswordVault, userName: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_commethod(11)
    def RetrieveAll(self: Windows.Security.Credentials.IPasswordVault) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.PasswordCredential]: ...
class IWebAccount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccount'
    _iid_ = Guid('{69473eb2-8031-49be-80bb-96cb46d99aba}')
    @winrt_commethod(6)
    def get_WebAccountProvider(self: Windows.Security.Credentials.IWebAccount) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_UserName(self: Windows.Security.Credentials.IWebAccount) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_State(self: Windows.Security.Credentials.IWebAccount) -> Windows.Security.Credentials.WebAccountState: ...
    WebAccountProvider = property(get_WebAccountProvider, None)
    UserName = property(get_UserName, None)
    State = property(get_State, None)
class IWebAccount2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccount2'
    _iid_ = Guid('{7b56d6f8-990b-4eb5-94a7-5621f3a8b824}')
    @winrt_commethod(6)
    def get_Id(self: Windows.Security.Credentials.IWebAccount2) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self: Windows.Security.Credentials.IWebAccount2) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(8)
    def GetPictureAsync(self: Windows.Security.Credentials.IWebAccount2, desizedSize: Windows.Security.Credentials.WebAccountPictureSize) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(9)
    def SignOutAsync(self: Windows.Security.Credentials.IWebAccount2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def SignOutWithClientIdAsync(self: Windows.Security.Credentials.IWebAccount2, clientId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class IWebAccountFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountFactory'
    _iid_ = Guid('{ac9afb39-1de9-4e92-b78f-0581a87f6e5c}')
    @winrt_commethod(6)
    def CreateWebAccount(self: Windows.Security.Credentials.IWebAccountFactory, webAccountProvider: Windows.Security.Credentials.WebAccountProvider, userName: WinRT_String, state: Windows.Security.Credentials.WebAccountState) -> Windows.Security.Credentials.WebAccount: ...
class IWebAccountProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider'
    _iid_ = Guid('{29dcc8c3-7ab9-4a7c-a336-b942f9dbf7c7}')
    @winrt_commethod(6)
    def get_Id(self: Windows.Security.Credentials.IWebAccountProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self: Windows.Security.Credentials.IWebAccountProvider) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IconUri(self: Windows.Security.Credentials.IWebAccountProvider) -> Windows.Foundation.Uri: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    IconUri = property(get_IconUri, None)
class IWebAccountProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider2'
    _iid_ = Guid('{4a01eb05-4e42-41d4-b518-e008a5163614}')
    @winrt_commethod(6)
    def get_DisplayPurpose(self: Windows.Security.Credentials.IWebAccountProvider2) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Authority(self: Windows.Security.Credentials.IWebAccountProvider2) -> WinRT_String: ...
    DisplayPurpose = property(get_DisplayPurpose, None)
    Authority = property(get_Authority, None)
class IWebAccountProvider3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider3'
    _iid_ = Guid('{da1c518b-970d-4d49-825c-f2706f8ca7fe}')
    @winrt_commethod(6)
    def get_User(self: Windows.Security.Credentials.IWebAccountProvider3) -> Windows.System.User: ...
    User = property(get_User, None)
class IWebAccountProvider4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider4'
    _iid_ = Guid('{718fd8db-e796-4210-b74e-84d29894b080}')
    @winrt_commethod(6)
    def get_IsSystemProvider(self: Windows.Security.Credentials.IWebAccountProvider4) -> Boolean: ...
    IsSystemProvider = property(get_IsSystemProvider, None)
class IWebAccountProviderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProviderFactory'
    _iid_ = Guid('{1d767df1-e1e1-4b9a-a774-5c7c7e3bf371}')
    @winrt_commethod(6)
    def CreateWebAccountProvider(self: Windows.Security.Credentials.IWebAccountProviderFactory, id: WinRT_String, displayName: WinRT_String, iconUri: Windows.Foundation.Uri) -> Windows.Security.Credentials.WebAccountProvider: ...
class KeyCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IKeyCredential
    _classid_ = 'Windows.Security.Credentials.KeyCredential'
    @winrt_mixinmethod
    def get_Name(self: Windows.Security.Credentials.IKeyCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def RetrievePublicKeyWithDefaultBlobType(self: Windows.Security.Credentials.IKeyCredential) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def RetrievePublicKeyWithBlobType(self: Windows.Security.Credentials.IKeyCredential, blobType: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def RequestSignAsync(self: Windows.Security.Credentials.IKeyCredential, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialOperationResult]: ...
    @winrt_mixinmethod
    def GetAttestationAsync(self: Windows.Security.Credentials.IKeyCredential) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialAttestationResult]: ...
    Name = property(get_Name, None)
class KeyCredentialAttestationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IKeyCredentialAttestationResult
    _classid_ = 'Windows.Security.Credentials.KeyCredentialAttestationResult'
    @winrt_mixinmethod
    def get_CertificateChainBuffer(self: Windows.Security.Credentials.IKeyCredentialAttestationResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AttestationBuffer(self: Windows.Security.Credentials.IKeyCredentialAttestationResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Credentials.IKeyCredentialAttestationResult) -> Windows.Security.Credentials.KeyCredentialAttestationStatus: ...
    CertificateChainBuffer = property(get_CertificateChainBuffer, None)
    AttestationBuffer = property(get_AttestationBuffer, None)
    Status = property(get_Status, None)
KeyCredentialAttestationStatus = Int32
KeyCredentialAttestationStatus_Success: KeyCredentialAttestationStatus = 0
KeyCredentialAttestationStatus_UnknownError: KeyCredentialAttestationStatus = 1
KeyCredentialAttestationStatus_NotSupported: KeyCredentialAttestationStatus = 2
KeyCredentialAttestationStatus_TemporaryFailure: KeyCredentialAttestationStatus = 3
KeyCredentialCreationOption = Int32
KeyCredentialCreationOption_ReplaceExisting: KeyCredentialCreationOption = 0
KeyCredentialCreationOption_FailIfExists: KeyCredentialCreationOption = 1
class KeyCredentialManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Credentials.KeyCredentialManager'
    @winrt_classmethod
    def IsSupportedAsync(cls: Windows.Security.Credentials.IKeyCredentialManagerStatics) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RenewAttestationAsync(cls: Windows.Security.Credentials.IKeyCredentialManagerStatics) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RequestCreateAsync(cls: Windows.Security.Credentials.IKeyCredentialManagerStatics, name: WinRT_String, option: Windows.Security.Credentials.KeyCredentialCreationOption) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_classmethod
    def OpenAsync(cls: Windows.Security.Credentials.IKeyCredentialManagerStatics, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_classmethod
    def DeleteAsync(cls: Windows.Security.Credentials.IKeyCredentialManagerStatics, name: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class KeyCredentialOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IKeyCredentialOperationResult
    _classid_ = 'Windows.Security.Credentials.KeyCredentialOperationResult'
    @winrt_mixinmethod
    def get_Result(self: Windows.Security.Credentials.IKeyCredentialOperationResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Credentials.IKeyCredentialOperationResult) -> Windows.Security.Credentials.KeyCredentialStatus: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class KeyCredentialRetrievalResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IKeyCredentialRetrievalResult
    _classid_ = 'Windows.Security.Credentials.KeyCredentialRetrievalResult'
    @winrt_mixinmethod
    def get_Credential(self: Windows.Security.Credentials.IKeyCredentialRetrievalResult) -> Windows.Security.Credentials.KeyCredential: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Credentials.IKeyCredentialRetrievalResult) -> Windows.Security.Credentials.KeyCredentialStatus: ...
    Credential = property(get_Credential, None)
    Status = property(get_Status, None)
KeyCredentialStatus = Int32
KeyCredentialStatus_Success: KeyCredentialStatus = 0
KeyCredentialStatus_UnknownError: KeyCredentialStatus = 1
KeyCredentialStatus_NotFound: KeyCredentialStatus = 2
KeyCredentialStatus_UserCanceled: KeyCredentialStatus = 3
KeyCredentialStatus_UserPrefersPassword: KeyCredentialStatus = 4
KeyCredentialStatus_CredentialAlreadyExists: KeyCredentialStatus = 5
KeyCredentialStatus_SecurityDeviceLocked: KeyCredentialStatus = 6
class PasswordCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IPasswordCredential
    _classid_ = 'Windows.Security.Credentials.PasswordCredential'
    @winrt_factorymethod
    def CreatePasswordCredential(cls: Windows.Security.Credentials.ICredentialFactory, resource: WinRT_String, userName: WinRT_String, password: WinRT_String) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_Resource(self: Windows.Security.Credentials.IPasswordCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Resource(self: Windows.Security.Credentials.IPasswordCredential, resource: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: Windows.Security.Credentials.IPasswordCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserName(self: Windows.Security.Credentials.IPasswordCredential, userName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: Windows.Security.Credentials.IPasswordCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Password(self: Windows.Security.Credentials.IPasswordCredential, password: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RetrievePassword(self: Windows.Security.Credentials.IPasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Security.Credentials.IPasswordCredential) -> Windows.Foundation.Collections.IPropertySet: ...
    Resource = property(get_Resource, put_Resource)
    UserName = property(get_UserName, put_UserName)
    Password = property(get_Password, put_Password)
    Properties = property(get_Properties, None)
class PasswordCredentialPropertyStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Security.Credentials.PasswordCredentialPropertyStore'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Security.Credentials.PasswordCredentialPropertyStore: ...
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
class PasswordVault(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IPasswordVault
    _classid_ = 'Windows.Security.Credentials.PasswordVault'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Security.Credentials.PasswordVault: ...
    @winrt_mixinmethod
    def Add(self: Windows.Security.Credentials.IPasswordVault, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Security.Credentials.IPasswordVault, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def Retrieve(self: Windows.Security.Credentials.IPasswordVault, resource: WinRT_String, userName: WinRT_String) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def FindAllByResource(self: Windows.Security.Credentials.IPasswordVault, resource: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_mixinmethod
    def FindAllByUserName(self: Windows.Security.Credentials.IPasswordVault, userName: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_mixinmethod
    def RetrieveAll(self: Windows.Security.Credentials.IPasswordVault) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.PasswordCredential]: ...
class WebAccount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IWebAccount
    _classid_ = 'Windows.Security.Credentials.WebAccount'
    @winrt_factorymethod
    def CreateWebAccount(cls: Windows.Security.Credentials.IWebAccountFactory, webAccountProvider: Windows.Security.Credentials.WebAccountProvider, userName: WinRT_String, state: Windows.Security.Credentials.WebAccountState) -> Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: Windows.Security.Credentials.IWebAccount) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_UserName(self: Windows.Security.Credentials.IWebAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Security.Credentials.IWebAccount) -> Windows.Security.Credentials.WebAccountState: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.Credentials.IWebAccount2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Security.Credentials.IWebAccount2) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def GetPictureAsync(self: Windows.Security.Credentials.IWebAccount2, desizedSize: Windows.Security.Credentials.WebAccountPictureSize) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def SignOutAsync(self: Windows.Security.Credentials.IWebAccount2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SignOutWithClientIdAsync(self: Windows.Security.Credentials.IWebAccount2, clientId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    WebAccountProvider = property(get_WebAccountProvider, None)
    UserName = property(get_UserName, None)
    State = property(get_State, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
WebAccountPictureSize = Int32
WebAccountPictureSize_Size64x64: WebAccountPictureSize = 64
WebAccountPictureSize_Size208x208: WebAccountPictureSize = 208
WebAccountPictureSize_Size424x424: WebAccountPictureSize = 424
WebAccountPictureSize_Size1080x1080: WebAccountPictureSize = 1080
class WebAccountProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Credentials.IWebAccountProvider
    _classid_ = 'Windows.Security.Credentials.WebAccountProvider'
    @winrt_factorymethod
    def CreateWebAccountProvider(cls: Windows.Security.Credentials.IWebAccountProviderFactory, id: WinRT_String, displayName: WinRT_String, iconUri: Windows.Foundation.Uri) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.Credentials.IWebAccountProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Security.Credentials.IWebAccountProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IconUri(self: Windows.Security.Credentials.IWebAccountProvider) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DisplayPurpose(self: Windows.Security.Credentials.IWebAccountProvider2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Authority(self: Windows.Security.Credentials.IWebAccountProvider2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Security.Credentials.IWebAccountProvider3) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_IsSystemProvider(self: Windows.Security.Credentials.IWebAccountProvider4) -> Boolean: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    IconUri = property(get_IconUri, None)
    DisplayPurpose = property(get_DisplayPurpose, None)
    Authority = property(get_Authority, None)
    User = property(get_User, None)
    IsSystemProvider = property(get_IsSystemProvider, None)
WebAccountState = Int32
WebAccountState_None: WebAccountState = 0
WebAccountState_Connected: WebAccountState = 1
WebAccountState_Error: WebAccountState = 2
make_head(_module, 'ICredentialFactory')
make_head(_module, 'IKeyCredential')
make_head(_module, 'IKeyCredentialAttestationResult')
make_head(_module, 'IKeyCredentialManagerStatics')
make_head(_module, 'IKeyCredentialOperationResult')
make_head(_module, 'IKeyCredentialRetrievalResult')
make_head(_module, 'IPasswordCredential')
make_head(_module, 'IPasswordVault')
make_head(_module, 'IWebAccount')
make_head(_module, 'IWebAccount2')
make_head(_module, 'IWebAccountFactory')
make_head(_module, 'IWebAccountProvider')
make_head(_module, 'IWebAccountProvider2')
make_head(_module, 'IWebAccountProvider3')
make_head(_module, 'IWebAccountProvider4')
make_head(_module, 'IWebAccountProviderFactory')
make_head(_module, 'KeyCredential')
make_head(_module, 'KeyCredentialAttestationResult')
make_head(_module, 'KeyCredentialManager')
make_head(_module, 'KeyCredentialOperationResult')
make_head(_module, 'KeyCredentialRetrievalResult')
make_head(_module, 'PasswordCredential')
make_head(_module, 'PasswordCredentialPropertyStore')
make_head(_module, 'PasswordVault')
make_head(_module, 'WebAccount')
make_head(_module, 'WebAccountProvider')
