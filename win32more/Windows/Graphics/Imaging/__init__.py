from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
BitmapAlphaMode = Int32
BitmapAlphaMode_Premultiplied: BitmapAlphaMode = 0
BitmapAlphaMode_Straight: BitmapAlphaMode = 1
BitmapAlphaMode_Ignore: BitmapAlphaMode = 2
class BitmapBounds(EasyCastStructure):
    X: UInt32
    Y: UInt32
    Width: UInt32
    Height: UInt32
class BitmapBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapBuffer
    _classid_ = 'Windows.Graphics.Imaging.BitmapBuffer'
    @winrt_mixinmethod
    def GetPlaneCount(self: win32more.Windows.Graphics.Imaging.IBitmapBuffer) -> Int32: ...
    @winrt_mixinmethod
    def GetPlaneDescription(self: win32more.Windows.Graphics.Imaging.IBitmapBuffer, index: Int32) -> win32more.Windows.Graphics.Imaging.BitmapPlaneDescription: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
BitmapBufferAccessMode = Int32
BitmapBufferAccessMode_Read: BitmapBufferAccessMode = 0
BitmapBufferAccessMode_ReadWrite: BitmapBufferAccessMode = 1
BitmapBufferAccessMode_Write: BitmapBufferAccessMode = 2
class BitmapCodecInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapCodecInformation
    _classid_ = 'Windows.Graphics.Imaging.BitmapCodecInformation'
    @winrt_mixinmethod
    def get_CodecId(self: win32more.Windows.Graphics.Imaging.IBitmapCodecInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_FileExtensions(self: win32more.Windows.Graphics.Imaging.IBitmapCodecInformation) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Graphics.Imaging.IBitmapCodecInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MimeTypes(self: win32more.Windows.Graphics.Imaging.IBitmapCodecInformation) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    CodecId = property(get_CodecId, None)
    FileExtensions = property(get_FileExtensions, None)
    FriendlyName = property(get_FriendlyName, None)
    MimeTypes = property(get_MimeTypes, None)
class _BitmapDecoder_Meta_(ComPtr.__class__):
    pass
class BitmapDecoder(ComPtr, metaclass=_BitmapDecoder_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapDecoder
    _classid_ = 'Windows.Graphics.Imaging.BitmapDecoder'
    @winrt_mixinmethod
    def get_BitmapContainerProperties(self: win32more.Windows.Graphics.Imaging.IBitmapDecoder) -> win32more.Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_mixinmethod
    def get_DecoderInformation(self: win32more.Windows.Graphics.Imaging.IBitmapDecoder) -> win32more.Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_mixinmethod
    def get_FrameCount(self: win32more.Windows.Graphics.Imaging.IBitmapDecoder) -> UInt32: ...
    @winrt_mixinmethod
    def GetPreviewAsync(self: win32more.Windows.Graphics.Imaging.IBitmapDecoder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def GetFrameAsync(self: win32more.Windows.Graphics.Imaging.IBitmapDecoder, frameIndex: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapFrame]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_DpiX(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_DpiY(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelWidth(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelHeight(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def GetPixelDataAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetPixelDataTransformedAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrame, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, transform: win32more.Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: win32more.Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: win32more.Windows.Graphics.Imaging.ColorManagementMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapConvertedAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapTransformedAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, transform: win32more.Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: win32more.Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: win32more.Windows.Graphics.Imaging.ColorManagementMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_classmethod
    def get_HeifDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics2) -> Guid: ...
    @winrt_classmethod
    def get_WebpDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BmpDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_PngDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_TiffDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_GifDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegXRDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_IcoDecoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def GetDecoderInformationEnumerator(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapDecoder]: ...
    @winrt_classmethod
    def CreateWithIdAsync(cls: win32more.Windows.Graphics.Imaging.IBitmapDecoderStatics, decoderId: Guid, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapDecoder]: ...
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    DecoderInformation = property(get_DecoderInformation, None)
    FrameCount = property(get_FrameCount, None)
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    DpiX = property(get_DpiX, None)
    DpiY = property(get_DpiY, None)
    PixelWidth = property(get_PixelWidth, None)
    PixelHeight = property(get_PixelHeight, None)
    OrientedPixelWidth = property(get_OrientedPixelWidth, None)
    OrientedPixelHeight = property(get_OrientedPixelHeight, None)
    _BitmapDecoder_Meta_.HeifDecoderId = property(get_HeifDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.WebpDecoderId = property(get_WebpDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.BmpDecoderId = property(get_BmpDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.JpegDecoderId = property(get_JpegDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.PngDecoderId = property(get_PngDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.TiffDecoderId = property(get_TiffDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.GifDecoderId = property(get_GifDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.JpegXRDecoderId = property(get_JpegXRDecoderId.__wrapped__, None)
    _BitmapDecoder_Meta_.IcoDecoderId = property(get_IcoDecoderId.__wrapped__, None)
class _BitmapEncoder_Meta_(ComPtr.__class__):
    pass
class BitmapEncoder(ComPtr, metaclass=_BitmapEncoder_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapEncoder
    _classid_ = 'Windows.Graphics.Imaging.BitmapEncoder'
    @winrt_mixinmethod
    def get_EncoderInformation(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> win32more.Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> win32more.Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_mixinmethod
    def get_BitmapContainerProperties(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> win32more.Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_mixinmethod
    def get_IsThumbnailGenerated(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsThumbnailGenerated(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_GeneratedThumbnailWidth(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> UInt32: ...
    @winrt_mixinmethod
    def put_GeneratedThumbnailWidth(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_GeneratedThumbnailHeight(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> UInt32: ...
    @winrt_mixinmethod
    def put_GeneratedThumbnailHeight(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BitmapTransform(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> win32more.Windows.Graphics.Imaging.BitmapTransform: ...
    @winrt_mixinmethod
    def SetPixelData(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, width: UInt32, height: UInt32, dpiX: Double, dpiY: Double, pixels: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def GoToNextFrameAsync(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GoToNextFrameWithEncodingOptionsAsync(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder, encodingOptions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Graphics.Imaging.IBitmapEncoder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetSoftwareBitmap(self: win32more.Windows.Graphics.Imaging.IBitmapEncoderWithSoftwareBitmap, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_classmethod
    def get_HeifEncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BmpEncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegEncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_PngEncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_TiffEncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_GifEncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegXREncoderId(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def GetEncoderInformationEnumerator(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics, encoderId: Guid, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_classmethod
    def CreateWithEncodingOptionsAsync(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics, encoderId: Guid, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, encodingOptions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_classmethod
    def CreateForTranscodingAsync(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, bitmapDecoder: win32more.Windows.Graphics.Imaging.BitmapDecoder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_classmethod
    def CreateForInPlacePropertyEncodingAsync(cls: win32more.Windows.Graphics.Imaging.IBitmapEncoderStatics, bitmapDecoder: win32more.Windows.Graphics.Imaging.BitmapDecoder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    EncoderInformation = property(get_EncoderInformation, None)
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    IsThumbnailGenerated = property(get_IsThumbnailGenerated, put_IsThumbnailGenerated)
    GeneratedThumbnailWidth = property(get_GeneratedThumbnailWidth, put_GeneratedThumbnailWidth)
    GeneratedThumbnailHeight = property(get_GeneratedThumbnailHeight, put_GeneratedThumbnailHeight)
    BitmapTransform = property(get_BitmapTransform, None)
    _BitmapEncoder_Meta_.HeifEncoderId = property(get_HeifEncoderId.__wrapped__, None)
    _BitmapEncoder_Meta_.BmpEncoderId = property(get_BmpEncoderId.__wrapped__, None)
    _BitmapEncoder_Meta_.JpegEncoderId = property(get_JpegEncoderId.__wrapped__, None)
    _BitmapEncoder_Meta_.PngEncoderId = property(get_PngEncoderId.__wrapped__, None)
    _BitmapEncoder_Meta_.TiffEncoderId = property(get_TiffEncoderId.__wrapped__, None)
    _BitmapEncoder_Meta_.GifEncoderId = property(get_GifEncoderId.__wrapped__, None)
    _BitmapEncoder_Meta_.JpegXREncoderId = property(get_JpegXREncoderId.__wrapped__, None)
BitmapFlip = Int32
BitmapFlip_None: BitmapFlip = 0
BitmapFlip_Horizontal: BitmapFlip = 1
BitmapFlip_Vertical: BitmapFlip = 2
class BitmapFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapFrame
    _classid_ = 'Windows.Graphics.Imaging.BitmapFrame'
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_DpiX(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_DpiY(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelWidth(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelHeight(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def GetPixelDataAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetPixelDataTransformedAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrame, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, transform: win32more.Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: win32more.Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: win32more.Windows.Graphics.Imaging.ColorManagementMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapConvertedAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapTransformedAsync(self: win32more.Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, transform: win32more.Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: win32more.Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: win32more.Windows.Graphics.Imaging.ColorManagementMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    DpiX = property(get_DpiX, None)
    DpiY = property(get_DpiY, None)
    PixelWidth = property(get_PixelWidth, None)
    PixelHeight = property(get_PixelHeight, None)
    OrientedPixelWidth = property(get_OrientedPixelWidth, None)
    OrientedPixelHeight = property(get_OrientedPixelHeight, None)
BitmapInterpolationMode = Int32
BitmapInterpolationMode_NearestNeighbor: BitmapInterpolationMode = 0
BitmapInterpolationMode_Linear: BitmapInterpolationMode = 1
BitmapInterpolationMode_Cubic: BitmapInterpolationMode = 2
BitmapInterpolationMode_Fant: BitmapInterpolationMode = 3
BitmapPixelFormat = Int32
BitmapPixelFormat_Unknown: BitmapPixelFormat = 0
BitmapPixelFormat_Rgba16: BitmapPixelFormat = 12
BitmapPixelFormat_Rgba8: BitmapPixelFormat = 30
BitmapPixelFormat_Gray16: BitmapPixelFormat = 57
BitmapPixelFormat_Gray8: BitmapPixelFormat = 62
BitmapPixelFormat_Bgra8: BitmapPixelFormat = 87
BitmapPixelFormat_Nv12: BitmapPixelFormat = 103
BitmapPixelFormat_P010: BitmapPixelFormat = 104
BitmapPixelFormat_Yuy2: BitmapPixelFormat = 107
class BitmapPlaneDescription(EasyCastStructure):
    StartIndex: Int32
    Width: Int32
    Height: Int32
    Stride: Int32
class BitmapProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapProperties
    _classid_ = 'Windows.Graphics.Imaging.BitmapProperties'
    @winrt_mixinmethod
    def SetPropertiesAsync(self: win32more.Windows.Graphics.Imaging.IBitmapProperties, propertiesToSet: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: win32more.Windows.Graphics.Imaging.IBitmapPropertiesView, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapPropertySet]: ...
class BitmapPropertiesView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapPropertiesView
    _classid_ = 'Windows.Graphics.Imaging.BitmapPropertiesView'
    @winrt_mixinmethod
    def GetPropertiesAsync(self: win32more.Windows.Graphics.Imaging.IBitmapPropertiesView, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapPropertySet]: ...
class BitmapPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]
    _classid_ = 'Windows.Graphics.Imaging.BitmapPropertySet'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Graphics.Imaging.BitmapPropertySet.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Imaging.BitmapPropertySet: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String) -> win32more.Windows.Graphics.Imaging.BitmapTypedValue: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String, value: win32more.Windows.Graphics.Imaging.BitmapTypedValue) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]: ...
    Size = property(get_Size, None)
BitmapRotation = Int32
BitmapRotation_None: BitmapRotation = 0
BitmapRotation_Clockwise90Degrees: BitmapRotation = 1
BitmapRotation_Clockwise180Degrees: BitmapRotation = 2
BitmapRotation_Clockwise270Degrees: BitmapRotation = 3
class BitmapSize(EasyCastStructure):
    Width: UInt32
    Height: UInt32
class BitmapTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapTransform
    _classid_ = 'Windows.Graphics.Imaging.BitmapTransform'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Graphics.Imaging.BitmapTransform.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Imaging.BitmapTransform: ...
    @winrt_mixinmethod
    def get_ScaledWidth(self: win32more.Windows.Graphics.Imaging.IBitmapTransform) -> UInt32: ...
    @winrt_mixinmethod
    def put_ScaledWidth(self: win32more.Windows.Graphics.Imaging.IBitmapTransform, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ScaledHeight(self: win32more.Windows.Graphics.Imaging.IBitmapTransform) -> UInt32: ...
    @winrt_mixinmethod
    def put_ScaledHeight(self: win32more.Windows.Graphics.Imaging.IBitmapTransform, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_InterpolationMode(self: win32more.Windows.Graphics.Imaging.IBitmapTransform) -> win32more.Windows.Graphics.Imaging.BitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_InterpolationMode(self: win32more.Windows.Graphics.Imaging.IBitmapTransform, value: win32more.Windows.Graphics.Imaging.BitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_Flip(self: win32more.Windows.Graphics.Imaging.IBitmapTransform) -> win32more.Windows.Graphics.Imaging.BitmapFlip: ...
    @winrt_mixinmethod
    def put_Flip(self: win32more.Windows.Graphics.Imaging.IBitmapTransform, value: win32more.Windows.Graphics.Imaging.BitmapFlip) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Windows.Graphics.Imaging.IBitmapTransform) -> win32more.Windows.Graphics.Imaging.BitmapRotation: ...
    @winrt_mixinmethod
    def put_Rotation(self: win32more.Windows.Graphics.Imaging.IBitmapTransform, value: win32more.Windows.Graphics.Imaging.BitmapRotation) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.Graphics.Imaging.IBitmapTransform) -> win32more.Windows.Graphics.Imaging.BitmapBounds: ...
    @winrt_mixinmethod
    def put_Bounds(self: win32more.Windows.Graphics.Imaging.IBitmapTransform, value: win32more.Windows.Graphics.Imaging.BitmapBounds) -> Void: ...
    ScaledWidth = property(get_ScaledWidth, put_ScaledWidth)
    ScaledHeight = property(get_ScaledHeight, put_ScaledHeight)
    InterpolationMode = property(get_InterpolationMode, put_InterpolationMode)
    Flip = property(get_Flip, put_Flip)
    Rotation = property(get_Rotation, put_Rotation)
    Bounds = property(get_Bounds, put_Bounds)
class BitmapTypedValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IBitmapTypedValue
    _classid_ = 'Windows.Graphics.Imaging.BitmapTypedValue'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 2:
            return win32more.Windows.Graphics.Imaging.BitmapTypedValue.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Imaging.IBitmapTypedValueFactory, value: win32more.Windows.Win32.System.WinRT.IInspectable, type: win32more.Windows.Foundation.PropertyType) -> win32more.Windows.Graphics.Imaging.BitmapTypedValue: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Graphics.Imaging.IBitmapTypedValue) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Graphics.Imaging.IBitmapTypedValue) -> win32more.Windows.Foundation.PropertyType: ...
    Value = property(get_Value, None)
    Type = property(get_Type, None)
ColorManagementMode = Int32
ColorManagementMode_DoNotColorManage: ColorManagementMode = 0
ColorManagementMode_ColorManageToSRgb: ColorManagementMode = 1
ExifOrientationMode = Int32
ExifOrientationMode_IgnoreExifOrientation: ExifOrientationMode = 0
ExifOrientationMode_RespectExifOrientation: ExifOrientationMode = 1
class IBitmapBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapBuffer'
    _iid_ = Guid('{a53e04c4-399c-438c-b28f-a63a6b83d1a1}')
    @winrt_commethod(6)
    def GetPlaneCount(self) -> Int32: ...
    @winrt_commethod(7)
    def GetPlaneDescription(self, index: Int32) -> win32more.Windows.Graphics.Imaging.BitmapPlaneDescription: ...
class IBitmapCodecInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapCodecInformation'
    _iid_ = Guid('{400caaf2-c4b0-4392-a3b0-6f6f9ba95cb4}')
    @winrt_commethod(6)
    def get_CodecId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_FileExtensions(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MimeTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    CodecId = property(get_CodecId, None)
    FileExtensions = property(get_FileExtensions, None)
    FriendlyName = property(get_FriendlyName, None)
    MimeTypes = property(get_MimeTypes, None)
class IBitmapDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapDecoder'
    _iid_ = Guid('{acef22ba-1d74-4c91-9dfc-9620745233e6}')
    @winrt_commethod(6)
    def get_BitmapContainerProperties(self) -> win32more.Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_commethod(7)
    def get_DecoderInformation(self) -> win32more.Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_commethod(8)
    def get_FrameCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def GetPreviewAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_commethod(10)
    def GetFrameAsync(self, frameIndex: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapFrame]: ...
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    DecoderInformation = property(get_DecoderInformation, None)
    FrameCount = property(get_FrameCount, None)
class IBitmapDecoderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapDecoderStatics'
    _iid_ = Guid('{438ccb26-bcef-4e95-bad6-23a822e58d01}')
    @winrt_commethod(6)
    def get_BmpDecoderId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_JpegDecoderId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_PngDecoderId(self) -> Guid: ...
    @winrt_commethod(9)
    def get_TiffDecoderId(self) -> Guid: ...
    @winrt_commethod(10)
    def get_GifDecoderId(self) -> Guid: ...
    @winrt_commethod(11)
    def get_JpegXRDecoderId(self) -> Guid: ...
    @winrt_commethod(12)
    def get_IcoDecoderId(self) -> Guid: ...
    @winrt_commethod(13)
    def GetDecoderInformationEnumerator(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_commethod(14)
    def CreateAsync(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapDecoder]: ...
    @winrt_commethod(15)
    def CreateWithIdAsync(self, decoderId: Guid, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapDecoder]: ...
    BmpDecoderId = property(get_BmpDecoderId, None)
    JpegDecoderId = property(get_JpegDecoderId, None)
    PngDecoderId = property(get_PngDecoderId, None)
    TiffDecoderId = property(get_TiffDecoderId, None)
    GifDecoderId = property(get_GifDecoderId, None)
    JpegXRDecoderId = property(get_JpegXRDecoderId, None)
    IcoDecoderId = property(get_IcoDecoderId, None)
class IBitmapDecoderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapDecoderStatics2'
    _iid_ = Guid('{50ba68ea-99a1-40c4-80d9-aef0dafa6c3f}')
    @winrt_commethod(6)
    def get_HeifDecoderId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_WebpDecoderId(self) -> Guid: ...
    HeifDecoderId = property(get_HeifDecoderId, None)
    WebpDecoderId = property(get_WebpDecoderId, None)
class IBitmapEncoder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapEncoder'
    _iid_ = Guid('{2bc468e3-e1f8-4b54-95e8-32919551ce62}')
    @winrt_commethod(6)
    def get_EncoderInformation(self) -> win32more.Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_commethod(7)
    def get_BitmapProperties(self) -> win32more.Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_commethod(8)
    def get_BitmapContainerProperties(self) -> win32more.Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_commethod(9)
    def get_IsThumbnailGenerated(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsThumbnailGenerated(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_GeneratedThumbnailWidth(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_GeneratedThumbnailWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_GeneratedThumbnailHeight(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_GeneratedThumbnailHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(15)
    def get_BitmapTransform(self) -> win32more.Windows.Graphics.Imaging.BitmapTransform: ...
    @winrt_commethod(16)
    def SetPixelData(self, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, width: UInt32, height: UInt32, dpiX: Double, dpiY: Double, pixels: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(17)
    def GoToNextFrameAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def GoToNextFrameWithEncodingOptionsAsync(self, encodingOptions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def FlushAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    EncoderInformation = property(get_EncoderInformation, None)
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    IsThumbnailGenerated = property(get_IsThumbnailGenerated, put_IsThumbnailGenerated)
    GeneratedThumbnailWidth = property(get_GeneratedThumbnailWidth, put_GeneratedThumbnailWidth)
    GeneratedThumbnailHeight = property(get_GeneratedThumbnailHeight, put_GeneratedThumbnailHeight)
    BitmapTransform = property(get_BitmapTransform, None)
class IBitmapEncoderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapEncoderStatics'
    _iid_ = Guid('{a74356a7-a4e4-4eb9-8e40-564de7e1ccb2}')
    @winrt_commethod(6)
    def get_BmpEncoderId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_JpegEncoderId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_PngEncoderId(self) -> Guid: ...
    @winrt_commethod(9)
    def get_TiffEncoderId(self) -> Guid: ...
    @winrt_commethod(10)
    def get_GifEncoderId(self) -> Guid: ...
    @winrt_commethod(11)
    def get_JpegXREncoderId(self) -> Guid: ...
    @winrt_commethod(12)
    def GetEncoderInformationEnumerator(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_commethod(13)
    def CreateAsync(self, encoderId: Guid, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_commethod(14)
    def CreateWithEncodingOptionsAsync(self, encoderId: Guid, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, encodingOptions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_commethod(15)
    def CreateForTranscodingAsync(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, bitmapDecoder: win32more.Windows.Graphics.Imaging.BitmapDecoder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_commethod(16)
    def CreateForInPlacePropertyEncodingAsync(self, bitmapDecoder: win32more.Windows.Graphics.Imaging.BitmapDecoder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapEncoder]: ...
    BmpEncoderId = property(get_BmpEncoderId, None)
    JpegEncoderId = property(get_JpegEncoderId, None)
    PngEncoderId = property(get_PngEncoderId, None)
    TiffEncoderId = property(get_TiffEncoderId, None)
    GifEncoderId = property(get_GifEncoderId, None)
    JpegXREncoderId = property(get_JpegXREncoderId, None)
class IBitmapEncoderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapEncoderStatics2'
    _iid_ = Guid('{33cbc259-fe31-41b1-b812-086d21e87e16}')
    @winrt_commethod(6)
    def get_HeifEncoderId(self) -> Guid: ...
    HeifEncoderId = property(get_HeifEncoderId, None)
class IBitmapEncoderWithSoftwareBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapEncoderWithSoftwareBitmap'
    _iid_ = Guid('{686cd241-4330-4c77-ace4-0334968b1768}')
    @winrt_commethod(6)
    def SetSoftwareBitmap(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
class IBitmapFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapFrame'
    _iid_ = Guid('{72a49a1c-8081-438d-91bc-94ecfc8185c6}')
    @winrt_commethod(6)
    def GetThumbnailAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_commethod(7)
    def get_BitmapProperties(self) -> win32more.Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_commethod(8)
    def get_BitmapPixelFormat(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(9)
    def get_BitmapAlphaMode(self) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(10)
    def get_DpiX(self) -> Double: ...
    @winrt_commethod(11)
    def get_DpiY(self) -> Double: ...
    @winrt_commethod(12)
    def get_PixelWidth(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_PixelHeight(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_OrientedPixelWidth(self) -> UInt32: ...
    @winrt_commethod(15)
    def get_OrientedPixelHeight(self) -> UInt32: ...
    @winrt_commethod(16)
    def GetPixelDataAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_commethod(17)
    def GetPixelDataTransformedAsync(self, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, transform: win32more.Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: win32more.Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: win32more.Windows.Graphics.Imaging.ColorManagementMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.PixelDataProvider]: ...
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    DpiX = property(get_DpiX, None)
    DpiY = property(get_DpiY, None)
    PixelWidth = property(get_PixelWidth, None)
    PixelHeight = property(get_PixelHeight, None)
    OrientedPixelWidth = property(get_OrientedPixelWidth, None)
    OrientedPixelHeight = property(get_OrientedPixelHeight, None)
class IBitmapFrameWithSoftwareBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap'
    _iid_ = Guid('{fe287c9a-420c-4963-87ad-691436e08383}')
    @winrt_commethod(6)
    def GetSoftwareBitmapAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_commethod(7)
    def GetSoftwareBitmapConvertedAsync(self, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_commethod(8)
    def GetSoftwareBitmapTransformedAsync(self, pixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: win32more.Windows.Graphics.Imaging.BitmapAlphaMode, transform: win32more.Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: win32more.Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: win32more.Windows.Graphics.Imaging.ColorManagementMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
class IBitmapProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapProperties'
    _iid_ = Guid('{ea9f4f1b-b505-4450-a4d1-e8ca94529d8d}')
    @winrt_commethod(6)
    def SetPropertiesAsync(self, propertiesToSet: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Graphics.Imaging.BitmapTypedValue]]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBitmapPropertiesView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapPropertiesView'
    _iid_ = Guid('{7e0fe87a-3a70-48f8-9c55-196cf5a545f5}')
    @winrt_commethod(6)
    def GetPropertiesAsync(self, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.BitmapPropertySet]: ...
class IBitmapTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapTransform'
    _iid_ = Guid('{ae755344-e268-4d35-adcf-e995d31a8d34}')
    @winrt_commethod(6)
    def get_ScaledWidth(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_ScaledWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_ScaledHeight(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_ScaledHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_InterpolationMode(self) -> win32more.Windows.Graphics.Imaging.BitmapInterpolationMode: ...
    @winrt_commethod(11)
    def put_InterpolationMode(self, value: win32more.Windows.Graphics.Imaging.BitmapInterpolationMode) -> Void: ...
    @winrt_commethod(12)
    def get_Flip(self) -> win32more.Windows.Graphics.Imaging.BitmapFlip: ...
    @winrt_commethod(13)
    def put_Flip(self, value: win32more.Windows.Graphics.Imaging.BitmapFlip) -> Void: ...
    @winrt_commethod(14)
    def get_Rotation(self) -> win32more.Windows.Graphics.Imaging.BitmapRotation: ...
    @winrt_commethod(15)
    def put_Rotation(self, value: win32more.Windows.Graphics.Imaging.BitmapRotation) -> Void: ...
    @winrt_commethod(16)
    def get_Bounds(self) -> win32more.Windows.Graphics.Imaging.BitmapBounds: ...
    @winrt_commethod(17)
    def put_Bounds(self, value: win32more.Windows.Graphics.Imaging.BitmapBounds) -> Void: ...
    ScaledWidth = property(get_ScaledWidth, put_ScaledWidth)
    ScaledHeight = property(get_ScaledHeight, put_ScaledHeight)
    InterpolationMode = property(get_InterpolationMode, put_InterpolationMode)
    Flip = property(get_Flip, put_Flip)
    Rotation = property(get_Rotation, put_Rotation)
    Bounds = property(get_Bounds, put_Bounds)
class IBitmapTypedValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapTypedValue'
    _iid_ = Guid('{cd8044a9-2443-4000-b0cd-79316c56f589}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Type(self) -> win32more.Windows.Foundation.PropertyType: ...
    Value = property(get_Value, None)
    Type = property(get_Type, None)
class IBitmapTypedValueFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IBitmapTypedValueFactory'
    _iid_ = Guid('{92dbb599-ce13-46bb-9545-cb3a3f63eb8b}')
    @winrt_commethod(6)
    def Create(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, type: win32more.Windows.Foundation.PropertyType) -> win32more.Windows.Graphics.Imaging.BitmapTypedValue: ...
class IPixelDataProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.IPixelDataProvider'
    _iid_ = Guid('{dd831f25-185c-4595-9fb9-ccbe6ec18a6f}')
    @winrt_commethod(6)
    def DetachPixelData(self) -> SZArray[Byte]: ...
class ISoftwareBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.ISoftwareBitmap'
    _iid_ = Guid('{689e0708-7eef-483f-963f-da938818e073}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(8)
    def get_PixelWidth(self) -> Int32: ...
    @winrt_commethod(9)
    def get_PixelHeight(self) -> Int32: ...
    @winrt_commethod(10)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_DpiX(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_DpiX(self) -> Double: ...
    @winrt_commethod(13)
    def put_DpiY(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_DpiY(self) -> Double: ...
    @winrt_commethod(15)
    def LockBuffer(self, mode: win32more.Windows.Graphics.Imaging.BitmapBufferAccessMode) -> win32more.Windows.Graphics.Imaging.BitmapBuffer: ...
    @winrt_commethod(16)
    def CopyTo(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(17)
    def CopyFromBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(18)
    def CopyToBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(19)
    def GetReadOnlyView(self) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    PixelWidth = property(get_PixelWidth, None)
    PixelHeight = property(get_PixelHeight, None)
    IsReadOnly = property(get_IsReadOnly, None)
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
class ISoftwareBitmapFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.ISoftwareBitmapFactory'
    _iid_ = Guid('{c99feb69-2d62-4d47-a6b3-4fdb6a07fdf8}')
    @winrt_commethod(6)
    def Create(self, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def CreateWithAlpha(self, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
class ISoftwareBitmapStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.ISoftwareBitmapStatics'
    _iid_ = Guid('{df0385db-672f-4a9d-806e-c2442f343e86}')
    @winrt_commethod(6)
    def Copy(self, source: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def Convert(self, source: win32more.Windows.Graphics.Imaging.SoftwareBitmap, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(8)
    def ConvertWithAlpha(self, source: win32more.Windows.Graphics.Imaging.SoftwareBitmap, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(9)
    def CreateCopyFromBuffer(self, source: win32more.Windows.Storage.Streams.IBuffer, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(10)
    def CreateCopyWithAlphaFromBuffer(self, source: win32more.Windows.Storage.Streams.IBuffer, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(11)
    def CreateCopyFromSurfaceAsync(self, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_commethod(12)
    def CreateCopyWithAlphaFromSurfaceAsync(self, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
class ImageStream(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType
    _classid_ = 'Windows.Graphics.Imaging.ImageStream'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Storage.Streams.IInputStream, buffer: win32more.Windows.Storage.Streams.IBuffer, count: UInt32, options: win32more.Windows.Storage.Streams.InputStreamOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    Size = property(get_Size, put_Size)
    Position = property(get_Position, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
JpegSubsamplingMode = Int32
JpegSubsamplingMode_Default: JpegSubsamplingMode = 0
JpegSubsamplingMode_Y4Cb2Cr0: JpegSubsamplingMode = 1
JpegSubsamplingMode_Y4Cb2Cr2: JpegSubsamplingMode = 2
JpegSubsamplingMode_Y4Cb4Cr4: JpegSubsamplingMode = 3
class PixelDataProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.IPixelDataProvider
    _classid_ = 'Windows.Graphics.Imaging.PixelDataProvider'
    @winrt_mixinmethod
    def DetachPixelData(self: win32more.Windows.Graphics.Imaging.IPixelDataProvider) -> SZArray[Byte]: ...
PngFilterMode = Int32
PngFilterMode_Automatic: PngFilterMode = 0
PngFilterMode_None: PngFilterMode = 1
PngFilterMode_Sub: PngFilterMode = 2
PngFilterMode_Up: PngFilterMode = 3
PngFilterMode_Average: PngFilterMode = 4
PngFilterMode_Paeth: PngFilterMode = 5
PngFilterMode_Adaptive: PngFilterMode = 6
class SoftwareBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Imaging.ISoftwareBitmap
    _classid_ = 'Windows.Graphics.Imaging.SoftwareBitmap'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 3:
            return win32more.Windows.Graphics.Imaging.SoftwareBitmap.Create(*args)
        elif len(args) == 4:
            return win32more.Windows.Graphics.Imaging.SoftwareBitmap.CreateWithAlpha(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapFactory, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_factorymethod
    def CreateWithAlpha(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapFactory, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> Int32: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> Boolean: ...
    @winrt_mixinmethod
    def put_DpiX(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DpiX(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> Double: ...
    @winrt_mixinmethod
    def put_DpiY(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DpiY(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> Double: ...
    @winrt_mixinmethod
    def LockBuffer(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap, mode: win32more.Windows.Graphics.Imaging.BitmapBufferAccessMode) -> win32more.Windows.Graphics.Imaging.BitmapBuffer: ...
    @winrt_mixinmethod
    def CopyTo(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def CopyFromBuffer(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def CopyToBuffer(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetReadOnlyView(self: win32more.Windows.Graphics.Imaging.ISoftwareBitmap) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def Copy(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def Convert(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: win32more.Windows.Graphics.Imaging.SoftwareBitmap, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def ConvertWithAlpha(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: win32more.Windows.Graphics.Imaging.SoftwareBitmap, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def CreateCopyFromBuffer(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: win32more.Windows.Storage.Streams.IBuffer, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def CreateCopyWithAlphaFromBuffer(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: win32more.Windows.Storage.Streams.IBuffer, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def CreateCopyFromSurfaceAsync(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_classmethod
    def CreateCopyWithAlphaFromSurfaceAsync(cls: win32more.Windows.Graphics.Imaging.ISoftwareBitmapStatics, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.SoftwareBitmap]: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    PixelWidth = property(get_PixelWidth, None)
    PixelHeight = property(get_PixelHeight, None)
    IsReadOnly = property(get_IsReadOnly, None)
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
TiffCompressionMode = Int32
TiffCompressionMode_Automatic: TiffCompressionMode = 0
TiffCompressionMode_None: TiffCompressionMode = 1
TiffCompressionMode_Ccitt3: TiffCompressionMode = 2
TiffCompressionMode_Ccitt4: TiffCompressionMode = 3
TiffCompressionMode_Lzw: TiffCompressionMode = 4
TiffCompressionMode_Rle: TiffCompressionMode = 5
TiffCompressionMode_Zip: TiffCompressionMode = 6
TiffCompressionMode_LzwhDifferencing: TiffCompressionMode = 7
make_ready(__name__)
