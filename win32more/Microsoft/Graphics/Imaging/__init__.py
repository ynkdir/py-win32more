from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Graphics.Imaging
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
class IImageBuffer(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Graphics.Imaging.IImageBuffer'
    _iid_ = Guid('{3baabd0b-1854-51f1-bd2a-74c87858f461}')
    @winrt_commethod(6)
    def get_Buffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_PixelFormat(self) -> win32more.Microsoft.Graphics.Imaging.ImageBufferPixelFormat: ...
    @winrt_commethod(8)
    def get_PixelHeight(self) -> Int32: ...
    @winrt_commethod(9)
    def get_PixelWidth(self) -> Int32: ...
    @winrt_commethod(10)
    def get_RowStride(self) -> Int32: ...
    @winrt_commethod(11)
    def CopyToByteArray(self, values: FillArray[Byte]) -> Void: ...
    @winrt_commethod(12)
    def CopyToSoftwareBitmap(self) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    Buffer = property(get_Buffer, None)
    PixelFormat = property(get_PixelFormat, None)
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
    RowStride = property(get_RowStride, None)
class IImageBufferStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Graphics.Imaging.IImageBufferStatics'
    _iid_ = Guid('{35b17bd3-f346-529f-8c0f-3bf96c56eb13}')
    @winrt_commethod(6)
    def CreateForBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer, pixelFormat: win32more.Microsoft.Graphics.Imaging.ImageBufferPixelFormat, width: Int32, height: Int32, rowStride: Int32) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    @winrt_commethod(7)
    def CreateForSoftwareBitmap(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
class ImageBuffer(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Imaging.IImageBuffer
    _classid_ = 'Microsoft.Graphics.Imaging.ImageBuffer'
    @winrt_mixinmethod
    def get_Buffer(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer) -> win32more.Microsoft.Graphics.Imaging.ImageBufferPixelFormat: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer) -> Int32: ...
    @winrt_mixinmethod
    def get_RowStride(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer) -> Int32: ...
    @winrt_mixinmethod
    def CopyToByteArray(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer, values: FillArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def CopyToSoftwareBitmap(self: win32more.Microsoft.Graphics.Imaging.IImageBuffer) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForBuffer(cls: win32more.Microsoft.Graphics.Imaging.IImageBufferStatics, buffer: win32more.Windows.Storage.Streams.IBuffer, pixelFormat: win32more.Microsoft.Graphics.Imaging.ImageBufferPixelFormat, width: Int32, height: Int32, rowStride: Int32) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    @winrt_classmethod
    def CreateForSoftwareBitmap(cls: win32more.Microsoft.Graphics.Imaging.IImageBufferStatics, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    Buffer = property(get_Buffer, None)
    PixelFormat = property(get_PixelFormat, None)
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
    RowStride = property(get_RowStride, None)
ImageBufferContract: UInt32 = 65536
class ImageBufferPixelFormat(Enum, Int32):
    Rgb8 = 137224
    Rgba8 = 30
    Argb8 = 2498570
    Bgra8 = 87
    Gray8 = 62


make_ready(__name__)
