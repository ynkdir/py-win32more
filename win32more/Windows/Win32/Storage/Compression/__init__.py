from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Compression
COMPRESS_ALGORITHM_INVALID: UInt32 = 0
COMPRESS_ALGORITHM_NULL: UInt32 = 1
COMPRESS_ALGORITHM_MAX: UInt32 = 6
COMPRESS_RAW: UInt32 = 536870912
@winfunctype('Cabinet.dll')
def CreateCompressor(Algorithm: win32more.Windows.Win32.Storage.Compression.COMPRESS_ALGORITHM, AllocationRoutines: POINTER(win32more.Windows.Win32.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES), CompressorHandle: POINTER(win32more.Windows.Win32.Storage.Compression.COMPRESSOR_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def SetCompressorInformation(CompressorHandle: win32more.Windows.Win32.Storage.Compression.COMPRESSOR_HANDLE, CompressInformationClass: win32more.Windows.Win32.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: VoidPtr, CompressInformationSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def QueryCompressorInformation(CompressorHandle: win32more.Windows.Win32.Storage.Compression.COMPRESSOR_HANDLE, CompressInformationClass: win32more.Windows.Win32.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: VoidPtr, CompressInformationSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def Compress(CompressorHandle: win32more.Windows.Win32.Storage.Compression.COMPRESSOR_HANDLE, UncompressedData: VoidPtr, UncompressedDataSize: UIntPtr, CompressedBuffer: VoidPtr, CompressedBufferSize: UIntPtr, CompressedDataSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def ResetCompressor(CompressorHandle: win32more.Windows.Win32.Storage.Compression.COMPRESSOR_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def CloseCompressor(CompressorHandle: win32more.Windows.Win32.Storage.Compression.COMPRESSOR_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def CreateDecompressor(Algorithm: win32more.Windows.Win32.Storage.Compression.COMPRESS_ALGORITHM, AllocationRoutines: POINTER(win32more.Windows.Win32.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES), DecompressorHandle: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def SetDecompressorInformation(DecompressorHandle: IntPtr, CompressInformationClass: win32more.Windows.Win32.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: VoidPtr, CompressInformationSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def QueryDecompressorInformation(DecompressorHandle: IntPtr, CompressInformationClass: win32more.Windows.Win32.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: VoidPtr, CompressInformationSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def Decompress(DecompressorHandle: IntPtr, CompressedData: VoidPtr, CompressedDataSize: UIntPtr, UncompressedBuffer: VoidPtr, UncompressedBufferSize: UIntPtr, UncompressedDataSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def ResetDecompressor(DecompressorHandle: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def CloseDecompressor(DecompressorHandle: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
COMPRESSOR_HANDLE = IntPtr
COMPRESS_ALGORITHM = UInt32
COMPRESS_ALGORITHM_MSZIP: COMPRESS_ALGORITHM = 2
COMPRESS_ALGORITHM_XPRESS: COMPRESS_ALGORITHM = 3
COMPRESS_ALGORITHM_XPRESS_HUFF: COMPRESS_ALGORITHM = 4
COMPRESS_ALGORITHM_LZMS: COMPRESS_ALGORITHM = 5
class COMPRESS_ALLOCATION_ROUTINES(EasyCastStructure):
    Allocate: win32more.Windows.Win32.Storage.Compression.PFN_COMPRESS_ALLOCATE
    Free: win32more.Windows.Win32.Storage.Compression.PFN_COMPRESS_FREE
    UserContext: VoidPtr
COMPRESS_INFORMATION_CLASS = Int32
COMPRESS_INFORMATION_CLASS_INVALID: COMPRESS_INFORMATION_CLASS = 0
COMPRESS_INFORMATION_CLASS_BLOCK_SIZE: COMPRESS_INFORMATION_CLASS = 1
COMPRESS_INFORMATION_CLASS_LEVEL: COMPRESS_INFORMATION_CLASS = 2
@cfunctype_pointer
def PFN_COMPRESS_ALLOCATE(UserContext: VoidPtr, Size: UIntPtr) -> VoidPtr: ...
@cfunctype_pointer
def PFN_COMPRESS_FREE(UserContext: VoidPtr, Memory: VoidPtr) -> Void: ...
make_ready(__name__)
