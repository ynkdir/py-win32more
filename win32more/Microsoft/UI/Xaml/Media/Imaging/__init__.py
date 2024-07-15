from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Media
import win32more.Microsoft.UI.Xaml.Media.Imaging
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class BitmapCreateOptions(Enum, UInt32):
    None_ = 0
    IgnoreImageCache = 8
class _BitmapImage_Meta_(ComPtr.__class__):
    pass
class BitmapImage(ComPtr, metaclass=_BitmapImage_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.BitmapImage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapImage.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapImage.CreateInstanceWithUriSource(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapImage: ...
    @winrt_factorymethod
    def CreateInstanceWithUriSource(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageFactory, uriSource: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapImage: ...
    @winrt_mixinmethod
    def get_CreateOptions(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapCreateOptions: ...
    @winrt_mixinmethod
    def put_CreateOptions(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, value: win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapCreateOptions) -> Void: ...
    @winrt_mixinmethod
    def get_UriSource(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_UriSource(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DecodePixelWidth(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Int32: ...
    @winrt_mixinmethod
    def put_DecodePixelWidth(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DecodePixelHeight(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Int32: ...
    @winrt_mixinmethod
    def put_DecodePixelHeight(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DecodePixelType(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> win32more.Microsoft.UI.Xaml.Media.Imaging.DecodePixelType: ...
    @winrt_mixinmethod
    def put_DecodePixelType(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, value: win32more.Microsoft.UI.Xaml.Media.Imaging.DecodePixelType) -> Void: ...
    @winrt_mixinmethod
    def get_IsAnimatedBitmap(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPlaying(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoPlay(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoPlay(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadProgress(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, handler: win32more.Microsoft.UI.Xaml.Media.Imaging.DownloadProgressEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadProgress(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageOpened(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageOpened(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageFailed(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, handler: win32more.Microsoft.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageFailed(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Play(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImage) -> Void: ...
    @winrt_classmethod
    def get_CreateOptionsProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_UriSourceProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DecodePixelWidthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DecodePixelHeightProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DecodePixelTypeProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsAnimatedBitmapProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsPlayingProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AutoPlayProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Microsoft.UI.Xaml.Media.ImageSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSource
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.BitmapSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapSource: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSource) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSource) -> Int32: ...
    @winrt_mixinmethod
    def SetSource(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSource, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def SetSourceAsync(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSource, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_PixelWidthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PixelHeightProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IBitmapSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
    _BitmapSource_Meta_.PixelHeightProperty = property(get_PixelHeightProperty, None)
    _BitmapSource_Meta_.PixelWidthProperty = property(get_PixelWidthProperty, None)
class DecodePixelType(Enum, Int32):
    Physical = 0
    Logical = 1
class DownloadProgressEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.DownloadProgressEventArgs'
    @winrt_mixinmethod
    def get_Progress(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def put_Progress(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs, value: Int32) -> Void: ...
    Progress = property(get_Progress, put_Progress)
class DownloadProgressEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9a8e4af5-b124-5205-8ae9-3496e063c569}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Media.Imaging.DownloadProgressEventArgs) -> Void: ...
class IBitmapImage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IBitmapImage'
    _iid_ = Guid('{5cc29916-a411-5bc2-a3c5-a00d99a59da8}')
    @winrt_commethod(6)
    def get_CreateOptions(self) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapCreateOptions: ...
    @winrt_commethod(7)
    def put_CreateOptions(self, value: win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapCreateOptions) -> Void: ...
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
    def get_DecodePixelType(self) -> win32more.Microsoft.UI.Xaml.Media.Imaging.DecodePixelType: ...
    @winrt_commethod(15)
    def put_DecodePixelType(self, value: win32more.Microsoft.UI.Xaml.Media.Imaging.DecodePixelType) -> Void: ...
    @winrt_commethod(16)
    def get_IsAnimatedBitmap(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsPlaying(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_AutoPlay(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_AutoPlay(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def add_DownloadProgress(self, handler: win32more.Microsoft.UI.Xaml.Media.Imaging.DownloadProgressEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_DownloadProgress(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_ImageOpened(self, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_ImageOpened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_ImageFailed(self, handler: win32more.Microsoft.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_ImageFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def Play(self) -> Void: ...
    @winrt_commethod(27)
    def Stop(self) -> Void: ...
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    CreateOptions = property(get_CreateOptions, put_CreateOptions)
    DecodePixelHeight = property(get_DecodePixelHeight, put_DecodePixelHeight)
    DecodePixelType = property(get_DecodePixelType, put_DecodePixelType)
    DecodePixelWidth = property(get_DecodePixelWidth, put_DecodePixelWidth)
    IsAnimatedBitmap = property(get_IsAnimatedBitmap, None)
    IsPlaying = property(get_IsPlaying, None)
    UriSource = property(get_UriSource, put_UriSource)
    DownloadProgress = event()
    ImageOpened = event()
    ImageFailed = event()
class IBitmapImageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IBitmapImageFactory'
    _iid_ = Guid('{f037e0e9-f229-522e-95c9-da2211a14b05}')
    @winrt_commethod(6)
    def CreateInstanceWithUriSource(self, uriSource: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapImage: ...
class IBitmapImageStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IBitmapImageStatics'
    _iid_ = Guid('{4bcf71a9-1897-51dc-8e3f-2c5c796d1cd9}')
    @winrt_commethod(6)
    def get_CreateOptionsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_UriSourceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_DecodePixelWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_DecodePixelHeightProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_DecodePixelTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_IsAnimatedBitmapProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_IsPlayingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_AutoPlayProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AutoPlayProperty = property(get_AutoPlayProperty, None)
    CreateOptionsProperty = property(get_CreateOptionsProperty, None)
    DecodePixelHeightProperty = property(get_DecodePixelHeightProperty, None)
    DecodePixelTypeProperty = property(get_DecodePixelTypeProperty, None)
    DecodePixelWidthProperty = property(get_DecodePixelWidthProperty, None)
    IsAnimatedBitmapProperty = property(get_IsAnimatedBitmapProperty, None)
    IsPlayingProperty = property(get_IsPlayingProperty, None)
    UriSourceProperty = property(get_UriSourceProperty, None)
class IBitmapSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IBitmapSource'
    _iid_ = Guid('{8424269d-9b82-534f-8fea-af5b5ef96bf2}')
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
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IBitmapSourceFactory'
    _iid_ = Guid('{0392f025-1868-5876-ad67-12e94a8da5bf}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapSource: ...
class IBitmapSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IBitmapSourceStatics'
    _iid_ = Guid('{efa3745e-4400-5f0b-bdc7-3f2911a3d719}')
    @winrt_commethod(6)
    def get_PixelWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PixelHeightProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PixelHeightProperty = property(get_PixelHeightProperty, None)
    PixelWidthProperty = property(get_PixelWidthProperty, None)
class IDownloadProgressEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IDownloadProgressEventArgs'
    _iid_ = Guid('{9a0ea80b-1a17-50d5-83f3-377738212619}')
    @winrt_commethod(6)
    def get_Progress(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Progress(self, value: Int32) -> Void: ...
    Progress = property(get_Progress, put_Progress)
class IRenderTargetBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap'
    _iid_ = Guid('{cf10407d-fa8b-57a3-9574-710529ae0b04}')
    @winrt_commethod(6)
    def get_PixelWidth(self) -> Int32: ...
    @winrt_commethod(7)
    def get_PixelHeight(self) -> Int32: ...
    @winrt_commethod(8)
    def RenderAsync(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RenderToSizeAsync(self, element: win32more.Microsoft.UI.Xaml.UIElement, scaledWidth: Int32, scaledHeight: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def GetPixelsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
class IRenderTargetBitmapStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmapStatics'
    _iid_ = Guid('{83e822e4-9f84-5986-93b0-e4f7019c367d}')
    @winrt_commethod(6)
    def get_PixelWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PixelHeightProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PixelHeightProperty = property(get_PixelHeightProperty, None)
    PixelWidthProperty = property(get_PixelWidthProperty, None)
class ISoftwareBitmapSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISoftwareBitmapSource'
    _iid_ = Guid('{a6aca802-1f24-5a1e-bf08-781a85ed5511}')
    @winrt_commethod(6)
    def SetBitmapAsync(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
class ISurfaceImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISurfaceImageSource'
    _iid_ = Guid('{ac078d9c-d0e0-5ff9-b73e-98e82e4c8d36}')
class ISurfaceImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISurfaceImageSourceFactory'
    _iid_ = Guid('{09a26ed2-11b3-5ef1-ac56-20d064ccca34}')
    @winrt_commethod(6)
    def CreateInstanceWithDimensions(self, pixelWidth: Int32, pixelHeight: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithDimensionsAndOpacity(self, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
class ISvgImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource'
    _iid_ = Guid('{d5b61d3c-b68d-53a2-b07b-ba6adfdd5887}')
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
    def add_Opened(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceOpenedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_OpenFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_OpenFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def SetSourceAsync(self, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus]: ...
    RasterizePixelHeight = property(get_RasterizePixelHeight, put_RasterizePixelHeight)
    RasterizePixelWidth = property(get_RasterizePixelWidth, put_RasterizePixelWidth)
    UriSource = property(get_UriSource, put_UriSource)
    Opened = event()
    OpenFailed = event()
class ISvgImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceFactory'
    _iid_ = Guid('{2f85673f-ac64-570d-9bda-94fa082eead9}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithUriSource(self, uriSource: win32more.Windows.Foundation.Uri, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource: ...
class ISvgImageSourceFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceFailedEventArgs'
    _iid_ = Guid('{76e66278-7804-5439-a50d-14c5ba896714}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class ISvgImageSourceOpenedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceOpenedEventArgs'
    _iid_ = Guid('{1c9860d5-38d0-5b21-8d48-072f1e254e39}')
class ISvgImageSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceStatics'
    _iid_ = Guid('{e3ad1068-f4c6-5513-a777-2980f0ba41bd}')
    @winrt_commethod(6)
    def get_UriSourceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RasterizePixelWidthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RasterizePixelHeightProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    RasterizePixelHeightProperty = property(get_RasterizePixelHeightProperty, None)
    RasterizePixelWidthProperty = property(get_RasterizePixelWidthProperty, None)
    UriSourceProperty = property(get_UriSourceProperty, None)
class IVirtualSurfaceImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSource'
    _iid_ = Guid('{e4ff96a6-fede-589c-a007-4178b53b6739}')
class IVirtualSurfaceImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSourceFactory'
    _iid_ = Guid('{08490f2c-04a8-5031-b9c7-707060d7cd48}')
    @winrt_commethod(6)
    def CreateInstanceWithDimensions(self, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithDimensionsAndOpacity(self, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean) -> win32more.Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
class IWriteableBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IWriteableBitmap'
    _iid_ = Guid('{78c824a9-0e43-5f1e-93bc-d046cca82b7e}')
    @winrt_commethod(6)
    def get_PixelBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def Invalidate(self) -> Void: ...
    PixelBuffer = property(get_PixelBuffer, None)
class IWriteableBitmapFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IWriteableBitmapFactory'
    _iid_ = Guid('{26e861d9-b080-512b-96c4-80050e7e08d1}')
    @winrt_commethod(6)
    def CreateInstanceWithDimensions(self, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Microsoft.UI.Xaml.Media.Imaging.WriteableBitmap: ...
class IXamlRenderingBackgroundTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTask'
    _iid_ = Guid('{7807000c-a050-5121-ac74-3322d5358e39}')
class IXamlRenderingBackgroundTaskFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskFactory'
    _iid_ = Guid('{205247a3-9ffe-599a-a21a-7181442a9d75}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask: ...
class IXamlRenderingBackgroundTaskOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskOverrides'
    _iid_ = Guid('{18733237-324b-57c0-89b2-5875472acc80}')
    @winrt_commethod(6)
    def OnRun(self, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class _RenderTargetBitmap_Meta_(ComPtr.__class__):
    pass
class RenderTargetBitmap(ComPtr, metaclass=_RenderTargetBitmap_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.ImageSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.RenderTargetBitmap'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.RenderTargetBitmap.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Imaging.RenderTargetBitmap: ...
    @winrt_mixinmethod
    def get_PixelWidth(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap) -> Int32: ...
    @winrt_mixinmethod
    def get_PixelHeight(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap) -> Int32: ...
    @winrt_mixinmethod
    def RenderAsync(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenderToSizeAsync(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap, element: win32more.Microsoft.UI.Xaml.UIElement, scaledWidth: Int32, scaledHeight: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetPixelsAsync(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def get_PixelWidthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmapStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PixelHeightProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IRenderTargetBitmapStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PixelHeight = property(get_PixelHeight, None)
    PixelWidth = property(get_PixelWidth, None)
    _RenderTargetBitmap_Meta_.PixelHeightProperty = property(get_PixelHeightProperty, None)
    _RenderTargetBitmap_Meta_.PixelWidthProperty = property(get_PixelWidthProperty, None)
class SoftwareBitmapSource(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.ImageSource
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.ISoftwareBitmapSource
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.SoftwareBitmapSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.SoftwareBitmapSource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SoftwareBitmapSource: ...
    @winrt_mixinmethod
    def SetBitmapAsync(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISoftwareBitmapSource, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class SurfaceImageSource(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.ImageSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.ISurfaceImageSource
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource.CreateInstanceWithDimensions(*args, None, None))
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource.CreateInstanceWithDimensionsAndOpacity(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDimensions(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDimensionsAndOpacity(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource: ...
class _SvgImageSource_Meta_(ComPtr.__class__):
    pass
class SvgImageSource(ComPtr, metaclass=_SvgImageSource_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.ImageSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.SvgImageSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource.CreateInstanceWithUriSource(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource: ...
    @winrt_factorymethod
    def CreateInstanceWithUriSource(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceFactory, uriSource: win32more.Windows.Foundation.Uri, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource: ...
    @winrt_mixinmethod
    def get_UriSource(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_UriSource(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_RasterizePixelWidth(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource) -> Double: ...
    @winrt_mixinmethod
    def put_RasterizePixelWidth(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RasterizePixelHeight(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource) -> Double: ...
    @winrt_mixinmethod
    def put_RasterizePixelHeight(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, value: Double) -> Void: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceOpenedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OpenFailed(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSource, win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenFailed(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetSourceAsync(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSource, streamSource: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus]: ...
    @winrt_classmethod
    def get_UriSourceProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RasterizePixelWidthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RasterizePixelHeightProperty(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceFailedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceFailedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceFailedEventArgs) -> win32more.Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class SvgImageSourceLoadStatus(Enum, Int32):
    Success = 0
    NetworkError = 1
    InvalidFormat = 2
    Other = 3
class SvgImageSourceOpenedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.ISvgImageSourceOpenedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.SvgImageSourceOpenedEventArgs'
class VirtualSurfaceImageSource(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Imaging.SurfaceImageSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSource
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource.CreateInstanceWithDimensions(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource.CreateInstanceWithDimensionsAndOpacity(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDimensions(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDimensionsAndOpacity(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IVirtualSurfaceImageSourceFactory, pixelWidth: Int32, pixelHeight: Int32, isOpaque: Boolean) -> win32more.Microsoft.UI.Xaml.Media.Imaging.VirtualSurfaceImageSource: ...
class WriteableBitmap(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Imaging.BitmapSource
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IWriteableBitmap
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.WriteableBitmap'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.WriteableBitmap.CreateInstanceWithDimensions(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithDimensions(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IWriteableBitmapFactory, pixelWidth: Int32, pixelHeight: Int32) -> win32more.Microsoft.UI.Xaml.Media.Imaging.WriteableBitmap: ...
    @winrt_mixinmethod
    def get_PixelBuffer(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IWriteableBitmap) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Invalidate(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IWriteableBitmap) -> Void: ...
    PixelBuffer = property(get_PixelBuffer, None)
class XamlRenderingBackgroundTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTask
    _classid_ = 'Microsoft.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Imaging.XamlRenderingBackgroundTask: ...
    @winrt_mixinmethod
    def OnRun(self: win32more.Microsoft.UI.Xaml.Media.Imaging.IXamlRenderingBackgroundTaskOverrides, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...


make_ready(__name__)
