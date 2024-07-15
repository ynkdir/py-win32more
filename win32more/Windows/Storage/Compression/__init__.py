from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Storage.Compression
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class CompressAlgorithm(Enum, Int32):
    InvalidAlgorithm = 0
    NullAlgorithm = 1
    Mszip = 2
    Xpress = 3
    XpressHuff = 4
    Lzms = 5
class Compressor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Storage.Compression.ICompressor
    _classid_ = 'Windows.Storage.Compression.Compressor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Storage.Compression.Compressor.CreateCompressor(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Storage.Compression.Compressor.CreateCompressorEx(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateCompressor(cls: win32more.Windows.Storage.Compression.ICompressorFactory, underlyingStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Storage.Compression.Compressor: ...
    @winrt_factorymethod
    def CreateCompressorEx(cls: win32more.Windows.Storage.Compression.ICompressorFactory, underlyingStream: win32more.Windows.Storage.Streams.IOutputStream, algorithm: win32more.Windows.Storage.Compression.CompressAlgorithm, blockSize: UInt32) -> win32more.Windows.Storage.Compression.Compressor: ...
    @winrt_mixinmethod
    def FinishAsync(self: win32more.Windows.Storage.Compression.ICompressor) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def DetachStream(self: win32more.Windows.Storage.Compression.ICompressor) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class Decompressor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Storage.Compression.IDecompressor
    _classid_ = 'Windows.Storage.Compression.Decompressor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Storage.Compression.Decompressor.CreateDecompressor(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateDecompressor(cls: win32more.Windows.Storage.Compression.IDecompressorFactory, underlyingStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Storage.Compression.Decompressor: ...
    @winrt_mixinmethod
    def DetachStream(self: win32more.Windows.Storage.Compression.IDecompressor) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Storage.Streams.IInputStream, buffer: win32more.Windows.Storage.Streams.IBuffer, count: UInt32, options: win32more.Windows.Storage.Streams.InputStreamOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class ICompressor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Storage.Compression.ICompressor'
    _iid_ = Guid('{0ac3645a-57ac-4ee1-b702-84d39d5424e0}')
    @winrt_commethod(6)
    def FinishAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def DetachStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
class ICompressorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Compression.ICompressorFactory'
    _iid_ = Guid('{5f3d96a4-2cfb-442c-a8ba-d7d11b039da0}')
    @winrt_commethod(6)
    def CreateCompressor(self, underlyingStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Storage.Compression.Compressor: ...
    @winrt_commethod(7)
    def CreateCompressorEx(self, underlyingStream: win32more.Windows.Storage.Streams.IOutputStream, algorithm: win32more.Windows.Storage.Compression.CompressAlgorithm, blockSize: UInt32) -> win32more.Windows.Storage.Compression.Compressor: ...
class IDecompressor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Storage.Compression.IDecompressor'
    _iid_ = Guid('{b883fe46-d68a-4c8b-ada0-4ee813fc5283}')
    @winrt_commethod(6)
    def DetachStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
class IDecompressorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Compression.IDecompressorFactory'
    _iid_ = Guid('{5337e252-1da2-42e1-8834-0379d28d742f}')
    @winrt_commethod(6)
    def CreateDecompressor(self, underlyingStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Storage.Compression.Decompressor: ...


make_ready(__name__)
