from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.DataDeduplication
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
DEDUP_CHUNKLIB_MAX_CHUNKS_ENUM = 1024
def _define_DDP_FILE_EXTENT_head():
    class DDP_FILE_EXTENT(Structure):
        pass
    return DDP_FILE_EXTENT
def _define_DDP_FILE_EXTENT():
    DDP_FILE_EXTENT = win32more.Storage.DataDeduplication.DDP_FILE_EXTENT_head
    DDP_FILE_EXTENT._fields_ = [
        ('Length', Int64),
        ('Offset', Int64),
    ]
    return DDP_FILE_EXTENT
DEDUP_BACKUP_SUPPORT_PARAM_TYPE = Int32
DEDUP_RECONSTRUCT_UNOPTIMIZED = 1
DEDUP_RECONSTRUCT_OPTIMIZED = 2
def _define_DEDUP_CHUNK_INFO_HASH32_head():
    class DEDUP_CHUNK_INFO_HASH32(Structure):
        pass
    return DEDUP_CHUNK_INFO_HASH32
def _define_DEDUP_CHUNK_INFO_HASH32():
    DEDUP_CHUNK_INFO_HASH32 = win32more.Storage.DataDeduplication.DEDUP_CHUNK_INFO_HASH32_head
    DEDUP_CHUNK_INFO_HASH32._fields_ = [
        ('ChunkFlags', UInt32),
        ('ChunkOffsetInStream', UInt64),
        ('ChunkSize', UInt64),
        ('HashVal', Byte * 32),
    ]
    return DEDUP_CHUNK_INFO_HASH32
def _define_DEDUP_CONTAINER_EXTENT_head():
    class DEDUP_CONTAINER_EXTENT(Structure):
        pass
    return DEDUP_CONTAINER_EXTENT
def _define_DEDUP_CONTAINER_EXTENT():
    DEDUP_CONTAINER_EXTENT = win32more.Storage.DataDeduplication.DEDUP_CONTAINER_EXTENT_head
    DEDUP_CONTAINER_EXTENT._fields_ = [
        ('ContainerIndex', UInt32),
        ('StartOffset', Int64),
        ('Length', Int64),
    ]
    return DEDUP_CONTAINER_EXTENT
DEDUP_SET_PARAM_TYPE = Int32
DEDUP_PT_MinChunkSizeBytes = 1
DEDUP_PT_MaxChunkSizeBytes = 2
DEDUP_PT_AvgChunkSizeBytes = 3
DEDUP_PT_InvariantChunking = 4
DEDUP_PT_DisableStrongHashComputation = 5
DedupBackupSupport = Guid('73d6b2ad-2984-4715-b2-e3-92-4c-14-97-44-dd')
def _define_DedupChunk_head():
    class DedupChunk(Structure):
        pass
    return DedupChunk
def _define_DedupChunk():
    DedupChunk = win32more.Storage.DataDeduplication.DedupChunk_head
    DedupChunk._fields_ = [
        ('Hash', win32more.Storage.DataDeduplication.DedupHash),
        ('Flags', win32more.Storage.DataDeduplication.DedupChunkFlags),
        ('LogicalSize', UInt32),
        ('DataSize', UInt32),
    ]
    return DedupChunk
DedupChunkFlags = Int32
DedupChunkFlags_None = 0
DedupChunkFlags_Compressed = 1
DedupChunkingAlgorithm = Int32
DedupChunkingAlgorithm_Unknonwn = 0
DedupChunkingAlgorithm_V1 = 1
DedupCompressionAlgorithm = Int32
DedupCompressionAlgorithm_Unknonwn = 0
DedupCompressionAlgorithm_Xpress = 1
DedupDataPort = Guid('8f107207-1829-48b2-a6-4b-e6-1f-8e-0d-9a-cb')
DedupDataPortManagerOption = Int32
DedupDataPortManagerOption_None = 0
DedupDataPortManagerOption_AutoStart = 1
DedupDataPortManagerOption_SkipReconciliation = 2
DedupDataPortRequestStatus = Int32
DedupDataPortRequestStatus_Unknown = 0
DedupDataPortRequestStatus_Queued = 1
DedupDataPortRequestStatus_Processing = 2
DedupDataPortRequestStatus_Partial = 3
DedupDataPortRequestStatus_Complete = 4
DedupDataPortRequestStatus_Failed = 5
DedupDataPortVolumeStatus = Int32
DedupDataPortVolumeStatus_Unknown = 0
DedupDataPortVolumeStatus_NotEnabled = 1
DedupDataPortVolumeStatus_NotAvailable = 2
DedupDataPortVolumeStatus_Initializing = 3
DedupDataPortVolumeStatus_Ready = 4
DedupDataPortVolumeStatus_Maintenance = 5
DedupDataPortVolumeStatus_Shutdown = 6
def _define_DedupHash_head():
    class DedupHash(Structure):
        pass
    return DedupHash
def _define_DedupHash():
    DedupHash = win32more.Storage.DataDeduplication.DedupHash_head
    DedupHash._fields_ = [
        ('Hash', Byte * 32),
    ]
    return DedupHash
DedupHashingAlgorithm = Int32
DedupHashingAlgorithm_Unknonwn = 0
DedupHashingAlgorithm_V1 = 1
def _define_DedupStream_head():
    class DedupStream(Structure):
        pass
    return DedupStream
def _define_DedupStream():
    DedupStream = win32more.Storage.DataDeduplication.DedupStream_head
    DedupStream._fields_ = [
        ('Path', win32more.Foundation.BSTR),
        ('Offset', UInt64),
        ('Length', UInt64),
        ('ChunkCount', UInt32),
    ]
    return DedupStream
def _define_DedupStreamEntry_head():
    class DedupStreamEntry(Structure):
        pass
    return DedupStreamEntry
def _define_DedupStreamEntry():
    DedupStreamEntry = win32more.Storage.DataDeduplication.DedupStreamEntry_head
    DedupStreamEntry._fields_ = [
        ('Hash', win32more.Storage.DataDeduplication.DedupHash),
        ('LogicalSize', UInt32),
        ('Offset', UInt64),
    ]
    return DedupStreamEntry
def _define_IDedupBackupSupport_head():
    class IDedupBackupSupport(win32more.System.Com.IUnknown_head):
        Guid = Guid('c719d963-2b2d-415e-ac-f7-7e-b7-ca-59-6f-f4')
    return IDedupBackupSupport
def _define_IDedupBackupSupport():
    IDedupBackupSupport = win32more.Storage.DataDeduplication.IDedupBackupSupport_head
    IDedupBackupSupport.RestoreFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),win32more.Storage.DataDeduplication.IDedupReadFileCallback_head,UInt32,POINTER(win32more.Foundation.HRESULT))(3, 'RestoreFiles', ((1, 'NumberOfFiles'),(1, 'FileFullPaths'),(1, 'Store'),(1, 'Flags'),(1, 'FileResults'),)))
    win32more.System.Com.IUnknown
    return IDedupBackupSupport
def _define_IDedupChunkLibrary_head():
    class IDedupChunkLibrary(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb5144d7-2720-4dcc-87-77-78-59-74-16-ec-23')
    return IDedupChunkLibrary
def _define_IDedupChunkLibrary():
    IDedupChunkLibrary = win32more.Storage.DataDeduplication.IDedupChunkLibrary_head
    IDedupChunkLibrary.InitializeForPushBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'InitializeForPushBuffers', ()))
    IDedupChunkLibrary.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Uninitialize', ()))
    IDedupChunkLibrary.SetParameter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.VARIANT)(5, 'SetParameter', ((1, 'dwParamType'),(1, 'vParamValue'),)))
    IDedupChunkLibrary.StartChunking = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.System.Com.IUnknown_head))(6, 'StartChunking', ((1, 'iidIteratorInterfaceID'),(1, 'ppChunksEnum'),)))
    win32more.System.Com.IUnknown
    return IDedupChunkLibrary
def _define_IDedupDataPort_head():
    class IDedupDataPort(win32more.System.Com.IUnknown_head):
        Guid = Guid('7963d734-40a9-4ea3-bb-f6-5a-89-d2-6f-7a-e8')
    return IDedupDataPort
def _define_IDedupDataPort():
    IDedupDataPort = win32more.Storage.DataDeduplication.IDedupDataPort_head
    IDedupDataPort.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.DataDeduplication.DedupDataPortVolumeStatus),POINTER(UInt32))(3, 'GetStatus', ((1, 'pStatus'),(1, 'pDataHeadroomMb'),)))
    IDedupDataPort.LookupChunks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DedupHash_head),POINTER(Guid))(4, 'LookupChunks', ((1, 'Count'),(1, 'pHashes'),(1, 'pRequestId'),)))
    IDedupDataPort.InsertChunks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DedupChunk_head),UInt32,c_char_p_no,POINTER(Guid))(5, 'InsertChunks', ((1, 'ChunkCount'),(1, 'pChunkMetadata'),(1, 'DataByteCount'),(1, 'pChunkData'),(1, 'pRequestId'),)))
    IDedupDataPort.InsertChunksWithStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DedupChunk_head),UInt32,win32more.System.Com.IStream_head,POINTER(Guid))(6, 'InsertChunksWithStream', ((1, 'ChunkCount'),(1, 'pChunkMetadata'),(1, 'DataByteCount'),(1, 'pChunkDataStream'),(1, 'pRequestId'),)))
    IDedupDataPort.CommitStreams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DedupStream_head),UInt32,POINTER(win32more.Storage.DataDeduplication.DedupStreamEntry_head),POINTER(Guid))(7, 'CommitStreams', ((1, 'StreamCount'),(1, 'pStreams'),(1, 'EntryCount'),(1, 'pEntries'),(1, 'pRequestId'),)))
    IDedupDataPort.CommitStreamsWithStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DedupStream_head),UInt32,win32more.System.Com.IStream_head,POINTER(Guid))(8, 'CommitStreamsWithStream', ((1, 'StreamCount'),(1, 'pStreams'),(1, 'EntryCount'),(1, 'pEntriesStream'),(1, 'pRequestId'),)))
    IDedupDataPort.GetStreams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(Guid))(9, 'GetStreams', ((1, 'StreamCount'),(1, 'pStreamPaths'),(1, 'pRequestId'),)))
    IDedupDataPort.GetStreamsResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Storage.DataDeduplication.DedupStream_head)),POINTER(UInt32),POINTER(POINTER(win32more.Storage.DataDeduplication.DedupStreamEntry_head)),POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus),POINTER(POINTER(win32more.Foundation.HRESULT)))(10, 'GetStreamsResults', ((1, 'RequestId'),(1, 'MaxWaitMs'),(1, 'StreamEntryIndex'),(1, 'pStreamCount'),(1, 'ppStreams'),(1, 'pEntryCount'),(1, 'ppEntries'),(1, 'pStatus'),(1, 'ppItemResults'),)))
    IDedupDataPort.GetChunks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DedupHash_head),POINTER(Guid))(11, 'GetChunks', ((1, 'Count'),(1, 'pHashes'),(1, 'pRequestId'),)))
    IDedupDataPort.GetChunksResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Storage.DataDeduplication.DedupChunk_head)),POINTER(UInt32),POINTER(c_char_p_no),POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus),POINTER(POINTER(win32more.Foundation.HRESULT)))(12, 'GetChunksResults', ((1, 'RequestId'),(1, 'MaxWaitMs'),(1, 'ChunkIndex'),(1, 'pChunkCount'),(1, 'ppChunkMetadata'),(1, 'pDataByteCount'),(1, 'ppChunkData'),(1, 'pStatus'),(1, 'ppItemResults'),)))
    IDedupDataPort.GetRequestStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus))(13, 'GetRequestStatus', ((1, 'RequestId'),(1, 'pStatus'),)))
    IDedupDataPort.GetRequestResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,POINTER(win32more.Foundation.HRESULT),POINTER(UInt32),POINTER(win32more.Storage.DataDeduplication.DedupDataPortRequestStatus),POINTER(POINTER(win32more.Foundation.HRESULT)))(14, 'GetRequestResults', ((1, 'RequestId'),(1, 'MaxWaitMs'),(1, 'pBatchResult'),(1, 'pBatchCount'),(1, 'pStatus'),(1, 'ppItemResults'),)))
    win32more.System.Com.IUnknown
    return IDedupDataPort
def _define_IDedupDataPortManager_head():
    class IDedupDataPortManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('44677452-b90a-445e-81-92-cd-cf-e8-15-11-fb')
    return IDedupDataPortManager
def _define_IDedupDataPortManager():
    IDedupDataPortManager = win32more.Storage.DataDeduplication.IDedupDataPortManager_head
    IDedupDataPortManager.GetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Storage.DataDeduplication.DedupChunkingAlgorithm),POINTER(win32more.Storage.DataDeduplication.DedupHashingAlgorithm),POINTER(win32more.Storage.DataDeduplication.DedupCompressionAlgorithm))(3, 'GetConfiguration', ((1, 'pMinChunkSize'),(1, 'pMaxChunkSize'),(1, 'pChunkingAlgorithm'),(1, 'pHashingAlgorithm'),(1, 'pCompressionAlgorithm'),)))
    IDedupDataPortManager.GetVolumeStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR,POINTER(win32more.Storage.DataDeduplication.DedupDataPortVolumeStatus))(4, 'GetVolumeStatus', ((1, 'Options'),(1, 'Path'),(1, 'pStatus'),)))
    IDedupDataPortManager.GetVolumeDataPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR,POINTER(win32more.Storage.DataDeduplication.IDedupDataPort_head))(5, 'GetVolumeDataPort', ((1, 'Options'),(1, 'Path'),(1, 'ppDataPort'),)))
    win32more.System.Com.IUnknown
    return IDedupDataPortManager
def _define_IDedupIterateChunksHash32_head():
    class IDedupIterateChunksHash32(win32more.System.Com.IUnknown_head):
        Guid = Guid('90b584d3-72aa-400f-97-67-ca-d8-66-a5-a2-d8')
    return IDedupIterateChunksHash32
def _define_IDedupIterateChunksHash32():
    IDedupIterateChunksHash32 = win32more.Storage.DataDeduplication.IDedupIterateChunksHash32_head
    IDedupIterateChunksHash32.PushBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(3, 'PushBuffer', ((1, 'pBuffer'),(1, 'ulBufferLength'),)))
    IDedupIterateChunksHash32.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.DataDeduplication.DEDUP_CHUNK_INFO_HASH32_head),POINTER(UInt32))(4, 'Next', ((1, 'ulMaxChunks'),(1, 'pArrChunks'),(1, 'pulFetched'),)))
    IDedupIterateChunksHash32.Drain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Drain', ()))
    IDedupIterateChunksHash32.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Reset', ()))
    win32more.System.Com.IUnknown
    return IDedupIterateChunksHash32
def _define_IDedupReadFileCallback_head():
    class IDedupReadFileCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('7bacc67a-2f1d-42d0-89-7e-6f-f6-2d-d5-33-bb')
    return IDedupReadFileCallback
def _define_IDedupReadFileCallback():
    IDedupReadFileCallback = win32more.Storage.DataDeduplication.IDedupReadFileCallback_head
    IDedupReadFileCallback.ReadBackupFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int64,UInt32,c_char_p_no,POINTER(UInt32),UInt32)(3, 'ReadBackupFile', ((1, 'FileFullPath'),(1, 'FileOffset'),(1, 'SizeToRead'),(1, 'FileBuffer'),(1, 'ReturnedSize'),(1, 'Flags'),)))
    IDedupReadFileCallback.OrderContainersRestore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(POINTER(win32more.Storage.DataDeduplication.DEDUP_CONTAINER_EXTENT_head)))(4, 'OrderContainersRestore', ((1, 'NumberOfContainers'),(1, 'ContainerPaths'),(1, 'ReadPlanEntries'),(1, 'ReadPlan'),)))
    IDedupReadFileCallback.PreviewContainerRead = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(win32more.Storage.DataDeduplication.DDP_FILE_EXTENT_head))(5, 'PreviewContainerRead', ((1, 'FileFullPath'),(1, 'NumberOfReads'),(1, 'ReadOffsets'),)))
    win32more.System.Com.IUnknown
    return IDedupReadFileCallback
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
