from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Security.Cryptography.Core
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class _AsymmetricAlgorithmNames_Meta_(ComPtr.__class__):
    pass
class AsymmetricAlgorithmNames(ComPtr, metaclass=_AsymmetricAlgorithmNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.AsymmetricAlgorithmNames'
    @winrt_classmethod
    def get_EcdsaSha256(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaSha384(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaSha512(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaPkcs1(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha1(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha256(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha384(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha512(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaP256Sha256(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaP384Sha384(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaP521Sha512(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DsaSha1(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DsaSha256(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha1(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha256(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha384(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha512(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha1(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha256(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha384(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha512(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    _AsymmetricAlgorithmNames_Meta_.DsaSha1 = property(get_DsaSha1, None)
    _AsymmetricAlgorithmNames_Meta_.DsaSha256 = property(get_DsaSha256, None)
    _AsymmetricAlgorithmNames_Meta_.EcdsaP256Sha256 = property(get_EcdsaP256Sha256, None)
    _AsymmetricAlgorithmNames_Meta_.EcdsaP384Sha384 = property(get_EcdsaP384Sha384, None)
    _AsymmetricAlgorithmNames_Meta_.EcdsaP521Sha512 = property(get_EcdsaP521Sha512, None)
    _AsymmetricAlgorithmNames_Meta_.EcdsaSha256 = property(get_EcdsaSha256, None)
    _AsymmetricAlgorithmNames_Meta_.EcdsaSha384 = property(get_EcdsaSha384, None)
    _AsymmetricAlgorithmNames_Meta_.EcdsaSha512 = property(get_EcdsaSha512, None)
    _AsymmetricAlgorithmNames_Meta_.RsaOaepSha1 = property(get_RsaOaepSha1, None)
    _AsymmetricAlgorithmNames_Meta_.RsaOaepSha256 = property(get_RsaOaepSha256, None)
    _AsymmetricAlgorithmNames_Meta_.RsaOaepSha384 = property(get_RsaOaepSha384, None)
    _AsymmetricAlgorithmNames_Meta_.RsaOaepSha512 = property(get_RsaOaepSha512, None)
    _AsymmetricAlgorithmNames_Meta_.RsaPkcs1 = property(get_RsaPkcs1, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPkcs1Sha1 = property(get_RsaSignPkcs1Sha1, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPkcs1Sha256 = property(get_RsaSignPkcs1Sha256, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPkcs1Sha384 = property(get_RsaSignPkcs1Sha384, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPkcs1Sha512 = property(get_RsaSignPkcs1Sha512, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPssSha1 = property(get_RsaSignPssSha1, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPssSha256 = property(get_RsaSignPssSha256, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPssSha384 = property(get_RsaSignPssSha384, None)
    _AsymmetricAlgorithmNames_Meta_.RsaSignPssSha512 = property(get_RsaSignPssSha512, None)
class AsymmetricKeyAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider
    _classid_ = 'Windows.Security.Cryptography.Core.AsymmetricKeyAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def CreateKeyPair(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keySize: UInt32) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportDefaultPrivateKeyBlob(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportKeyPairWithBlobType(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: win32more.Windows.Storage.Streams.IBuffer, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportDefaultPublicKeyBlob(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportPublicKeyWithBlobType(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: win32more.Windows.Storage.Streams.IBuffer, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def CreateKeyPairWithCurveName(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider2, curveName: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def CreateKeyPairWithCurveParameters(self: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider2, parameters: PassArray[Byte]) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: win32more.Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProviderStatics, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.AsymmetricKeyAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
class Capi1KdfTargetAlgorithm(Enum, Int32):
    NotAes = 0
    Aes = 1
class CryptographicEngine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.CryptographicEngine'
    @winrt_classmethod
    def SignHashedData(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def VerifySignatureWithHashInput(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, signature: win32more.Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_classmethod
    def DecryptAsync(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, iv: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def SignAsync(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def SignHashedDataAsync(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def Encrypt(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, iv: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def Decrypt(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, iv: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def EncryptAndAuthenticate(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, nonce: win32more.Windows.Storage.Streams.IBuffer, authenticatedData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.EncryptedAndAuthenticatedData: ...
    @winrt_classmethod
    def DecryptAndAuthenticate(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, nonce: win32more.Windows.Storage.Streams.IBuffer, authenticationTag: win32more.Windows.Storage.Streams.IBuffer, authenticatedData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def Sign(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def VerifySignature(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, signature: win32more.Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_classmethod
    def DeriveKeyMaterial(cls: win32more.Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, parameters: win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters, desiredKeySize: UInt32) -> win32more.Windows.Storage.Streams.IBuffer: ...
class CryptographicHash(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IHashComputation
    _classid_ = 'Windows.Security.Cryptography.Core.CryptographicHash'
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Security.Cryptography.Core.IHashComputation, data: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetValueAndReset(self: win32more.Windows.Security.Cryptography.Core.IHashComputation) -> win32more.Windows.Storage.Streams.IBuffer: ...
class CryptographicKey(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.ICryptographicKey
    _classid_ = 'Windows.Security.Cryptography.Core.CryptographicKey'
    @winrt_mixinmethod
    def get_KeySize(self: win32more.Windows.Security.Cryptography.Core.ICryptographicKey) -> UInt32: ...
    @winrt_mixinmethod
    def ExportDefaultPrivateKeyBlobType(self: win32more.Windows.Security.Cryptography.Core.ICryptographicKey) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def ExportPrivateKeyWithBlobType(self: win32more.Windows.Security.Cryptography.Core.ICryptographicKey, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def ExportDefaultPublicKeyBlobType(self: win32more.Windows.Security.Cryptography.Core.ICryptographicKey) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def ExportPublicKeyWithBlobType(self: win32more.Windows.Security.Cryptography.Core.ICryptographicKey, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Storage.Streams.IBuffer: ...
    KeySize = property(get_KeySize, None)
class CryptographicPadding(Enum, Int32):
    None_ = 0
    RsaOaep = 1
    RsaPkcs1V15 = 2
    RsaPss = 3
class CryptographicPrivateKeyBlobType(Enum, Int32):
    Pkcs8RawPrivateKeyInfo = 0
    Pkcs1RsaPrivateKey = 1
    BCryptPrivateKey = 2
    Capi1PrivateKey = 3
    BCryptEccFullPrivateKey = 4
class CryptographicPublicKeyBlobType(Enum, Int32):
    X509SubjectPublicKeyInfo = 0
    Pkcs1RsaPublicKey = 1
    BCryptPublicKey = 2
    Capi1PublicKey = 3
    BCryptEccFullPublicKey = 4
class _EccCurveNames_Meta_(ComPtr.__class__):
    pass
class EccCurveNames(ComPtr, metaclass=_EccCurveNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.EccCurveNames'
    @winrt_classmethod
    def get_BrainpoolP160r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP160t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP192r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP192t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP224r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP224t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP256r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP256t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP320r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP320t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP384r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP384t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP512r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP512t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Curve25519(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ec192wapi(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP192(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP224(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP256(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP384(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP521(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NumsP256t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NumsP384t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NumsP512t1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP160k1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP160r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP160r2(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP192k1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP192r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP224k1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP224r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP256k1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP256r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP384r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP521r1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wtls7(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wtls9(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wtls12(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P192v1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P192v2(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P192v3(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P239v1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P239v2(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P239v3(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P256v1(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AllEccCurveNames(cls: win32more.Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    _EccCurveNames_Meta_.AllEccCurveNames = property(get_AllEccCurveNames, None)
    _EccCurveNames_Meta_.BrainpoolP160r1 = property(get_BrainpoolP160r1, None)
    _EccCurveNames_Meta_.BrainpoolP160t1 = property(get_BrainpoolP160t1, None)
    _EccCurveNames_Meta_.BrainpoolP192r1 = property(get_BrainpoolP192r1, None)
    _EccCurveNames_Meta_.BrainpoolP192t1 = property(get_BrainpoolP192t1, None)
    _EccCurveNames_Meta_.BrainpoolP224r1 = property(get_BrainpoolP224r1, None)
    _EccCurveNames_Meta_.BrainpoolP224t1 = property(get_BrainpoolP224t1, None)
    _EccCurveNames_Meta_.BrainpoolP256r1 = property(get_BrainpoolP256r1, None)
    _EccCurveNames_Meta_.BrainpoolP256t1 = property(get_BrainpoolP256t1, None)
    _EccCurveNames_Meta_.BrainpoolP320r1 = property(get_BrainpoolP320r1, None)
    _EccCurveNames_Meta_.BrainpoolP320t1 = property(get_BrainpoolP320t1, None)
    _EccCurveNames_Meta_.BrainpoolP384r1 = property(get_BrainpoolP384r1, None)
    _EccCurveNames_Meta_.BrainpoolP384t1 = property(get_BrainpoolP384t1, None)
    _EccCurveNames_Meta_.BrainpoolP512r1 = property(get_BrainpoolP512r1, None)
    _EccCurveNames_Meta_.BrainpoolP512t1 = property(get_BrainpoolP512t1, None)
    _EccCurveNames_Meta_.Curve25519 = property(get_Curve25519, None)
    _EccCurveNames_Meta_.Ec192wapi = property(get_Ec192wapi, None)
    _EccCurveNames_Meta_.NistP192 = property(get_NistP192, None)
    _EccCurveNames_Meta_.NistP224 = property(get_NistP224, None)
    _EccCurveNames_Meta_.NistP256 = property(get_NistP256, None)
    _EccCurveNames_Meta_.NistP384 = property(get_NistP384, None)
    _EccCurveNames_Meta_.NistP521 = property(get_NistP521, None)
    _EccCurveNames_Meta_.NumsP256t1 = property(get_NumsP256t1, None)
    _EccCurveNames_Meta_.NumsP384t1 = property(get_NumsP384t1, None)
    _EccCurveNames_Meta_.NumsP512t1 = property(get_NumsP512t1, None)
    _EccCurveNames_Meta_.SecP160k1 = property(get_SecP160k1, None)
    _EccCurveNames_Meta_.SecP160r1 = property(get_SecP160r1, None)
    _EccCurveNames_Meta_.SecP160r2 = property(get_SecP160r2, None)
    _EccCurveNames_Meta_.SecP192k1 = property(get_SecP192k1, None)
    _EccCurveNames_Meta_.SecP192r1 = property(get_SecP192r1, None)
    _EccCurveNames_Meta_.SecP224k1 = property(get_SecP224k1, None)
    _EccCurveNames_Meta_.SecP224r1 = property(get_SecP224r1, None)
    _EccCurveNames_Meta_.SecP256k1 = property(get_SecP256k1, None)
    _EccCurveNames_Meta_.SecP256r1 = property(get_SecP256r1, None)
    _EccCurveNames_Meta_.SecP384r1 = property(get_SecP384r1, None)
    _EccCurveNames_Meta_.SecP521r1 = property(get_SecP521r1, None)
    _EccCurveNames_Meta_.Wtls12 = property(get_Wtls12, None)
    _EccCurveNames_Meta_.Wtls7 = property(get_Wtls7, None)
    _EccCurveNames_Meta_.Wtls9 = property(get_Wtls9, None)
    _EccCurveNames_Meta_.X962P192v1 = property(get_X962P192v1, None)
    _EccCurveNames_Meta_.X962P192v2 = property(get_X962P192v2, None)
    _EccCurveNames_Meta_.X962P192v3 = property(get_X962P192v3, None)
    _EccCurveNames_Meta_.X962P239v1 = property(get_X962P239v1, None)
    _EccCurveNames_Meta_.X962P239v2 = property(get_X962P239v2, None)
    _EccCurveNames_Meta_.X962P239v3 = property(get_X962P239v3, None)
    _EccCurveNames_Meta_.X962P256v1 = property(get_X962P256v1, None)
class EncryptedAndAuthenticatedData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IEncryptedAndAuthenticatedData
    _classid_ = 'Windows.Security.Cryptography.Core.EncryptedAndAuthenticatedData'
    @winrt_mixinmethod
    def get_EncryptedData(self: win32more.Windows.Security.Cryptography.Core.IEncryptedAndAuthenticatedData) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AuthenticationTag(self: win32more.Windows.Security.Cryptography.Core.IEncryptedAndAuthenticatedData) -> win32more.Windows.Storage.Streams.IBuffer: ...
    AuthenticationTag = property(get_AuthenticationTag, None)
    EncryptedData = property(get_EncryptedData, None)
class _HashAlgorithmNames_Meta_(ComPtr.__class__):
    pass
class HashAlgorithmNames(ComPtr, metaclass=_HashAlgorithmNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.HashAlgorithmNames'
    @winrt_classmethod
    def get_Md5(cls: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha1(cls: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha256(cls: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha384(cls: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha512(cls: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    _HashAlgorithmNames_Meta_.Md5 = property(get_Md5, None)
    _HashAlgorithmNames_Meta_.Sha1 = property(get_Sha1, None)
    _HashAlgorithmNames_Meta_.Sha256 = property(get_Sha256, None)
    _HashAlgorithmNames_Meta_.Sha384 = property(get_Sha384, None)
    _HashAlgorithmNames_Meta_.Sha512 = property(get_Sha512, None)
class HashAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmProvider
    _classid_ = 'Windows.Security.Cryptography.Core.HashAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HashLength(self: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmProvider) -> UInt32: ...
    @winrt_mixinmethod
    def HashData(self: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmProvider, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def CreateHash(self: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmProvider) -> win32more.Windows.Security.Cryptography.Core.CryptographicHash: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: win32more.Windows.Security.Cryptography.Core.IHashAlgorithmProviderStatics, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.HashAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
    HashLength = property(get_HashLength, None)
class IAsymmetricAlgorithmNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics'
    _iid_ = Guid('{caf6fce4-67c0-46aa-84f9-752e77449f9b}')
    @winrt_commethod(6)
    def get_RsaPkcs1(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RsaOaepSha1(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RsaOaepSha256(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_RsaOaepSha384(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_RsaOaepSha512(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_EcdsaP256Sha256(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_EcdsaP384Sha384(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_EcdsaP521Sha512(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_DsaSha1(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_DsaSha256(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_RsaSignPkcs1Sha1(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_RsaSignPkcs1Sha256(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_RsaSignPkcs1Sha384(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_RsaSignPkcs1Sha512(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_RsaSignPssSha1(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_RsaSignPssSha256(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_RsaSignPssSha384(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_RsaSignPssSha512(self) -> WinRT_String: ...
    DsaSha1 = property(get_DsaSha1, None)
    DsaSha256 = property(get_DsaSha256, None)
    EcdsaP256Sha256 = property(get_EcdsaP256Sha256, None)
    EcdsaP384Sha384 = property(get_EcdsaP384Sha384, None)
    EcdsaP521Sha512 = property(get_EcdsaP521Sha512, None)
    RsaOaepSha1 = property(get_RsaOaepSha1, None)
    RsaOaepSha256 = property(get_RsaOaepSha256, None)
    RsaOaepSha384 = property(get_RsaOaepSha384, None)
    RsaOaepSha512 = property(get_RsaOaepSha512, None)
    RsaPkcs1 = property(get_RsaPkcs1, None)
    RsaSignPkcs1Sha1 = property(get_RsaSignPkcs1Sha1, None)
    RsaSignPkcs1Sha256 = property(get_RsaSignPkcs1Sha256, None)
    RsaSignPkcs1Sha384 = property(get_RsaSignPkcs1Sha384, None)
    RsaSignPkcs1Sha512 = property(get_RsaSignPkcs1Sha512, None)
    RsaSignPssSha1 = property(get_RsaSignPssSha1, None)
    RsaSignPssSha256 = property(get_RsaSignPssSha256, None)
    RsaSignPssSha384 = property(get_RsaSignPssSha384, None)
    RsaSignPssSha512 = property(get_RsaSignPssSha512, None)
class IAsymmetricAlgorithmNamesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2'
    _iid_ = Guid('{f141c0d6-4bff-4f23-ba66-6045b137d5df}')
    @winrt_commethod(6)
    def get_EcdsaSha256(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EcdsaSha384(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EcdsaSha512(self) -> WinRT_String: ...
    EcdsaSha256 = property(get_EcdsaSha256, None)
    EcdsaSha384 = property(get_EcdsaSha384, None)
    EcdsaSha512 = property(get_EcdsaSha512, None)
class IAsymmetricKeyAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider'
    _iid_ = Guid('{e8d2ff37-6259-4e88-b7e0-94191fde699e}')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateKeyPair(self, keySize: UInt32) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(8)
    def ImportDefaultPrivateKeyBlob(self, keyBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(9)
    def ImportKeyPairWithBlobType(self, keyBlob: win32more.Windows.Storage.Streams.IBuffer, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(10)
    def ImportDefaultPublicKeyBlob(self, keyBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(11)
    def ImportPublicKeyWithBlobType(self, keyBlob: win32more.Windows.Storage.Streams.IBuffer, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
class IAsymmetricKeyAlgorithmProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider2'
    _iid_ = Guid('{4e322a7e-7c4d-4997-ac4f-1b848b36306e}')
    @winrt_commethod(6)
    def CreateKeyPairWithCurveName(self, curveName: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(7)
    def CreateKeyPairWithCurveParameters(self, parameters: PassArray[Byte]) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
class IAsymmetricKeyAlgorithmProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProviderStatics'
    _iid_ = Guid('{425bde18-a7f3-47a6-a8d2-c48d6033a65c}')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.AsymmetricKeyAlgorithmProvider: ...
class ICryptographicEngineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.ICryptographicEngineStatics'
    _iid_ = Guid('{9fea0639-6ff7-4c85-a095-95eb31715eb9}')
    @winrt_commethod(6)
    def Encrypt(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, iv: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def Decrypt(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, iv: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def EncryptAndAuthenticate(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, nonce: win32more.Windows.Storage.Streams.IBuffer, authenticatedData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.EncryptedAndAuthenticatedData: ...
    @winrt_commethod(9)
    def DecryptAndAuthenticate(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, nonce: win32more.Windows.Storage.Streams.IBuffer, authenticationTag: win32more.Windows.Storage.Streams.IBuffer, authenticatedData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def Sign(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def VerifySignature(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, signature: win32more.Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_commethod(12)
    def DeriveKeyMaterial(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, parameters: win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters, desiredKeySize: UInt32) -> win32more.Windows.Storage.Streams.IBuffer: ...
class ICryptographicEngineStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.ICryptographicEngineStatics2'
    _iid_ = Guid('{675948fe-df9f-4191-92c7-6ce6f58420e0}')
    @winrt_commethod(6)
    def SignHashedData(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def VerifySignatureWithHashInput(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, signature: win32more.Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_commethod(8)
    def DecryptAsync(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer, iv: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def SignAsync(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(10)
    def SignHashedDataAsync(self, key: win32more.Windows.Security.Cryptography.Core.CryptographicKey, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
class ICryptographicKey(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.ICryptographicKey'
    _iid_ = Guid('{ed2a3b70-8e7b-4009-8401-ffd1a62eeb27}')
    @winrt_commethod(6)
    def get_KeySize(self) -> UInt32: ...
    @winrt_commethod(7)
    def ExportDefaultPrivateKeyBlobType(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def ExportPrivateKeyWithBlobType(self, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def ExportDefaultPublicKeyBlobType(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def ExportPublicKeyWithBlobType(self, BlobType: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Storage.Streams.IBuffer: ...
    KeySize = property(get_KeySize, None)
class IEccCurveNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IEccCurveNamesStatics'
    _iid_ = Guid('{b3ff930c-aeeb-409e-b7d4-9b95295aaecf}')
    @winrt_commethod(6)
    def get_BrainpoolP160r1(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BrainpoolP160t1(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_BrainpoolP192r1(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_BrainpoolP192t1(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_BrainpoolP224r1(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_BrainpoolP224t1(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_BrainpoolP256r1(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_BrainpoolP256t1(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_BrainpoolP320r1(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_BrainpoolP320t1(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_BrainpoolP384r1(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_BrainpoolP384t1(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_BrainpoolP512r1(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_BrainpoolP512t1(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Curve25519(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Ec192wapi(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_NistP192(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_NistP224(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_NistP256(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_NistP384(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_NistP521(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_NumsP256t1(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def get_NumsP384t1(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def get_NumsP512t1(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def get_SecP160k1(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def get_SecP160r1(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def get_SecP160r2(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def get_SecP192k1(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_SecP192r1(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def get_SecP224k1(self) -> WinRT_String: ...
    @winrt_commethod(36)
    def get_SecP224r1(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_SecP256k1(self) -> WinRT_String: ...
    @winrt_commethod(38)
    def get_SecP256r1(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def get_SecP384r1(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def get_SecP521r1(self) -> WinRT_String: ...
    @winrt_commethod(41)
    def get_Wtls7(self) -> WinRT_String: ...
    @winrt_commethod(42)
    def get_Wtls9(self) -> WinRT_String: ...
    @winrt_commethod(43)
    def get_Wtls12(self) -> WinRT_String: ...
    @winrt_commethod(44)
    def get_X962P192v1(self) -> WinRT_String: ...
    @winrt_commethod(45)
    def get_X962P192v2(self) -> WinRT_String: ...
    @winrt_commethod(46)
    def get_X962P192v3(self) -> WinRT_String: ...
    @winrt_commethod(47)
    def get_X962P239v1(self) -> WinRT_String: ...
    @winrt_commethod(48)
    def get_X962P239v2(self) -> WinRT_String: ...
    @winrt_commethod(49)
    def get_X962P239v3(self) -> WinRT_String: ...
    @winrt_commethod(50)
    def get_X962P256v1(self) -> WinRT_String: ...
    @winrt_commethod(51)
    def get_AllEccCurveNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    AllEccCurveNames = property(get_AllEccCurveNames, None)
    BrainpoolP160r1 = property(get_BrainpoolP160r1, None)
    BrainpoolP160t1 = property(get_BrainpoolP160t1, None)
    BrainpoolP192r1 = property(get_BrainpoolP192r1, None)
    BrainpoolP192t1 = property(get_BrainpoolP192t1, None)
    BrainpoolP224r1 = property(get_BrainpoolP224r1, None)
    BrainpoolP224t1 = property(get_BrainpoolP224t1, None)
    BrainpoolP256r1 = property(get_BrainpoolP256r1, None)
    BrainpoolP256t1 = property(get_BrainpoolP256t1, None)
    BrainpoolP320r1 = property(get_BrainpoolP320r1, None)
    BrainpoolP320t1 = property(get_BrainpoolP320t1, None)
    BrainpoolP384r1 = property(get_BrainpoolP384r1, None)
    BrainpoolP384t1 = property(get_BrainpoolP384t1, None)
    BrainpoolP512r1 = property(get_BrainpoolP512r1, None)
    BrainpoolP512t1 = property(get_BrainpoolP512t1, None)
    Curve25519 = property(get_Curve25519, None)
    Ec192wapi = property(get_Ec192wapi, None)
    NistP192 = property(get_NistP192, None)
    NistP224 = property(get_NistP224, None)
    NistP256 = property(get_NistP256, None)
    NistP384 = property(get_NistP384, None)
    NistP521 = property(get_NistP521, None)
    NumsP256t1 = property(get_NumsP256t1, None)
    NumsP384t1 = property(get_NumsP384t1, None)
    NumsP512t1 = property(get_NumsP512t1, None)
    SecP160k1 = property(get_SecP160k1, None)
    SecP160r1 = property(get_SecP160r1, None)
    SecP160r2 = property(get_SecP160r2, None)
    SecP192k1 = property(get_SecP192k1, None)
    SecP192r1 = property(get_SecP192r1, None)
    SecP224k1 = property(get_SecP224k1, None)
    SecP224r1 = property(get_SecP224r1, None)
    SecP256k1 = property(get_SecP256k1, None)
    SecP256r1 = property(get_SecP256r1, None)
    SecP384r1 = property(get_SecP384r1, None)
    SecP521r1 = property(get_SecP521r1, None)
    Wtls12 = property(get_Wtls12, None)
    Wtls7 = property(get_Wtls7, None)
    Wtls9 = property(get_Wtls9, None)
    X962P192v1 = property(get_X962P192v1, None)
    X962P192v2 = property(get_X962P192v2, None)
    X962P192v3 = property(get_X962P192v3, None)
    X962P239v1 = property(get_X962P239v1, None)
    X962P239v2 = property(get_X962P239v2, None)
    X962P239v3 = property(get_X962P239v3, None)
    X962P256v1 = property(get_X962P256v1, None)
class IEncryptedAndAuthenticatedData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IEncryptedAndAuthenticatedData'
    _iid_ = Guid('{6fa42fe7-1ecb-4b00-bea5-60b83f862f17}')
    @winrt_commethod(6)
    def get_EncryptedData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_AuthenticationTag(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    AuthenticationTag = property(get_AuthenticationTag, None)
    EncryptedData = property(get_EncryptedData, None)
class IHashAlgorithmNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics'
    _iid_ = Guid('{6b5e0516-de96-4f0a-8d57-dcc9dae36c76}')
    @winrt_commethod(6)
    def get_Md5(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Sha1(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Sha256(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Sha384(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Sha512(self) -> WinRT_String: ...
    Md5 = property(get_Md5, None)
    Sha1 = property(get_Sha1, None)
    Sha256 = property(get_Sha256, None)
    Sha384 = property(get_Sha384, None)
    Sha512 = property(get_Sha512, None)
class IHashAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IHashAlgorithmProvider'
    _iid_ = Guid('{be9b3080-b2c3-422b-bce1-ec90efb5d7b5}')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HashLength(self) -> UInt32: ...
    @winrt_commethod(8)
    def HashData(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def CreateHash(self) -> win32more.Windows.Security.Cryptography.Core.CryptographicHash: ...
    AlgorithmName = property(get_AlgorithmName, None)
    HashLength = property(get_HashLength, None)
class IHashAlgorithmProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IHashAlgorithmProviderStatics'
    _iid_ = Guid('{9fac9741-5cc4-4336-ae38-6212b75a915a}')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.HashAlgorithmProvider: ...
class IHashComputation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IHashComputation'
    _iid_ = Guid('{5904d1b6-ad31-4603-a3a4-b1bda98e2562}')
    @winrt_commethod(6)
    def Append(self, data: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def GetValueAndReset(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
class IKeyDerivationAlgorithmNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics'
    _iid_ = Guid('{7b6e363e-94d2-4739-a57b-022e0c3a402a}')
    @winrt_commethod(6)
    def get_Pbkdf2Md5(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Pbkdf2Sha1(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Pbkdf2Sha256(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Pbkdf2Sha384(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Pbkdf2Sha512(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Sp800108CtrHmacMd5(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Sp800108CtrHmacSha1(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Sp800108CtrHmacSha256(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Sp800108CtrHmacSha384(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Sp800108CtrHmacSha512(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Sp80056aConcatMd5(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_Sp80056aConcatSha1(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Sp80056aConcatSha256(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Sp80056aConcatSha384(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Sp80056aConcatSha512(self) -> WinRT_String: ...
    Pbkdf2Md5 = property(get_Pbkdf2Md5, None)
    Pbkdf2Sha1 = property(get_Pbkdf2Sha1, None)
    Pbkdf2Sha256 = property(get_Pbkdf2Sha256, None)
    Pbkdf2Sha384 = property(get_Pbkdf2Sha384, None)
    Pbkdf2Sha512 = property(get_Pbkdf2Sha512, None)
    Sp800108CtrHmacMd5 = property(get_Sp800108CtrHmacMd5, None)
    Sp800108CtrHmacSha1 = property(get_Sp800108CtrHmacSha1, None)
    Sp800108CtrHmacSha256 = property(get_Sp800108CtrHmacSha256, None)
    Sp800108CtrHmacSha384 = property(get_Sp800108CtrHmacSha384, None)
    Sp800108CtrHmacSha512 = property(get_Sp800108CtrHmacSha512, None)
    Sp80056aConcatMd5 = property(get_Sp80056aConcatMd5, None)
    Sp80056aConcatSha1 = property(get_Sp80056aConcatSha1, None)
    Sp80056aConcatSha256 = property(get_Sp80056aConcatSha256, None)
    Sp80056aConcatSha384 = property(get_Sp80056aConcatSha384, None)
    Sp80056aConcatSha512 = property(get_Sp80056aConcatSha512, None)
class IKeyDerivationAlgorithmNamesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2'
    _iid_ = Guid('{57953fab-6044-466f-97f4-337b7808384d}')
    @winrt_commethod(6)
    def get_CapiKdfMd5(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CapiKdfSha1(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_CapiKdfSha256(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CapiKdfSha384(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_CapiKdfSha512(self) -> WinRT_String: ...
    CapiKdfMd5 = property(get_CapiKdfMd5, None)
    CapiKdfSha1 = property(get_CapiKdfSha1, None)
    CapiKdfSha256 = property(get_CapiKdfSha256, None)
    CapiKdfSha384 = property(get_CapiKdfSha384, None)
    CapiKdfSha512 = property(get_CapiKdfSha512, None)
class IKeyDerivationAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProvider'
    _iid_ = Guid('{e1fba83b-4671-43b7-9158-763aaa98b6bf}')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateKey(self, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
class IKeyDerivationAlgorithmProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProviderStatics'
    _iid_ = Guid('{0a22097a-0a1c-443b-9418-b9498aeb1603}')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationAlgorithmProvider: ...
class IKeyDerivationParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationParameters'
    _iid_ = Guid('{7bf05967-047b-4a8c-964a-469ffd5522e2}')
    @winrt_commethod(6)
    def get_KdfGenericBinary(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_KdfGenericBinary(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_IterationCount(self) -> UInt32: ...
    IterationCount = property(get_IterationCount, None)
    KdfGenericBinary = property(get_KdfGenericBinary, put_KdfGenericBinary)
class IKeyDerivationParameters2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationParameters2'
    _iid_ = Guid('{cd4166d1-417e-4f4c-b666-c0d879f3f8e0}')
    @winrt_commethod(6)
    def get_Capi1KdfTargetAlgorithm(self) -> win32more.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm: ...
    @winrt_commethod(7)
    def put_Capi1KdfTargetAlgorithm(self, value: win32more.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> Void: ...
    Capi1KdfTargetAlgorithm = property(get_Capi1KdfTargetAlgorithm, put_Capi1KdfTargetAlgorithm)
class IKeyDerivationParametersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics'
    _iid_ = Guid('{ea961fbe-f37f-4146-9dfe-a456f1735f4b}')
    @winrt_commethod(6)
    def BuildForPbkdf2(self, pbkdf2Salt: win32more.Windows.Storage.Streams.IBuffer, iterationCount: UInt32) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_commethod(7)
    def BuildForSP800108(self, label: win32more.Windows.Storage.Streams.IBuffer, context: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_commethod(8)
    def BuildForSP80056a(self, algorithmId: win32more.Windows.Storage.Streams.IBuffer, partyUInfo: win32more.Windows.Storage.Streams.IBuffer, partyVInfo: win32more.Windows.Storage.Streams.IBuffer, suppPubInfo: win32more.Windows.Storage.Streams.IBuffer, suppPrivInfo: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
class IKeyDerivationParametersStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics2'
    _iid_ = Guid('{a5783dd5-58e3-4efb-b283-a1653126e1be}')
    @winrt_commethod(6)
    def BuildForCapi1Kdf(self, capi1KdfTargetAlgorithm: win32more.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
class IMacAlgorithmNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics'
    _iid_ = Guid('{41412678-fb1e-43a4-895e-a9026e4390a3}')
    @winrt_commethod(6)
    def get_HmacMd5(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HmacSha1(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_HmacSha256(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_HmacSha384(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_HmacSha512(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AesCmac(self) -> WinRT_String: ...
    AesCmac = property(get_AesCmac, None)
    HmacMd5 = property(get_HmacMd5, None)
    HmacSha1 = property(get_HmacSha1, None)
    HmacSha256 = property(get_HmacSha256, None)
    HmacSha384 = property(get_HmacSha384, None)
    HmacSha512 = property(get_HmacSha512, None)
class IMacAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IMacAlgorithmProvider'
    _iid_ = Guid('{4a3fc5c3-1cbd-41ce-a092-aa0bc5d2d2f5}')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MacLength(self) -> UInt32: ...
    @winrt_commethod(8)
    def CreateKey(self, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
    MacLength = property(get_MacLength, None)
class IMacAlgorithmProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IMacAlgorithmProvider2'
    _iid_ = Guid('{6da32a15-d931-42ed-8e7e-c301caee119c}')
    @winrt_commethod(6)
    def CreateHash(self, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicHash: ...
class IMacAlgorithmProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IMacAlgorithmProviderStatics'
    _iid_ = Guid('{c9bdc147-cc77-4df0-9e4e-b921e080644c}')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.MacAlgorithmProvider: ...
class IPersistedKeyProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.IPersistedKeyProviderStatics'
    _iid_ = Guid('{77274814-d9d4-4cf5-b668-e0457df30894}')
    @winrt_commethod(6)
    def OpenKeyPairFromCertificateAsync(self, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: win32more.Windows.Security.Cryptography.Core.CryptographicPadding) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Core.CryptographicKey]: ...
    @winrt_commethod(7)
    def OpenPublicKeyFromCertificate(self, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: win32more.Windows.Security.Cryptography.Core.CryptographicPadding) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
class ISymmetricAlgorithmNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics'
    _iid_ = Guid('{6870727b-c996-4eae-84d7-79b2aeb73b9c}')
    @winrt_commethod(6)
    def get_DesCbc(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DesEcb(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_TripleDesCbc(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TripleDesEcb(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Rc2Cbc(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Rc2Ecb(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_AesCbc(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_AesEcb(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_AesGcm(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_AesCcm(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_AesCbcPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_AesEcbPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_DesCbcPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_DesEcbPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_TripleDesCbcPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_TripleDesEcbPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_Rc2CbcPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_Rc2EcbPkcs7(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_Rc4(self) -> WinRT_String: ...
    AesCbc = property(get_AesCbc, None)
    AesCbcPkcs7 = property(get_AesCbcPkcs7, None)
    AesCcm = property(get_AesCcm, None)
    AesEcb = property(get_AesEcb, None)
    AesEcbPkcs7 = property(get_AesEcbPkcs7, None)
    AesGcm = property(get_AesGcm, None)
    DesCbc = property(get_DesCbc, None)
    DesCbcPkcs7 = property(get_DesCbcPkcs7, None)
    DesEcb = property(get_DesEcb, None)
    DesEcbPkcs7 = property(get_DesEcbPkcs7, None)
    Rc2Cbc = property(get_Rc2Cbc, None)
    Rc2CbcPkcs7 = property(get_Rc2CbcPkcs7, None)
    Rc2Ecb = property(get_Rc2Ecb, None)
    Rc2EcbPkcs7 = property(get_Rc2EcbPkcs7, None)
    Rc4 = property(get_Rc4, None)
    TripleDesCbc = property(get_TripleDesCbc, None)
    TripleDesCbcPkcs7 = property(get_TripleDesCbcPkcs7, None)
    TripleDesEcb = property(get_TripleDesEcb, None)
    TripleDesEcbPkcs7 = property(get_TripleDesEcbPkcs7, None)
class ISymmetricKeyAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider'
    _iid_ = Guid('{3d7e4a33-3bd0-4902-8ac8-470d50d21376}')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BlockLength(self) -> UInt32: ...
    @winrt_commethod(8)
    def CreateSymmetricKey(self, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
    BlockLength = property(get_BlockLength, None)
class ISymmetricKeyAlgorithmProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProviderStatics'
    _iid_ = Guid('{8d3b2326-1f37-491f-b60e-f5431b26b483}')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.SymmetricKeyAlgorithmProvider: ...
class _KeyDerivationAlgorithmNames_Meta_(ComPtr.__class__):
    pass
class KeyDerivationAlgorithmNames(ComPtr, metaclass=_KeyDerivationAlgorithmNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.KeyDerivationAlgorithmNames'
    @winrt_classmethod
    def get_CapiKdfMd5(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha1(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha256(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha384(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha512(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Md5(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha1(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha256(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha384(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha512(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacMd5(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha1(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha256(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha384(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha512(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatMd5(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha1(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha256(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha384(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha512(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    _KeyDerivationAlgorithmNames_Meta_.CapiKdfMd5 = property(get_CapiKdfMd5, None)
    _KeyDerivationAlgorithmNames_Meta_.CapiKdfSha1 = property(get_CapiKdfSha1, None)
    _KeyDerivationAlgorithmNames_Meta_.CapiKdfSha256 = property(get_CapiKdfSha256, None)
    _KeyDerivationAlgorithmNames_Meta_.CapiKdfSha384 = property(get_CapiKdfSha384, None)
    _KeyDerivationAlgorithmNames_Meta_.CapiKdfSha512 = property(get_CapiKdfSha512, None)
    _KeyDerivationAlgorithmNames_Meta_.Pbkdf2Md5 = property(get_Pbkdf2Md5, None)
    _KeyDerivationAlgorithmNames_Meta_.Pbkdf2Sha1 = property(get_Pbkdf2Sha1, None)
    _KeyDerivationAlgorithmNames_Meta_.Pbkdf2Sha256 = property(get_Pbkdf2Sha256, None)
    _KeyDerivationAlgorithmNames_Meta_.Pbkdf2Sha384 = property(get_Pbkdf2Sha384, None)
    _KeyDerivationAlgorithmNames_Meta_.Pbkdf2Sha512 = property(get_Pbkdf2Sha512, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp800108CtrHmacMd5 = property(get_Sp800108CtrHmacMd5, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp800108CtrHmacSha1 = property(get_Sp800108CtrHmacSha1, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp800108CtrHmacSha256 = property(get_Sp800108CtrHmacSha256, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp800108CtrHmacSha384 = property(get_Sp800108CtrHmacSha384, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp800108CtrHmacSha512 = property(get_Sp800108CtrHmacSha512, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp80056aConcatMd5 = property(get_Sp80056aConcatMd5, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp80056aConcatSha1 = property(get_Sp80056aConcatSha1, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp80056aConcatSha256 = property(get_Sp80056aConcatSha256, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp80056aConcatSha384 = property(get_Sp80056aConcatSha384, None)
    _KeyDerivationAlgorithmNames_Meta_.Sp80056aConcatSha512 = property(get_Sp80056aConcatSha512, None)
class KeyDerivationAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProvider
    _classid_ = 'Windows.Security.Cryptography.Core.KeyDerivationAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def CreateKey(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProvider, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProviderStatics, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
class KeyDerivationParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParameters
    _classid_ = 'Windows.Security.Cryptography.Core.KeyDerivationParameters'
    @winrt_mixinmethod
    def get_KdfGenericBinary(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParameters) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_KdfGenericBinary(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParameters, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_IterationCount(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParameters) -> UInt32: ...
    @winrt_mixinmethod
    def get_Capi1KdfTargetAlgorithm(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParameters2) -> win32more.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm: ...
    @winrt_mixinmethod
    def put_Capi1KdfTargetAlgorithm(self: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParameters2, value: win32more.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> Void: ...
    @winrt_classmethod
    def BuildForCapi1Kdf(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics2, capi1KdfTargetAlgorithm: win32more.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_classmethod
    def BuildForPbkdf2(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics, pbkdf2Salt: win32more.Windows.Storage.Streams.IBuffer, iterationCount: UInt32) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_classmethod
    def BuildForSP800108(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics, label: win32more.Windows.Storage.Streams.IBuffer, context: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_classmethod
    def BuildForSP80056a(cls: win32more.Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics, algorithmId: win32more.Windows.Storage.Streams.IBuffer, partyUInfo: win32more.Windows.Storage.Streams.IBuffer, partyVInfo: win32more.Windows.Storage.Streams.IBuffer, suppPubInfo: win32more.Windows.Storage.Streams.IBuffer, suppPrivInfo: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    Capi1KdfTargetAlgorithm = property(get_Capi1KdfTargetAlgorithm, put_Capi1KdfTargetAlgorithm)
    IterationCount = property(get_IterationCount, None)
    KdfGenericBinary = property(get_KdfGenericBinary, put_KdfGenericBinary)
class _MacAlgorithmNames_Meta_(ComPtr.__class__):
    pass
class MacAlgorithmNames(ComPtr, metaclass=_MacAlgorithmNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.MacAlgorithmNames'
    @winrt_classmethod
    def get_HmacMd5(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha1(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha256(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha384(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha512(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCmac(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    _MacAlgorithmNames_Meta_.AesCmac = property(get_AesCmac, None)
    _MacAlgorithmNames_Meta_.HmacMd5 = property(get_HmacMd5, None)
    _MacAlgorithmNames_Meta_.HmacSha1 = property(get_HmacSha1, None)
    _MacAlgorithmNames_Meta_.HmacSha256 = property(get_HmacSha256, None)
    _MacAlgorithmNames_Meta_.HmacSha384 = property(get_HmacSha384, None)
    _MacAlgorithmNames_Meta_.HmacSha512 = property(get_HmacSha512, None)
class MacAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmProvider
    _classid_ = 'Windows.Security.Cryptography.Core.MacAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MacLength(self: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmProvider) -> UInt32: ...
    @winrt_mixinmethod
    def CreateKey(self: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmProvider, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def CreateHash(self: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmProvider2, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicHash: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: win32more.Windows.Security.Cryptography.Core.IMacAlgorithmProviderStatics, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.MacAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
    MacLength = property(get_MacLength, None)
class PersistedKeyProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.PersistedKeyProvider'
    @winrt_classmethod
    def OpenKeyPairFromCertificateAsync(cls: win32more.Windows.Security.Cryptography.Core.IPersistedKeyProviderStatics, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: win32more.Windows.Security.Cryptography.Core.CryptographicPadding) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Core.CryptographicKey]: ...
    @winrt_classmethod
    def OpenPublicKeyFromCertificate(cls: win32more.Windows.Security.Cryptography.Core.IPersistedKeyProviderStatics, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: win32more.Windows.Security.Cryptography.Core.CryptographicPadding) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
class _SymmetricAlgorithmNames_Meta_(ComPtr.__class__):
    pass
class SymmetricAlgorithmNames(ComPtr, metaclass=_SymmetricAlgorithmNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Core.SymmetricAlgorithmNames'
    @winrt_classmethod
    def get_DesCbc(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DesEcb(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesCbc(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesEcb(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2Cbc(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2Ecb(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCbc(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesEcb(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesGcm(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCcm(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCbcPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesEcbPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DesCbcPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DesEcbPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesCbcPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesEcbPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2CbcPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2EcbPkcs7(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc4(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    _SymmetricAlgorithmNames_Meta_.AesCbc = property(get_AesCbc, None)
    _SymmetricAlgorithmNames_Meta_.AesCbcPkcs7 = property(get_AesCbcPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.AesCcm = property(get_AesCcm, None)
    _SymmetricAlgorithmNames_Meta_.AesEcb = property(get_AesEcb, None)
    _SymmetricAlgorithmNames_Meta_.AesEcbPkcs7 = property(get_AesEcbPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.AesGcm = property(get_AesGcm, None)
    _SymmetricAlgorithmNames_Meta_.DesCbc = property(get_DesCbc, None)
    _SymmetricAlgorithmNames_Meta_.DesCbcPkcs7 = property(get_DesCbcPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.DesEcb = property(get_DesEcb, None)
    _SymmetricAlgorithmNames_Meta_.DesEcbPkcs7 = property(get_DesEcbPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.Rc2Cbc = property(get_Rc2Cbc, None)
    _SymmetricAlgorithmNames_Meta_.Rc2CbcPkcs7 = property(get_Rc2CbcPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.Rc2Ecb = property(get_Rc2Ecb, None)
    _SymmetricAlgorithmNames_Meta_.Rc2EcbPkcs7 = property(get_Rc2EcbPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.Rc4 = property(get_Rc4, None)
    _SymmetricAlgorithmNames_Meta_.TripleDesCbc = property(get_TripleDesCbc, None)
    _SymmetricAlgorithmNames_Meta_.TripleDesCbcPkcs7 = property(get_TripleDesCbcPkcs7, None)
    _SymmetricAlgorithmNames_Meta_.TripleDesEcb = property(get_TripleDesEcb, None)
    _SymmetricAlgorithmNames_Meta_.TripleDesEcbPkcs7 = property(get_TripleDesEcbPkcs7, None)
class SymmetricKeyAlgorithmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider
    _classid_ = 'Windows.Security.Cryptography.Core.SymmetricKeyAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: win32more.Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BlockLength(self: win32more.Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider) -> UInt32: ...
    @winrt_mixinmethod
    def CreateSymmetricKey(self: win32more.Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider, keyMaterial: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: win32more.Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProviderStatics, algorithm: WinRT_String) -> win32more.Windows.Security.Cryptography.Core.SymmetricKeyAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
    BlockLength = property(get_BlockLength, None)


make_ready(__name__)
