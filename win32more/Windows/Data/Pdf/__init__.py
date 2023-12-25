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
import win32more.Windows.Data.Pdf
import win32more.Windows.Foundation
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
class IPdfDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Pdf.IPdfDocument'
    _iid_ = Guid('{ac7ebedd-80fa-4089-846e-81b77ff5a86c}')
    @winrt_commethod(6)
    def GetPage(self, pageIndex: UInt32) -> win32more.Windows.Data.Pdf.PdfPage: ...
    @winrt_commethod(7)
    def get_PageCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_IsPasswordProtected(self) -> Boolean: ...
    PageCount = property(get_PageCount, None)
    IsPasswordProtected = property(get_IsPasswordProtected, None)
class IPdfDocumentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Pdf.IPdfDocumentStatics'
    _iid_ = Guid('{433a0b5f-c007-4788-90f2-08143d922599}')
    @winrt_commethod(6)
    def LoadFromFileAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    @winrt_commethod(7)
    def LoadFromFileWithPasswordAsync(self, file: win32more.Windows.Storage.IStorageFile, password: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    @winrt_commethod(8)
    def LoadFromStreamAsync(self, inputStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    @winrt_commethod(9)
    def LoadFromStreamWithPasswordAsync(self, inputStream: win32more.Windows.Storage.Streams.IRandomAccessStream, password: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
class IPdfPage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Pdf.IPdfPage'
    _iid_ = Guid('{9db4b0c8-5320-4cfc-ad76-493fdad0e594}')
    @winrt_commethod(6)
    def RenderToStreamAsync(self, outputStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RenderWithOptionsToStreamAsync(self, outputStream: win32more.Windows.Storage.Streams.IRandomAccessStream, options: win32more.Windows.Data.Pdf.PdfPageRenderOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def PreparePageAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_Index(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def get_Dimensions(self) -> win32more.Windows.Data.Pdf.PdfPageDimensions: ...
    @winrt_commethod(12)
    def get_Rotation(self) -> win32more.Windows.Data.Pdf.PdfPageRotation: ...
    @winrt_commethod(13)
    def get_PreferredZoom(self) -> Single: ...
    Index = property(get_Index, None)
    Size = property(get_Size, None)
    Dimensions = property(get_Dimensions, None)
    Rotation = property(get_Rotation, None)
    PreferredZoom = property(get_PreferredZoom, None)
class IPdfPageDimensions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Pdf.IPdfPageDimensions'
    _iid_ = Guid('{22170471-313e-44e8-835d-63a3e7624a10}')
    @winrt_commethod(6)
    def get_MediaBox(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_CropBox(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def get_BleedBox(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def get_TrimBox(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def get_ArtBox(self) -> win32more.Windows.Foundation.Rect: ...
    MediaBox = property(get_MediaBox, None)
    CropBox = property(get_CropBox, None)
    BleedBox = property(get_BleedBox, None)
    TrimBox = property(get_TrimBox, None)
    ArtBox = property(get_ArtBox, None)
class IPdfPageRenderOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Pdf.IPdfPageRenderOptions'
    _iid_ = Guid('{3c98056f-b7cf-4c29-9a04-52d90267f425}')
    @winrt_commethod(6)
    def get_SourceRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_SourceRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(8)
    def get_DestinationWidth(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_DestinationWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_DestinationHeight(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_DestinationHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Pdf.IPdfDocument
    _classid_ = 'Windows.Data.Pdf.PdfDocument'
    @winrt_mixinmethod
    def GetPage(self: win32more.Windows.Data.Pdf.IPdfDocument, pageIndex: UInt32) -> win32more.Windows.Data.Pdf.PdfPage: ...
    @winrt_mixinmethod
    def get_PageCount(self: win32more.Windows.Data.Pdf.IPdfDocument) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsPasswordProtected(self: win32more.Windows.Data.Pdf.IPdfDocument) -> Boolean: ...
    @winrt_classmethod
    def LoadFromFileAsync(cls: win32more.Windows.Data.Pdf.IPdfDocumentStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    @winrt_classmethod
    def LoadFromFileWithPasswordAsync(cls: win32more.Windows.Data.Pdf.IPdfDocumentStatics, file: win32more.Windows.Storage.IStorageFile, password: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    @winrt_classmethod
    def LoadFromStreamAsync(cls: win32more.Windows.Data.Pdf.IPdfDocumentStatics, inputStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    @winrt_classmethod
    def LoadFromStreamWithPasswordAsync(cls: win32more.Windows.Data.Pdf.IPdfDocumentStatics, inputStream: win32more.Windows.Storage.Streams.IRandomAccessStream, password: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Data.Pdf.PdfDocument]: ...
    PageCount = property(get_PageCount, None)
    IsPasswordProtected = property(get_IsPasswordProtected, None)
class PdfPage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Pdf.IPdfPage
    _classid_ = 'Windows.Data.Pdf.PdfPage'
    @winrt_mixinmethod
    def RenderToStreamAsync(self: win32more.Windows.Data.Pdf.IPdfPage, outputStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenderWithOptionsToStreamAsync(self: win32more.Windows.Data.Pdf.IPdfPage, outputStream: win32more.Windows.Storage.Streams.IRandomAccessStream, options: win32more.Windows.Data.Pdf.PdfPageRenderOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PreparePageAsync(self: win32more.Windows.Data.Pdf.IPdfPage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Index(self: win32more.Windows.Data.Pdf.IPdfPage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Data.Pdf.IPdfPage) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_Dimensions(self: win32more.Windows.Data.Pdf.IPdfPage) -> win32more.Windows.Data.Pdf.PdfPageDimensions: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Windows.Data.Pdf.IPdfPage) -> win32more.Windows.Data.Pdf.PdfPageRotation: ...
    @winrt_mixinmethod
    def get_PreferredZoom(self: win32more.Windows.Data.Pdf.IPdfPage) -> Single: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Index = property(get_Index, None)
    Size = property(get_Size, None)
    Dimensions = property(get_Dimensions, None)
    Rotation = property(get_Rotation, None)
    PreferredZoom = property(get_PreferredZoom, None)
class PdfPageDimensions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Pdf.IPdfPageDimensions
    _classid_ = 'Windows.Data.Pdf.PdfPageDimensions'
    @winrt_mixinmethod
    def get_MediaBox(self: win32more.Windows.Data.Pdf.IPdfPageDimensions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_CropBox(self: win32more.Windows.Data.Pdf.IPdfPageDimensions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_BleedBox(self: win32more.Windows.Data.Pdf.IPdfPageDimensions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_TrimBox(self: win32more.Windows.Data.Pdf.IPdfPageDimensions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ArtBox(self: win32more.Windows.Data.Pdf.IPdfPageDimensions) -> win32more.Windows.Foundation.Rect: ...
    MediaBox = property(get_MediaBox, None)
    CropBox = property(get_CropBox, None)
    BleedBox = property(get_BleedBox, None)
    TrimBox = property(get_TrimBox, None)
    ArtBox = property(get_ArtBox, None)
class PdfPageRenderOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Pdf.IPdfPageRenderOptions
    _classid_ = 'Windows.Data.Pdf.PdfPageRenderOptions'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Data.Pdf.PdfPageRenderOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Data.Pdf.PdfPageRenderOptions: ...
    @winrt_mixinmethod
    def get_SourceRect(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_SourceRect(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationWidth(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_DestinationWidth(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationHeight(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_DestinationHeight(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_IsIgnoringHighContrast(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIgnoringHighContrast(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BitmapEncoderId(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions) -> Guid: ...
    @winrt_mixinmethod
    def put_BitmapEncoderId(self: win32more.Windows.Data.Pdf.IPdfPageRenderOptions, value: Guid) -> Void: ...
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
make_ready(__name__)
