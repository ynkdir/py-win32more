from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Storage.DataDeduplication
import Windows.Win32.System.Com
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DEDUP_CHUNKLIB_MAX_CHUNKS_ENUM: UInt32 = 1024
class DDP_FILE_EXTENT(EasyCastStructure):
    Length: Int64
    Offset: Int64
DEDUP_BACKUP_SUPPORT_PARAM_TYPE = Int32
DEDUP_RECONSTRUCT_UNOPTIMIZED: DEDUP_BACKUP_SUPPORT_PARAM_TYPE = 1
DEDUP_RECONSTRUCT_OPTIMIZED: DEDUP_BACKUP_SUPPORT_PARAM_TYPE = 2
class DEDUP_CHUNK_INFO_HASH32(EasyCastStructure):
    ChunkFlags: UInt32
    ChunkOffsetInStream: UInt64
    ChunkSize: UInt64
    HashVal: Byte * 32
class DEDUP_CONTAINER_EXTENT(EasyCastStructure):
    ContainerIndex: UInt32
    StartOffset: Int64
    Length: Int64
DEDUP_SET_PARAM_TYPE = Int32
DEDUP_PT_MinChunkSizeBytes: DEDUP_SET_PARAM_TYPE = 1
DEDUP_PT_MaxChunkSizeBytes: DEDUP_SET_PARAM_TYPE = 2
DEDUP_PT_AvgChunkSizeBytes: DEDUP_SET_PARAM_TYPE = 3
DEDUP_PT_InvariantChunking: DEDUP_SET_PARAM_TYPE = 4
DEDUP_PT_DisableStrongHashComputation: DEDUP_SET_PARAM_TYPE = 5
DedupBackupSupport = Guid('{73d6b2ad-2984-4715-b2e3-924c149744dd}')
class DedupChunk(EasyCastStructure):
    Hash: Windows.Win32.Storage.DataDeduplication.DedupHash
    Flags: Windows.Win32.Storage.DataDeduplication.DedupChunkFlags
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
DedupDataPort = Guid('{8f107207-1829-48b2-a64b-e61f8e0d9acb}')
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
class DedupHash(EasyCastStructure):
    Hash: Byte * 32
DedupHashingAlgorithm = Int32
DedupHashingAlgorithm_Unknonwn: DedupHashingAlgorithm = 0
DedupHashingAlgorithm_V1: DedupHashingAlgorithm = 1
class DedupStream(EasyCastStructure):
    Path: Windows.Win32.Foundation.BSTR
    Offset: UInt64
    Length: UInt64
    ChunkCount: UInt32
class DedupStreamEntry(EasyCastStructure):
    Hash: Windows.Win32.Storage.DataDeduplication.DedupHash
    LogicalSize: UInt32
    Offset: UInt64
class IDedupBackupSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c719d963-2b2d-415e-acf7-7eb7ca596ff4}')
    @commethod(3)
    def RestoreFiles(self, NumberOfFiles: UInt32, FileFullPaths: POINTER(Windows.Win32.Foundation.BSTR), Store: Windows.Win32.Storage.DataDeduplication.IDedupReadFileCallback_head, Flags: UInt32, FileResults: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IDedupChunkLibrary(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb5144d7-2720-4dcc-8777-78597416ec23}')
    @commethod(3)
    def InitializeForPushBuffers(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetParameter(self, dwParamType: UInt32, vParamValue: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StartChunking(self, iidIteratorInterfaceID: Guid, ppChunksEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDedupDataPort(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7963d734-40a9-4ea3-bbf6-5a89d26f7ae8}')
    @commethod(3)
    def GetStatus(self, pStatus: POINTER(Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus), pDataHeadroomMb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LookupChunks(self, Count: UInt32, pHashes: POINTER(Windows.Win32.Storage.DataDeduplication.DedupHash_head), pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertChunks(self, ChunkCount: UInt32, pChunkMetadata: POINTER(Windows.Win32.Storage.DataDeduplication.DedupChunk_head), DataByteCount: UInt32, pChunkData: POINTER(Byte), pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InsertChunksWithStream(self, ChunkCount: UInt32, pChunkMetadata: POINTER(Windows.Win32.Storage.DataDeduplication.DedupChunk_head), DataByteCount: UInt32, pChunkDataStream: Windows.Win32.System.Com.IStream_head, pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CommitStreams(self, StreamCount: UInt32, pStreams: POINTER(Windows.Win32.Storage.DataDeduplication.DedupStream_head), EntryCount: UInt32, pEntries: POINTER(Windows.Win32.Storage.DataDeduplication.DedupStreamEntry_head), pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitStreamsWithStream(self, StreamCount: UInt32, pStreams: POINTER(Windows.Win32.Storage.DataDeduplication.DedupStream_head), EntryCount: UInt32, pEntriesStream: Windows.Win32.System.Com.IStream_head, pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreams(self, StreamCount: UInt32, pStreamPaths: POINTER(Windows.Win32.Foundation.BSTR), pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStreamsResults(self, RequestId: Guid, MaxWaitMs: UInt32, StreamEntryIndex: UInt32, pStreamCount: POINTER(UInt32), ppStreams: POINTER(POINTER(Windows.Win32.Storage.DataDeduplication.DedupStream_head)), pEntryCount: POINTER(UInt32), ppEntries: POINTER(POINTER(Windows.Win32.Storage.DataDeduplication.DedupStreamEntry_head)), pStatus: POINTER(Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(Windows.Win32.Foundation.HRESULT))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetChunks(self, Count: UInt32, pHashes: POINTER(Windows.Win32.Storage.DataDeduplication.DedupHash_head), pRequestId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChunksResults(self, RequestId: Guid, MaxWaitMs: UInt32, ChunkIndex: UInt32, pChunkCount: POINTER(UInt32), ppChunkMetadata: POINTER(POINTER(Windows.Win32.Storage.DataDeduplication.DedupChunk_head)), pDataByteCount: POINTER(UInt32), ppChunkData: POINTER(POINTER(Byte)), pStatus: POINTER(Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(Windows.Win32.Foundation.HRESULT))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRequestStatus(self, RequestId: Guid, pStatus: POINTER(Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRequestResults(self, RequestId: Guid, MaxWaitMs: UInt32, pBatchResult: POINTER(Windows.Win32.Foundation.HRESULT), pBatchCount: POINTER(UInt32), pStatus: POINTER(Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(Windows.Win32.Foundation.HRESULT))) -> Windows.Win32.Foundation.HRESULT: ...
class IDedupDataPortManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44677452-b90a-445e-8192-cdcfe81511fb}')
    @commethod(3)
    def GetConfiguration(self, pMinChunkSize: POINTER(UInt32), pMaxChunkSize: POINTER(UInt32), pChunkingAlgorithm: POINTER(Windows.Win32.Storage.DataDeduplication.DedupChunkingAlgorithm), pHashingAlgorithm: POINTER(Windows.Win32.Storage.DataDeduplication.DedupHashingAlgorithm), pCompressionAlgorithm: POINTER(Windows.Win32.Storage.DataDeduplication.DedupCompressionAlgorithm)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVolumeStatus(self, Options: UInt32, Path: Windows.Win32.Foundation.BSTR, pStatus: POINTER(Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVolumeDataPort(self, Options: UInt32, Path: Windows.Win32.Foundation.BSTR, ppDataPort: POINTER(Windows.Win32.Storage.DataDeduplication.IDedupDataPort_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDedupIterateChunksHash32(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90b584d3-72aa-400f-9767-cad866a5a2d8}')
    @commethod(3)
    def PushBuffer(self, pBuffer: POINTER(Byte), ulBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulMaxChunks: UInt32, pArrChunks: POINTER(Windows.Win32.Storage.DataDeduplication.DEDUP_CHUNK_INFO_HASH32_head), pulFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Drain(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDedupReadFileCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bacc67a-2f1d-42d0-897e-6ff62dd533bb}')
    @commethod(3)
    def ReadBackupFile(self, FileFullPath: Windows.Win32.Foundation.BSTR, FileOffset: Int64, SizeToRead: UInt32, FileBuffer: POINTER(Byte), ReturnedSize: POINTER(UInt32), Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OrderContainersRestore(self, NumberOfContainers: UInt32, ContainerPaths: POINTER(Windows.Win32.Foundation.BSTR), ReadPlanEntries: POINTER(UInt32), ReadPlan: POINTER(POINTER(Windows.Win32.Storage.DataDeduplication.DEDUP_CONTAINER_EXTENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PreviewContainerRead(self, FileFullPath: Windows.Win32.Foundation.BSTR, NumberOfReads: UInt32, ReadOffsets: POINTER(Windows.Win32.Storage.DataDeduplication.DDP_FILE_EXTENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
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
