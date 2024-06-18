from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Storage.Packaging.Opc
import win32more.Windows.Win32.System.Com
OPC_E_NONCONFORMING_URI: win32more.Windows.Win32.Foundation.HRESULT = -2142175231
OPC_E_RELATIVE_URI_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2142175230
OPC_E_RELATIONSHIP_URI_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2142175229
OPC_E_PART_CANNOT_BE_DIRECTORY: win32more.Windows.Win32.Foundation.HRESULT = -2142175228
OPC_E_UNEXPECTED_CONTENT_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2142175227
OPC_E_INVALID_CONTENT_TYPE_XML: win32more.Windows.Win32.Foundation.HRESULT = -2142175226
OPC_E_MISSING_CONTENT_TYPES: win32more.Windows.Win32.Foundation.HRESULT = -2142175225
OPC_E_NONCONFORMING_CONTENT_TYPES_XML: win32more.Windows.Win32.Foundation.HRESULT = -2142175224
OPC_E_NONCONFORMING_RELS_XML: win32more.Windows.Win32.Foundation.HRESULT = -2142175223
OPC_E_INVALID_RELS_XML: win32more.Windows.Win32.Foundation.HRESULT = -2142175222
OPC_E_DUPLICATE_PART: win32more.Windows.Win32.Foundation.HRESULT = -2142175221
OPC_E_INVALID_OVERRIDE_PART_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2142175220
OPC_E_DUPLICATE_OVERRIDE_PART: win32more.Windows.Win32.Foundation.HRESULT = -2142175219
OPC_E_INVALID_DEFAULT_EXTENSION: win32more.Windows.Win32.Foundation.HRESULT = -2142175218
OPC_E_DUPLICATE_DEFAULT_EXTENSION: win32more.Windows.Win32.Foundation.HRESULT = -2142175217
OPC_E_INVALID_RELATIONSHIP_ID: win32more.Windows.Win32.Foundation.HRESULT = -2142175216
OPC_E_INVALID_RELATIONSHIP_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2142175215
OPC_E_INVALID_RELATIONSHIP_TARGET: win32more.Windows.Win32.Foundation.HRESULT = -2142175214
OPC_E_DUPLICATE_RELATIONSHIP: win32more.Windows.Win32.Foundation.HRESULT = -2142175213
OPC_E_CONFLICTING_SETTINGS: win32more.Windows.Win32.Foundation.HRESULT = -2142175212
OPC_E_DUPLICATE_PIECE: win32more.Windows.Win32.Foundation.HRESULT = -2142175211
OPC_E_INVALID_PIECE: win32more.Windows.Win32.Foundation.HRESULT = -2142175210
OPC_E_MISSING_PIECE: win32more.Windows.Win32.Foundation.HRESULT = -2142175209
OPC_E_NO_SUCH_PART: win32more.Windows.Win32.Foundation.HRESULT = -2142175208
OPC_E_DS_SIGNATURE_CORRUPT: win32more.Windows.Win32.Foundation.HRESULT = -2142175207
OPC_E_DS_DIGEST_VALUE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2142175206
OPC_E_DS_DUPLICATE_SIGNATURE_ORIGIN_RELATIONSHIP: win32more.Windows.Win32.Foundation.HRESULT = -2142175205
OPC_E_DS_INVALID_SIGNATURE_ORIGIN_RELATIONSHIP: win32more.Windows.Win32.Foundation.HRESULT = -2142175204
OPC_E_DS_INVALID_CERTIFICATE_RELATIONSHIP: win32more.Windows.Win32.Foundation.HRESULT = -2142175203
OPC_E_DS_EXTERNAL_SIGNATURE: win32more.Windows.Win32.Foundation.HRESULT = -2142175202
OPC_E_DS_MISSING_SIGNATURE_ORIGIN_PART: win32more.Windows.Win32.Foundation.HRESULT = -2142175201
OPC_E_DS_MISSING_SIGNATURE_PART: win32more.Windows.Win32.Foundation.HRESULT = -2142175200
OPC_E_DS_INVALID_RELATIONSHIP_TRANSFORM_XML: win32more.Windows.Win32.Foundation.HRESULT = -2142175199
OPC_E_DS_INVALID_CANONICALIZATION_METHOD: win32more.Windows.Win32.Foundation.HRESULT = -2142175198
OPC_E_DS_INVALID_RELATIONSHIPS_SIGNING_OPTION: win32more.Windows.Win32.Foundation.HRESULT = -2142175197
OPC_E_DS_INVALID_OPC_SIGNATURE_TIME_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2142175196
OPC_E_DS_PACKAGE_REFERENCE_URI_RESERVED: win32more.Windows.Win32.Foundation.HRESULT = -2142175195
OPC_E_DS_MISSING_SIGNATURE_PROPERTIES_ELEMENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175194
OPC_E_DS_MISSING_SIGNATURE_PROPERTY_ELEMENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175193
OPC_E_DS_DUPLICATE_SIGNATURE_PROPERTY_ELEMENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175192
OPC_E_DS_MISSING_SIGNATURE_TIME_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -2142175191
OPC_E_DS_INVALID_SIGNATURE_XML: win32more.Windows.Win32.Foundation.HRESULT = -2142175190
OPC_E_DS_INVALID_SIGNATURE_COUNT: win32more.Windows.Win32.Foundation.HRESULT = -2142175189
OPC_E_DS_MISSING_SIGNATURE_ALGORITHM: win32more.Windows.Win32.Foundation.HRESULT = -2142175188
OPC_E_DS_DUPLICATE_PACKAGE_OBJECT_REFERENCES: win32more.Windows.Win32.Foundation.HRESULT = -2142175187
OPC_E_DS_MISSING_PACKAGE_OBJECT_REFERENCE: win32more.Windows.Win32.Foundation.HRESULT = -2142175186
OPC_E_DS_EXTERNAL_SIGNATURE_REFERENCE: win32more.Windows.Win32.Foundation.HRESULT = -2142175185
OPC_E_DS_REFERENCE_MISSING_CONTENT_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2142175184
OPC_E_DS_MULTIPLE_RELATIONSHIP_TRANSFORMS: win32more.Windows.Win32.Foundation.HRESULT = -2142175183
OPC_E_DS_MISSING_CANONICALIZATION_TRANSFORM: win32more.Windows.Win32.Foundation.HRESULT = -2142175182
OPC_E_MC_UNEXPECTED_ELEMENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175181
OPC_E_MC_UNEXPECTED_REQUIRES_ATTR: win32more.Windows.Win32.Foundation.HRESULT = -2142175180
OPC_E_MC_MISSING_REQUIRES_ATTR: win32more.Windows.Win32.Foundation.HRESULT = -2142175179
OPC_E_MC_UNEXPECTED_ATTR: win32more.Windows.Win32.Foundation.HRESULT = -2142175178
OPC_E_MC_INVALID_PREFIX_LIST: win32more.Windows.Win32.Foundation.HRESULT = -2142175177
OPC_E_MC_INVALID_QNAME_LIST: win32more.Windows.Win32.Foundation.HRESULT = -2142175176
OPC_E_MC_NESTED_ALTERNATE_CONTENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175175
OPC_E_MC_UNEXPECTED_CHOICE: win32more.Windows.Win32.Foundation.HRESULT = -2142175174
OPC_E_MC_MISSING_CHOICE: win32more.Windows.Win32.Foundation.HRESULT = -2142175173
OPC_E_MC_INVALID_ENUM_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2142175172
OPC_E_MC_UNKNOWN_NAMESPACE: win32more.Windows.Win32.Foundation.HRESULT = -2142175170
OPC_E_MC_UNKNOWN_PREFIX: win32more.Windows.Win32.Foundation.HRESULT = -2142175169
OPC_E_MC_INVALID_ATTRIBUTES_ON_IGNORABLE_ELEMENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175168
OPC_E_MC_INVALID_XMLNS_ATTRIBUTE: win32more.Windows.Win32.Foundation.HRESULT = -2142175167
OPC_E_INVALID_XML_ENCODING: win32more.Windows.Win32.Foundation.HRESULT = -2142175166
OPC_E_DS_SIGNATURE_REFERENCE_MISSING_URI: win32more.Windows.Win32.Foundation.HRESULT = -2142175165
OPC_E_INVALID_CONTENT_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2142175164
OPC_E_DS_SIGNATURE_PROPERTY_MISSING_TARGET: win32more.Windows.Win32.Foundation.HRESULT = -2142175163
OPC_E_DS_SIGNATURE_METHOD_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2142175162
OPC_E_DS_DEFAULT_DIGEST_METHOD_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2142175161
OPC_E_NO_SUCH_RELATIONSHIP: win32more.Windows.Win32.Foundation.HRESULT = -2142175160
OPC_E_MC_MULTIPLE_FALLBACK_ELEMENTS: win32more.Windows.Win32.Foundation.HRESULT = -2142175159
OPC_E_MC_INCONSISTENT_PROCESS_CONTENT: win32more.Windows.Win32.Foundation.HRESULT = -2142175158
OPC_E_MC_INCONSISTENT_PRESERVE_ATTRIBUTES: win32more.Windows.Win32.Foundation.HRESULT = -2142175157
OPC_E_MC_INCONSISTENT_PRESERVE_ELEMENTS: win32more.Windows.Win32.Foundation.HRESULT = -2142175156
OPC_E_INVALID_RELATIONSHIP_TARGET_MODE: win32more.Windows.Win32.Foundation.HRESULT = -2142175155
OPC_E_COULD_NOT_RECOVER: win32more.Windows.Win32.Foundation.HRESULT = -2142175154
OPC_E_UNSUPPORTED_PACKAGE: win32more.Windows.Win32.Foundation.HRESULT = -2142175153
OPC_E_ENUM_COLLECTION_CHANGED: win32more.Windows.Win32.Foundation.HRESULT = -2142175152
OPC_E_ENUM_CANNOT_MOVE_NEXT: win32more.Windows.Win32.Foundation.HRESULT = -2142175151
OPC_E_ENUM_CANNOT_MOVE_PREVIOUS: win32more.Windows.Win32.Foundation.HRESULT = -2142175150
OPC_E_ENUM_INVALID_POSITION: win32more.Windows.Win32.Foundation.HRESULT = -2142175149
OPC_E_DS_SIGNATURE_ORIGIN_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2142175148
OPC_E_DS_UNSIGNED_PACKAGE: win32more.Windows.Win32.Foundation.HRESULT = -2142175147
OPC_E_DS_MISSING_CERTIFICATE_PART: win32more.Windows.Win32.Foundation.HRESULT = -2142175146
OPC_E_NO_SUCH_SETTINGS: win32more.Windows.Win32.Foundation.HRESULT = -2142175145
OPC_E_ZIP_INCORRECT_DATA_SIZE: win32more.Windows.Win32.Foundation.HRESULT = -2142171135
OPC_E_ZIP_CORRUPTED_ARCHIVE: win32more.Windows.Win32.Foundation.HRESULT = -2142171134
OPC_E_ZIP_COMPRESSION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2142171133
OPC_E_ZIP_DECOMPRESSION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2142171132
OPC_E_ZIP_INCONSISTENT_FILEITEM: win32more.Windows.Win32.Foundation.HRESULT = -2142171131
OPC_E_ZIP_INCONSISTENT_DIRECTORY: win32more.Windows.Win32.Foundation.HRESULT = -2142171130
OPC_E_ZIP_MISSING_DATA_DESCRIPTOR: win32more.Windows.Win32.Foundation.HRESULT = -2142171129
OPC_E_ZIP_UNSUPPORTEDARCHIVE: win32more.Windows.Win32.Foundation.HRESULT = -2142171128
OPC_E_ZIP_CENTRAL_DIRECTORY_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2142171127
OPC_E_ZIP_NAME_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2142171126
OPC_E_ZIP_DUPLICATE_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2142171125
OPC_E_ZIP_COMMENT_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2142171124
OPC_E_ZIP_EXTRA_FIELDS_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2142171123
OPC_E_ZIP_FILE_HEADER_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2142171122
OPC_E_ZIP_MISSING_END_OF_CENTRAL_DIRECTORY: win32more.Windows.Win32.Foundation.HRESULT = -2142171121
OPC_E_ZIP_REQUIRES_64_BIT: win32more.Windows.Win32.Foundation.HRESULT = -2142171120
class IOpcCertificateEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85131937-8f24-421f-b439-59ab24d140b8}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, certificate: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcCertificateSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56ea4325-8e2d-4167-b1a4-e486d24c8fa7}')
    @commethod(3)
    def Add(self, certificate: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, certificate: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(self, certificateEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcDigitalSignature(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52ab21dd-1cd0-4949-bc80-0c1232d00cb4}')
    @commethod(3)
    def GetNamespaces(self, prefixes: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), namespaces: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignatureId(self, signatureId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignaturePartName(self, signaturePartName: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignatureMethod(self, signatureMethod: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCanonicalizationMethod(self, canonicalizationMethod: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignatureValue(self, signatureValue: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSignaturePartReferenceEnumerator(self, partReferenceEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSignatureRelationshipReferenceEnumerator(self, relationshipReferenceEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSigningTime(self, signingTime: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTimeFormat(self, timeFormat: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPackageObjectReference(self, packageObjectReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCertificateEnumerator(self, certificateEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCustomReferenceEnumerator(self, customReferenceEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCustomObjectEnumerator(self, customObjectEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSignatureXml(self, signatureXml: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcDigitalSignatureEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{967b6882-0ba3-4358-b9e7-b64c75063c5e}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, digitalSignature: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcDigitalSignatureManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5e62a0b-696d-462f-94df-72e33cef2659}')
    @commethod(3)
    def GetSignatureOriginPartName(self, signatureOriginPartName: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSignatureOriginPartName(self, signatureOriginPartName: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignatureEnumerator(self, signatureEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveSignature(self, signaturePartName: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateSigningOptions(self, signingOptions: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSigningOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Validate(self, signature: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature, certificate: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), validationResult: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_VALIDATION_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Sign(self, certificate: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), signingOptions: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSigningOptions, digitalSignature: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ReplaceSignatureXml(self, signaturePartName: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, newSignatureXml: POINTER(Byte), count: UInt32, digitalSignature: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignature)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d0b4446-cd73-4ab3-94f4-8ccdf6116154}')
    @commethod(3)
    def CreatePackageRootUri(self, rootUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePartUri(self, pwzUri: win32more.Windows.Win32.Foundation.PWSTR, partUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStreamOnFile(self, filename: win32more.Windows.Win32.Foundation.PWSTR, ioMode: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_STREAM_IO_MODE, securityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwFlagsAndAttributes: UInt32, stream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreatePackage(self, package: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPackage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReadPackageFromStream(self, stream: win32more.Windows.Win32.System.Com.IStream, flags: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_READ_FLAGS, package: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPackage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WritePackageToStream(self, package: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPackage, flags: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_WRITE_FLAGS, stream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateDigitalSignatureManager(self, package: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPackage, signatureManager: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcDigitalSignatureManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcPackage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee70}')
    @commethod(3)
    def GetPartSet(self, partSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRelationshipSet(self, relationshipSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcPart(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee71}')
    @commethod(3)
    def GetRelationshipSet(self, relationshipSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContentStream(self, stream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetName(self, name: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetContentType(self, contentType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCompressionOptions(self, compressionOptions: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcPartEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee75}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, part: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPart)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcPartSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee73}')
    @commethod(3)
    def GetPart(self, name: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, part: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPart)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePart(self, name: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, contentType: win32more.Windows.Win32.Foundation.PWSTR, compressionOptions: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS, part: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPart)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeletePart(self, name: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PartExists(self, name: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, partExists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEnumerator(self, partEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcPartUri(ComPtr):
    extends: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcUri
    _iid_ = Guid('{7d3babe7-88b2-46ba-85cb-4203cb016c87}')
    @commethod(31)
    def ComparePartUri(self, partUri: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, comparisonResult: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetSourceUri(self, sourceUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def IsRelationshipsPartUri(self, isRelationshipUri: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationship(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee72}')
    @commethod(3)
    def GetId(self, relationshipIdentifier: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRelationshipType(self, relationshipType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceUri(self, sourceUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTargetUri(self, targetUri: POINTER(win32more.Windows.Win32.System.Com.IUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTargetMode(self, targetMode: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_URI_TARGET_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee76}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, relationship: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationship)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSelector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f8f26c7f-b28f-4899-84c8-5d5639ede75f}')
    @commethod(3)
    def GetSelectorType(self, selector: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSelectionCriterion(self, selectionCriterion: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSelectorEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e50a181-a91b-48ac-88d2-bca3d8f8c0b1}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, relationshipSelector: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSelectorSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e34c269-a4d3-47c0-b5c4-87ff2b3b6136}')
    @commethod(3)
    def Create(self, selector: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR, selectionCriterion: win32more.Windows.Win32.Foundation.PWSTR, relationshipSelector: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, relationshipSelector: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelector) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(self, relationshipSelectorEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcRelationshipSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42195949-3b79-4fc8-89c6-fc7fb979ee74}')
    @commethod(3)
    def GetRelationship(self, relationshipIdentifier: win32more.Windows.Win32.Foundation.PWSTR, relationship: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationship)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRelationship(self, relationshipIdentifier: win32more.Windows.Win32.Foundation.PWSTR, relationshipType: win32more.Windows.Win32.Foundation.PWSTR, targetUri: win32more.Windows.Win32.System.Com.IUri, targetMode: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_URI_TARGET_MODE, relationship: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationship)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteRelationship(self, relationshipIdentifier: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RelationshipExists(self, relationshipIdentifier: win32more.Windows.Win32.Foundation.PWSTR, relationshipExists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEnumerator(self, relationshipEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnumeratorForType(self, relationshipType: win32more.Windows.Win32.Foundation.PWSTR, relationshipEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRelationshipsContentStream(self, contents: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureCustomObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d77a19e-62c1-44e7-becd-45da5ae51a56}')
    @commethod(3)
    def GetXml(self, xmlMarkup: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureCustomObjectEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5ee4fe1d-e1b0-4683-8079-7ea0fcf80b4c}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, customObject: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureCustomObjectSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f792ac5-7947-4e11-bc3d-2659ff046ae1}')
    @commethod(3)
    def Create(self, xmlMarkup: POINTER(Byte), count: UInt32, customObject: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, customObject: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(self, customObjectEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignaturePartReference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e24231ca-59f4-484e-b64b-36eeda36072c}')
    @commethod(3)
    def GetPartName(self, partName: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContentType(self, contentType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDigestMethod(self, digestMethod: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDigestValue(self, digestValue: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransformMethod(self, transformMethod: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignaturePartReferenceEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{80eb1561-8c77-49cf-8266-459b356ee99a}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, partReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignaturePartReferenceSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6c9fe28c-ecd9-4b22-9d36-7fdde670fec0}')
    @commethod(3)
    def Create(self, partUri: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, digestMethod: win32more.Windows.Win32.Foundation.PWSTR, transformMethod: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD, partReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, partReference: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReference) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(self, partReferenceEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureReference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b47005e-3011-4edc-be6f-0f65e5ab0342}')
    @commethod(3)
    def GetId(self, referenceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUri(self, referenceUri: POINTER(win32more.Windows.Win32.System.Com.IUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(self, type: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformMethod(self, transformMethod: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDigestMethod(self, digestMethod: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDigestValue(self, digestValue: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureReferenceEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cfa59a45-28b1-4868-969e-fa8097fdc12a}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, reference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureReferenceSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f3b02d31-ab12-42dd-9e2f-2b16761c3c1e}')
    @commethod(3)
    def Create(self, referenceUri: win32more.Windows.Win32.System.Com.IUri, referenceId: win32more.Windows.Win32.Foundation.PWSTR, type: win32more.Windows.Win32.Foundation.PWSTR, digestMethod: win32more.Windows.Win32.Foundation.PWSTR, transformMethod: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD, reference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, reference: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReference) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnumerator(self, referenceEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureRelationshipReference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{57babac6-9d4a-4e50-8b86-e5d4051eae7c}')
    @commethod(3)
    def GetSourceUri(self, sourceUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDigestMethod(self, digestMethod: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDigestValue(self, digestValue: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformMethod(self, transformMethod: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRelationshipSigningOption(self, relationshipSigningOption: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRelationshipSelectorEnumerator(self, selectorEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureRelationshipReferenceEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{773ba3e4-f021-48e4-aa04-9816db5d3495}')
    @commethod(3)
    def MoveNext(self, hasNext: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MovePrevious(self, hasPrevious: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, relationshipReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, copy: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSignatureRelationshipReferenceSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f863ca5-3631-404c-828d-807e0715069b}')
    @commethod(3)
    def Create(self, sourceUri: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcUri, digestMethod: win32more.Windows.Win32.Foundation.PWSTR, relationshipSigningOption: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION, selectorSet: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorSet, transformMethod: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD, relationshipReference: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRelationshipSelectorSet(self, selectorSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcRelationshipSelectorSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, relationshipReference: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReference) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(self, relationshipReferenceEnumerator: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcSigningOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50d2d6a5-7aeb-46c0-b241-43ab0e9b407e}')
    @commethod(3)
    def GetSignatureId(self, signatureId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSignatureId(self, signatureId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignatureMethod(self, signatureMethod: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSignatureMethod(self, signatureMethod: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultDigestMethod(self, digestMethod: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDefaultDigestMethod(self, digestMethod: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCertificateEmbeddingOption(self, embeddingOption: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCertificateEmbeddingOption(self, embeddingOption: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTimeFormat(self, timeFormat: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimeFormat(self, timeFormat: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSignaturePartReferenceSet(self, partReferenceSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignaturePartReferenceSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSignatureRelationshipReferenceSet(self, relationshipReferenceSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCustomObjectSet(self, customObjectSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCustomReferenceSet(self, customReferenceSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCertificateSet(self, certificateSet: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcCertificateSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSignaturePartName(self, signaturePartName: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetSignaturePartName(self, signaturePartName: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpcUri(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUri
    _iid_ = Guid('{bc9c1b9b-d62c-49eb-aef0-3b4e0b28ebed}')
    @commethod(28)
    def GetRelationshipsPartUri(self, relationshipPartUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetRelativeUri(self, targetPartUri: win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri, relativeUri: POINTER(win32more.Windows.Win32.System.Com.IUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CombinePartUri(self, relativeUri: win32more.Windows.Win32.System.Com.IUri, combinedUri: POINTER(win32more.Windows.Win32.Storage.Packaging.Opc.IOpcPartUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
OPC_CANONICALIZATION_METHOD = Int32
OPC_CANONICALIZATION_NONE: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD = 0
OPC_CANONICALIZATION_C14N: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD = 1
OPC_CANONICALIZATION_C14N_WITH_COMMENTS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD = 2
OPC_CERTIFICATE_EMBEDDING_OPTION = Int32
OPC_CERTIFICATE_IN_CERTIFICATE_PART: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION = 0
OPC_CERTIFICATE_IN_SIGNATURE_PART: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION = 1
OPC_CERTIFICATE_NOT_EMBEDDED: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION = 2
OPC_COMPRESSION_OPTIONS = Int32
OPC_COMPRESSION_NONE: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS = -1
OPC_COMPRESSION_NORMAL: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS = 0
OPC_COMPRESSION_MAXIMUM: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS = 1
OPC_COMPRESSION_FAST: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS = 2
OPC_COMPRESSION_SUPERFAST: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS = 3
OPC_READ_FLAGS = Int32
OPC_READ_DEFAULT: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_READ_FLAGS = 0
OPC_VALIDATE_ON_LOAD: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_READ_FLAGS = 1
OPC_CACHE_ON_ACCESS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_READ_FLAGS = 2
OPC_RELATIONSHIPS_SIGNING_OPTION = Int32
OPC_RELATIONSHIP_SIGN_USING_SELECTORS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION = 0
OPC_RELATIONSHIP_SIGN_PART: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION = 1
OPC_RELATIONSHIP_SELECTOR = Int32
OPC_RELATIONSHIP_SELECT_BY_ID: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR = 0
OPC_RELATIONSHIP_SELECT_BY_TYPE: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR = 1
OPC_SIGNATURE_TIME_FORMAT = Int32
OPC_SIGNATURE_TIME_FORMAT_MILLISECONDS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT = 0
OPC_SIGNATURE_TIME_FORMAT_SECONDS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT = 1
OPC_SIGNATURE_TIME_FORMAT_MINUTES: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT = 2
OPC_SIGNATURE_TIME_FORMAT_DAYS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT = 3
OPC_SIGNATURE_TIME_FORMAT_MONTHS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT = 4
OPC_SIGNATURE_TIME_FORMAT_YEARS: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT = 5
OPC_SIGNATURE_VALIDATION_RESULT = Int32
OPC_SIGNATURE_VALID: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_VALIDATION_RESULT = 0
OPC_SIGNATURE_INVALID: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_VALIDATION_RESULT = -1
OPC_STREAM_IO_MODE = Int32
OPC_STREAM_IO_READ: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_STREAM_IO_MODE = 1
OPC_STREAM_IO_WRITE: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_STREAM_IO_MODE = 2
OPC_URI_TARGET_MODE = Int32
OPC_URI_TARGET_MODE_INTERNAL: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_URI_TARGET_MODE = 0
OPC_URI_TARGET_MODE_EXTERNAL: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_URI_TARGET_MODE = 1
OPC_WRITE_FLAGS = Int32
OPC_WRITE_DEFAULT: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_WRITE_FLAGS = 0
OPC_WRITE_FORCE_ZIP32: win32more.Windows.Win32.Storage.Packaging.Opc.OPC_WRITE_FLAGS = 1
OpcFactory = Guid('{6b2d6ba0-9f3e-4f27-920b-313cc426a39e}')


make_ready(__name__)
