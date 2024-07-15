from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class Certificate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificate
    _classid_ = 'Windows.Security.Cryptography.Certificates.Certificate'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.Certificate.CreateCertificate(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateCertificate(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateFactory, certBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def BuildChainAsync(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate, certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_mixinmethod
    def BuildChainWithParametersAsync(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate, certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate], parameters: win32more.Windows.Security.Cryptography.Certificates.ChainBuildingParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def GetHashValue(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def GetHashValueWithAlgorithm(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate, hashAlgorithmName: WinRT_String) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def GetCertificateBlob(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Issuer(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasPrivateKey(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStronglyProtected(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValidFrom(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ValidTo(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EnhancedKeyUsages(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsSecurityDeviceBound(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate2) -> Boolean: ...
    @winrt_mixinmethod
    def get_KeyUsages(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate2) -> win32more.Windows.Security.Cryptography.Certificates.CertificateKeyUsages: ...
    @winrt_mixinmethod
    def get_KeyAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SignatureAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SignatureHashAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SubjectAlternativeName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate2) -> win32more.Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_mixinmethod
    def get_IsPerUser(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate3) -> Boolean: ...
    @winrt_mixinmethod
    def get_StoreName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_KeyStorageProviderName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificate3) -> WinRT_String: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HasPrivateKey = property(get_HasPrivateKey, None)
    IsPerUser = property(get_IsPerUser, None)
    IsSecurityDeviceBound = property(get_IsSecurityDeviceBound, None)
    IsStronglyProtected = property(get_IsStronglyProtected, None)
    Issuer = property(get_Issuer, None)
    KeyAlgorithmName = property(get_KeyAlgorithmName, None)
    KeyStorageProviderName = property(get_KeyStorageProviderName, None)
    KeyUsages = property(get_KeyUsages, None)
    SerialNumber = property(get_SerialNumber, None)
    SignatureAlgorithmName = property(get_SignatureAlgorithmName, None)
    SignatureHashAlgorithmName = property(get_SignatureHashAlgorithmName, None)
    StoreName = property(get_StoreName, None)
    Subject = property(get_Subject, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
class CertificateChain(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificateChain
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateChain'
    @winrt_mixinmethod
    def Validate(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateChain) -> win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_mixinmethod
    def ValidateWithParameters(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateChain, parameter: win32more.Windows.Security.Cryptography.Certificates.ChainValidationParameters) -> win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_mixinmethod
    def GetCertificates(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateChain, includeRoot: Boolean) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
class CertificateChainPolicy(Enum, Int32):
    Base = 0
    Ssl = 1
    NTAuthentication = 2
    MicrosoftRoot = 3
class _CertificateEnrollmentManager_Meta_(ComPtr.__class__):
    pass
class CertificateEnrollmentManager(ComPtr, metaclass=_CertificateEnrollmentManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateEnrollmentManager'
    @winrt_classmethod
    def ImportPfxDataToKspWithParametersAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics3, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: win32more.Windows.Security.Cryptography.Certificates.PfxImportParameters) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_UserCertificateEnrollmentManager(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics2) -> win32more.Windows.Security.Cryptography.Certificates.UserCertificateEnrollmentManager: ...
    @winrt_classmethod
    def ImportPfxDataToKspAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics2, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def CreateRequestAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics, request: win32more.Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def InstallCertificateAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics, certificate: WinRT_String, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ImportPfxDataAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    _CertificateEnrollmentManager_Meta_.UserCertificateEnrollmentManager = property(get_UserCertificateEnrollmentManager, None)
class CertificateExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateExtension'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CertificateExtension.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.CertificateExtension: ...
    @winrt_mixinmethod
    def get_ObjectId(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ObjectId(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsCritical(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCritical(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def EncodeValue(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateExtension, value: PassArray[Byte]) -> Void: ...
    IsCritical = property(get_IsCritical, put_IsCritical)
    ObjectId = property(get_ObjectId, put_ObjectId)
    Value = property(get_Value, put_Value)
class CertificateKeyUsages(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateKeyUsages'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CertificateKeyUsages.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.CertificateKeyUsages: ...
    @winrt_mixinmethod
    def get_EncipherOnly(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_EncipherOnly(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrlSign(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrlSign(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyCertificateSign(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeyCertificateSign(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyAgreement(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeyAgreement(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DataEncipherment(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_DataEncipherment(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyEncipherment(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeyEncipherment(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NonRepudiation(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_NonRepudiation(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DigitalSignature(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages) -> Boolean: ...
    @winrt_mixinmethod
    def put_DigitalSignature(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateKeyUsages, value: Boolean) -> Void: ...
    CrlSign = property(get_CrlSign, put_CrlSign)
    DataEncipherment = property(get_DataEncipherment, put_DataEncipherment)
    DigitalSignature = property(get_DigitalSignature, put_DigitalSignature)
    EncipherOnly = property(get_EncipherOnly, put_EncipherOnly)
    KeyAgreement = property(get_KeyAgreement, put_KeyAgreement)
    KeyCertificateSign = property(get_KeyCertificateSign, put_KeyCertificateSign)
    KeyEncipherment = property(get_KeyEncipherment, put_KeyEncipherment)
    NonRepudiation = property(get_NonRepudiation, put_NonRepudiation)
class CertificateQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateQuery'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CertificateQuery.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.CertificateQuery: ...
    @winrt_mixinmethod
    def get_EnhancedKeyUsages(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IssuerName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IssuerName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbprint(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def put_Thumbprint(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery, value: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareOnly(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery) -> Boolean: ...
    @winrt_mixinmethod
    def put_HardwareOnly(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeDuplicates(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeDuplicates(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeExpiredCertificates(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeExpiredCertificates(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StoreName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StoreName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateQuery2, value: WinRT_String) -> Void: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HardwareOnly = property(get_HardwareOnly, put_HardwareOnly)
    IncludeDuplicates = property(get_IncludeDuplicates, put_IncludeDuplicates)
    IncludeExpiredCertificates = property(get_IncludeExpiredCertificates, put_IncludeExpiredCertificates)
    IssuerName = property(get_IssuerName, put_IssuerName)
    StoreName = property(get_StoreName, put_StoreName)
    Thumbprint = property(get_Thumbprint, put_Thumbprint)
class CertificateRequestProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateRequestProperties'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CertificateRequestProperties.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.CertificateRequestProperties: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KeyAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_KeyAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KeySize(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_KeySize(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HashAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HashAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Exportable(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> win32more.Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_mixinmethod
    def put_Exportable(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: win32more.Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_mixinmethod
    def get_KeyUsages(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> win32more.Windows.Security.Cryptography.Certificates.EnrollKeyUsages: ...
    @winrt_mixinmethod
    def put_KeyUsages(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: win32more.Windows.Security.Cryptography.Certificates.EnrollKeyUsages) -> Void: ...
    @winrt_mixinmethod
    def get_KeyProtectionLevel(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_mixinmethod
    def put_KeyProtectionLevel(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_KeyStorageProviderName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_KeyStorageProviderName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SmartcardReaderName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SmartcardReaderName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SigningCertificate(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_SigningCertificate(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_AttestationCredentialCertificate(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_AttestationCredentialCertificate(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_CurveName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CurveName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CurveParameters(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def put_CurveParameters(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def get_ContainerNamePrefix(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContainerNamePrefix(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContainerName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContainerName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UseExistingKey(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseExistingKey(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressedDefaults(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SubjectAlternativeName(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4) -> win32more.Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_mixinmethod
    def get_Extensions(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.CertificateExtension]: ...
    AttestationCredentialCertificate = property(get_AttestationCredentialCertificate, put_AttestationCredentialCertificate)
    ContainerName = property(get_ContainerName, put_ContainerName)
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    CurveName = property(get_CurveName, put_CurveName)
    CurveParameters = property(get_CurveParameters, put_CurveParameters)
    Exportable = property(get_Exportable, put_Exportable)
    Extensions = property(get_Extensions, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    KeyAlgorithmName = property(get_KeyAlgorithmName, put_KeyAlgorithmName)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    KeySize = property(get_KeySize, put_KeySize)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    KeyUsages = property(get_KeyUsages, put_KeyUsages)
    SigningCertificate = property(get_SigningCertificate, put_SigningCertificate)
    SmartcardReaderName = property(get_SmartcardReaderName, put_SmartcardReaderName)
    Subject = property(get_Subject, put_Subject)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
    SuppressedDefaults = property(get_SuppressedDefaults, None)
    UseExistingKey = property(get_UseExistingKey, put_UseExistingKey)
class CertificateStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICertificateStore
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateStore'
    @winrt_mixinmethod
    def Add(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateStore, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def Delete(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateStore, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Security.Cryptography.Certificates.ICertificateStore2) -> WinRT_String: ...
    Name = property(get_Name, None)
class _CertificateStores_Meta_(ComPtr.__class__):
    pass
class CertificateStores(ComPtr, metaclass=_CertificateStores_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.CertificateStores'
    @winrt_classmethod
    def GetUserStoreByName(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateStoresStatics2, storeName: WinRT_String) -> win32more.Windows.Security.Cryptography.Certificates.UserCertificateStore: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateStoresStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_classmethod
    def FindAllWithQueryAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateStoresStatics, query: win32more.Windows.Security.Cryptography.Certificates.CertificateQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_classmethod
    def get_TrustedRootCertificationAuthorities(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateStoresStatics) -> win32more.Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_classmethod
    def get_IntermediateCertificationAuthorities(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateStoresStatics) -> win32more.Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_classmethod
    def GetStoreByName(cls: win32more.Windows.Security.Cryptography.Certificates.ICertificateStoresStatics, storeName: WinRT_String) -> win32more.Windows.Security.Cryptography.Certificates.CertificateStore: ...
    _CertificateStores_Meta_.IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
    _CertificateStores_Meta_.TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
class ChainBuildingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters
    _classid_ = 'Windows.Security.Cryptography.Certificates.ChainBuildingParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.ChainBuildingParameters.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.ChainBuildingParameters: ...
    @winrt_mixinmethod
    def get_EnhancedKeyUsages(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ValidationTimestamp(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_ValidationTimestamp(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_RevocationCheckEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_RevocationCheckEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NetworkRetrievalEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_NetworkRetrievalEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AuthorityInformationAccessEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_AuthorityInformationAccessEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentTimeValidationEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_CurrentTimeValidationEnabled(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExclusiveTrustRoots(self: win32more.Windows.Security.Cryptography.Certificates.IChainBuildingParameters) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    AuthorityInformationAccessEnabled = property(get_AuthorityInformationAccessEnabled, put_AuthorityInformationAccessEnabled)
    CurrentTimeValidationEnabled = property(get_CurrentTimeValidationEnabled, put_CurrentTimeValidationEnabled)
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    ExclusiveTrustRoots = property(get_ExclusiveTrustRoots, None)
    NetworkRetrievalEnabled = property(get_NetworkRetrievalEnabled, put_NetworkRetrievalEnabled)
    RevocationCheckEnabled = property(get_RevocationCheckEnabled, put_RevocationCheckEnabled)
    ValidationTimestamp = property(get_ValidationTimestamp, put_ValidationTimestamp)
class ChainValidationParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.IChainValidationParameters
    _classid_ = 'Windows.Security.Cryptography.Certificates.ChainValidationParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.ChainValidationParameters.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.ChainValidationParameters: ...
    @winrt_mixinmethod
    def get_CertificateChainPolicy(self: win32more.Windows.Security.Cryptography.Certificates.IChainValidationParameters) -> win32more.Windows.Security.Cryptography.Certificates.CertificateChainPolicy: ...
    @winrt_mixinmethod
    def put_CertificateChainPolicy(self: win32more.Windows.Security.Cryptography.Certificates.IChainValidationParameters, value: win32more.Windows.Security.Cryptography.Certificates.CertificateChainPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_ServerDnsName(self: win32more.Windows.Security.Cryptography.Certificates.IChainValidationParameters) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_ServerDnsName(self: win32more.Windows.Security.Cryptography.Certificates.IChainValidationParameters, value: win32more.Windows.Networking.HostName) -> Void: ...
    CertificateChainPolicy = property(get_CertificateChainPolicy, put_CertificateChainPolicy)
    ServerDnsName = property(get_ServerDnsName, put_ServerDnsName)
class ChainValidationResult(Enum, Int32):
    Success = 0
    Untrusted = 1
    Revoked = 2
    Expired = 3
    IncompleteChain = 4
    InvalidSignature = 5
    WrongUsage = 6
    InvalidName = 7
    InvalidCertificateAuthorityPolicy = 8
    BasicConstraintsError = 9
    UnknownCriticalExtension = 10
    RevocationInformationMissing = 11
    RevocationFailure = 12
    OtherErrors = 13
class CmsAttachedSignature(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignature
    _classid_ = 'Windows.Security.Cryptography.Certificates.CmsAttachedSignature'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CmsAttachedSignature.CreateCmsAttachedSignature(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateCmsAttachedSignature(cls: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignatureFactory, inputBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Certificates.CmsAttachedSignature: ...
    @winrt_mixinmethod
    def get_Certificates(self: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_Signers(self: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_mixinmethod
    def VerifySignature(self: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignature) -> win32more.Windows.Security.Cryptography.Certificates.SignatureValidationResult: ...
    @winrt_classmethod
    def GenerateSignatureAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICmsAttachedSignatureStatics, data: win32more.Windows.Storage.Streams.IBuffer, signers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    Certificates = property(get_Certificates, None)
    Content = property(get_Content, None)
    Signers = property(get_Signers, None)
class CmsDetachedSignature(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICmsDetachedSignature
    _classid_ = 'Windows.Security.Cryptography.Certificates.CmsDetachedSignature'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CmsDetachedSignature.CreateCmsDetachedSignature(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateCmsDetachedSignature(cls: win32more.Windows.Security.Cryptography.Certificates.ICmsDetachedSignatureFactory, inputBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Certificates.CmsDetachedSignature: ...
    @winrt_mixinmethod
    def get_Certificates(self: win32more.Windows.Security.Cryptography.Certificates.ICmsDetachedSignature) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def get_Signers(self: win32more.Windows.Security.Cryptography.Certificates.ICmsDetachedSignature) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_mixinmethod
    def VerifySignatureAsync(self: win32more.Windows.Security.Cryptography.Certificates.ICmsDetachedSignature, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Certificates.SignatureValidationResult]: ...
    @winrt_classmethod
    def GenerateSignatureAsync(cls: win32more.Windows.Security.Cryptography.Certificates.ICmsDetachedSignatureStatics, data: win32more.Windows.Storage.Streams.IInputStream, signers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    Certificates = property(get_Certificates, None)
    Signers = property(get_Signers, None)
class CmsSignerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICmsSignerInfo
    _classid_ = 'Windows.Security.Cryptography.Certificates.CmsSignerInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo: ...
    @winrt_mixinmethod
    def get_Certificate(self: win32more.Windows.Security.Cryptography.Certificates.ICmsSignerInfo) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_Certificate(self: win32more.Windows.Security.Cryptography.Certificates.ICmsSignerInfo, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_HashAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICmsSignerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HashAlgorithmName(self: win32more.Windows.Security.Cryptography.Certificates.ICmsSignerInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TimestampInfo(self: win32more.Windows.Security.Cryptography.Certificates.ICmsSignerInfo) -> win32more.Windows.Security.Cryptography.Certificates.CmsTimestampInfo: ...
    Certificate = property(get_Certificate, put_Certificate)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    TimestampInfo = property(get_TimestampInfo, None)
class CmsTimestampInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ICmsTimestampInfo
    _classid_ = 'Windows.Security.Cryptography.Certificates.CmsTimestampInfo'
    @winrt_mixinmethod
    def get_SigningCertificate(self: win32more.Windows.Security.Cryptography.Certificates.ICmsTimestampInfo) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_Certificates(self: win32more.Windows.Security.Cryptography.Certificates.ICmsTimestampInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Security.Cryptography.Certificates.ICmsTimestampInfo) -> win32more.Windows.Foundation.DateTime: ...
    Certificates = property(get_Certificates, None)
    SigningCertificate = property(get_SigningCertificate, None)
    Timestamp = property(get_Timestamp, None)
class EnrollKeyUsages(Enum, UInt32):
    None_ = 0
    Decryption = 1
    Signing = 2
    KeyAgreement = 4
    All = 16777215
class ExportOption(Enum, Int32):
    NotExportable = 0
    Exportable = 1
class ICertificate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificate'
    _iid_ = Guid('{333f740c-04d8-43b3-b278-8c5fcc9be5a0}')
    @winrt_commethod(6)
    def BuildChainAsync(self, certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_commethod(7)
    def BuildChainWithParametersAsync(self, certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate], parameters: win32more.Windows.Security.Cryptography.Certificates.ChainBuildingParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Certificates.CertificateChain]: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(9)
    def GetHashValue(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(10)
    def GetHashValueWithAlgorithm(self, hashAlgorithmName: WinRT_String) -> ReceiveArray[Byte]: ...
    @winrt_commethod(11)
    def GetCertificateBlob(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Issuer(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_HasPrivateKey(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsStronglyProtected(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_ValidFrom(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(17)
    def get_ValidTo(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(18)
    def get_EnhancedKeyUsages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(19)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_FriendlyName(self) -> WinRT_String: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HasPrivateKey = property(get_HasPrivateKey, None)
    IsStronglyProtected = property(get_IsStronglyProtected, None)
    Issuer = property(get_Issuer, None)
    SerialNumber = property(get_SerialNumber, None)
    Subject = property(get_Subject, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
class ICertificate2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificate2'
    _iid_ = Guid('{17b8374c-8a25-4d96-a492-8fc29ac4fda6}')
    @winrt_commethod(6)
    def get_IsSecurityDeviceBound(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_KeyUsages(self) -> win32more.Windows.Security.Cryptography.Certificates.CertificateKeyUsages: ...
    @winrt_commethod(8)
    def get_KeyAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SignatureAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SignatureHashAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SubjectAlternativeName(self) -> win32more.Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    IsSecurityDeviceBound = property(get_IsSecurityDeviceBound, None)
    KeyAlgorithmName = property(get_KeyAlgorithmName, None)
    KeyUsages = property(get_KeyUsages, None)
    SignatureAlgorithmName = property(get_SignatureAlgorithmName, None)
    SignatureHashAlgorithmName = property(get_SignatureHashAlgorithmName, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
class ICertificate3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificate3'
    _iid_ = Guid('{be51a966-ae5f-4652-ace7-c6d7e7724cf3}')
    @winrt_commethod(6)
    def get_IsPerUser(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_StoreName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_KeyStorageProviderName(self) -> WinRT_String: ...
    IsPerUser = property(get_IsPerUser, None)
    KeyStorageProviderName = property(get_KeyStorageProviderName, None)
    StoreName = property(get_StoreName, None)
class ICertificateChain(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateChain'
    _iid_ = Guid('{20bf5385-3691-4501-a62c-fd97278b31ee}')
    @winrt_commethod(6)
    def Validate(self) -> win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_commethod(7)
    def ValidateWithParameters(self, parameter: win32more.Windows.Security.Cryptography.Certificates.ChainValidationParameters) -> win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult: ...
    @winrt_commethod(8)
    def GetCertificates(self, includeRoot: Boolean) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
class ICertificateEnrollmentManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics'
    _iid_ = Guid('{8846ef3f-a986-48fb-9fd7-9aec06935bf1}')
    @winrt_commethod(6)
    def CreateRequestAsync(self, request: win32more.Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def InstallCertificateAsync(self, certificate: WinRT_String, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ImportPfxDataAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICertificateEnrollmentManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics2'
    _iid_ = Guid('{dc5b1c33-6429-4014-999c-5d9735802d1d}')
    @winrt_commethod(6)
    def get_UserCertificateEnrollmentManager(self) -> win32more.Windows.Security.Cryptography.Certificates.UserCertificateEnrollmentManager: ...
    @winrt_commethod(7)
    def ImportPfxDataToKspAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    UserCertificateEnrollmentManager = property(get_UserCertificateEnrollmentManager, None)
class ICertificateEnrollmentManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateEnrollmentManagerStatics3'
    _iid_ = Guid('{fdec82be-617c-425a-b72d-398b26ac7264}')
    @winrt_commethod(6)
    def ImportPfxDataToKspWithParametersAsync(self, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: win32more.Windows.Security.Cryptography.Certificates.PfxImportParameters) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICertificateExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateExtension'
    _iid_ = Guid('{84cf0656-a9e6-454d-8e45-2ea7c4bcd53b}')
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
    def get_Value(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(12)
    def put_Value(self, value: PassArray[Byte]) -> Void: ...
    IsCritical = property(get_IsCritical, put_IsCritical)
    ObjectId = property(get_ObjectId, put_ObjectId)
    Value = property(get_Value, put_Value)
class ICertificateFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateFactory'
    _iid_ = Guid('{17b4221c-4baf-44a2-9608-04fb62b16942}')
    @winrt_commethod(6)
    def CreateCertificate(self, certBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
class ICertificateKeyUsages(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateKeyUsages'
    _iid_ = Guid('{6ac6206f-e1cf-486a-b485-a69c83e46fd1}')
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
    CrlSign = property(get_CrlSign, put_CrlSign)
    DataEncipherment = property(get_DataEncipherment, put_DataEncipherment)
    DigitalSignature = property(get_DigitalSignature, put_DigitalSignature)
    EncipherOnly = property(get_EncipherOnly, put_EncipherOnly)
    KeyAgreement = property(get_KeyAgreement, put_KeyAgreement)
    KeyCertificateSign = property(get_KeyCertificateSign, put_KeyCertificateSign)
    KeyEncipherment = property(get_KeyEncipherment, put_KeyEncipherment)
    NonRepudiation = property(get_NonRepudiation, put_NonRepudiation)
class ICertificateQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateQuery'
    _iid_ = Guid('{5b082a31-a728-4916-b5ee-ffcb8acf2417}')
    @winrt_commethod(6)
    def get_EnhancedKeyUsages(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_IssuerName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_IssuerName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Thumbprint(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(12)
    def put_Thumbprint(self, value: PassArray[Byte]) -> Void: ...
    @winrt_commethod(13)
    def get_HardwareOnly(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_HardwareOnly(self, value: Boolean) -> Void: ...
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HardwareOnly = property(get_HardwareOnly, put_HardwareOnly)
    IssuerName = property(get_IssuerName, put_IssuerName)
    Thumbprint = property(get_Thumbprint, put_Thumbprint)
class ICertificateQuery2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateQuery2'
    _iid_ = Guid('{935a0af7-0bd9-4f75-b8c2-e27a7f74eecd}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateRequestProperties'
    _iid_ = Guid('{487e84f6-94e2-4dce-8833-1a700a37a29a}')
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
    def get_Exportable(self) -> win32more.Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_commethod(17)
    def put_Exportable(self, value: win32more.Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_commethod(18)
    def get_KeyUsages(self) -> win32more.Windows.Security.Cryptography.Certificates.EnrollKeyUsages: ...
    @winrt_commethod(19)
    def put_KeyUsages(self, value: win32more.Windows.Security.Cryptography.Certificates.EnrollKeyUsages) -> Void: ...
    @winrt_commethod(20)
    def get_KeyProtectionLevel(self) -> win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_commethod(21)
    def put_KeyProtectionLevel(self, value: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_commethod(22)
    def get_KeyStorageProviderName(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def put_KeyStorageProviderName(self, value: WinRT_String) -> Void: ...
    Exportable = property(get_Exportable, put_Exportable)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    KeyAlgorithmName = property(get_KeyAlgorithmName, put_KeyAlgorithmName)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    KeySize = property(get_KeySize, put_KeySize)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    KeyUsages = property(get_KeyUsages, put_KeyUsages)
    Subject = property(get_Subject, put_Subject)
class ICertificateRequestProperties2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateRequestProperties2'
    _iid_ = Guid('{3da0c954-d73f-4ff3-a0a6-0677c0ada05b}')
    @winrt_commethod(6)
    def get_SmartcardReaderName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SmartcardReaderName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_SigningCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def put_SigningCertificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(10)
    def get_AttestationCredentialCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(11)
    def put_AttestationCredentialCertificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    AttestationCredentialCertificate = property(get_AttestationCredentialCertificate, put_AttestationCredentialCertificate)
    SigningCertificate = property(get_SigningCertificate, put_SigningCertificate)
    SmartcardReaderName = property(get_SmartcardReaderName, put_SmartcardReaderName)
class ICertificateRequestProperties3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateRequestProperties3'
    _iid_ = Guid('{e687f616-734d-46b1-9d4c-6edfdbfc845b}')
    @winrt_commethod(6)
    def get_CurveName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_CurveName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_CurveParameters(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(9)
    def put_CurveParameters(self, value: PassArray[Byte]) -> Void: ...
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
    ContainerName = property(get_ContainerName, put_ContainerName)
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    CurveName = property(get_CurveName, put_CurveName)
    CurveParameters = property(get_CurveParameters, put_CurveParameters)
    UseExistingKey = property(get_UseExistingKey, put_UseExistingKey)
class ICertificateRequestProperties4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateRequestProperties4'
    _iid_ = Guid('{4e429ad2-1c61-4fea-b8fe-135fb19cdce4}')
    @winrt_commethod(6)
    def get_SuppressedDefaults(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_SubjectAlternativeName(self) -> win32more.Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.CertificateExtension]: ...
    Extensions = property(get_Extensions, None)
    SubjectAlternativeName = property(get_SubjectAlternativeName, None)
    SuppressedDefaults = property(get_SuppressedDefaults, None)
class ICertificateStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateStore'
    _iid_ = Guid('{b0bff720-344e-4331-af14-a7f7a7ebc93a}')
    @winrt_commethod(6)
    def Add(self, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(7)
    def Delete(self, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
class ICertificateStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateStore2'
    _iid_ = Guid('{c7e68e4a-417d-4d1a-babd-15687e549974}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class ICertificateStoresStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateStoresStatics'
    _iid_ = Guid('{fbecc739-c6fe-4de7-99cf-74c3e596e032}')
    @winrt_commethod(6)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_commethod(7)
    def FindAllWithQueryAsync(self, query: win32more.Windows.Security.Cryptography.Certificates.CertificateQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]]: ...
    @winrt_commethod(8)
    def get_TrustedRootCertificationAuthorities(self) -> win32more.Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_commethod(9)
    def get_IntermediateCertificationAuthorities(self) -> win32more.Windows.Security.Cryptography.Certificates.CertificateStore: ...
    @winrt_commethod(10)
    def GetStoreByName(self, storeName: WinRT_String) -> win32more.Windows.Security.Cryptography.Certificates.CertificateStore: ...
    IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
    TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
class ICertificateStoresStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICertificateStoresStatics2'
    _iid_ = Guid('{fa900b79-a0d4-4b8c-bc55-c0a37eb141ed}')
    @winrt_commethod(6)
    def GetUserStoreByName(self, storeName: WinRT_String) -> win32more.Windows.Security.Cryptography.Certificates.UserCertificateStore: ...
class IChainBuildingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IChainBuildingParameters'
    _iid_ = Guid('{422ba922-7c8d-47b7-b59b-b12703733ac3}')
    @winrt_commethod(6)
    def get_EnhancedKeyUsages(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_ValidationTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def put_ValidationTimestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
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
    def get_ExclusiveTrustRoots(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    AuthorityInformationAccessEnabled = property(get_AuthorityInformationAccessEnabled, put_AuthorityInformationAccessEnabled)
    CurrentTimeValidationEnabled = property(get_CurrentTimeValidationEnabled, put_CurrentTimeValidationEnabled)
    EnhancedKeyUsages = property(get_EnhancedKeyUsages, None)
    ExclusiveTrustRoots = property(get_ExclusiveTrustRoots, None)
    NetworkRetrievalEnabled = property(get_NetworkRetrievalEnabled, put_NetworkRetrievalEnabled)
    RevocationCheckEnabled = property(get_RevocationCheckEnabled, put_RevocationCheckEnabled)
    ValidationTimestamp = property(get_ValidationTimestamp, put_ValidationTimestamp)
class IChainValidationParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IChainValidationParameters'
    _iid_ = Guid('{c4743b4a-7eb0-4b56-a040-b9c8e655ddf3}')
    @winrt_commethod(6)
    def get_CertificateChainPolicy(self) -> win32more.Windows.Security.Cryptography.Certificates.CertificateChainPolicy: ...
    @winrt_commethod(7)
    def put_CertificateChainPolicy(self, value: win32more.Windows.Security.Cryptography.Certificates.CertificateChainPolicy) -> Void: ...
    @winrt_commethod(8)
    def get_ServerDnsName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def put_ServerDnsName(self, value: win32more.Windows.Networking.HostName) -> Void: ...
    CertificateChainPolicy = property(get_CertificateChainPolicy, put_CertificateChainPolicy)
    ServerDnsName = property(get_ServerDnsName, put_ServerDnsName)
class ICmsAttachedSignature(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsAttachedSignature'
    _iid_ = Guid('{61899d9d-3757-4ecb-bddc-0ca357d7a936}')
    @winrt_commethod(6)
    def get_Certificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(7)
    def get_Content(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(8)
    def get_Signers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_commethod(9)
    def VerifySignature(self) -> win32more.Windows.Security.Cryptography.Certificates.SignatureValidationResult: ...
    Certificates = property(get_Certificates, None)
    Content = property(get_Content, None)
    Signers = property(get_Signers, None)
class ICmsAttachedSignatureFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsAttachedSignatureFactory'
    _iid_ = Guid('{d0c8fc15-f757-4c64-a362-52cc1c77cffb}')
    @winrt_commethod(6)
    def CreateCmsAttachedSignature(self, inputBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Certificates.CmsAttachedSignature: ...
class ICmsAttachedSignatureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsAttachedSignatureStatics'
    _iid_ = Guid('{87989c8e-b0ad-498d-a7f5-78b59bce4b36}')
    @winrt_commethod(6)
    def GenerateSignatureAsync(self, data: win32more.Windows.Storage.Streams.IBuffer, signers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
class ICmsDetachedSignature(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsDetachedSignature'
    _iid_ = Guid('{0f1ef154-f65e-4536-8339-5944081db2ca}')
    @winrt_commethod(6)
    def get_Certificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(7)
    def get_Signers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo]: ...
    @winrt_commethod(8)
    def VerifySignatureAsync(self, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Certificates.SignatureValidationResult]: ...
    Certificates = property(get_Certificates, None)
    Signers = property(get_Signers, None)
class ICmsDetachedSignatureFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsDetachedSignatureFactory'
    _iid_ = Guid('{c4ab3503-ae7f-4387-ad19-00f150e48ebb}')
    @winrt_commethod(6)
    def CreateCmsDetachedSignature(self, inputBlob: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Security.Cryptography.Certificates.CmsDetachedSignature: ...
class ICmsDetachedSignatureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsDetachedSignatureStatics'
    _iid_ = Guid('{3d114cfd-bf9b-4682-9be6-91f57c053808}')
    @winrt_commethod(6)
    def GenerateSignatureAsync(self, data: win32more.Windows.Storage.Streams.IInputStream, signers: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.CmsSignerInfo], certificates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Cryptography.Certificates.Certificate]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
class ICmsSignerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsSignerInfo'
    _iid_ = Guid('{50d020db-1d2f-4c1a-b5c5-d0188ff91f47}')
    @winrt_commethod(6)
    def get_Certificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def put_Certificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(8)
    def get_HashAlgorithmName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_HashAlgorithmName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_TimestampInfo(self) -> win32more.Windows.Security.Cryptography.Certificates.CmsTimestampInfo: ...
    Certificate = property(get_Certificate, put_Certificate)
    HashAlgorithmName = property(get_HashAlgorithmName, put_HashAlgorithmName)
    TimestampInfo = property(get_TimestampInfo, None)
class ICmsTimestampInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ICmsTimestampInfo'
    _iid_ = Guid('{2f5f00f2-2c18-4f88-8435-c534086076f5}')
    @winrt_commethod(6)
    def get_SigningCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_Certificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    Certificates = property(get_Certificates, None)
    SigningCertificate = property(get_SigningCertificate, None)
    Timestamp = property(get_Timestamp, None)
class IKeyAlgorithmNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics'
    _iid_ = Guid('{479065d7-7ac7-4581-8c3b-d07027140448}')
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
    Dsa = property(get_Dsa, None)
    Ecdh256 = property(get_Ecdh256, None)
    Ecdh384 = property(get_Ecdh384, None)
    Ecdh521 = property(get_Ecdh521, None)
    Ecdsa256 = property(get_Ecdsa256, None)
    Ecdsa384 = property(get_Ecdsa384, None)
    Ecdsa521 = property(get_Ecdsa521, None)
    Rsa = property(get_Rsa, None)
class IKeyAlgorithmNamesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics2'
    _iid_ = Guid('{c99b5686-e1fd-4a4a-893d-a26f33dd8bb4}')
    @winrt_commethod(6)
    def get_Ecdsa(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Ecdh(self) -> WinRT_String: ...
    Ecdh = property(get_Ecdh, None)
    Ecdsa = property(get_Ecdsa, None)
class IKeyAttestationHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics'
    _iid_ = Guid('{1648e246-f644-4326-88be-3af102d30e0c}')
    @winrt_commethod(6)
    def DecryptTpmAttestationCredentialAsync(self, credential: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def GetTpmAttestationCredentialId(self, credential: WinRT_String) -> WinRT_String: ...
class IKeyAttestationHelperStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics2'
    _iid_ = Guid('{9c590b2c-a6c6-4a5e-9e64-e85d5279df97}')
    @winrt_commethod(6)
    def DecryptTpmAttestationCredentialWithContainerNameAsync(self, credential: WinRT_String, containerName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class IKeyStorageProviderNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics'
    _iid_ = Guid('{af186ae0-5529-4602-bd94-0aab91957b5c}')
    @winrt_commethod(6)
    def get_SoftwareKeyStorageProvider(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SmartcardKeyStorageProvider(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PlatformKeyStorageProvider(self) -> WinRT_String: ...
    PlatformKeyStorageProvider = property(get_PlatformKeyStorageProvider, None)
    SmartcardKeyStorageProvider = property(get_SmartcardKeyStorageProvider, None)
    SoftwareKeyStorageProvider = property(get_SoftwareKeyStorageProvider, None)
class IKeyStorageProviderNamesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics2'
    _iid_ = Guid('{262d743d-9c2e-41cc-8812-c4d971dd7c60}')
    @winrt_commethod(6)
    def get_PassportKeyStorageProvider(self) -> WinRT_String: ...
    PassportKeyStorageProvider = property(get_PassportKeyStorageProvider, None)
class IPfxImportParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IPfxImportParameters'
    _iid_ = Guid('{680d3511-9a08-47c8-864a-2edd4d8eb46c}')
    @winrt_commethod(6)
    def get_Exportable(self) -> win32more.Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_commethod(7)
    def put_Exportable(self, value: win32more.Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_commethod(8)
    def get_KeyProtectionLevel(self) -> win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_commethod(9)
    def put_KeyProtectionLevel(self, value: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_commethod(10)
    def get_InstallOptions(self) -> win32more.Windows.Security.Cryptography.Certificates.InstallOptions: ...
    @winrt_commethod(11)
    def put_InstallOptions(self, value: win32more.Windows.Security.Cryptography.Certificates.InstallOptions) -> Void: ...
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
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    Exportable = property(get_Exportable, put_Exportable)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    InstallOptions = property(get_InstallOptions, put_InstallOptions)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    ReaderName = property(get_ReaderName, put_ReaderName)
class IStandardCertificateStoreNamesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics'
    _iid_ = Guid('{0c154adb-a496-41f8-8fe5-9e96f36efbf8}')
    @winrt_commethod(6)
    def get_Personal(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TrustedRootCertificationAuthorities(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IntermediateCertificationAuthorities(self) -> WinRT_String: ...
    IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
    Personal = property(get_Personal, None)
    TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
class ISubjectAlternativeNameInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo'
    _iid_ = Guid('{582859f1-569d-4c20-be7b-4e1c9a0bc52b}')
    @winrt_commethod(6)
    def get_EmailName(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_IPAddress(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Url(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DnsName(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_DistinguishedName(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PrincipalName(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    DistinguishedName = property(get_DistinguishedName, None)
    DnsName = property(get_DnsName, None)
    EmailName = property(get_EmailName, None)
    IPAddress = property(get_IPAddress, None)
    PrincipalName = property(get_PrincipalName, None)
    Url = property(get_Url, None)
class ISubjectAlternativeNameInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2'
    _iid_ = Guid('{437a78c6-1c51-41ea-b34a-3d654398a370}')
    @winrt_commethod(6)
    def get_EmailNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_IPAddresses(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Urls(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DnsNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(10)
    def get_DistinguishedNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PrincipalNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(12)
    def get_Extension(self) -> win32more.Windows.Security.Cryptography.Certificates.CertificateExtension: ...
    DistinguishedNames = property(get_DistinguishedNames, None)
    DnsNames = property(get_DnsNames, None)
    EmailNames = property(get_EmailNames, None)
    Extension = property(get_Extension, None)
    IPAddresses = property(get_IPAddresses, None)
    PrincipalNames = property(get_PrincipalNames, None)
    Urls = property(get_Urls, None)
class IUserCertificateEnrollmentManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager'
    _iid_ = Guid('{96313718-22e1-4819-b20b-ab46a6eca06e}')
    @winrt_commethod(6)
    def CreateRequestAsync(self, request: win32more.Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def InstallCertificateAsync(self, certificate: WinRT_String, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ImportPfxDataAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ImportPfxDataToKspAsync(self, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IUserCertificateEnrollmentManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager2'
    _iid_ = Guid('{0dad9cb1-65de-492a-b86d-fc5c482c3747}')
    @winrt_commethod(6)
    def ImportPfxDataToKspWithParametersAsync(self, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: win32more.Windows.Security.Cryptography.Certificates.PfxImportParameters) -> win32more.Windows.Foundation.IAsyncAction: ...
class IUserCertificateStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.IUserCertificateStore'
    _iid_ = Guid('{c9fb1d83-789f-4b4e-9180-045a757aac6d}')
    @winrt_commethod(6)
    def RequestAddAsync(self, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RequestDeleteAsync(self, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class InstallOptions(Enum, UInt32):
    None_ = 0
    DeleteExpired = 1
class _KeyAlgorithmNames_Meta_(ComPtr.__class__):
    pass
class KeyAlgorithmNames(ComPtr, metaclass=_KeyAlgorithmNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.KeyAlgorithmNames'
    @winrt_classmethod
    def get_Ecdsa(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rsa(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Dsa(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh256(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh384(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdh521(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdsa256(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdsa384(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ecdsa521(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAlgorithmNamesStatics) -> WinRT_String: ...
    _KeyAlgorithmNames_Meta_.Dsa = property(get_Dsa, None)
    _KeyAlgorithmNames_Meta_.Ecdh = property(get_Ecdh, None)
    _KeyAlgorithmNames_Meta_.Ecdh256 = property(get_Ecdh256, None)
    _KeyAlgorithmNames_Meta_.Ecdh384 = property(get_Ecdh384, None)
    _KeyAlgorithmNames_Meta_.Ecdh521 = property(get_Ecdh521, None)
    _KeyAlgorithmNames_Meta_.Ecdsa = property(get_Ecdsa, None)
    _KeyAlgorithmNames_Meta_.Ecdsa256 = property(get_Ecdsa256, None)
    _KeyAlgorithmNames_Meta_.Ecdsa384 = property(get_Ecdsa384, None)
    _KeyAlgorithmNames_Meta_.Ecdsa521 = property(get_Ecdsa521, None)
    _KeyAlgorithmNames_Meta_.Rsa = property(get_Rsa, None)
class KeyAttestationHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.KeyAttestationHelper'
    @winrt_classmethod
    def DecryptTpmAttestationCredentialWithContainerNameAsync(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics2, credential: WinRT_String, containerName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def DecryptTpmAttestationCredentialAsync(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics, credential: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetTpmAttestationCredentialId(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyAttestationHelperStatics, credential: WinRT_String) -> WinRT_String: ...
class KeyProtectionLevel(Enum, Int32):
    NoConsent = 0
    ConsentOnly = 1
    ConsentWithPassword = 2
    ConsentWithFingerprint = 3
class KeySize(Enum, Int32):
    Invalid = 0
    Rsa2048 = 2048
    Rsa4096 = 4096
class _KeyStorageProviderNames_Meta_(ComPtr.__class__):
    pass
class KeyStorageProviderNames(ComPtr, metaclass=_KeyStorageProviderNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.KeyStorageProviderNames'
    @winrt_classmethod
    def get_PassportKeyStorageProvider(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_SoftwareKeyStorageProvider(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SmartcardKeyStorageProvider(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PlatformKeyStorageProvider(cls: win32more.Windows.Security.Cryptography.Certificates.IKeyStorageProviderNamesStatics) -> WinRT_String: ...
    _KeyStorageProviderNames_Meta_.PassportKeyStorageProvider = property(get_PassportKeyStorageProvider, None)
    _KeyStorageProviderNames_Meta_.PlatformKeyStorageProvider = property(get_PlatformKeyStorageProvider, None)
    _KeyStorageProviderNames_Meta_.SmartcardKeyStorageProvider = property(get_SmartcardKeyStorageProvider, None)
    _KeyStorageProviderNames_Meta_.SoftwareKeyStorageProvider = property(get_SoftwareKeyStorageProvider, None)
class PfxImportParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters
    _classid_ = 'Windows.Security.Cryptography.Certificates.PfxImportParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.PfxImportParameters.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.PfxImportParameters: ...
    @winrt_mixinmethod
    def get_Exportable(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> win32more.Windows.Security.Cryptography.Certificates.ExportOption: ...
    @winrt_mixinmethod
    def put_Exportable(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: win32more.Windows.Security.Cryptography.Certificates.ExportOption) -> Void: ...
    @winrt_mixinmethod
    def get_KeyProtectionLevel(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel: ...
    @winrt_mixinmethod
    def put_KeyProtectionLevel(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_InstallOptions(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> win32more.Windows.Security.Cryptography.Certificates.InstallOptions: ...
    @winrt_mixinmethod
    def put_InstallOptions(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: win32more.Windows.Security.Cryptography.Certificates.InstallOptions) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KeyStorageProviderName(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_KeyStorageProviderName(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContainerNamePrefix(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContainerNamePrefix(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ReaderName(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReaderName(self: win32more.Windows.Security.Cryptography.Certificates.IPfxImportParameters, value: WinRT_String) -> Void: ...
    ContainerNamePrefix = property(get_ContainerNamePrefix, put_ContainerNamePrefix)
    Exportable = property(get_Exportable, put_Exportable)
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    InstallOptions = property(get_InstallOptions, put_InstallOptions)
    KeyProtectionLevel = property(get_KeyProtectionLevel, put_KeyProtectionLevel)
    KeyStorageProviderName = property(get_KeyStorageProviderName, put_KeyStorageProviderName)
    ReaderName = property(get_ReaderName, put_ReaderName)
class SignatureValidationResult(Enum, Int32):
    Success = 0
    InvalidParameter = 1
    BadMessage = 2
    InvalidSignature = 3
    OtherErrors = 4
class _StandardCertificateStoreNames_Meta_(ComPtr.__class__):
    pass
class StandardCertificateStoreNames(ComPtr, metaclass=_StandardCertificateStoreNames_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.Certificates.StandardCertificateStoreNames'
    @winrt_classmethod
    def get_Personal(cls: win32more.Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TrustedRootCertificationAuthorities(cls: win32more.Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IntermediateCertificationAuthorities(cls: win32more.Windows.Security.Cryptography.Certificates.IStandardCertificateStoreNamesStatics) -> WinRT_String: ...
    _StandardCertificateStoreNames_Meta_.IntermediateCertificationAuthorities = property(get_IntermediateCertificationAuthorities, None)
    _StandardCertificateStoreNames_Meta_.Personal = property(get_Personal, None)
    _StandardCertificateStoreNames_Meta_.TrustedRootCertificationAuthorities = property(get_TrustedRootCertificationAuthorities, None)
class SubjectAlternativeNameInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo
    _classid_ = 'Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.Certificates.SubjectAlternativeNameInfo: ...
    @winrt_mixinmethod
    def get_EmailName(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IPAddress(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Url(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DnsName(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DistinguishedName(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PrincipalName(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_EmailNames(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IPAddresses(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Urls(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DnsNames(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DistinguishedNames(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PrincipalNames(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Extension(self: win32more.Windows.Security.Cryptography.Certificates.ISubjectAlternativeNameInfo2) -> win32more.Windows.Security.Cryptography.Certificates.CertificateExtension: ...
    DistinguishedName = property(get_DistinguishedName, None)
    DistinguishedNames = property(get_DistinguishedNames, None)
    DnsName = property(get_DnsName, None)
    DnsNames = property(get_DnsNames, None)
    EmailName = property(get_EmailName, None)
    EmailNames = property(get_EmailNames, None)
    Extension = property(get_Extension, None)
    IPAddress = property(get_IPAddress, None)
    IPAddresses = property(get_IPAddresses, None)
    PrincipalName = property(get_PrincipalName, None)
    PrincipalNames = property(get_PrincipalNames, None)
    Url = property(get_Url, None)
    Urls = property(get_Urls, None)
class UserCertificateEnrollmentManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager
    _classid_ = 'Windows.Security.Cryptography.Certificates.UserCertificateEnrollmentManager'
    @winrt_mixinmethod
    def CreateRequestAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, request: win32more.Windows.Security.Cryptography.Certificates.CertificateRequestProperties) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def InstallCertificateAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, certificate: WinRT_String, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportPfxDataAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportPfxDataToKspAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager, pfxData: WinRT_String, password: WinRT_String, exportable: win32more.Windows.Security.Cryptography.Certificates.ExportOption, keyProtectionLevel: win32more.Windows.Security.Cryptography.Certificates.KeyProtectionLevel, installOption: win32more.Windows.Security.Cryptography.Certificates.InstallOptions, friendlyName: WinRT_String, keyStorageProvider: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportPfxDataToKspWithParametersAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateEnrollmentManager2, pfxData: WinRT_String, password: WinRT_String, pfxImportParameters: win32more.Windows.Security.Cryptography.Certificates.PfxImportParameters) -> win32more.Windows.Foundation.IAsyncAction: ...
class UserCertificateStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateStore
    _classid_ = 'Windows.Security.Cryptography.Certificates.UserCertificateStore'
    @winrt_mixinmethod
    def RequestAddAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateStore, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestDeleteAsync(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateStore, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Security.Cryptography.Certificates.IUserCertificateStore) -> WinRT_String: ...
    Name = property(get_Name, None)


make_ready(__name__)
