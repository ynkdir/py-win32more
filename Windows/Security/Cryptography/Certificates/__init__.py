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
import Windows.Networking
import Windows.Security.Cryptography.Certificates
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
class Certificate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.Certificate'
    @winrt_factorymethod
    def CreateCertificate(cls: Windows.Security.Cryptography.Certificates.ICertificateFactory, certBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def BuildChainAsync(self: Windows.Security.Cryptography.Certificates.ICertificate, certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate]) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_mixinmethod
    def BuildChainWithParametersAsync(self: Windows.Security.Cryptography.Certificates.ICertificate, certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate], parameters: Windows.Security.Cryptography.Certificates.ChainBuildingParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: Windows.Security.Cryptography.Certificates.ICertificate) -> c_char_p_no: ...
    @winrt_mixinmethod
    def GetHashValue(self: Windows.Security.Cryptography.Certificates.ICertificate) -> c_char_p_no: ...
    @winrt_mixinmethod
    def GetHashValueWithAlgorithm(self: Windows.Security.Cryptography.Certificates.ICertificate, hashAlgorithmName: WinRT_String) -> c_char_p_no: ...
    @winrt_mixinmethod
    def GetCertificateBlob(self: Windows.Security.Cryptography.Certificates.ICertificate) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.Security.Cryptography.Certificates.ICertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Issuer(self: Windows.Security.Cryptography.Certificates.ICertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasPrivateKey(self: Windows.Security.Cryptography.Certificates.ICertificate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStronglyProtected(self: Windows.Security.Cryptography.Certificates.ICertificate) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValidFrom(self: Windows.Security.Cryptography.Certificates.ICertificate) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ValidTo(self: Windows.Security.Cryptography.Certificates.ICertificate) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EnhancedKeyUsages(self: Windows.Security.Cryptography.Certificates.ICertificate) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: Windows.Security.Cryptography.Certificates.ICertificate, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Security.Cryptography.Certificates.ICertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsSecurityDeviceBound(self: Windows.Security.Cryptography.Certificates.ICertificate2) -> Boolean: ...
    @winrt_mixinmethod
    def get_KeyUsages(self: Windows.Security.Cryptography.Certificates.ICertificate2) -> Windows.Security.Cryptography.Certificates.CertificateKeyUsages: ...
    @winrt_mixinmethod
    def get_KeyAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificate2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SignatureAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificate2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SignatureHashAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificate2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SubjectAlternativeName(self: Windows.Security.Cryptography.Certificates.ICertificate2) -> Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_mixinmethod
    def get_IsPerUser(self: Windows.Security.Cryptography.Certificates.ICertificate3) -> Boolean: ...
    @winrt_mixinmethod
    def get_StoreName(self: Windows.Security.Cryptography.Certificates.ICertificate3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_KeyStorageProviderName(self: Windows.Security.Cryptography.Certificates.ICertificate3) -> WinRT_String: ...
    SerialNumber = property(get_SerialNumber, None)
    Subject = property(get_Subject, None)
    Issuer = property(get_Issuer, None)
    HasPrivateKey = property(get_HasPrivateKey, None)
    IsStronglyProtected = property(get_IsStronglyProtected, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    IsSecurityDeviceBound = property(get_IsSecurityDeviceBound, None)
    KeyUsages = property(get_KeyUsages, None)
    KeyAlgorithmName = property(get_KeyAlgorithmName, None)
    SignatureAlgorithmName = property(get_SignatureAlgorithmName, None)
    SignatureHashAlgorithmName = property(get_SignatureHashAlgorithmName, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
    IsPerUser = property(get_IsPerUser, None)
    StoreName = property(get_StoreName, None)
    KeyStorageProviderName = property(get_KeyStorageProviderName, None)
class CertificateChain(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateChain'
    @winrt_mixinmethod
    def Validate(self: Windows.Security.Cryptography.Certificates.ICertificateChain) -> Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_mixinmethod
    def ValidateWithParameters(self: Windows.Security.Cryptography.Certificates.ICertificateChain, parameter: Windows.Security.Cryptography.Certificates.ChainValidationParameters) -> Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_mixinmethod
    def GetCertificates(self: Windows.Security.Cryptography.Certificates.ICertificateChain, includeRoot: Boolean) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
CertificateChainPolicy = Int32
CertificateChainPolicy_Base: CertificateChainPolicy = 0
CertificateChainPolicy_Ssl: CertificateChainPolicy = 1
CertificateChainPolicy_NTAuthentication: CertificateChainPolicy = 2
CertificateChainPolicy_MicrosoftRoot: CertificateChainPolicy = 3
class CertificateEnrollmentManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateEnrollmentManager'
    @winrt_classmethod
    def ImportPfxDataToKspWithParametersAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics3, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: Windows.Security.Cryptography.Certificates.PfxImportParameters) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_UserCertificateEnrollmentManager(cls: Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics2) -> Windows.Security.Cryptography.Certificates.UserCertificateEnrollmentManager: ...
    @winrt_classmethod
    def ImportPfxDataToKspAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics2, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def CreateRequestAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics, request: Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def InstallCertificateAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics, certificate: WinRT_String, installOption: Windows.Security.Cryptography.Certificates.InstallOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ImportPfxDataAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    UserCertificateEnrollmentManager = property(get_UserCertificateEnrollmentManager, None)
class CertificateExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateExtension'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.CertificateExtension: ...
    @winrt_mixinmethod
    def get_ObjectId(self: Windows.Security.Cryptography.Certificates.ICertificateExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ObjectId(self: Windows.Security.Cryptography.Certificates.ICertificateExtension, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsCritical(self: Windows.Security.Cryptography.Certificates.ICertificateExtension) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCritical(self: Windows.Security.Cryptography.Certificates.ICertificateExtension, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def EncodeValue(self: Windows.Security.Cryptography.Certificates.ICertificateExtension, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Security.Cryptography.Certificates.ICertificateExtension) -> c_char_p_no: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Security.Cryptography.Certificates.ICertificateExtension, value: c_char_p_no) -> Void: ...
    ObjectId = property(get_ObjectId, put_ObjectId)
    IsCritical = property(get_IsCritical, put_IsCritical)
    Value = property(get_Value, put_Value)
class CertificateKeyUsages(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateKeyUsages'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.CertificateKeyUsages: ...
    @winrt_mixinmethod
    def get_EncipherOnly(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_EncipherOnly(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrlSign(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrlSign(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyCertificateSign(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeyCertificateSign(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyAgreement(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeyAgreement(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DataEncipherment(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_DataEncipherment(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyEncipherment(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeyEncipherment(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NonRepudiation(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_NonRepudiation(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DigitalSignature(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_DigitalSignature(self: Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    EncipherOnly = property(get_EncipherOnly, put_EncipherOnly)
    CrlSign = property(get_CrlSign, put_CrlSign)
    KeyCertificateSign = property(get_KeyCertificateSign, put_KeyCertificateSign)
    KeyAgreement = property(get_KeyAgreement, put_KeyAgreement)
    DataEncipherment = property(get_DataEncipherment, put_DataEncipherment)
    KeyEncipherment = property(get_KeyEncipherment, put_KeyEncipherment)
    NonRepudiation = property(get_NonRepudiation, put_NonRepudiation)
    DigitalSignature = property(get_DigitalSignature, put_DigitalSignature)
class CertificateQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateQuery'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.CertificateQuery: ...
    @winrt_mixinmethod
    def get_EnhancedKeyUsages(self: Windows.Security.Cryptography.Certificates.ICertificateQuery) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IssuerName(self: Windows.Security.Cryptography.Certificates.ICertificateQuery) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IssuerName(self: Windows.Security.Cryptography.Certificates.ICertificateQuery, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Security.Cryptography.Certificates.ICertificateQuery) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: Windows.Security.Cryptography.Certificates.ICertificateQuery, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbprint(self: Windows.Security.Cryptography.Certificates.ICertificateQuery) -> c_char_p_no: ...
    @winrt_mixinmethod
    def put_Thumbprint(self: Windows.Security.Cryptography.Certificates.ICertificateQuery, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareOnly(self: Windows.Security.Cryptography.Certificates.ICertificateQuery) -> Boolean: ...
    @winrt_mixinmethod
    def put_HardwareOnly(self: Windows.Security.Cryptography.Certificates.ICertificateQuery, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeDuplicates(self: Windows.Security.Cryptography.Certificates.ICertificateQuery2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeDuplicates(self: Windows.Security.Cryptography.Certificates.ICertificateQuery2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeExpiredCertificates(self: Windows.Security.Cryptography.Certificates.ICertificateQuery2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeExpiredCertificates(self: Windows.Security.Cryptography.Certificates.ICertificateQuery2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StoreName(self: Windows.Security.Cryptography.Certificates.ICertificateQuery2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StoreName(self: Windows.Security.Cryptography.Certificates.ICertificateQuery2, value: WinRT_String) -> Void: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    IssuerName = property(get_IssuerName, put_IssuerName)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    Thumbprint = property(get_Thumbprint, put_Thumbprint)
    HardwareOnly = property(get_HardwareOnly, put_HardwareOnly)
    IncludeDuplicates = property(get_IncludeDuplicates, put_IncludeDuplicates)
    IncludeExpiredCertificates = property(get_IncludeExpiredCertificates, put_IncludeExpiredCertificates)
    StoreName = property(get_StoreName, put_StoreName)
class CertificateRequestProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateRequestProperties'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.CertificateRequestProperties: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KeyAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_KeyAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KeySize(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_KeySize(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HashAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HashAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Exportable(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_mixinmethod
    def put_Exportable(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_mixinmethod
    def get_KeyUsages(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> Windows.Security.Cryptography.Certificates.EnrollKeyUsages: ...
    @winrt_mixinmethod
    def put_KeyUsages(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: Windows.Security.Cryptography.Certificates.EnrollKeyUsages) -> Void: ...
    @winrt_mixinmethod
    def get_KeyProtectionLevel(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_mixinmethod
    def put_KeyProtectionLevel(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_KeyStorageProviderName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_KeyStorageProviderName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SmartcardReaderName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SmartcardReaderName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SigningCertificate(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_SigningCertificate(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_AttestationCredentialCertificate(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_AttestationCredentialCertificate(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_CurveName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CurveName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CurveParameters(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> c_char_p_no: ...
    @winrt_mixinmethod
    def put_CurveParameters(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def get_ContainerNamePrefix(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContainerNamePrefix(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContainerName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContainerName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UseExistingKey(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseExistingKey(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressedDefaults(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SubjectAlternativeName(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4) -> Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_mixinmethod
    def get_Extensions(self: Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.CertificateExtension]: ...
    Subject = property(get_Subject, put_Subject)
    KeyAlgorithmName = property(get_KeyAlgorithmName, put_KeyAlgorithmName)
    KeySize = property(get_KeySize, put_KeySize)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    Exportable = property(get_Exportable, put_Exportable)
    KeyUsages = property(get_KeyUsages, put_KeyUsages)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    SmartcardReaderName = property(get_SmartcardReaderName, put_SmartcardReaderName)
    SigningCertificate = property(get_SigningCertificate, put_SigningCertificate)
    AttestationCredentialCertificate = property(get_AttestationCredentialCertificate, put_AttestationCredentialCertificate)
    CurveName = property(get_CurveName, put_CurveName)
    CurveParameters = property(get_CurveParameters, put_CurveParameters)
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    ContainerName = property(get_ContainerName, put_ContainerName)
    UseExistingKey = property(get_UseExistingKey, put_UseExistingKey)
    SuppressedDefaults = property(get_SuppressedDefaults, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
    Extensions = property(get_Extensions, None)
class CertificateStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateStore'
    @winrt_mixinmethod
    def Add(self: Windows.Security.Cryptography.Certificates.ICertificateStore, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def Delete(self: Windows.Security.Cryptography.Certificates.ICertificateStore, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Security.Cryptography.Certificates.ICertificateStore2) -> WinRT_String: ...
    Name = property(get_Name, None)
class CertificateStores(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CertificateStores'
    @winrt_classmethod
    def GetUserStoreByName(cls: Windows.Security.Cryptography.Certificates.ICertificateStoresStatics2, storeName: WinRT_String) -> Windows.Security.Cryptography.Certificates.UserCertificateStore: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateStoresStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_classmethod
    def FindAllWithQueryAsync(cls: Windows.Security.Cryptography.Certificates.ICertificateStoresStatics, query: Windows.Security.Cryptography.Certificates.CertificateQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_classmethod
    def get_TrustedRootCertificationAuthorities(cls: Windows.Security.Cryptography.Certificates.ICertificateStoresStatics) -> Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_classmethod
    def get_IntermediateCertificationAuthorities(cls: Windows.Security.Cryptography.Certificates.ICertificateStoresStatics) -> Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_classmethod
    def GetStoreByName(cls: Windows.Security.Cryptography.Certificates.ICertificateStoresStatics, storeName: WinRT_String) -> Windows.Security.Cryptography.Certificates.CertificateStore: ...
    TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
    IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
class ChainBuildingParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.ChainBuildingParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.ChainBuildingParameters: ...
    @winrt_mixinmethod
    def get_EnhancedKeyUsages(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ValidationTimestamp(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_ValidationTimestamp(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_RevocationCheckEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_RevocationCheckEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NetworkRetrievalEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_NetworkRetrievalEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AuthorityInformationAccessEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_AuthorityInformationAccessEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentTimeValidationEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_CurrentTimeValidationEnabled(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusiveTrustRoots(self: Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.Certificate]: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    ValidationTimestamp = property(get_ValidationTimestamp, put_ValidationTimestamp)
    RevocationCheckEnabled = property(get_RevocationCheckEnabled, put_RevocationCheckEnabled)
    NetworkRetrievalEnabled = property(get_NetworkRetrievalEnabled, put_NetworkRetrievalEnabled)
    AuthorityInformationAccessEnabled = property(get_AuthorityInformationAccessEnabled, put_AuthorityInformationAccessEnabled)
    CurrentTimeValidationEnabled = property(get_CurrentTimeValidationEnabled, put_CurrentTimeValidationEnabled)
    ExclusiveTrustRoots = property(get_ExclusiveTrustRoots, None)
class ChainValidationParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.ChainValidationParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.ChainValidationParameters: ...
    @winrt_mixinmethod
    def get_CertificateChainPolicy(self: Windows.Security.Cryptography.Certificates.IChainValidationParameters) -> Windows.Security.Cryptography.Certificates.CertificateChainPolicy: ...
    @winrt_mixinmethod
    def put_CertificateChainPolicy(self: Windows.Security.Cryptography.Certificates.IChainValidationParameters, value: Windows.Security.Cryptography.Certificates.CertificateChainPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_ServerDnsName(self: Windows.Security.Cryptography.Certificates.IChainValidationParameters) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_ServerDnsName(self: Windows.Security.Cryptography.Certificates.IChainValidationParameters, value: Windows.Networking.HostName) -> Void: ...
    CertificateChainPolicy = property(get_CertificateChainPolicy, put_CertificateChainPolicy)
    ServerDnsName = property(get_ServerDnsName, put_ServerDnsName)
ChainValidationResult = Int32
ChainValidationResult_Success: ChainValidationResult = 0
ChainValidationResult_Untrusted: ChainValidationResult = 1
ChainValidationResult_Revoked: ChainValidationResult = 2
ChainValidationResult_Expired: ChainValidationResult = 3
ChainValidationResult_IncompleteChain: ChainValidationResult = 4
ChainValidationResult_InvalidSignature: ChainValidationResult = 5
ChainValidationResult_WrongUsage: ChainValidationResult = 6
ChainValidationResult_InvalidName: ChainValidationResult = 7
ChainValidationResult_InvalidCertificateAuthorityPolicy: ChainValidationResult = 8
ChainValidationResult_BasicConstraintsError: ChainValidationResult = 9
ChainValidationResult_UnknownCriticalExtension: ChainValidationResult = 10
ChainValidationResult_RevocationInformationMissing: ChainValidationResult = 11
ChainValidationResult_RevocationFailure: ChainValidationResult = 12
ChainValidationResult_OtherErrors: ChainValidationResult = 13
class CmsAttachedSignature(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CmsAttachedSignature'
    @winrt_factorymethod
    def CreateCmsAttachedSignature(cls: Windows.Security.Cryptography.Certificates.ICmsAttachedSignatureFactory, inputBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Certificates.CmsAttachedSignature: ...
    @winrt_mixinmethod
    def get_Certificates(self: Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_Signers(self: Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_mixinmethod
    def VerifySignature(self: Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> Windows.Security.Cryptography.Certificates.SignatureValidationResult: ...
    @winrt_classmethod
    def GenerateSignatureAsync(cls: Windows.Security.Cryptography.Certificates.ICmsAttachedSignatureStatics, data: Windows.Storage.Streams.IBuffer, signers: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    Certificates = property(get_Certificates, None)
    Content = property(get_Content, None)
    Signers = property(get_Signers, None)
class CmsDetachedSignature(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CmsDetachedSignature'
    @winrt_factorymethod
    def CreateCmsDetachedSignature(cls: Windows.Security.Cryptography.Certificates.ICmsDetachedSignatureFactory, inputBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Certificates.CmsDetachedSignature: ...
    @winrt_mixinmethod
    def get_Certificates(self: Windows.Security.Cryptography.Certificates.ICmsDetachedSignature) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def get_Signers(self: Windows.Security.Cryptography.Certificates.ICmsDetachedSignature) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_mixinmethod
    def VerifySignatureAsync(self: Windows.Security.Cryptography.Certificates.ICmsDetachedSignature, data: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Certificates.SignatureValidationResult]: ...
    @winrt_classmethod
    def GenerateSignatureAsync(cls: Windows.Security.Cryptography.Certificates.ICmsDetachedSignatureStatics, data: Windows.Storage.Streams.IInputStream, signers: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    Certificates = property(get_Certificates, None)
    Signers = property(get_Signers, None)
class CmsSignerInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CmsSignerInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.CmsSignerInfo: ...
    @winrt_mixinmethod
    def get_Certificate(self: Windows.Security.Cryptography.Certificates.ICmsSignerInfo) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_Certificate(self: Windows.Security.Cryptography.Certificates.ICmsSignerInfo, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_HashAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICmsSignerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HashAlgorithmName(self: Windows.Security.Cryptography.Certificates.ICmsSignerInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TimestampInfo(self: Windows.Security.Cryptography.Certificates.ICmsSignerInfo) -> Windows.Security.Cryptography.Certificates.CmsTimestampInfo: ...
    Certificate = property(get_Certificate, put_Certificate)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    TimestampInfo = property(get_TimestampInfo, None)
class CmsTimestampInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.CmsTimestampInfo'
    @winrt_mixinmethod
    def get_SigningCertificate(self: Windows.Security.Cryptography.Certificates.ICmsTimestampInfo) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_Certificates(self: Windows.Security.Cryptography.Certificates.ICmsTimestampInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Security.Cryptography.Certificates.ICmsTimestampInfo) -> Windows.Foundation.DateTime: ...
    SigningCertificate = property(get_SigningCertificate, None)
    Certificates = property(get_Certificates, None)
    Timestamp = property(get_Timestamp, None)
EnrollKeyUsages = UInt32
EnrollKeyUsages_None: EnrollKeyUsages = 0
EnrollKeyUsages_Decryption: EnrollKeyUsages = 1
EnrollKeyUsages_Signing: EnrollKeyUsages = 2
EnrollKeyUsages_KeyAgreement: EnrollKeyUsages = 4
EnrollKeyUsages_All: EnrollKeyUsages = 16777215
ExportOption = Int32
ExportOption_NotExportable: ExportOption = 0
ExportOption_Exportable: ExportOption = 1
class ICertificate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('333f740c-04d8-43b3-b2-78-8c-5f-cc-9b-e5-a0')
    @winrt_commethod(6)
    def BuildChainAsync(self, certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate]) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_commethod(7)
    def BuildChainWithParametersAsync(self, certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate], parameters: Windows.Security.Cryptography.Certificates.ChainBuildingParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> c_char_p_no: ...
    @winrt_commethod(9)
    def GetHashValue(self) -> c_char_p_no: ...
    @winrt_commethod(10)
    def GetHashValueWithAlgorithm(self, hashAlgorithmName: WinRT_String) -> c_char_p_no: ...
    @winrt_commethod(11)
    def GetCertificateBlob(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Issuer(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_HasPrivateKey(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsStronglyProtected(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_ValidFrom(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(17)
    def get_ValidTo(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(18)
    def get_EnhancedKeyUsages(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(19)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_FriendlyName(self) -> WinRT_String: ...
    SerialNumber = property(get_SerialNumber, None)
    Subject = property(get_Subject, None)
    Issuer = property(get_Issuer, None)
    HasPrivateKey = property(get_HasPrivateKey, None)
    IsStronglyProtected = property(get_IsStronglyProtected, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
class ICertificate2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('17b8374c-8a25-4d96-a4-92-8f-c2-9a-c4-fd-a6')
    @winrt_commethod(6)
    def get_IsSecurityDeviceBound(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_KeyUsages(self) -> Windows.Security.Cryptography.Certificates.CertificateKeyUsages: ...
    @winrt_commethod(8)
    def get_KeyAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SignatureAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SignatureHashAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SubjectAlternativeName(self) -> Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    IsSecurityDeviceBound = property(get_IsSecurityDeviceBound, None)
    KeyUsages = property(get_KeyUsages, None)
    KeyAlgorithmName = property(get_KeyAlgorithmName, None)
    SignatureAlgorithmName = property(get_SignatureAlgorithmName, None)
    SignatureHashAlgorithmName = property(get_SignatureHashAlgorithmName, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
class ICertificate3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('be51a966-ae5f-4652-ac-e7-c6-d7-e7-72-4c-f3')
    @winrt_commethod(6)
    def get_IsPerUser(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_StoreName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_KeyStorageProviderName(self) -> WinRT_String: ...
    IsPerUser = property(get_IsPerUser, None)
    StoreName = property(get_StoreName, None)
    KeyStorageProviderName = property(get_KeyStorageProviderName, None)
class ICertificateChain(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20bf5385-3691-4501-a6-2c-fd-97-27-8b-31-ee')
    @winrt_commethod(6)
    def Validate(self) -> Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_commethod(7)
    def ValidateWithParameters(self, parameter: Windows.Security.Cryptography.Certificates.ChainValidationParameters) -> Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_commethod(8)
    def GetCertificates(self, includeRoot: Boolean) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
class ICertificateEnrollmentManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8846ef3f-a986-48fb-9f-d7-9a-ec-06-93-5b-f1')
    @winrt_commethod(6)
    def CreateRequestAsync(self, request: Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def InstallCertificateAsync(self, certificate: WinRT_String, installOption: Windows.Security.Cryptography.Certificates.InstallOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ImportPfxDataAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class ICertificateEnrollmentManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dc5b1c33-6429-4014-99-9c-5d-97-35-80-2d-1d')
    @winrt_commethod(6)
    def get_UserCertificateEnrollmentManager(self) -> Windows.Security.Cryptography.Certificates.UserCertificateEnrollmentManager: ...
    @winrt_commethod(7)
    def ImportPfxDataToKspAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    UserCertificateEnrollmentManager = property(get_UserCertificateEnrollmentManager, None)
class ICertificateEnrollmentManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fdec82be-617c-425a-b7-2d-39-8b-26-ac-72-64')
    @winrt_commethod(6)
    def ImportPfxDataToKspWithParametersAsync(self, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: Windows.Security.Cryptography.Certificates.PfxImportParameters) -> Windows.Foundation.IAsyncAction: ...
class ICertificateExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('84cf0656-a9e6-454d-8e-45-2e-a7-c4-bc-d5-3b')
    @winrt_commethod(6)
    def get_ObjectId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ObjectId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IsCritical(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsCritical(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def EncodeValue(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Value(self) -> c_char_p_no: ...
    @winrt_commethod(12)
    def put_Value(self, value: c_char_p_no) -> Void: ...
    ObjectId = property(get_ObjectId, put_ObjectId)
    IsCritical = property(get_IsCritical, put_IsCritical)
    Value = property(get_Value, put_Value)
class ICertificateFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('17b4221c-4baf-44a2-96-08-04-fb-62-b1-69-42')
    @winrt_commethod(6)
    def CreateCertificate(self, certBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Certificates.Certificate: ...
class ICertificateKeyUsages(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6ac6206f-e1cf-486a-b4-85-a6-9c-83-e4-6f-d1')
    @winrt_commethod(6)
    def get_EncipherOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_EncipherOnly(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CrlSign(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CrlSign(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_KeyCertificateSign(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_KeyCertificateSign(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_KeyAgreement(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_KeyAgreement(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_DataEncipherment(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_DataEncipherment(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_KeyEncipherment(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_KeyEncipherment(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_NonRepudiation(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_NonRepudiation(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_DigitalSignature(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_DigitalSignature(self, value: Boolean) -> Void: ...
    EncipherOnly = property(get_EncipherOnly, put_EncipherOnly)
    CrlSign = property(get_CrlSign, put_CrlSign)
    KeyCertificateSign = property(get_KeyCertificateSign, put_KeyCertificateSign)
    KeyAgreement = property(get_KeyAgreement, put_KeyAgreement)
    DataEncipherment = property(get_DataEncipherment, put_DataEncipherment)
    KeyEncipherment = property(get_KeyEncipherment, put_KeyEncipherment)
    NonRepudiation = property(get_NonRepudiation, put_NonRepudiation)
    DigitalSignature = property(get_DigitalSignature, put_DigitalSignature)
class ICertificateQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5b082a31-a728-4916-b5-ee-ff-cb-8a-cf-24-17')
    @winrt_commethod(6)
    def get_EnhancedKeyUsages(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_IssuerName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_IssuerName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Thumbprint(self) -> c_char_p_no: ...
    @winrt_commethod(12)
    def put_Thumbprint(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(13)
    def get_HardwareOnly(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_HardwareOnly(self, value: Boolean) -> Void: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    IssuerName = property(get_IssuerName, put_IssuerName)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    Thumbprint = property(get_Thumbprint, put_Thumbprint)
    HardwareOnly = property(get_HardwareOnly, put_HardwareOnly)
class ICertificateQuery2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('935a0af7-0bd9-4f75-b8-c2-e2-7a-7f-74-ee-cd')
    @winrt_commethod(6)
    def get_IncludeDuplicates(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IncludeDuplicates(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IncludeExpiredCertificates(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IncludeExpiredCertificates(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_StoreName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_StoreName(self, value: WinRT_String) -> Void: ...
    IncludeDuplicates = property(get_IncludeDuplicates, put_IncludeDuplicates)
    IncludeExpiredCertificates = property(get_IncludeExpiredCertificates, put_IncludeExpiredCertificates)
    StoreName = property(get_StoreName, put_StoreName)
class ICertificateRequestProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('487e84f6-94e2-4dce-88-33-1a-70-0a-37-a2-9a')
    @winrt_commethod(6)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Subject(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_KeyAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_KeyAlgorithmName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_KeySize(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_KeySize(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_HashAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_HashAlgorithmName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Exportable(self) -> Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_commethod(17)
    def put_Exportable(self, value: Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_commethod(18)
    def get_KeyUsages(self) -> Windows.Security.Cryptography.Certificates.EnrollKeyUsages: ...
    @winrt_commethod(19)
    def put_KeyUsages(self, value: Windows.Security.Cryptography.Certificates.EnrollKeyUsages) -> Void: ...
    @winrt_commethod(20)
    def get_KeyProtectionLevel(self) -> Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_commethod(21)
    def put_KeyProtectionLevel(self, value: Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_commethod(22)
    def get_KeyStorageProviderName(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def put_KeyStorageProviderName(self, value: WinRT_String) -> Void: ...
    Subject = property(get_Subject, put_Subject)
    KeyAlgorithmName = property(get_KeyAlgorithmName, put_KeyAlgorithmName)
    KeySize = property(get_KeySize, put_KeySize)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    Exportable = property(get_Exportable, put_Exportable)
    KeyUsages = property(get_KeyUsages, put_KeyUsages)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
class ICertificateRequestProperties2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3da0c954-d73f-4ff3-a0-a6-06-77-c0-ad-a0-5b')
    @winrt_commethod(6)
    def get_SmartcardReaderName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SmartcardReaderName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_SigningCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def put_SigningCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(10)
    def get_AttestationCredentialCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(11)
    def put_AttestationCredentialCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    SmartcardReaderName = property(get_SmartcardReaderName, put_SmartcardReaderName)
    SigningCertificate = property(get_SigningCertificate, put_SigningCertificate)
    AttestationCredentialCertificate = property(get_AttestationCredentialCertificate, put_AttestationCredentialCertificate)
class ICertificateRequestProperties3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e687f616-734d-46b1-9d-4c-6e-df-db-fc-84-5b')
    @winrt_commethod(6)
    def get_CurveName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_CurveName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_CurveParameters(self) -> c_char_p_no: ...
    @winrt_commethod(9)
    def put_CurveParameters(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(10)
    def get_ContainerNamePrefix(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ContainerNamePrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_ContainerName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_ContainerName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_UseExistingKey(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_UseExistingKey(self, value: Boolean) -> Void: ...
    CurveName = property(get_CurveName, put_CurveName)
    CurveParameters = property(get_CurveParameters, put_CurveParameters)
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    ContainerName = property(get_ContainerName, put_ContainerName)
    UseExistingKey = property(get_UseExistingKey, put_UseExistingKey)
class ICertificateRequestProperties4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e429ad2-1c61-4fea-b8-fe-13-5f-b1-9c-dc-e4')
    @winrt_commethod(6)
    def get_SuppressedDefaults(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_SubjectAlternativeName(self) -> Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.CertificateExtension]: ...
    SuppressedDefaults = property(get_SuppressedDefaults, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
    Extensions = property(get_Extensions, None)
class ICertificateStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b0bff720-344e-4331-af-14-a7-f7-a7-eb-c9-3a')
    @winrt_commethod(6)
    def Add(self, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(7)
    def Delete(self, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
class ICertificateStore2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c7e68e4a-417d-4d1a-ba-bd-15-68-7e-54-99-74')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class ICertificateStoresStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbecc739-c6fe-4de7-99-cf-74-c3-e5-96-e0-32')
    @winrt_commethod(6)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_commethod(7)
    def FindAllWithQueryAsync(self, query: Windows.Security.Cryptography.Certificates.CertificateQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_commethod(8)
    def get_TrustedRootCertificationAuthorities(self) -> Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_commethod(9)
    def get_IntermediateCertificationAuthorities(self) -> Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_commethod(10)
    def GetStoreByName(self, storeName: WinRT_String) -> Windows.Security.Cryptography.Certificates.CertificateStore: ...
    TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
    IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
class ICertificateStoresStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fa900b79-a0d4-4b8c-bc-55-c0-a3-7e-b1-41-ed')
    @winrt_commethod(6)
    def GetUserStoreByName(self, storeName: WinRT_String) -> Windows.Security.Cryptography.Certificates.UserCertificateStore: ...
class IChainBuildingParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('422ba922-7c8d-47b7-b5-9b-b1-27-03-73-3a-c3')
    @winrt_commethod(6)
    def get_EnhancedKeyUsages(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_ValidationTimestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def put_ValidationTimestamp(self, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(9)
    def get_RevocationCheckEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_RevocationCheckEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_NetworkRetrievalEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_NetworkRetrievalEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_AuthorityInformationAccessEnabled(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_AuthorityInformationAccessEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_CurrentTimeValidationEnabled(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_CurrentTimeValidationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_ExclusiveTrustRoots(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.Certificate]: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    ValidationTimestamp = property(get_ValidationTimestamp, put_ValidationTimestamp)
    RevocationCheckEnabled = property(get_RevocationCheckEnabled, put_RevocationCheckEnabled)
    NetworkRetrievalEnabled = property(get_NetworkRetrievalEnabled, put_NetworkRetrievalEnabled)
    AuthorityInformationAccessEnabled = property(get_AuthorityInformationAccessEnabled, put_AuthorityInformationAccessEnabled)
    CurrentTimeValidationEnabled = property(get_CurrentTimeValidationEnabled, put_CurrentTimeValidationEnabled)
    ExclusiveTrustRoots = property(get_ExclusiveTrustRoots, None)
class IChainValidationParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c4743b4a-7eb0-4b56-a0-40-b9-c8-e6-55-dd-f3')
    @winrt_commethod(6)
    def get_CertificateChainPolicy(self) -> Windows.Security.Cryptography.Certificates.CertificateChainPolicy: ...
    @winrt_commethod(7)
    def put_CertificateChainPolicy(self, value: Windows.Security.Cryptography.Certificates.CertificateChainPolicy) -> Void: ...
    @winrt_commethod(8)
    def get_ServerDnsName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def put_ServerDnsName(self, value: Windows.Networking.HostName) -> Void: ...
    CertificateChainPolicy = property(get_CertificateChainPolicy, put_CertificateChainPolicy)
    ServerDnsName = property(get_ServerDnsName, put_ServerDnsName)
class ICmsAttachedSignature(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('61899d9d-3757-4ecb-bd-dc-0c-a3-57-d7-a9-36')
    @winrt_commethod(6)
    def get_Certificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(7)
    def get_Content(self) -> c_char_p_no: ...
    @winrt_commethod(8)
    def get_Signers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_commethod(9)
    def VerifySignature(self) -> Windows.Security.Cryptography.Certificates.SignatureValidationResult: ...
    Certificates = property(get_Certificates, None)
    Content = property(get_Content, None)
    Signers = property(get_Signers, None)
class ICmsAttachedSignatureFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d0c8fc15-f757-4c64-a3-62-52-cc-1c-77-cf-fb')
    @winrt_commethod(6)
    def CreateCmsAttachedSignature(self, inputBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Certificates.CmsAttachedSignature: ...
class ICmsAttachedSignatureStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('87989c8e-b0ad-498d-a7-f5-78-b5-9b-ce-4b-36')
    @winrt_commethod(6)
    def GenerateSignatureAsync(self, data: Windows.Storage.Streams.IBuffer, signers: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
class ICmsDetachedSignature(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0f1ef154-f65e-4536-83-39-59-44-08-1d-b2-ca')
    @winrt_commethod(6)
    def get_Certificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(7)
    def get_Signers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_commethod(8)
    def VerifySignatureAsync(self, data: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.Cryptography.Certificates.SignatureValidationResult]: ...
    Certificates = property(get_Certificates, None)
    Signers = property(get_Signers, None)
class ICmsDetachedSignatureFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c4ab3503-ae7f-4387-ad-19-00-f1-50-e4-8e-bb')
    @winrt_commethod(6)
    def CreateCmsDetachedSignature(self, inputBlob: Windows.Storage.Streams.IBuffer) -> Windows.Security.Cryptography.Certificates.CmsDetachedSignature: ...
class ICmsDetachedSignatureStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d114cfd-bf9b-4682-9b-e6-91-f5-7c-05-38-08')
    @winrt_commethod(6)
    def GenerateSignatureAsync(self, data: Windows.Storage.Streams.IInputStream, signers: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: Windows.Foundation.Collections.IIterable[Windows.Security.Cryptography.Certificates.Certificate]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
class ICmsSignerInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('50d020db-1d2f-4c1a-b5-c5-d0-18-8f-f9-1f-47')
    @winrt_commethod(6)
    def get_Certificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def put_Certificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(8)
    def get_HashAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_HashAlgorithmName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_TimestampInfo(self) -> Windows.Security.Cryptography.Certificates.CmsTimestampInfo: ...
    Certificate = property(get_Certificate, put_Certificate)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    TimestampInfo = property(get_TimestampInfo, None)
class ICmsTimestampInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f5f00f2-2c18-4f88-84-35-c5-34-08-60-76-f5')
    @winrt_commethod(6)
    def get_SigningCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_Certificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    SigningCertificate = property(get_SigningCertificate, None)
    Certificates = property(get_Certificates, None)
    Timestamp = property(get_Timestamp, None)
class IKeyAlgorithmNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('479065d7-7ac7-4581-8c-3b-d0-70-27-14-04-48')
    @winrt_commethod(6)
    def get_Rsa(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Dsa(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Ecdh256(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Ecdh384(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Ecdh521(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Ecdsa256(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Ecdsa384(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Ecdsa521(self) -> WinRT_String: ...
    Rsa = property(get_Rsa, None)
    Dsa = property(get_Dsa, None)
    Ecdh256 = property(get_Ecdh256, None)
    Ecdh384 = property(get_Ecdh384, None)
    Ecdh521 = property(get_Ecdh521, None)
    Ecdsa256 = property(get_Ecdsa256, None)
    Ecdsa384 = property(get_Ecdsa384, None)
    Ecdsa521 = property(get_Ecdsa521, None)
class IKeyAlgorithmNamesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c99b5686-e1fd-4a4a-89-3d-a2-6f-33-dd-8b-b4')
    @winrt_commethod(6)
    def get_Ecdsa(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Ecdh(self) -> WinRT_String: ...
    Ecdsa = property(get_Ecdsa, None)
    Ecdh = property(get_Ecdh, None)
class IKeyAttestationHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1648e246-f644-4326-88-be-3a-f1-02-d3-0e-0c')
    @winrt_commethod(6)
    def DecryptTpmAttestationCredentialAsync(self, credential: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def GetTpmAttestationCredentialId(self, credential: WinRT_String) -> WinRT_String: ...
class IKeyAttestationHelperStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9c590b2c-a6c6-4a5e-9e-64-e8-5d-52-79-df-97')
    @winrt_commethod(6)
    def DecryptTpmAttestationCredentialWithContainerNameAsync(self, credential: WinRT_String, containerName: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class IKeyStorageProviderNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('af186ae0-5529-4602-bd-94-0a-ab-91-95-7b-5c')
    @winrt_commethod(6)
    def get_SoftwareKeyStorageProvider(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SmartcardKeyStorageProvider(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PlatformKeyStorageProvider(self) -> WinRT_String: ...
    SoftwareKeyStorageProvider = property(get_SoftwareKeyStorageProvider, None)
    SmartcardKeyStorageProvider = property(get_SmartcardKeyStorageProvider, None)
    PlatformKeyStorageProvider = property(get_PlatformKeyStorageProvider, None)
class IKeyStorageProviderNamesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('262d743d-9c2e-41cc-88-12-c4-d9-71-dd-7c-60')
    @winrt_commethod(6)
    def get_PassportKeyStorageProvider(self) -> WinRT_String: ...
    PassportKeyStorageProvider = property(get_PassportKeyStorageProvider, None)
class IPfxImportParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('680d3511-9a08-47c8-86-4a-2e-dd-4d-8e-b4-6c')
    @winrt_commethod(6)
    def get_Exportable(self) -> Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_commethod(7)
    def put_Exportable(self, value: Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_commethod(8)
    def get_KeyProtectionLevel(self) -> Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_commethod(9)
    def put_KeyProtectionLevel(self, value: Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_commethod(10)
    def get_InstallOptions(self) -> Windows.Security.Cryptography.Certificates.InstallOptions: ...
    @winrt_commethod(11)
    def put_InstallOptions(self, value: Windows.Security.Cryptography.Certificates.InstallOptions) -> Void: ...
    @winrt_commethod(12)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_KeyStorageProviderName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_KeyStorageProviderName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_ContainerNamePrefix(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_ContainerNamePrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_ReaderName(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_ReaderName(self, value: WinRT_String) -> Void: ...
    Exportable = property(get_Exportable, put_Exportable)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    InstallOptions = property(get_InstallOptions, put_InstallOptions)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    ReaderName = property(get_ReaderName, put_ReaderName)
class IStandardCertificateStoreNamesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c154adb-a496-41f8-8f-e5-9e-96-f3-6e-fb-f8')
    @winrt_commethod(6)
    def get_Personal(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TrustedRootCertificationAuthorities(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IntermediateCertificationAuthorities(self) -> WinRT_String: ...
    Personal = property(get_Personal, None)
    TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
    IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
class ISubjectAlternativeNameInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('582859f1-569d-4c20-be-7b-4e-1c-9a-0b-c5-2b')
    @winrt_commethod(6)
    def get_EmailName(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_IPAddress(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Url(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DnsName(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_DistinguishedName(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PrincipalName(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    EmailName = property(get_EmailName, None)
    IPAddress = property(get_IPAddress, None)
    Url = property(get_Url, None)
    DnsName = property(get_DnsName, None)
    DistinguishedName = property(get_DistinguishedName, None)
    PrincipalName = property(get_PrincipalName, None)
class ISubjectAlternativeNameInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('437a78c6-1c51-41ea-b3-4a-3d-65-43-98-a3-70')
    @winrt_commethod(6)
    def get_EmailNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_IPAddresses(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Urls(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DnsNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(10)
    def get_DistinguishedNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PrincipalNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(12)
    def get_Extension(self) -> Windows.Security.Cryptography.Certificates.CertificateExtension: ...
    EmailNames = property(get_EmailNames, None)
    IPAddresses = property(get_IPAddresses, None)
    Urls = property(get_Urls, None)
    DnsNames = property(get_DnsNames, None)
    DistinguishedNames = property(get_DistinguishedNames, None)
    PrincipalNames = property(get_PrincipalNames, None)
    Extension = property(get_Extension, None)
class IUserCertificateEnrollmentManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96313718-22e1-4819-b2-0b-ab-46-a6-ec-a0-6e')
    @winrt_commethod(6)
    def CreateRequestAsync(self, request: Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def InstallCertificateAsync(self, certificate: WinRT_String, installOption: Windows.Security.Cryptography.Certificates.InstallOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ImportPfxDataAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ImportPfxDataToKspAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IUserCertificateEnrollmentManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0dad9cb1-65de-492a-b8-6d-fc-5c-48-2c-37-47')
    @winrt_commethod(6)
    def ImportPfxDataToKspWithParametersAsync(self, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: Windows.Security.Cryptography.Certificates.PfxImportParameters) -> Windows.Foundation.IAsyncAction: ...
class IUserCertificateStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c9fb1d83-789f-4b4e-91-80-04-5a-75-7a-ac-6d')
    @winrt_commethod(6)
    def RequestAddAsync(self, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RequestDeleteAsync(self, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
InstallOptions = UInt32
InstallOptions_None: InstallOptions = 0
InstallOptions_DeleteExpired: InstallOptions = 1
class KeyAlgorithmNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.KeyAlgorithmNames'
    @winrt_classmethod
    def get_Ecdsa(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rsa(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Dsa(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh256(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh384(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh521(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdsa256(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdsa384(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdsa521(cls: Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    Ecdsa = property(get_Ecdsa, None)
    Ecdh = property(get_Ecdh, None)
    Rsa = property(get_Rsa, None)
    Dsa = property(get_Dsa, None)
    Ecdh256 = property(get_Ecdh256, None)
    Ecdh384 = property(get_Ecdh384, None)
    Ecdh521 = property(get_Ecdh521, None)
    Ecdsa256 = property(get_Ecdsa256, None)
    Ecdsa384 = property(get_Ecdsa384, None)
    Ecdsa521 = property(get_Ecdsa521, None)
class KeyAttestationHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.KeyAttestationHelper'
    @winrt_classmethod
    def DecryptTpmAttestationCredentialWithContainerNameAsync(cls: Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics2, credential: WinRT_String, containerName: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def DecryptTpmAttestationCredentialAsync(cls: Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics, credential: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetTpmAttestationCredentialId(cls: Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics, credential: WinRT_String) -> WinRT_String: ...
KeyProtectionLevel = Int32
KeyProtectionLevel_NoConsent: KeyProtectionLevel = 0
KeyProtectionLevel_ConsentOnly: KeyProtectionLevel = 1
KeyProtectionLevel_ConsentWithPassword: KeyProtectionLevel = 2
KeyProtectionLevel_ConsentWithFingerprint: KeyProtectionLevel = 3
KeySize = Int32
KeySize_Invalid: KeySize = 0
KeySize_Rsa2048: KeySize = 2048
KeySize_Rsa4096: KeySize = 4096
class KeyStorageProviderNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.KeyStorageProviderNames'
    @winrt_classmethod
    def get_PassportKeyStorageProvider(cls: Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_SoftwareKeyStorageProvider(cls: Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SmartcardKeyStorageProvider(cls: Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PlatformKeyStorageProvider(cls: Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics) -> WinRT_String: ...
    PassportKeyStorageProvider = property(get_PassportKeyStorageProvider, None)
    SoftwareKeyStorageProvider = property(get_SoftwareKeyStorageProvider, None)
    SmartcardKeyStorageProvider = property(get_SmartcardKeyStorageProvider, None)
    PlatformKeyStorageProvider = property(get_PlatformKeyStorageProvider, None)
class PfxImportParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.PfxImportParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.PfxImportParameters: ...
    @winrt_mixinmethod
    def get_Exportable(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_mixinmethod
    def put_Exportable(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_mixinmethod
    def get_KeyProtectionLevel(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_mixinmethod
    def put_KeyProtectionLevel(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_InstallOptions(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> Windows.Security.Cryptography.Certificates.InstallOptions: ...
    @winrt_mixinmethod
    def put_InstallOptions(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: Windows.Security.Cryptography.Certificates.InstallOptions) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KeyStorageProviderName(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_KeyStorageProviderName(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContainerNamePrefix(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContainerNamePrefix(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ReaderName(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReaderName(self: Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    Exportable = property(get_Exportable, put_Exportable)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    InstallOptions = property(get_InstallOptions, put_InstallOptions)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    ReaderName = property(get_ReaderName, put_ReaderName)
SignatureValidationResult = Int32
SignatureValidationResult_Success: SignatureValidationResult = 0
SignatureValidationResult_InvalidParameter: SignatureValidationResult = 1
SignatureValidationResult_BadMessage: SignatureValidationResult = 2
SignatureValidationResult_InvalidSignature: SignatureValidationResult = 3
SignatureValidationResult_OtherErrors: SignatureValidationResult = 4
class StandardCertificateStoreNames(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.StandardCertificateStoreNames'
    @winrt_classmethod
    def get_Personal(cls: Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TrustedRootCertificationAuthorities(cls: Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IntermediateCertificationAuthorities(cls: Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics) -> WinRT_String: ...
    Personal = property(get_Personal, None)
    TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
    IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
class SubjectAlternativeNameInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_mixinmethod
    def get_EmailName(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IPAddress(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Url(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DnsName(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DistinguishedName(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PrincipalName(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_EmailNames(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IPAddresses(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Urls(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DnsNames(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DistinguishedNames(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PrincipalNames(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Extension(self: Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> Windows.Security.Cryptography.Certificates.CertificateExtension: ...
    EmailName = property(get_EmailName, None)
    IPAddress = property(get_IPAddress, None)
    Url = property(get_Url, None)
    DnsName = property(get_DnsName, None)
    DistinguishedName = property(get_DistinguishedName, None)
    PrincipalName = property(get_PrincipalName, None)
    EmailNames = property(get_EmailNames, None)
    IPAddresses = property(get_IPAddresses, None)
    Urls = property(get_Urls, None)
    DnsNames = property(get_DnsNames, None)
    DistinguishedNames = property(get_DistinguishedNames, None)
    PrincipalNames = property(get_PrincipalNames, None)
    Extension = property(get_Extension, None)
class UserCertificateEnrollmentManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.UserCertificateEnrollmentManager'
    @winrt_mixinmethod
    def CreateRequestAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, request: Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def InstallCertificateAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, certificate: WinRT_String, installOption: Windows.Security.Cryptography.Certificates.InstallOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportPfxDataAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportPfxDataToKspAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, pfxData: WinRT_String, password: WinRT_String, exportable: Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportPfxDataToKspWithParametersAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager2, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: Windows.Security.Cryptography.Certificates.PfxImportParameters) -> Windows.Foundation.IAsyncAction: ...
class UserCertificateStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.Certificates.UserCertificateStore'
    @winrt_mixinmethod
    def RequestAddAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateStore, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestDeleteAsync(self: Windows.Security.Cryptography.Certificates.IUserCertificateStore, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Security.Cryptography.Certificates.IUserCertificateStore) -> WinRT_String: ...
    Name = property(get_Name, None)
make_head(_module, 'Certificate')
make_head(_module, 'CertificateChain')
make_head(_module, 'CertificateEnrollmentManager')
make_head(_module, 'CertificateExtension')
make_head(_module, 'CertificateKeyUsages')
make_head(_module, 'CertificateQuery')
make_head(_module, 'CertificateRequestProperties')
make_head(_module, 'CertificateStore')
make_head(_module, 'CertificateStores')
make_head(_module, 'ChainBuildingParameters')
make_head(_module, 'ChainValidationParameters')
make_head(_module, 'CmsAttachedSignature')
make_head(_module, 'CmsDetachedSignature')
make_head(_module, 'CmsSignerInfo')
make_head(_module, 'CmsTimestampInfo')
make_head(_module, 'ICertificate')
make_head(_module, 'ICertificate2')
make_head(_module, 'ICertificate3')
make_head(_module, 'ICertificateChain')
make_head(_module, 'ICertificateEnrollmentManagerStatics')
make_head(_module, 'ICertificateEnrollmentManagerStatics2')
make_head(_module, 'ICertificateEnrollmentManagerStatics3')
make_head(_module, 'ICertificateExtension')
make_head(_module, 'ICertificateFactory')
make_head(_module, 'ICertificateKeyUsages')
make_head(_module, 'ICertificateQuery')
make_head(_module, 'ICertificateQuery2')
make_head(_module, 'ICertificateRequestProperties')
make_head(_module, 'ICertificateRequestProperties2')
make_head(_module, 'ICertificateRequestProperties3')
make_head(_module, 'ICertificateRequestProperties4')
make_head(_module, 'ICertificateStore')
make_head(_module, 'ICertificateStore2')
make_head(_module, 'ICertificateStoresStatics')
make_head(_module, 'ICertificateStoresStatics2')
make_head(_module, 'IChainBuildingParameters')
make_head(_module, 'IChainValidationParameters')
make_head(_module, 'ICmsAttachedSignature')
make_head(_module, 'ICmsAttachedSignatureFactory')
make_head(_module, 'ICmsAttachedSignatureStatics')
make_head(_module, 'ICmsDetachedSignature')
make_head(_module, 'ICmsDetachedSignatureFactory')
make_head(_module, 'ICmsDetachedSignatureStatics')
make_head(_module, 'ICmsSignerInfo')
make_head(_module, 'ICmsTimestampInfo')
make_head(_module, 'IKeyAlgorithmNamesStatics')
make_head(_module, 'IKeyAlgorithmNamesStatics2')
make_head(_module, 'IKeyAttestationHelperStatics')
make_head(_module, 'IKeyAttestationHelperStatics2')
make_head(_module, 'IKeyStorageProviderNamesStatics')
make_head(_module, 'IKeyStorageProviderNamesStatics2')
make_head(_module, 'IPfxImportParameters')
make_head(_module, 'IStandardCertificateStoreNamesStatics')
make_head(_module, 'ISubjectAlternativeNameInfo')
make_head(_module, 'ISubjectAlternativeNameInfo2')
make_head(_module, 'IUserCertificateEnrollmentManager')
make_head(_module, 'IUserCertificateEnrollmentManager2')
make_head(_module, 'IUserCertificateStore')
make_head(_module, 'KeyAlgorithmNames')
make_head(_module, 'KeyAttestationHelper')
make_head(_module, 'KeyStorageProviderNames')
make_head(_module, 'PfxImportParameters')
make_head(_module, 'StandardCertificateStoreNames')
make_head(_module, 'SubjectAlternativeNameInfo')
make_head(_module, 'UserCertificateEnrollmentManager')
make_head(_module, 'UserCertificateStore')
