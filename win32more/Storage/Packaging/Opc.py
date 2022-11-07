from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Security.Cryptography
import win32more.Storage.Packaging.Opc
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
OPC_E_NONCONFORMING_URI = -2142175231
OPC_E_RELATIVE_URI_REQUIRED = -2142175230
OPC_E_RELATIONSHIP_URI_REQUIRED = -2142175229
OPC_E_PART_CANNOT_BE_DIRECTORY = -2142175228
OPC_E_UNEXPECTED_CONTENT_TYPE = -2142175227
OPC_E_INVALID_CONTENT_TYPE_XML = -2142175226
OPC_E_MISSING_CONTENT_TYPES = -2142175225
OPC_E_NONCONFORMING_CONTENT_TYPES_XML = -2142175224
OPC_E_NONCONFORMING_RELS_XML = -2142175223
OPC_E_INVALID_RELS_XML = -2142175222
OPC_E_DUPLICATE_PART = -2142175221
OPC_E_INVALID_OVERRIDE_PART_NAME = -2142175220
OPC_E_DUPLICATE_OVERRIDE_PART = -2142175219
OPC_E_INVALID_DEFAULT_EXTENSION = -2142175218
OPC_E_DUPLICATE_DEFAULT_EXTENSION = -2142175217
OPC_E_INVALID_RELATIONSHIP_ID = -2142175216
OPC_E_INVALID_RELATIONSHIP_TYPE = -2142175215
OPC_E_INVALID_RELATIONSHIP_TARGET = -2142175214
OPC_E_DUPLICATE_RELATIONSHIP = -2142175213
OPC_E_CONFLICTING_SETTINGS = -2142175212
OPC_E_DUPLICATE_PIECE = -2142175211
OPC_E_INVALID_PIECE = -2142175210
OPC_E_MISSING_PIECE = -2142175209
OPC_E_NO_SUCH_PART = -2142175208
OPC_E_DS_SIGNATURE_CORRUPT = -2142175207
OPC_E_DS_DIGEST_VALUE_ERROR = -2142175206
OPC_E_DS_DUPLICATE_SIGNATURE_ORIGIN_RELATIONSHIP = -2142175205
OPC_E_DS_INVALID_SIGNATURE_ORIGIN_RELATIONSHIP = -2142175204
OPC_E_DS_INVALID_CERTIFICATE_RELATIONSHIP = -2142175203
OPC_E_DS_EXTERNAL_SIGNATURE = -2142175202
OPC_E_DS_MISSING_SIGNATURE_ORIGIN_PART = -2142175201
OPC_E_DS_MISSING_SIGNATURE_PART = -2142175200
OPC_E_DS_INVALID_RELATIONSHIP_TRANSFORM_XML = -2142175199
OPC_E_DS_INVALID_CANONICALIZATION_METHOD = -2142175198
OPC_E_DS_INVALID_RELATIONSHIPS_SIGNING_OPTION = -2142175197
OPC_E_DS_INVALID_OPC_SIGNATURE_TIME_FORMAT = -2142175196
OPC_E_DS_PACKAGE_REFERENCE_URI_RESERVED = -2142175195
OPC_E_DS_MISSING_SIGNATURE_PROPERTIES_ELEMENT = -2142175194
OPC_E_DS_MISSING_SIGNATURE_PROPERTY_ELEMENT = -2142175193
OPC_E_DS_DUPLICATE_SIGNATURE_PROPERTY_ELEMENT = -2142175192
OPC_E_DS_MISSING_SIGNATURE_TIME_PROPERTY = -2142175191
OPC_E_DS_INVALID_SIGNATURE_XML = -2142175190
OPC_E_DS_INVALID_SIGNATURE_COUNT = -2142175189
OPC_E_DS_MISSING_SIGNATURE_ALGORITHM = -2142175188
OPC_E_DS_DUPLICATE_PACKAGE_OBJECT_REFERENCES = -2142175187
OPC_E_DS_MISSING_PACKAGE_OBJECT_REFERENCE = -2142175186
OPC_E_DS_EXTERNAL_SIGNATURE_REFERENCE = -2142175185
OPC_E_DS_REFERENCE_MISSING_CONTENT_TYPE = -2142175184
OPC_E_DS_MULTIPLE_RELATIONSHIP_TRANSFORMS = -2142175183
OPC_E_DS_MISSING_CANONICALIZATION_TRANSFORM = -2142175182
OPC_E_MC_UNEXPECTED_ELEMENT = -2142175181
OPC_E_MC_UNEXPECTED_REQUIRES_ATTR = -2142175180
OPC_E_MC_MISSING_REQUIRES_ATTR = -2142175179
OPC_E_MC_UNEXPECTED_ATTR = -2142175178
OPC_E_MC_INVALID_PREFIX_LIST = -2142175177
OPC_E_MC_INVALID_QNAME_LIST = -2142175176
OPC_E_MC_NESTED_ALTERNATE_CONTENT = -2142175175
OPC_E_MC_UNEXPECTED_CHOICE = -2142175174
OPC_E_MC_MISSING_CHOICE = -2142175173
OPC_E_MC_INVALID_ENUM_TYPE = -2142175172
OPC_E_MC_UNKNOWN_NAMESPACE = -2142175170
OPC_E_MC_UNKNOWN_PREFIX = -2142175169
OPC_E_MC_INVALID_ATTRIBUTES_ON_IGNORABLE_ELEMENT = -2142175168
OPC_E_MC_INVALID_XMLNS_ATTRIBUTE = -2142175167
OPC_E_INVALID_XML_ENCODING = -2142175166
OPC_E_DS_SIGNATURE_REFERENCE_MISSING_URI = -2142175165
OPC_E_INVALID_CONTENT_TYPE = -2142175164
OPC_E_DS_SIGNATURE_PROPERTY_MISSING_TARGET = -2142175163
OPC_E_DS_SIGNATURE_METHOD_NOT_SET = -2142175162
OPC_E_DS_DEFAULT_DIGEST_METHOD_NOT_SET = -2142175161
OPC_E_NO_SUCH_RELATIONSHIP = -2142175160
OPC_E_MC_MULTIPLE_FALLBACK_ELEMENTS = -2142175159
OPC_E_MC_INCONSISTENT_PROCESS_CONTENT = -2142175158
OPC_E_MC_INCONSISTENT_PRESERVE_ATTRIBUTES = -2142175157
OPC_E_MC_INCONSISTENT_PRESERVE_ELEMENTS = -2142175156
OPC_E_INVALID_RELATIONSHIP_TARGET_MODE = -2142175155
OPC_E_COULD_NOT_RECOVER = -2142175154
OPC_E_UNSUPPORTED_PACKAGE = -2142175153
OPC_E_ENUM_COLLECTION_CHANGED = -2142175152
OPC_E_ENUM_CANNOT_MOVE_NEXT = -2142175151
OPC_E_ENUM_CANNOT_MOVE_PREVIOUS = -2142175150
OPC_E_ENUM_INVALID_POSITION = -2142175149
OPC_E_DS_SIGNATURE_ORIGIN_EXISTS = -2142175148
OPC_E_DS_UNSIGNED_PACKAGE = -2142175147
OPC_E_DS_MISSING_CERTIFICATE_PART = -2142175146
OPC_E_NO_SUCH_SETTINGS = -2142175145
OPC_E_ZIP_INCORRECT_DATA_SIZE = -2142171135
OPC_E_ZIP_CORRUPTED_ARCHIVE = -2142171134
OPC_E_ZIP_COMPRESSION_FAILED = -2142171133
OPC_E_ZIP_DECOMPRESSION_FAILED = -2142171132
OPC_E_ZIP_INCONSISTENT_FILEITEM = -2142171131
OPC_E_ZIP_INCONSISTENT_DIRECTORY = -2142171130
OPC_E_ZIP_MISSING_DATA_DESCRIPTOR = -2142171129
OPC_E_ZIP_UNSUPPORTEDARCHIVE = -2142171128
OPC_E_ZIP_CENTRAL_DIRECTORY_TOO_LARGE = -2142171127
OPC_E_ZIP_NAME_TOO_LARGE = -2142171126
OPC_E_ZIP_DUPLICATE_NAME = -2142171125
OPC_E_ZIP_COMMENT_TOO_LARGE = -2142171124
OPC_E_ZIP_EXTRA_FIELDS_TOO_LARGE = -2142171123
OPC_E_ZIP_FILE_HEADER_TOO_LARGE = -2142171122
OPC_E_ZIP_MISSING_END_OF_CENTRAL_DIRECTORY = -2142171121
OPC_E_ZIP_REQUIRES_64_BIT = -2142171120
OpcFactory = Guid('6b2d6ba0-9f3e-4f27-920b-313cc426a39e')
def _define_IOpcUri_head():
    class IOpcUri(win32more.System.Com.IUri_head):
        Guid = Guid('bc9c1b9b-d62c-49eb-aef0-3b4e0b28ebed')
    return IOpcUri
def _define_IOpcUri():
    IOpcUri = win32more.Storage.Packaging.Opc.IOpcUri_head
    IOpcUri.GetRelationshipsPartUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(28, 'GetRelationshipsPartUri', ((1, 'relationshipPartUri'),)))
    IOpcUri.GetRelativeUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.System.Com.IUri_head), use_last_error=False)(29, 'GetRelativeUri', ((1, 'targetPartUri'),(1, 'relativeUri'),)))
    IOpcUri.CombinePartUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(30, 'CombinePartUri', ((1, 'relativeUri'),(1, 'combinedUri'),)))
    win32more.System.Com.IUri
    return IOpcUri
def _define_IOpcPartUri_head():
    class IOpcPartUri(win32more.Storage.Packaging.Opc.IOpcUri_head):
        Guid = Guid('7d3babe7-88b2-46ba-85cb-4203cb016c87')
    return IOpcPartUri
def _define_IOpcPartUri():
    IOpcPartUri = win32more.Storage.Packaging.Opc.IOpcPartUri_head
    IOpcPartUri.ComparePartUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(Int32), use_last_error=False)(31, 'ComparePartUri', ((1, 'partUri'),(1, 'comparisonResult'),)))
    IOpcPartUri.GetSourceUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcUri_head), use_last_error=False)(32, 'GetSourceUri', ((1, 'sourceUri'),)))
    IOpcPartUri.IsRelationshipsPartUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(33, 'IsRelationshipsPartUri', ((1, 'isRelationshipUri'),)))
    win32more.Storage.Packaging.Opc.IOpcUri
    return IOpcPartUri
OPC_URI_TARGET_MODE = Int32
OPC_URI_TARGET_MODE_INTERNAL = 0
OPC_URI_TARGET_MODE_EXTERNAL = 1
OPC_COMPRESSION_OPTIONS = Int32
OPC_COMPRESSION_NONE = -1
OPC_COMPRESSION_NORMAL = 0
OPC_COMPRESSION_MAXIMUM = 1
OPC_COMPRESSION_FAST = 2
OPC_COMPRESSION_SUPERFAST = 3
OPC_STREAM_IO_MODE = Int32
OPC_STREAM_IO_READ = 1
OPC_STREAM_IO_WRITE = 2
OPC_READ_FLAGS = UInt32
OPC_READ_DEFAULT = 0
OPC_VALIDATE_ON_LOAD = 1
OPC_CACHE_ON_ACCESS = 2
OPC_WRITE_FLAGS = UInt32
OPC_WRITE_DEFAULT = 0
OPC_WRITE_FORCE_ZIP32 = 1
OPC_SIGNATURE_VALIDATION_RESULT = Int32
OPC_SIGNATURE_VALID = 0
OPC_SIGNATURE_INVALID = -1
OPC_CANONICALIZATION_METHOD = Int32
OPC_CANONICALIZATION_NONE = 0
OPC_CANONICALIZATION_C14N = 1
OPC_CANONICALIZATION_C14N_WITH_COMMENTS = 2
OPC_RELATIONSHIP_SELECTOR = Int32
OPC_RELATIONSHIP_SELECT_BY_ID = 0
OPC_RELATIONSHIP_SELECT_BY_TYPE = 1
OPC_RELATIONSHIPS_SIGNING_OPTION = Int32
OPC_RELATIONSHIP_SIGN_USING_SELECTORS = 0
OPC_RELATIONSHIP_SIGN_PART = 1
OPC_CERTIFICATE_EMBEDDING_OPTION = Int32
OPC_CERTIFICATE_IN_CERTIFICATE_PART = 0
OPC_CERTIFICATE_IN_SIGNATURE_PART = 1
OPC_CERTIFICATE_NOT_EMBEDDED = 2
OPC_SIGNATURE_TIME_FORMAT = Int32
OPC_SIGNATURE_TIME_FORMAT_MILLISECONDS = 0
OPC_SIGNATURE_TIME_FORMAT_SECONDS = 1
OPC_SIGNATURE_TIME_FORMAT_MINUTES = 2
OPC_SIGNATURE_TIME_FORMAT_DAYS = 3
OPC_SIGNATURE_TIME_FORMAT_MONTHS = 4
OPC_SIGNATURE_TIME_FORMAT_YEARS = 5
def _define_IOpcPackage_head():
    class IOpcPackage(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee70')
    return IOpcPackage
def _define_IOpcPackage():
    IOpcPackage = win32more.Storage.Packaging.Opc.IOpcPackage_head
    IOpcPackage.GetPartSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartSet_head), use_last_error=False)(3, 'GetPartSet', ((1, 'partSet'),)))
    IOpcPackage.GetRelationshipSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSet_head), use_last_error=False)(4, 'GetRelationshipSet', ((1, 'relationshipSet'),)))
    win32more.System.Com.IUnknown
    return IOpcPackage
def _define_IOpcPart_head():
    class IOpcPart(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee71')
    return IOpcPart
def _define_IOpcPart():
    IOpcPart = win32more.Storage.Packaging.Opc.IOpcPart_head
    IOpcPart.GetRelationshipSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSet_head), use_last_error=False)(3, 'GetRelationshipSet', ((1, 'relationshipSet'),)))
    IOpcPart.GetContentStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(4, 'GetContentStream', ((1, 'stream'),)))
    IOpcPart.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(5, 'GetName', ((1, 'name'),)))
    IOpcPart.GetContentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetContentType', ((1, 'contentType'),)))
    IOpcPart.GetCompressionOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS), use_last_error=False)(7, 'GetCompressionOptions', ((1, 'compressionOptions'),)))
    win32more.System.Com.IUnknown
    return IOpcPart
def _define_IOpcRelationship_head():
    class IOpcRelationship(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee72')
    return IOpcRelationship
def _define_IOpcRelationship():
    IOpcRelationship = win32more.Storage.Packaging.Opc.IOpcRelationship_head
    IOpcRelationship.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetId', ((1, 'relationshipIdentifier'),)))
    IOpcRelationship.GetRelationshipType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetRelationshipType', ((1, 'relationshipType'),)))
    IOpcRelationship.GetSourceUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcUri_head), use_last_error=False)(5, 'GetSourceUri', ((1, 'sourceUri'),)))
    IOpcRelationship.GetTargetUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUri_head), use_last_error=False)(6, 'GetTargetUri', ((1, 'targetUri'),)))
    IOpcRelationship.GetTargetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_URI_TARGET_MODE), use_last_error=False)(7, 'GetTargetMode', ((1, 'targetMode'),)))
    win32more.System.Com.IUnknown
    return IOpcRelationship
def _define_IOpcPartSet_head():
    class IOpcPartSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee73')
    return IOpcPartSet
def _define_IOpcPartSet():
    IOpcPartSet = win32more.Storage.Packaging.Opc.IOpcPartSet_head
    IOpcPartSet.GetPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Packaging.Opc.IOpcPart_head), use_last_error=False)(3, 'GetPart', ((1, 'name'),(1, 'part'),)))
    IOpcPartSet.CreatePart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.OPC_COMPRESSION_OPTIONS,POINTER(win32more.Storage.Packaging.Opc.IOpcPart_head), use_last_error=False)(4, 'CreatePart', ((1, 'name'),(1, 'contentType'),(1, 'compressionOptions'),(1, 'part'),)))
    IOpcPartSet.DeletePart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head, use_last_error=False)(5, 'DeletePart', ((1, 'name'),)))
    IOpcPartSet.PartExists = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'PartExists', ((1, 'name'),(1, 'partExists'),)))
    IOpcPartSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartEnumerator_head), use_last_error=False)(7, 'GetEnumerator', ((1, 'partEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcPartSet
def _define_IOpcRelationshipSet_head():
    class IOpcRelationshipSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee74')
    return IOpcRelationshipSet
def _define_IOpcRelationshipSet():
    IOpcRelationshipSet = win32more.Storage.Packaging.Opc.IOpcRelationshipSet_head
    IOpcRelationshipSet.GetRelationship = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationship_head), use_last_error=False)(3, 'GetRelationship', ((1, 'relationshipIdentifier'),(1, 'relationship'),)))
    IOpcRelationshipSet.CreateRelationship = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.IUri_head,win32more.Storage.Packaging.Opc.OPC_URI_TARGET_MODE,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationship_head), use_last_error=False)(4, 'CreateRelationship', ((1, 'relationshipIdentifier'),(1, 'relationshipType'),(1, 'targetUri'),(1, 'targetMode'),(1, 'relationship'),)))
    IOpcRelationshipSet.DeleteRelationship = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'DeleteRelationship', ((1, 'relationshipIdentifier'),)))
    IOpcRelationshipSet.RelationshipExists = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'RelationshipExists', ((1, 'relationshipIdentifier'),(1, 'relationshipExists'),)))
    IOpcRelationshipSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head), use_last_error=False)(7, 'GetEnumerator', ((1, 'relationshipEnumerator'),)))
    IOpcRelationshipSet.GetEnumeratorForType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head), use_last_error=False)(8, 'GetEnumeratorForType', ((1, 'relationshipType'),(1, 'relationshipEnumerator'),)))
    IOpcRelationshipSet.GetRelationshipsContentStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(9, 'GetRelationshipsContentStream', ((1, 'contents'),)))
    win32more.System.Com.IUnknown
    return IOpcRelationshipSet
def _define_IOpcPartEnumerator_head():
    class IOpcPartEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee75')
    return IOpcPartEnumerator
def _define_IOpcPartEnumerator():
    IOpcPartEnumerator = win32more.Storage.Packaging.Opc.IOpcPartEnumerator_head
    IOpcPartEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcPartEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcPartEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPart_head), use_last_error=False)(5, 'GetCurrent', ((1, 'part'),)))
    IOpcPartEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcPartEnumerator
def _define_IOpcRelationshipEnumerator_head():
    class IOpcRelationshipEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('42195949-3b79-4fc8-89c6-fc7fb979ee76')
    return IOpcRelationshipEnumerator
def _define_IOpcRelationshipEnumerator():
    IOpcRelationshipEnumerator = win32more.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head
    IOpcRelationshipEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcRelationshipEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcRelationshipEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationship_head), use_last_error=False)(5, 'GetCurrent', ((1, 'relationship'),)))
    IOpcRelationshipEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcRelationshipEnumerator
def _define_IOpcSignaturePartReference_head():
    class IOpcSignaturePartReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('e24231ca-59f4-484e-b64b-36eeda36072c')
    return IOpcSignaturePartReference
def _define_IOpcSignaturePartReference():
    IOpcSignaturePartReference = win32more.Storage.Packaging.Opc.IOpcSignaturePartReference_head
    IOpcSignaturePartReference.GetPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(3, 'GetPartName', ((1, 'partName'),)))
    IOpcSignaturePartReference.GetContentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetContentType', ((1, 'contentType'),)))
    IOpcSignaturePartReference.GetDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetDigestMethod', ((1, 'digestMethod'),)))
    IOpcSignaturePartReference.GetDigestValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(6, 'GetDigestValue', ((1, 'digestValue'),(1, 'count'),)))
    IOpcSignaturePartReference.GetTransformMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD), use_last_error=False)(7, 'GetTransformMethod', ((1, 'transformMethod'),)))
    win32more.System.Com.IUnknown
    return IOpcSignaturePartReference
def _define_IOpcSignatureRelationshipReference_head():
    class IOpcSignatureRelationshipReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('57babac6-9d4a-4e50-8b86-e5d4051eae7c')
    return IOpcSignatureRelationshipReference
def _define_IOpcSignatureRelationshipReference():
    IOpcSignatureRelationshipReference = win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head
    IOpcSignatureRelationshipReference.GetSourceUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcUri_head), use_last_error=False)(3, 'GetSourceUri', ((1, 'sourceUri'),)))
    IOpcSignatureRelationshipReference.GetDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetDigestMethod', ((1, 'digestMethod'),)))
    IOpcSignatureRelationshipReference.GetDigestValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(5, 'GetDigestValue', ((1, 'digestValue'),(1, 'count'),)))
    IOpcSignatureRelationshipReference.GetTransformMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD), use_last_error=False)(6, 'GetTransformMethod', ((1, 'transformMethod'),)))
    IOpcSignatureRelationshipReference.GetRelationshipSigningOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION), use_last_error=False)(7, 'GetRelationshipSigningOption', ((1, 'relationshipSigningOption'),)))
    IOpcSignatureRelationshipReference.GetRelationshipSelectorEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head), use_last_error=False)(8, 'GetRelationshipSelectorEnumerator', ((1, 'selectorEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureRelationshipReference
def _define_IOpcRelationshipSelector_head():
    class IOpcRelationshipSelector(win32more.System.Com.IUnknown_head):
        Guid = Guid('f8f26c7f-b28f-4899-84c8-5d5639ede75f')
    return IOpcRelationshipSelector
def _define_IOpcRelationshipSelector():
    IOpcRelationshipSelector = win32more.Storage.Packaging.Opc.IOpcRelationshipSelector_head
    IOpcRelationshipSelector.GetSelectorType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR), use_last_error=False)(3, 'GetSelectorType', ((1, 'selector'),)))
    IOpcRelationshipSelector.GetSelectionCriterion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetSelectionCriterion', ((1, 'selectionCriterion'),)))
    win32more.System.Com.IUnknown
    return IOpcRelationshipSelector
def _define_IOpcSignatureReference_head():
    class IOpcSignatureReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('1b47005e-3011-4edc-be6f-0f65e5ab0342')
    return IOpcSignatureReference
def _define_IOpcSignatureReference():
    IOpcSignatureReference = win32more.Storage.Packaging.Opc.IOpcSignatureReference_head
    IOpcSignatureReference.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetId', ((1, 'referenceId'),)))
    IOpcSignatureReference.GetUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUri_head), use_last_error=False)(4, 'GetUri', ((1, 'referenceUri'),)))
    IOpcSignatureReference.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetType', ((1, 'type'),)))
    IOpcSignatureReference.GetTransformMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD), use_last_error=False)(6, 'GetTransformMethod', ((1, 'transformMethod'),)))
    IOpcSignatureReference.GetDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetDigestMethod', ((1, 'digestMethod'),)))
    IOpcSignatureReference.GetDigestValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(8, 'GetDigestValue', ((1, 'digestValue'),(1, 'count'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureReference
def _define_IOpcSignatureCustomObject_head():
    class IOpcSignatureCustomObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d77a19e-62c1-44e7-becd-45da5ae51a56')
    return IOpcSignatureCustomObject
def _define_IOpcSignatureCustomObject():
    IOpcSignatureCustomObject = win32more.Storage.Packaging.Opc.IOpcSignatureCustomObject_head
    IOpcSignatureCustomObject.GetXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(3, 'GetXml', ((1, 'xmlMarkup'),(1, 'count'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureCustomObject
def _define_IOpcDigitalSignature_head():
    class IOpcDigitalSignature(win32more.System.Com.IUnknown_head):
        Guid = Guid('52ab21dd-1cd0-4949-bc80-0c1232d00cb4')
    return IOpcDigitalSignature
def _define_IOpcDigitalSignature():
    IOpcDigitalSignature = win32more.Storage.Packaging.Opc.IOpcDigitalSignature_head
    IOpcDigitalSignature.GetNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32), use_last_error=False)(3, 'GetNamespaces', ((1, 'prefixes'),(1, 'namespaces'),(1, 'count'),)))
    IOpcDigitalSignature.GetSignatureId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetSignatureId', ((1, 'signatureId'),)))
    IOpcDigitalSignature.GetSignaturePartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(5, 'GetSignaturePartName', ((1, 'signaturePartName'),)))
    IOpcDigitalSignature.GetSignatureMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetSignatureMethod', ((1, 'signatureMethod'),)))
    IOpcDigitalSignature.GetCanonicalizationMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD), use_last_error=False)(7, 'GetCanonicalizationMethod', ((1, 'canonicalizationMethod'),)))
    IOpcDigitalSignature.GetSignatureValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(8, 'GetSignatureValue', ((1, 'signatureValue'),(1, 'count'),)))
    IOpcDigitalSignature.GetSignaturePartReferenceEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head), use_last_error=False)(9, 'GetSignaturePartReferenceEnumerator', ((1, 'partReferenceEnumerator'),)))
    IOpcDigitalSignature.GetSignatureRelationshipReferenceEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head), use_last_error=False)(10, 'GetSignatureRelationshipReferenceEnumerator', ((1, 'relationshipReferenceEnumerator'),)))
    IOpcDigitalSignature.GetSigningTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'GetSigningTime', ((1, 'signingTime'),)))
    IOpcDigitalSignature.GetTimeFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT), use_last_error=False)(12, 'GetTimeFormat', ((1, 'timeFormat'),)))
    IOpcDigitalSignature.GetPackageObjectReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReference_head), use_last_error=False)(13, 'GetPackageObjectReference', ((1, 'packageObjectReference'),)))
    IOpcDigitalSignature.GetCertificateEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateEnumerator_head), use_last_error=False)(14, 'GetCertificateEnumerator', ((1, 'certificateEnumerator'),)))
    IOpcDigitalSignature.GetCustomReferenceEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head), use_last_error=False)(15, 'GetCustomReferenceEnumerator', ((1, 'customReferenceEnumerator'),)))
    IOpcDigitalSignature.GetCustomObjectEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head), use_last_error=False)(16, 'GetCustomObjectEnumerator', ((1, 'customObjectEnumerator'),)))
    IOpcDigitalSignature.GetSignatureXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(17, 'GetSignatureXml', ((1, 'signatureXml'),(1, 'count'),)))
    win32more.System.Com.IUnknown
    return IOpcDigitalSignature
def _define_IOpcSigningOptions_head():
    class IOpcSigningOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('50d2d6a5-7aeb-46c0-b241-43ab0e9b407e')
    return IOpcSigningOptions
def _define_IOpcSigningOptions():
    IOpcSigningOptions = win32more.Storage.Packaging.Opc.IOpcSigningOptions_head
    IOpcSigningOptions.GetSignatureId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetSignatureId', ((1, 'signatureId'),)))
    IOpcSigningOptions.SetSignatureId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetSignatureId', ((1, 'signatureId'),)))
    IOpcSigningOptions.GetSignatureMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetSignatureMethod', ((1, 'signatureMethod'),)))
    IOpcSigningOptions.SetSignatureMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'SetSignatureMethod', ((1, 'signatureMethod'),)))
    IOpcSigningOptions.GetDefaultDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetDefaultDigestMethod', ((1, 'digestMethod'),)))
    IOpcSigningOptions.SetDefaultDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'SetDefaultDigestMethod', ((1, 'digestMethod'),)))
    IOpcSigningOptions.GetCertificateEmbeddingOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION), use_last_error=False)(9, 'GetCertificateEmbeddingOption', ((1, 'embeddingOption'),)))
    IOpcSigningOptions.SetCertificateEmbeddingOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.OPC_CERTIFICATE_EMBEDDING_OPTION, use_last_error=False)(10, 'SetCertificateEmbeddingOption', ((1, 'embeddingOption'),)))
    IOpcSigningOptions.GetTimeFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT), use_last_error=False)(11, 'GetTimeFormat', ((1, 'timeFormat'),)))
    IOpcSigningOptions.SetTimeFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT, use_last_error=False)(12, 'SetTimeFormat', ((1, 'timeFormat'),)))
    IOpcSigningOptions.GetSignaturePartReferenceSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignaturePartReferenceSet_head), use_last_error=False)(13, 'GetSignaturePartReferenceSet', ((1, 'partReferenceSet'),)))
    IOpcSigningOptions.GetSignatureRelationshipReferenceSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceSet_head), use_last_error=False)(14, 'GetSignatureRelationshipReferenceSet', ((1, 'relationshipReferenceSet'),)))
    IOpcSigningOptions.GetCustomObjectSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet_head), use_last_error=False)(15, 'GetCustomObjectSet', ((1, 'customObjectSet'),)))
    IOpcSigningOptions.GetCustomReferenceSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceSet_head), use_last_error=False)(16, 'GetCustomReferenceSet', ((1, 'customReferenceSet'),)))
    IOpcSigningOptions.GetCertificateSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateSet_head), use_last_error=False)(17, 'GetCertificateSet', ((1, 'certificateSet'),)))
    IOpcSigningOptions.GetSignaturePartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(18, 'GetSignaturePartName', ((1, 'signaturePartName'),)))
    IOpcSigningOptions.SetSignaturePartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head, use_last_error=False)(19, 'SetSignaturePartName', ((1, 'signaturePartName'),)))
    win32more.System.Com.IUnknown
    return IOpcSigningOptions
def _define_IOpcDigitalSignatureManager_head():
    class IOpcDigitalSignatureManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5e62a0b-696d-462f-94df-72e33cef2659')
    return IOpcDigitalSignatureManager
def _define_IOpcDigitalSignatureManager():
    IOpcDigitalSignatureManager = win32more.Storage.Packaging.Opc.IOpcDigitalSignatureManager_head
    IOpcDigitalSignatureManager.GetSignatureOriginPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(3, 'GetSignatureOriginPartName', ((1, 'signatureOriginPartName'),)))
    IOpcDigitalSignatureManager.SetSignatureOriginPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head, use_last_error=False)(4, 'SetSignatureOriginPartName', ((1, 'signatureOriginPartName'),)))
    IOpcDigitalSignatureManager.GetSignatureEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator_head), use_last_error=False)(5, 'GetSignatureEnumerator', ((1, 'signatureEnumerator'),)))
    IOpcDigitalSignatureManager.RemoveSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head, use_last_error=False)(6, 'RemoveSignature', ((1, 'signaturePartName'),)))
    IOpcDigitalSignatureManager.CreateSigningOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSigningOptions_head), use_last_error=False)(7, 'CreateSigningOptions', ((1, 'signingOptions'),)))
    IOpcDigitalSignatureManager.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcDigitalSignature_head,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_VALIDATION_RESULT), use_last_error=False)(8, 'Validate', ((1, 'signature'),(1, 'certificate'),(1, 'validationResult'),)))
    IOpcDigitalSignatureManager.Sign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),win32more.Storage.Packaging.Opc.IOpcSigningOptions_head,POINTER(win32more.Storage.Packaging.Opc.IOpcDigitalSignature_head), use_last_error=False)(9, 'Sign', ((1, 'certificate'),(1, 'signingOptions'),(1, 'digitalSignature'),)))
    IOpcDigitalSignatureManager.ReplaceSignatureXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,c_char_p_no,UInt32,POINTER(win32more.Storage.Packaging.Opc.IOpcDigitalSignature_head), use_last_error=False)(10, 'ReplaceSignatureXml', ((1, 'signaturePartName'),(1, 'newSignatureXml'),(1, 'count'),(1, 'digitalSignature'),)))
    win32more.System.Com.IUnknown
    return IOpcDigitalSignatureManager
def _define_IOpcSignaturePartReferenceEnumerator_head():
    class IOpcSignaturePartReferenceEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('80eb1561-8c77-49cf-8266-459b356ee99a')
    return IOpcSignaturePartReferenceEnumerator
def _define_IOpcSignaturePartReferenceEnumerator():
    IOpcSignaturePartReferenceEnumerator = win32more.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head
    IOpcSignaturePartReferenceEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcSignaturePartReferenceEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcSignaturePartReferenceEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignaturePartReference_head), use_last_error=False)(5, 'GetCurrent', ((1, 'partReference'),)))
    IOpcSignaturePartReferenceEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcSignaturePartReferenceEnumerator
def _define_IOpcSignatureRelationshipReferenceEnumerator_head():
    class IOpcSignatureRelationshipReferenceEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('773ba3e4-f021-48e4-aa04-9816db5d3495')
    return IOpcSignatureRelationshipReferenceEnumerator
def _define_IOpcSignatureRelationshipReferenceEnumerator():
    IOpcSignatureRelationshipReferenceEnumerator = win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head
    IOpcSignatureRelationshipReferenceEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcSignatureRelationshipReferenceEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcSignatureRelationshipReferenceEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head), use_last_error=False)(5, 'GetCurrent', ((1, 'relationshipReference'),)))
    IOpcSignatureRelationshipReferenceEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureRelationshipReferenceEnumerator
def _define_IOpcRelationshipSelectorEnumerator_head():
    class IOpcRelationshipSelectorEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e50a181-a91b-48ac-88d2-bca3d8f8c0b1')
    return IOpcRelationshipSelectorEnumerator
def _define_IOpcRelationshipSelectorEnumerator():
    IOpcRelationshipSelectorEnumerator = win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head
    IOpcRelationshipSelectorEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcRelationshipSelectorEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcRelationshipSelectorEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSelector_head), use_last_error=False)(5, 'GetCurrent', ((1, 'relationshipSelector'),)))
    IOpcRelationshipSelectorEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcRelationshipSelectorEnumerator
def _define_IOpcSignatureReferenceEnumerator_head():
    class IOpcSignatureReferenceEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('cfa59a45-28b1-4868-969e-fa8097fdc12a')
    return IOpcSignatureReferenceEnumerator
def _define_IOpcSignatureReferenceEnumerator():
    IOpcSignatureReferenceEnumerator = win32more.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head
    IOpcSignatureReferenceEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcSignatureReferenceEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcSignatureReferenceEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReference_head), use_last_error=False)(5, 'GetCurrent', ((1, 'reference'),)))
    IOpcSignatureReferenceEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureReferenceEnumerator
def _define_IOpcSignatureCustomObjectEnumerator_head():
    class IOpcSignatureCustomObjectEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ee4fe1d-e1b0-4683-8079-7ea0fcf80b4c')
    return IOpcSignatureCustomObjectEnumerator
def _define_IOpcSignatureCustomObjectEnumerator():
    IOpcSignatureCustomObjectEnumerator = win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head
    IOpcSignatureCustomObjectEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcSignatureCustomObjectEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcSignatureCustomObjectEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObject_head), use_last_error=False)(5, 'GetCurrent', ((1, 'customObject'),)))
    IOpcSignatureCustomObjectEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureCustomObjectEnumerator
def _define_IOpcCertificateEnumerator_head():
    class IOpcCertificateEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('85131937-8f24-421f-b439-59ab24d140b8')
    return IOpcCertificateEnumerator
def _define_IOpcCertificateEnumerator():
    IOpcCertificateEnumerator = win32more.Storage.Packaging.Opc.IOpcCertificateEnumerator_head
    IOpcCertificateEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcCertificateEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcCertificateEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)), use_last_error=False)(5, 'GetCurrent', ((1, 'certificate'),)))
    IOpcCertificateEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcCertificateEnumerator
def _define_IOpcDigitalSignatureEnumerator_head():
    class IOpcDigitalSignatureEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('967b6882-0ba3-4358-b9e7-b64c75063c5e')
    return IOpcDigitalSignatureEnumerator
def _define_IOpcDigitalSignatureEnumerator():
    IOpcDigitalSignatureEnumerator = win32more.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator_head
    IOpcDigitalSignatureEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasNext'),)))
    IOpcDigitalSignatureEnumerator.MovePrevious = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'MovePrevious', ((1, 'hasPrevious'),)))
    IOpcDigitalSignatureEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcDigitalSignature_head), use_last_error=False)(5, 'GetCurrent', ((1, 'digitalSignature'),)))
    IOpcDigitalSignatureEnumerator.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcDigitalSignatureEnumerator_head), use_last_error=False)(6, 'Clone', ((1, 'copy'),)))
    win32more.System.Com.IUnknown
    return IOpcDigitalSignatureEnumerator
def _define_IOpcSignaturePartReferenceSet_head():
    class IOpcSignaturePartReferenceSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('6c9fe28c-ecd9-4b22-9d36-7fdde670fec0')
    return IOpcSignaturePartReferenceSet
def _define_IOpcSignaturePartReferenceSet():
    IOpcSignaturePartReferenceSet = win32more.Storage.Packaging.Opc.IOpcSignaturePartReferenceSet_head
    IOpcSignaturePartReferenceSet.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD,POINTER(win32more.Storage.Packaging.Opc.IOpcSignaturePartReference_head), use_last_error=False)(3, 'Create', ((1, 'partUri'),(1, 'digestMethod'),(1, 'transformMethod'),(1, 'partReference'),)))
    IOpcSignaturePartReferenceSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcSignaturePartReference_head, use_last_error=False)(4, 'Delete', ((1, 'partReference'),)))
    IOpcSignaturePartReferenceSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignaturePartReferenceEnumerator_head), use_last_error=False)(5, 'GetEnumerator', ((1, 'partReferenceEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcSignaturePartReferenceSet
def _define_IOpcSignatureRelationshipReferenceSet_head():
    class IOpcSignatureRelationshipReferenceSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f863ca5-3631-404c-828d-807e0715069b')
    return IOpcSignatureRelationshipReferenceSet
def _define_IOpcSignatureRelationshipReferenceSet():
    IOpcSignatureRelationshipReferenceSet = win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceSet_head
    IOpcSignatureRelationshipReferenceSet.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcUri_head,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.OPC_RELATIONSHIPS_SIGNING_OPTION,win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorSet_head,win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head), use_last_error=False)(3, 'Create', ((1, 'sourceUri'),(1, 'digestMethod'),(1, 'relationshipSigningOption'),(1, 'selectorSet'),(1, 'transformMethod'),(1, 'relationshipReference'),)))
    IOpcSignatureRelationshipReferenceSet.CreateRelationshipSelectorSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorSet_head), use_last_error=False)(4, 'CreateRelationshipSelectorSet', ((1, 'selectorSet'),)))
    IOpcSignatureRelationshipReferenceSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReference_head, use_last_error=False)(5, 'Delete', ((1, 'relationshipReference'),)))
    IOpcSignatureRelationshipReferenceSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureRelationshipReferenceEnumerator_head), use_last_error=False)(6, 'GetEnumerator', ((1, 'relationshipReferenceEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureRelationshipReferenceSet
def _define_IOpcRelationshipSelectorSet_head():
    class IOpcRelationshipSelectorSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e34c269-a4d3-47c0-b5c4-87ff2b3b6136')
    return IOpcRelationshipSelectorSet
def _define_IOpcRelationshipSelectorSet():
    IOpcRelationshipSelectorSet = win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorSet_head
    IOpcRelationshipSelectorSet.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.OPC_RELATIONSHIP_SELECTOR,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSelector_head), use_last_error=False)(3, 'Create', ((1, 'selector'),(1, 'selectionCriterion'),(1, 'relationshipSelector'),)))
    IOpcRelationshipSelectorSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcRelationshipSelector_head, use_last_error=False)(4, 'Delete', ((1, 'relationshipSelector'),)))
    IOpcRelationshipSelectorSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcRelationshipSelectorEnumerator_head), use_last_error=False)(5, 'GetEnumerator', ((1, 'relationshipSelectorEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcRelationshipSelectorSet
def _define_IOpcSignatureReferenceSet_head():
    class IOpcSignatureReferenceSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('f3b02d31-ab12-42dd-9e2f-2b16761c3c1e')
    return IOpcSignatureReferenceSet
def _define_IOpcSignatureReferenceSet():
    IOpcSignatureReferenceSet = win32more.Storage.Packaging.Opc.IOpcSignatureReferenceSet_head
    IOpcSignatureReferenceSet.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.OPC_CANONICALIZATION_METHOD,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReference_head), use_last_error=False)(3, 'Create', ((1, 'referenceUri'),(1, 'referenceId'),(1, 'type'),(1, 'digestMethod'),(1, 'transformMethod'),(1, 'reference'),)))
    IOpcSignatureReferenceSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcSignatureReference_head, use_last_error=False)(4, 'Delete', ((1, 'reference'),)))
    IOpcSignatureReferenceSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head), use_last_error=False)(5, 'GetEnumerator', ((1, 'referenceEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureReferenceSet
def _define_IOpcSignatureCustomObjectSet_head():
    class IOpcSignatureCustomObjectSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('8f792ac5-7947-4e11-bc3d-2659ff046ae1')
    return IOpcSignatureCustomObjectSet
def _define_IOpcSignatureCustomObjectSet():
    IOpcSignatureCustomObjectSet = win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet_head
    IOpcSignatureCustomObjectSet.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObject_head), use_last_error=False)(3, 'Create', ((1, 'xmlMarkup'),(1, 'count'),(1, 'customObject'),)))
    IOpcSignatureCustomObjectSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcSignatureCustomObject_head, use_last_error=False)(4, 'Delete', ((1, 'customObject'),)))
    IOpcSignatureCustomObjectSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head), use_last_error=False)(5, 'GetEnumerator', ((1, 'customObjectEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcSignatureCustomObjectSet
def _define_IOpcCertificateSet_head():
    class IOpcCertificateSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('56ea4325-8e2d-4167-b1a4-e486d24c8fa7')
    return IOpcCertificateSet
def _define_IOpcCertificateSet():
    IOpcCertificateSet = win32more.Storage.Packaging.Opc.IOpcCertificateSet_head
    IOpcCertificateSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(3, 'Add', ((1, 'certificate'),)))
    IOpcCertificateSet.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), use_last_error=False)(4, 'Remove', ((1, 'certificate'),)))
    IOpcCertificateSet.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateEnumerator_head), use_last_error=False)(5, 'GetEnumerator', ((1, 'certificateEnumerator'),)))
    win32more.System.Com.IUnknown
    return IOpcCertificateSet
def _define_IOpcFactory_head():
    class IOpcFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d0b4446-cd73-4ab3-94f4-8ccdf6116154')
    return IOpcFactory
def _define_IOpcFactory():
    IOpcFactory = win32more.Storage.Packaging.Opc.IOpcFactory_head
    IOpcFactory.CreatePackageRootUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcUri_head), use_last_error=False)(3, 'CreatePackageRootUri', ((1, 'rootUri'),)))
    IOpcFactory.CreatePartUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), use_last_error=False)(4, 'CreatePartUri', ((1, 'pwzUri'),(1, 'partUri'),)))
    IOpcFactory.CreateStreamOnFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.OPC_STREAM_IO_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(5, 'CreateStreamOnFile', ((1, 'filename'),(1, 'ioMode'),(1, 'securityAttributes'),(1, 'dwFlagsAndAttributes'),(1, 'stream'),)))
    IOpcFactory.CreatePackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPackage_head), use_last_error=False)(6, 'CreatePackage', ((1, 'package'),)))
    IOpcFactory.ReadPackageFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.OPC_READ_FLAGS,POINTER(win32more.Storage.Packaging.Opc.IOpcPackage_head), use_last_error=False)(7, 'ReadPackageFromStream', ((1, 'stream'),(1, 'flags'),(1, 'package'),)))
    IOpcFactory.WritePackageToStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPackage_head,win32more.Storage.Packaging.Opc.OPC_WRITE_FLAGS,win32more.System.Com.IStream_head, use_last_error=False)(8, 'WritePackageToStream', ((1, 'package'),(1, 'flags'),(1, 'stream'),)))
    IOpcFactory.CreateDigitalSignatureManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPackage_head,POINTER(win32more.Storage.Packaging.Opc.IOpcDigitalSignatureManager_head), use_last_error=False)(9, 'CreateDigitalSignatureManager', ((1, 'package'),(1, 'signatureManager'),)))
    win32more.System.Com.IUnknown
    return IOpcFactory
__all__ = [
    "OPC_E_NONCONFORMING_URI",
    "OPC_E_RELATIVE_URI_REQUIRED",
    "OPC_E_RELATIONSHIP_URI_REQUIRED",
    "OPC_E_PART_CANNOT_BE_DIRECTORY",
    "OPC_E_UNEXPECTED_CONTENT_TYPE",
    "OPC_E_INVALID_CONTENT_TYPE_XML",
    "OPC_E_MISSING_CONTENT_TYPES",
    "OPC_E_NONCONFORMING_CONTENT_TYPES_XML",
    "OPC_E_NONCONFORMING_RELS_XML",
    "OPC_E_INVALID_RELS_XML",
    "OPC_E_DUPLICATE_PART",
    "OPC_E_INVALID_OVERRIDE_PART_NAME",
    "OPC_E_DUPLICATE_OVERRIDE_PART",
    "OPC_E_INVALID_DEFAULT_EXTENSION",
    "OPC_E_DUPLICATE_DEFAULT_EXTENSION",
    "OPC_E_INVALID_RELATIONSHIP_ID",
    "OPC_E_INVALID_RELATIONSHIP_TYPE",
    "OPC_E_INVALID_RELATIONSHIP_TARGET",
    "OPC_E_DUPLICATE_RELATIONSHIP",
    "OPC_E_CONFLICTING_SETTINGS",
    "OPC_E_DUPLICATE_PIECE",
    "OPC_E_INVALID_PIECE",
    "OPC_E_MISSING_PIECE",
    "OPC_E_NO_SUCH_PART",
    "OPC_E_DS_SIGNATURE_CORRUPT",
    "OPC_E_DS_DIGEST_VALUE_ERROR",
    "OPC_E_DS_DUPLICATE_SIGNATURE_ORIGIN_RELATIONSHIP",
    "OPC_E_DS_INVALID_SIGNATURE_ORIGIN_RELATIONSHIP",
    "OPC_E_DS_INVALID_CERTIFICATE_RELATIONSHIP",
    "OPC_E_DS_EXTERNAL_SIGNATURE",
    "OPC_E_DS_MISSING_SIGNATURE_ORIGIN_PART",
    "OPC_E_DS_MISSING_SIGNATURE_PART",
    "OPC_E_DS_INVALID_RELATIONSHIP_TRANSFORM_XML",
    "OPC_E_DS_INVALID_CANONICALIZATION_METHOD",
    "OPC_E_DS_INVALID_RELATIONSHIPS_SIGNING_OPTION",
    "OPC_E_DS_INVALID_OPC_SIGNATURE_TIME_FORMAT",
    "OPC_E_DS_PACKAGE_REFERENCE_URI_RESERVED",
    "OPC_E_DS_MISSING_SIGNATURE_PROPERTIES_ELEMENT",
    "OPC_E_DS_MISSING_SIGNATURE_PROPERTY_ELEMENT",
    "OPC_E_DS_DUPLICATE_SIGNATURE_PROPERTY_ELEMENT",
    "OPC_E_DS_MISSING_SIGNATURE_TIME_PROPERTY",
    "OPC_E_DS_INVALID_SIGNATURE_XML",
    "OPC_E_DS_INVALID_SIGNATURE_COUNT",
    "OPC_E_DS_MISSING_SIGNATURE_ALGORITHM",
    "OPC_E_DS_DUPLICATE_PACKAGE_OBJECT_REFERENCES",
    "OPC_E_DS_MISSING_PACKAGE_OBJECT_REFERENCE",
    "OPC_E_DS_EXTERNAL_SIGNATURE_REFERENCE",
    "OPC_E_DS_REFERENCE_MISSING_CONTENT_TYPE",
    "OPC_E_DS_MULTIPLE_RELATIONSHIP_TRANSFORMS",
    "OPC_E_DS_MISSING_CANONICALIZATION_TRANSFORM",
    "OPC_E_MC_UNEXPECTED_ELEMENT",
    "OPC_E_MC_UNEXPECTED_REQUIRES_ATTR",
    "OPC_E_MC_MISSING_REQUIRES_ATTR",
    "OPC_E_MC_UNEXPECTED_ATTR",
    "OPC_E_MC_INVALID_PREFIX_LIST",
    "OPC_E_MC_INVALID_QNAME_LIST",
    "OPC_E_MC_NESTED_ALTERNATE_CONTENT",
    "OPC_E_MC_UNEXPECTED_CHOICE",
    "OPC_E_MC_MISSING_CHOICE",
    "OPC_E_MC_INVALID_ENUM_TYPE",
    "OPC_E_MC_UNKNOWN_NAMESPACE",
    "OPC_E_MC_UNKNOWN_PREFIX",
    "OPC_E_MC_INVALID_ATTRIBUTES_ON_IGNORABLE_ELEMENT",
    "OPC_E_MC_INVALID_XMLNS_ATTRIBUTE",
    "OPC_E_INVALID_XML_ENCODING",
    "OPC_E_DS_SIGNATURE_REFERENCE_MISSING_URI",
    "OPC_E_INVALID_CONTENT_TYPE",
    "OPC_E_DS_SIGNATURE_PROPERTY_MISSING_TARGET",
    "OPC_E_DS_SIGNATURE_METHOD_NOT_SET",
    "OPC_E_DS_DEFAULT_DIGEST_METHOD_NOT_SET",
    "OPC_E_NO_SUCH_RELATIONSHIP",
    "OPC_E_MC_MULTIPLE_FALLBACK_ELEMENTS",
    "OPC_E_MC_INCONSISTENT_PROCESS_CONTENT",
    "OPC_E_MC_INCONSISTENT_PRESERVE_ATTRIBUTES",
    "OPC_E_MC_INCONSISTENT_PRESERVE_ELEMENTS",
    "OPC_E_INVALID_RELATIONSHIP_TARGET_MODE",
    "OPC_E_COULD_NOT_RECOVER",
    "OPC_E_UNSUPPORTED_PACKAGE",
    "OPC_E_ENUM_COLLECTION_CHANGED",
    "OPC_E_ENUM_CANNOT_MOVE_NEXT",
    "OPC_E_ENUM_CANNOT_MOVE_PREVIOUS",
    "OPC_E_ENUM_INVALID_POSITION",
    "OPC_E_DS_SIGNATURE_ORIGIN_EXISTS",
    "OPC_E_DS_UNSIGNED_PACKAGE",
    "OPC_E_DS_MISSING_CERTIFICATE_PART",
    "OPC_E_NO_SUCH_SETTINGS",
    "OPC_E_ZIP_INCORRECT_DATA_SIZE",
    "OPC_E_ZIP_CORRUPTED_ARCHIVE",
    "OPC_E_ZIP_COMPRESSION_FAILED",
    "OPC_E_ZIP_DECOMPRESSION_FAILED",
    "OPC_E_ZIP_INCONSISTENT_FILEITEM",
    "OPC_E_ZIP_INCONSISTENT_DIRECTORY",
    "OPC_E_ZIP_MISSING_DATA_DESCRIPTOR",
    "OPC_E_ZIP_UNSUPPORTEDARCHIVE",
    "OPC_E_ZIP_CENTRAL_DIRECTORY_TOO_LARGE",
    "OPC_E_ZIP_NAME_TOO_LARGE",
    "OPC_E_ZIP_DUPLICATE_NAME",
    "OPC_E_ZIP_COMMENT_TOO_LARGE",
    "OPC_E_ZIP_EXTRA_FIELDS_TOO_LARGE",
    "OPC_E_ZIP_FILE_HEADER_TOO_LARGE",
    "OPC_E_ZIP_MISSING_END_OF_CENTRAL_DIRECTORY",
    "OPC_E_ZIP_REQUIRES_64_BIT",
    "OpcFactory",
    "IOpcUri",
    "IOpcPartUri",
    "OPC_URI_TARGET_MODE",
    "OPC_URI_TARGET_MODE_INTERNAL",
    "OPC_URI_TARGET_MODE_EXTERNAL",
    "OPC_COMPRESSION_OPTIONS",
    "OPC_COMPRESSION_NONE",
    "OPC_COMPRESSION_NORMAL",
    "OPC_COMPRESSION_MAXIMUM",
    "OPC_COMPRESSION_FAST",
    "OPC_COMPRESSION_SUPERFAST",
    "OPC_STREAM_IO_MODE",
    "OPC_STREAM_IO_READ",
    "OPC_STREAM_IO_WRITE",
    "OPC_READ_FLAGS",
    "OPC_READ_DEFAULT",
    "OPC_VALIDATE_ON_LOAD",
    "OPC_CACHE_ON_ACCESS",
    "OPC_WRITE_FLAGS",
    "OPC_WRITE_DEFAULT",
    "OPC_WRITE_FORCE_ZIP32",
    "OPC_SIGNATURE_VALIDATION_RESULT",
    "OPC_SIGNATURE_VALID",
    "OPC_SIGNATURE_INVALID",
    "OPC_CANONICALIZATION_METHOD",
    "OPC_CANONICALIZATION_NONE",
    "OPC_CANONICALIZATION_C14N",
    "OPC_CANONICALIZATION_C14N_WITH_COMMENTS",
    "OPC_RELATIONSHIP_SELECTOR",
    "OPC_RELATIONSHIP_SELECT_BY_ID",
    "OPC_RELATIONSHIP_SELECT_BY_TYPE",
    "OPC_RELATIONSHIPS_SIGNING_OPTION",
    "OPC_RELATIONSHIP_SIGN_USING_SELECTORS",
    "OPC_RELATIONSHIP_SIGN_PART",
    "OPC_CERTIFICATE_EMBEDDING_OPTION",
    "OPC_CERTIFICATE_IN_CERTIFICATE_PART",
    "OPC_CERTIFICATE_IN_SIGNATURE_PART",
    "OPC_CERTIFICATE_NOT_EMBEDDED",
    "OPC_SIGNATURE_TIME_FORMAT",
    "OPC_SIGNATURE_TIME_FORMAT_MILLISECONDS",
    "OPC_SIGNATURE_TIME_FORMAT_SECONDS",
    "OPC_SIGNATURE_TIME_FORMAT_MINUTES",
    "OPC_SIGNATURE_TIME_FORMAT_DAYS",
    "OPC_SIGNATURE_TIME_FORMAT_MONTHS",
    "OPC_SIGNATURE_TIME_FORMAT_YEARS",
    "IOpcPackage",
    "IOpcPart",
    "IOpcRelationship",
    "IOpcPartSet",
    "IOpcRelationshipSet",
    "IOpcPartEnumerator",
    "IOpcRelationshipEnumerator",
    "IOpcSignaturePartReference",
    "IOpcSignatureRelationshipReference",
    "IOpcRelationshipSelector",
    "IOpcSignatureReference",
    "IOpcSignatureCustomObject",
    "IOpcDigitalSignature",
    "IOpcSigningOptions",
    "IOpcDigitalSignatureManager",
    "IOpcSignaturePartReferenceEnumerator",
    "IOpcSignatureRelationshipReferenceEnumerator",
    "IOpcRelationshipSelectorEnumerator",
    "IOpcSignatureReferenceEnumerator",
    "IOpcSignatureCustomObjectEnumerator",
    "IOpcCertificateEnumerator",
    "IOpcDigitalSignatureEnumerator",
    "IOpcSignaturePartReferenceSet",
    "IOpcSignatureRelationshipReferenceSet",
    "IOpcRelationshipSelectorSet",
    "IOpcSignatureReferenceSet",
    "IOpcSignatureCustomObjectSet",
    "IOpcCertificateSet",
    "IOpcFactory",
]
