from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.Compression
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
COMPRESS_ALGORITHM_INVALID = 0
COMPRESS_ALGORITHM_NULL = 1
COMPRESS_ALGORITHM_MAX = 6
COMPRESS_RAW = 536870912
def _define_CreateCompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESS_ALGORITHM,POINTER(win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head),POINTER(IntPtr))(('CreateCompressor', windll['Cabinet.dll']), ((1, 'Algorithm'),(1, 'AllocationRoutines'),(1, 'CompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr)(('SetCompressorInformation', windll['Cabinet.dll']), ((1, 'CompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryCompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr)(('QueryCompressorInformation', windll['Cabinet.dll']), ((1, 'CompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Compress():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE,c_void_p,UIntPtr,c_void_p,UIntPtr,POINTER(UIntPtr))(('Compress', windll['Cabinet.dll']), ((1, 'CompressorHandle'),(1, 'UncompressedData'),(1, 'UncompressedDataSize'),(1, 'CompressedBuffer'),(1, 'CompressedBufferSize'),(1, 'CompressedDataSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetCompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE)(('ResetCompressor', windll['Cabinet.dll']), ((1, 'CompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseCompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESSOR_HANDLE)(('CloseCompressor', windll['Cabinet.dll']), ((1, 'CompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDecompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.Compression.COMPRESS_ALGORITHM,POINTER(win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head),POINTER(IntPtr))(('CreateDecompressor', windll['Cabinet.dll']), ((1, 'Algorithm'),(1, 'AllocationRoutines'),(1, 'DecompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDecompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr)(('SetDecompressorInformation', windll['Cabinet.dll']), ((1, 'DecompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryDecompressorInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS,c_void_p,UIntPtr)(('QueryDecompressorInformation', windll['Cabinet.dll']), ((1, 'DecompressorHandle'),(1, 'CompressInformationClass'),(1, 'CompressInformation'),(1, 'CompressInformationSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Decompress():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,UIntPtr,c_void_p,UIntPtr,POINTER(UIntPtr))(('Decompress', windll['Cabinet.dll']), ((1, 'DecompressorHandle'),(1, 'CompressedData'),(1, 'CompressedDataSize'),(1, 'UncompressedBuffer'),(1, 'UncompressedBufferSize'),(1, 'UncompressedDataSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetDecompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr)(('ResetDecompressor', windll['Cabinet.dll']), ((1, 'DecompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseDecompressor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr)(('CloseDecompressor', windll['Cabinet.dll']), ((1, 'DecompressorHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
COMPRESS_ALGORITHM = UInt32
COMPRESS_ALGORITHM_MSZIP = 2
COMPRESS_ALGORITHM_XPRESS = 3
COMPRESS_ALGORITHM_XPRESS_HUFF = 4
COMPRESS_ALGORITHM_LZMS = 5
def _define_COMPRESS_ALLOCATION_ROUTINES_head():
    class COMPRESS_ALLOCATION_ROUTINES(Structure):
        pass
    return COMPRESS_ALLOCATION_ROUTINES
def _define_COMPRESS_ALLOCATION_ROUTINES():
    COMPRESS_ALLOCATION_ROUTINES = win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head
    COMPRESS_ALLOCATION_ROUTINES._fields_ = [
        ('Allocate', win32more.Storage.Compression.PFN_COMPRESS_ALLOCATE),
        ('Free', win32more.Storage.Compression.PFN_COMPRESS_FREE),
        ('UserContext', c_void_p),
    ]
    return COMPRESS_ALLOCATION_ROUTINES
COMPRESS_INFORMATION_CLASS = Int32
COMPRESS_INFORMATION_CLASS_INVALID = 0
COMPRESS_INFORMATION_CLASS_BLOCK_SIZE = 1
COMPRESS_INFORMATION_CLASS_LEVEL = 2
COMPRESSOR_HANDLE = IntPtr
def _define_PFN_COMPRESS_ALLOCATE():
    return CFUNCTYPE(c_void_p,c_void_p,UIntPtr)
def _define_PFN_COMPRESS_FREE():
    return CFUNCTYPE(Void,c_void_p,c_void_p)
__all__ = [
    "COMPRESSOR_HANDLE",
    "COMPRESS_ALGORITHM",
    "COMPRESS_ALGORITHM_INVALID",
    "COMPRESS_ALGORITHM_LZMS",
    "COMPRESS_ALGORITHM_MAX",
    "COMPRESS_ALGORITHM_MSZIP",
    "COMPRESS_ALGORITHM_NULL",
    "COMPRESS_ALGORITHM_XPRESS",
    "COMPRESS_ALGORITHM_XPRESS_HUFF",
    "COMPRESS_ALLOCATION_ROUTINES",
    "COMPRESS_INFORMATION_CLASS",
    "COMPRESS_INFORMATION_CLASS_BLOCK_SIZE",
    "COMPRESS_INFORMATION_CLASS_INVALID",
    "COMPRESS_INFORMATION_CLASS_LEVEL",
    "COMPRESS_RAW",
    "CloseCompressor",
    "CloseDecompressor",
    "Compress",
    "CreateCompressor",
    "CreateDecompressor",
    "Decompress",
    "PFN_COMPRESS_ALLOCATE",
    "PFN_COMPRESS_FREE",
    "QueryCompressorInformation",
    "QueryDecompressorInformation",
    "ResetCompressor",
    "ResetDecompressor",
    "SetCompressorInformation",
    "SetDecompressorInformation",
]
