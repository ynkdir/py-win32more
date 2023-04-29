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
import Windows.Data.Pdf
import Windows.Foundation
import Windows.Storage
import Windows.Storage.Streams
import Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPdfDocument(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ac7ebedd-80fa-4089-84-6e-81-b7-7f-f5-a8-6c')
    @winrt_commethod(6)
    def GetPage(self, pageIndex: UInt32) -> Windows.Data.Pdf.PdfPage: ...
    @winrt_commethod(7)
    def get_PageCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_IsPasswordProtected(self) -> Boolean: ...
    PageCount = property(get_PageCount, None)
    IsPasswordProtected = property(get_IsPasswordProtected, None)
class IPdfDocumentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('433a0b5f-c007-4788-90-f2-08-14-3d-92-25-99')
    @winrt_commethod(6)
    def LoadFromFileAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    @winrt_commethod(7)
    def LoadFromFileWithPasswordAsync(self, file: Windows.Storage.IStorageFile, password: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    @winrt_commethod(8)
    def LoadFromStreamAsync(self, inputStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    @winrt_commethod(9)
    def LoadFromStreamWithPasswordAsync(self, inputStream: Windows.Storage.Streams.IRandomAccessStream, password: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
class IPdfPage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9db4b0c8-5320-4cfc-ad-76-49-3f-da-d0-e5-94')
    @winrt_commethod(6)
    def RenderToStreamAsync(self, outputStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RenderWithOptionsToStreamAsync(self, outputStream: Windows.Storage.Streams.IRandomAccessStream, options: Windows.Data.Pdf.PdfPageRenderOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def PreparePageAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_Index(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Size(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def get_Dimensions(self) -> Windows.Data.Pdf.PdfPageDimensions: ...
    @winrt_commethod(12)
    def get_Rotation(self) -> Windows.Data.Pdf.PdfPageRotation: ...
    @winrt_commethod(13)
    def get_PreferredZoom(self) -> Single: ...
    Index = property(get_Index, None)
    Size = property(get_Size, None)
    Dimensions = property(get_Dimensions, None)
    Rotation = property(get_Rotation, None)
    PreferredZoom = property(get_PreferredZoom, None)
class IPdfPageDimensions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('22170471-313e-44e8-83-5d-63-a3-e7-62-4a-10')
    @winrt_commethod(6)
    def get_MediaBox(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_CropBox(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_BleedBox(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def get_TrimBox(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def get_ArtBox(self) -> Windows.Foundation.Rect: ...
    MediaBox = property(get_MediaBox, None)
    CropBox = property(get_CropBox, None)
    BleedBox = property(get_BleedBox, None)
    TrimBox = property(get_TrimBox, None)
    ArtBox = property(get_ArtBox, None)
class IPdfPageRenderOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c98056f-b7cf-4c29-9a-04-52-d9-02-67-f4-25')
    @winrt_commethod(6)
    def get_SourceRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_SourceRect(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(8)
    def get_DestinationWidth(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_DestinationWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_DestinationHeight(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_DestinationHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_BackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_IsIgnoringHighContrast(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsIgnoringHighContrast(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_BitmapEncoderId(self) -> Guid: ...
    @winrt_commethod(17)
    def put_BitmapEncoderId(self, value: Guid) -> Void: ...
    SourceRect = property(get_SourceRect, put_SourceRect)
    DestinationWidth = property(get_DestinationWidth, put_DestinationWidth)
    DestinationHeight = property(get_DestinationHeight, put_DestinationHeight)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    IsIgnoringHighContrast = property(get_IsIgnoringHighContrast, put_IsIgnoringHighContrast)
    BitmapEncoderId = property(get_BitmapEncoderId, put_BitmapEncoderId)
class PdfDocument(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Pdf.PdfDocument'
    @winrt_mixinmethod
    def GetPage(self: Windows.Data.Pdf.IPdfDocument, pageIndex: UInt32) -> Windows.Data.Pdf.PdfPage: ...
    @winrt_mixinmethod
    def get_PageCount(self: Windows.Data.Pdf.IPdfDocument) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsPasswordProtected(self: Windows.Data.Pdf.IPdfDocument) -> Boolean: ...
    @winrt_classmethod
    def LoadFromFileAsync(cls: Windows.Data.Pdf.IPdfDocumentStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    @winrt_classmethod
    def LoadFromFileWithPasswordAsync(cls: Windows.Data.Pdf.IPdfDocumentStatics, file: Windows.Storage.IStorageFile, password: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    @winrt_classmethod
    def LoadFromStreamAsync(cls: Windows.Data.Pdf.IPdfDocumentStatics, inputStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    @winrt_classmethod
    def LoadFromStreamWithPasswordAsync(cls: Windows.Data.Pdf.IPdfDocumentStatics, inputStream: Windows.Storage.Streams.IRandomAccessStream, password: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Data.Pdf.PdfDocument]: ...
    PageCount = property(get_PageCount, None)
    IsPasswordProtected = property(get_IsPasswordProtected, None)
class PdfPage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Pdf.PdfPage'
    @winrt_mixinmethod
    def RenderToStreamAsync(self: Windows.Data.Pdf.IPdfPage, outputStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenderWithOptionsToStreamAsync(self: Windows.Data.Pdf.IPdfPage, outputStream: Windows.Storage.Streams.IRandomAccessStream, options: Windows.Data.Pdf.PdfPageRenderOptions) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PreparePageAsync(self: Windows.Data.Pdf.IPdfPage) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Index(self: Windows.Data.Pdf.IPdfPage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Data.Pdf.IPdfPage) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_Dimensions(self: Windows.Data.Pdf.IPdfPage) -> Windows.Data.Pdf.PdfPageDimensions: ...
    @winrt_mixinmethod
    def get_Rotation(self: Windows.Data.Pdf.IPdfPage) -> Windows.Data.Pdf.PdfPageRotation: ...
    @winrt_mixinmethod
    def get_PreferredZoom(self: Windows.Data.Pdf.IPdfPage) -> Single: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Index = property(get_Index, None)
    Size = property(get_Size, None)
    Dimensions = property(get_Dimensions, None)
    Rotation = property(get_Rotation, None)
    PreferredZoom = property(get_PreferredZoom, None)
class PdfPageDimensions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Pdf.PdfPageDimensions'
    @winrt_mixinmethod
    def get_MediaBox(self: Windows.Data.Pdf.IPdfPageDimensions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CropBox(self: Windows.Data.Pdf.IPdfPageDimensions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_BleedBox(self: Windows.Data.Pdf.IPdfPageDimensions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_TrimBox(self: Windows.Data.Pdf.IPdfPageDimensions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ArtBox(self: Windows.Data.Pdf.IPdfPageDimensions) -> Windows.Foundation.Rect: ...
    MediaBox = property(get_MediaBox, None)
    CropBox = property(get_CropBox, None)
    BleedBox = property(get_BleedBox, None)
    TrimBox = property(get_TrimBox, None)
    ArtBox = property(get_ArtBox, None)
class PdfPageRenderOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Pdf.PdfPageRenderOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Data.Pdf.PdfPageRenderOptions: ...
    @winrt_mixinmethod
    def get_SourceRect(self: Windows.Data.Pdf.IPdfPageRenderOptions) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_SourceRect(self: Windows.Data.Pdf.IPdfPageRenderOptions, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationWidth(self: Windows.Data.Pdf.IPdfPageRenderOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_DestinationWidth(self: Windows.Data.Pdf.IPdfPageRenderOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationHeight(self: Windows.Data.Pdf.IPdfPageRenderOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_DestinationHeight(self: Windows.Data.Pdf.IPdfPageRenderOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.Data.Pdf.IPdfPageRenderOptions) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.Data.Pdf.IPdfPageRenderOptions, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_IsIgnoringHighContrast(self: Windows.Data.Pdf.IPdfPageRenderOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIgnoringHighContrast(self: Windows.Data.Pdf.IPdfPageRenderOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BitmapEncoderId(self: Windows.Data.Pdf.IPdfPageRenderOptions) -> Guid: ...
    @winrt_mixinmethod
    def put_BitmapEncoderId(self: Windows.Data.Pdf.IPdfPageRenderOptions, value: Guid) -> Void: ...
    SourceRect = property(get_SourceRect, put_SourceRect)
    DestinationWidth = property(get_DestinationWidth, put_DestinationWidth)
    DestinationHeight = property(get_DestinationHeight, put_DestinationHeight)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    IsIgnoringHighContrast = property(get_IsIgnoringHighContrast, put_IsIgnoringHighContrast)
    BitmapEncoderId = property(get_BitmapEncoderId, put_BitmapEncoderId)
PdfPageRotation = Int32
PdfPageRotation_Normal: PdfPageRotation = 0
PdfPageRotation_Rotate90: PdfPageRotation = 1
PdfPageRotation_Rotate180: PdfPageRotation = 2
PdfPageRotation_Rotate270: PdfPageRotation = 3
make_head(_module, 'IPdfDocument')
make_head(_module, 'IPdfDocumentStatics')
make_head(_module, 'IPdfPage')
make_head(_module, 'IPdfPageDimensions')
make_head(_module, 'IPdfPageRenderOptions')
make_head(_module, 'PdfDocument')
make_head(_module, 'PdfPage')
make_head(_module, 'PdfPageDimensions')
make_head(_module, 'PdfPageRenderOptions')
