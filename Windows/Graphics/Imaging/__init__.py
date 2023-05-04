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
import Windows.Foundation.Collections
import Windows.Graphics.DirectX.Direct3D11
import Windows.Graphics.Imaging
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapBuffer'
    @winrt_mixinmethod
    def GetPlaneCount(self: Windows.Graphics.Imaging.IBitmapBuffer) -> Int32: ...
    @winrt_mixinmethod
    def GetPlaneDescription(self: Windows.Graphics.Imaging.IBitmapBuffer, index: Int32) -> Windows.Graphics.Imaging.BitmapPlaneDescription: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
BitmapBufferAccessMode = Int32
BitmapBufferAccessMode_Read: BitmapBufferAccessMode = 0
BitmapBufferAccessMode_ReadWrite: BitmapBufferAccessMode = 1
BitmapBufferAccessMode_Write: BitmapBufferAccessMode = 2
class BitmapCodecInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapCodecInformation'
    @winrt_mixinmethod
    def get_CodecId(self: Windows.Graphics.Imaging.IBitmapCodecInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_FileExtensions(self: Windows.Graphics.Imaging.IBitmapCodecInformation) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Graphics.Imaging.IBitmapCodecInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MimeTypes(self: Windows.Graphics.Imaging.IBitmapCodecInformation) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    CodecId = property(get_CodecId, None)
    FileExtensions = property(get_FileExtensions, None)
    FriendlyName = property(get_FriendlyName, None)
    MimeTypes = property(get_MimeTypes, None)
class BitmapDecoder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapDecoder'
    @winrt_mixinmethod
    def get_BitmapContainerProperties(self: Windows.Graphics.Imaging.IBitmapDecoder) -> Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_mixinmethod
    def get_DecoderInformation(self: Windows.Graphics.Imaging.IBitmapDecoder) -> Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_mixinmethod
    def get_FrameCount(self: Windows.Graphics.Imaging.IBitmapDecoder) -> UInt32: ...
    @winrt_mixinmethod
    def GetPreviewAsync(self: Windows.Graphics.Imaging.IBitmapDecoder) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def GetFrameAsync(self: Windows.Graphics.Imaging.IBitmapDecoder, frameIndex: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapFrame]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_DpiX(self: Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_DpiY(self: Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelWidth(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelHeight(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def GetPixelDataAsync(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetPixelDataTransformedAsync(self: Windows.Graphics.Imaging.IBitmapFrame, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, transform: Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: Windows.Graphics.Imaging.ColorManagementMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapAsync(self: Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapConvertedAsync(self: Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapTransformedAsync(self: Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, transform: Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: Windows.Graphics.Imaging.ColorManagementMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_classmethod
    def get_HeifDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics2) -> Guid: ...
    @winrt_classmethod
    def get_WebpDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BmpDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_PngDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_TiffDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_GifDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegXRDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_IcoDecoderId(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Guid: ...
    @winrt_classmethod
    def GetDecoderInformationEnumerator(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapDecoder]: ...
    @winrt_classmethod
    def CreateWithIdAsync(cls: Windows.Graphics.Imaging.IBitmapDecoderStatics, decoderId: Guid, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapDecoder]: ...
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
    HeifDecoderId = property(get_HeifDecoderId, None)
    WebpDecoderId = property(get_WebpDecoderId, None)
    BmpDecoderId = property(get_BmpDecoderId, None)
    JpegDecoderId = property(get_JpegDecoderId, None)
    PngDecoderId = property(get_PngDecoderId, None)
    TiffDecoderId = property(get_TiffDecoderId, None)
    GifDecoderId = property(get_GifDecoderId, None)
    JpegXRDecoderId = property(get_JpegXRDecoderId, None)
    IcoDecoderId = property(get_IcoDecoderId, None)
class BitmapEncoder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapEncoder'
    @winrt_mixinmethod
    def get_EncoderInformation(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_mixinmethod
    def get_BitmapContainerProperties(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_mixinmethod
    def get_IsThumbnailGenerated(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsThumbnailGenerated(self: Windows.Graphics.Imaging.IBitmapEncoder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_GeneratedThumbnailWidth(self: Windows.Graphics.Imaging.IBitmapEncoder) -> UInt32: ...
    @winrt_mixinmethod
    def put_GeneratedThumbnailWidth(self: Windows.Graphics.Imaging.IBitmapEncoder, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_GeneratedThumbnailHeight(self: Windows.Graphics.Imaging.IBitmapEncoder) -> UInt32: ...
    @winrt_mixinmethod
    def put_GeneratedThumbnailHeight(self: Windows.Graphics.Imaging.IBitmapEncoder, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BitmapTransform(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Windows.Graphics.Imaging.BitmapTransform: ...
    @winrt_mixinmethod
    def SetPixelData(self: Windows.Graphics.Imaging.IBitmapEncoder, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, width: UInt32, height: UInt32, dpiX: Double, dpiY: Double, pixels: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GoToNextFrameAsync(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GoToNextFrameWithEncodingOptionsAsync(self: Windows.Graphics.Imaging.IBitmapEncoder, encodingOptions: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FlushAsync(self: Windows.Graphics.Imaging.IBitmapEncoder) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetSoftwareBitmap(self: Windows.Graphics.Imaging.IBitmapEncoderWithSoftwareBitmap, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_classmethod
    def get_HeifEncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BmpEncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegEncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_PngEncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_TiffEncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_GifEncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def get_JpegXREncoderId(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Guid: ...
    @winrt_classmethod
    def GetEncoderInformationEnumerator(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics, encoderId: Guid, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_classmethod
    def CreateWithEncodingOptionsAsync(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics, encoderId: Guid, stream: Windows.Storage.Streams.IRandomAccessStream, encodingOptions: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_classmethod
    def CreateForTranscodingAsync(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics, stream: Windows.Storage.Streams.IRandomAccessStream, bitmapDecoder: Windows.Graphics.Imaging.BitmapDecoder) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_classmethod
    def CreateForInPlacePropertyEncodingAsync(cls: Windows.Graphics.Imaging.IBitmapEncoderStatics, bitmapDecoder: Windows.Graphics.Imaging.BitmapDecoder) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    EncoderInformation = property(get_EncoderInformation, None)
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    IsThumbnailGenerated = property(get_IsThumbnailGenerated, put_IsThumbnailGenerated)
    GeneratedThumbnailWidth = property(get_GeneratedThumbnailWidth, put_GeneratedThumbnailWidth)
    GeneratedThumbnailHeight = property(get_GeneratedThumbnailHeight, put_GeneratedThumbnailHeight)
    BitmapTransform = property(get_BitmapTransform, None)
    HeifEncoderId = property(get_HeifEncoderId, None)
    BmpEncoderId = property(get_BmpEncoderId, None)
    JpegEncoderId = property(get_JpegEncoderId, None)
    PngEncoderId = property(get_PngEncoderId, None)
    TiffEncoderId = property(get_TiffEncoderId, None)
    GifEncoderId = property(get_GifEncoderId, None)
    JpegXREncoderId = property(get_JpegXREncoderId, None)
BitmapFlip = Int32
BitmapFlip_None: BitmapFlip = 0
BitmapFlip_Horizontal: BitmapFlip = 1
BitmapFlip_Vertical: BitmapFlip = 2
class BitmapFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapFrame'
    @winrt_mixinmethod
    def GetThumbnailAsync(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_DpiX(self: Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_DpiY(self: Windows.Graphics.Imaging.IBitmapFrame) -> Double: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelWidth(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_OrientedPixelHeight(self: Windows.Graphics.Imaging.IBitmapFrame) -> UInt32: ...
    @winrt_mixinmethod
    def GetPixelDataAsync(self: Windows.Graphics.Imaging.IBitmapFrame) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetPixelDataTransformedAsync(self: Windows.Graphics.Imaging.IBitmapFrame, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, transform: Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: Windows.Graphics.Imaging.ColorManagementMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapAsync(self: Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapConvertedAsync(self: Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_mixinmethod
    def GetSoftwareBitmapTransformedAsync(self: Windows.Graphics.Imaging.IBitmapFrameWithSoftwareBitmap, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, transform: Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: Windows.Graphics.Imaging.ColorManagementMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapProperties'
    @winrt_mixinmethod
    def SetPropertiesAsync(self: Windows.Graphics.Imaging.IBitmapProperties, propertiesToSet: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: Windows.Graphics.Imaging.IBitmapPropertiesView, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapPropertySet]: ...
class BitmapPropertiesView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapPropertiesView'
    @winrt_mixinmethod
    def GetPropertiesAsync(self: Windows.Graphics.Imaging.IBitmapPropertiesView, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapPropertySet]: ...
class BitmapPropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapPropertySet'
    @winrt_activatemethod
    def New(cls) -> Windows.Graphics.Imaging.BitmapPropertySet: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String) -> Windows.Graphics.Imaging.BitmapTypedValue: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String, value: Windows.Graphics.Imaging.BitmapTypedValue) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.Graphics.Imaging.BitmapTransform: ...
    @winrt_mixinmethod
    def get_ScaledWidth(self: Windows.Graphics.Imaging.IBitmapTransform) -> UInt32: ...
    @winrt_mixinmethod
    def put_ScaledWidth(self: Windows.Graphics.Imaging.IBitmapTransform, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ScaledHeight(self: Windows.Graphics.Imaging.IBitmapTransform) -> UInt32: ...
    @winrt_mixinmethod
    def put_ScaledHeight(self: Windows.Graphics.Imaging.IBitmapTransform, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_InterpolationMode(self: Windows.Graphics.Imaging.IBitmapTransform) -> Windows.Graphics.Imaging.BitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_InterpolationMode(self: Windows.Graphics.Imaging.IBitmapTransform, value: Windows.Graphics.Imaging.BitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_Flip(self: Windows.Graphics.Imaging.IBitmapTransform) -> Windows.Graphics.Imaging.BitmapFlip: ...
    @winrt_mixinmethod
    def put_Flip(self: Windows.Graphics.Imaging.IBitmapTransform, value: Windows.Graphics.Imaging.BitmapFlip) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: Windows.Graphics.Imaging.IBitmapTransform) -> Windows.Graphics.Imaging.BitmapRotation: ...
    @winrt_mixinmethod
    def put_Rotation(self: Windows.Graphics.Imaging.IBitmapTransform, value: Windows.Graphics.Imaging.BitmapRotation) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: Windows.Graphics.Imaging.IBitmapTransform) -> Windows.Graphics.Imaging.BitmapBounds: ...
    @winrt_mixinmethod
    def put_Bounds(self: Windows.Graphics.Imaging.IBitmapTransform, value: Windows.Graphics.Imaging.BitmapBounds) -> Void: ...
    ScaledWidth = property(get_ScaledWidth, put_ScaledWidth)
    ScaledHeight = property(get_ScaledHeight, put_ScaledHeight)
    InterpolationMode = property(get_InterpolationMode, put_InterpolationMode)
    Flip = property(get_Flip, put_Flip)
    Rotation = property(get_Rotation, put_Rotation)
    Bounds = property(get_Bounds, put_Bounds)
class BitmapTypedValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.BitmapTypedValue'
    @winrt_factorymethod
    def Create(cls: Windows.Graphics.Imaging.IBitmapTypedValueFactory, value: Windows.Win32.System.WinRT.IInspectable_head, type: Windows.Foundation.PropertyType) -> Windows.Graphics.Imaging.BitmapTypedValue: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Imaging.IBitmapTypedValue) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Graphics.Imaging.IBitmapTypedValue) -> Windows.Foundation.PropertyType: ...
    Value = property(get_Value, None)
    Type = property(get_Type, None)
ColorManagementMode = Int32
ColorManagementMode_DoNotColorManage: ColorManagementMode = 0
ColorManagementMode_ColorManageToSRgb: ColorManagementMode = 1
ExifOrientationMode = Int32
ExifOrientationMode_IgnoreExifOrientation: ExifOrientationMode = 0
ExifOrientationMode_RespectExifOrientation: ExifOrientationMode = 1
class IBitmapBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a53e04c4-399c-438c-b28f-a63a6b83d1a1}')
    @winrt_commethod(6)
    def GetPlaneCount(self) -> Int32: ...
    @winrt_commethod(7)
    def GetPlaneDescription(self, index: Int32) -> Windows.Graphics.Imaging.BitmapPlaneDescription: ...
class IBitmapCodecInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{400caaf2-c4b0-4392-a3b0-6f6f9ba95cb4}')
    @winrt_commethod(6)
    def get_CodecId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_FileExtensions(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MimeTypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    CodecId = property(get_CodecId, None)
    FileExtensions = property(get_FileExtensions, None)
    FriendlyName = property(get_FriendlyName, None)
    MimeTypes = property(get_MimeTypes, None)
class IBitmapDecoder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{acef22ba-1d74-4c91-9dfc-9620745233e6}')
    @winrt_commethod(6)
    def get_BitmapContainerProperties(self) -> Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_commethod(7)
    def get_DecoderInformation(self) -> Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_commethod(8)
    def get_FrameCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def GetPreviewAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_commethod(10)
    def GetFrameAsync(self, frameIndex: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapFrame]: ...
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    DecoderInformation = property(get_DecoderInformation, None)
    FrameCount = property(get_FrameCount, None)
class IBitmapDecoderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def GetDecoderInformationEnumerator(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_commethod(14)
    def CreateAsync(self, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapDecoder]: ...
    @winrt_commethod(15)
    def CreateWithIdAsync(self, decoderId: Guid, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapDecoder]: ...
    BmpDecoderId = property(get_BmpDecoderId, None)
    JpegDecoderId = property(get_JpegDecoderId, None)
    PngDecoderId = property(get_PngDecoderId, None)
    TiffDecoderId = property(get_TiffDecoderId, None)
    GifDecoderId = property(get_GifDecoderId, None)
    JpegXRDecoderId = property(get_JpegXRDecoderId, None)
    IcoDecoderId = property(get_IcoDecoderId, None)
class IBitmapDecoderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{50ba68ea-99a1-40c4-80d9-aef0dafa6c3f}')
    @winrt_commethod(6)
    def get_HeifDecoderId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_WebpDecoderId(self) -> Guid: ...
    HeifDecoderId = property(get_HeifDecoderId, None)
    WebpDecoderId = property(get_WebpDecoderId, None)
class IBitmapEncoder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2bc468e3-e1f8-4b54-95e8-32919551ce62}')
    @winrt_commethod(6)
    def get_EncoderInformation(self) -> Windows.Graphics.Imaging.BitmapCodecInformation: ...
    @winrt_commethod(7)
    def get_BitmapProperties(self) -> Windows.Graphics.Imaging.BitmapProperties: ...
    @winrt_commethod(8)
    def get_BitmapContainerProperties(self) -> Windows.Graphics.Imaging.BitmapProperties: ...
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
    def get_BitmapTransform(self) -> Windows.Graphics.Imaging.BitmapTransform: ...
    @winrt_commethod(16)
    def SetPixelData(self, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, width: UInt32, height: UInt32, dpiX: Double, dpiY: Double, pixels: c_char_p_no) -> Void: ...
    @winrt_commethod(17)
    def GoToNextFrameAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def GoToNextFrameWithEncodingOptionsAsync(self, encodingOptions: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def FlushAsync(self) -> Windows.Foundation.IAsyncAction: ...
    EncoderInformation = property(get_EncoderInformation, None)
    BitmapProperties = property(get_BitmapProperties, None)
    BitmapContainerProperties = property(get_BitmapContainerProperties, None)
    IsThumbnailGenerated = property(get_IsThumbnailGenerated, put_IsThumbnailGenerated)
    GeneratedThumbnailWidth = property(get_GeneratedThumbnailWidth, put_GeneratedThumbnailWidth)
    GeneratedThumbnailHeight = property(get_GeneratedThumbnailHeight, put_GeneratedThumbnailHeight)
    BitmapTransform = property(get_BitmapTransform, None)
class IBitmapEncoderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def GetEncoderInformationEnumerator(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapCodecInformation]: ...
    @winrt_commethod(13)
    def CreateAsync(self, encoderId: Guid, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_commethod(14)
    def CreateWithEncodingOptionsAsync(self, encoderId: Guid, stream: Windows.Storage.Streams.IRandomAccessStream, encodingOptions: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_commethod(15)
    def CreateForTranscodingAsync(self, stream: Windows.Storage.Streams.IRandomAccessStream, bitmapDecoder: Windows.Graphics.Imaging.BitmapDecoder) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    @winrt_commethod(16)
    def CreateForInPlacePropertyEncodingAsync(self, bitmapDecoder: Windows.Graphics.Imaging.BitmapDecoder) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapEncoder]: ...
    BmpEncoderId = property(get_BmpEncoderId, None)
    JpegEncoderId = property(get_JpegEncoderId, None)
    PngEncoderId = property(get_PngEncoderId, None)
    TiffEncoderId = property(get_TiffEncoderId, None)
    GifEncoderId = property(get_GifEncoderId, None)
    JpegXREncoderId = property(get_JpegXREncoderId, None)
class IBitmapEncoderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{33cbc259-fe31-41b1-b812-086d21e87e16}')
    @winrt_commethod(6)
    def get_HeifEncoderId(self) -> Guid: ...
    HeifEncoderId = property(get_HeifEncoderId, None)
class IBitmapEncoderWithSoftwareBitmap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{686cd241-4330-4c77-ace4-0334968b1768}')
    @winrt_commethod(6)
    def SetSoftwareBitmap(self, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
class IBitmapFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{72a49a1c-8081-438d-91bc-94ecfc8185c6}')
    @winrt_commethod(6)
    def GetThumbnailAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_commethod(7)
    def get_BitmapProperties(self) -> Windows.Graphics.Imaging.BitmapPropertiesView: ...
    @winrt_commethod(8)
    def get_BitmapPixelFormat(self) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(9)
    def get_BitmapAlphaMode(self) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
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
    def GetPixelDataAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.PixelDataProvider]: ...
    @winrt_commethod(17)
    def GetPixelDataTransformedAsync(self, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, transform: Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: Windows.Graphics.Imaging.ColorManagementMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.PixelDataProvider]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fe287c9a-420c-4963-87ad-691436e08383}')
    @winrt_commethod(6)
    def GetSoftwareBitmapAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_commethod(7)
    def GetSoftwareBitmapConvertedAsync(self, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_commethod(8)
    def GetSoftwareBitmapTransformedAsync(self, pixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat, alphaMode: Windows.Graphics.Imaging.BitmapAlphaMode, transform: Windows.Graphics.Imaging.BitmapTransform, exifOrientationMode: Windows.Graphics.Imaging.ExifOrientationMode, colorManagementMode: Windows.Graphics.Imaging.ColorManagementMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
class IBitmapProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ea9f4f1b-b505-4450-a4d1-e8ca94529d8d}')
    @winrt_commethod(6)
    def SetPropertiesAsync(self, propertiesToSet: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Graphics.Imaging.BitmapTypedValue]]) -> Windows.Foundation.IAsyncAction: ...
class IBitmapPropertiesView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7e0fe87a-3a70-48f8-9c55-196cf5a545f5}')
    @winrt_commethod(6)
    def GetPropertiesAsync(self, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.BitmapPropertySet]: ...
class IBitmapTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_InterpolationMode(self) -> Windows.Graphics.Imaging.BitmapInterpolationMode: ...
    @winrt_commethod(11)
    def put_InterpolationMode(self, value: Windows.Graphics.Imaging.BitmapInterpolationMode) -> Void: ...
    @winrt_commethod(12)
    def get_Flip(self) -> Windows.Graphics.Imaging.BitmapFlip: ...
    @winrt_commethod(13)
    def put_Flip(self, value: Windows.Graphics.Imaging.BitmapFlip) -> Void: ...
    @winrt_commethod(14)
    def get_Rotation(self) -> Windows.Graphics.Imaging.BitmapRotation: ...
    @winrt_commethod(15)
    def put_Rotation(self, value: Windows.Graphics.Imaging.BitmapRotation) -> Void: ...
    @winrt_commethod(16)
    def get_Bounds(self) -> Windows.Graphics.Imaging.BitmapBounds: ...
    @winrt_commethod(17)
    def put_Bounds(self, value: Windows.Graphics.Imaging.BitmapBounds) -> Void: ...
    ScaledWidth = property(get_ScaledWidth, put_ScaledWidth)
    ScaledHeight = property(get_ScaledHeight, put_ScaledHeight)
    InterpolationMode = property(get_InterpolationMode, put_InterpolationMode)
    Flip = property(get_Flip, put_Flip)
    Rotation = property(get_Rotation, put_Rotation)
    Bounds = property(get_Bounds, put_Bounds)
class IBitmapTypedValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cd8044a9-2443-4000-b0cd-79316c56f589}')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_Type(self) -> Windows.Foundation.PropertyType: ...
    Value = property(get_Value, None)
    Type = property(get_Type, None)
class IBitmapTypedValueFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{92dbb599-ce13-46bb-9545-cb3a3f63eb8b}')
    @winrt_commethod(6)
    def Create(self, value: Windows.Win32.System.WinRT.IInspectable_head, type: Windows.Foundation.PropertyType) -> Windows.Graphics.Imaging.BitmapTypedValue: ...
class IPixelDataProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dd831f25-185c-4595-9fb9-ccbe6ec18a6f}')
    @winrt_commethod(6)
    def DetachPixelData(self) -> c_char_p_no: ...
class ISoftwareBitmap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{689e0708-7eef-483f-963f-da938818e073}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
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
    def LockBuffer(self, mode: Windows.Graphics.Imaging.BitmapBufferAccessMode) -> Windows.Graphics.Imaging.BitmapBuffer: ...
    @winrt_commethod(16)
    def CopyTo(self, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(17)
    def CopyFromBuffer(self, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(18)
    def CopyToBuffer(self, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(19)
    def GetReadOnlyView(self) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    PixelWidth = property(get_PixelWidth, None)
    PixelHeight = property(get_PixelHeight, None)
    IsReadOnly = property(get_IsReadOnly, None)
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
class ISoftwareBitmapFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c99feb69-2d62-4d47-a6b3-4fdb6a07fdf8}')
    @winrt_commethod(6)
    def Create(self, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def CreateWithAlpha(self, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
class ISoftwareBitmapStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{df0385db-672f-4a9d-806e-c2442f343e86}')
    @winrt_commethod(6)
    def Copy(self, source: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def Convert(self, source: Windows.Graphics.Imaging.SoftwareBitmap, format: Windows.Graphics.Imaging.BitmapPixelFormat) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(8)
    def ConvertWithAlpha(self, source: Windows.Graphics.Imaging.SoftwareBitmap, format: Windows.Graphics.Imaging.BitmapPixelFormat, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(9)
    def CreateCopyFromBuffer(self, source: Windows.Storage.Streams.IBuffer, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(10)
    def CreateCopyWithAlphaFromBuffer(self, source: Windows.Storage.Streams.IBuffer, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(11)
    def CreateCopyFromSurfaceAsync(self, surface: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_commethod(12)
    def CreateCopyWithAlphaFromSurfaceAsync(self, surface: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
class ImageStream(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.ImageStream'
    @winrt_mixinmethod
    def get_Size(self: Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: Windows.Storage.Streams.IInputStream, buffer: Windows.Storage.Streams.IBuffer, count: UInt32, options: Windows.Storage.Streams.InputStreamOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: Windows.Storage.Streams.IOutputStream, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.PixelDataProvider'
    @winrt_mixinmethod
    def DetachPixelData(self: Windows.Graphics.Imaging.IPixelDataProvider) -> c_char_p_no: ...
PngFilterMode = Int32
PngFilterMode_Automatic: PngFilterMode = 0
PngFilterMode_None: PngFilterMode = 1
PngFilterMode_Sub: PngFilterMode = 2
PngFilterMode_Up: PngFilterMode = 3
PngFilterMode_Average: PngFilterMode = 4
PngFilterMode_Paeth: PngFilterMode = 5
PngFilterMode_Adaptive: PngFilterMode = 6
class SoftwareBitmap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Imaging.SoftwareBitmap'
    @winrt_factorymethod
    def Create(cls: Windows.Graphics.Imaging.ISoftwareBitmapFactory, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_factorymethod
    def CreateWithAlpha(cls: Windows.Graphics.Imaging.ISoftwareBitmapFactory, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Int32: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Boolean: ...
    @winrt_mixinmethod
    def put_DpiX(self: Windows.Graphics.Imaging.ISoftwareBitmap, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DpiX(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Double: ...
    @winrt_mixinmethod
    def put_DpiY(self: Windows.Graphics.Imaging.ISoftwareBitmap, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_DpiY(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Double: ...
    @winrt_mixinmethod
    def LockBuffer(self: Windows.Graphics.Imaging.ISoftwareBitmap, mode: Windows.Graphics.Imaging.BitmapBufferAccessMode) -> Windows.Graphics.Imaging.BitmapBuffer: ...
    @winrt_mixinmethod
    def CopyTo(self: Windows.Graphics.Imaging.ISoftwareBitmap, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def CopyFromBuffer(self: Windows.Graphics.Imaging.ISoftwareBitmap, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def CopyToBuffer(self: Windows.Graphics.Imaging.ISoftwareBitmap, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetReadOnlyView(self: Windows.Graphics.Imaging.ISoftwareBitmap) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def Copy(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def Convert(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: Windows.Graphics.Imaging.SoftwareBitmap, format: Windows.Graphics.Imaging.BitmapPixelFormat) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def ConvertWithAlpha(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: Windows.Graphics.Imaging.SoftwareBitmap, format: Windows.Graphics.Imaging.BitmapPixelFormat, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def CreateCopyFromBuffer(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: Windows.Storage.Streams.IBuffer, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def CreateCopyWithAlphaFromBuffer(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, source: Windows.Storage.Streams.IBuffer, format: Windows.Graphics.Imaging.BitmapPixelFormat, width: Int32, height: Int32, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_classmethod
    def CreateCopyFromSurfaceAsync(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, surface: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
    @winrt_classmethod
    def CreateCopyWithAlphaFromSurfaceAsync(cls: Windows.Graphics.Imaging.ISoftwareBitmapStatics, surface: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Imaging.SoftwareBitmap]: ...
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
make_head(_module, 'BitmapBounds')
make_head(_module, 'BitmapBuffer')
make_head(_module, 'BitmapCodecInformation')
make_head(_module, 'BitmapDecoder')
make_head(_module, 'BitmapEncoder')
make_head(_module, 'BitmapFrame')
make_head(_module, 'BitmapPlaneDescription')
make_head(_module, 'BitmapProperties')
make_head(_module, 'BitmapPropertiesView')
make_head(_module, 'BitmapPropertySet')
make_head(_module, 'BitmapSize')
make_head(_module, 'BitmapTransform')
make_head(_module, 'BitmapTypedValue')
make_head(_module, 'IBitmapBuffer')
make_head(_module, 'IBitmapCodecInformation')
make_head(_module, 'IBitmapDecoder')
make_head(_module, 'IBitmapDecoderStatics')
make_head(_module, 'IBitmapDecoderStatics2')
make_head(_module, 'IBitmapEncoder')
make_head(_module, 'IBitmapEncoderStatics')
make_head(_module, 'IBitmapEncoderStatics2')
make_head(_module, 'IBitmapEncoderWithSoftwareBitmap')
make_head(_module, 'IBitmapFrame')
make_head(_module, 'IBitmapFrameWithSoftwareBitmap')
make_head(_module, 'IBitmapProperties')
make_head(_module, 'IBitmapPropertiesView')
make_head(_module, 'IBitmapTransform')
make_head(_module, 'IBitmapTypedValue')
make_head(_module, 'IBitmapTypedValueFactory')
make_head(_module, 'IPixelDataProvider')
make_head(_module, 'ISoftwareBitmap')
make_head(_module, 'ISoftwareBitmapFactory')
make_head(_module, 'ISoftwareBitmapStatics')
make_head(_module, 'ImageStream')
make_head(_module, 'PixelDataProvider')
make_head(_module, 'SoftwareBitmap')
