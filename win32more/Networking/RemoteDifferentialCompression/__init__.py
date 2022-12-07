from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.RemoteDifferentialCompression
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
RDCE_TABLE_FULL: UInt32 = 2147745793
RDCE_TABLE_CORRUPT: UInt32 = 2147745794
MSRDC_SIGNATURE_HASHSIZE: UInt32 = 16
SimilarityFileIdMinSize: UInt32 = 4
SimilarityFileIdMaxSize: UInt32 = 32
MSRDC_VERSION: UInt32 = 65536
MSRDC_MINIMUM_COMPATIBLE_APP_VERSION: UInt32 = 65536
MSRDC_MINIMUM_DEPTH: UInt32 = 1
MSRDC_MAXIMUM_DEPTH: UInt32 = 8
MSRDC_MINIMUM_COMPAREBUFFER: UInt32 = 100000
MSRDC_MAXIMUM_COMPAREBUFFER: UInt32 = 1073741824
MSRDC_DEFAULT_COMPAREBUFFER: UInt32 = 3200000
MSRDC_MINIMUM_INPUTBUFFERSIZE: UInt32 = 1024
MSRDC_MINIMUM_HORIZONSIZE: UInt32 = 128
MSRDC_MAXIMUM_HORIZONSIZE: UInt32 = 16384
MSRDC_MINIMUM_HASHWINDOWSIZE: UInt32 = 2
MSRDC_MAXIMUM_HASHWINDOWSIZE: UInt32 = 96
MSRDC_DEFAULT_HASHWINDOWSIZE_1: UInt32 = 48
MSRDC_DEFAULT_HORIZONSIZE_1: UInt32 = 1024
MSRDC_DEFAULT_HASHWINDOWSIZE_N: UInt32 = 2
MSRDC_DEFAULT_HORIZONSIZE_N: UInt32 = 128
MSRDC_MAXIMUM_TRAITVALUE: UInt32 = 63
MSRDC_MINIMUM_MATCHESREQUIRED: UInt32 = 1
MSRDC_MAXIMUM_MATCHESREQUIRED: UInt32 = 16
class FindSimilarFileIndexResults(Structure):
    m_FileIndex: UInt32
    m_MatchCount: UInt32
FindSimilarResults = Guid('96236a93-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
GeneratorParametersType = Int32
RDCGENTYPE_Unused: GeneratorParametersType = 0
RDCGENTYPE_FilterMax: GeneratorParametersType = 1
class IFindSimilarResults(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a81-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def GetSize(size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNextFileId(numTraitsMatched: POINTER(UInt32), similarityFileId: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head)) -> win32more.Foundation.HRESULT: ...
class IRdcComparator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a77-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def Process(endOfInput: win32more.Foundation.BOOL, endOfOutput: POINTER(win32more.Foundation.BOOL), inputBuffer: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head), outputBuffer: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcNeedPointer_head), rdc_ErrorCode: POINTER(win32more.Networking.RemoteDifferentialCompression.RDC_ErrorCode)) -> win32more.Foundation.HRESULT: ...
class IRdcFileReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a74-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def GetFileSize(fileSize: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Read(offsetFileStart: UInt64, bytesToRead: UInt32, bytesActuallyRead: POINTER(UInt32), buffer: c_char_p_no, eof: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilePosition(offsetFromStart: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class IRdcFileWriter(c_void_p):
    extends: win32more.Networking.RemoteDifferentialCompression.IRdcFileReader
    Guid = Guid('96236a75-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(6)
    def Write(offsetFileStart: UInt64, bytesToWrite: UInt32, buffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Truncate() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def DeleteOnClose() -> win32more.Foundation.HRESULT: ...
class IRdcGenerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a73-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def GetGeneratorParameters(level: UInt32, iGeneratorParameters: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Process(endOfInput: win32more.Foundation.BOOL, endOfOutput: POINTER(win32more.Foundation.BOOL), inputBuffer: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head), depth: UInt32, outputBuffers: POINTER(POINTER(win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head)), rdc_ErrorCode: POINTER(win32more.Networking.RemoteDifferentialCompression.RDC_ErrorCode)) -> win32more.Foundation.HRESULT: ...
class IRdcGeneratorFilterMaxParameters(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a72-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def GetHorizonSize(horizonSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetHorizonSize(horizonSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetHashWindowSize(hashWindowSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetHashWindowSize(hashWindowSize: UInt32) -> win32more.Foundation.HRESULT: ...
class IRdcGeneratorParameters(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a71-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def GetGeneratorParametersType(parametersType: POINTER(win32more.Networking.RemoteDifferentialCompression.GeneratorParametersType)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetParametersVersion(currentVersion: POINTER(UInt32), minimumCompatibleAppVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSerializeSize(size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(size: UInt32, parametersBlob: c_char_p_no, bytesWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IRdcLibrary(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a78-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def ComputeDefaultRecursionDepth(fileSize: UInt64, depth: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateGeneratorParameters(parametersType: win32more.Networking.RemoteDifferentialCompression.GeneratorParametersType, level: UInt32, iGeneratorParameters: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OpenGeneratorParameters(size: UInt32, parametersBlob: c_char_p_no, iGeneratorParameters: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateGenerator(depth: UInt32, iGeneratorParametersArray: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head), iGenerator: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGenerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateComparator(iSeedSignaturesFile: win32more.Networking.RemoteDifferentialCompression.IRdcFileReader_head, comparatorBufferSize: UInt32, iComparator: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcComparator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateSignatureReader(iFileReader: win32more.Networking.RemoteDifferentialCompression.IRdcFileReader_head, iSignatureReader: POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcSignatureReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRDCVersion(currentVersion: POINTER(UInt32), minimumCompatibleAppVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IRdcSignatureReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a76-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def ReadHeader(rdc_ErrorCode: POINTER(win32more.Networking.RemoteDifferentialCompression.RDC_ErrorCode)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReadSignatures(rdcSignaturePointer: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcSignaturePointer_head), endOfOutput: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IRdcSimilarityGenerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a80-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def EnableSimilarity() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Results(similarityData: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head)) -> win32more.Foundation.HRESULT: ...
class ISimilarity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a83-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def CreateTable(path: win32more.Foundation.PWSTR, truncate: win32more.Foundation.BOOL, securityDescriptor: c_char_p_no, recordSize: UInt32, isNew: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTableIndirect(mapping: win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head, fileIdFile: win32more.Networking.RemoteDifferentialCompression.IRdcFileWriter_head, truncate: win32more.Foundation.BOOL, recordSize: UInt32, isNew: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CloseTable(isValid: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Append(similarityFileId: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head), similarityData: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FindSimilarFileId(similarityData: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head), numberOfMatchesRequired: UInt16, resultsSize: UInt32, findSimilarResults: POINTER(win32more.Networking.RemoteDifferentialCompression.IFindSimilarResults_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CopyAndSwap(newSimilarityTables: win32more.Networking.RemoteDifferentialCompression.ISimilarity_head, reportProgress: win32more.Networking.RemoteDifferentialCompression.ISimilarityReportProgress_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordCount(recordCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISimilarityFileIdTable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a7f-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def CreateTable(path: win32more.Foundation.PWSTR, truncate: win32more.Foundation.BOOL, securityDescriptor: c_char_p_no, recordSize: UInt32, isNew: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTableIndirect(fileIdFile: win32more.Networking.RemoteDifferentialCompression.IRdcFileWriter_head, truncate: win32more.Foundation.BOOL, recordSize: UInt32, isNew: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CloseTable(isValid: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Append(similarityFileId: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head), similarityFileIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Lookup(similarityFileIndex: UInt32, similarityFileId: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Invalidate(similarityFileIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordCount(recordCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISimilarityReportProgress(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a7a-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def ReportProgress(percentCompleted: UInt32) -> win32more.Foundation.HRESULT: ...
class ISimilarityTableDumpState(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a7b-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def GetNextData(resultsSize: UInt32, resultsUsed: POINTER(UInt32), eof: POINTER(win32more.Foundation.BOOL), results: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityDumpData_head)) -> win32more.Foundation.HRESULT: ...
class ISimilarityTraitsMappedView(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a7c-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def Flush() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unmap() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Get(index: UInt64, dirty: win32more.Foundation.BOOL, numElements: UInt32, viewInfo: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityMappedViewInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetView(mappedPageBegin: POINTER(c_char_p_no), mappedPageEnd: POINTER(c_char_p_no)) -> Void: ...
class ISimilarityTraitsMapping(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a7d-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def CloseMapping() -> Void: ...
    @commethod(4)
    def SetFileSize(fileSize: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(fileSize: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OpenMapping(accessMode: win32more.Networking.RemoteDifferentialCompression.RdcMappingAccessMode, begin: UInt64, end: UInt64, actualEnd: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ResizeMapping(accessMode: win32more.Networking.RemoteDifferentialCompression.RdcMappingAccessMode, begin: UInt64, end: UInt64, actualEnd: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPageSize(pageSize: POINTER(UInt32)) -> Void: ...
    @commethod(9)
    def CreateView(minimumMappedPages: UInt32, accessMode: win32more.Networking.RemoteDifferentialCompression.RdcMappingAccessMode, mappedView: POINTER(win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMappedView_head)) -> win32more.Foundation.HRESULT: ...
class ISimilarityTraitsTable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('96236a7e-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
    @commethod(3)
    def CreateTable(path: win32more.Foundation.PWSTR, truncate: win32more.Foundation.BOOL, securityDescriptor: c_char_p_no, isNew: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTableIndirect(mapping: win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head, truncate: win32more.Foundation.BOOL, isNew: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CloseTable(isValid: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Append(data: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head), fileIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FindSimilarFileIndex(similarityData: POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head), numberOfMatchesRequired: UInt16, findSimilarFileIndexResults: POINTER(win32more.Networking.RemoteDifferentialCompression.FindSimilarFileIndexResults_head), resultsSize: UInt32, resultsUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def BeginDump(similarityTableDumpState: POINTER(win32more.Networking.RemoteDifferentialCompression.ISimilarityTableDumpState_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastIndex(fileIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
RDC_ErrorCode = Int32
RDC_NoError: RDC_ErrorCode = 0
RDC_HeaderVersionNewer: RDC_ErrorCode = 1
RDC_HeaderVersionOlder: RDC_ErrorCode = 2
RDC_HeaderMissingOrCorrupt: RDC_ErrorCode = 3
RDC_HeaderWrongType: RDC_ErrorCode = 4
RDC_DataMissingOrCorrupt: RDC_ErrorCode = 5
RDC_DataTooManyRecords: RDC_ErrorCode = 6
RDC_FileChecksumMismatch: RDC_ErrorCode = 7
RDC_ApplicationError: RDC_ErrorCode = 8
RDC_Aborted: RDC_ErrorCode = 9
RDC_Win32Error: RDC_ErrorCode = 10
class RdcBufferPointer(Structure):
    m_Size: UInt32
    m_Used: UInt32
    m_Data: c_char_p_no
RdcComparator = Guid('96236a8b-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcCreatedTables = Int32
RDCTABLE_InvalidOrUnknown: RdcCreatedTables = 0
RDCTABLE_Existing: RdcCreatedTables = 1
RDCTABLE_New: RdcCreatedTables = 2
RdcFileReader = Guid('96236a89-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcGenerator = Guid('96236a88-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcGeneratorFilterMaxParameters = Guid('96236a87-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcGeneratorParameters = Guid('96236a86-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcLibrary = Guid('96236a85-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcMappingAccessMode = Int32
RDCMAPPING_Undefined: RdcMappingAccessMode = 0
RDCMAPPING_ReadOnly: RdcMappingAccessMode = 1
RDCMAPPING_ReadWrite: RdcMappingAccessMode = 2
class RdcNeed(Structure):
    m_BlockType: win32more.Networking.RemoteDifferentialCompression.RdcNeedType
    m_FileOffset: UInt64
    m_BlockLength: UInt64
class RdcNeedPointer(Structure):
    m_Size: UInt32
    m_Used: UInt32
    m_Data: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcNeed_head)
RdcNeedType = Int32
RDCNEED_SOURCE: RdcNeedType = 0
RDCNEED_TARGET: RdcNeedType = 1
RDCNEED_SEED: RdcNeedType = 2
RDCNEED_SEED_MAX: RdcNeedType = 255
class RdcSignature(Structure):
    m_Signature: Byte * 16
    m_BlockLength: UInt16
class RdcSignaturePointer(Structure):
    m_Size: UInt32
    m_Used: UInt32
    m_Data: POINTER(win32more.Networking.RemoteDifferentialCompression.RdcSignature_head)
RdcSignatureReader = Guid('96236a8a-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
RdcSimilarityGenerator = Guid('96236a92-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
Similarity = Guid('96236a91-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
class SimilarityData(Structure):
    m_Data: Byte * 16
class SimilarityDumpData(Structure):
    m_FileIndex: UInt32
    m_Data: win32more.Networking.RemoteDifferentialCompression.SimilarityData
class SimilarityFileId(Structure):
    m_FileId: Byte * 32
SimilarityFileIdTable = Guid('96236a90-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
class SimilarityMappedViewInfo(Structure):
    m_Data: c_char_p_no
    m_Length: UInt32
SimilarityReportProgress = Guid('96236a8d-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
SimilarityTableDumpState = Guid('96236a8e-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
SimilarityTraitsMappedView = Guid('96236a95-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
SimilarityTraitsMapping = Guid('96236a94-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
SimilarityTraitsTable = Guid('96236a8f-9dbc-11da-9e-3f-00-11-11-4a-e3-11')
make_head(_module, 'FindSimilarFileIndexResults')
make_head(_module, 'IFindSimilarResults')
make_head(_module, 'IRdcComparator')
make_head(_module, 'IRdcFileReader')
make_head(_module, 'IRdcFileWriter')
make_head(_module, 'IRdcGenerator')
make_head(_module, 'IRdcGeneratorFilterMaxParameters')
make_head(_module, 'IRdcGeneratorParameters')
make_head(_module, 'IRdcLibrary')
make_head(_module, 'IRdcSignatureReader')
make_head(_module, 'IRdcSimilarityGenerator')
make_head(_module, 'ISimilarity')
make_head(_module, 'ISimilarityFileIdTable')
make_head(_module, 'ISimilarityReportProgress')
make_head(_module, 'ISimilarityTableDumpState')
make_head(_module, 'ISimilarityTraitsMappedView')
make_head(_module, 'ISimilarityTraitsMapping')
make_head(_module, 'ISimilarityTraitsTable')
make_head(_module, 'RdcBufferPointer')
make_head(_module, 'RdcNeed')
make_head(_module, 'RdcNeedPointer')
make_head(_module, 'RdcSignature')
make_head(_module, 'RdcSignaturePointer')
make_head(_module, 'SimilarityData')
make_head(_module, 'SimilarityDumpData')
make_head(_module, 'SimilarityFileId')
make_head(_module, 'SimilarityMappedViewInfo')
__all__ = [
    "FindSimilarFileIndexResults",
    "FindSimilarResults",
    "GeneratorParametersType",
    "IFindSimilarResults",
    "IRdcComparator",
    "IRdcFileReader",
    "IRdcFileWriter",
    "IRdcGenerator",
    "IRdcGeneratorFilterMaxParameters",
    "IRdcGeneratorParameters",
    "IRdcLibrary",
    "IRdcSignatureReader",
    "IRdcSimilarityGenerator",
    "ISimilarity",
    "ISimilarityFileIdTable",
    "ISimilarityReportProgress",
    "ISimilarityTableDumpState",
    "ISimilarityTraitsMappedView",
    "ISimilarityTraitsMapping",
    "ISimilarityTraitsTable",
    "MSRDC_DEFAULT_COMPAREBUFFER",
    "MSRDC_DEFAULT_HASHWINDOWSIZE_1",
    "MSRDC_DEFAULT_HASHWINDOWSIZE_N",
    "MSRDC_DEFAULT_HORIZONSIZE_1",
    "MSRDC_DEFAULT_HORIZONSIZE_N",
    "MSRDC_MAXIMUM_COMPAREBUFFER",
    "MSRDC_MAXIMUM_DEPTH",
    "MSRDC_MAXIMUM_HASHWINDOWSIZE",
    "MSRDC_MAXIMUM_HORIZONSIZE",
    "MSRDC_MAXIMUM_MATCHESREQUIRED",
    "MSRDC_MAXIMUM_TRAITVALUE",
    "MSRDC_MINIMUM_COMPAREBUFFER",
    "MSRDC_MINIMUM_COMPATIBLE_APP_VERSION",
    "MSRDC_MINIMUM_DEPTH",
    "MSRDC_MINIMUM_HASHWINDOWSIZE",
    "MSRDC_MINIMUM_HORIZONSIZE",
    "MSRDC_MINIMUM_INPUTBUFFERSIZE",
    "MSRDC_MINIMUM_MATCHESREQUIRED",
    "MSRDC_SIGNATURE_HASHSIZE",
    "MSRDC_VERSION",
    "RDCE_TABLE_CORRUPT",
    "RDCE_TABLE_FULL",
    "RDCGENTYPE_FilterMax",
    "RDCGENTYPE_Unused",
    "RDCMAPPING_ReadOnly",
    "RDCMAPPING_ReadWrite",
    "RDCMAPPING_Undefined",
    "RDCNEED_SEED",
    "RDCNEED_SEED_MAX",
    "RDCNEED_SOURCE",
    "RDCNEED_TARGET",
    "RDCTABLE_Existing",
    "RDCTABLE_InvalidOrUnknown",
    "RDCTABLE_New",
    "RDC_Aborted",
    "RDC_ApplicationError",
    "RDC_DataMissingOrCorrupt",
    "RDC_DataTooManyRecords",
    "RDC_ErrorCode",
    "RDC_FileChecksumMismatch",
    "RDC_HeaderMissingOrCorrupt",
    "RDC_HeaderVersionNewer",
    "RDC_HeaderVersionOlder",
    "RDC_HeaderWrongType",
    "RDC_NoError",
    "RDC_Win32Error",
    "RdcBufferPointer",
    "RdcComparator",
    "RdcCreatedTables",
    "RdcFileReader",
    "RdcGenerator",
    "RdcGeneratorFilterMaxParameters",
    "RdcGeneratorParameters",
    "RdcLibrary",
    "RdcMappingAccessMode",
    "RdcNeed",
    "RdcNeedPointer",
    "RdcNeedType",
    "RdcSignature",
    "RdcSignaturePointer",
    "RdcSignatureReader",
    "RdcSimilarityGenerator",
    "Similarity",
    "SimilarityData",
    "SimilarityDumpData",
    "SimilarityFileId",
    "SimilarityFileIdMaxSize",
    "SimilarityFileIdMinSize",
    "SimilarityFileIdTable",
    "SimilarityMappedViewInfo",
    "SimilarityReportProgress",
    "SimilarityTableDumpState",
    "SimilarityTraitsMappedView",
    "SimilarityTraitsMapping",
    "SimilarityTraitsTable",
]
