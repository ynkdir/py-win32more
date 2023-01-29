from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.DataDeduplication
import win32more.System.Com
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
DEDUP_CHUNKLIB_MAX_CHUNKS_ENUM: UInt32 = 1024
class DDP_FILE_EXTENT(Structure):
    Length: Int64
    Offset: Int64
DEDUP_BACKUP_SUPPORT_PARAM_TYPE = Int32
DEDUP_RECONSTRUCT_UNOPTIMIZED: DEDUP_BACKUP_SUPPORT_PARAM_TYPE = 1
DEDUP_RECONSTRUCT_OPTIMIZED: DEDUP_BACKUP_SUPPORT_PARAM_TYPE = 2
class DEDUP_CHUNK_INFO_HASH32(Structure):
    ChunkFlags: UInt32
    ChunkOffsetInStream: UInt64
    ChunkSize: UInt64
    HashVal: Byte * 32
class DEDUP_CONTAINER_EXTENT(Structure):
    ContainerIndex: UInt32
    StartOffset: Int64
    Length: Int64
DEDUP_SET_PARAM_TYPE = Int32
DEDUP_PT_MinChunkSizeBytes: DEDUP_SET_PARAM_TYPE = 1
DEDUP_PT_MaxChunkSizeBytes: DEDUP_SET_PARAM_TYPE = 2
DEDUP_PT_AvgChunkSizeBytes: DEDUP_SET_PARAM_TYPE = 3
DEDUP_PT_InvariantChunking: DEDUP_SET_PARAM_TYPE = 4
DEDUP_PT_DisableStrongHashComputation: DEDUP_SET_PARAM_TYPE = 5
DedupBackupSupport = Guid('73d6b2ad-2984-4715-b2-e3-92-4c-14-97-44-dd')
class DedupChunk(Structure):
    Hash: win32more.Storage.DataDeduplication.DedupHash
    Flags: win32more.Storage.DataDeduplication.DedupChunkFlags
    LogicalSize: UInt32
    DataSize: UInt32
DedupChunkFlags = Int32
DedupChunkFlags_None: DedupChunkFlags = 0
DedupChunkFlags_Compressed: DedupChunkFlags = 1
DedupChunkingAlgorithm = Int32
DedupChunkingAlgorithm_Unknonwn: DedupChunkingAlgorithm = 0
DedupChunkingAlgorithm_V1: DedupChunkingAlgorithm = 1
DedupCompressionAlgorithm = Int32
DedupCompressionAlgorithm_Unknonwn: DedupCompressionAlgorithm = 0
DedupCompressionAlgorithm_Xpress: DedupCompressionAlgorithm = 1
DedupDataPort = Guid('8f107207-1829-48b2-a6-4b-e6-1f-8e-0d-9a-cb')
DedupDataPortManagerOption = Int32
DedupDataPortManagerOption_None: DedupDataPortManagerOption = 0
DedupDataPortManagerOption_AutoStart: DedupDataPortManagerOption = 1
DedupDataPortManagerOption_SkipReconciliation: DedupDataPortManagerOption = 2
DedupDataPortRequestStatus = Int32
DedupDataPortRequestStatus_Unknown: DedupDataPortRequestStatus = 0
DedupDataPortRequestStatus_Queued: DedupDataPortRequestStatus = 1
DedupDataPortRequestStatus_Processing: DedupDataPortRequestStatus = 2
DedupDataPortRequestStatus_Partial: DedupDataPortRequestStatus = 3
DedupDataPortRequestStatus_Complete: DedupDataPortRequestStatus = 4
DedupDataPortRequestStatus_Failed: DedupDataPortRequestStatus = 5
DedupDataPortVolumeStatus = Int32
DedupDataPortVolumeStatus_Unknown: DedupDataPortVolumeStatus = 0
DedupDataPortVolumeStatus_NotEnabled: DedupDataPortVolumeStatus = 1
DedupDataPortVolumeStatus_NotAvailable: DedupDataPortVolumeStatus = 2
DedupDataPortVolumeStatus_Initializing: DedupDataPortVolumeStatus = 3
DedupDataPortVolumeStatus_Ready: DedupDataPortVolumeStatus = 4
DedupDataPortVolumeStatus_Maintenance: DedupDataPortVolumeStatus = 5
DedupDataPortVolumeStatus_Shutdown: DedupDataPortVolumeStatus = 6
class DedupHash(Structure):
    Hash: Byte * 32
DedupHashingAlgorithm = Int32
DedupHashingAlgorithm_Unknonwn: DedupHashingAlgorithm = 0
DedupHashingAlgorithm_V1: DedupHashingAlgorithm = 1
class DedupStream(Structure):
    Path: win32more.Foundation.BSTR
    Offset: UInt64
    Length: UInt64
    ChunkCount: UInt32
class DedupStreamEntry(Structure):
    Hash: win32more.Storage.DataDeduplication.DedupHash
    LogicalSize: UInt32
    Offset: UInt64
class IDedupBackupSupport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c719d963-2b2d-415e-ac-f7-7e-b7-ca-59-6f-f4')
    @commethod(3)
    def RestoreFiles(NumberOfFiles: UInt32, FileFullPaths: POINTER(win32more.Foundation.BSTR), Store: win32more.Storage.DataDeduplication.IDedupReadFileCallback_head, Flags: UInt32, FileResults: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
class IDedupChunkLibrary(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bb5144d7-2720-4dcc-87-77-78-59-74-16-ec-23')
    @commethod(3)
    def InitializeForPushBuffers() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetParameter(dwParamType: UInt32, vParamValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def StartChunking(iidIteratorInterfaceID: Guid, ppChunksEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IDedupDataPort(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7963d734-40a9-4ea3-bb-f6-5a-89-d2-6f-7a-e8')
    @commethod(3)
    def GetStatus(pStatus: POINTER(win32more.Storage.DataDeduplication.DedupDataPortVolumeStatus), pDataHeadroomMb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LookupChunks(Count: UInt32, pHashes: POINTER(win32more.Storage.DataDeduplication.DedupHash_head), pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertChunks(ChunkCount: UInt32, pChunkMetadata: POINTER(win32more.Storage.DataDeduplication.DedupChunk_head), DataByteCount: UInt32, pChunkData: c_char_p_no, pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def InsertChunksWithStream(ChunkCount: UInt32, pChunkMetadata: POINTER(win32more.Storage.DataDeduplication.DedupChunk_head), DataByteCount: UInt32, pChunkDataStream: win32more.System.Com.IStream_head, pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CommitStreams(StreamCount: UInt32, pStreams: POINTER(win32more.Storage.DataDeduplication.DedupStream_head), EntryCount: UInt32, pEntries: POINTER(win32more.Storage.DataDeduplication.DedupStreamEntry_head), pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CommitStreamsWithStream(StreamCount: UInt32, pStreams: POINTER(win32more.Storage.DataDeduplication.DedupStream_head), EntryCount: UInt32, pEntriesStream: win32more.System.Com.IStream_head, pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreams(StreamCount: UInt32, pStreamPaths: POINTER(win32more.Foundation.BSTR), pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetStreamsResults(RequestId: Guid, MaxWaitMs: UInt32, StreamEntryIndex: UInt32, pStreamCount: POINTER(UInt32), ppStreams: POINTER(POINTER(win32more.Storage.DataDeduplication.DedupStream_head)), pEntryCount: POINTER(UInt32), ppEntries: POINTER(POINTER(win32more.Storage.DataDeduplication.DedupStreamEntry_head)), pStatus: POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(win32more.Foundation.HRESULT))) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetChunks(Count: UInt32, pHashes: POINTER(win32more.Storage.DataDeduplication.DedupHash_head), pRequestId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetChunksResults(RequestId: Guid, MaxWaitMs: UInt32, ChunkIndex: UInt32, pChunkCount: POINTER(UInt32), ppChunkMetadata: POINTER(POINTER(win32more.Storage.DataDeduplication.DedupChunk_head)), pDataByteCount: POINTER(UInt32), ppChunkData: POINTER(c_char_p_no), pStatus: POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(win32more.Foundation.HRESULT))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRequestStatus(RequestId: Guid, pStatus: POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRequestResults(RequestId: Guid, MaxWaitMs: UInt32, pBatchResult: POINTER(win32more.Foundation.HRESULT), pBatchCount: POINTER(UInt32), pStatus: POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(win32more.Foundation.HRESULT))) -> win32more.Foundation.HRESULT: ...
class IDedupDataPortManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('44677452-b90a-445e-81-92-cd-cf-e8-15-11-fb')
    @commethod(3)
    def GetConfiguration(pMinChunkSize: POINTER(UInt32), pMaxChunkSize: POINTER(UInt32), pChunkingAlgorithm: POINTER(win32more.Storage.DataDeduplication.DedupChunkingAlgorithm), pHashingAlgorithm: POINTER(win32more.Storage.DataDeduplication.DedupHashingAlgorithm), pCompressionAlgorithm: POINTER(win32more.Storage.DataDeduplication.DedupCompressionAlgorithm)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVolumeStatus(Options: UInt32, Path: win32more.Foundation.BSTR, pStatus: POINTER(win32more.Storage.DataDeduplication.DedupDataPortVolumeStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVolumeDataPort(Options: UInt32, Path: win32more.Foundation.BSTR, ppDataPort: POINTER(win32more.Storage.DataDeduplication.IDedupDataPort_head)) -> win32more.Foundation.HRESULT: ...
class IDedupIterateChunksHash32(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('90b584d3-72aa-400f-97-67-ca-d8-66-a5-a2-d8')
    @commethod(3)
    def PushBuffer(pBuffer: c_char_p_no, ulBufferLength: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulMaxChunks: UInt32, pArrChunks: POINTER(win32more.Storage.DataDeduplication.DEDUP_CHUNK_INFO_HASH32_head), pulFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Drain() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Reset() -> win32more.Foundation.HRESULT: ...
class IDedupReadFileCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7bacc67a-2f1d-42d0-89-7e-6f-f6-2d-d5-33-bb')
    @commethod(3)
    def ReadBackupFile(FileFullPath: win32more.Foundation.BSTR, FileOffset: Int64, SizeToRead: UInt32, FileBuffer: c_char_p_no, ReturnedSize: POINTER(UInt32), Flags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OrderContainersRestore(NumberOfContainers: UInt32, ContainerPaths: POINTER(win32more.Foundation.BSTR), ReadPlanEntries: POINTER(UInt32), ReadPlan: POINTER(POINTER(win32more.Storage.DataDeduplication.DEDUP_CONTAINER_EXTENT_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PreviewContainerRead(FileFullPath: win32more.Foundation.BSTR, NumberOfReads: UInt32, ReadOffsets: POINTER(win32more.Storage.DataDeduplication.DDP_FILE_EXTENT_head)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'DDP_FILE_EXTENT')
make_head(_module, 'DEDUP_CHUNK_INFO_HASH32')
make_head(_module, 'DEDUP_CONTAINER_EXTENT')
make_head(_module, 'DedupChunk')
make_head(_module, 'DedupHash')
make_head(_module, 'DedupStream')
make_head(_module, 'DedupStreamEntry')
make_head(_module, 'IDedupBackupSupport')
make_head(_module, 'IDedupChunkLibrary')
make_head(_module, 'IDedupDataPort')
make_head(_module, 'IDedupDataPortManager')
make_head(_module, 'IDedupIterateChunksHash32')
make_head(_module, 'IDedupReadFileCallback')
__all__ = [
    "DDP_FILE_EXTENT",
    "DEDUP_BACKUP_SUPPORT_PARAM_TYPE",
    "DEDUP_CHUNKLIB_MAX_CHUNKS_ENUM",
    "DEDUP_CHUNK_INFO_HASH32",
    "DEDUP_CONTAINER_EXTENT",
    "DEDUP_PT_AvgChunkSizeBytes",
    "DEDUP_PT_DisableStrongHashComputation",
    "DEDUP_PT_InvariantChunking",
    "DEDUP_PT_MaxChunkSizeBytes",
    "DEDUP_PT_MinChunkSizeBytes",
    "DEDUP_RECONSTRUCT_OPTIMIZED",
    "DEDUP_RECONSTRUCT_UNOPTIMIZED",
    "DEDUP_SET_PARAM_TYPE",
    "DedupBackupSupport",
    "DedupChunk",
    "DedupChunkFlags",
    "DedupChunkFlags_Compressed",
    "DedupChunkFlags_None",
    "DedupChunkingAlgorithm",
    "DedupChunkingAlgorithm_Unknonwn",
    "DedupChunkingAlgorithm_V1",
    "DedupCompressionAlgorithm",
    "DedupCompressionAlgorithm_Unknonwn",
    "DedupCompressionAlgorithm_Xpress",
    "DedupDataPort",
    "DedupDataPortManagerOption",
    "DedupDataPortManagerOption_AutoStart",
    "DedupDataPortManagerOption_None",
    "DedupDataPortManagerOption_SkipReconciliation",
    "DedupDataPortRequestStatus",
    "DedupDataPortRequestStatus_Complete",
    "DedupDataPortRequestStatus_Failed",
    "DedupDataPortRequestStatus_Partial",
    "DedupDataPortRequestStatus_Processing",
    "DedupDataPortRequestStatus_Queued",
    "DedupDataPortRequestStatus_Unknown",
    "DedupDataPortVolumeStatus",
    "DedupDataPortVolumeStatus_Initializing",
    "DedupDataPortVolumeStatus_Maintenance",
    "DedupDataPortVolumeStatus_NotAvailable",
    "DedupDataPortVolumeStatus_NotEnabled",
    "DedupDataPortVolumeStatus_Ready",
    "DedupDataPortVolumeStatus_Shutdown",
    "DedupDataPortVolumeStatus_Unknown",
    "DedupHash",
    "DedupHashingAlgorithm",
    "DedupHashingAlgorithm_Unknonwn",
    "DedupHashingAlgorithm_V1",
    "DedupStream",
    "DedupStreamEntry",
    "IDedupBackupSupport",
    "IDedupChunkLibrary",
    "IDedupDataPort",
    "IDedupDataPortManager",
    "IDedupIterateChunksHash32",
    "IDedupReadFileCallback",
]
_arch_optional = [
]
