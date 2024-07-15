from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Media
import win32more.Windows.UI.Xaml.Media.Imaging
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class BitmapCreateOptions(Enum, UInt32):
    None_ = 0
    IgnoreImageCache = 8
class _BitmapImage_Meta_(ComPtr.__class__):
    pass
class BitmapImage(ComPtr, metaclass=_BitmapImage_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Imaging.BitmapSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.BitmapImage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage.CreateInstanceWithUriSource(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage: ...
    @winrt_factorymethod
    def CreateInstanceWithUriSource(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageFactory, uriSource: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage: ...
    @winrt_mixinmethod
    def get_CreateOptions(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapCreateOptions: ...
    @winrt_mixinmethod
    def put_CreateOptions(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, value: win32more.Windows.UI.Xaml.Media.Imaging.BitmapCreateOptions) -> Void: ...
    @winrt_mixinmethod
    def get_UriSource(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_UriSource(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DecodePixelWidth(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage) -> Int32: ...
    @winrt_mixinmethod
    def put_DecodePixelWidth(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DecodePixelHeight(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage) -> Int32: ...
    @winrt_mixinmethod
    def put_DecodePixelHeight(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadProgress(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, handler: win32more.Windows.UI.Xaml.Media.Imaging.DownloadProgressEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadProgress(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageOpened(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageOpened(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageFailed(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, handler: win32more.Windows.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageFailed(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DecodePixelType(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage2) -> win32more.Windows.UI.Xaml.Media.Imaging.DecodePixelType: ...
    @winrt_mixinmethod
    def put_DecodePixelType(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage2, value: win32more.Windows.UI.Xaml.Media.Imaging.DecodePixelType) -> Void: ...
    @winrt_mixinmethod
    def get_IsAnimatedBitmap(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage3) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlaying(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage3) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoPlay(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage3) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoPlay(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Play(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage3) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImage3) -> Void: ...
    @winrt_classmethod
    def get_IsAnimatedBitmapProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsPlayingProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AutoPlayProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DecodePixelTypeProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CreateOptionsProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_UriSourceProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DecodePixelWidthProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DecodePixelHeightProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    CreateOptions = property(get_CreateOptions, put_CreateOptions)
    DecodePixelHeight = property(get_DecodePixelHeight, put_DecodePixelHeight)
    DecodePixelType = property(get_DecodePixelType, put_DecodePixelType)
    DecodePixelWidth = property(get_DecodePixelWidth, put_DecodePixelWidth)
    IsAnimatedBitmap = property(get_IsAnimatedBitmap, None)
    IsPlaying = property(get_IsPlaying, None)
    UriSource = property(get_UriSource, put_UriSource)
    _BitmapImage_Meta_.AutoPlayProperty = property(get_AutoPlayProperty, None)
    _BitmapImage_Meta_.CreateOptionsProperty = property(get_CreateOptionsProperty, None)
    _BitmapImage_Meta_.DecodePixelHeightProperty = property(get_DecodePixelHeightProperty, None)
    _BitmapImage_Meta_.DecodePixelTypeProperty = property(get_DecodePixelTypeProperty, None)
    _BitmapImage_Meta_.DecodePixelWidthProperty = property(get_DecodePixelWidthProperty, None)
    _BitmapImage_Meta_.IsAnimatedBitmapProperty = property(get_IsAnimatedBitmapProperty, None)
    _BitmapImage_Meta_.IsPlayingProperty = property(get_IsPlayingProperty, None)
    _BitmapImage_Meta_.UriSourceProperty = property(get_UriSourceProperty, None)
    DownloadProgress = event()
    ImageOpened = event()
    ImageFailed = event()
class _BitmapSource_Meta_(ComPtr.__class__):
    pass
class BitmapSource(ComPtr, metaclass=_BitmapSource_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.ImageSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSource
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.BitmapSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.BitmapSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapSource: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSource) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSource) -> Int32: ...
    @winrt_mixinmethod
    def SetSource(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSource, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def SetSourceAsync(self: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSource, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_PixelWidthProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PixelHeightProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IBitmapSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
    _BitmapSource_Meta_.PixelHeightProperty = property(get_PixelHeightProperty, None)
    _BitmapSource_Meta_.PixelWidthProperty = property(get_PixelWidthProperty, None)
class DecodePixelType(Enum, Int32):
    Physical = 0
    Logical = 1
class DownloadProgressEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.DownloadProgressEventArgs'
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def put_Progress(self: win32more.Windows.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs, value: Int32) -> Void: ...
    Progress = property(get_Progress, put_Progress)
class DownloadProgressEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1abaee23-74ee-4cc7-99ba-b171e3cda61e}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Media.Imaging.DownloadProgressEventArgs) -> Void: ...
class IBitmapImage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImage'
    _iid_ = Guid('{31af3271-e3b4-442d-a341-4c0226b2725b}')
    @winrt_commethod(6)
    def get_CreateOptions(self) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapCreateOptions: ...
    @winrt_commethod(7)
    def put_CreateOptions(self, value: win32more.Windows.UI.Xaml.Media.Imaging.BitmapCreateOptions) -> Void: ...
    @winrt_commethod(8)
    def get_UriSource(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_UriSource(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(10)
    def get_DecodePixelWidth(self) -> Int32: ...
    @winrt_commethod(11)
    def put_DecodePixelWidth(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_DecodePixelHeight(self) -> Int32: ...
    @winrt_commethod(13)
    def put_DecodePixelHeight(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def add_DownloadProgress(self, handler: win32more.Windows.UI.Xaml.Media.Imaging.DownloadProgressEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DownloadProgress(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ImageOpened(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ImageOpened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ImageFailed(self, handler: win32more.Windows.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ImageFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CreateOptions = property(get_CreateOptions, put_CreateOptions)
    DecodePixelHeight = property(get_DecodePixelHeight, put_DecodePixelHeight)
    DecodePixelWidth = property(get_DecodePixelWidth, put_DecodePixelWidth)
    UriSource = property(get_UriSource, put_UriSource)
    DownloadProgress = event()
    ImageOpened = event()
    ImageFailed = event()
class IBitmapImage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImage2'
    _iid_ = Guid('{1069c1b6-8c9b-4762-be3d-759f5698f2b3}')
    @winrt_commethod(6)
    def get_DecodePixelType(self) -> win32more.Windows.UI.Xaml.Media.Imaging.DecodePixelType: ...
    @winrt_commethod(7)
    def put_DecodePixelType(self, value: win32more.Windows.UI.Xaml.Media.Imaging.DecodePixelType) -> Void: ...
    DecodePixelType = property(get_DecodePixelType, put_DecodePixelType)
class IBitmapImage3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImage3'
    _iid_ = Guid('{f1de6f26-3c73-453f-a7ba-9b85c18b3733}')
    @winrt_commethod(6)
    def get_IsAnimatedBitmap(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsPlaying(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_AutoPlay(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AutoPlay(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def Play(self) -> Void: ...
    @winrt_commethod(11)
    def Stop(self) -> Void: ...
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    IsAnimatedBitmap = property(get_IsAnimatedBitmap, None)
    IsPlaying = property(get_IsPlaying, None)
class IBitmapImageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImageFactory'
    _iid_ = Guid('{c9132978-4810-4e5e-8087-03671ee60d85}')
    @winrt_commethod(6)
    def CreateInstanceWithUriSource(self, uriSource: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapImage: ...
class IBitmapImageStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics'
    _iid_ = Guid('{9e282143-70e8-437c-9fa4-2cbf295cff84}')
    @winrt_commethod(6)
    def get_CreateOptionsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_UriSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_DecodePixelWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_DecodePixelHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CreateOptionsProperty = property(get_CreateOptionsProperty, None)
    DecodePixelHeightProperty = property(get_DecodePixelHeightProperty, None)
    DecodePixelWidthProperty = property(get_DecodePixelWidthProperty, None)
    UriSourceProperty = property(get_UriSourceProperty, None)
class IBitmapImageStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics2'
    _iid_ = Guid('{c5f5576a-75af-41a4-b893-8fe91fee2882}')
    @winrt_commethod(6)
    def get_DecodePixelTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DecodePixelTypeProperty = property(get_DecodePixelTypeProperty, None)
class IBitmapImageStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapImageStatics3'
    _iid_ = Guid('{2b44e30d-f6d5-4411-a8cd-bf7603c4faa0}')
    @winrt_commethod(6)
    def get_IsAnimatedBitmapProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_IsPlayingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AutoPlayProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AutoPlayProperty = property(get_AutoPlayProperty, None)
    IsAnimatedBitmapProperty = property(get_IsAnimatedBitmapProperty, None)
    IsPlayingProperty = property(get_IsPlayingProperty, None)
class IBitmapSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapSource'
    _iid_ = Guid('{23d86411-202f-41b2-8c5b-a8a3b333800b}')
    @winrt_commethod(6)
    def get_PixelWidth(self) -> Int32: ...
    @winrt_commethod(7)
    def get_PixelHeight(self) -> Int32: ...
    @winrt_commethod(8)
    def SetSource(self, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(9)
    def SetSourceAsync(self, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
class IBitmapSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapSourceFactory'
    _iid_ = Guid('{e240420e-d4a7-49a4-a0b4-a59fdd77e508}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.BitmapSource: ...
class IBitmapSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IBitmapSourceStatics'
    _iid_ = Guid('{9a9c9981-827b-4e51-891b-8a15b511842d}')
    @winrt_commethod(6)
    def get_PixelWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PixelHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PixelHeightProperty = property(get_PixelHeightProperty, None)
    PixelWidthProperty = property(get_PixelWidthProperty, None)
class IDownloadProgressEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs'
    _iid_ = Guid('{7311e0d4-fe94-4e70-9b90-cdd47ac23afb}')
    @winrt_commethod(6)
    def get_Progress(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Progress(self, value: Int32) -> Void: ...
    Progress = property(get_Progress, put_Progress)
class IRenderTargetBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap'
    _iid_ = Guid('{500dee81-893c-4c0a-8fec-4678ac717589}')
    @winrt_commethod(6)
    def get_PixelWidth(self) -> Int32: ...
    @winrt_commethod(7)
    def get_PixelHeight(self) -> Int32: ...
    @winrt_commethod(8)
    def RenderAsync(self, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RenderToSizeAsync(self, element: win32more.Windows.UI.Xaml.UIElement, scaledWidth: Int32, scaledHeight: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def GetPixelsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
class IRenderTargetBitmapStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmapStatics'
    _iid_ = Guid('{f0a1efee-c131-4d40-9c47-f7d7cf2b077f}')
    @winrt_commethod(6)
    def get_PixelWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PixelHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PixelHeightProperty = property(get_PixelHeightProperty, None)
    PixelWidthProperty = property(get_PixelWidthProperty, None)
class ISoftwareBitmapSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISoftwareBitmapSource'
    _iid_ = Guid('{d2dd9ed0-d3c5-4056-91b5-b7c1d1e8130e}')
    @winrt_commethod(6)
    def SetBitmapAsync(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
class ISurfaceImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISurfaceImageSource'
    _iid_ = Guid('{62f7d416-c714-4c4c-8273-f839bc58135c}')
class ISurfaceImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISurfaceImageSourceFactory'
    _iid_ = Guid('{3ab2212a-ef65-4a5f-bfac-73993e8c12c9}')
    @winrt_commethod(6)
    def CreateInstanceWithDimensions(self, pixelWidth: Int32, pixelHeight: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithDimensionsAndOpacity(self, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
class ISvgImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISvgImageSource'
    _iid_ = Guid('{03e1cec3-0ca8-4a4e-8d7c-c808a0838586}')
    @winrt_commethod(6)
    def get_UriSource(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_UriSource(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_RasterizePixelWidth(self) -> Double: ...
    @winrt_commethod(9)
    def put_RasterizePixelWidth(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_RasterizePixelHeight(self) -> Double: ...
    @winrt_commethod(11)
    def put_RasterizePixelHeight(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def add_Opened(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceOpenedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_OpenFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_OpenFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def SetSourceAsync(self, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus]: ...
    RasterizePixelHeight = property(get_RasterizePixelHeight, put_RasterizePixelHeight)
    RasterizePixelWidth = property(get_RasterizePixelWidth, put_RasterizePixelWidth)
    UriSource = property(get_UriSource, put_UriSource)
    Opened = event()
    OpenFailed = event()
class ISvgImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISvgImageSourceFactory'
    _iid_ = Guid('{c794e9e7-cf23-4d72-bf1a-dfaa16d8ea52}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithUriSource(self, uriSource: win32more.Windows.Foundation.Uri, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource: ...
class ISvgImageSourceFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISvgImageSourceFailedEventArgs'
    _iid_ = Guid('{68bb3170-3ccc-4035-ac01-9834543d744e}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class ISvgImageSourceOpenedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISvgImageSourceOpenedEventArgs'
    _iid_ = Guid('{85ef4c16-748e-4008-95c7-6a23dd7316db}')
class ISvgImageSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.ISvgImageSourceStatics'
    _iid_ = Guid('{9c6638ce-bed1-4aab-acbb-d3e2185d315a}')
    @winrt_commethod(6)
    def get_UriSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RasterizePixelWidthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RasterizePixelHeightProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RasterizePixelHeightProperty = property(get_RasterizePixelHeightProperty, None)
    RasterizePixelWidthProperty = property(get_RasterizePixelWidthProperty, None)
    UriSourceProperty = property(get_UriSourceProperty, None)
class IVirtualSurfaceImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSource'
    _iid_ = Guid('{4a711fea-bfac-11e0-a06a-9de44724019b}')
class IVirtualSurfaceImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSourceFactory'
    _iid_ = Guid('{3ab2212a-bfac-11e0-8a92-69e44724019b}')
    @winrt_commethod(6)
    def CreateInstanceWithDimensions(self, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithDimensionsAndOpacity(self, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean) -> win32more.Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
class IWriteableBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IWriteableBitmap'
    _iid_ = Guid('{bf0b7e6f-df7c-4a85-8413-a1216285835c}')
    @winrt_commethod(6)
    def get_PixelBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def Invalidate(self) -> Void: ...
    PixelBuffer = property(get_PixelBuffer, None)
class IWriteableBitmapFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IWriteableBitmapFactory'
    _iid_ = Guid('{5563ebb1-3ef2-42c5-9c6d-1cf5dcc041ff}')
    @winrt_commethod(6)
    def CreateInstanceWithDimensions(self, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Windows.UI.Xaml.Media.Imaging.WriteableBitmap: ...
class IXamlRenderingBackgroundTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTask'
    _iid_ = Guid('{5d5fe9aa-533e-44b8-a975-fc5f1e3bff52}')
class IXamlRenderingBackgroundTaskFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskFactory'
    _iid_ = Guid('{a3d1bb63-38f8-4da3-9fca-fd8128a2cbf9}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask: ...
class IXamlRenderingBackgroundTaskOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskOverrides'
    _iid_ = Guid('{9c2a6997-a908-4711-b4b2-a960db3d8e5a}')
    @winrt_commethod(6)
    def OnRun(self, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class _RenderTargetBitmap_Meta_(ComPtr.__class__):
    pass
class RenderTargetBitmap(ComPtr, metaclass=_RenderTargetBitmap_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.ImageSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.RenderTargetBitmap'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.RenderTargetBitmap.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Imaging.RenderTargetBitmap: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap) -> Int32: ...
    @winrt_mixinmethod
    def RenderAsync(self: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenderToSizeAsync(self: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap, element: win32more.Windows.UI.Xaml.UIElement, scaledWidth: Int32, scaledHeight: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetPixelsAsync(self: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def get_PixelWidthProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmapStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PixelHeightProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.IRenderTargetBitmapStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
    _RenderTargetBitmap_Meta_.PixelHeightProperty = property(get_PixelHeightProperty, None)
    _RenderTargetBitmap_Meta_.PixelWidthProperty = property(get_PixelWidthProperty, None)
class SoftwareBitmapSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.ImageSource
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.ISoftwareBitmapSource
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.SoftwareBitmapSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.SoftwareBitmapSource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Imaging.SoftwareBitmapSource: ...
    @winrt_mixinmethod
    def SetBitmapAsync(self: win32more.Windows.UI.Xaml.Media.Imaging.ISoftwareBitmapSource, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class SurfaceImageSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.ImageSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.ISurfaceImageSource
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.SurfaceImageSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource.CreateInstanceWithDimensions(*args, None, None))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource.CreateInstanceWithDimensionsAndOpacity(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDimensions(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDimensionsAndOpacity(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
class _SvgImageSource_Meta_(ComPtr.__class__):
    pass
class SvgImageSource(ComPtr, metaclass=_SvgImageSource_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.ImageSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.SvgImageSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource.CreateInstanceWithUriSource(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource: ...
    @winrt_factorymethod
    def CreateInstanceWithUriSource(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceFactory, uriSource: win32more.Windows.Foundation.Uri, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource: ...
    @winrt_mixinmethod
    def get_UriSource(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_UriSource(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_RasterizePixelWidth(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource) -> Double: ...
    @winrt_mixinmethod
    def put_RasterizePixelWidth(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RasterizePixelHeight(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource) -> Double: ...
    @winrt_mixinmethod
    def put_RasterizePixelHeight(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, value: Double) -> Void: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceOpenedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OpenFailed(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenFailed(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetSourceAsync(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSource, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus]: ...
    @winrt_classmethod
    def get_UriSourceProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RasterizePixelWidthProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RasterizePixelHeightProperty(cls: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RasterizePixelHeight = property(get_RasterizePixelHeight, put_RasterizePixelHeight)
    RasterizePixelWidth = property(get_RasterizePixelWidth, put_RasterizePixelWidth)
    UriSource = property(get_UriSource, put_UriSource)
    _SvgImageSource_Meta_.RasterizePixelHeightProperty = property(get_RasterizePixelHeightProperty, None)
    _SvgImageSource_Meta_.RasterizePixelWidthProperty = property(get_RasterizePixelWidthProperty, None)
    _SvgImageSource_Meta_.UriSourceProperty = property(get_UriSourceProperty, None)
    Opened = event()
    OpenFailed = event()
class SvgImageSourceFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceFailedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.SvgImageSourceFailedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceFailedEventArgs) -> win32more.Windows.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class SvgImageSourceLoadStatus(Enum, Int32):
    Success = 0
    NetworkError = 1
    InvalidFormat = 2
    Other = 3
class SvgImageSourceOpenedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.ISvgImageSourceOpenedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.SvgImageSourceOpenedEventArgs'
class VirtualSurfaceImageSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Imaging.SurfaceImageSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSource
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource.CreateInstanceWithDimensions(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource.CreateInstanceWithDimensionsAndOpacity(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDimensions(cls: win32more.Windows.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDimensionsAndOpacity(cls: win32more.Windows.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean) -> win32more.Windows.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
class WriteableBitmap(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Imaging.BitmapSource
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IWriteableBitmap
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.WriteableBitmap'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.WriteableBitmap.CreateInstanceWithDimensions(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDimensions(cls: win32more.Windows.UI.Xaml.Media.Imaging.IWriteableBitmapFactory, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Windows.UI.Xaml.Media.Imaging.WriteableBitmap: ...
    @winrt_mixinmethod
    def get_PixelBuffer(self: win32more.Windows.UI.Xaml.Media.Imaging.IWriteableBitmap) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Invalidate(self: win32more.Windows.UI.Xaml.Media.Imaging.IWriteableBitmap) -> Void: ...
    PixelBuffer = property(get_PixelBuffer, None)
class XamlRenderingBackgroundTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTask
    _classid_ = 'Windows.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask: ...
    @winrt_mixinmethod
    def OnRun(self: win32more.Windows.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskOverrides, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...


make_ready(__name__)
