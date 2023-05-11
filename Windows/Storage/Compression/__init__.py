from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Storage.Compression
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CompressAlgorithm = Int32
CompressAlgorithm_InvalidAlgorithm: CompressAlgorithm = 0
CompressAlgorithm_NullAlgorithm: CompressAlgorithm = 1
CompressAlgorithm_Mszip: CompressAlgorithm = 2
CompressAlgorithm_Xpress: CompressAlgorithm = 3
CompressAlgorithm_XpressHuff: CompressAlgorithm = 4
CompressAlgorithm_Lzms: CompressAlgorithm = 5
class Compressor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Compression.ICompressor
    _classid_ = 'Windows.Storage.Compression.Compressor'
    @winrt_factorymethod
    def CreateCompressor(cls: Windows.Storage.Compression.ICompressorFactory, underlyingStream: Windows.Storage.Streams.IOutputStream) -> Windows.Storage.Compression.Compressor: ...
    @winrt_factorymethod
    def CreateCompressorEx(cls: Windows.Storage.Compression.ICompressorFactory, underlyingStream: Windows.Storage.Streams.IOutputStream, algorithm: Windows.Storage.Compression.CompressAlgorithm, blockSize: UInt32) -> Windows.Storage.Compression.Compressor: ...
    @winrt_mixinmethod
    def FinishAsync(self: Windows.Storage.Compression.ICompressor) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def DetachStream(self: Windows.Storage.Compression.ICompressor) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def WriteAsync(self: Windows.Storage.Streams.IOutputStream, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class Decompressor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Compression.IDecompressor
    _classid_ = 'Windows.Storage.Compression.Decompressor'
    @winrt_factorymethod
    def CreateDecompressor(cls: Windows.Storage.Compression.IDecompressorFactory, underlyingStream: Windows.Storage.Streams.IInputStream) -> Windows.Storage.Compression.Decompressor: ...
    @winrt_mixinmethod
    def DetachStream(self: Windows.Storage.Compression.IDecompressor) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def ReadAsync(self: Windows.Storage.Streams.IInputStream, buffer: Windows.Storage.Streams.IBuffer, count: UInt32, options: Windows.Storage.Streams.InputStreamOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class ICompressor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Compression.ICompressor'
    _iid_ = Guid('{0ac3645a-57ac-4ee1-b702-84d39d5424e0}')
    @winrt_commethod(6)
    def FinishAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def DetachStream(self) -> Windows.Storage.Streams.IOutputStream: ...
class ICompressorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Compression.ICompressorFactory'
    _iid_ = Guid('{5f3d96a4-2cfb-442c-a8ba-d7d11b039da0}')
    @winrt_commethod(6)
    def CreateCompressor(self, underlyingStream: Windows.Storage.Streams.IOutputStream) -> Windows.Storage.Compression.Compressor: ...
    @winrt_commethod(7)
    def CreateCompressorEx(self, underlyingStream: Windows.Storage.Streams.IOutputStream, algorithm: Windows.Storage.Compression.CompressAlgorithm, blockSize: UInt32) -> Windows.Storage.Compression.Compressor: ...
class IDecompressor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Compression.IDecompressor'
    _iid_ = Guid('{b883fe46-d68a-4c8b-ada0-4ee813fc5283}')
    @winrt_commethod(6)
    def DetachStream(self) -> Windows.Storage.Streams.IInputStream: ...
class IDecompressorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Compression.IDecompressorFactory'
    _iid_ = Guid('{5337e252-1da2-42e1-8834-0379d28d742f}')
    @winrt_commethod(6)
    def CreateDecompressor(self, underlyingStream: Windows.Storage.Streams.IInputStream) -> Windows.Storage.Compression.Decompressor: ...
make_head(_module, 'Compressor')
make_head(_module, 'Decompressor')
make_head(_module, 'ICompressor')
make_head(_module, 'ICompressorFactory')
make_head(_module, 'IDecompressor')
make_head(_module, 'IDecompressorFactory')
