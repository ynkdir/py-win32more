from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.DataDeduplication
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
DEDUP_CHUNKLIB_MAX_CHUNKS_ENUM: UInt32 = 1024
class DDP_FILE_EXTENT(Structure):
    Length: Int64
    Offset: Int64
DEDUP_BACKUP_SUPPORT_PARAM_TYPE = Int32
DEDUP_RECONSTRUCT_UNOPTIMIZED: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_BACKUP_SUPPORT_PARAM_TYPE = 1
DEDUP_RECONSTRUCT_OPTIMIZED: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_BACKUP_SUPPORT_PARAM_TYPE = 2
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
DEDUP_PT_MinChunkSizeBytes: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_SET_PARAM_TYPE = 1
DEDUP_PT_MaxChunkSizeBytes: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_SET_PARAM_TYPE = 2
DEDUP_PT_AvgChunkSizeBytes: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_SET_PARAM_TYPE = 3
DEDUP_PT_InvariantChunking: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_SET_PARAM_TYPE = 4
DEDUP_PT_DisableStrongHashComputation: win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_SET_PARAM_TYPE = 5
DedupBackupSupport = Guid('{73d6b2ad-2984-4715-b2e3-924c149744dd}')
class DedupChunk(Structure):
    Hash: win32more.Windows.Win32.Storage.DataDeduplication.DedupHash
    Flags: win32more.Windows.Win32.Storage.DataDeduplication.DedupChunkFlags
    LogicalSize: UInt32
    DataSize: UInt32
DedupChunkFlags = Int32
DedupChunkFlags_None: win32more.Windows.Win32.Storage.DataDeduplication.DedupChunkFlags = 0
DedupChunkFlags_Compressed: win32more.Windows.Win32.Storage.DataDeduplication.DedupChunkFlags = 1
DedupChunkingAlgorithm = Int32
DedupChunkingAlgorithm_Unknonwn: win32more.Windows.Win32.Storage.DataDeduplication.DedupChunkingAlgorithm = 0
DedupChunkingAlgorithm_V1: win32more.Windows.Win32.Storage.DataDeduplication.DedupChunkingAlgorithm = 1
DedupCompressionAlgorithm = Int32
DedupCompressionAlgorithm_Unknonwn: win32more.Windows.Win32.Storage.DataDeduplication.DedupCompressionAlgorithm = 0
DedupCompressionAlgorithm_Xpress: win32more.Windows.Win32.Storage.DataDeduplication.DedupCompressionAlgorithm = 1
DedupDataPort = Guid('{8f107207-1829-48b2-a64b-e61f8e0d9acb}')
DedupDataPortManagerOption = Int32
DedupDataPortManagerOption_None: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortManagerOption = 0
DedupDataPortManagerOption_AutoStart: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortManagerOption = 1
DedupDataPortManagerOption_SkipReconciliation: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortManagerOption = 2
DedupDataPortRequestStatus = Int32
DedupDataPortRequestStatus_Unknown: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus = 0
DedupDataPortRequestStatus_Queued: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus = 1
DedupDataPortRequestStatus_Processing: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus = 2
DedupDataPortRequestStatus_Partial: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus = 3
DedupDataPortRequestStatus_Complete: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus = 4
DedupDataPortRequestStatus_Failed: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus = 5
DedupDataPortVolumeStatus = Int32
DedupDataPortVolumeStatus_Unknown: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 0
DedupDataPortVolumeStatus_NotEnabled: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 1
DedupDataPortVolumeStatus_NotAvailable: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 2
DedupDataPortVolumeStatus_Initializing: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 3
DedupDataPortVolumeStatus_Ready: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 4
DedupDataPortVolumeStatus_Maintenance: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 5
DedupDataPortVolumeStatus_Shutdown: win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus = 6
class DedupHash(Structure):
    Hash: Byte * 32
DedupHashingAlgorithm = Int32
DedupHashingAlgorithm_Unknonwn: win32more.Windows.Win32.Storage.DataDeduplication.DedupHashingAlgorithm = 0
DedupHashingAlgorithm_V1: win32more.Windows.Win32.Storage.DataDeduplication.DedupHashingAlgorithm = 1
class DedupStream(Structure):
    Path: win32more.Windows.Win32.Foundation.BSTR
    Offset: UInt64
    Length: UInt64
    ChunkCount: UInt32
class DedupStreamEntry(Structure):
    Hash: win32more.Windows.Win32.Storage.DataDeduplication.DedupHash
    LogicalSize: UInt32
    Offset: UInt64
class IDedupBackupSupport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c719d963-2b2d-415e-acf7-7eb7ca596ff4}')
    @commethod(3)
    def RestoreFiles(self, NumberOfFiles: UInt32, FileFullPaths: POINTER(win32more.Windows.Win32.Foundation.BSTR), Store: win32more.Windows.Win32.Storage.DataDeduplication.IDedupReadFileCallback, Flags: UInt32, FileResults: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDedupChunkLibrary(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb5144d7-2720-4dcc-8777-78597416ec23}')
    @commethod(3)
    def InitializeForPushBuffers(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetParameter(self, dwParamType: UInt32, vParamValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StartChunking(self, iidIteratorInterfaceID: Guid, ppChunksEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDedupDataPort(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7963d734-40a9-4ea3-bbf6-5a89d26f7ae8}')
    @commethod(3)
    def GetStatus(self, pStatus: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus), pDataHeadroomMb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LookupChunks(self, Count: UInt32, pHashes: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupHash), pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertChunks(self, ChunkCount: UInt32, pChunkMetadata: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupChunk), DataByteCount: UInt32, pChunkData: POINTER(Byte), pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InsertChunksWithStream(self, ChunkCount: UInt32, pChunkMetadata: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupChunk), DataByteCount: UInt32, pChunkDataStream: win32more.Windows.Win32.System.Com.IStream, pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CommitStreams(self, StreamCount: UInt32, pStreams: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupStream), EntryCount: UInt32, pEntries: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupStreamEntry), pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitStreamsWithStream(self, StreamCount: UInt32, pStreams: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupStream), EntryCount: UInt32, pEntriesStream: win32more.Windows.Win32.System.Com.IStream, pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreams(self, StreamCount: UInt32, pStreamPaths: POINTER(win32more.Windows.Win32.Foundation.BSTR), pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStreamsResults(self, RequestId: Guid, MaxWaitMs: UInt32, StreamEntryIndex: UInt32, pStreamCount: POINTER(UInt32), ppStreams: POINTER(POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupStream)), pEntryCount: POINTER(UInt32), ppEntries: POINTER(POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupStreamEntry)), pStatus: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(win32more.Windows.Win32.Foundation.HRESULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetChunks(self, Count: UInt32, pHashes: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupHash), pRequestId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetChunksResults(self, RequestId: Guid, MaxWaitMs: UInt32, ChunkIndex: UInt32, pChunkCount: POINTER(UInt32), ppChunkMetadata: POINTER(POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupChunk)), pDataByteCount: POINTER(UInt32), ppChunkData: POINTER(POINTER(Byte)), pStatus: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(win32more.Windows.Win32.Foundation.HRESULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRequestStatus(self, RequestId: Guid, pStatus: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRequestResults(self, RequestId: Guid, MaxWaitMs: UInt32, pBatchResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), pBatchCount: POINTER(UInt32), pStatus: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortRequestStatus), ppItemResults: POINTER(POINTER(win32more.Windows.Win32.Foundation.HRESULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDedupDataPortManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44677452-b90a-445e-8192-cdcfe81511fb}')
    @commethod(3)
    def GetConfiguration(self, pMinChunkSize: POINTER(UInt32), pMaxChunkSize: POINTER(UInt32), pChunkingAlgorithm: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupChunkingAlgorithm), pHashingAlgorithm: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupHashingAlgorithm), pCompressionAlgorithm: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupCompressionAlgorithm)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVolumeStatus(self, Options: UInt32, Path: win32more.Windows.Win32.Foundation.BSTR, pStatus: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DedupDataPortVolumeStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVolumeDataPort(self, Options: UInt32, Path: win32more.Windows.Win32.Foundation.BSTR, ppDataPort: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.IDedupDataPort)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDedupIterateChunksHash32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90b584d3-72aa-400f-9767-cad866a5a2d8}')
    @commethod(3)
    def PushBuffer(self, pBuffer: POINTER(Byte), ulBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulMaxChunks: UInt32, pArrChunks: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_CHUNK_INFO_HASH32), pulFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Drain(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDedupReadFileCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bacc67a-2f1d-42d0-897e-6ff62dd533bb}')
    @commethod(3)
    def ReadBackupFile(self, FileFullPath: win32more.Windows.Win32.Foundation.BSTR, FileOffset: Int64, SizeToRead: UInt32, FileBuffer: POINTER(Byte), ReturnedSize: POINTER(UInt32), Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OrderContainersRestore(self, NumberOfContainers: UInt32, ContainerPaths: POINTER(win32more.Windows.Win32.Foundation.BSTR), ReadPlanEntries: POINTER(UInt32), ReadPlan: POINTER(POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DEDUP_CONTAINER_EXTENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PreviewContainerRead(self, FileFullPath: win32more.Windows.Win32.Foundation.BSTR, NumberOfReads: UInt32, ReadOffsets: POINTER(win32more.Windows.Win32.Storage.DataDeduplication.DDP_FILE_EXTENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
