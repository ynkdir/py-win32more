from win32more import *
import win32more.Storage.Packaging.Appx
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Storage.Packaging.Appx, name, eval(f"_define_{name}()"))
    return getattr(win32more.Storage.Packaging.Appx, name)
PACKAGE_PROPERTY_FRAMEWORK = 1
PACKAGE_PROPERTY_RESOURCE = 2
PACKAGE_PROPERTY_BUNDLE = 4
PACKAGE_PROPERTY_OPTIONAL = 8
PACKAGE_FILTER_HEAD = 16
PACKAGE_FILTER_DIRECT = 32
PACKAGE_FILTER_RESOURCE = 64
PACKAGE_FILTER_BUNDLE = 128
PACKAGE_INFORMATION_BASIC = 0
PACKAGE_INFORMATION_FULL = 256
PACKAGE_PROPERTY_DEVELOPMENT_MODE = 65536
PACKAGE_FILTER_OPTIONAL = 131072
PACKAGE_PROPERTY_IS_IN_RELATED_SET = 262144
PACKAGE_FILTER_IS_IN_RELATED_SET = 262144
PACKAGE_PROPERTY_STATIC = 524288
PACKAGE_FILTER_STATIC = 524288
PACKAGE_PROPERTY_DYNAMIC = 1048576
PACKAGE_FILTER_DYNAMIC = 1048576
PACKAGE_PROPERTY_HOSTRUNTIME = 2097152
PACKAGE_FILTER_HOSTRUNTIME = 2097152
PACKAGE_FILTER_ALL_LOADED = 0
PACKAGE_DEPENDENCY_RANK_DEFAULT = 0
AppxFactory = Guid('5842a140-ff9f-4166-8f5c-62f5b7b0c781')
AppxBundleFactory = Guid('378e0446-5384-43b7-8877-e7dbdd883446')
AppxPackagingDiagnosticEventSinkManager = Guid('50ca0a46-1588-4161-8ed2-ef9e469ced5d')
AppxEncryptionFactory = Guid('dc664fdd-d868-46ee-8780-8d196cb739f7')
AppxPackageEditor = Guid('f004f2ca-aebc-4b0d-bf58-e516d5bcc0ab')
def _define_APPX_PACKAGE_SETTINGS_head():
    class APPX_PACKAGE_SETTINGS(Structure):
        pass
    return APPX_PACKAGE_SETTINGS
def _define_APPX_PACKAGE_SETTINGS():
    APPX_PACKAGE_SETTINGS = win32more.Storage.Packaging.Appx.APPX_PACKAGE_SETTINGS_head
    APPX_PACKAGE_SETTINGS._fields_ = [
        ("forceZip32", win32more.Foundation.BOOL),
        ("hashMethod", win32more.System.Com.IUri_head),
    ]
    return APPX_PACKAGE_SETTINGS
APPX_COMPRESSION_OPTION = Int32
APPX_COMPRESSION_OPTION_NONE = 0
APPX_COMPRESSION_OPTION_NORMAL = 1
APPX_COMPRESSION_OPTION_MAXIMUM = 2
APPX_COMPRESSION_OPTION_FAST = 3
APPX_COMPRESSION_OPTION_SUPERFAST = 4
def _define_APPX_PACKAGE_WRITER_PAYLOAD_STREAM_head():
    class APPX_PACKAGE_WRITER_PAYLOAD_STREAM(Structure):
        pass
    return APPX_PACKAGE_WRITER_PAYLOAD_STREAM
def _define_APPX_PACKAGE_WRITER_PAYLOAD_STREAM():
    APPX_PACKAGE_WRITER_PAYLOAD_STREAM = win32more.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM_head
    APPX_PACKAGE_WRITER_PAYLOAD_STREAM._fields_ = [
        ("inputStream", win32more.System.Com.IStream_head),
        ("fileName", win32more.Foundation.PWSTR),
        ("contentType", win32more.Foundation.PWSTR),
        ("compressionOption", win32more.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION),
    ]
    return APPX_PACKAGE_WRITER_PAYLOAD_STREAM
APPX_FOOTPRINT_FILE_TYPE = Int32
APPX_FOOTPRINT_FILE_TYPE_MANIFEST = 0
APPX_FOOTPRINT_FILE_TYPE_BLOCKMAP = 1
APPX_FOOTPRINT_FILE_TYPE_SIGNATURE = 2
APPX_FOOTPRINT_FILE_TYPE_CODEINTEGRITY = 3
APPX_FOOTPRINT_FILE_TYPE_CONTENTGROUPMAP = 4
APPX_BUNDLE_FOOTPRINT_FILE_TYPE = Int32
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_FIRST = 0
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_MANIFEST = 0
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_BLOCKMAP = 1
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_SIGNATURE = 2
APPX_BUNDLE_FOOTPRINT_FILE_TYPE_LAST = 2
APPX_CAPABILITIES = UInt32
APPX_CAPABILITY_INTERNET_CLIENT = 1
APPX_CAPABILITY_INTERNET_CLIENT_SERVER = 2
APPX_CAPABILITY_PRIVATE_NETWORK_CLIENT_SERVER = 4
APPX_CAPABILITY_DOCUMENTS_LIBRARY = 8
APPX_CAPABILITY_PICTURES_LIBRARY = 16
APPX_CAPABILITY_VIDEOS_LIBRARY = 32
APPX_CAPABILITY_MUSIC_LIBRARY = 64
APPX_CAPABILITY_ENTERPRISE_AUTHENTICATION = 128
APPX_CAPABILITY_SHARED_USER_CERTIFICATES = 256
APPX_CAPABILITY_REMOVABLE_STORAGE = 512
APPX_CAPABILITY_APPOINTMENTS = 1024
APPX_CAPABILITY_CONTACTS = 2048
APPX_PACKAGE_ARCHITECTURE = Int32
APPX_PACKAGE_ARCHITECTURE_X86 = 0
APPX_PACKAGE_ARCHITECTURE_ARM = 5
APPX_PACKAGE_ARCHITECTURE_X64 = 9
APPX_PACKAGE_ARCHITECTURE_NEUTRAL = 11
APPX_PACKAGE_ARCHITECTURE_ARM64 = 12
APPX_PACKAGE_ARCHITECTURE2 = Int32
APPX_PACKAGE_ARCHITECTURE2_X86 = 0
APPX_PACKAGE_ARCHITECTURE2_ARM = 5
APPX_PACKAGE_ARCHITECTURE2_X64 = 9
APPX_PACKAGE_ARCHITECTURE2_NEUTRAL = 11
APPX_PACKAGE_ARCHITECTURE2_ARM64 = 12
APPX_PACKAGE_ARCHITECTURE2_X86_ON_ARM64 = 14
APPX_PACKAGE_ARCHITECTURE2_UNKNOWN = 65535
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE = Int32
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_APPLICATION = 0
APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_RESOURCE = 1
DX_FEATURE_LEVEL = Int32
DX_FEATURE_LEVEL_UNSPECIFIED = 0
DX_FEATURE_LEVEL_9 = 1
DX_FEATURE_LEVEL_10 = 2
DX_FEATURE_LEVEL_11 = 3
APPX_CAPABILITY_CLASS_TYPE = Int32
APPX_CAPABILITY_CLASS_DEFAULT = 0
APPX_CAPABILITY_CLASS_GENERAL = 1
APPX_CAPABILITY_CLASS_RESTRICTED = 2
APPX_CAPABILITY_CLASS_WINDOWS = 4
APPX_CAPABILITY_CLASS_ALL = 7
APPX_CAPABILITY_CLASS_CUSTOM = 8
APPX_PACKAGING_CONTEXT_CHANGE_TYPE = Int32
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_START = 0
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_CHANGE = 1
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_DETAILS = 2
APPX_PACKAGING_CONTEXT_CHANGE_TYPE_END = 3
def _define_IAppxFactory_head():
    class IAppxFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('beb94909-e451-438b-b5a7-d79e767b75d8')
    return IAppxFactory
def _define_IAppxFactory():
    IAppxFactory = win32more.Storage.Packaging.Appx.IAppxFactory_head
    IAppxFactory.CreatePackageWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_PACKAGE_SETTINGS_head),POINTER(win32more.Storage.Packaging.Appx.IAppxPackageWriter_head), use_last_error=False)(3, 'CreatePackageWriter', ((1, 'outputStream'),(1, 'settings'),(1, 'packageWriter'),)))
    IAppxFactory.CreatePackageReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxPackageReader_head), use_last_error=False)(4, 'CreatePackageReader', ((1, 'inputStream'),(1, 'packageReader'),)))
    IAppxFactory.CreateManifestReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestReader_head), use_last_error=False)(5, 'CreateManifestReader', ((1, 'inputStream'),(1, 'manifestReader'),)))
    IAppxFactory.CreateBlockMapReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapReader_head), use_last_error=False)(6, 'CreateBlockMapReader', ((1, 'inputStream'),(1, 'blockMapReader'),)))
    IAppxFactory.CreateValidatedBlockMapReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapReader_head), use_last_error=False)(7, 'CreateValidatedBlockMapReader', ((1, 'blockMapStream'),(1, 'signatureFileName'),(1, 'blockMapReader'),)))
    return IAppxFactory
def _define_IAppxFactory2_head():
    class IAppxFactory2(win32more.System.Com.IUnknown_head):
        Guid = Guid('f1346df2-c282-4e22-b918-743a929a8d55')
    return IAppxFactory2
def _define_IAppxFactory2():
    IAppxFactory2 = win32more.Storage.Packaging.Appx.IAppxFactory2_head
    IAppxFactory2.CreateContentGroupMapReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroupMapReader_head), use_last_error=False)(3, 'CreateContentGroupMapReader', ((1, 'inputStream'),(1, 'contentGroupMapReader'),)))
    IAppxFactory2.CreateSourceContentGroupMapReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxSourceContentGroupMapReader_head), use_last_error=False)(4, 'CreateSourceContentGroupMapReader', ((1, 'inputStream'),(1, 'reader'),)))
    IAppxFactory2.CreateContentGroupMapWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroupMapWriter_head), use_last_error=False)(5, 'CreateContentGroupMapWriter', ((1, 'stream'),(1, 'contentGroupMapWriter'),)))
    return IAppxFactory2
def _define_IAppxPackageReader_head():
    class IAppxPackageReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('b5c49650-99bc-481c-9a34-3d53a4106708')
    return IAppxPackageReader
def _define_IAppxPackageReader():
    IAppxPackageReader = win32more.Storage.Packaging.Appx.IAppxPackageReader_head
    IAppxPackageReader.GetBlockMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapReader_head), use_last_error=False)(3, 'GetBlockMap', ((1, 'blockMapReader'),)))
    IAppxPackageReader.GetFootprintFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Appx.APPX_FOOTPRINT_FILE_TYPE,POINTER(win32more.Storage.Packaging.Appx.IAppxFile_head), use_last_error=False)(4, 'GetFootprintFile', ((1, 'type'),(1, 'file'),)))
    IAppxPackageReader.GetPayloadFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Appx.IAppxFile_head), use_last_error=False)(5, 'GetPayloadFile', ((1, 'fileName'),(1, 'file'),)))
    IAppxPackageReader.GetPayloadFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxFilesEnumerator_head), use_last_error=False)(6, 'GetPayloadFiles', ((1, 'filesEnumerator'),)))
    IAppxPackageReader.GetManifest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestReader_head), use_last_error=False)(7, 'GetManifest', ((1, 'manifestReader'),)))
    return IAppxPackageReader
def _define_IAppxPackageWriter_head():
    class IAppxPackageWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('9099e33b-246f-41e4-881a-008eb613f858')
    return IAppxPackageWriter
def _define_IAppxPackageWriter():
    IAppxPackageWriter = win32more.Storage.Packaging.Appx.IAppxPackageWriter_head
    IAppxPackageWriter.AddPayloadFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddPayloadFile', ((1, 'fileName'),(1, 'contentType'),(1, 'compressionOption'),(1, 'inputStream'),)))
    IAppxPackageWriter.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(4, 'Close', ((1, 'manifest'),)))
    return IAppxPackageWriter
def _define_IAppxPackageWriter2_head():
    class IAppxPackageWriter2(win32more.System.Com.IUnknown_head):
        Guid = Guid('2cf5c4fd-e54c-4ea5-ba4e-f8c4b105a8c8')
    return IAppxPackageWriter2
def _define_IAppxPackageWriter2():
    IAppxPackageWriter2 = win32more.Storage.Packaging.Appx.IAppxPackageWriter2_head
    IAppxPackageWriter2.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head, use_last_error=False)(3, 'Close', ((1, 'manifest'),(1, 'contentGroupMap'),)))
    return IAppxPackageWriter2
def _define_IAppxPackageWriter3_head():
    class IAppxPackageWriter3(win32more.System.Com.IUnknown_head):
        Guid = Guid('a83aacd3-41c0-4501-b8a3-74164f50b2fd')
    return IAppxPackageWriter3
def _define_IAppxPackageWriter3():
    IAppxPackageWriter3 = win32more.Storage.Packaging.Appx.IAppxPackageWriter3_head
    IAppxPackageWriter3.AddPayloadFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM),UInt64, use_last_error=False)(3, 'AddPayloadFiles', ((1, 'fileCount'),(1, 'payloadFiles'),(1, 'memoryLimit'),)))
    return IAppxPackageWriter3
def _define_IAppxFile_head():
    class IAppxFile(win32more.System.Com.IUnknown_head):
        Guid = Guid('91df827b-94fd-468f-827b-57f41b2f6f2e')
    return IAppxFile
def _define_IAppxFile():
    IAppxFile = win32more.Storage.Packaging.Appx.IAppxFile_head
    IAppxFile.GetCompressionOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION), use_last_error=False)(3, 'GetCompressionOption', ((1, 'compressionOption'),)))
    IAppxFile.GetContentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetContentType', ((1, 'contentType'),)))
    IAppxFile.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetName', ((1, 'fileName'),)))
    IAppxFile.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(6, 'GetSize', ((1, 'size'),)))
    IAppxFile.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(7, 'GetStream', ((1, 'stream'),)))
    return IAppxFile
def _define_IAppxFilesEnumerator_head():
    class IAppxFilesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('f007eeaf-9831-411c-9847-917cdc62d1fe')
    return IAppxFilesEnumerator
def _define_IAppxFilesEnumerator():
    IAppxFilesEnumerator = win32more.Storage.Packaging.Appx.IAppxFilesEnumerator_head
    IAppxFilesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxFile_head), use_last_error=False)(3, 'GetCurrent', ((1, 'file'),)))
    IAppxFilesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxFilesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxFilesEnumerator
def _define_IAppxBlockMapReader_head():
    class IAppxBlockMapReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('5efec991-bca3-42d1-9ec2-e92d609ec22a')
    return IAppxBlockMapReader
def _define_IAppxBlockMapReader():
    IAppxBlockMapReader = win32more.Storage.Packaging.Appx.IAppxBlockMapReader_head
    IAppxBlockMapReader.GetFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapFile_head), use_last_error=False)(3, 'GetFile', ((1, 'filename'),(1, 'file'),)))
    IAppxBlockMapReader.GetFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapFilesEnumerator_head), use_last_error=False)(4, 'GetFiles', ((1, 'enumerator'),)))
    IAppxBlockMapReader.GetHashMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUri_head), use_last_error=False)(5, 'GetHashMethod', ((1, 'hashMethod'),)))
    IAppxBlockMapReader.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(6, 'GetStream', ((1, 'blockMapStream'),)))
    return IAppxBlockMapReader
def _define_IAppxBlockMapFile_head():
    class IAppxBlockMapFile(win32more.System.Com.IUnknown_head):
        Guid = Guid('277672ac-4f63-42c1-8abc-beae3600eb59')
    return IAppxBlockMapFile
def _define_IAppxBlockMapFile():
    IAppxBlockMapFile = win32more.Storage.Packaging.Appx.IAppxBlockMapFile_head
    IAppxBlockMapFile.GetBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapBlocksEnumerator_head), use_last_error=False)(3, 'GetBlocks', ((1, 'blocks'),)))
    IAppxBlockMapFile.GetLocalFileHeaderSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetLocalFileHeaderSize', ((1, 'lfhSize'),)))
    IAppxBlockMapFile.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetName', ((1, 'name'),)))
    IAppxBlockMapFile.GetUncompressedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(6, 'GetUncompressedSize', ((1, 'size'),)))
    IAppxBlockMapFile.ValidateFileHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'ValidateFileHash', ((1, 'fileStream'),(1, 'isValid'),)))
    return IAppxBlockMapFile
def _define_IAppxBlockMapFilesEnumerator_head():
    class IAppxBlockMapFilesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('02b856a2-4262-4070-bacb-1a8cbbc42305')
    return IAppxBlockMapFilesEnumerator
def _define_IAppxBlockMapFilesEnumerator():
    IAppxBlockMapFilesEnumerator = win32more.Storage.Packaging.Appx.IAppxBlockMapFilesEnumerator_head
    IAppxBlockMapFilesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapFile_head), use_last_error=False)(3, 'GetCurrent', ((1, 'file'),)))
    IAppxBlockMapFilesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxBlockMapFilesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasCurrent'),)))
    return IAppxBlockMapFilesEnumerator
def _define_IAppxBlockMapBlock_head():
    class IAppxBlockMapBlock(win32more.System.Com.IUnknown_head):
        Guid = Guid('75cf3930-3244-4fe0-a8c8-e0bcb270b889')
    return IAppxBlockMapBlock
def _define_IAppxBlockMapBlock():
    IAppxBlockMapBlock = win32more.Storage.Packaging.Appx.IAppxBlockMapBlock_head
    IAppxBlockMapBlock.GetHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(3, 'GetHash', ((1, 'bufferSize'),(1, 'buffer'),)))
    IAppxBlockMapBlock.GetCompressedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetCompressedSize', ((1, 'size'),)))
    return IAppxBlockMapBlock
def _define_IAppxBlockMapBlocksEnumerator_head():
    class IAppxBlockMapBlocksEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('6b429b5b-36ef-479e-b9eb-0c1482b49e16')
    return IAppxBlockMapBlocksEnumerator
def _define_IAppxBlockMapBlocksEnumerator():
    IAppxBlockMapBlocksEnumerator = win32more.Storage.Packaging.Appx.IAppxBlockMapBlocksEnumerator_head
    IAppxBlockMapBlocksEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapBlock_head), use_last_error=False)(3, 'GetCurrent', ((1, 'block'),)))
    IAppxBlockMapBlocksEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxBlockMapBlocksEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxBlockMapBlocksEnumerator
def _define_IAppxManifestReader_head():
    class IAppxManifestReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e1bd148-55a0-4480-a3d1-15544710637c')
    return IAppxManifestReader
def _define_IAppxManifestReader():
    IAppxManifestReader = win32more.Storage.Packaging.Appx.IAppxManifestReader_head
    IAppxManifestReader.GetPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestPackageId_head), use_last_error=False)(3, 'GetPackageId', ((1, 'packageId'),)))
    IAppxManifestReader.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestProperties_head), use_last_error=False)(4, 'GetProperties', ((1, 'packageProperties'),)))
    IAppxManifestReader.GetPackageDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestPackageDependenciesEnumerator_head), use_last_error=False)(5, 'GetPackageDependencies', ((1, 'dependencies'),)))
    IAppxManifestReader.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.APPX_CAPABILITIES), use_last_error=False)(6, 'GetCapabilities', ((1, 'capabilities'),)))
    IAppxManifestReader.GetResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestResourcesEnumerator_head), use_last_error=False)(7, 'GetResources', ((1, 'resources'),)))
    IAppxManifestReader.GetDeviceCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestDeviceCapabilitiesEnumerator_head), use_last_error=False)(8, 'GetDeviceCapabilities', ((1, 'deviceCapabilities'),)))
    IAppxManifestReader.GetPrerequisite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt64), use_last_error=False)(9, 'GetPrerequisite', ((1, 'name'),(1, 'value'),)))
    IAppxManifestReader.GetApplications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestApplicationsEnumerator_head), use_last_error=False)(10, 'GetApplications', ((1, 'applications'),)))
    IAppxManifestReader.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(11, 'GetStream', ((1, 'manifestStream'),)))
    return IAppxManifestReader
def _define_IAppxManifestReader2_head():
    class IAppxManifestReader2(win32more.Storage.Packaging.Appx.IAppxManifestReader_head):
        Guid = Guid('d06f67bc-b31d-4eba-a8af-638e73e77b4d')
    return IAppxManifestReader2
def _define_IAppxManifestReader2():
    IAppxManifestReader2 = win32more.Storage.Packaging.Appx.IAppxManifestReader2_head
    IAppxManifestReader2.GetQualifiedResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator_head), use_last_error=False)(12, 'GetQualifiedResources', ((1, 'resources'),)))
    return IAppxManifestReader2
def _define_IAppxManifestReader3_head():
    class IAppxManifestReader3(win32more.Storage.Packaging.Appx.IAppxManifestReader2_head):
        Guid = Guid('c43825ab-69b7-400a-9709-cc37f5a72d24')
    return IAppxManifestReader3
def _define_IAppxManifestReader3():
    IAppxManifestReader3 = win32more.Storage.Packaging.Appx.IAppxManifestReader3_head
    IAppxManifestReader3.GetCapabilitiesByCapabilityClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Appx.APPX_CAPABILITY_CLASS_TYPE,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestCapabilitiesEnumerator_head), use_last_error=False)(13, 'GetCapabilitiesByCapabilityClass', ((1, 'capabilityClass'),(1, 'capabilities'),)))
    IAppxManifestReader3.GetTargetDeviceFamilies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator_head), use_last_error=False)(14, 'GetTargetDeviceFamilies', ((1, 'targetDeviceFamilies'),)))
    return IAppxManifestReader3
def _define_IAppxManifestReader4_head():
    class IAppxManifestReader4(win32more.Storage.Packaging.Appx.IAppxManifestReader3_head):
        Guid = Guid('4579bb7c-741d-4161-b5a1-47bd3b78ad9b')
    return IAppxManifestReader4
def _define_IAppxManifestReader4():
    IAppxManifestReader4 = win32more.Storage.Packaging.Appx.IAppxManifestReader4_head
    IAppxManifestReader4.GetOptionalPackageInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestOptionalPackageInfo_head), use_last_error=False)(15, 'GetOptionalPackageInfo', ((1, 'optionalPackageInfo'),)))
    return IAppxManifestReader4
def _define_IAppxManifestReader5_head():
    class IAppxManifestReader5(win32more.System.Com.IUnknown_head):
        Guid = Guid('8d7ae132-a690-4c00-b75a-6aae1feaac80')
    return IAppxManifestReader5
def _define_IAppxManifestReader5():
    IAppxManifestReader5 = win32more.Storage.Packaging.Appx.IAppxManifestReader5_head
    IAppxManifestReader5.GetMainPackageDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestMainPackageDependenciesEnumerator_head), use_last_error=False)(3, 'GetMainPackageDependencies', ((1, 'mainPackageDependencies'),)))
    return IAppxManifestReader5
def _define_IAppxManifestReader6_head():
    class IAppxManifestReader6(win32more.System.Com.IUnknown_head):
        Guid = Guid('34deaca4-d3c0-4e3e-b312-e42625e3807e')
    return IAppxManifestReader6
def _define_IAppxManifestReader6():
    IAppxManifestReader6 = win32more.Storage.Packaging.Appx.IAppxManifestReader6_head
    IAppxManifestReader6.GetIsNonQualifiedResourcePackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetIsNonQualifiedResourcePackage', ((1, 'isNonQualifiedResourcePackage'),)))
    return IAppxManifestReader6
def _define_IAppxManifestReader7_head():
    class IAppxManifestReader7(win32more.System.Com.IUnknown_head):
        Guid = Guid('8efe6f27-0ce0-4988-b32d-738eb63db3b7')
    return IAppxManifestReader7
def _define_IAppxManifestReader7():
    IAppxManifestReader7 = win32more.Storage.Packaging.Appx.IAppxManifestReader7_head
    IAppxManifestReader7.GetDriverDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestDriverDependenciesEnumerator_head), use_last_error=False)(3, 'GetDriverDependencies', ((1, 'driverDependencies'),)))
    IAppxManifestReader7.GetOSPackageDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestOSPackageDependenciesEnumerator_head), use_last_error=False)(4, 'GetOSPackageDependencies', ((1, 'osPackageDependencies'),)))
    IAppxManifestReader7.GetHostRuntimeDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependenciesEnumerator_head), use_last_error=False)(5, 'GetHostRuntimeDependencies', ((1, 'hostRuntimeDependencies'),)))
    return IAppxManifestReader7
def _define_IAppxManifestDriverDependenciesEnumerator_head():
    class IAppxManifestDriverDependenciesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('fe039db2-467f-4755-8404-8f5eb6865b33')
    return IAppxManifestDriverDependenciesEnumerator
def _define_IAppxManifestDriverDependenciesEnumerator():
    IAppxManifestDriverDependenciesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestDriverDependenciesEnumerator_head
    IAppxManifestDriverDependenciesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestDriverDependency_head), use_last_error=False)(3, 'GetCurrent', ((1, 'driverDependency'),)))
    IAppxManifestDriverDependenciesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestDriverDependenciesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestDriverDependenciesEnumerator
def _define_IAppxManifestDriverDependency_head():
    class IAppxManifestDriverDependency(win32more.System.Com.IUnknown_head):
        Guid = Guid('1210cb94-5a92-4602-be24-79f318af4af9')
    return IAppxManifestDriverDependency
def _define_IAppxManifestDriverDependency():
    IAppxManifestDriverDependency = win32more.Storage.Packaging.Appx.IAppxManifestDriverDependency_head
    IAppxManifestDriverDependency.GetDriverConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestDriverConstraintsEnumerator_head), use_last_error=False)(3, 'GetDriverConstraints', ((1, 'driverConstraints'),)))
    return IAppxManifestDriverDependency
def _define_IAppxManifestDriverConstraintsEnumerator_head():
    class IAppxManifestDriverConstraintsEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('d402b2d1-f600-49e0-95e6-975d8da13d89')
    return IAppxManifestDriverConstraintsEnumerator
def _define_IAppxManifestDriverConstraintsEnumerator():
    IAppxManifestDriverConstraintsEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestDriverConstraintsEnumerator_head
    IAppxManifestDriverConstraintsEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestDriverConstraint_head), use_last_error=False)(3, 'GetCurrent', ((1, 'driverConstraint'),)))
    IAppxManifestDriverConstraintsEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestDriverConstraintsEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestDriverConstraintsEnumerator
def _define_IAppxManifestDriverConstraint_head():
    class IAppxManifestDriverConstraint(win32more.System.Com.IUnknown_head):
        Guid = Guid('c031bee4-bbcc-48ea-a237-c34045c80a07')
    return IAppxManifestDriverConstraint
def _define_IAppxManifestDriverConstraint():
    IAppxManifestDriverConstraint = win32more.Storage.Packaging.Appx.IAppxManifestDriverConstraint_head
    IAppxManifestDriverConstraint.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestDriverConstraint.GetMinVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(4, 'GetMinVersion', ((1, 'minVersion'),)))
    IAppxManifestDriverConstraint.GetMinDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetMinDate', ((1, 'minDate'),)))
    return IAppxManifestDriverConstraint
def _define_IAppxManifestOSPackageDependenciesEnumerator_head():
    class IAppxManifestOSPackageDependenciesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('b84e2fc3-f8ec-4bc1-8ae2-156346f5ffea')
    return IAppxManifestOSPackageDependenciesEnumerator
def _define_IAppxManifestOSPackageDependenciesEnumerator():
    IAppxManifestOSPackageDependenciesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestOSPackageDependenciesEnumerator_head
    IAppxManifestOSPackageDependenciesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestOSPackageDependency_head), use_last_error=False)(3, 'GetCurrent', ((1, 'osPackageDependency'),)))
    IAppxManifestOSPackageDependenciesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestOSPackageDependenciesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestOSPackageDependenciesEnumerator
def _define_IAppxManifestOSPackageDependency_head():
    class IAppxManifestOSPackageDependency(win32more.System.Com.IUnknown_head):
        Guid = Guid('154995ee-54a6-4f14-ac97-d8cf0519644b')
    return IAppxManifestOSPackageDependency
def _define_IAppxManifestOSPackageDependency():
    IAppxManifestOSPackageDependency = win32more.Storage.Packaging.Appx.IAppxManifestOSPackageDependency_head
    IAppxManifestOSPackageDependency.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestOSPackageDependency.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(4, 'GetVersion', ((1, 'version'),)))
    return IAppxManifestOSPackageDependency
def _define_IAppxManifestHostRuntimeDependenciesEnumerator_head():
    class IAppxManifestHostRuntimeDependenciesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('6427a646-7f49-433e-b1a6-0da309f6885a')
    return IAppxManifestHostRuntimeDependenciesEnumerator
def _define_IAppxManifestHostRuntimeDependenciesEnumerator():
    IAppxManifestHostRuntimeDependenciesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependenciesEnumerator_head
    IAppxManifestHostRuntimeDependenciesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependency_head), use_last_error=False)(3, 'GetCurrent', ((1, 'hostRuntimeDependency'),)))
    IAppxManifestHostRuntimeDependenciesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestHostRuntimeDependenciesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestHostRuntimeDependenciesEnumerator
def _define_IAppxManifestHostRuntimeDependency_head():
    class IAppxManifestHostRuntimeDependency(win32more.System.Com.IUnknown_head):
        Guid = Guid('3455d234-8414-410d-95c7-7b35255b8391')
    return IAppxManifestHostRuntimeDependency
def _define_IAppxManifestHostRuntimeDependency():
    IAppxManifestHostRuntimeDependency = win32more.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependency_head
    IAppxManifestHostRuntimeDependency.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestHostRuntimeDependency.GetPublisher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetPublisher', ((1, 'publisher'),)))
    IAppxManifestHostRuntimeDependency.GetMinVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetMinVersion', ((1, 'minVersion'),)))
    return IAppxManifestHostRuntimeDependency
def _define_IAppxManifestHostRuntimeDependency2_head():
    class IAppxManifestHostRuntimeDependency2(win32more.System.Com.IUnknown_head):
        Guid = Guid('c26f23a8-ee10-4ad6-b898-2b4d7aebfe6a')
    return IAppxManifestHostRuntimeDependency2
def _define_IAppxManifestHostRuntimeDependency2():
    IAppxManifestHostRuntimeDependency2 = win32more.Storage.Packaging.Appx.IAppxManifestHostRuntimeDependency2_head
    IAppxManifestHostRuntimeDependency2.GetPackageFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetPackageFamilyName', ((1, 'packageFamilyName'),)))
    return IAppxManifestHostRuntimeDependency2
def _define_IAppxManifestOptionalPackageInfo_head():
    class IAppxManifestOptionalPackageInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('2634847d-5b5d-4fe5-a243-002ff95edc7e')
    return IAppxManifestOptionalPackageInfo
def _define_IAppxManifestOptionalPackageInfo():
    IAppxManifestOptionalPackageInfo = win32more.Storage.Packaging.Appx.IAppxManifestOptionalPackageInfo_head
    IAppxManifestOptionalPackageInfo.GetIsOptionalPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetIsOptionalPackage', ((1, 'isOptionalPackage'),)))
    IAppxManifestOptionalPackageInfo.GetMainPackageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetMainPackageName', ((1, 'mainPackageName'),)))
    return IAppxManifestOptionalPackageInfo
def _define_IAppxManifestMainPackageDependenciesEnumerator_head():
    class IAppxManifestMainPackageDependenciesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('a99c4f00-51d2-4f0f-ba46-7ed5255ebdff')
    return IAppxManifestMainPackageDependenciesEnumerator
def _define_IAppxManifestMainPackageDependenciesEnumerator():
    IAppxManifestMainPackageDependenciesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestMainPackageDependenciesEnumerator_head
    IAppxManifestMainPackageDependenciesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestMainPackageDependency_head), use_last_error=False)(3, 'GetCurrent', ((1, 'mainPackageDependency'),)))
    IAppxManifestMainPackageDependenciesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestMainPackageDependenciesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestMainPackageDependenciesEnumerator
def _define_IAppxManifestMainPackageDependency_head():
    class IAppxManifestMainPackageDependency(win32more.System.Com.IUnknown_head):
        Guid = Guid('05d0611c-bc29-46d5-97e2-84b9c79bd8ae')
    return IAppxManifestMainPackageDependency
def _define_IAppxManifestMainPackageDependency():
    IAppxManifestMainPackageDependency = win32more.Storage.Packaging.Appx.IAppxManifestMainPackageDependency_head
    IAppxManifestMainPackageDependency.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestMainPackageDependency.GetPublisher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetPublisher', ((1, 'publisher'),)))
    IAppxManifestMainPackageDependency.GetPackageFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetPackageFamilyName', ((1, 'packageFamilyName'),)))
    return IAppxManifestMainPackageDependency
def _define_IAppxManifestPackageId_head():
    class IAppxManifestPackageId(win32more.System.Com.IUnknown_head):
        Guid = Guid('283ce2d7-7153-4a91-9649-7a0f7240945f')
    return IAppxManifestPackageId
def _define_IAppxManifestPackageId():
    IAppxManifestPackageId = win32more.Storage.Packaging.Appx.IAppxManifestPackageId_head
    IAppxManifestPackageId.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestPackageId.GetArchitecture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE), use_last_error=False)(4, 'GetArchitecture', ((1, 'architecture'),)))
    IAppxManifestPackageId.GetPublisher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetPublisher', ((1, 'publisher'),)))
    IAppxManifestPackageId.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(6, 'GetVersion', ((1, 'packageVersion'),)))
    IAppxManifestPackageId.GetResourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetResourceId', ((1, 'resourceId'),)))
    IAppxManifestPackageId.ComparePublisher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'ComparePublisher', ((1, 'other'),(1, 'isSame'),)))
    IAppxManifestPackageId.GetPackageFullName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetPackageFullName', ((1, 'packageFullName'),)))
    IAppxManifestPackageId.GetPackageFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'GetPackageFamilyName', ((1, 'packageFamilyName'),)))
    return IAppxManifestPackageId
def _define_IAppxManifestPackageId2_head():
    class IAppxManifestPackageId2(win32more.Storage.Packaging.Appx.IAppxManifestPackageId_head):
        Guid = Guid('2256999d-d617-42f1-880e-0ba4542319d5')
    return IAppxManifestPackageId2
def _define_IAppxManifestPackageId2():
    IAppxManifestPackageId2 = win32more.Storage.Packaging.Appx.IAppxManifestPackageId2_head
    IAppxManifestPackageId2.GetArchitecture2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.APPX_PACKAGE_ARCHITECTURE2), use_last_error=False)(11, 'GetArchitecture2', ((1, 'architecture'),)))
    return IAppxManifestPackageId2
def _define_IAppxManifestProperties_head():
    class IAppxManifestProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('03faf64d-f26f-4b2c-aaf7-8fe7789b8bca')
    return IAppxManifestProperties
def _define_IAppxManifestProperties():
    IAppxManifestProperties = win32more.Storage.Packaging.Appx.IAppxManifestProperties_head
    IAppxManifestProperties.GetBoolValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetBoolValue', ((1, 'name'),(1, 'value'),)))
    IAppxManifestProperties.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetStringValue', ((1, 'name'),(1, 'value'),)))
    return IAppxManifestProperties
def _define_IAppxManifestTargetDeviceFamiliesEnumerator_head():
    class IAppxManifestTargetDeviceFamiliesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('36537f36-27a4-4788-88c0-733819575017')
    return IAppxManifestTargetDeviceFamiliesEnumerator
def _define_IAppxManifestTargetDeviceFamiliesEnumerator():
    IAppxManifestTargetDeviceFamiliesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator_head
    IAppxManifestTargetDeviceFamiliesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamily_head), use_last_error=False)(3, 'GetCurrent', ((1, 'targetDeviceFamily'),)))
    IAppxManifestTargetDeviceFamiliesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestTargetDeviceFamiliesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestTargetDeviceFamiliesEnumerator
def _define_IAppxManifestTargetDeviceFamily_head():
    class IAppxManifestTargetDeviceFamily(win32more.System.Com.IUnknown_head):
        Guid = Guid('9091b09b-c8d5-4f31-8687-a338259faefb')
    return IAppxManifestTargetDeviceFamily
def _define_IAppxManifestTargetDeviceFamily():
    IAppxManifestTargetDeviceFamily = win32more.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamily_head
    IAppxManifestTargetDeviceFamily.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestTargetDeviceFamily.GetMinVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(4, 'GetMinVersion', ((1, 'minVersion'),)))
    IAppxManifestTargetDeviceFamily.GetMaxVersionTested = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetMaxVersionTested', ((1, 'maxVersionTested'),)))
    return IAppxManifestTargetDeviceFamily
def _define_IAppxManifestPackageDependenciesEnumerator_head():
    class IAppxManifestPackageDependenciesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('b43bbcf9-65a6-42dd-bac0-8c6741e7f5a4')
    return IAppxManifestPackageDependenciesEnumerator
def _define_IAppxManifestPackageDependenciesEnumerator():
    IAppxManifestPackageDependenciesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestPackageDependenciesEnumerator_head
    IAppxManifestPackageDependenciesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestPackageDependency_head), use_last_error=False)(3, 'GetCurrent', ((1, 'dependency'),)))
    IAppxManifestPackageDependenciesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestPackageDependenciesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestPackageDependenciesEnumerator
def _define_IAppxManifestPackageDependency_head():
    class IAppxManifestPackageDependency(win32more.System.Com.IUnknown_head):
        Guid = Guid('e4946b59-733e-43f0-a724-3bde4c1285a0')
    return IAppxManifestPackageDependency
def _define_IAppxManifestPackageDependency():
    IAppxManifestPackageDependency = win32more.Storage.Packaging.Appx.IAppxManifestPackageDependency_head
    IAppxManifestPackageDependency.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'name'),)))
    IAppxManifestPackageDependency.GetPublisher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetPublisher', ((1, 'publisher'),)))
    IAppxManifestPackageDependency.GetMinVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetMinVersion', ((1, 'minVersion'),)))
    return IAppxManifestPackageDependency
def _define_IAppxManifestPackageDependency2_head():
    class IAppxManifestPackageDependency2(win32more.Storage.Packaging.Appx.IAppxManifestPackageDependency_head):
        Guid = Guid('dda0b713-f3ff-49d3-898a-2786780c5d98')
    return IAppxManifestPackageDependency2
def _define_IAppxManifestPackageDependency2():
    IAppxManifestPackageDependency2 = win32more.Storage.Packaging.Appx.IAppxManifestPackageDependency2_head
    IAppxManifestPackageDependency2.GetMaxMajorVersionTested = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(6, 'GetMaxMajorVersionTested', ((1, 'maxMajorVersionTested'),)))
    return IAppxManifestPackageDependency2
def _define_IAppxManifestPackageDependency3_head():
    class IAppxManifestPackageDependency3(win32more.System.Com.IUnknown_head):
        Guid = Guid('1ac56374-6198-4d6b-92e4-749d5ab8a895')
    return IAppxManifestPackageDependency3
def _define_IAppxManifestPackageDependency3():
    IAppxManifestPackageDependency3 = win32more.Storage.Packaging.Appx.IAppxManifestPackageDependency3_head
    IAppxManifestPackageDependency3.GetIsOptional = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetIsOptional', ((1, 'isOptional'),)))
    return IAppxManifestPackageDependency3
def _define_IAppxManifestResourcesEnumerator_head():
    class IAppxManifestResourcesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('de4dfbbd-881a-48bb-858c-d6f2baeae6ed')
    return IAppxManifestResourcesEnumerator
def _define_IAppxManifestResourcesEnumerator():
    IAppxManifestResourcesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestResourcesEnumerator_head
    IAppxManifestResourcesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetCurrent', ((1, 'resource'),)))
    IAppxManifestResourcesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestResourcesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestResourcesEnumerator
def _define_IAppxManifestDeviceCapabilitiesEnumerator_head():
    class IAppxManifestDeviceCapabilitiesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('30204541-427b-4a1c-bacf-655bf463a540')
    return IAppxManifestDeviceCapabilitiesEnumerator
def _define_IAppxManifestDeviceCapabilitiesEnumerator():
    IAppxManifestDeviceCapabilitiesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestDeviceCapabilitiesEnumerator_head
    IAppxManifestDeviceCapabilitiesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetCurrent', ((1, 'deviceCapability'),)))
    IAppxManifestDeviceCapabilitiesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestDeviceCapabilitiesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestDeviceCapabilitiesEnumerator
def _define_IAppxManifestCapabilitiesEnumerator_head():
    class IAppxManifestCapabilitiesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('11d22258-f470-42c1-b291-8361c5437e41')
    return IAppxManifestCapabilitiesEnumerator
def _define_IAppxManifestCapabilitiesEnumerator():
    IAppxManifestCapabilitiesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestCapabilitiesEnumerator_head
    IAppxManifestCapabilitiesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetCurrent', ((1, 'capability'),)))
    IAppxManifestCapabilitiesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestCapabilitiesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestCapabilitiesEnumerator
def _define_IAppxManifestApplicationsEnumerator_head():
    class IAppxManifestApplicationsEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('9eb8a55a-f04b-4d0d-808d-686185d4847a')
    return IAppxManifestApplicationsEnumerator
def _define_IAppxManifestApplicationsEnumerator():
    IAppxManifestApplicationsEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestApplicationsEnumerator_head
    IAppxManifestApplicationsEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestApplication_head), use_last_error=False)(3, 'GetCurrent', ((1, 'application'),)))
    IAppxManifestApplicationsEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestApplicationsEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestApplicationsEnumerator
def _define_IAppxManifestApplication_head():
    class IAppxManifestApplication(win32more.System.Com.IUnknown_head):
        Guid = Guid('5da89bf4-3773-46be-b650-7e744863b7e8')
    return IAppxManifestApplication
def _define_IAppxManifestApplication():
    IAppxManifestApplication = win32more.Storage.Packaging.Appx.IAppxManifestApplication_head
    IAppxManifestApplication.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetStringValue', ((1, 'name'),(1, 'value'),)))
    IAppxManifestApplication.GetAppUserModelId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetAppUserModelId', ((1, 'appUserModelId'),)))
    return IAppxManifestApplication
def _define_IAppxManifestQualifiedResourcesEnumerator_head():
    class IAppxManifestQualifiedResourcesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ef6adfe-3762-4a8f-9373-2fc5d444c8d2')
    return IAppxManifestQualifiedResourcesEnumerator
def _define_IAppxManifestQualifiedResourcesEnumerator():
    IAppxManifestQualifiedResourcesEnumerator = win32more.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator_head
    IAppxManifestQualifiedResourcesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestQualifiedResource_head), use_last_error=False)(3, 'GetCurrent', ((1, 'resource'),)))
    IAppxManifestQualifiedResourcesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxManifestQualifiedResourcesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxManifestQualifiedResourcesEnumerator
def _define_IAppxManifestQualifiedResource_head():
    class IAppxManifestQualifiedResource(win32more.System.Com.IUnknown_head):
        Guid = Guid('3b53a497-3c5c-48d1-9ea3-bb7eac8cd7d4')
    return IAppxManifestQualifiedResource
def _define_IAppxManifestQualifiedResource():
    IAppxManifestQualifiedResource = win32more.Storage.Packaging.Appx.IAppxManifestQualifiedResource_head
    IAppxManifestQualifiedResource.GetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetLanguage', ((1, 'language'),)))
    IAppxManifestQualifiedResource.GetScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetScale', ((1, 'scale'),)))
    IAppxManifestQualifiedResource.GetDXFeatureLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.DX_FEATURE_LEVEL), use_last_error=False)(5, 'GetDXFeatureLevel', ((1, 'dxFeatureLevel'),)))
    return IAppxManifestQualifiedResource
def _define_IAppxBundleFactory_head():
    class IAppxBundleFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('bba65864-965f-4a5f-855f-f074bdbf3a7b')
    return IAppxBundleFactory
def _define_IAppxBundleFactory():
    IAppxBundleFactory = win32more.Storage.Packaging.Appx.IAppxBundleFactory_head
    IAppxBundleFactory.CreateBundleWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt64,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleWriter_head), use_last_error=False)(3, 'CreateBundleWriter', ((1, 'outputStream'),(1, 'bundleVersion'),(1, 'bundleWriter'),)))
    IAppxBundleFactory.CreateBundleReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleReader_head), use_last_error=False)(4, 'CreateBundleReader', ((1, 'inputStream'),(1, 'bundleReader'),)))
    IAppxBundleFactory.CreateBundleManifestReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestReader_head), use_last_error=False)(5, 'CreateBundleManifestReader', ((1, 'inputStream'),(1, 'manifestReader'),)))
    return IAppxBundleFactory
def _define_IAppxBundleWriter_head():
    class IAppxBundleWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec446fe8-bfec-4c64-ab4f-49f038f0c6d2')
    return IAppxBundleWriter
def _define_IAppxBundleWriter():
    IAppxBundleWriter = win32more.Storage.Packaging.Appx.IAppxBundleWriter_head
    IAppxBundleWriter.AddPayloadPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddPayloadPackage', ((1, 'fileName'),(1, 'packageStream'),)))
    IAppxBundleWriter.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    return IAppxBundleWriter
def _define_IAppxBundleWriter2_head():
    class IAppxBundleWriter2(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d8fe971-01cc-49a0-b685-233851279962')
    return IAppxBundleWriter2
def _define_IAppxBundleWriter2():
    IAppxBundleWriter2 = win32more.Storage.Packaging.Appx.IAppxBundleWriter2_head
    IAppxBundleWriter2.AddExternalPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddExternalPackageReference', ((1, 'fileName'),(1, 'inputStream'),)))
    return IAppxBundleWriter2
def _define_IAppxBundleWriter3_head():
    class IAppxBundleWriter3(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad711152-f969-4193-82d5-9ddf2786d21a')
    return IAppxBundleWriter3
def _define_IAppxBundleWriter3():
    IAppxBundleWriter3 = win32more.Storage.Packaging.Appx.IAppxBundleWriter3_head
    IAppxBundleWriter3.AddPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddPackageReference', ((1, 'fileName'),(1, 'inputStream'),)))
    IAppxBundleWriter3.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'Close', ((1, 'hashMethodString'),)))
    return IAppxBundleWriter3
def _define_IAppxBundleWriter4_head():
    class IAppxBundleWriter4(win32more.System.Com.IUnknown_head):
        Guid = Guid('9cd9d523-5009-4c01-9882-dc029fbd47a3')
    return IAppxBundleWriter4
def _define_IAppxBundleWriter4():
    IAppxBundleWriter4 = win32more.Storage.Packaging.Appx.IAppxBundleWriter4_head
    IAppxBundleWriter4.AddPayloadPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.Foundation.BOOL, use_last_error=False)(3, 'AddPayloadPackage', ((1, 'fileName'),(1, 'packageStream'),(1, 'isDefaultApplicablePackage'),)))
    IAppxBundleWriter4.AddPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.Foundation.BOOL, use_last_error=False)(4, 'AddPackageReference', ((1, 'fileName'),(1, 'inputStream'),(1, 'isDefaultApplicablePackage'),)))
    IAppxBundleWriter4.AddExternalPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.Foundation.BOOL, use_last_error=False)(5, 'AddExternalPackageReference', ((1, 'fileName'),(1, 'inputStream'),(1, 'isDefaultApplicablePackage'),)))
    return IAppxBundleWriter4
def _define_IAppxBundleReader_head():
    class IAppxBundleReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('dd75b8c0-ba76-43b0-ae0f-68656a1dc5c8')
    return IAppxBundleReader
def _define_IAppxBundleReader():
    IAppxBundleReader = win32more.Storage.Packaging.Appx.IAppxBundleReader_head
    IAppxBundleReader.GetFootprintFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Appx.APPX_BUNDLE_FOOTPRINT_FILE_TYPE,POINTER(win32more.Storage.Packaging.Appx.IAppxFile_head), use_last_error=False)(3, 'GetFootprintFile', ((1, 'fileType'),(1, 'footprintFile'),)))
    IAppxBundleReader.GetBlockMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBlockMapReader_head), use_last_error=False)(4, 'GetBlockMap', ((1, 'blockMapReader'),)))
    IAppxBundleReader.GetManifest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestReader_head), use_last_error=False)(5, 'GetManifest', ((1, 'manifestReader'),)))
    IAppxBundleReader.GetPayloadPackages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxFilesEnumerator_head), use_last_error=False)(6, 'GetPayloadPackages', ((1, 'payloadPackages'),)))
    IAppxBundleReader.GetPayloadPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Appx.IAppxFile_head), use_last_error=False)(7, 'GetPayloadPackage', ((1, 'fileName'),(1, 'payloadPackage'),)))
    return IAppxBundleReader
def _define_IAppxBundleManifestReader_head():
    class IAppxBundleManifestReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf0ebbc1-cc99-4106-91eb-e67462e04fb0')
    return IAppxBundleManifestReader
def _define_IAppxBundleManifestReader():
    IAppxBundleManifestReader = win32more.Storage.Packaging.Appx.IAppxBundleManifestReader_head
    IAppxBundleManifestReader.GetPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestPackageId_head), use_last_error=False)(3, 'GetPackageId', ((1, 'packageId'),)))
    IAppxBundleManifestReader.GetPackageInfoItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator_head), use_last_error=False)(4, 'GetPackageInfoItems', ((1, 'packageInfoItems'),)))
    IAppxBundleManifestReader.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(5, 'GetStream', ((1, 'manifestStream'),)))
    return IAppxBundleManifestReader
def _define_IAppxBundleManifestReader2_head():
    class IAppxBundleManifestReader2(win32more.System.Com.IUnknown_head):
        Guid = Guid('5517df70-033f-4af2-8213-87d766805c02')
    return IAppxBundleManifestReader2
def _define_IAppxBundleManifestReader2():
    IAppxBundleManifestReader2 = win32more.Storage.Packaging.Appx.IAppxBundleManifestReader2_head
    IAppxBundleManifestReader2.GetOptionalBundles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfoEnumerator_head), use_last_error=False)(3, 'GetOptionalBundles', ((1, 'optionalBundles'),)))
    return IAppxBundleManifestReader2
def _define_IAppxBundleManifestPackageInfoEnumerator_head():
    class IAppxBundleManifestPackageInfoEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('f9b856ee-49a6-4e19-b2b0-6a2406d63a32')
    return IAppxBundleManifestPackageInfoEnumerator
def _define_IAppxBundleManifestPackageInfoEnumerator():
    IAppxBundleManifestPackageInfoEnumerator = win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator_head
    IAppxBundleManifestPackageInfoEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo_head), use_last_error=False)(3, 'GetCurrent', ((1, 'packageInfo'),)))
    IAppxBundleManifestPackageInfoEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxBundleManifestPackageInfoEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxBundleManifestPackageInfoEnumerator
def _define_IAppxBundleManifestPackageInfo_head():
    class IAppxBundleManifestPackageInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('54cd06c1-268f-40bb-8ed2-757a9ebaec8d')
    return IAppxBundleManifestPackageInfo
def _define_IAppxBundleManifestPackageInfo():
    IAppxBundleManifestPackageInfo = win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo_head
    IAppxBundleManifestPackageInfo.GetPackageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE), use_last_error=False)(3, 'GetPackageType', ((1, 'packageType'),)))
    IAppxBundleManifestPackageInfo.GetPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestPackageId_head), use_last_error=False)(4, 'GetPackageId', ((1, 'packageId'),)))
    IAppxBundleManifestPackageInfo.GetFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetFileName', ((1, 'fileName'),)))
    IAppxBundleManifestPackageInfo.GetOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(6, 'GetOffset', ((1, 'offset'),)))
    IAppxBundleManifestPackageInfo.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(7, 'GetSize', ((1, 'size'),)))
    IAppxBundleManifestPackageInfo.GetResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestQualifiedResourcesEnumerator_head), use_last_error=False)(8, 'GetResources', ((1, 'resources'),)))
    return IAppxBundleManifestPackageInfo
def _define_IAppxBundleManifestPackageInfo2_head():
    class IAppxBundleManifestPackageInfo2(win32more.System.Com.IUnknown_head):
        Guid = Guid('44c2acbc-b2cf-4ccb-bbdb-9c6da8c3bc9e')
    return IAppxBundleManifestPackageInfo2
def _define_IAppxBundleManifestPackageInfo2():
    IAppxBundleManifestPackageInfo2 = win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo2_head
    IAppxBundleManifestPackageInfo2.GetIsPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetIsPackageReference', ((1, 'isPackageReference'),)))
    IAppxBundleManifestPackageInfo2.GetIsNonQualifiedResourcePackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetIsNonQualifiedResourcePackage', ((1, 'isNonQualifiedResourcePackage'),)))
    IAppxBundleManifestPackageInfo2.GetIsDefaultApplicablePackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetIsDefaultApplicablePackage', ((1, 'isDefaultApplicablePackage'),)))
    return IAppxBundleManifestPackageInfo2
def _define_IAppxBundleManifestPackageInfo3_head():
    class IAppxBundleManifestPackageInfo3(win32more.System.Com.IUnknown_head):
        Guid = Guid('6ba74b98-bb74-4296-80d0-5f4256a99675')
    return IAppxBundleManifestPackageInfo3
def _define_IAppxBundleManifestPackageInfo3():
    IAppxBundleManifestPackageInfo3 = win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo3_head
    IAppxBundleManifestPackageInfo3.GetTargetDeviceFamilies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestTargetDeviceFamiliesEnumerator_head), use_last_error=False)(3, 'GetTargetDeviceFamilies', ((1, 'targetDeviceFamilies'),)))
    return IAppxBundleManifestPackageInfo3
def _define_IAppxBundleManifestPackageInfo4_head():
    class IAppxBundleManifestPackageInfo4(win32more.System.Com.IUnknown_head):
        Guid = Guid('5da6f13d-a8a7-4532-857c-1393d659371d')
    return IAppxBundleManifestPackageInfo4
def _define_IAppxBundleManifestPackageInfo4():
    IAppxBundleManifestPackageInfo4 = win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfo4_head
    IAppxBundleManifestPackageInfo4.GetIsStub = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetIsStub', ((1, 'isStub'),)))
    return IAppxBundleManifestPackageInfo4
def _define_IAppxBundleManifestOptionalBundleInfoEnumerator_head():
    class IAppxBundleManifestOptionalBundleInfoEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('9a178793-f97e-46ac-aaca-dd5ba4c177c8')
    return IAppxBundleManifestOptionalBundleInfoEnumerator
def _define_IAppxBundleManifestOptionalBundleInfoEnumerator():
    IAppxBundleManifestOptionalBundleInfoEnumerator = win32more.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfoEnumerator_head
    IAppxBundleManifestOptionalBundleInfoEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfo_head), use_last_error=False)(3, 'GetCurrent', ((1, 'optionalBundle'),)))
    IAppxBundleManifestOptionalBundleInfoEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxBundleManifestOptionalBundleInfoEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxBundleManifestOptionalBundleInfoEnumerator
def _define_IAppxBundleManifestOptionalBundleInfo_head():
    class IAppxBundleManifestOptionalBundleInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('515bf2e8-bcb0-4d69-8c48-e383147b6e12')
    return IAppxBundleManifestOptionalBundleInfo
def _define_IAppxBundleManifestOptionalBundleInfo():
    IAppxBundleManifestOptionalBundleInfo = win32more.Storage.Packaging.Appx.IAppxBundleManifestOptionalBundleInfo_head
    IAppxBundleManifestOptionalBundleInfo.GetPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxManifestPackageId_head), use_last_error=False)(3, 'GetPackageId', ((1, 'packageId'),)))
    IAppxBundleManifestOptionalBundleInfo.GetFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetFileName', ((1, 'fileName'),)))
    IAppxBundleManifestOptionalBundleInfo.GetPackageInfoItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxBundleManifestPackageInfoEnumerator_head), use_last_error=False)(5, 'GetPackageInfoItems', ((1, 'packageInfoItems'),)))
    return IAppxBundleManifestOptionalBundleInfo
def _define_IAppxContentGroupFilesEnumerator_head():
    class IAppxContentGroupFilesEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('1a09a2fd-7440-44eb-8c84-848205a6a1cc')
    return IAppxContentGroupFilesEnumerator
def _define_IAppxContentGroupFilesEnumerator():
    IAppxContentGroupFilesEnumerator = win32more.Storage.Packaging.Appx.IAppxContentGroupFilesEnumerator_head
    IAppxContentGroupFilesEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetCurrent', ((1, 'file'),)))
    IAppxContentGroupFilesEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxContentGroupFilesEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxContentGroupFilesEnumerator
def _define_IAppxContentGroup_head():
    class IAppxContentGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('328f6468-c04f-4e3c-b6fa-6b8d27f3003a')
    return IAppxContentGroup
def _define_IAppxContentGroup():
    IAppxContentGroup = win32more.Storage.Packaging.Appx.IAppxContentGroup_head
    IAppxContentGroup.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetName', ((1, 'groupName'),)))
    IAppxContentGroup.GetFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroupFilesEnumerator_head), use_last_error=False)(4, 'GetFiles', ((1, 'enumerator'),)))
    return IAppxContentGroup
def _define_IAppxContentGroupsEnumerator_head():
    class IAppxContentGroupsEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('3264e477-16d1-4d63-823e-7d2984696634')
    return IAppxContentGroupsEnumerator
def _define_IAppxContentGroupsEnumerator():
    IAppxContentGroupsEnumerator = win32more.Storage.Packaging.Appx.IAppxContentGroupsEnumerator_head
    IAppxContentGroupsEnumerator.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroup_head), use_last_error=False)(3, 'GetCurrent', ((1, 'stream'),)))
    IAppxContentGroupsEnumerator.GetHasCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetHasCurrent', ((1, 'hasCurrent'),)))
    IAppxContentGroupsEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'MoveNext', ((1, 'hasNext'),)))
    return IAppxContentGroupsEnumerator
def _define_IAppxContentGroupMapReader_head():
    class IAppxContentGroupMapReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('418726d8-dd99-4f5d-9886-157add20de01')
    return IAppxContentGroupMapReader
def _define_IAppxContentGroupMapReader():
    IAppxContentGroupMapReader = win32more.Storage.Packaging.Appx.IAppxContentGroupMapReader_head
    IAppxContentGroupMapReader.GetRequiredGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroup_head), use_last_error=False)(3, 'GetRequiredGroup', ((1, 'requiredGroup'),)))
    IAppxContentGroupMapReader.GetAutomaticGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroupsEnumerator_head), use_last_error=False)(4, 'GetAutomaticGroups', ((1, 'automaticGroupsEnumerator'),)))
    return IAppxContentGroupMapReader
def _define_IAppxSourceContentGroupMapReader_head():
    class IAppxSourceContentGroupMapReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('f329791d-540b-4a9f-bc75-3282b7d73193')
    return IAppxSourceContentGroupMapReader
def _define_IAppxSourceContentGroupMapReader():
    IAppxSourceContentGroupMapReader = win32more.Storage.Packaging.Appx.IAppxSourceContentGroupMapReader_head
    IAppxSourceContentGroupMapReader.GetRequiredGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroup_head), use_last_error=False)(3, 'GetRequiredGroup', ((1, 'requiredGroup'),)))
    IAppxSourceContentGroupMapReader.GetAutomaticGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.IAppxContentGroupsEnumerator_head), use_last_error=False)(4, 'GetAutomaticGroups', ((1, 'automaticGroupsEnumerator'),)))
    return IAppxSourceContentGroupMapReader
def _define_IAppxContentGroupMapWriter_head():
    class IAppxContentGroupMapWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('d07ab776-a9de-4798-8c14-3db31e687c78')
    return IAppxContentGroupMapWriter
def _define_IAppxContentGroupMapWriter():
    IAppxContentGroupMapWriter = win32more.Storage.Packaging.Appx.IAppxContentGroupMapWriter_head
    IAppxContentGroupMapWriter.AddAutomaticGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'AddAutomaticGroup', ((1, 'groupName'),)))
    IAppxContentGroupMapWriter.AddAutomaticFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'AddAutomaticFile', ((1, 'fileName'),)))
    IAppxContentGroupMapWriter.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Close', ()))
    return IAppxContentGroupMapWriter
def _define_IAppxPackagingDiagnosticEventSink_head():
    class IAppxPackagingDiagnosticEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('17239d47-6adb-45d2-80f6-f9cbc3bf059d')
    return IAppxPackagingDiagnosticEventSink
def _define_IAppxPackagingDiagnosticEventSink():
    IAppxPackagingDiagnosticEventSink = win32more.Storage.Packaging.Appx.IAppxPackagingDiagnosticEventSink_head
    IAppxPackagingDiagnosticEventSink.ReportContextChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Appx.APPX_PACKAGING_CONTEXT_CHANGE_TYPE,Int32,win32more.Foundation.PSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'ReportContextChange', ((1, 'changeType'),(1, 'contextId'),(1, 'contextName'),(1, 'contextMessage'),(1, 'detailsMessage'),)))
    IAppxPackagingDiagnosticEventSink.ReportError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'ReportError', ((1, 'errorMessage'),)))
    return IAppxPackagingDiagnosticEventSink
def _define_IAppxPackagingDiagnosticEventSinkManager_head():
    class IAppxPackagingDiagnosticEventSinkManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('369648fa-a7eb-4909-a15d-6954a078f18a')
    return IAppxPackagingDiagnosticEventSinkManager
def _define_IAppxPackagingDiagnosticEventSinkManager():
    IAppxPackagingDiagnosticEventSinkManager = win32more.Storage.Packaging.Appx.IAppxPackagingDiagnosticEventSinkManager_head
    IAppxPackagingDiagnosticEventSinkManager.SetSinkForProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Appx.IAppxPackagingDiagnosticEventSink_head, use_last_error=False)(3, 'SetSinkForProcess', ((1, 'sink'),)))
    return IAppxPackagingDiagnosticEventSinkManager
def _define_APPX_ENCRYPTED_PACKAGE_SETTINGS_head():
    class APPX_ENCRYPTED_PACKAGE_SETTINGS(Structure):
        pass
    return APPX_ENCRYPTED_PACKAGE_SETTINGS
def _define_APPX_ENCRYPTED_PACKAGE_SETTINGS():
    APPX_ENCRYPTED_PACKAGE_SETTINGS = win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head
    APPX_ENCRYPTED_PACKAGE_SETTINGS._fields_ = [
        ("keyLength", UInt32),
        ("encryptionAlgorithm", win32more.Foundation.PWSTR),
        ("useDiffusion", win32more.Foundation.BOOL),
        ("blockMapHashAlgorithm", win32more.System.Com.IUri_head),
    ]
    return APPX_ENCRYPTED_PACKAGE_SETTINGS
APPX_ENCRYPTED_PACKAGE_OPTIONS = UInt32
APPX_ENCRYPTED_PACKAGE_OPTION_NONE = 0
APPX_ENCRYPTED_PACKAGE_OPTION_DIFFUSION = 1
APPX_ENCRYPTED_PACKAGE_OPTION_PAGE_HASHING = 2
def _define_APPX_ENCRYPTED_PACKAGE_SETTINGS2_head():
    class APPX_ENCRYPTED_PACKAGE_SETTINGS2(Structure):
        pass
    return APPX_ENCRYPTED_PACKAGE_SETTINGS2
def _define_APPX_ENCRYPTED_PACKAGE_SETTINGS2():
    APPX_ENCRYPTED_PACKAGE_SETTINGS2 = win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head
    APPX_ENCRYPTED_PACKAGE_SETTINGS2._fields_ = [
        ("keyLength", UInt32),
        ("encryptionAlgorithm", win32more.Foundation.PWSTR),
        ("blockMapHashAlgorithm", win32more.System.Com.IUri_head),
        ("options", UInt32),
    ]
    return APPX_ENCRYPTED_PACKAGE_SETTINGS2
def _define_APPX_KEY_INFO_head():
    class APPX_KEY_INFO(Structure):
        pass
    return APPX_KEY_INFO
def _define_APPX_KEY_INFO():
    APPX_KEY_INFO = win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head
    APPX_KEY_INFO._fields_ = [
        ("keyLength", UInt32),
        ("keyIdLength", UInt32),
        ("key", c_char_p_no),
        ("keyId", c_char_p_no),
    ]
    return APPX_KEY_INFO
def _define_APPX_ENCRYPTED_EXEMPTIONS_head():
    class APPX_ENCRYPTED_EXEMPTIONS(Structure):
        pass
    return APPX_ENCRYPTED_EXEMPTIONS
def _define_APPX_ENCRYPTED_EXEMPTIONS():
    APPX_ENCRYPTED_EXEMPTIONS = win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head
    APPX_ENCRYPTED_EXEMPTIONS._fields_ = [
        ("count", UInt32),
        ("plainTextFiles", POINTER(win32more.Foundation.PWSTR)),
    ]
    return APPX_ENCRYPTED_EXEMPTIONS
def _define_IAppxEncryptionFactory_head():
    class IAppxEncryptionFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('80e8e04d-8c88-44ae-a011-7cadf6fb2e72')
    return IAppxEncryptionFactory
def _define_IAppxEncryptionFactory():
    IAppxEncryptionFactory = win32more.Storage.Packaging.Appx.IAppxEncryptionFactory_head
    IAppxEncryptionFactory.EncryptPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), use_last_error=False)(3, 'EncryptPackage', ((1, 'inputStream'),(1, 'outputStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),)))
    IAppxEncryptionFactory.DecryptPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head), use_last_error=False)(4, 'DecryptPackage', ((1, 'inputStream'),(1, 'outputStream'),(1, 'keyInfo'),)))
    IAppxEncryptionFactory.CreateEncryptedPackageWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head),POINTER(win32more.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head), use_last_error=False)(5, 'CreateEncryptedPackageWriter', ((1, 'outputStream'),(1, 'manifestStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),(1, 'packageWriter'),)))
    IAppxEncryptionFactory.CreateEncryptedPackageReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.IAppxPackageReader_head), use_last_error=False)(6, 'CreateEncryptedPackageReader', ((1, 'inputStream'),(1, 'keyInfo'),(1, 'packageReader'),)))
    IAppxEncryptionFactory.EncryptBundle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), use_last_error=False)(7, 'EncryptBundle', ((1, 'inputStream'),(1, 'outputStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),)))
    IAppxEncryptionFactory.DecryptBundle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head), use_last_error=False)(8, 'DecryptBundle', ((1, 'inputStream'),(1, 'outputStream'),(1, 'keyInfo'),)))
    IAppxEncryptionFactory.CreateEncryptedBundleWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt64,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head),POINTER(win32more.Storage.Packaging.Appx.IAppxEncryptedBundleWriter_head), use_last_error=False)(9, 'CreateEncryptedBundleWriter', ((1, 'outputStream'),(1, 'bundleVersion'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),(1, 'bundleWriter'),)))
    IAppxEncryptionFactory.CreateEncryptedBundleReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.IAppxBundleReader_head), use_last_error=False)(10, 'CreateEncryptedBundleReader', ((1, 'inputStream'),(1, 'keyInfo'),(1, 'bundleReader'),)))
    return IAppxEncryptionFactory
def _define_IAppxEncryptionFactory2_head():
    class IAppxEncryptionFactory2(win32more.System.Com.IUnknown_head):
        Guid = Guid('c1b11eee-c4ba-4ab2-a55d-d015fe8ff64f')
    return IAppxEncryptionFactory2
def _define_IAppxEncryptionFactory2():
    IAppxEncryptionFactory2 = win32more.Storage.Packaging.Appx.IAppxEncryptionFactory2_head
    IAppxEncryptionFactory2.CreateEncryptedPackageWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head),POINTER(win32more.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head), use_last_error=False)(3, 'CreateEncryptedPackageWriter', ((1, 'outputStream'),(1, 'manifestStream'),(1, 'contentGroupMapStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),(1, 'packageWriter'),)))
    return IAppxEncryptionFactory2
def _define_IAppxEncryptionFactory3_head():
    class IAppxEncryptionFactory3(win32more.System.Com.IUnknown_head):
        Guid = Guid('09edca37-cd64-47d6-b7e8-1cb11d4f7e05')
    return IAppxEncryptionFactory3
def _define_IAppxEncryptionFactory3():
    IAppxEncryptionFactory3 = win32more.Storage.Packaging.Appx.IAppxEncryptionFactory3_head
    IAppxEncryptionFactory3.EncryptPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), use_last_error=False)(3, 'EncryptPackage', ((1, 'inputStream'),(1, 'outputStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),)))
    IAppxEncryptionFactory3.CreateEncryptedPackageWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head),POINTER(win32more.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head), use_last_error=False)(4, 'CreateEncryptedPackageWriter', ((1, 'outputStream'),(1, 'manifestStream'),(1, 'contentGroupMapStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),(1, 'packageWriter'),)))
    IAppxEncryptionFactory3.EncryptBundle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head), use_last_error=False)(5, 'EncryptBundle', ((1, 'inputStream'),(1, 'outputStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),)))
    IAppxEncryptionFactory3.CreateEncryptedBundleWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt64,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head),POINTER(win32more.Storage.Packaging.Appx.IAppxEncryptedBundleWriter_head), use_last_error=False)(6, 'CreateEncryptedBundleWriter', ((1, 'outputStream'),(1, 'bundleVersion'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),(1, 'bundleWriter'),)))
    return IAppxEncryptionFactory3
def _define_IAppxEncryptionFactory4_head():
    class IAppxEncryptionFactory4(win32more.System.Com.IUnknown_head):
        Guid = Guid('a879611f-12fd-41fe-85d5-06ae779bbaf5')
    return IAppxEncryptionFactory4
def _define_IAppxEncryptionFactory4():
    IAppxEncryptionFactory4 = win32more.Storage.Packaging.Appx.IAppxEncryptionFactory4_head
    IAppxEncryptionFactory4.EncryptPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head),POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_EXEMPTIONS_head),UInt64, use_last_error=False)(3, 'EncryptPackage', ((1, 'inputStream'),(1, 'outputStream'),(1, 'settings'),(1, 'keyInfo'),(1, 'exemptedFiles'),(1, 'memoryLimit'),)))
    return IAppxEncryptionFactory4
def _define_IAppxEncryptedPackageWriter_head():
    class IAppxEncryptedPackageWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('f43d0b0b-1379-40e2-9b29-682ea2bf42af')
    return IAppxEncryptedPackageWriter
def _define_IAppxEncryptedPackageWriter():
    IAppxEncryptedPackageWriter = win32more.Storage.Packaging.Appx.IAppxEncryptedPackageWriter_head
    IAppxEncryptedPackageWriter.AddPayloadFileEncrypted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Appx.APPX_COMPRESSION_OPTION,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddPayloadFileEncrypted', ((1, 'fileName'),(1, 'compressionOption'),(1, 'inputStream'),)))
    IAppxEncryptedPackageWriter.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    return IAppxEncryptedPackageWriter
def _define_IAppxEncryptedPackageWriter2_head():
    class IAppxEncryptedPackageWriter2(win32more.System.Com.IUnknown_head):
        Guid = Guid('3e475447-3a25-40b5-8ad2-f953ae50c92d')
    return IAppxEncryptedPackageWriter2
def _define_IAppxEncryptedPackageWriter2():
    IAppxEncryptedPackageWriter2 = win32more.Storage.Packaging.Appx.IAppxEncryptedPackageWriter2_head
    IAppxEncryptedPackageWriter2.AddPayloadFilesEncrypted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Packaging.Appx.APPX_PACKAGE_WRITER_PAYLOAD_STREAM),UInt64, use_last_error=False)(3, 'AddPayloadFilesEncrypted', ((1, 'fileCount'),(1, 'payloadFiles'),(1, 'memoryLimit'),)))
    return IAppxEncryptedPackageWriter2
def _define_IAppxEncryptedBundleWriter_head():
    class IAppxEncryptedBundleWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('80b0902f-7bf0-4117-b8c6-4279ef81ee77')
    return IAppxEncryptedBundleWriter
def _define_IAppxEncryptedBundleWriter():
    IAppxEncryptedBundleWriter = win32more.Storage.Packaging.Appx.IAppxEncryptedBundleWriter_head
    IAppxEncryptedBundleWriter.AddPayloadPackageEncrypted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddPayloadPackageEncrypted', ((1, 'fileName'),(1, 'packageStream'),)))
    IAppxEncryptedBundleWriter.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    return IAppxEncryptedBundleWriter
def _define_IAppxEncryptedBundleWriter2_head():
    class IAppxEncryptedBundleWriter2(win32more.System.Com.IUnknown_head):
        Guid = Guid('e644be82-f0fa-42b8-a956-8d1cb48ee379')
    return IAppxEncryptedBundleWriter2
def _define_IAppxEncryptedBundleWriter2():
    IAppxEncryptedBundleWriter2 = win32more.Storage.Packaging.Appx.IAppxEncryptedBundleWriter2_head
    IAppxEncryptedBundleWriter2.AddExternalPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(3, 'AddExternalPackageReference', ((1, 'fileName'),(1, 'inputStream'),)))
    return IAppxEncryptedBundleWriter2
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION = Int32
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION_APPEND_DELTA = 0
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS = UInt32
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_NONE = 0
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_SKIP_VALIDATION = 1
APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_LOCALIZED = 2
def _define_IAppxEncryptedBundleWriter3_head():
    class IAppxEncryptedBundleWriter3(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d34deb3-5cae-4dd3-977c-504932a51d31')
    return IAppxEncryptedBundleWriter3
def _define_IAppxEncryptedBundleWriter3():
    IAppxEncryptedBundleWriter3 = win32more.Storage.Packaging.Appx.IAppxEncryptedBundleWriter3_head
    IAppxEncryptedBundleWriter3.AddPayloadPackageEncrypted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.Foundation.BOOL, use_last_error=False)(3, 'AddPayloadPackageEncrypted', ((1, 'fileName'),(1, 'packageStream'),(1, 'isDefaultApplicablePackage'),)))
    IAppxEncryptedBundleWriter3.AddExternalPackageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.Foundation.BOOL, use_last_error=False)(4, 'AddExternalPackageReference', ((1, 'fileName'),(1, 'inputStream'),(1, 'isDefaultApplicablePackage'),)))
    return IAppxEncryptedBundleWriter3
def _define_IAppxPackageEditor_head():
    class IAppxPackageEditor(win32more.System.Com.IUnknown_head):
        Guid = Guid('e2adb6dc-5e71-4416-86b6-86e5f5291a6b')
    return IAppxPackageEditor
def _define_IAppxPackageEditor():
    IAppxPackageEditor = win32more.Storage.Packaging.Appx.IAppxPackageEditor_head
    IAppxPackageEditor.SetWorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetWorkingDirectory', ((1, 'workingDirectory'),)))
    IAppxPackageEditor.CreateDeltaPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head, use_last_error=False)(4, 'CreateDeltaPackage', ((1, 'updatedPackageStream'),(1, 'baselinePackageStream'),(1, 'deltaPackageStream'),)))
    IAppxPackageEditor.CreateDeltaPackageUsingBaselineBlockMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(5, 'CreateDeltaPackageUsingBaselineBlockMap', ((1, 'updatedPackageStream'),(1, 'baselineBlockMapStream'),(1, 'baselinePackageFullName'),(1, 'deltaPackageStream'),)))
    IAppxPackageEditor.UpdatePackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION, use_last_error=False)(6, 'UpdatePackage', ((1, 'baselinePackageStream'),(1, 'deltaPackageStream'),(1, 'updateOption'),)))
    IAppxPackageEditor.UpdateEncryptedPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION,POINTER(win32more.Storage.Packaging.Appx.APPX_ENCRYPTED_PACKAGE_SETTINGS2_head),POINTER(win32more.Storage.Packaging.Appx.APPX_KEY_INFO_head), use_last_error=False)(7, 'UpdateEncryptedPackage', ((1, 'baselineEncryptedPackageStream'),(1, 'deltaPackageStream'),(1, 'updateOption'),(1, 'settings'),(1, 'keyInfo'),)))
    IAppxPackageEditor.UpdatePackageManifest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.Foundation.BOOL,win32more.Storage.Packaging.Appx.APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS, use_last_error=False)(8, 'UpdatePackageManifest', ((1, 'packageStream'),(1, 'updatedManifestStream'),(1, 'isPackageEncrypted'),(1, 'options'),)))
    return IAppxPackageEditor
def _define_PACKAGE_VERSION_head():
    class PACKAGE_VERSION(Structure):
        pass
    return PACKAGE_VERSION
def _define_PACKAGE_VERSION():
    PACKAGE_VERSION = win32more.Storage.Packaging.Appx.PACKAGE_VERSION_head
    class PACKAGE_VERSION__Anonymous_e__Union(Union):
        pass
    class PACKAGE_VERSION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PACKAGE_VERSION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("Revision", UInt16),
        ("Build", UInt16),
        ("Minor", UInt16),
        ("Major", UInt16),
    ]
    PACKAGE_VERSION__Anonymous_e__Union._pack_ = 4
    PACKAGE_VERSION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PACKAGE_VERSION__Anonymous_e__Union._fields_ = [
        ("Version", UInt64),
        ("Anonymous", PACKAGE_VERSION__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    PACKAGE_VERSION._anonymous_ = [
        'Anonymous',
    ]
    PACKAGE_VERSION._fields_ = [
        ("Anonymous", PACKAGE_VERSION__Anonymous_e__Union),
    ]
    return PACKAGE_VERSION
def _define_PACKAGE_ID_head():
    class PACKAGE_ID(Structure):
        pass
    return PACKAGE_ID
def _define_PACKAGE_ID():
    PACKAGE_ID = win32more.Storage.Packaging.Appx.PACKAGE_ID_head
    PACKAGE_ID._pack_ = 4
    PACKAGE_ID._fields_ = [
        ("reserved", UInt32),
        ("processorArchitecture", UInt32),
        ("version", win32more.Storage.Packaging.Appx.PACKAGE_VERSION),
        ("name", win32more.Foundation.PWSTR),
        ("publisher", win32more.Foundation.PWSTR),
        ("resourceId", win32more.Foundation.PWSTR),
        ("publisherId", win32more.Foundation.PWSTR),
    ]
    return PACKAGE_ID
PackagePathType = Int32
PackagePathType_Install = 0
PackagePathType_Mutable = 1
PackagePathType_Effective = 2
PackagePathType_MachineExternal = 3
PackagePathType_UserExternal = 4
PackagePathType_EffectiveExternal = 5
PackageOrigin = Int32
PackageOrigin_Unknown = 0
PackageOrigin_Unsigned = 1
PackageOrigin_Inbox = 2
PackageOrigin_Store = 3
PackageOrigin_DeveloperUnsigned = 4
PackageOrigin_DeveloperSigned = 5
PackageOrigin_LineOfBusiness = 6
def _define__PACKAGE_INFO_REFERENCE_head():
    class _PACKAGE_INFO_REFERENCE(Structure):
        pass
    return _PACKAGE_INFO_REFERENCE
def _define__PACKAGE_INFO_REFERENCE():
    _PACKAGE_INFO_REFERENCE = win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head
    _PACKAGE_INFO_REFERENCE._fields_ = [
        ("reserved", c_void_p),
    ]
    return _PACKAGE_INFO_REFERENCE
def _define_PACKAGE_INFO_head():
    class PACKAGE_INFO(Structure):
        pass
    return PACKAGE_INFO
def _define_PACKAGE_INFO():
    PACKAGE_INFO = win32more.Storage.Packaging.Appx.PACKAGE_INFO_head
    PACKAGE_INFO._pack_ = 4
    PACKAGE_INFO._fields_ = [
        ("reserved", UInt32),
        ("flags", UInt32),
        ("path", win32more.Foundation.PWSTR),
        ("packageFullName", win32more.Foundation.PWSTR),
        ("packageFamilyName", win32more.Foundation.PWSTR),
        ("packageId", win32more.Storage.Packaging.Appx.PACKAGE_ID),
    ]
    return PACKAGE_INFO
CreatePackageDependencyOptions = Int32
CreatePackageDependencyOptions_None = 0
CreatePackageDependencyOptions_DoNotVerifyDependencyResolution = 1
CreatePackageDependencyOptions_ScopeIsSystem = 2
PackageDependencyLifetimeKind = Int32
PackageDependencyLifetimeKind_Process = 0
PackageDependencyLifetimeKind_FilePath = 1
PackageDependencyLifetimeKind_RegistryKey = 2
AddPackageDependencyOptions = Int32
AddPackageDependencyOptions_None = 0
AddPackageDependencyOptions_PrependIfRankCollision = 1
PackageDependencyProcessorArchitectures = Int32
PackageDependencyProcessorArchitectures_None = 0
PackageDependencyProcessorArchitectures_Neutral = 1
PackageDependencyProcessorArchitectures_X86 = 2
PackageDependencyProcessorArchitectures_X64 = 4
PackageDependencyProcessorArchitectures_Arm = 8
PackageDependencyProcessorArchitectures_Arm64 = 16
PackageDependencyProcessorArchitectures_X86A64 = 32
def _define_PACKAGEDEPENDENCY_CONTEXT___head():
    class PACKAGEDEPENDENCY_CONTEXT__(Structure):
        pass
    return PACKAGEDEPENDENCY_CONTEXT__
def _define_PACKAGEDEPENDENCY_CONTEXT__():
    PACKAGEDEPENDENCY_CONTEXT__ = win32more.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head
    PACKAGEDEPENDENCY_CONTEXT__._fields_ = [
        ("unused", Int32),
    ]
    return PACKAGEDEPENDENCY_CONTEXT__
AppPolicyLifecycleManagement = Int32
AppPolicyLifecycleManagement_Unmanaged = 0
AppPolicyLifecycleManagement_Managed = 1
AppPolicyWindowingModel = Int32
AppPolicyWindowingModel_None = 0
AppPolicyWindowingModel_Universal = 1
AppPolicyWindowingModel_ClassicDesktop = 2
AppPolicyWindowingModel_ClassicPhone = 3
AppPolicyMediaFoundationCodecLoading = Int32
AppPolicyMediaFoundationCodecLoading_All = 0
AppPolicyMediaFoundationCodecLoading_InboxOnly = 1
AppPolicyClrCompat = Int32
AppPolicyClrCompat_Other = 0
AppPolicyClrCompat_ClassicDesktop = 1
AppPolicyClrCompat_Universal = 2
AppPolicyClrCompat_PackagedDesktop = 3
AppPolicyThreadInitializationType = Int32
AppPolicyThreadInitializationType_None = 0
AppPolicyThreadInitializationType_InitializeWinRT = 1
AppPolicyShowDeveloperDiagnostic = Int32
AppPolicyShowDeveloperDiagnostic_None = 0
AppPolicyShowDeveloperDiagnostic_ShowUI = 1
AppPolicyProcessTerminationMethod = Int32
AppPolicyProcessTerminationMethod_ExitProcess = 0
AppPolicyProcessTerminationMethod_TerminateProcess = 1
AppPolicyCreateFileAccess = Int32
AppPolicyCreateFileAccess_Full = 0
AppPolicyCreateFileAccess_Limited = 1
def _define_PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head():
    class PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__(Structure):
        pass
    return PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__
def _define_PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__():
    PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__ = win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head
    PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__._fields_ = [
        ("unused", Int32),
    ]
    return PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__
def _define_GetCurrentPackageId():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),c_char_p_no, use_last_error=False)(("GetCurrentPackageId", windll["KERNEL32"]), ((1, 'bufferLength'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackageFullName():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetCurrentPackageFullName", windll["KERNEL32"]), ((1, 'packageFullNameLength'),(1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackageFamilyName():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetCurrentPackageFamilyName", windll["KERNEL32"]), ((1, 'packageFamilyNameLength'),(1, 'packageFamilyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackagePath():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetCurrentPackagePath", windll["KERNEL32"]), ((1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageId():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),c_char_p_no, use_last_error=False)(("GetPackageId", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'bufferLength'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackageFullName", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'packageFullNameLength'),(1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageFullNameFromToken():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackageFullNameFromToken", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'token'),(1, 'packageFullNameLength'),(1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageFamilyName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackageFamilyName", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'packageFamilyNameLength'),(1, 'packageFamilyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageFamilyNameFromToken():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackageFamilyNameFromToken", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'token'),(1, 'packageFamilyNameLength'),(1, 'packageFamilyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackagePath():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_ID_head),UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackagePath", windll["KERNEL32"]), ((1, 'packageId'),(1, 'reserved'),(1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackagePathByFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackagePathByFullName", windll["KERNEL32"]), ((1, 'packageFullName'),(1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStagedPackagePathByFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetStagedPackagePathByFullName", windll["KERNEL32"]), ((1, 'packageFullName'),(1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackagePathByFullName2():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Appx.PackagePathType,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackagePathByFullName2", windll["api-ms-win-appmodel-runtime-l1-1-3"]), ((1, 'packageFullName'),(1, 'packagePathType'),(1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStagedPackagePathByFullName2():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Appx.PackagePathType,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetStagedPackagePathByFullName2", windll["api-ms-win-appmodel-runtime-l1-1-3"]), ((1, 'packageFullName'),(1, 'packagePathType'),(1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackageInfo2():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.Storage.Packaging.Appx.PackagePathType,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetCurrentPackageInfo2", windll["api-ms-win-appmodel-runtime-l1-1-3"]), ((1, 'flags'),(1, 'packagePathType'),(1, 'bufferLength'),(1, 'buffer'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackagePath2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Packaging.Appx.PackagePathType,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetCurrentPackagePath2", windll["api-ms-win-appmodel-runtime-l1-1-3"]), ((1, 'packagePathType'),(1, 'pathLength'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentApplicationUserModelId():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetCurrentApplicationUserModelId", windll["KERNEL32"]), ((1, 'applicationUserModelIdLength'),(1, 'applicationUserModelId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetApplicationUserModelId():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetApplicationUserModelId", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'applicationUserModelIdLength'),(1, 'applicationUserModelId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetApplicationUserModelIdFromToken():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetApplicationUserModelIdFromToken", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'token'),(1, 'applicationUserModelIdLength'),(1, 'applicationUserModelId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyPackageFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("VerifyPackageFullName", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyPackageFamilyName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("VerifyPackageFamilyName", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'packageFamilyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyPackageId():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_ID_head), use_last_error=False)(("VerifyPackageId", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'packageId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyApplicationUserModelId():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("VerifyApplicationUserModelId", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'applicationUserModelId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerifyPackageRelativeApplicationId():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("VerifyPackageRelativeApplicationId", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'packageRelativeApplicationId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackageIdFromFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),c_char_p_no, use_last_error=False)(("PackageIdFromFullName", windll["KERNEL32"]), ((1, 'packageFullName'),(1, 'flags'),(1, 'bufferLength'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackageFullNameFromId():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_ID_head),POINTER(UInt32),POINTER(Char), use_last_error=False)(("PackageFullNameFromId", windll["KERNEL32"]), ((1, 'packageId'),(1, 'packageFullNameLength'),(1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackageFamilyNameFromId():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_ID_head),POINTER(UInt32),POINTER(Char), use_last_error=False)(("PackageFamilyNameFromId", windll["KERNEL32"]), ((1, 'packageId'),(1, 'packageFamilyNameLength'),(1, 'packageFamilyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackageFamilyNameFromFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("PackageFamilyNameFromFullName", windll["KERNEL32"]), ((1, 'packageFullName'),(1, 'packageFamilyNameLength'),(1, 'packageFamilyName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackageNameAndPublisherIdFromFamilyName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("PackageNameAndPublisherIdFromFamilyName", windll["KERNEL32"]), ((1, 'packageFamilyName'),(1, 'packageNameLength'),(1, 'packageName'),(1, 'packagePublisherIdLength'),(1, 'packagePublisherId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FormatApplicationUserModelId():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char), use_last_error=False)(("FormatApplicationUserModelId", windll["KERNEL32"]), ((1, 'packageFamilyName'),(1, 'packageRelativeApplicationId'),(1, 'applicationUserModelIdLength'),(1, 'applicationUserModelId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ParseApplicationUserModelId():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(Char), use_last_error=False)(("ParseApplicationUserModelId", windll["KERNEL32"]), ((1, 'applicationUserModelId'),(1, 'packageFamilyNameLength'),(1, 'packageFamilyName'),(1, 'packageRelativeApplicationIdLength'),(1, 'packageRelativeApplicationId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackagesByPackageFamily():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetPackagesByPackageFamily", windll["KERNEL32"]), ((1, 'packageFamilyName'),(1, 'count'),(1, 'packageFullNames'),(1, 'bufferLength'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindPackagesByPackageFamily():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(Char),POINTER(UInt32), use_last_error=False)(("FindPackagesByPackageFamily", windll["KERNEL32"]), ((1, 'packageFamilyName'),(1, 'packageFilters'),(1, 'count'),(1, 'packageFullNames'),(1, 'bufferLength'),(1, 'buffer'),(1, 'packageProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStagedPackageOrigin():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Appx.PackageOrigin), use_last_error=False)(("GetStagedPackageOrigin", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'packageFullName'),(1, 'origin'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackageInfo():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetCurrentPackageInfo", windll["KERNEL32"]), ((1, 'flags'),(1, 'bufferLength'),(1, 'buffer'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenPackageInfoByFullName():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head)), use_last_error=False)(("OpenPackageInfoByFullName", windll["KERNEL32"]), ((1, 'packageFullName'),(1, 'reserved'),(1, 'packageInfoReference'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenPackageInfoByFullNameForUser():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSID,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head)), use_last_error=False)(("OpenPackageInfoByFullNameForUser", windll["api-ms-win-appmodel-runtime-l1-1-1"]), ((1, 'userSid'),(1, 'packageFullName'),(1, 'reserved'),(1, 'packageInfoReference'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClosePackageInfo():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head), use_last_error=False)(("ClosePackageInfo", windll["KERNEL32"]), ((1, 'packageInfoReference'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageInfo():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head),UInt32,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetPackageInfo", windll["KERNEL32"]), ((1, 'packageInfoReference'),(1, 'flags'),(1, 'bufferLength'),(1, 'buffer'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageApplicationIds():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head),POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetPackageApplicationIds", windll["KERNEL32"]), ((1, 'packageInfoReference'),(1, 'bufferLength'),(1, 'buffer'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPackageInfo2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Packaging.Appx._PACKAGE_INFO_REFERENCE_head),UInt32,win32more.Storage.Packaging.Appx.PackagePathType,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetPackageInfo2", windll["api-ms-win-appmodel-runtime-l1-1-3"]), ((1, 'packageInfoReference'),(1, 'flags'),(1, 'packagePathType'),(1, 'bufferLength'),(1, 'buffer'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckIsMSIXPackage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("CheckIsMSIXPackage", windll["KERNEL32"]), ((1, 'packageFullName'),(1, 'isMSIXPackage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TryCreatePackageDependency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Appx.PACKAGE_VERSION,win32more.Storage.Packaging.Appx.PackageDependencyProcessorArchitectures,win32more.Storage.Packaging.Appx.PackageDependencyLifetimeKind,win32more.Foundation.PWSTR,win32more.Storage.Packaging.Appx.CreatePackageDependencyOptions,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("TryCreatePackageDependency", windll["KERNEL32"]), ((1, 'user'),(1, 'packageFamilyName'),(1, 'minVersion'),(1, 'packageDependencyProcessorArchitectures'),(1, 'lifetimeKind'),(1, 'lifetimeArtifact'),(1, 'options'),(1, 'packageDependencyId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeletePackageDependency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("DeletePackageDependency", windll["KERNEL32"]), ((1, 'packageDependencyId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddPackageDependency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,win32more.Storage.Packaging.Appx.AddPackageDependencyOptions,POINTER(POINTER(win32more.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head)),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("AddPackageDependency", windll["KERNEL32"]), ((1, 'packageDependencyId'),(1, 'rank'),(1, 'options'),(1, 'packageDependencyContext'),(1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemovePackageDependency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head), use_last_error=False)(("RemovePackageDependency", windll["KERNEL32"]), ((1, 'packageDependencyContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetResolvedPackageFullNameForPackageDependency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("GetResolvedPackageFullNameForPackageDependency", windll["KERNEL32"]), ((1, 'packageDependencyId'),(1, 'packageFullName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIdForPackageDependencyContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.PACKAGEDEPENDENCY_CONTEXT___head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("GetIdForPackageDependencyContext", windll["KERNEL32"]), ((1, 'packageDependencyContext'),(1, 'packageDependencyId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetLifecycleManagement():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyLifecycleManagement), use_last_error=False)(("AppPolicyGetLifecycleManagement", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetWindowingModel():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyWindowingModel), use_last_error=False)(("AppPolicyGetWindowingModel", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetMediaFoundationCodecLoading():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyMediaFoundationCodecLoading), use_last_error=False)(("AppPolicyGetMediaFoundationCodecLoading", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetClrCompat():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyClrCompat), use_last_error=False)(("AppPolicyGetClrCompat", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetThreadInitializationType():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyThreadInitializationType), use_last_error=False)(("AppPolicyGetThreadInitializationType", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetShowDeveloperDiagnostic():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyShowDeveloperDiagnostic), use_last_error=False)(("AppPolicyGetShowDeveloperDiagnostic", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetProcessTerminationMethod():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyProcessTerminationMethod), use_last_error=False)(("AppPolicyGetProcessTerminationMethod", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AppPolicyGetCreateFileAccess():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Packaging.Appx.AppPolicyCreateFileAccess), use_last_error=False)(("AppPolicyGetCreateFileAccess", windll["KERNEL32"]), ((1, 'processToken'),(1, 'policy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePackageVirtualizationContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head)), use_last_error=False)(("CreatePackageVirtualizationContext", windll["KERNEL32"]), ((1, 'packageFamilyName'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ActivatePackageVirtualizationContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head),POINTER(UIntPtr), use_last_error=False)(("ActivatePackageVirtualizationContext", windll["KERNEL32"]), ((1, 'context'),(1, 'cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleasePackageVirtualizationContext():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head), use_last_error=False)(("ReleasePackageVirtualizationContext", windll["KERNEL32"]), ((1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeactivatePackageVirtualizationContext():
    try:
        return WINFUNCTYPE(Void,UIntPtr, use_last_error=False)(("DeactivatePackageVirtualizationContext", windll["KERNEL32"]), ((1, 'cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DuplicatePackageVirtualizationContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head),POINTER(POINTER(win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head)), use_last_error=False)(("DuplicatePackageVirtualizationContext", windll["KERNEL32"]), ((1, 'sourceContext'),(1, 'destContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPackageVirtualizationContext():
    try:
        return WINFUNCTYPE(POINTER(win32more.Storage.Packaging.Appx.PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE___head), use_last_error=False)(("GetCurrentPackageVirtualizationContext", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessesInVirtualizationContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(win32more.Foundation.HANDLE)), use_last_error=False)(("GetProcessesInVirtualizationContext", windll["KERNEL32"]), ((1, 'packageFamilyName'),(1, 'count'),(1, 'processes'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PACKAGE_PROPERTY_FRAMEWORK",
    "PACKAGE_PROPERTY_RESOURCE",
    "PACKAGE_PROPERTY_BUNDLE",
    "PACKAGE_PROPERTY_OPTIONAL",
    "PACKAGE_FILTER_HEAD",
    "PACKAGE_FILTER_DIRECT",
    "PACKAGE_FILTER_RESOURCE",
    "PACKAGE_FILTER_BUNDLE",
    "PACKAGE_INFORMATION_BASIC",
    "PACKAGE_INFORMATION_FULL",
    "PACKAGE_PROPERTY_DEVELOPMENT_MODE",
    "PACKAGE_FILTER_OPTIONAL",
    "PACKAGE_PROPERTY_IS_IN_RELATED_SET",
    "PACKAGE_FILTER_IS_IN_RELATED_SET",
    "PACKAGE_PROPERTY_STATIC",
    "PACKAGE_FILTER_STATIC",
    "PACKAGE_PROPERTY_DYNAMIC",
    "PACKAGE_FILTER_DYNAMIC",
    "PACKAGE_PROPERTY_HOSTRUNTIME",
    "PACKAGE_FILTER_HOSTRUNTIME",
    "PACKAGE_FILTER_ALL_LOADED",
    "PACKAGE_DEPENDENCY_RANK_DEFAULT",
    "AppxFactory",
    "AppxBundleFactory",
    "AppxPackagingDiagnosticEventSinkManager",
    "AppxEncryptionFactory",
    "AppxPackageEditor",
    "APPX_PACKAGE_SETTINGS",
    "APPX_COMPRESSION_OPTION",
    "APPX_COMPRESSION_OPTION_NONE",
    "APPX_COMPRESSION_OPTION_NORMAL",
    "APPX_COMPRESSION_OPTION_MAXIMUM",
    "APPX_COMPRESSION_OPTION_FAST",
    "APPX_COMPRESSION_OPTION_SUPERFAST",
    "APPX_PACKAGE_WRITER_PAYLOAD_STREAM",
    "APPX_FOOTPRINT_FILE_TYPE",
    "APPX_FOOTPRINT_FILE_TYPE_MANIFEST",
    "APPX_FOOTPRINT_FILE_TYPE_BLOCKMAP",
    "APPX_FOOTPRINT_FILE_TYPE_SIGNATURE",
    "APPX_FOOTPRINT_FILE_TYPE_CODEINTEGRITY",
    "APPX_FOOTPRINT_FILE_TYPE_CONTENTGROUPMAP",
    "APPX_BUNDLE_FOOTPRINT_FILE_TYPE",
    "APPX_BUNDLE_FOOTPRINT_FILE_TYPE_FIRST",
    "APPX_BUNDLE_FOOTPRINT_FILE_TYPE_MANIFEST",
    "APPX_BUNDLE_FOOTPRINT_FILE_TYPE_BLOCKMAP",
    "APPX_BUNDLE_FOOTPRINT_FILE_TYPE_SIGNATURE",
    "APPX_BUNDLE_FOOTPRINT_FILE_TYPE_LAST",
    "APPX_CAPABILITIES",
    "APPX_CAPABILITY_INTERNET_CLIENT",
    "APPX_CAPABILITY_INTERNET_CLIENT_SERVER",
    "APPX_CAPABILITY_PRIVATE_NETWORK_CLIENT_SERVER",
    "APPX_CAPABILITY_DOCUMENTS_LIBRARY",
    "APPX_CAPABILITY_PICTURES_LIBRARY",
    "APPX_CAPABILITY_VIDEOS_LIBRARY",
    "APPX_CAPABILITY_MUSIC_LIBRARY",
    "APPX_CAPABILITY_ENTERPRISE_AUTHENTICATION",
    "APPX_CAPABILITY_SHARED_USER_CERTIFICATES",
    "APPX_CAPABILITY_REMOVABLE_STORAGE",
    "APPX_CAPABILITY_APPOINTMENTS",
    "APPX_CAPABILITY_CONTACTS",
    "APPX_PACKAGE_ARCHITECTURE",
    "APPX_PACKAGE_ARCHITECTURE_X86",
    "APPX_PACKAGE_ARCHITECTURE_ARM",
    "APPX_PACKAGE_ARCHITECTURE_X64",
    "APPX_PACKAGE_ARCHITECTURE_NEUTRAL",
    "APPX_PACKAGE_ARCHITECTURE_ARM64",
    "APPX_PACKAGE_ARCHITECTURE2",
    "APPX_PACKAGE_ARCHITECTURE2_X86",
    "APPX_PACKAGE_ARCHITECTURE2_ARM",
    "APPX_PACKAGE_ARCHITECTURE2_X64",
    "APPX_PACKAGE_ARCHITECTURE2_NEUTRAL",
    "APPX_PACKAGE_ARCHITECTURE2_ARM64",
    "APPX_PACKAGE_ARCHITECTURE2_X86_ON_ARM64",
    "APPX_PACKAGE_ARCHITECTURE2_UNKNOWN",
    "APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE",
    "APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_APPLICATION",
    "APPX_BUNDLE_PAYLOAD_PACKAGE_TYPE_RESOURCE",
    "DX_FEATURE_LEVEL",
    "DX_FEATURE_LEVEL_UNSPECIFIED",
    "DX_FEATURE_LEVEL_9",
    "DX_FEATURE_LEVEL_10",
    "DX_FEATURE_LEVEL_11",
    "APPX_CAPABILITY_CLASS_TYPE",
    "APPX_CAPABILITY_CLASS_DEFAULT",
    "APPX_CAPABILITY_CLASS_GENERAL",
    "APPX_CAPABILITY_CLASS_RESTRICTED",
    "APPX_CAPABILITY_CLASS_WINDOWS",
    "APPX_CAPABILITY_CLASS_ALL",
    "APPX_CAPABILITY_CLASS_CUSTOM",
    "APPX_PACKAGING_CONTEXT_CHANGE_TYPE",
    "APPX_PACKAGING_CONTEXT_CHANGE_TYPE_START",
    "APPX_PACKAGING_CONTEXT_CHANGE_TYPE_CHANGE",
    "APPX_PACKAGING_CONTEXT_CHANGE_TYPE_DETAILS",
    "APPX_PACKAGING_CONTEXT_CHANGE_TYPE_END",
    "IAppxFactory",
    "IAppxFactory2",
    "IAppxPackageReader",
    "IAppxPackageWriter",
    "IAppxPackageWriter2",
    "IAppxPackageWriter3",
    "IAppxFile",
    "IAppxFilesEnumerator",
    "IAppxBlockMapReader",
    "IAppxBlockMapFile",
    "IAppxBlockMapFilesEnumerator",
    "IAppxBlockMapBlock",
    "IAppxBlockMapBlocksEnumerator",
    "IAppxManifestReader",
    "IAppxManifestReader2",
    "IAppxManifestReader3",
    "IAppxManifestReader4",
    "IAppxManifestReader5",
    "IAppxManifestReader6",
    "IAppxManifestReader7",
    "IAppxManifestDriverDependenciesEnumerator",
    "IAppxManifestDriverDependency",
    "IAppxManifestDriverConstraintsEnumerator",
    "IAppxManifestDriverConstraint",
    "IAppxManifestOSPackageDependenciesEnumerator",
    "IAppxManifestOSPackageDependency",
    "IAppxManifestHostRuntimeDependenciesEnumerator",
    "IAppxManifestHostRuntimeDependency",
    "IAppxManifestHostRuntimeDependency2",
    "IAppxManifestOptionalPackageInfo",
    "IAppxManifestMainPackageDependenciesEnumerator",
    "IAppxManifestMainPackageDependency",
    "IAppxManifestPackageId",
    "IAppxManifestPackageId2",
    "IAppxManifestProperties",
    "IAppxManifestTargetDeviceFamiliesEnumerator",
    "IAppxManifestTargetDeviceFamily",
    "IAppxManifestPackageDependenciesEnumerator",
    "IAppxManifestPackageDependency",
    "IAppxManifestPackageDependency2",
    "IAppxManifestPackageDependency3",
    "IAppxManifestResourcesEnumerator",
    "IAppxManifestDeviceCapabilitiesEnumerator",
    "IAppxManifestCapabilitiesEnumerator",
    "IAppxManifestApplicationsEnumerator",
    "IAppxManifestApplication",
    "IAppxManifestQualifiedResourcesEnumerator",
    "IAppxManifestQualifiedResource",
    "IAppxBundleFactory",
    "IAppxBundleWriter",
    "IAppxBundleWriter2",
    "IAppxBundleWriter3",
    "IAppxBundleWriter4",
    "IAppxBundleReader",
    "IAppxBundleManifestReader",
    "IAppxBundleManifestReader2",
    "IAppxBundleManifestPackageInfoEnumerator",
    "IAppxBundleManifestPackageInfo",
    "IAppxBundleManifestPackageInfo2",
    "IAppxBundleManifestPackageInfo3",
    "IAppxBundleManifestPackageInfo4",
    "IAppxBundleManifestOptionalBundleInfoEnumerator",
    "IAppxBundleManifestOptionalBundleInfo",
    "IAppxContentGroupFilesEnumerator",
    "IAppxContentGroup",
    "IAppxContentGroupsEnumerator",
    "IAppxContentGroupMapReader",
    "IAppxSourceContentGroupMapReader",
    "IAppxContentGroupMapWriter",
    "IAppxPackagingDiagnosticEventSink",
    "IAppxPackagingDiagnosticEventSinkManager",
    "APPX_ENCRYPTED_PACKAGE_SETTINGS",
    "APPX_ENCRYPTED_PACKAGE_OPTIONS",
    "APPX_ENCRYPTED_PACKAGE_OPTION_NONE",
    "APPX_ENCRYPTED_PACKAGE_OPTION_DIFFUSION",
    "APPX_ENCRYPTED_PACKAGE_OPTION_PAGE_HASHING",
    "APPX_ENCRYPTED_PACKAGE_SETTINGS2",
    "APPX_KEY_INFO",
    "APPX_ENCRYPTED_EXEMPTIONS",
    "IAppxEncryptionFactory",
    "IAppxEncryptionFactory2",
    "IAppxEncryptionFactory3",
    "IAppxEncryptionFactory4",
    "IAppxEncryptedPackageWriter",
    "IAppxEncryptedPackageWriter2",
    "IAppxEncryptedBundleWriter",
    "IAppxEncryptedBundleWriter2",
    "APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION",
    "APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_OPTION_APPEND_DELTA",
    "APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTIONS",
    "APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_NONE",
    "APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_SKIP_VALIDATION",
    "APPX_PACKAGE_EDITOR_UPDATE_PACKAGE_MANIFEST_OPTION_LOCALIZED",
    "IAppxEncryptedBundleWriter3",
    "IAppxPackageEditor",
    "PACKAGE_VERSION",
    "PACKAGE_ID",
    "PackagePathType",
    "PackagePathType_Install",
    "PackagePathType_Mutable",
    "PackagePathType_Effective",
    "PackagePathType_MachineExternal",
    "PackagePathType_UserExternal",
    "PackagePathType_EffectiveExternal",
    "PackageOrigin",
    "PackageOrigin_Unknown",
    "PackageOrigin_Unsigned",
    "PackageOrigin_Inbox",
    "PackageOrigin_Store",
    "PackageOrigin_DeveloperUnsigned",
    "PackageOrigin_DeveloperSigned",
    "PackageOrigin_LineOfBusiness",
    "_PACKAGE_INFO_REFERENCE",
    "PACKAGE_INFO",
    "CreatePackageDependencyOptions",
    "CreatePackageDependencyOptions_None",
    "CreatePackageDependencyOptions_DoNotVerifyDependencyResolution",
    "CreatePackageDependencyOptions_ScopeIsSystem",
    "PackageDependencyLifetimeKind",
    "PackageDependencyLifetimeKind_Process",
    "PackageDependencyLifetimeKind_FilePath",
    "PackageDependencyLifetimeKind_RegistryKey",
    "AddPackageDependencyOptions",
    "AddPackageDependencyOptions_None",
    "AddPackageDependencyOptions_PrependIfRankCollision",
    "PackageDependencyProcessorArchitectures",
    "PackageDependencyProcessorArchitectures_None",
    "PackageDependencyProcessorArchitectures_Neutral",
    "PackageDependencyProcessorArchitectures_X86",
    "PackageDependencyProcessorArchitectures_X64",
    "PackageDependencyProcessorArchitectures_Arm",
    "PackageDependencyProcessorArchitectures_Arm64",
    "PackageDependencyProcessorArchitectures_X86A64",
    "PACKAGEDEPENDENCY_CONTEXT__",
    "AppPolicyLifecycleManagement",
    "AppPolicyLifecycleManagement_Unmanaged",
    "AppPolicyLifecycleManagement_Managed",
    "AppPolicyWindowingModel",
    "AppPolicyWindowingModel_None",
    "AppPolicyWindowingModel_Universal",
    "AppPolicyWindowingModel_ClassicDesktop",
    "AppPolicyWindowingModel_ClassicPhone",
    "AppPolicyMediaFoundationCodecLoading",
    "AppPolicyMediaFoundationCodecLoading_All",
    "AppPolicyMediaFoundationCodecLoading_InboxOnly",
    "AppPolicyClrCompat",
    "AppPolicyClrCompat_Other",
    "AppPolicyClrCompat_ClassicDesktop",
    "AppPolicyClrCompat_Universal",
    "AppPolicyClrCompat_PackagedDesktop",
    "AppPolicyThreadInitializationType",
    "AppPolicyThreadInitializationType_None",
    "AppPolicyThreadInitializationType_InitializeWinRT",
    "AppPolicyShowDeveloperDiagnostic",
    "AppPolicyShowDeveloperDiagnostic_None",
    "AppPolicyShowDeveloperDiagnostic_ShowUI",
    "AppPolicyProcessTerminationMethod",
    "AppPolicyProcessTerminationMethod_ExitProcess",
    "AppPolicyProcessTerminationMethod_TerminateProcess",
    "AppPolicyCreateFileAccess",
    "AppPolicyCreateFileAccess_Full",
    "AppPolicyCreateFileAccess_Limited",
    "PACKAGE_VIRTUALIZATION_CONTEXT_HANDLE__",
    "GetCurrentPackageId",
    "GetCurrentPackageFullName",
    "GetCurrentPackageFamilyName",
    "GetCurrentPackagePath",
    "GetPackageId",
    "GetPackageFullName",
    "GetPackageFullNameFromToken",
    "GetPackageFamilyName",
    "GetPackageFamilyNameFromToken",
    "GetPackagePath",
    "GetPackagePathByFullName",
    "GetStagedPackagePathByFullName",
    "GetPackagePathByFullName2",
    "GetStagedPackagePathByFullName2",
    "GetCurrentPackageInfo2",
    "GetCurrentPackagePath2",
    "GetCurrentApplicationUserModelId",
    "GetApplicationUserModelId",
    "GetApplicationUserModelIdFromToken",
    "VerifyPackageFullName",
    "VerifyPackageFamilyName",
    "VerifyPackageId",
    "VerifyApplicationUserModelId",
    "VerifyPackageRelativeApplicationId",
    "PackageIdFromFullName",
    "PackageFullNameFromId",
    "PackageFamilyNameFromId",
    "PackageFamilyNameFromFullName",
    "PackageNameAndPublisherIdFromFamilyName",
    "FormatApplicationUserModelId",
    "ParseApplicationUserModelId",
    "GetPackagesByPackageFamily",
    "FindPackagesByPackageFamily",
    "GetStagedPackageOrigin",
    "GetCurrentPackageInfo",
    "OpenPackageInfoByFullName",
    "OpenPackageInfoByFullNameForUser",
    "ClosePackageInfo",
    "GetPackageInfo",
    "GetPackageApplicationIds",
    "GetPackageInfo2",
    "CheckIsMSIXPackage",
    "TryCreatePackageDependency",
    "DeletePackageDependency",
    "AddPackageDependency",
    "RemovePackageDependency",
    "GetResolvedPackageFullNameForPackageDependency",
    "GetIdForPackageDependencyContext",
    "AppPolicyGetLifecycleManagement",
    "AppPolicyGetWindowingModel",
    "AppPolicyGetMediaFoundationCodecLoading",
    "AppPolicyGetClrCompat",
    "AppPolicyGetThreadInitializationType",
    "AppPolicyGetShowDeveloperDiagnostic",
    "AppPolicyGetProcessTerminationMethod",
    "AppPolicyGetCreateFileAccess",
    "CreatePackageVirtualizationContext",
    "ActivatePackageVirtualizationContext",
    "ReleasePackageVirtualizationContext",
    "DeactivatePackageVirtualizationContext",
    "DuplicatePackageVirtualizationContext",
    "GetCurrentPackageVirtualizationContext",
    "GetProcessesInVirtualizationContext",
]
