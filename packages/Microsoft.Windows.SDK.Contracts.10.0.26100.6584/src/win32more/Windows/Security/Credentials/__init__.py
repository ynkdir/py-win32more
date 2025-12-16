from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Credentials
import win32more.Windows.Security.Cryptography.Core
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI
class AttestationChallengeHandler(MulticastDelegate):
    extends: IUnknown
    _iid_ = Guid('{f6ae35b0-d805-587d-944f-a09bd032acf5}')
    @winrt_commethod(3)
    def Invoke(self, challenge: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
class ChallengeResponseKind(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.ChallengeResponseKind'
    VirtualizationBasedSecurityEnclave = 0
class ICredentialFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.ICredentialFactory'
    _iid_ = Guid('{54ef13a1-bf26-47b5-97dd-de779b7cad58}')
    @winrt_commethod(6)
    def CreatePasswordCredential(self, resource: hstr, userName: hstr, password: hstr) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
class IKeyCredential(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredential'
    _iid_ = Guid('{9585ef8d-457b-4847-b11a-fa960bbdb138}')
    @winrt_commethod(6)
    def get_Name(self) -> hstr: ...
    @winrt_commethod(7)
    def RetrievePublicKeyWithDefaultBlobType(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def RetrievePublicKeyWithBlobType(self, blobType: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def RequestSignAsync(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialOperationResult]: ...
    @winrt_commethod(10)
    def GetAttestationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialAttestationResult]: ...
    Name = property(get_Name, None)
class IKeyCredential2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredential2'
    _iid_ = Guid('{ca343273-f558-53ef-b943-4a3ec81a217e}')
    @winrt_commethod(6)
    def RequestDeriveSharedSecretAsync(self, windowId: win32more.Windows.UI.WindowId, message: hstr, publicKey: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialOperationResult]: ...
    @winrt_commethod(7)
    def RetrieveAuthorizationContext(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
class IKeyCredentialAttestationResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialAttestationResult'
    _iid_ = Guid('{78aab3a1-a3c1-4103-b6cc-472c44171cbb}')
    @winrt_commethod(6)
    def get_CertificateChainBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_AttestationBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Security.Credentials.KeyCredentialAttestationStatus: ...
    AttestationBuffer = property(get_AttestationBuffer, None)
    CertificateChainBuffer = property(get_CertificateChainBuffer, None)
    Status = property(get_Status, None)
class IKeyCredentialCacheConfiguration(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialCacheConfiguration'
    _iid_ = Guid('{438bd21a-61ff-5468-95a6-b1d5216e458d}')
    @winrt_commethod(6)
    def get_CacheOption(self) -> win32more.Windows.Security.Credentials.KeyCredentialCacheOption: ...
    @winrt_commethod(7)
    def get_Timeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_UsageCount(self) -> UInt32: ...
    CacheOption = property(get_CacheOption, None)
    Timeout = property(get_Timeout, None)
    UsageCount = property(get_UsageCount, None)
class IKeyCredentialCacheConfigurationFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialCacheConfigurationFactory'
    _iid_ = Guid('{9948c31b-c827-5b58-9442-40acd8ab1e7d}')
    @winrt_commethod(6)
    def CreateInstance(self, cacheOption: win32more.Windows.Security.Credentials.KeyCredentialCacheOption, timeout: win32more.Windows.Foundation.TimeSpan, usageCount: UInt32) -> win32more.Windows.Security.Credentials.KeyCredentialCacheConfiguration: ...
class IKeyCredentialManagerExtendedStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialManagerExtendedStatics'
    _iid_ = Guid('{a5312d27-b408-5011-9b36-b07ab0a67a7e}')
    @winrt_commethod(6)
    def RequestCreateAsync(self, name: hstr, option: win32more.Windows.Security.Credentials.KeyCredentialCreationOption, algorithm: hstr, message: hstr, cacheConfiguration: win32more.Windows.Security.Credentials.KeyCredentialCacheConfiguration, windowId: win32more.Windows.UI.WindowId, callbackType: win32more.Windows.Security.Credentials.ChallengeResponseKind, attestationCallback: win32more.Windows.Security.Credentials.AttestationChallengeHandler) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_commethod(7)
    def OpenAsync(self, name: hstr, callbackType: win32more.Windows.Security.Credentials.ChallengeResponseKind, attestationCallback: win32more.Windows.Security.Credentials.AttestationChallengeHandler) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
class IKeyCredentialManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialManagerStatics'
    _iid_ = Guid('{6aac468b-0ef1-4ce0-8290-4106da6a63b5}')
    @winrt_commethod(6)
    def IsSupportedAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RenewAttestationAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def RequestCreateAsync(self, name: hstr, option: win32more.Windows.Security.Credentials.KeyCredentialCreationOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_commethod(9)
    def OpenAsync(self, name: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_commethod(10)
    def DeleteAsync(self, name: hstr) -> win32more.Windows.Foundation.IAsyncAction: ...
class IKeyCredentialOperationResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialOperationResult'
    _iid_ = Guid('{f53786c1-5261-4cdd-976d-cc909ac71620}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Security.Credentials.KeyCredentialStatus: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class IKeyCredentialRetrievalResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IKeyCredentialRetrievalResult'
    _iid_ = Guid('{58cd7703-8d87-4249-9b58-f6598cc9644e}')
    @winrt_commethod(6)
    def get_Credential(self) -> win32more.Windows.Security.Credentials.KeyCredential: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Security.Credentials.KeyCredentialStatus: ...
    Credential = property(get_Credential, None)
    Status = property(get_Status, None)
class IPasswordCredential(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IPasswordCredential'
    _iid_ = Guid('{6ab18989-c720-41a7-a6c1-feadb36329a0}')
    @winrt_commethod(6)
    def get_Resource(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Resource(self, resource: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_UserName(self) -> hstr: ...
    @winrt_commethod(9)
    def put_UserName(self, userName: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_Password(self) -> hstr: ...
    @winrt_commethod(11)
    def put_Password(self, password: hstr) -> Void: ...
    @winrt_commethod(12)
    def RetrievePassword(self) -> Void: ...
    @winrt_commethod(13)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Password = property(get_Password, put_Password)
    Properties = property(get_Properties, None)
    Resource = property(get_Resource, put_Resource)
    UserName = property(get_UserName, put_UserName)
class IPasswordVault(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IPasswordVault'
    _iid_ = Guid('{61fd2c0b-c8d4-48c1-a54f-bc5a64205af2}')
    @winrt_commethod(6)
    def Add(self, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(7)
    def Remove(self, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(8)
    def Retrieve(self, resource: hstr, userName: hstr) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(9)
    def FindAllByResource(self, resource: hstr) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_commethod(10)
    def FindAllByUserName(self, userName: hstr) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_commethod(11)
    def RetrieveAll(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.PasswordCredential]: ...
class IWebAccount(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccount'
    _iid_ = Guid('{69473eb2-8031-49be-80bb-96cb46d99aba}')
    @winrt_commethod(6)
    def get_WebAccountProvider(self) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_UserName(self) -> hstr: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.Security.Credentials.WebAccountState: ...
    State = property(get_State, None)
    UserName = property(get_UserName, None)
    WebAccountProvider = property(get_WebAccountProvider, None)
class IWebAccount2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccount2'
    _iid_ = Guid('{7b56d6f8-990b-4eb5-94a7-5621f3a8b824}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[hstr, hstr]: ...
    @winrt_commethod(8)
    def GetPictureAsync(self, desizedSize: win32more.Windows.Security.Credentials.WebAccountPictureSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(9)
    def SignOutAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def SignOutWithClientIdAsync(self, clientId: hstr) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class IWebAccountFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountFactory'
    _iid_ = Guid('{ac9afb39-1de9-4e92-b78f-0581a87f6e5c}')
    @winrt_commethod(6)
    def CreateWebAccount(self, webAccountProvider: win32more.Windows.Security.Credentials.WebAccountProvider, userName: hstr, state: win32more.Windows.Security.Credentials.WebAccountState) -> win32more.Windows.Security.Credentials.WebAccount: ...
class IWebAccountProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider'
    _iid_ = Guid('{29dcc8c3-7ab9-4a7c-a336-b942f9dbf7c7}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> hstr: ...
    @winrt_commethod(8)
    def get_IconUri(self) -> win32more.Windows.Foundation.Uri: ...
    DisplayName = property(get_DisplayName, None)
    IconUri = property(get_IconUri, None)
    Id = property(get_Id, None)
class IWebAccountProvider2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider2'
    _iid_ = Guid('{4a01eb05-4e42-41d4-b518-e008a5163614}')
    @winrt_commethod(6)
    def get_DisplayPurpose(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Authority(self) -> hstr: ...
    Authority = property(get_Authority, None)
    DisplayPurpose = property(get_DisplayPurpose, None)
class IWebAccountProvider3(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider3'
    _iid_ = Guid('{da1c518b-970d-4d49-825c-f2706f8ca7fe}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IWebAccountProvider4(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProvider4'
    _iid_ = Guid('{718fd8db-e796-4210-b74e-84d29894b080}')
    @winrt_commethod(6)
    def get_IsSystemProvider(self) -> Boolean: ...
    IsSystemProvider = property(get_IsSystemProvider, None)
class IWebAccountProviderFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.IWebAccountProviderFactory'
    _iid_ = Guid('{1d767df1-e1e1-4b9a-a774-5c7c7e3bf371}')
    @winrt_commethod(6)
    def CreateWebAccountProvider(self, id: hstr, displayName: hstr, iconUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
class KeyCredential(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IKeyCredential
    _classid_ = 'Windows.Security.Credentials.KeyCredential'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Security.Credentials.IKeyCredential) -> hstr: ...
    @winrt_mixinmethod
    def RetrievePublicKeyWithDefaultBlobType(self: win32more.Windows.Security.Credentials.IKeyCredential) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def RetrievePublicKeyWithBlobType(self: win32more.Windows.Security.Credentials.IKeyCredential, blobType: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def RequestSignAsync(self: win32more.Windows.Security.Credentials.IKeyCredential, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialOperationResult]: ...
    @winrt_mixinmethod
    def GetAttestationAsync(self: win32more.Windows.Security.Credentials.IKeyCredential) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialAttestationResult]: ...
    @winrt_mixinmethod
    def RequestDeriveSharedSecretAsync(self: win32more.Windows.Security.Credentials.IKeyCredential2, windowId: win32more.Windows.UI.WindowId, message: hstr, publicKey: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialOperationResult]: ...
    @winrt_mixinmethod
    def RetrieveAuthorizationContext(self: win32more.Windows.Security.Credentials.IKeyCredential2) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Name = property(get_Name, None)
class KeyCredentialAttestationResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IKeyCredentialAttestationResult
    _classid_ = 'Windows.Security.Credentials.KeyCredentialAttestationResult'
    @winrt_mixinmethod
    def get_CertificateChainBuffer(self: win32more.Windows.Security.Credentials.IKeyCredentialAttestationResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AttestationBuffer(self: win32more.Windows.Security.Credentials.IKeyCredentialAttestationResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Credentials.IKeyCredentialAttestationResult) -> win32more.Windows.Security.Credentials.KeyCredentialAttestationStatus: ...
    AttestationBuffer = property(get_AttestationBuffer, None)
    CertificateChainBuffer = property(get_CertificateChainBuffer, None)
    Status = property(get_Status, None)
class KeyCredentialAttestationStatus(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.KeyCredentialAttestationStatus'
    Success = 0
    UnknownError = 1
    NotSupported = 2
    TemporaryFailure = 3
class KeyCredentialCacheConfiguration(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IKeyCredentialCacheConfiguration
    _classid_ = 'Windows.Security.Credentials.KeyCredentialCacheConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Credentials.KeyCredentialCacheConfiguration.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Security.Credentials.IKeyCredentialCacheConfigurationFactory, cacheOption: win32more.Windows.Security.Credentials.KeyCredentialCacheOption, timeout: win32more.Windows.Foundation.TimeSpan, usageCount: UInt32) -> win32more.Windows.Security.Credentials.KeyCredentialCacheConfiguration: ...
    @winrt_mixinmethod
    def get_CacheOption(self: win32more.Windows.Security.Credentials.IKeyCredentialCacheConfiguration) -> win32more.Windows.Security.Credentials.KeyCredentialCacheOption: ...
    @winrt_mixinmethod
    def get_Timeout(self: win32more.Windows.Security.Credentials.IKeyCredentialCacheConfiguration) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UsageCount(self: win32more.Windows.Security.Credentials.IKeyCredentialCacheConfiguration) -> UInt32: ...
    CacheOption = property(get_CacheOption, None)
    Timeout = property(get_Timeout, None)
    UsageCount = property(get_UsageCount, None)
class KeyCredentialCacheOption(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.KeyCredentialCacheOption'
    NoCache = 1
    CacheWhenUnlocked = 2
    CacheUnderLock = 4
class KeyCredentialCreationOption(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.KeyCredentialCreationOption'
    ReplaceExisting = 0
    FailIfExists = 1
class KeyCredentialManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Credentials.KeyCredentialManager'
    @winrt_overload
    @winrt_classmethod
    def RequestCreateAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerExtendedStatics, name: hstr, option: win32more.Windows.Security.Credentials.KeyCredentialCreationOption, algorithm: hstr, message: hstr, cacheConfiguration: win32more.Windows.Security.Credentials.KeyCredentialCacheConfiguration, windowId: win32more.Windows.UI.WindowId, callbackType: win32more.Windows.Security.Credentials.ChallengeResponseKind, attestationCallback: win32more.Windows.Security.Credentials.AttestationChallengeHandler) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_overload
    @winrt_classmethod
    def OpenAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerExtendedStatics, name: hstr, callbackType: win32more.Windows.Security.Credentials.ChallengeResponseKind, attestationCallback: win32more.Windows.Security.Credentials.AttestationChallengeHandler) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_classmethod
    def IsSupportedAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RenewAttestationAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerStatics) -> win32more.Windows.Foundation.IAsyncAction: ...
    @RequestCreateAsync.register
    @winrt_classmethod
    def RequestCreateAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerStatics, name: hstr, option: win32more.Windows.Security.Credentials.KeyCredentialCreationOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @OpenAsync.register
    @winrt_classmethod
    def OpenAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerStatics, name: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.KeyCredentialRetrievalResult]: ...
    @winrt_classmethod
    def DeleteAsync(cls: win32more.Windows.Security.Credentials.IKeyCredentialManagerStatics, name: hstr) -> win32more.Windows.Foundation.IAsyncAction: ...
class KeyCredentialOperationResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IKeyCredentialOperationResult
    _classid_ = 'Windows.Security.Credentials.KeyCredentialOperationResult'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Security.Credentials.IKeyCredentialOperationResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Credentials.IKeyCredentialOperationResult) -> win32more.Windows.Security.Credentials.KeyCredentialStatus: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class KeyCredentialRetrievalResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IKeyCredentialRetrievalResult
    _classid_ = 'Windows.Security.Credentials.KeyCredentialRetrievalResult'
    @winrt_mixinmethod
    def get_Credential(self: win32more.Windows.Security.Credentials.IKeyCredentialRetrievalResult) -> win32more.Windows.Security.Credentials.KeyCredential: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Credentials.IKeyCredentialRetrievalResult) -> win32more.Windows.Security.Credentials.KeyCredentialStatus: ...
    Credential = property(get_Credential, None)
    Status = property(get_Status, None)
class KeyCredentialStatus(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.KeyCredentialStatus'
    Success = 0
    UnknownError = 1
    NotFound = 2
    UserCanceled = 3
    UserPrefersPassword = 4
    CredentialAlreadyExists = 5
    SecurityDeviceLocked = 6
class PasswordCredential(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IPasswordCredential
    _classid_ = 'Windows.Security.Credentials.PasswordCredential'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Credentials.PasswordCredential.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Credentials.PasswordCredential.CreatePasswordCredential(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_factorymethod
    def CreatePasswordCredential(cls: win32more.Windows.Security.Credentials.ICredentialFactory, resource: hstr, userName: hstr, password: hstr) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_Resource(self: win32more.Windows.Security.Credentials.IPasswordCredential) -> hstr: ...
    @winrt_mixinmethod
    def put_Resource(self: win32more.Windows.Security.Credentials.IPasswordCredential, resource: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.Security.Credentials.IPasswordCredential) -> hstr: ...
    @winrt_mixinmethod
    def put_UserName(self: win32more.Windows.Security.Credentials.IPasswordCredential, userName: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: win32more.Windows.Security.Credentials.IPasswordCredential) -> hstr: ...
    @winrt_mixinmethod
    def put_Password(self: win32more.Windows.Security.Credentials.IPasswordCredential, password: hstr) -> Void: ...
    @winrt_mixinmethod
    def RetrievePassword(self: win32more.Windows.Security.Credentials.IPasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Credentials.IPasswordCredential) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Password = property(get_Password, put_Password)
    Properties = property(get_Properties, None)
    Resource = property(get_Resource, put_Resource)
    UserName = property(get_UserName, put_UserName)
class PasswordCredentialPropertyStore(ComPtr):
    extends: IInspectable
    implements: Tuple[MappingProtocol[hstr, IInspectable]]
    default_interface: win32more.Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Security.Credentials.PasswordCredentialPropertyStore'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Credentials.PasswordCredentialPropertyStore.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Credentials.PasswordCredentialPropertyStore: ...
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[hstr, IInspectable], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[hstr, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[hstr, IInspectable], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable], key: hstr) -> IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable], key: hstr) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[hstr, IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable], key: hstr, value: IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable], key: hstr) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[hstr, IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[hstr, IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[hstr, IInspectable]]: ...
    Size = property(get_Size, None)
    MapChanged = event(add_MapChanged, remove_MapChanged)
class PasswordVault(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IPasswordVault
    _classid_ = 'Windows.Security.Credentials.PasswordVault'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Credentials.PasswordVault.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Credentials.PasswordVault: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.Security.Credentials.IPasswordVault, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Security.Credentials.IPasswordVault, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def Retrieve(self: win32more.Windows.Security.Credentials.IPasswordVault, resource: hstr, userName: hstr) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def FindAllByResource(self: win32more.Windows.Security.Credentials.IPasswordVault, resource: hstr) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_mixinmethod
    def FindAllByUserName(self: win32more.Windows.Security.Credentials.IPasswordVault, userName: hstr) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.PasswordCredential]: ...
    @winrt_mixinmethod
    def RetrieveAll(self: win32more.Windows.Security.Credentials.IPasswordVault) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.PasswordCredential]: ...
class WebAccount(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IWebAccount
    _classid_ = 'Windows.Security.Credentials.WebAccount'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Credentials.WebAccount.CreateWebAccount(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWebAccount(cls: win32more.Windows.Security.Credentials.IWebAccountFactory, webAccountProvider: win32more.Windows.Security.Credentials.WebAccountProvider, userName: hstr, state: win32more.Windows.Security.Credentials.WebAccountState) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: win32more.Windows.Security.Credentials.IWebAccount) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.Security.Credentials.IWebAccount) -> hstr: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Security.Credentials.IWebAccount) -> win32more.Windows.Security.Credentials.WebAccountState: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Security.Credentials.IWebAccount2) -> hstr: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Credentials.IWebAccount2) -> win32more.Windows.Foundation.Collections.IMapView[hstr, hstr]: ...
    @winrt_mixinmethod
    def GetPictureAsync(self: win32more.Windows.Security.Credentials.IWebAccount2, desizedSize: win32more.Windows.Security.Credentials.WebAccountPictureSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def SignOutAsync(self: win32more.Windows.Security.Credentials.IWebAccount2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SignOutWithClientIdAsync(self: win32more.Windows.Security.Credentials.IWebAccount2, clientId: hstr) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    State = property(get_State, None)
    UserName = property(get_UserName, None)
    WebAccountProvider = property(get_WebAccountProvider, None)
class WebAccountPictureSize(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.WebAccountPictureSize'
    Size64x64 = 64
    Size208x208 = 208
    Size424x424 = 424
    Size1080x1080 = 1080
class WebAccountProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Credentials.IWebAccountProvider
    _classid_ = 'Windows.Security.Credentials.WebAccountProvider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Credentials.WebAccountProvider.CreateWebAccountProvider(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWebAccountProvider(cls: win32more.Windows.Security.Credentials.IWebAccountProviderFactory, id: hstr, displayName: hstr, iconUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Security.Credentials.IWebAccountProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Security.Credentials.IWebAccountProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_IconUri(self: win32more.Windows.Security.Credentials.IWebAccountProvider) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DisplayPurpose(self: win32more.Windows.Security.Credentials.IWebAccountProvider2) -> hstr: ...
    @winrt_mixinmethod
    def get_Authority(self: win32more.Windows.Security.Credentials.IWebAccountProvider2) -> hstr: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Security.Credentials.IWebAccountProvider3) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_IsSystemProvider(self: win32more.Windows.Security.Credentials.IWebAccountProvider4) -> Boolean: ...
    Authority = property(get_Authority, None)
    DisplayName = property(get_DisplayName, None)
    DisplayPurpose = property(get_DisplayPurpose, None)
    IconUri = property(get_IconUri, None)
    Id = property(get_Id, None)
    IsSystemProvider = property(get_IsSystemProvider, None)
    User = property(get_User, None)
class WebAccountState(Enum, Int32):
    _name_ = 'Windows.Security.Credentials.WebAccountState'
    None_ = 0
    Connected = 1
    Error = 2


make_ready(__name__)
