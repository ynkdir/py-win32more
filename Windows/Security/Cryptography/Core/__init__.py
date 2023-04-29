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
import Windows.Security.Cryptography.Certificates
import Windows.Security.Cryptography.Core
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
class AsymmetricAlgorithmNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.AsymmetricAlgorithmNames'
    @winrt_classmethod
    def get_EcdsaSha256(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaSha384(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaSha512(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaPkcs1(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha1(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha256(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha384(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaOaepSha512(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaP256Sha256(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaP384Sha384(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EcdsaP521Sha512(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DsaSha1(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DsaSha256(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha1(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha256(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha384(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPkcs1Sha512(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha1(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha256(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha384(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RsaSignPssSha512(cls: Windows.Security.Cryptography.Core.IAsymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    EcdsaSha256 = property(get_EcdsaSha256, None)
    EcdsaSha384 = property(get_EcdsaSha384, None)
    EcdsaSha512 = property(get_EcdsaSha512, None)
    RsaPkcs1 = property(get_RsaPkcs1, None)
    RsaOaepSha1 = property(get_RsaOaepSha1, None)
    RsaOaepSha256 = property(get_RsaOaepSha256, None)
    RsaOaepSha384 = property(get_RsaOaepSha384, None)
    RsaOaepSha512 = property(get_RsaOaepSha512, None)
    EcdsaP256Sha256 = property(get_EcdsaP256Sha256, None)
    EcdsaP384Sha384 = property(get_EcdsaP384Sha384, None)
    EcdsaP521Sha512 = property(get_EcdsaP521Sha512, None)
    DsaSha1 = property(get_DsaSha1, None)
    DsaSha256 = property(get_DsaSha256, None)
    RsaSignPkcs1Sha1 = property(get_RsaSignPkcs1Sha1, None)
    RsaSignPkcs1Sha256 = property(get_RsaSignPkcs1Sha256, None)
    RsaSignPkcs1Sha384 = property(get_RsaSignPkcs1Sha384, None)
    RsaSignPkcs1Sha512 = property(get_RsaSignPkcs1Sha512, None)
    RsaSignPssSha1 = property(get_RsaSignPssSha1, None)
    RsaSignPssSha256 = property(get_RsaSignPssSha256, None)
    RsaSignPssSha384 = property(get_RsaSignPssSha384, None)
    RsaSignPssSha512 = property(get_RsaSignPssSha512, None)
class AsymmetricKeyAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.AsymmetricKeyAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def CreateKeyPair(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keySize: UInt32) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportDefaultPrivateKeyBlob(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportKeyPairWithBlobType(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: Windows.Storage.Streams.IBuffer, BlobType: Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportDefaultPublicKeyBlob(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def ImportPublicKeyWithBlobType(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider, keyBlob: Windows.Storage.Streams.IBuffer, BlobType: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def CreateKeyPairWithCurveName(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider2, curveName: WinRT_String) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def CreateKeyPairWithCurveParameters(self: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProvider2, parameters: c_char_p_no) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: Windows.Security.Cryptography.Core.IAsymmetricKeyAlgorithmProviderStatics, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.AsymmetricKeyAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
Capi1KdfTargetAlgorithm = Int32
Capi1KdfTargetAlgorithm_NotAes: Capi1KdfTargetAlgorithm = 0
Capi1KdfTargetAlgorithm_Aes: Capi1KdfTargetAlgorithm = 1
class CryptographicEngine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.CryptographicEngine'
    @winrt_classmethod
    def SignHashedData(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def VerifySignatureWithHashInput(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, signature: Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_classmethod
    def DecryptAsync(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, iv: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def SignAsync(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def SignHashedDataAsync(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics2, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def Encrypt(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, iv: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def Decrypt(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, iv: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def EncryptAndAuthenticate(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, nonce: Windows.Storage.Streams.IBuffer, authenticatedData: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.EncryptedAndAuthenticatedData: ...
    @winrt_classmethod
    def DecryptAndAuthenticate(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, nonce: Windows.Storage.Streams.IBuffer, authenticationTag: Windows.Storage.Streams.IBuffer, authenticatedData: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def Sign(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def VerifySignature(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, signature: Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_classmethod
    def DeriveKeyMaterial(cls: Windows.Security.Cryptography.Core.ICryptographicEngineStatics, key: Windows.Security.Cryptography.Core.CryptographicKey, parameters: Windows.Security.Cryptography.Core.KeyDerivationParameters, desiredKeySize: UInt32) -> Windows.Storage.Streams.IBuffer: ...
class CryptographicHash(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.CryptographicHash'
    @winrt_mixinmethod
    def Append(self: Windows.Security.Cryptography.Core.IHashComputation, data: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetValueAndReset(self: Windows.Security.Cryptography.Core.IHashComputation) -> Windows.Storage.Streams.IBuffer: ...
class CryptographicKey(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.CryptographicKey'
    @winrt_mixinmethod
    def get_KeySize(self: Windows.Security.Cryptography.Core.ICryptographicKey) -> UInt32: ...
    @winrt_mixinmethod
    def ExportDefaultPrivateKeyBlobType(self: Windows.Security.Cryptography.Core.ICryptographicKey) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def ExportPrivateKeyWithBlobType(self: Windows.Security.Cryptography.Core.ICryptographicKey, BlobType: Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def ExportDefaultPublicKeyBlobType(self: Windows.Security.Cryptography.Core.ICryptographicKey) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def ExportPublicKeyWithBlobType(self: Windows.Security.Cryptography.Core.ICryptographicKey, BlobType: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Storage.Streams.IBuffer: ...
    KeySize = property(get_KeySize, None)
CryptographicPadding = Int32
CryptographicPadding_None: CryptographicPadding = 0
CryptographicPadding_RsaOaep: CryptographicPadding = 1
CryptographicPadding_RsaPkcs1V15: CryptographicPadding = 2
CryptographicPadding_RsaPss: CryptographicPadding = 3
CryptographicPrivateKeyBlobType = Int32
CryptographicPrivateKeyBlobType_Pkcs8RawPrivateKeyInfo: CryptographicPrivateKeyBlobType = 0
CryptographicPrivateKeyBlobType_Pkcs1RsaPrivateKey: CryptographicPrivateKeyBlobType = 1
CryptographicPrivateKeyBlobType_BCryptPrivateKey: CryptographicPrivateKeyBlobType = 2
CryptographicPrivateKeyBlobType_Capi1PrivateKey: CryptographicPrivateKeyBlobType = 3
CryptographicPrivateKeyBlobType_BCryptEccFullPrivateKey: CryptographicPrivateKeyBlobType = 4
CryptographicPublicKeyBlobType = Int32
CryptographicPublicKeyBlobType_X509SubjectPublicKeyInfo: CryptographicPublicKeyBlobType = 0
CryptographicPublicKeyBlobType_Pkcs1RsaPublicKey: CryptographicPublicKeyBlobType = 1
CryptographicPublicKeyBlobType_BCryptPublicKey: CryptographicPublicKeyBlobType = 2
CryptographicPublicKeyBlobType_Capi1PublicKey: CryptographicPublicKeyBlobType = 3
CryptographicPublicKeyBlobType_BCryptEccFullPublicKey: CryptographicPublicKeyBlobType = 4
class EccCurveNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.EccCurveNames'
    @winrt_classmethod
    def get_BrainpoolP160r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP160t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP192r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP192t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP224r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP224t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP256r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP256t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP320r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP320t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP384r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP384t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP512r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BrainpoolP512t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Curve25519(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ec192wapi(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP192(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP224(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP256(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP384(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NistP521(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NumsP256t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NumsP384t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NumsP512t1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP160k1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP160r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP160r2(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP192k1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP192r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP224k1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP224r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP256k1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP256r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP384r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SecP521r1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wtls7(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wtls9(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wtls12(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P192v1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P192v2(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P192v3(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P239v1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P239v2(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P239v3(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_X962P256v1(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AllEccCurveNames(cls: Windows.Security.Cryptography.Core.IEccCurveNamesStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
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
    Wtls7 = property(get_Wtls7, None)
    Wtls9 = property(get_Wtls9, None)
    Wtls12 = property(get_Wtls12, None)
    X962P192v1 = property(get_X962P192v1, None)
    X962P192v2 = property(get_X962P192v2, None)
    X962P192v3 = property(get_X962P192v3, None)
    X962P239v1 = property(get_X962P239v1, None)
    X962P239v2 = property(get_X962P239v2, None)
    X962P239v3 = property(get_X962P239v3, None)
    X962P256v1 = property(get_X962P256v1, None)
    AllEccCurveNames = property(get_AllEccCurveNames, None)
class EncryptedAndAuthenticatedData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.EncryptedAndAuthenticatedData'
    @winrt_mixinmethod
    def get_EncryptedData(self: Windows.Security.Cryptography.Core.IEncryptedAndAuthenticatedData) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AuthenticationTag(self: Windows.Security.Cryptography.Core.IEncryptedAndAuthenticatedData) -> Windows.Storage.Streams.IBuffer: ...
    EncryptedData = property(get_EncryptedData, None)
    AuthenticationTag = property(get_AuthenticationTag, None)
class HashAlgorithmNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.HashAlgorithmNames'
    @winrt_classmethod
    def get_Md5(cls: Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha1(cls: Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha256(cls: Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha384(cls: Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sha512(cls: Windows.Security.Cryptography.Core.IHashAlgorithmNamesStatics) -> WinRT_String: ...
    Md5 = property(get_Md5, None)
    Sha1 = property(get_Sha1, None)
    Sha256 = property(get_Sha256, None)
    Sha384 = property(get_Sha384, None)
    Sha512 = property(get_Sha512, None)
class HashAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.HashAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: Windows.Security.Cryptography.Core.IHashAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HashLength(self: Windows.Security.Cryptography.Core.IHashAlgorithmProvider) -> UInt32: ...
    @winrt_mixinmethod
    def HashData(self: Windows.Security.Cryptography.Core.IHashAlgorithmProvider, data: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def CreateHash(self: Windows.Security.Cryptography.Core.IHashAlgorithmProvider) -> Windows.Security.Cryptography.Core.CryptographicHash: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: Windows.Security.Cryptography.Core.IHashAlgorithmProviderStatics, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.HashAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
    HashLength = property(get_HashLength, None)
class IAsymmetricAlgorithmNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('caf6fce4-67c0-46aa-84-f9-75-2e-77-44-9f-9b')
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
    RsaPkcs1 = property(get_RsaPkcs1, None)
    RsaOaepSha1 = property(get_RsaOaepSha1, None)
    RsaOaepSha256 = property(get_RsaOaepSha256, None)
    RsaOaepSha384 = property(get_RsaOaepSha384, None)
    RsaOaepSha512 = property(get_RsaOaepSha512, None)
    EcdsaP256Sha256 = property(get_EcdsaP256Sha256, None)
    EcdsaP384Sha384 = property(get_EcdsaP384Sha384, None)
    EcdsaP521Sha512 = property(get_EcdsaP521Sha512, None)
    DsaSha1 = property(get_DsaSha1, None)
    DsaSha256 = property(get_DsaSha256, None)
    RsaSignPkcs1Sha1 = property(get_RsaSignPkcs1Sha1, None)
    RsaSignPkcs1Sha256 = property(get_RsaSignPkcs1Sha256, None)
    RsaSignPkcs1Sha384 = property(get_RsaSignPkcs1Sha384, None)
    RsaSignPkcs1Sha512 = property(get_RsaSignPkcs1Sha512, None)
    RsaSignPssSha1 = property(get_RsaSignPssSha1, None)
    RsaSignPssSha256 = property(get_RsaSignPssSha256, None)
    RsaSignPssSha384 = property(get_RsaSignPssSha384, None)
    RsaSignPssSha512 = property(get_RsaSignPssSha512, None)
class IAsymmetricAlgorithmNamesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f141c0d6-4bff-4f23-ba-66-60-45-b1-37-d5-df')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e8d2ff37-6259-4e88-b7-e0-94-19-1f-de-69-9e')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateKeyPair(self, keySize: UInt32) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(8)
    def ImportDefaultPrivateKeyBlob(self, keyBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(9)
    def ImportKeyPairWithBlobType(self, keyBlob: Windows.Storage.Streams.IBuffer, BlobType: Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(10)
    def ImportDefaultPublicKeyBlob(self, keyBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(11)
    def ImportPublicKeyWithBlobType(self, keyBlob: Windows.Storage.Streams.IBuffer, BlobType: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
class IAsymmetricKeyAlgorithmProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4e322a7e-7c4d-4997-ac-4f-1b-84-8b-36-30-6e')
    @winrt_commethod(6)
    def CreateKeyPairWithCurveName(self, curveName: WinRT_String) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_commethod(7)
    def CreateKeyPairWithCurveParameters(self, parameters: c_char_p_no) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
class IAsymmetricKeyAlgorithmProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('425bde18-a7f3-47a6-a8-d2-c4-8d-60-33-a6-5c')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.AsymmetricKeyAlgorithmProvider: ...
class ICryptographicEngineStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9fea0639-6ff7-4c85-a0-95-95-eb-31-71-5e-b9')
    @winrt_commethod(6)
    def Encrypt(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, iv: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def Decrypt(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, iv: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def EncryptAndAuthenticate(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, nonce: Windows.Storage.Streams.IBuffer, authenticatedData: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.EncryptedAndAuthenticatedData: ...
    @winrt_commethod(9)
    def DecryptAndAuthenticate(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, nonce: Windows.Storage.Streams.IBuffer, authenticationTag: Windows.Storage.Streams.IBuffer, authenticatedData: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def Sign(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def VerifySignature(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, signature: Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_commethod(12)
    def DeriveKeyMaterial(self, key: Windows.Security.Cryptography.Core.CryptographicKey, parameters: Windows.Security.Cryptography.Core.KeyDerivationParameters, desiredKeySize: UInt32) -> Windows.Storage.Streams.IBuffer: ...
class ICryptographicEngineStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('675948fe-df9f-4191-92-c7-6c-e6-f5-84-20-e0')
    @winrt_commethod(6)
    def SignHashedData(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def VerifySignatureWithHashInput(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, signature: Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_commethod(8)
    def DecryptAsync(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer, iv: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def SignAsync(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(10)
    def SignHashedDataAsync(self, key: Windows.Security.Cryptography.Core.CryptographicKey, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
class ICryptographicKey(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ed2a3b70-8e7b-4009-84-01-ff-d1-a6-2e-eb-27')
    @winrt_commethod(6)
    def get_KeySize(self) -> UInt32: ...
    @winrt_commethod(7)
    def ExportDefaultPrivateKeyBlobType(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def ExportPrivateKeyWithBlobType(self, BlobType: Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def ExportDefaultPublicKeyBlobType(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def ExportPublicKeyWithBlobType(self, BlobType: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Storage.Streams.IBuffer: ...
    KeySize = property(get_KeySize, None)
class IEccCurveNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b3ff930c-aeeb-409e-b7-d4-9b-95-29-5a-ae-cf')
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
    def get_AllEccCurveNames(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
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
    Wtls7 = property(get_Wtls7, None)
    Wtls9 = property(get_Wtls9, None)
    Wtls12 = property(get_Wtls12, None)
    X962P192v1 = property(get_X962P192v1, None)
    X962P192v2 = property(get_X962P192v2, None)
    X962P192v3 = property(get_X962P192v3, None)
    X962P239v1 = property(get_X962P239v1, None)
    X962P239v2 = property(get_X962P239v2, None)
    X962P239v3 = property(get_X962P239v3, None)
    X962P256v1 = property(get_X962P256v1, None)
    AllEccCurveNames = property(get_AllEccCurveNames, None)
class IEncryptedAndAuthenticatedData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6fa42fe7-1ecb-4b00-be-a5-60-b8-3f-86-2f-17')
    @winrt_commethod(6)
    def get_EncryptedData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_AuthenticationTag(self) -> Windows.Storage.Streams.IBuffer: ...
    EncryptedData = property(get_EncryptedData, None)
    AuthenticationTag = property(get_AuthenticationTag, None)
class IHashAlgorithmNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6b5e0516-de96-4f0a-8d-57-dc-c9-da-e3-6c-76')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('be9b3080-b2c3-422b-bc-e1-ec-90-ef-b5-d7-b5')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HashLength(self) -> UInt32: ...
    @winrt_commethod(8)
    def HashData(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def CreateHash(self) -> Windows.Security.Cryptography.Core.CryptographicHash: ...
    AlgorithmName = property(get_AlgorithmName, None)
    HashLength = property(get_HashLength, None)
class IHashAlgorithmProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9fac9741-5cc4-4336-ae-38-62-12-b7-5a-91-5a')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.HashAlgorithmProvider: ...
class IHashComputation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5904d1b6-ad31-4603-a3-a4-b1-bd-a9-8e-25-62')
    @winrt_commethod(6)
    def Append(self, data: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def GetValueAndReset(self) -> Windows.Storage.Streams.IBuffer: ...
class IKeyDerivationAlgorithmNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7b6e363e-94d2-4739-a5-7b-02-2e-0c-3a-40-2a')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('57953fab-6044-466f-97-f4-33-7b-78-08-38-4d')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e1fba83b-4671-43b7-91-58-76-3a-aa-98-b6-bf')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateKey(self, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
class IKeyDerivationAlgorithmProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0a22097a-0a1c-443b-94-18-b9-49-8a-eb-16-03')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.KeyDerivationAlgorithmProvider: ...
class IKeyDerivationParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7bf05967-047b-4a8c-96-4a-46-9f-fd-55-22-e2')
    @winrt_commethod(6)
    def get_KdfGenericBinary(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_KdfGenericBinary(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_IterationCount(self) -> UInt32: ...
    KdfGenericBinary = property(get_KdfGenericBinary, put_KdfGenericBinary)
    IterationCount = property(get_IterationCount, None)
class IKeyDerivationParameters2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cd4166d1-417e-4f4c-b6-66-c0-d8-79-f3-f8-e0')
    @winrt_commethod(6)
    def get_Capi1KdfTargetAlgorithm(self) -> Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm: ...
    @winrt_commethod(7)
    def put_Capi1KdfTargetAlgorithm(self, value: Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> Void: ...
    Capi1KdfTargetAlgorithm = property(get_Capi1KdfTargetAlgorithm, put_Capi1KdfTargetAlgorithm)
class IKeyDerivationParametersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ea961fbe-f37f-4146-9d-fe-a4-56-f1-73-5f-4b')
    @winrt_commethod(6)
    def BuildForPbkdf2(self, pbkdf2Salt: Windows.Storage.Streams.IBuffer, iterationCount: UInt32) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_commethod(7)
    def BuildForSP800108(self, label: Windows.Storage.Streams.IBuffer, context: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_commethod(8)
    def BuildForSP80056a(self, algorithmId: Windows.Storage.Streams.IBuffer, partyUInfo: Windows.Storage.Streams.IBuffer, partyVInfo: Windows.Storage.Streams.IBuffer, suppPubInfo: Windows.Storage.Streams.IBuffer, suppPrivInfo: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
class IKeyDerivationParametersStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a5783dd5-58e3-4efb-b2-83-a1-65-31-26-e1-be')
    @winrt_commethod(6)
    def BuildForCapi1Kdf(self, capi1KdfTargetAlgorithm: Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
class IMacAlgorithmNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('41412678-fb1e-43a4-89-5e-a9-02-6e-43-90-a3')
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
    HmacMd5 = property(get_HmacMd5, None)
    HmacSha1 = property(get_HmacSha1, None)
    HmacSha256 = property(get_HmacSha256, None)
    HmacSha384 = property(get_HmacSha384, None)
    HmacSha512 = property(get_HmacSha512, None)
    AesCmac = property(get_AesCmac, None)
class IMacAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4a3fc5c3-1cbd-41ce-a0-92-aa-0b-c5-d2-d2-f5')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MacLength(self) -> UInt32: ...
    @winrt_commethod(8)
    def CreateKey(self, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
    MacLength = property(get_MacLength, None)
class IMacAlgorithmProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6da32a15-d931-42ed-8e-7e-c3-01-ca-ee-11-9c')
    @winrt_commethod(6)
    def CreateHash(self, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicHash: ...
class IMacAlgorithmProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c9bdc147-cc77-4df0-9e-4e-b9-21-e0-80-64-4c')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.MacAlgorithmProvider: ...
class IPersistedKeyProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('77274814-d9d4-4cf5-b6-68-e0-45-7d-f3-08-94')
    @winrt_commethod(6)
    def OpenKeyPairFromCertificateAsync(self, certificate: Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: Windows.Security.Cryptography.Core.CryptographicPadding) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Core.CryptographicKey]: ...
    @winrt_commethod(7)
    def OpenPublicKeyFromCertificate(self, certificate: Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: Windows.Security.Cryptography.Core.CryptographicPadding) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
class ISymmetricAlgorithmNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6870727b-c996-4eae-84-d7-79-b2-ae-b7-3b-9c')
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
    DesCbc = property(get_DesCbc, None)
    DesEcb = property(get_DesEcb, None)
    TripleDesCbc = property(get_TripleDesCbc, None)
    TripleDesEcb = property(get_TripleDesEcb, None)
    Rc2Cbc = property(get_Rc2Cbc, None)
    Rc2Ecb = property(get_Rc2Ecb, None)
    AesCbc = property(get_AesCbc, None)
    AesEcb = property(get_AesEcb, None)
    AesGcm = property(get_AesGcm, None)
    AesCcm = property(get_AesCcm, None)
    AesCbcPkcs7 = property(get_AesCbcPkcs7, None)
    AesEcbPkcs7 = property(get_AesEcbPkcs7, None)
    DesCbcPkcs7 = property(get_DesCbcPkcs7, None)
    DesEcbPkcs7 = property(get_DesEcbPkcs7, None)
    TripleDesCbcPkcs7 = property(get_TripleDesCbcPkcs7, None)
    TripleDesEcbPkcs7 = property(get_TripleDesEcbPkcs7, None)
    Rc2CbcPkcs7 = property(get_Rc2CbcPkcs7, None)
    Rc2EcbPkcs7 = property(get_Rc2EcbPkcs7, None)
    Rc4 = property(get_Rc4, None)
class ISymmetricKeyAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3d7e4a33-3bd0-4902-8a-c8-47-0d-50-d2-13-76')
    @winrt_commethod(6)
    def get_AlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BlockLength(self) -> UInt32: ...
    @winrt_commethod(8)
    def CreateSymmetricKey(self, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    AlgorithmName = property(get_AlgorithmName, None)
    BlockLength = property(get_BlockLength, None)
class ISymmetricKeyAlgorithmProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8d3b2326-1f37-491f-b6-0e-f5-43-1b-26-b4-83')
    @winrt_commethod(6)
    def OpenAlgorithm(self, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.SymmetricKeyAlgorithmProvider: ...
class KeyDerivationAlgorithmNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.KeyDerivationAlgorithmNames'
    @winrt_classmethod
    def get_CapiKdfMd5(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha1(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha256(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha384(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_CapiKdfSha512(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Md5(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha1(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha256(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha384(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pbkdf2Sha512(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacMd5(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha1(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha256(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha384(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp800108CtrHmacSha512(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatMd5(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha1(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha256(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha384(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sp80056aConcatSha512(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmNamesStatics) -> WinRT_String: ...
    CapiKdfMd5 = property(get_CapiKdfMd5, None)
    CapiKdfSha1 = property(get_CapiKdfSha1, None)
    CapiKdfSha256 = property(get_CapiKdfSha256, None)
    CapiKdfSha384 = property(get_CapiKdfSha384, None)
    CapiKdfSha512 = property(get_CapiKdfSha512, None)
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
class KeyDerivationAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.KeyDerivationAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def CreateKey(self: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProvider, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: Windows.Security.Cryptography.Core.IKeyDerivationAlgorithmProviderStatics, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.KeyDerivationAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
class KeyDerivationParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.KeyDerivationParameters'
    @winrt_mixinmethod
    def get_KdfGenericBinary(self: Windows.Security.Cryptography.Core.IKeyDerivationParameters) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_KdfGenericBinary(self: Windows.Security.Cryptography.Core.IKeyDerivationParameters, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_IterationCount(self: Windows.Security.Cryptography.Core.IKeyDerivationParameters) -> UInt32: ...
    @winrt_mixinmethod
    def get_Capi1KdfTargetAlgorithm(self: Windows.Security.Cryptography.Core.IKeyDerivationParameters2) -> Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm: ...
    @winrt_mixinmethod
    def put_Capi1KdfTargetAlgorithm(self: Windows.Security.Cryptography.Core.IKeyDerivationParameters2, value: Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> Void: ...
    @winrt_classmethod
    def BuildForCapi1Kdf(cls: Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics2, capi1KdfTargetAlgorithm: Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_classmethod
    def BuildForPbkdf2(cls: Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics, pbkdf2Salt: Windows.Storage.Streams.IBuffer, iterationCount: UInt32) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_classmethod
    def BuildForSP800108(cls: Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics, label: Windows.Storage.Streams.IBuffer, context: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    @winrt_classmethod
    def BuildForSP80056a(cls: Windows.Security.Cryptography.Core.IKeyDerivationParametersStatics, algorithmId: Windows.Storage.Streams.IBuffer, partyUInfo: Windows.Storage.Streams.IBuffer, partyVInfo: Windows.Storage.Streams.IBuffer, suppPubInfo: Windows.Storage.Streams.IBuffer, suppPrivInfo: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.KeyDerivationParameters: ...
    KdfGenericBinary = property(get_KdfGenericBinary, put_KdfGenericBinary)
    IterationCount = property(get_IterationCount, None)
    Capi1KdfTargetAlgorithm = property(get_Capi1KdfTargetAlgorithm, put_Capi1KdfTargetAlgorithm)
class MacAlgorithmNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.MacAlgorithmNames'
    @winrt_classmethod
    def get_HmacMd5(cls: Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha1(cls: Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha256(cls: Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha384(cls: Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HmacSha512(cls: Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCmac(cls: Windows.Security.Cryptography.Core.IMacAlgorithmNamesStatics) -> WinRT_String: ...
    HmacMd5 = property(get_HmacMd5, None)
    HmacSha1 = property(get_HmacSha1, None)
    HmacSha256 = property(get_HmacSha256, None)
    HmacSha384 = property(get_HmacSha384, None)
    HmacSha512 = property(get_HmacSha512, None)
    AesCmac = property(get_AesCmac, None)
class MacAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.MacAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: Windows.Security.Cryptography.Core.IMacAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MacLength(self: Windows.Security.Cryptography.Core.IMacAlgorithmProvider) -> UInt32: ...
    @winrt_mixinmethod
    def CreateKey(self: Windows.Security.Cryptography.Core.IMacAlgorithmProvider, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_mixinmethod
    def CreateHash(self: Windows.Security.Cryptography.Core.IMacAlgorithmProvider2, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicHash: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: Windows.Security.Cryptography.Core.IMacAlgorithmProviderStatics, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.MacAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
    MacLength = property(get_MacLength, None)
class PersistedKeyProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.PersistedKeyProvider'
    @winrt_classmethod
    def OpenKeyPairFromCertificateAsync(cls: Windows.Security.Cryptography.Core.IPersistedKeyProviderStatics, certificate: Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: Windows.Security.Cryptography.Core.CryptographicPadding) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Core.CryptographicKey]: ...
    @winrt_classmethod
    def OpenPublicKeyFromCertificate(cls: Windows.Security.Cryptography.Core.IPersistedKeyProviderStatics, certificate: Windows.Security.Cryptography.Certificates.Certificate, hashAlgorithmName: WinRT_String, padding: Windows.Security.Cryptography.Core.CryptographicPadding) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
class SymmetricAlgorithmNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.SymmetricAlgorithmNames'
    @winrt_classmethod
    def get_DesCbc(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DesEcb(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesCbc(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesEcb(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2Cbc(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2Ecb(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCbc(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesEcb(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesGcm(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCcm(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesCbcPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AesEcbPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DesCbcPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DesEcbPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesCbcPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TripleDesEcbPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2CbcPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc2EcbPkcs7(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rc4(cls: Windows.Security.Cryptography.Core.ISymmetricAlgorithmNamesStatics) -> WinRT_String: ...
    DesCbc = property(get_DesCbc, None)
    DesEcb = property(get_DesEcb, None)
    TripleDesCbc = property(get_TripleDesCbc, None)
    TripleDesEcb = property(get_TripleDesEcb, None)
    Rc2Cbc = property(get_Rc2Cbc, None)
    Rc2Ecb = property(get_Rc2Ecb, None)
    AesCbc = property(get_AesCbc, None)
    AesEcb = property(get_AesEcb, None)
    AesGcm = property(get_AesGcm, None)
    AesCcm = property(get_AesCcm, None)
    AesCbcPkcs7 = property(get_AesCbcPkcs7, None)
    AesEcbPkcs7 = property(get_AesEcbPkcs7, None)
    DesCbcPkcs7 = property(get_DesCbcPkcs7, None)
    DesEcbPkcs7 = property(get_DesEcbPkcs7, None)
    TripleDesCbcPkcs7 = property(get_TripleDesCbcPkcs7, None)
    TripleDesEcbPkcs7 = property(get_TripleDesEcbPkcs7, None)
    Rc2CbcPkcs7 = property(get_Rc2CbcPkcs7, None)
    Rc2EcbPkcs7 = property(get_Rc2EcbPkcs7, None)
    Rc4 = property(get_Rc4, None)
class SymmetricKeyAlgorithmProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Core.SymmetricKeyAlgorithmProvider'
    @winrt_mixinmethod
    def get_AlgorithmName(self: Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BlockLength(self: Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider) -> UInt32: ...
    @winrt_mixinmethod
    def CreateSymmetricKey(self: Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProvider, keyMaterial: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Core.CryptographicKey: ...
    @winrt_classmethod
    def OpenAlgorithm(cls: Windows.Security.Cryptography.Core.ISymmetricKeyAlgorithmProviderStatics, algorithm: WinRT_String) -> Windows.Security.Cryptography.Core.SymmetricKeyAlgorithmProvider: ...
    AlgorithmName = property(get_AlgorithmName, None)
    BlockLength = property(get_BlockLength, None)
make_head(_module, 'AsymmetricAlgorithmNames')
make_head(_module, 'AsymmetricKeyAlgorithmProvider')
make_head(_module, 'CryptographicEngine')
make_head(_module, 'CryptographicHash')
make_head(_module, 'CryptographicKey')
make_head(_module, 'EccCurveNames')
make_head(_module, 'EncryptedAndAuthenticatedData')
make_head(_module, 'HashAlgorithmNames')
make_head(_module, 'HashAlgorithmProvider')
make_head(_module, 'IAsymmetricAlgorithmNamesStatics')
make_head(_module, 'IAsymmetricAlgorithmNamesStatics2')
make_head(_module, 'IAsymmetricKeyAlgorithmProvider')
make_head(_module, 'IAsymmetricKeyAlgorithmProvider2')
make_head(_module, 'IAsymmetricKeyAlgorithmProviderStatics')
make_head(_module, 'ICryptographicEngineStatics')
make_head(_module, 'ICryptographicEngineStatics2')
make_head(_module, 'ICryptographicKey')
make_head(_module, 'IEccCurveNamesStatics')
make_head(_module, 'IEncryptedAndAuthenticatedData')
make_head(_module, 'IHashAlgorithmNamesStatics')
make_head(_module, 'IHashAlgorithmProvider')
make_head(_module, 'IHashAlgorithmProviderStatics')
make_head(_module, 'IHashComputation')
make_head(_module, 'IKeyDerivationAlgorithmNamesStatics')
make_head(_module, 'IKeyDerivationAlgorithmNamesStatics2')
make_head(_module, 'IKeyDerivationAlgorithmProvider')
make_head(_module, 'IKeyDerivationAlgorithmProviderStatics')
make_head(_module, 'IKeyDerivationParameters')
make_head(_module, 'IKeyDerivationParameters2')
make_head(_module, 'IKeyDerivationParametersStatics')
make_head(_module, 'IKeyDerivationParametersStatics2')
make_head(_module, 'IMacAlgorithmNamesStatics')
make_head(_module, 'IMacAlgorithmProvider')
make_head(_module, 'IMacAlgorithmProvider2')
make_head(_module, 'IMacAlgorithmProviderStatics')
make_head(_module, 'IPersistedKeyProviderStatics')
make_head(_module, 'ISymmetricAlgorithmNamesStatics')
make_head(_module, 'ISymmetricKeyAlgorithmProvider')
make_head(_module, 'ISymmetricKeyAlgorithmProviderStatics')
make_head(_module, 'KeyDerivationAlgorithmNames')
make_head(_module, 'KeyDerivationAlgorithmProvider')
make_head(_module, 'KeyDerivationParameters')
make_head(_module, 'MacAlgorithmNames')
make_head(_module, 'MacAlgorithmProvider')
make_head(_module, 'PersistedKeyProvider')
make_head(_module, 'SymmetricAlgorithmNames')
make_head(_module, 'SymmetricKeyAlgorithmProvider')
