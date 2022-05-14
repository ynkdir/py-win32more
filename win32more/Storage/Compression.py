from win32more import *
import win32more.Storage.Compression
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Storage.Compression, name, eval(f"_define_{name}()"))
    return getattr(win32more.Storage.Compression, name)
COMPRESS_ALGORITHM_INVALID = 0
COMPRESS_ALGORITHM_NULL = 1
COMPRESS_ALGORITHM_MAX = 6
COMPRESS_RAW = 536870912
COMPRESS_ALGORITHM = UInt32
COMPRESS_ALGORITHM_MSZIP = 2
COMPRESS_ALGORITHM_XPRESS = 3
COMPRESS_ALGORITHM_XPRESS_HUFF = 4
COMPRESS_ALGORITHM_LZMS = 5
COMPRESSOR_HANDLE = IntPtr
def _define_PFN_COMPRESS_ALLOCATE():
    return CFUNCTYPE(c_void_p,c_void_p,UIntPtr, use_last_error=False)
def _define_PFN_COMPRESS_FREE():
    return CFUNCTYPE(Void,c_void_p,c_void_p, use_last_error=False)
def _define_COMPRESS_ALLOCATION_ROUTINES_head():
    class COMPRESS_ALLOCATION_ROUTINES(Structure):
        pass
    return COMPRESS_ALLOCATION_ROUTINES
def _define_COMPRESS_ALLOCATION_ROUTINES():
    COMPRESS_ALLOCATION_ROUTINES = win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head
    COMPRESS_ALLOCATION_ROUTINES._fields_ = [
        ("Allocate", win32more.Storage.Compression.PFN_COMPRESS_ALLOCATE),
        ("Free", win32more.Storage.Compression.PFN_COMPRESS_FREE),
        ("UserContext", c_void_p),
    ]
    return COMPRESS_ALLOCATION_ROUTINES
COMPRESS_INFORMATION_CLASS = Int32
COMPRESS_INFORMATION_CLASS_INVALID = 0
COMPRESS_INFORMATION_CLASS_BLOCK_SIZE = 1
COMPRESS_INFORMATION_CLASS_LEVEL = 2
def _define_CreateCompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESS_ALGORITHM,POINTER(win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head),POINTER(IntPtr), use_last_error=True)(("CreateCompressor", windll["Cabinet"]), ((1, 'Algorithm'),(1, 'AllocationRoutines'),(1, 'CompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr, use_last_error=True)(("SetCompressorInformation", windll["Cabinet"]), ((1, 'CompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryCompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr, use_last_error=True)(("QueryCompressorInformation", windll["Cabinet"]), ((1, 'CompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Compress():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE,c_void_p,UIntPtr,c_void_p,UIntPtr,POINTER(UIntPtr), use_last_error=True)(("Compress", windll["Cabinet"]), ((1, 'CompressorHandle'),(1, 'UncompressedData'),(1, 'UncompressedDataSize'),(1, 'CompressedBuffer'),(1, 'CompressedBufferSize'),(1, 'CompressedDataSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetCompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE, use_last_error=True)(("ResetCompressor", windll["Cabinet"]), ((1, 'CompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseCompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE, use_last_error=True)(("CloseCompressor", windll["Cabinet"]), ((1, 'CompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDecompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESS_ALGORITHM,POINTER(win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head),POINTER(IntPtr), use_last_error=True)(("CreateDecompressor", windll["Cabinet"]), ((1, 'Algorithm'),(1, 'AllocationRoutines'),(1, 'DecompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDecompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr, use_last_error=True)(("SetDecompressorInformation", windll["Cabinet"]), ((1, 'DecompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryDecompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr, use_last_error=True)(("QueryDecompressorInformation", windll["Cabinet"]), ((1, 'DecompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Decompress():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,UIntPtr,c_void_p,UIntPtr,POINTER(UIntPtr), use_last_error=True)(("Decompress", windll["Cabinet"]), ((1, 'DecompressorHandle'),(1, 'CompressedData'),(1, 'CompressedDataSize'),(1, 'UncompressedBuffer'),(1, 'UncompressedBufferSize'),(1, 'UncompressedDataSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetDecompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=True)(("ResetDecompressor", windll["Cabinet"]), ((1, 'DecompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseDecompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=True)(("CloseDecompressor", windll["Cabinet"]), ((1, 'DecompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "COMPRESS_ALGORITHM_INVALID",
    "COMPRESS_ALGORITHM_NULL",
    "COMPRESS_ALGORITHM_MAX",
    "COMPRESS_RAW",
    "COMPRESS_ALGORITHM",
    "COMPRESS_ALGORITHM_MSZIP",
    "COMPRESS_ALGORITHM_XPRESS",
    "COMPRESS_ALGORITHM_XPRESS_HUFF",
    "COMPRESS_ALGORITHM_LZMS",
    "COMPRESSOR_HANDLE",
    "PFN_COMPRESS_ALLOCATE",
    "PFN_COMPRESS_FREE",
    "COMPRESS_ALLOCATION_ROUTINES",
    "COMPRESS_INFORMATION_CLASS",
    "COMPRESS_INFORMATION_CLASS_INVALID",
    "COMPRESS_INFORMATION_CLASS_BLOCK_SIZE",
    "COMPRESS_INFORMATION_CLASS_LEVEL",
    "CreateCompressor",
    "SetCompressorInformation",
    "QueryCompressorInformation",
    "Compress",
    "ResetCompressor",
    "CloseCompressor",
    "CreateDecompressor",
    "SetDecompressorInformation",
    "QueryDecompressorInformation",
    "Decompress",
    "ResetDecompressor",
    "CloseDecompressor",
]
