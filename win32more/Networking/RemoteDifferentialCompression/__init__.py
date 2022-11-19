from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.RemoteDifferentialCompression
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
RDCE_TABLE_FULL = 2147745793
RDCE_TABLE_CORRUPT = 2147745794
MSRDC_SIGNATURE_HASHSIZE = 16
SimilarityFileIdMinSize = 4
SimilarityFileIdMaxSize = 32
MSRDC_VERSION = 65536
MSRDC_MINIMUM_COMPATIBLE_APP_VERSION = 65536
MSRDC_MINIMUM_DEPTH = 1
MSRDC_MAXIMUM_DEPTH = 8
MSRDC_MINIMUM_COMPAREBUFFER = 100000
MSRDC_MAXIMUM_COMPAREBUFFER = 1073741824
MSRDC_DEFAULT_COMPAREBUFFER = 3200000
MSRDC_MINIMUM_INPUTBUFFERSIZE = 1024
MSRDC_MINIMUM_HORIZONSIZE = 128
MSRDC_MAXIMUM_HORIZONSIZE = 16384
MSRDC_MINIMUM_HASHWINDOWSIZE = 2
MSRDC_MAXIMUM_HASHWINDOWSIZE = 96
MSRDC_DEFAULT_HASHWINDOWSIZE_1 = 48
MSRDC_DEFAULT_HORIZONSIZE_1 = 1024
MSRDC_DEFAULT_HASHWINDOWSIZE_N = 2
MSRDC_DEFAULT_HORIZONSIZE_N = 128
MSRDC_MAXIMUM_TRAITVALUE = 63
MSRDC_MINIMUM_MATCHESREQUIRED = 1
MSRDC_MAXIMUM_MATCHESREQUIRED = 16
RdcLibrary = Guid('96236a85-9dbc-11da-9e3f-0011114ae311')
RdcGeneratorParameters = Guid('96236a86-9dbc-11da-9e3f-0011114ae311')
RdcGeneratorFilterMaxParameters = Guid('96236a87-9dbc-11da-9e3f-0011114ae311')
RdcGenerator = Guid('96236a88-9dbc-11da-9e3f-0011114ae311')
RdcFileReader = Guid('96236a89-9dbc-11da-9e3f-0011114ae311')
RdcSignatureReader = Guid('96236a8a-9dbc-11da-9e3f-0011114ae311')
RdcComparator = Guid('96236a8b-9dbc-11da-9e3f-0011114ae311')
SimilarityReportProgress = Guid('96236a8d-9dbc-11da-9e3f-0011114ae311')
SimilarityTableDumpState = Guid('96236a8e-9dbc-11da-9e3f-0011114ae311')
SimilarityTraitsTable = Guid('96236a8f-9dbc-11da-9e3f-0011114ae311')
SimilarityFileIdTable = Guid('96236a90-9dbc-11da-9e3f-0011114ae311')
Similarity = Guid('96236a91-9dbc-11da-9e3f-0011114ae311')
RdcSimilarityGenerator = Guid('96236a92-9dbc-11da-9e3f-0011114ae311')
FindSimilarResults = Guid('96236a93-9dbc-11da-9e3f-0011114ae311')
SimilarityTraitsMapping = Guid('96236a94-9dbc-11da-9e3f-0011114ae311')
SimilarityTraitsMappedView = Guid('96236a95-9dbc-11da-9e3f-0011114ae311')
RDC_ErrorCode = Int32
RDC_NoError = 0
RDC_HeaderVersionNewer = 1
RDC_HeaderVersionOlder = 2
RDC_HeaderMissingOrCorrupt = 3
RDC_HeaderWrongType = 4
RDC_DataMissingOrCorrupt = 5
RDC_DataTooManyRecords = 6
RDC_FileChecksumMismatch = 7
RDC_ApplicationError = 8
RDC_Aborted = 9
RDC_Win32Error = 10
GeneratorParametersType = Int32
RDCGENTYPE_Unused = 0
RDCGENTYPE_FilterMax = 1
RdcNeedType = Int32
RDCNEED_SOURCE = 0
RDCNEED_TARGET = 1
RDCNEED_SEED = 2
RDCNEED_SEED_MAX = 255
def _define_RdcNeed_head():
    class RdcNeed(Structure):
        pass
    return RdcNeed
def _define_RdcNeed():
    RdcNeed = win32more.Networking.RemoteDifferentialCompression.RdcNeed_head
    RdcNeed._fields_ = [
        ("m_BlockType", win32more.Networking.RemoteDifferentialCompression.RdcNeedType),
        ("m_FileOffset", UInt64),
        ("m_BlockLength", UInt64),
    ]
    return RdcNeed
def _define_RdcBufferPointer_head():
    class RdcBufferPointer(Structure):
        pass
    return RdcBufferPointer
def _define_RdcBufferPointer():
    RdcBufferPointer = win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head
    RdcBufferPointer._fields_ = [
        ("m_Size", UInt32),
        ("m_Used", UInt32),
        ("m_Data", c_char_p_no),
    ]
    return RdcBufferPointer
def _define_RdcNeedPointer_head():
    class RdcNeedPointer(Structure):
        pass
    return RdcNeedPointer
def _define_RdcNeedPointer():
    RdcNeedPointer = win32more.Networking.RemoteDifferentialCompression.RdcNeedPointer_head
    RdcNeedPointer._fields_ = [
        ("m_Size", UInt32),
        ("m_Used", UInt32),
        ("m_Data", POINTER(win32more.Networking.RemoteDifferentialCompression.RdcNeed_head)),
    ]
    return RdcNeedPointer
def _define_RdcSignature_head():
    class RdcSignature(Structure):
        pass
    return RdcSignature
def _define_RdcSignature():
    RdcSignature = win32more.Networking.RemoteDifferentialCompression.RdcSignature_head
    RdcSignature._fields_ = [
        ("m_Signature", Byte * 16),
        ("m_BlockLength", UInt16),
    ]
    return RdcSignature
def _define_RdcSignaturePointer_head():
    class RdcSignaturePointer(Structure):
        pass
    return RdcSignaturePointer
def _define_RdcSignaturePointer():
    RdcSignaturePointer = win32more.Networking.RemoteDifferentialCompression.RdcSignaturePointer_head
    RdcSignaturePointer._fields_ = [
        ("m_Size", UInt32),
        ("m_Used", UInt32),
        ("m_Data", POINTER(win32more.Networking.RemoteDifferentialCompression.RdcSignature_head)),
    ]
    return RdcSignaturePointer
RdcCreatedTables = Int32
RDCTABLE_InvalidOrUnknown = 0
RDCTABLE_Existing = 1
RDCTABLE_New = 2
RdcMappingAccessMode = Int32
RDCMAPPING_Undefined = 0
RDCMAPPING_ReadOnly = 1
RDCMAPPING_ReadWrite = 2
def _define_SimilarityMappedViewInfo_head():
    class SimilarityMappedViewInfo(Structure):
        pass
    return SimilarityMappedViewInfo
def _define_SimilarityMappedViewInfo():
    SimilarityMappedViewInfo = win32more.Networking.RemoteDifferentialCompression.SimilarityMappedViewInfo_head
    SimilarityMappedViewInfo._fields_ = [
        ("m_Data", c_char_p_no),
        ("m_Length", UInt32),
    ]
    return SimilarityMappedViewInfo
def _define_SimilarityData_head():
    class SimilarityData(Structure):
        pass
    return SimilarityData
def _define_SimilarityData():
    SimilarityData = win32more.Networking.RemoteDifferentialCompression.SimilarityData_head
    SimilarityData._fields_ = [
        ("m_Data", Byte * 16),
    ]
    return SimilarityData
def _define_FindSimilarFileIndexResults_head():
    class FindSimilarFileIndexResults(Structure):
        pass
    return FindSimilarFileIndexResults
def _define_FindSimilarFileIndexResults():
    FindSimilarFileIndexResults = win32more.Networking.RemoteDifferentialCompression.FindSimilarFileIndexResults_head
    FindSimilarFileIndexResults._fields_ = [
        ("m_FileIndex", UInt32),
        ("m_MatchCount", UInt32),
    ]
    return FindSimilarFileIndexResults
def _define_SimilarityDumpData_head():
    class SimilarityDumpData(Structure):
        pass
    return SimilarityDumpData
def _define_SimilarityDumpData():
    SimilarityDumpData = win32more.Networking.RemoteDifferentialCompression.SimilarityDumpData_head
    SimilarityDumpData._fields_ = [
        ("m_FileIndex", UInt32),
        ("m_Data", win32more.Networking.RemoteDifferentialCompression.SimilarityData),
    ]
    return SimilarityDumpData
def _define_SimilarityFileId_head():
    class SimilarityFileId(Structure):
        pass
    return SimilarityFileId
def _define_SimilarityFileId():
    SimilarityFileId = win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head
    SimilarityFileId._fields_ = [
        ("m_FileId", Byte * 32),
    ]
    return SimilarityFileId
def _define_IRdcGeneratorParameters_head():
    class IRdcGeneratorParameters(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a71-9dbc-11da-9e3f-0011114ae311')
    return IRdcGeneratorParameters
def _define_IRdcGeneratorParameters():
    IRdcGeneratorParameters = win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head
    IRdcGeneratorParameters.GetGeneratorParametersType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.GeneratorParametersType), use_last_error=False)(3, 'GetGeneratorParametersType', ((1, 'parametersType'),)))
    IRdcGeneratorParameters.GetParametersVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetParametersVersion', ((1, 'currentVersion'),(1, 'minimumCompatibleAppVersion'),)))
    IRdcGeneratorParameters.GetSerializeSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetSerializeSize', ((1, 'size'),)))
    IRdcGeneratorParameters.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(6, 'Serialize', ((1, 'size'),(1, 'parametersBlob'),(1, 'bytesWritten'),)))
    win32more.System.Com.IUnknown
    return IRdcGeneratorParameters
def _define_IRdcGeneratorFilterMaxParameters_head():
    class IRdcGeneratorFilterMaxParameters(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a72-9dbc-11da-9e3f-0011114ae311')
    return IRdcGeneratorFilterMaxParameters
def _define_IRdcGeneratorFilterMaxParameters():
    IRdcGeneratorFilterMaxParameters = win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorFilterMaxParameters_head
    IRdcGeneratorFilterMaxParameters.GetHorizonSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetHorizonSize', ((1, 'horizonSize'),)))
    IRdcGeneratorFilterMaxParameters.SetHorizonSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetHorizonSize', ((1, 'horizonSize'),)))
    IRdcGeneratorFilterMaxParameters.GetHashWindowSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetHashWindowSize', ((1, 'hashWindowSize'),)))
    IRdcGeneratorFilterMaxParameters.SetHashWindowSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetHashWindowSize', ((1, 'hashWindowSize'),)))
    win32more.System.Com.IUnknown
    return IRdcGeneratorFilterMaxParameters
def _define_IRdcGenerator_head():
    class IRdcGenerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a73-9dbc-11da-9e3f-0011114ae311')
    return IRdcGenerator
def _define_IRdcGenerator():
    IRdcGenerator = win32more.Networking.RemoteDifferentialCompression.IRdcGenerator_head
    IRdcGenerator.GetGeneratorParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head), use_last_error=False)(3, 'GetGeneratorParameters', ((1, 'level'),(1, 'iGeneratorParameters'),)))
    IRdcGenerator.Process = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head),UInt32,POINTER(POINTER(win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head)),POINTER(win32more.Networking.RemoteDifferentialCompression.RDC_ErrorCode), use_last_error=False)(4, 'Process', ((1, 'endOfInput'),(1, 'endOfOutput'),(1, 'inputBuffer'),(1, 'depth'),(1, 'outputBuffers'),(1, 'rdc_ErrorCode'),)))
    win32more.System.Com.IUnknown
    return IRdcGenerator
def _define_IRdcFileReader_head():
    class IRdcFileReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a74-9dbc-11da-9e3f-0011114ae311')
    return IRdcFileReader
def _define_IRdcFileReader():
    IRdcFileReader = win32more.Networking.RemoteDifferentialCompression.IRdcFileReader_head
    IRdcFileReader.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(3, 'GetFileSize', ((1, 'fileSize'),)))
    IRdcFileReader.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'Read', ((1, 'offsetFileStart'),(1, 'bytesToRead'),(1, 'bytesActuallyRead'),(1, 'buffer'),(1, 'eof'),)))
    IRdcFileReader.GetFilePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetFilePosition', ((1, 'offsetFromStart'),)))
    win32more.System.Com.IUnknown
    return IRdcFileReader
def _define_IRdcFileWriter_head():
    class IRdcFileWriter(win32more.Networking.RemoteDifferentialCompression.IRdcFileReader_head):
        Guid = Guid('96236a75-9dbc-11da-9e3f-0011114ae311')
    return IRdcFileWriter
def _define_IRdcFileWriter():
    IRdcFileWriter = win32more.Networking.RemoteDifferentialCompression.IRdcFileWriter_head
    IRdcFileWriter.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,c_char_p_no, use_last_error=False)(6, 'Write', ((1, 'offsetFileStart'),(1, 'bytesToWrite'),(1, 'buffer'),)))
    IRdcFileWriter.Truncate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Truncate', ()))
    IRdcFileWriter.DeleteOnClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'DeleteOnClose', ()))
    win32more.Networking.RemoteDifferentialCompression.IRdcFileReader
    return IRdcFileWriter
def _define_IRdcSignatureReader_head():
    class IRdcSignatureReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a76-9dbc-11da-9e3f-0011114ae311')
    return IRdcSignatureReader
def _define_IRdcSignatureReader():
    IRdcSignatureReader = win32more.Networking.RemoteDifferentialCompression.IRdcSignatureReader_head
    IRdcSignatureReader.ReadHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.RDC_ErrorCode), use_last_error=False)(3, 'ReadHeader', ((1, 'rdc_ErrorCode'),)))
    IRdcSignatureReader.ReadSignatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcSignaturePointer_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'ReadSignatures', ((1, 'rdcSignaturePointer'),(1, 'endOfOutput'),)))
    win32more.System.Com.IUnknown
    return IRdcSignatureReader
def _define_IRdcComparator_head():
    class IRdcComparator(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a77-9dbc-11da-9e3f-0011114ae311')
    return IRdcComparator
def _define_IRdcComparator():
    IRdcComparator = win32more.Networking.RemoteDifferentialCompression.IRdcComparator_head
    IRdcComparator.Process = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.RemoteDifferentialCompression.RdcBufferPointer_head),POINTER(win32more.Networking.RemoteDifferentialCompression.RdcNeedPointer_head),POINTER(win32more.Networking.RemoteDifferentialCompression.RDC_ErrorCode), use_last_error=False)(3, 'Process', ((1, 'endOfInput'),(1, 'endOfOutput'),(1, 'inputBuffer'),(1, 'outputBuffer'),(1, 'rdc_ErrorCode'),)))
    win32more.System.Com.IUnknown
    return IRdcComparator
def _define_IRdcLibrary_head():
    class IRdcLibrary(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a78-9dbc-11da-9e3f-0011114ae311')
    return IRdcLibrary
def _define_IRdcLibrary():
    IRdcLibrary = win32more.Networking.RemoteDifferentialCompression.IRdcLibrary_head
    IRdcLibrary.ComputeDefaultRecursionDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt32), use_last_error=False)(3, 'ComputeDefaultRecursionDepth', ((1, 'fileSize'),(1, 'depth'),)))
    IRdcLibrary.CreateGeneratorParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.GeneratorParametersType,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head), use_last_error=False)(4, 'CreateGeneratorParameters', ((1, 'parametersType'),(1, 'level'),(1, 'iGeneratorParameters'),)))
    IRdcLibrary.OpenGeneratorParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head), use_last_error=False)(5, 'OpenGeneratorParameters', ((1, 'size'),(1, 'parametersBlob'),(1, 'iGeneratorParameters'),)))
    IRdcLibrary.CreateGenerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head),POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcGenerator_head), use_last_error=False)(6, 'CreateGenerator', ((1, 'depth'),(1, 'iGeneratorParametersArray'),(1, 'iGenerator'),)))
    IRdcLibrary.CreateComparator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.IRdcFileReader_head,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcComparator_head), use_last_error=False)(7, 'CreateComparator', ((1, 'iSeedSignaturesFile'),(1, 'comparatorBufferSize'),(1, 'iComparator'),)))
    IRdcLibrary.CreateSignatureReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.IRdcFileReader_head,POINTER(win32more.Networking.RemoteDifferentialCompression.IRdcSignatureReader_head), use_last_error=False)(8, 'CreateSignatureReader', ((1, 'iFileReader'),(1, 'iSignatureReader'),)))
    IRdcLibrary.GetRDCVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(9, 'GetRDCVersion', ((1, 'currentVersion'),(1, 'minimumCompatibleAppVersion'),)))
    win32more.System.Com.IUnknown
    return IRdcLibrary
def _define_ISimilarityReportProgress_head():
    class ISimilarityReportProgress(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a7a-9dbc-11da-9e3f-0011114ae311')
    return ISimilarityReportProgress
def _define_ISimilarityReportProgress():
    ISimilarityReportProgress = win32more.Networking.RemoteDifferentialCompression.ISimilarityReportProgress_head
    ISimilarityReportProgress.ReportProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'ReportProgress', ((1, 'percentCompleted'),)))
    win32more.System.Com.IUnknown
    return ISimilarityReportProgress
def _define_ISimilarityTableDumpState_head():
    class ISimilarityTableDumpState(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a7b-9dbc-11da-9e3f-0011114ae311')
    return ISimilarityTableDumpState
def _define_ISimilarityTableDumpState():
    ISimilarityTableDumpState = win32more.Networking.RemoteDifferentialCompression.ISimilarityTableDumpState_head
    ISimilarityTableDumpState.GetNextData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityDumpData_head), use_last_error=False)(3, 'GetNextData', ((1, 'resultsSize'),(1, 'resultsUsed'),(1, 'eof'),(1, 'results'),)))
    win32more.System.Com.IUnknown
    return ISimilarityTableDumpState
def _define_ISimilarityTraitsMappedView_head():
    class ISimilarityTraitsMappedView(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a7c-9dbc-11da-9e3f-0011114ae311')
    return ISimilarityTraitsMappedView
def _define_ISimilarityTraitsMappedView():
    ISimilarityTraitsMappedView = win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMappedView_head
    ISimilarityTraitsMappedView.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Flush', ()))
    ISimilarityTraitsMappedView.Unmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Unmap', ()))
    ISimilarityTraitsMappedView.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.Foundation.BOOL,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityMappedViewInfo_head), use_last_error=False)(5, 'Get', ((1, 'index'),(1, 'dirty'),(1, 'numElements'),(1, 'viewInfo'),)))
    ISimilarityTraitsMappedView.GetView = COMMETHOD(WINFUNCTYPE(Void,POINTER(c_char_p_no),POINTER(c_char_p_no), use_last_error=False)(6, 'GetView', ((1, 'mappedPageBegin'),(1, 'mappedPageEnd'),)))
    win32more.System.Com.IUnknown
    return ISimilarityTraitsMappedView
def _define_ISimilarityTraitsMapping_head():
    class ISimilarityTraitsMapping(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a7d-9dbc-11da-9e3f-0011114ae311')
    return ISimilarityTraitsMapping
def _define_ISimilarityTraitsMapping():
    ISimilarityTraitsMapping = win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head
    ISimilarityTraitsMapping.CloseMapping = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(3, 'CloseMapping', ()))
    ISimilarityTraitsMapping.SetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(4, 'SetFileSize', ((1, 'fileSize'),)))
    ISimilarityTraitsMapping.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetFileSize', ((1, 'fileSize'),)))
    ISimilarityTraitsMapping.OpenMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.RdcMappingAccessMode,UInt64,UInt64,POINTER(UInt64), use_last_error=False)(6, 'OpenMapping', ((1, 'accessMode'),(1, 'begin'),(1, 'end'),(1, 'actualEnd'),)))
    ISimilarityTraitsMapping.ResizeMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.RdcMappingAccessMode,UInt64,UInt64,POINTER(UInt64), use_last_error=False)(7, 'ResizeMapping', ((1, 'accessMode'),(1, 'begin'),(1, 'end'),(1, 'actualEnd'),)))
    ISimilarityTraitsMapping.GetPageSize = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32), use_last_error=False)(8, 'GetPageSize', ((1, 'pageSize'),)))
    ISimilarityTraitsMapping.CreateView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Networking.RemoteDifferentialCompression.RdcMappingAccessMode,POINTER(win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMappedView_head), use_last_error=False)(9, 'CreateView', ((1, 'minimumMappedPages'),(1, 'accessMode'),(1, 'mappedView'),)))
    win32more.System.Com.IUnknown
    return ISimilarityTraitsMapping
def _define_ISimilarityTraitsTable_head():
    class ISimilarityTraitsTable(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a7e-9dbc-11da-9e3f-0011114ae311')
    return ISimilarityTraitsTable
def _define_ISimilarityTraitsTable():
    ISimilarityTraitsTable = win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsTable_head
    ISimilarityTraitsTable.CreateTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,c_char_p_no,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables), use_last_error=False)(3, 'CreateTable', ((1, 'path'),(1, 'truncate'),(1, 'securityDescriptor'),(1, 'isNew'),)))
    ISimilarityTraitsTable.CreateTableIndirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head,win32more.Foundation.BOOL,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables), use_last_error=False)(4, 'CreateTableIndirect', ((1, 'mapping'),(1, 'truncate'),(1, 'isNew'),)))
    ISimilarityTraitsTable.CloseTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'CloseTable', ((1, 'isValid'),)))
    ISimilarityTraitsTable.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head),UInt32, use_last_error=False)(6, 'Append', ((1, 'data'),(1, 'fileIndex'),)))
    ISimilarityTraitsTable.FindSimilarFileIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head),UInt16,POINTER(win32more.Networking.RemoteDifferentialCompression.FindSimilarFileIndexResults_head),UInt32,POINTER(UInt32), use_last_error=False)(7, 'FindSimilarFileIndex', ((1, 'similarityData'),(1, 'numberOfMatchesRequired'),(1, 'findSimilarFileIndexResults'),(1, 'resultsSize'),(1, 'resultsUsed'),)))
    ISimilarityTraitsTable.BeginDump = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.ISimilarityTableDumpState_head), use_last_error=False)(8, 'BeginDump', ((1, 'similarityTableDumpState'),)))
    ISimilarityTraitsTable.GetLastIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetLastIndex', ((1, 'fileIndex'),)))
    win32more.System.Com.IUnknown
    return ISimilarityTraitsTable
def _define_ISimilarityFileIdTable_head():
    class ISimilarityFileIdTable(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a7f-9dbc-11da-9e3f-0011114ae311')
    return ISimilarityFileIdTable
def _define_ISimilarityFileIdTable():
    ISimilarityFileIdTable = win32more.Networking.RemoteDifferentialCompression.ISimilarityFileIdTable_head
    ISimilarityFileIdTable.CreateTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,c_char_p_no,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables), use_last_error=False)(3, 'CreateTable', ((1, 'path'),(1, 'truncate'),(1, 'securityDescriptor'),(1, 'recordSize'),(1, 'isNew'),)))
    ISimilarityFileIdTable.CreateTableIndirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.IRdcFileWriter_head,win32more.Foundation.BOOL,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables), use_last_error=False)(4, 'CreateTableIndirect', ((1, 'fileIdFile'),(1, 'truncate'),(1, 'recordSize'),(1, 'isNew'),)))
    ISimilarityFileIdTable.CloseTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'CloseTable', ((1, 'isValid'),)))
    ISimilarityFileIdTable.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head),POINTER(UInt32), use_last_error=False)(6, 'Append', ((1, 'similarityFileId'),(1, 'similarityFileIndex'),)))
    ISimilarityFileIdTable.Lookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head), use_last_error=False)(7, 'Lookup', ((1, 'similarityFileIndex'),(1, 'similarityFileId'),)))
    ISimilarityFileIdTable.Invalidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Invalidate', ((1, 'similarityFileIndex'),)))
    ISimilarityFileIdTable.GetRecordCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetRecordCount', ((1, 'recordCount'),)))
    win32more.System.Com.IUnknown
    return ISimilarityFileIdTable
def _define_IRdcSimilarityGenerator_head():
    class IRdcSimilarityGenerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a80-9dbc-11da-9e3f-0011114ae311')
    return IRdcSimilarityGenerator
def _define_IRdcSimilarityGenerator():
    IRdcSimilarityGenerator = win32more.Networking.RemoteDifferentialCompression.IRdcSimilarityGenerator_head
    IRdcSimilarityGenerator.EnableSimilarity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'EnableSimilarity', ()))
    IRdcSimilarityGenerator.Results = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head), use_last_error=False)(4, 'Results', ((1, 'similarityData'),)))
    win32more.System.Com.IUnknown
    return IRdcSimilarityGenerator
def _define_IFindSimilarResults_head():
    class IFindSimilarResults(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a81-9dbc-11da-9e3f-0011114ae311')
    return IFindSimilarResults
def _define_IFindSimilarResults():
    IFindSimilarResults = win32more.Networking.RemoteDifferentialCompression.IFindSimilarResults_head
    IFindSimilarResults.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetSize', ((1, 'size'),)))
    IFindSimilarResults.GetNextFileId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head), use_last_error=False)(4, 'GetNextFileId', ((1, 'numTraitsMatched'),(1, 'similarityFileId'),)))
    win32more.System.Com.IUnknown
    return IFindSimilarResults
def _define_ISimilarity_head():
    class ISimilarity(win32more.System.Com.IUnknown_head):
        Guid = Guid('96236a83-9dbc-11da-9e3f-0011114ae311')
    return ISimilarity
def _define_ISimilarity():
    ISimilarity = win32more.Networking.RemoteDifferentialCompression.ISimilarity_head
    ISimilarity.CreateTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,c_char_p_no,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables), use_last_error=False)(3, 'CreateTable', ((1, 'path'),(1, 'truncate'),(1, 'securityDescriptor'),(1, 'recordSize'),(1, 'isNew'),)))
    ISimilarity.CreateTableIndirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head,win32more.Networking.RemoteDifferentialCompression.IRdcFileWriter_head,win32more.Foundation.BOOL,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.RdcCreatedTables), use_last_error=False)(4, 'CreateTableIndirect', ((1, 'mapping'),(1, 'fileIdFile'),(1, 'truncate'),(1, 'recordSize'),(1, 'isNew'),)))
    ISimilarity.CloseTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'CloseTable', ((1, 'isValid'),)))
    ISimilarity.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityFileId_head),POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head), use_last_error=False)(6, 'Append', ((1, 'similarityFileId'),(1, 'similarityData'),)))
    ISimilarity.FindSimilarFileId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.RemoteDifferentialCompression.SimilarityData_head),UInt16,UInt32,POINTER(win32more.Networking.RemoteDifferentialCompression.IFindSimilarResults_head), use_last_error=False)(7, 'FindSimilarFileId', ((1, 'similarityData'),(1, 'numberOfMatchesRequired'),(1, 'resultsSize'),(1, 'findSimilarResults'),)))
    ISimilarity.CopyAndSwap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.RemoteDifferentialCompression.ISimilarity_head,win32more.Networking.RemoteDifferentialCompression.ISimilarityReportProgress_head, use_last_error=False)(8, 'CopyAndSwap', ((1, 'newSimilarityTables'),(1, 'reportProgress'),)))
    ISimilarity.GetRecordCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetRecordCount', ((1, 'recordCount'),)))
    win32more.System.Com.IUnknown
    return ISimilarity
__all__ = [
    "RDCE_TABLE_FULL",
    "RDCE_TABLE_CORRUPT",
    "MSRDC_SIGNATURE_HASHSIZE",
    "SimilarityFileIdMinSize",
    "SimilarityFileIdMaxSize",
    "MSRDC_VERSION",
    "MSRDC_MINIMUM_COMPATIBLE_APP_VERSION",
    "MSRDC_MINIMUM_DEPTH",
    "MSRDC_MAXIMUM_DEPTH",
    "MSRDC_MINIMUM_COMPAREBUFFER",
    "MSRDC_MAXIMUM_COMPAREBUFFER",
    "MSRDC_DEFAULT_COMPAREBUFFER",
    "MSRDC_MINIMUM_INPUTBUFFERSIZE",
    "MSRDC_MINIMUM_HORIZONSIZE",
    "MSRDC_MAXIMUM_HORIZONSIZE",
    "MSRDC_MINIMUM_HASHWINDOWSIZE",
    "MSRDC_MAXIMUM_HASHWINDOWSIZE",
    "MSRDC_DEFAULT_HASHWINDOWSIZE_1",
    "MSRDC_DEFAULT_HORIZONSIZE_1",
    "MSRDC_DEFAULT_HASHWINDOWSIZE_N",
    "MSRDC_DEFAULT_HORIZONSIZE_N",
    "MSRDC_MAXIMUM_TRAITVALUE",
    "MSRDC_MINIMUM_MATCHESREQUIRED",
    "MSRDC_MAXIMUM_MATCHESREQUIRED",
    "RdcLibrary",
    "RdcGeneratorParameters",
    "RdcGeneratorFilterMaxParameters",
    "RdcGenerator",
    "RdcFileReader",
    "RdcSignatureReader",
    "RdcComparator",
    "SimilarityReportProgress",
    "SimilarityTableDumpState",
    "SimilarityTraitsTable",
    "SimilarityFileIdTable",
    "Similarity",
    "RdcSimilarityGenerator",
    "FindSimilarResults",
    "SimilarityTraitsMapping",
    "SimilarityTraitsMappedView",
    "RDC_ErrorCode",
    "RDC_NoError",
    "RDC_HeaderVersionNewer",
    "RDC_HeaderVersionOlder",
    "RDC_HeaderMissingOrCorrupt",
    "RDC_HeaderWrongType",
    "RDC_DataMissingOrCorrupt",
    "RDC_DataTooManyRecords",
    "RDC_FileChecksumMismatch",
    "RDC_ApplicationError",
    "RDC_Aborted",
    "RDC_Win32Error",
    "GeneratorParametersType",
    "RDCGENTYPE_Unused",
    "RDCGENTYPE_FilterMax",
    "RdcNeedType",
    "RDCNEED_SOURCE",
    "RDCNEED_TARGET",
    "RDCNEED_SEED",
    "RDCNEED_SEED_MAX",
    "RdcNeed",
    "RdcBufferPointer",
    "RdcNeedPointer",
    "RdcSignature",
    "RdcSignaturePointer",
    "RdcCreatedTables",
    "RDCTABLE_InvalidOrUnknown",
    "RDCTABLE_Existing",
    "RDCTABLE_New",
    "RdcMappingAccessMode",
    "RDCMAPPING_Undefined",
    "RDCMAPPING_ReadOnly",
    "RDCMAPPING_ReadWrite",
    "SimilarityMappedViewInfo",
    "SimilarityData",
    "FindSimilarFileIndexResults",
    "SimilarityDumpData",
    "SimilarityFileId",
    "IRdcGeneratorParameters",
    "IRdcGeneratorFilterMaxParameters",
    "IRdcGenerator",
    "IRdcFileReader",
    "IRdcFileWriter",
    "IRdcSignatureReader",
    "IRdcComparator",
    "IRdcLibrary",
    "ISimilarityReportProgress",
    "ISimilarityTableDumpState",
    "ISimilarityTraitsMappedView",
    "ISimilarityTraitsMapping",
    "ISimilarityTraitsTable",
    "ISimilarityFileIdTable",
    "IRdcSimilarityGenerator",
    "IFindSimilarResults",
    "ISimilarity",
]
