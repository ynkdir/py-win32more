from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.Cryptography
import Windows.Win32.Storage.Packaging.Opc
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
OPC_E_NONCONFORMING_URI: Windows.Win32.Foundation.HRESULT = -2142175231
OPC_E_RELATIVE_URI_REQUIRED: Windows.Win32.Foundation.HRESULT = -2142175230
OPC_E_RELATIONSHIP_URI_REQUIRED: Windows.Win32.Foundation.HRESULT = -2142175229
OPC_E_PART_CANNOT_BE_DIRECTORY: Windows.Win32.Foundation.HRESULT = -2142175228
OPC_E_UNEXPECTED_CONTENT_TYPE: Windows.Win32.Foundation.HRESULT = -2142175227
OPC_E_INVALID_CONTENT_TYPE_XML: Windows.Win32.Foundation.HRESULT = -2142175226
OPC_E_MISSING_CONTENT_TYPES: Windows.Win32.Foundation.HRESULT = -2142175225
OPC_E_NONCONFORMING_CONTENT_TYPES_XML: Windows.Win32.Foundation.HRESULT = -2142175224
OPC_E_NONCONFORMING_RELS_XML: Windows.Win32.Foundation.HRESULT = -2142175223
OPC_E_INVALID_RELS_XML: Windows.Win32.Foundation.HRESULT = -2142175222
OPC_E_DUPLICATE_PART: Windows.Win32.Foundation.HRESULT = -2142175221
OPC_E_INVALID_OVERRIDE_PART_NAME: Windows.Win32.Foundation.HRESULT = -2142175220
OPC_E_DUPLICATE_OVERRIDE_PART: Windows.Win32.Foundation.HRESULT = -2142175219
OPC_E_INVALID_DEFAULT_EXTENSION: Windows.Win32.Foundation.HRESULT = -2142175218
OPC_E_DUPLICATE_DEFAULT_EXTENSION: Windows.Win32.Foundation.HRESULT = -2142175217
OPC_E_INVALID_RELATIONSHIP_ID: Windows.Win32.Foundation.HRESULT = -2142175216
OPC_E_INVALID_RELATIONSHIP_TYPE: Windows.Win32.Foundation.HRESULT = -2142175215
OPC_E_INVALID_RELATIONSHIP_TARGET: Windows.Win32.Foundation.HRESULT = -2142175214
OPC_E_DUPLICATE_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142175213
OPC_E_CONFLICTING_SETTINGS: Windows.Win32.Foundation.HRESULT = -2142175212
OPC_E_DUPLICATE_PIECE: Windows.Win32.Foundation.HRESULT = -2142175211
OPC_E_INVALID_PIECE: Windows.Win32.Foundation.HRESULT = -2142175210
OPC_E_MISSING_PIECE: Windows.Win32.Foundation.HRESULT = -2142175209
OPC_E_NO_SUCH_PART: Windows.Win32.Foundation.HRESULT = -2142175208
OPC_E_DS_SIGNATURE_CORRUPT: Windows.Win32.Foundation.HRESULT = -2142175207
OPC_E_DS_DIGEST_VALUE_ERROR: Windows.Win32.Foundation.HRESULT = -2142175206
OPC_E_DS_DUPLICATE_SIGNATURE_ORIGIN_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142175205
OPC_E_DS_INVALID_SIGNATURE_ORIGIN_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142175204
OPC_E_DS_INVALID_CERTIFICATE_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142175203
OPC_E_DS_EXTERNAL_SIGNATURE: Windows.Win32.Foundation.HRESULT = -2142175202
OPC_E_DS_MISSING_SIGNATURE_ORIGIN_PART: Windows.Win32.Foundation.HRESULT = -2142175201
OPC_E_DS_MISSING_SIGNATURE_PART: Windows.Win32.Foundation.HRESULT = -2142175200
OPC_E_DS_INVALID_RELATIONSHIP_TRANSFORM_XML: Windows.Win32.Foundation.HRESULT = -2142175199
OPC_E_DS_INVALID_CANONICALIZATION_METHOD: Windows.Win32.Foundation.HRESULT = -2142175198
OPC_E_DS_INVALID_RELATIONSHIPS_SIGNING_OPTION: Windows.Win32.Foundation.HRESULT = -2142175197
OPC_E_DS_INVALID_OPC_SIGNATURE_TIME_FORMAT: Windows.Win32.Foundation.HRESULT = -2142175196
OPC_E_DS_PACKAGE_REFERENCE_URI_RESERVED: Windows.Win32.Foundation.HRESULT = -2142175195
OPC_E_DS_MISSING_SIGNATURE_PROPERTIES_ELEMENT: Windows.Win32.Foundation.HRESULT = -2142175194
OPC_E_DS_MISSING_SIGNATURE_PROPERTY_ELEMENT: Windows.Win32.Foundation.HRESULT = -2142175193
OPC_E_DS_DUPLICATE_SIGNATURE_PROPERTY_ELEMENT: Windows.Win32.Foundation.HRESULT = -2142175192
OPC_E_DS_MISSING_SIGNATURE_TIME_PROPERTY: Windows.Win32.Foundation.HRESULT = -2142175191
OPC_E_DS_INVALID_SIGNATURE_XML: Windows.Win32.Foundation.HRESULT = -2142175190
OPC_E_DS_INVALID_SIGNATURE_COUNT: Windows.Win32.Foundation.HRESULT = -2142175189
OPC_E_DS_MISSING_SIGNATURE_ALGORITHM: Windows.Win32.Foundation.HRESULT = -2142175188
OPC_E_DS_DUPLICATE_PACKAGE_OBJECT_REFERENCES: Windows.Win32.Foundation.HRESULT = -2142175187
OPC_E_DS_MISSING_PACKAGE_OBJECT_REFERENCE: Windows.Win32.Foundation.HRESULT = -2142175186
OPC_E_DS_EXTERNAL_SIGNATURE_REFERENCE: Windows.Win32.Foundation.HRESULT = -2142175185
OPC_E_DS_REFERENCE_MISSING_CONTENT_TYPE: Windows.Win32.Foundation.HRESULT = -2142175184
OPC_E_DS_MULTIPLE_RELATIONSHIP_TRANSFORMS: Windows.Win32.Foundation.HRESULT = -2142175183
OPC_E_DS_MISSING_CANONICALIZATION_TRANSFORM: Windows.Win32.Foundation.HRESULT = -2142175182
OPC_E_MC_UNEXPECTED_ELEMENT: Windows.Win32.Foundation.HRESULT = -2142175181
OPC_E_MC_UNEXPECTED_REQUIRES_ATTR: Windows.Win32.Foundation.HRESULT = -2142175180
OPC_E_MC_MISSING_REQUIRES_ATTR: Windows.Win32.Foundation.HRESULT = -2142175179
OPC_E_MC_UNEXPECTED_ATTR: Windows.Win32.Foundation.HRESULT = -2142175178
OPC_E_MC_INVALID_PREFIX_LIST: Windows.Win32.Foundation.HRESULT = -2142175177
OPC_E_MC_INVALID_QNAME_LIST: Windows.Win32.Foundation.HRESULT = -2142175176
OPC_E_MC_NESTED_ALTERNATE_CONTENT: Windows.Win32.Foundation.HRESULT = -2142175175
OPC_E_MC_UNEXPECTED_CHOICE: Windows.Win32.Foundation.HRESULT = -2142175174
OPC_E_MC_MISSING_CHOICE: Windows.Win32.Foundation.HRESULT = -2142175173
OPC_E_MC_INVALID_ENUM_TYPE: Windows.Win32.Foundation.HRESULT = -2142175172
OPC_E_MC_UNKNOWN_NAMESPACE: Windows.Win32.Foundation.HRESULT = -2142175170
OPC_E_MC_UNKNOWN_PREFIX: Windows.Win32.Foundation.HRESULT = -2142175169
OPC_E_MC_INVALID_ATTRIBUTES_ON_IGNORABLE_ELEMENT: Windows.Win32.Foundation.HRESULT = -2142175168
OPC_E_MC_INVALID_XMLNS_ATTRIBUTE: Windows.Win32.Foundation.HRESULT = -2142175167
OPC_E_INVALID_XML_ENCODING: Windows.Win32.Foundation.HRESULT = -2142175166
OPC_E_DS_SIGNATURE_REFERENCE_MISSING_URI: Windows.Win32.Foundation.HRESULT = -2142175165
OPC_E_INVALID_CONTENT_TYPE: Windows.Win32.Foundation.HRESULT = -2142175164
OPC_E_DS_SIGNATURE_PROPERTY_MISSING_TARGET: Windows.Win32.Foundation.HRESULT = -2142175163
OPC_E_DS_SIGNATURE_METHOD_NOT_SET: Windows.Win32.Foundation.HRESULT = -2142175162
OPC_E_DS_DEFAULT_DIGEST_METHOD_NOT_SET: Windows.Win32.Foundation.HRESULT = -2142175161
OPC_E_NO_SUCH_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142175160
OPC_E_MC_MULTIPLE_FALLBACK_ELEMENTS: Windows.Win32.Foundation.HRESULT = -2142175159
OPC_E_MC_INCONSISTENT_PROCESS_CONTENT: Windows.Win32.Foundation.HRESULT = -2142175158
OPC_E_MC_INCONSISTENT_PRESERVE_ATTRIBUTES: Windows.Win32.Foundation.HRESULT = -2142175157
OPC_E_MC_INCONSISTENT_PRESERVE_ELEMENTS: Windows.Win32.Foundation.HRESULT = -2142175156
OPC_E_INVALID_RELATIONSHIP_TARGET_MODE: Windows.Win32.Foundation.HRESULT = -2142175155
OPC_E_COULD_NOT_RECOVER: Windows.Win32.Foundation.HRESULT = -2142175154
OPC_E_UNSUPPORTED_PACKAGE: Windows.Win32.Foundation.HRESULT = -2142175153
OPC_E_ENUM_COLLECTION_CHANGED: Windows.Win32.Foundation.HRESULT = -2142175152
OPC_E_ENUM_CANNOT_MOVE_NEXT: Windows.Win32.Foundation.HRESULT = -2142175151
OPC_E_ENUM_CANNOT_MOVE_PREVIOUS: Windows.Win32.Foundation.HRESULT = -2142175150
OPC_E_ENUM_INVALID_POSITION: Windows.Win32.Foundation.HRESULT = -2142175149
OPC_E_DS_SIGNATURE_ORIGIN_EXISTS: Windows.Win32.Foundation.HRESULT = -2142175148
OPC_E_DS_UNSIGNED_PACKAGE: Windows.Win32.Foundation.HRESULT = -2142175147
OPC_E_DS_MISSING_CERTIFICATE_PART: Windows.Win32.Foundation.HRESULT = -2142175146
OPC_E_NO_SUCH_SETTINGS: Windows.Win32.Foundation.HRESULT = -2142175145
OPC_E_ZIP_INCORRECT_DATA_SIZE: Windows.Win32.Foundation.HRESULT = -2142171135
OPC_E_ZIP_CORRUPTED_ARCHIVE: Windows.Win32.Foundation.HRESULT = -2142171134
OPC_E_ZIP_COMPRESSION_FAILED: Windows.Win32.Foundation.HRESULT = -2142171133
OPC_E_ZIP_DECOMPRESSION_FAILED: Windows.Win32.Foundation.HRESULT = -2142171132
OPC_E_ZIP_INCONSISTENT_FILEITEM: Windows.Win32.Foundation.HRESULT = -2142171131
OPC_E_ZIP_INCONSISTENT_DIRECTORY: Windows.Win32.Foundation.HRESULT = -2142171130
OPC_E_ZIP_MISSING_DATA_DESCRIPTOR: Windows.Win32.Foundation.HRESULT = -2142171129
OPC_E_ZIP_UNSUPPORTEDARCHIVE: Windows.Win32.Foundation.HRESULT = -2142171128
OPC_E_ZIP_CENTRAL_DIRECTORY_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2142171127
OPC_E_ZIP_NAME_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2142171126
OPC_E_ZIP_DUPLICATE_NAME: Windows.Win32.Foundation.HRESULT = -2142171125
OPC_E_ZIP_COMMENT_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2142171124
OPC_E_ZIP_EXTRA_FIELDS_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2142171123
OPC_E_ZIP_FILE_HEADER_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2142171122
OPC_E_ZIP_MISSING_END_OF_CENTRAL_DIRECTORY: Windows.Win32.Foundation.HRESULT = -2142171121
OPC_E_ZIP_REQUIRES_64_BIT: Windows.Win32.Foundation.HRESULT = -2142171120
class IOpcCertificateEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85131937-8f24-421f-b4-39-59-ab-24-d1-40-b8')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(certificate: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcCertificateSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('56ea4325-8e2d-4167-b1-a4-e4-86-d2-4c-8f-a7')
    @commethod(3)
    def Add(certificate: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(certificate: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(certificateEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcDigitalSignature(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('52ab21dd-1cd0-4949-bc-80-0c-12-32-d0-0c-b4')
    @commethod(3)
    def GetNamespaces(prefixes: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), namespaces: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignatureId(signatureId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignaturePartName(signaturePartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignatureMethod(signatureMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCanonicalizationMethod(canonicalizationMethod: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignatureValue(signatureValue: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSignaturePartReferenceEnumerator(partReferenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSignatureRelationshipReferenceEnumerator(relationshipReferenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSigningTime(signingTime: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTimeFormat(timeFormat: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPackageObjectReference(packageObjectReference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCertificateEnumerator(certificateEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCustomReferenceEnumerator(customReferenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCustomObjectEnumerator(customObjectEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSignatureXml(signatureXml: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcDigitalSignatureEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('967b6882-0ba3-4358-b9-e7-b6-4c-75-06-3c-5e')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(digitalSignature: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcDigitalSignatureManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d5e62a0b-696d-462f-94-df-72-e3-3c-ef-26-59')
    @commethod(3)
    def GetSignatureOriginPartName(signatureOriginPartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSignatureOriginPartName(signatureOriginPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignatureEnumerator(signatureEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveSignature(signaturePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSigningOptions(signingOptions: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSigningOptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Validate(signature: Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature_head, certificate: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), validationResult: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_VALIDATION_RESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Sign(certificate: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), signingOptions: Windows.Win32.Storage.Packaging.Opc.IOpcSigningOptions_head, digitalSignature: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ReplaceSignatureXml(signaturePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, newSignatureXml: c_char_p_no, count: UInt32, digitalSignature: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6d0b4446-cd73-4ab3-94-f4-8c-cd-f6-11-61-54')
    @commethod(3)
    def CreatePackageRootUri(rootUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePartUri(pwzUri: Windows.Win32.Foundation.PWSTR, partUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStreamOnFile(filename: Windows.Win32.Foundation.PWSTR, ioMode: Windows.Win32.Storage.Packaging.Opc.OPC_STREAM_IO_MODE, securityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwFlagsAndAttributes: UInt32, stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreatePackage(package: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReadPackageFromStream(stream: Windows.Win32.System.Com.IStream_head, flags: Windows.Win32.Storage.Packaging.Opc.OPC_READ_FLAGS, package: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WritePackageToStream(package: Windows.Win32.Storage.Packaging.Opc.IOpcPackage_head, flags: Windows.Win32.Storage.Packaging.Opc.OPC_WRITE_FLAGS, stream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateDigitalSignatureManager(package: Windows.Win32.Storage.Packaging.Opc.IOpcPackage_head, signatureManager: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignatureManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcPackage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-70')
    @commethod(3)
    def GetPartSet(partSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRelationshipSet(relationshipSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcPart(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-71')
    @commethod(3)
    def GetRelationshipSet(relationshipSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContentStream(stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetName(name: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetContentType(contentType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCompressionOptions(compressionOptions: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcPartEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-75')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(part: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPart_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcPartSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-73')
    @commethod(3)
    def GetPart(name: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPart_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePart(name: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, contentType: Windows.Win32.Foundation.PWSTR, compressionOptions: Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS, part: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPart_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeletePart(name: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PartExists(name: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, partExists: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEnumerator(partEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcPartUri(c_void_p):
    extends: Windows.Win32.Storage.Packaging.Opc.IOpcUri
    Guid = Guid('7d3babe7-88b2-46ba-85-cb-42-03-cb-01-6c-87')
    @commethod(31)
    def ComparePartUri(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, comparisonResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetSourceUri(sourceUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def IsRelationshipsPartUri(isRelationshipUri: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationship(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-72')
    @commethod(3)
    def GetId(relationshipIdentifier: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRelationshipType(relationshipType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceUri(sourceUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTargetUri(targetUri: POINTER(Windows.Win32.System.Com.IUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTargetMode(targetMode: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_URI_TARGET_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-76')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(relationship: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationship_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSelector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f8f26c7f-b28f-4899-84-c8-5d-56-39-ed-e7-5f')
    @commethod(3)
    def GetSelectorType(selector: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSelectionCriterion(selectionCriterion: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSelectorEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5e50a181-a91b-48ac-88-d2-bc-a3-d8-f8-c0-b1')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(relationshipSelector: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSelectorSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6e34c269-a4d3-47c0-b5-c4-87-ff-2b-3b-61-36')
    @commethod(3)
    def Create(selector: Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR, selectionCriterion: Windows.Win32.Foundation.PWSTR, relationshipSelector: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(relationshipSelector: Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(relationshipSelectorEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('42195949-3b79-4fc8-89-c6-fc-7f-b9-79-ee-74')
    @commethod(3)
    def GetRelationship(relationshipIdentifier: Windows.Win32.Foundation.PWSTR, relationship: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationship_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRelationship(relationshipIdentifier: Windows.Win32.Foundation.PWSTR, relationshipType: Windows.Win32.Foundation.PWSTR, targetUri: Windows.Win32.System.Com.IUri_head, targetMode: Windows.Win32.Storage.Packaging.Opc.OPC_URI_TARGET_MODE, relationship: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationship_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteRelationship(relationshipIdentifier: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RelationshipExists(relationshipIdentifier: Windows.Win32.Foundation.PWSTR, relationshipExists: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEnumerator(relationshipEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnumeratorForType(relationshipType: Windows.Win32.Foundation.PWSTR, relationshipEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRelationshipsContentStream(contents: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureCustomObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d77a19e-62c1-44e7-be-cd-45-da-5a-e5-1a-56')
    @commethod(3)
    def GetXml(xmlMarkup: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureCustomObjectEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5ee4fe1d-e1b0-4683-80-79-7e-a0-fc-f8-0b-4c')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(customObject: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureCustomObjectSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8f792ac5-7947-4e11-bc-3d-26-59-ff-04-6a-e1')
    @commethod(3)
    def Create(xmlMarkup: c_char_p_no, count: UInt32, customObject: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(customObject: Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(customObjectEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignaturePartReference(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e24231ca-59f4-484e-b6-4b-36-ee-da-36-07-2c')
    @commethod(3)
    def GetPartName(partName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContentType(contentType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDigestMethod(digestMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDigestValue(digestValue: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransformMethod(transformMethod: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignaturePartReferenceEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('80eb1561-8c77-49cf-82-66-45-9b-35-6e-e9-9a')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(partReference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignaturePartReferenceSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6c9fe28c-ecd9-4b22-9d-36-7f-dd-e6-70-fe-c0')
    @commethod(3)
    def Create(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, digestMethod: Windows.Win32.Foundation.PWSTR, transformMethod: Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD, partReference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(partReference: Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReference_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(partReferenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureReference(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1b47005e-3011-4edc-be-6f-0f-65-e5-ab-03-42')
    @commethod(3)
    def GetId(referenceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUri(referenceUri: POINTER(Windows.Win32.System.Com.IUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(type: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformMethod(transformMethod: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDigestMethod(digestMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDigestValue(digestValue: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureReferenceEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cfa59a45-28b1-4868-96-9e-fa-80-97-fd-c1-2a')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(reference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureReferenceSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f3b02d31-ab12-42dd-9e-2f-2b-16-76-1c-3c-1e')
    @commethod(3)
    def Create(referenceUri: Windows.Win32.System.Com.IUri_head, referenceId: Windows.Win32.Foundation.PWSTR, type: Windows.Win32.Foundation.PWSTR, digestMethod: Windows.Win32.Foundation.PWSTR, transformMethod: Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD, reference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(reference: Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(referenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureRelationshipReference(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('57babac6-9d4a-4e50-8b-86-e5-d4-05-1e-ae-7c')
    @commethod(3)
    def GetSourceUri(sourceUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDigestMethod(digestMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDigestValue(digestValue: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformMethod(transformMethod: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRelationshipSigningOption(relationshipSigningOption: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRelationshipSelectorEnumerator(selectorEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureRelationshipReferenceEnumerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('773ba3e4-f021-48e4-aa-04-98-16-db-5d-34-95')
    @commethod(3)
    def MoveNext(hasNext: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(hasPrevious: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(relationshipReference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(copy: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureRelationshipReferenceSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9f863ca5-3631-404c-82-8d-80-7e-07-15-06-9b')
    @commethod(3)
    def Create(sourceUri: Windows.Win32.Storage.Packaging.Opc.IOpcUri_head, digestMethod: Windows.Win32.Foundation.PWSTR, relationshipSigningOption: Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION, selectorSet: Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorSet_head, transformMethod: Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD, relationshipReference: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRelationshipSelectorSet(selectorSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(relationshipReference: Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(relationshipReferenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcSigningOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('50d2d6a5-7aeb-46c0-b2-41-43-ab-0e-9b-40-7e')
    @commethod(3)
    def GetSignatureId(signatureId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSignatureId(signatureId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignatureMethod(signatureMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSignatureMethod(signatureMethod: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultDigestMethod(digestMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDefaultDigestMethod(digestMethod: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCertificateEmbeddingOption(embeddingOption: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCertificateEmbeddingOption(embeddingOption: Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTimeFormat(timeFormat: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimeFormat(timeFormat: Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSignaturePartReferenceSet(partReferenceSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSignatureRelationshipReferenceSet(relationshipReferenceSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCustomObjectSet(customObjectSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCustomReferenceSet(customReferenceSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCertificateSet(certificateSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcCertificateSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSignaturePartName(signaturePartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetSignaturePartName(signaturePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IOpcUri(c_void_p):
    extends: Windows.Win32.System.Com.IUri
    Guid = Guid('bc9c1b9b-d62c-49eb-ae-f0-3b-4e-0b-28-eb-ed')
    @commethod(28)
    def GetRelationshipsPartUri(relationshipPartUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetRelativeUri(targetPartUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, relativeUri: POINTER(Windows.Win32.System.Com.IUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CombinePartUri(relativeUri: Windows.Win32.System.Com.IUri_head, combinedUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
OPC_CANONICALIZATION_METHOD = Int32
OPC_CANONICALIZATION_NONE: OPC_CANONICALIZATION_METHOD = 0
OPC_CANONICALIZATION_C14N: OPC_CANONICALIZATION_METHOD = 1
OPC_CANONICALIZATION_C14N_WITH_COMMENTS: OPC_CANONICALIZATION_METHOD = 2
OPC_CERTIFICATE_EMBEDDING_OPTION = Int32
OPC_CERTIFICATE_IN_CERTIFICATE_PART: OPC_CERTIFICATE_EMBEDDING_OPTION = 0
OPC_CERTIFICATE_IN_SIGNATURE_PART: OPC_CERTIFICATE_EMBEDDING_OPTION = 1
OPC_CERTIFICATE_NOT_EMBEDDED: OPC_CERTIFICATE_EMBEDDING_OPTION = 2
OPC_COMPRESSION_OPTIONS = Int32
OPC_COMPRESSION_NONE: OPC_COMPRESSION_OPTIONS = -1
OPC_COMPRESSION_NORMAL: OPC_COMPRESSION_OPTIONS = 0
OPC_COMPRESSION_MAXIMUM: OPC_COMPRESSION_OPTIONS = 1
OPC_COMPRESSION_FAST: OPC_COMPRESSION_OPTIONS = 2
OPC_COMPRESSION_SUPERFAST: OPC_COMPRESSION_OPTIONS = 3
OPC_READ_FLAGS = Int32
OPC_READ_DEFAULT: OPC_READ_FLAGS = 0
OPC_VALIDATE_ON_LOAD: OPC_READ_FLAGS = 1
OPC_CACHE_ON_ACCESS: OPC_READ_FLAGS = 2
OPC_RELATIONSHIPS_SIGNING_OPTION = Int32
OPC_RELATIONSHIP_SIGN_USING_SELECTORS: OPC_RELATIONSHIPS_SIGNING_OPTION = 0
OPC_RELATIONSHIP_SIGN_PART: OPC_RELATIONSHIPS_SIGNING_OPTION = 1
OPC_RELATIONSHIP_SELECTOR = Int32
OPC_RELATIONSHIP_SELECT_BY_ID: OPC_RELATIONSHIP_SELECTOR = 0
OPC_RELATIONSHIP_SELECT_BY_TYPE: OPC_RELATIONSHIP_SELECTOR = 1
OPC_SIGNATURE_TIME_FORMAT = Int32
OPC_SIGNATURE_TIME_FORMAT_MILLISECONDS: OPC_SIGNATURE_TIME_FORMAT = 0
OPC_SIGNATURE_TIME_FORMAT_SECONDS: OPC_SIGNATURE_TIME_FORMAT = 1
OPC_SIGNATURE_TIME_FORMAT_MINUTES: OPC_SIGNATURE_TIME_FORMAT = 2
OPC_SIGNATURE_TIME_FORMAT_DAYS: OPC_SIGNATURE_TIME_FORMAT = 3
OPC_SIGNATURE_TIME_FORMAT_MONTHS: OPC_SIGNATURE_TIME_FORMAT = 4
OPC_SIGNATURE_TIME_FORMAT_YEARS: OPC_SIGNATURE_TIME_FORMAT = 5
OPC_SIGNATURE_VALIDATION_RESULT = Int32
OPC_SIGNATURE_VALID: OPC_SIGNATURE_VALIDATION_RESULT = 0
OPC_SIGNATURE_INVALID: OPC_SIGNATURE_VALIDATION_RESULT = -1
OPC_STREAM_IO_MODE = Int32
OPC_STREAM_IO_READ: OPC_STREAM_IO_MODE = 1
OPC_STREAM_IO_WRITE: OPC_STREAM_IO_MODE = 2
OPC_URI_TARGET_MODE = Int32
OPC_URI_TARGET_MODE_INTERNAL: OPC_URI_TARGET_MODE = 0
OPC_URI_TARGET_MODE_EXTERNAL: OPC_URI_TARGET_MODE = 1
OPC_WRITE_FLAGS = Int32
OPC_WRITE_DEFAULT: OPC_WRITE_FLAGS = 0
OPC_WRITE_FORCE_ZIP32: OPC_WRITE_FLAGS = 1
OpcFactory = Guid('6b2d6ba0-9f3e-4f27-92-0b-31-3c-c4-26-a3-9e')
make_head(_module, 'IOpcCertificateEnumerator')
make_head(_module, 'IOpcCertificateSet')
make_head(_module, 'IOpcDigitalSignature')
make_head(_module, 'IOpcDigitalSignatureEnumerator')
make_head(_module, 'IOpcDigitalSignatureManager')
make_head(_module, 'IOpcFactory')
make_head(_module, 'IOpcPackage')
make_head(_module, 'IOpcPart')
make_head(_module, 'IOpcPartEnumerator')
make_head(_module, 'IOpcPartSet')
make_head(_module, 'IOpcPartUri')
make_head(_module, 'IOpcRelationship')
make_head(_module, 'IOpcRelationshipEnumerator')
make_head(_module, 'IOpcRelationshipSelector')
make_head(_module, 'IOpcRelationshipSelectorEnumerator')
make_head(_module, 'IOpcRelationshipSelectorSet')
make_head(_module, 'IOpcRelationshipSet')
make_head(_module, 'IOpcSignatureCustomObject')
make_head(_module, 'IOpcSignatureCustomObjectEnumerator')
make_head(_module, 'IOpcSignatureCustomObjectSet')
make_head(_module, 'IOpcSignaturePartReference')
make_head(_module, 'IOpcSignaturePartReferenceEnumerator')
make_head(_module, 'IOpcSignaturePartReferenceSet')
make_head(_module, 'IOpcSignatureReference')
make_head(_module, 'IOpcSignatureReferenceEnumerator')
make_head(_module, 'IOpcSignatureReferenceSet')
make_head(_module, 'IOpcSignatureRelationshipReference')
make_head(_module, 'IOpcSignatureRelationshipReferenceEnumerator')
make_head(_module, 'IOpcSignatureRelationshipReferenceSet')
make_head(_module, 'IOpcSigningOptions')
make_head(_module, 'IOpcUri')
__all__ = [
    "IOpcCertificateEnumerator",
    "IOpcCertificateSet",
    "IOpcDigitalSignature",
    "IOpcDigitalSignatureEnumerator",
    "IOpcDigitalSignatureManager",
    "IOpcFactory",
    "IOpcPackage",
    "IOpcPart",
    "IOpcPartEnumerator",
    "IOpcPartSet",
    "IOpcPartUri",
    "IOpcRelationship",
    "IOpcRelationshipEnumerator",
    "IOpcRelationshipSelector",
    "IOpcRelationshipSelectorEnumerator",
    "IOpcRelationshipSelectorSet",
    "IOpcRelationshipSet",
    "IOpcSignatureCustomObject",
    "IOpcSignatureCustomObjectEnumerator",
    "IOpcSignatureCustomObjectSet",
    "IOpcSignaturePartReference",
    "IOpcSignaturePartReferenceEnumerator",
    "IOpcSignaturePartReferenceSet",
    "IOpcSignatureReference",
    "IOpcSignatureReferenceEnumerator",
    "IOpcSignatureReferenceSet",
    "IOpcSignatureRelationshipReference",
    "IOpcSignatureRelationshipReferenceEnumerator",
    "IOpcSignatureRelationshipReferenceSet",
    "IOpcSigningOptions",
    "IOpcUri",
    "OPC_CACHE_ON_ACCESS",
    "OPC_CANONICALIZATION_C14N",
    "OPC_CANONICALIZATION_C14N_WITH_COMMENTS",
    "OPC_CANONICALIZATION_METHOD",
    "OPC_CANONICALIZATION_NONE",
    "OPC_CERTIFICATE_EMBEDDING_OPTION",
    "OPC_CERTIFICATE_IN_CERTIFICATE_PART",
    "OPC_CERTIFICATE_IN_SIGNATURE_PART",
    "OPC_CERTIFICATE_NOT_EMBEDDED",
    "OPC_COMPRESSION_FAST",
    "OPC_COMPRESSION_MAXIMUM",
    "OPC_COMPRESSION_NONE",
    "OPC_COMPRESSION_NORMAL",
    "OPC_COMPRESSION_OPTIONS",
    "OPC_COMPRESSION_SUPERFAST",
    "OPC_E_CONFLICTING_SETTINGS",
    "OPC_E_COULD_NOT_RECOVER",
    "OPC_E_DS_DEFAULT_DIGEST_METHOD_NOT_SET",
    "OPC_E_DS_DIGEST_VALUE_ERROR",
    "OPC_E_DS_DUPLICATE_PACKAGE_OBJECT_REFERENCES",
    "OPC_E_DS_DUPLICATE_SIGNATURE_ORIGIN_RELATIONSHIP",
    "OPC_E_DS_DUPLICATE_SIGNATURE_PROPERTY_ELEMENT",
    "OPC_E_DS_EXTERNAL_SIGNATURE",
    "OPC_E_DS_EXTERNAL_SIGNATURE_REFERENCE",
    "OPC_E_DS_INVALID_CANONICALIZATION_METHOD",
    "OPC_E_DS_INVALID_CERTIFICATE_RELATIONSHIP",
    "OPC_E_DS_INVALID_OPC_SIGNATURE_TIME_FORMAT",
    "OPC_E_DS_INVALID_RELATIONSHIPS_SIGNING_OPTION",
    "OPC_E_DS_INVALID_RELATIONSHIP_TRANSFORM_XML",
    "OPC_E_DS_INVALID_SIGNATURE_COUNT",
    "OPC_E_DS_INVALID_SIGNATURE_ORIGIN_RELATIONSHIP",
    "OPC_E_DS_INVALID_SIGNATURE_XML",
    "OPC_E_DS_MISSING_CANONICALIZATION_TRANSFORM",
    "OPC_E_DS_MISSING_CERTIFICATE_PART",
    "OPC_E_DS_MISSING_PACKAGE_OBJECT_REFERENCE",
    "OPC_E_DS_MISSING_SIGNATURE_ALGORITHM",
    "OPC_E_DS_MISSING_SIGNATURE_ORIGIN_PART",
    "OPC_E_DS_MISSING_SIGNATURE_PART",
    "OPC_E_DS_MISSING_SIGNATURE_PROPERTIES_ELEMENT",
    "OPC_E_DS_MISSING_SIGNATURE_PROPERTY_ELEMENT",
    "OPC_E_DS_MISSING_SIGNATURE_TIME_PROPERTY",
    "OPC_E_DS_MULTIPLE_RELATIONSHIP_TRANSFORMS",
    "OPC_E_DS_PACKAGE_REFERENCE_URI_RESERVED",
    "OPC_E_DS_REFERENCE_MISSING_CONTENT_TYPE",
    "OPC_E_DS_SIGNATURE_CORRUPT",
    "OPC_E_DS_SIGNATURE_METHOD_NOT_SET",
    "OPC_E_DS_SIGNATURE_ORIGIN_EXISTS",
    "OPC_E_DS_SIGNATURE_PROPERTY_MISSING_TARGET",
    "OPC_E_DS_SIGNATURE_REFERENCE_MISSING_URI",
    "OPC_E_DS_UNSIGNED_PACKAGE",
    "OPC_E_DUPLICATE_DEFAULT_EXTENSION",
    "OPC_E_DUPLICATE_OVERRIDE_PART",
    "OPC_E_DUPLICATE_PART",
    "OPC_E_DUPLICATE_PIECE",
    "OPC_E_DUPLICATE_RELATIONSHIP",
    "OPC_E_ENUM_CANNOT_MOVE_NEXT",
    "OPC_E_ENUM_CANNOT_MOVE_PREVIOUS",
    "OPC_E_ENUM_COLLECTION_CHANGED",
    "OPC_E_ENUM_INVALID_POSITION",
    "OPC_E_INVALID_CONTENT_TYPE",
    "OPC_E_INVALID_CONTENT_TYPE_XML",
    "OPC_E_INVALID_DEFAULT_EXTENSION",
    "OPC_E_INVALID_OVERRIDE_PART_NAME",
    "OPC_E_INVALID_PIECE",
    "OPC_E_INVALID_RELATIONSHIP_ID",
    "OPC_E_INVALID_RELATIONSHIP_TARGET",
    "OPC_E_INVALID_RELATIONSHIP_TARGET_MODE",
    "OPC_E_INVALID_RELATIONSHIP_TYPE",
    "OPC_E_INVALID_RELS_XML",
    "OPC_E_INVALID_XML_ENCODING",
    "OPC_E_MC_INCONSISTENT_PRESERVE_ATTRIBUTES",
    "OPC_E_MC_INCONSISTENT_PRESERVE_ELEMENTS",
    "OPC_E_MC_INCONSISTENT_PROCESS_CONTENT",
    "OPC_E_MC_INVALID_ATTRIBUTES_ON_IGNORABLE_ELEMENT",
    "OPC_E_MC_INVALID_ENUM_TYPE",
    "OPC_E_MC_INVALID_PREFIX_LIST",
    "OPC_E_MC_INVALID_QNAME_LIST",
    "OPC_E_MC_INVALID_XMLNS_ATTRIBUTE",
    "OPC_E_MC_MISSING_CHOICE",
    "OPC_E_MC_MISSING_REQUIRES_ATTR",
    "OPC_E_MC_MULTIPLE_FALLBACK_ELEMENTS",
    "OPC_E_MC_NESTED_ALTERNATE_CONTENT",
    "OPC_E_MC_UNEXPECTED_ATTR",
    "OPC_E_MC_UNEXPECTED_CHOICE",
    "OPC_E_MC_UNEXPECTED_ELEMENT",
    "OPC_E_MC_UNEXPECTED_REQUIRES_ATTR",
    "OPC_E_MC_UNKNOWN_NAMESPACE",
    "OPC_E_MC_UNKNOWN_PREFIX",
    "OPC_E_MISSING_CONTENT_TYPES",
    "OPC_E_MISSING_PIECE",
    "OPC_E_NONCONFORMING_CONTENT_TYPES_XML",
    "OPC_E_NONCONFORMING_RELS_XML",
    "OPC_E_NONCONFORMING_URI",
    "OPC_E_NO_SUCH_PART",
    "OPC_E_NO_SUCH_RELATIONSHIP",
    "OPC_E_NO_SUCH_SETTINGS",
    "OPC_E_PART_CANNOT_BE_DIRECTORY",
    "OPC_E_RELATIONSHIP_URI_REQUIRED",
    "OPC_E_RELATIVE_URI_REQUIRED",
    "OPC_E_UNEXPECTED_CONTENT_TYPE",
    "OPC_E_UNSUPPORTED_PACKAGE",
    "OPC_E_ZIP_CENTRAL_DIRECTORY_TOO_LARGE",
    "OPC_E_ZIP_COMMENT_TOO_LARGE",
    "OPC_E_ZIP_COMPRESSION_FAILED",
    "OPC_E_ZIP_CORRUPTED_ARCHIVE",
    "OPC_E_ZIP_DECOMPRESSION_FAILED",
    "OPC_E_ZIP_DUPLICATE_NAME",
    "OPC_E_ZIP_EXTRA_FIELDS_TOO_LARGE",
    "OPC_E_ZIP_FILE_HEADER_TOO_LARGE",
    "OPC_E_ZIP_INCONSISTENT_DIRECTORY",
    "OPC_E_ZIP_INCONSISTENT_FILEITEM",
    "OPC_E_ZIP_INCORRECT_DATA_SIZE",
    "OPC_E_ZIP_MISSING_DATA_DESCRIPTOR",
    "OPC_E_ZIP_MISSING_END_OF_CENTRAL_DIRECTORY",
    "OPC_E_ZIP_NAME_TOO_LARGE",
    "OPC_E_ZIP_REQUIRES_64_BIT",
    "OPC_E_ZIP_UNSUPPORTEDARCHIVE",
    "OPC_READ_DEFAULT",
    "OPC_READ_FLAGS",
    "OPC_RELATIONSHIPS_SIGNING_OPTION",
    "OPC_RELATIONSHIP_SELECTOR",
    "OPC_RELATIONSHIP_SELECT_BY_ID",
    "OPC_RELATIONSHIP_SELECT_BY_TYPE",
    "OPC_RELATIONSHIP_SIGN_PART",
    "OPC_RELATIONSHIP_SIGN_USING_SELECTORS",
    "OPC_SIGNATURE_INVALID",
    "OPC_SIGNATURE_TIME_FORMAT",
    "OPC_SIGNATURE_TIME_FORMAT_DAYS",
    "OPC_SIGNATURE_TIME_FORMAT_MILLISECONDS",
    "OPC_SIGNATURE_TIME_FORMAT_MINUTES",
    "OPC_SIGNATURE_TIME_FORMAT_MONTHS",
    "OPC_SIGNATURE_TIME_FORMAT_SECONDS",
    "OPC_SIGNATURE_TIME_FORMAT_YEARS",
    "OPC_SIGNATURE_VALID",
    "OPC_SIGNATURE_VALIDATION_RESULT",
    "OPC_STREAM_IO_MODE",
    "OPC_STREAM_IO_READ",
    "OPC_STREAM_IO_WRITE",
    "OPC_URI_TARGET_MODE",
    "OPC_URI_TARGET_MODE_EXTERNAL",
    "OPC_URI_TARGET_MODE_INTERNAL",
    "OPC_VALIDATE_ON_LOAD",
    "OPC_WRITE_DEFAULT",
    "OPC_WRITE_FLAGS",
    "OPC_WRITE_FORCE_ZIP32",
    "OpcFactory",
]
_arch_optional = [
]
