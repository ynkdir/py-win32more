from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI
import win32more.Microsoft.Windows.Media.Capture
import win32more.Windows.Foundation
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class CameraCaptureUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUI
    _classid_ = 'Microsoft.Windows.Media.Capture.CameraCaptureUI'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.Media.Capture.CameraCaptureUI.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIFactory, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUI: ...
    @winrt_mixinmethod
    def get_PhotoSettings(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUI) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_mixinmethod
    def get_VideoSettings(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUI) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_mixinmethod
    def CaptureFileAsync(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUI, mode: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    PhotoSettings = property(get_PhotoSettings, None)
    VideoSettings = property(get_VideoSettings, None)
CameraCaptureUIContract: UInt32 = 65536
class CameraCaptureUIMaxPhotoResolution(Enum, Int32):
    HighestAvailable = 0
    VerySmallQvga = 1
    SmallVga = 2
    MediumXga = 3
    Large3M = 4
    VeryLarge5M = 5
class CameraCaptureUIMaxVideoResolution(Enum, Int32):
    HighestAvailable = 0
    LowDefinition = 1
    StandardDefinition = 2
    HighDefinition = 3
class CameraCaptureUIMode(Enum, Int32):
    PhotoOrVideo = 0
    Photo = 1
    Video = 2
class CameraCaptureUIPhotoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings
    _classid_ = 'Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_mixinmethod
    def get_AllowCropping(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCropping(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CroppedAspectRatio(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CroppedAspectRatio(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_CroppedSizeInPixels(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CroppedSizeInPixels(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_Format(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoFormat: ...
    @winrt_mixinmethod
    def put_Format(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoFormat) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution: ...
    @winrt_mixinmethod
    def put_MaxResolution(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution) -> Void: ...
    AllowCropping = property(get_AllowCropping, put_AllowCropping)
    CroppedAspectRatio = property(get_CroppedAspectRatio, put_CroppedAspectRatio)
    CroppedSizeInPixels = property(get_CroppedSizeInPixels, put_CroppedSizeInPixels)
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class CameraCaptureUIPhotoFormat(Enum, Int32):
    Jpeg = 0
    Png = 1
    JpegXR = 2
class CameraCaptureUIVideoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings
    _classid_ = 'Microsoft.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_mixinmethod
    def get_AllowTrimming(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowTrimming(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Format(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoFormat: ...
    @winrt_mixinmethod
    def put_Format(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoFormat) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDurationInSeconds(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Single: ...
    @winrt_mixinmethod
    def put_MaxDurationInSeconds(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution: ...
    @winrt_mixinmethod
    def put_MaxResolution(self: win32more.Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution) -> Void: ...
    AllowTrimming = property(get_AllowTrimming, put_AllowTrimming)
    Format = property(get_Format, put_Format)
    MaxDurationInSeconds = property(get_MaxDurationInSeconds, put_MaxDurationInSeconds)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class CameraCaptureUIVideoFormat(Enum, Int32):
    Mp4 = 0
    Wmv = 1
class ICameraCaptureUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Media.Capture.ICameraCaptureUI'
    _iid_ = Guid('{c001d024-c617-5742-9ae1-8fd31be07f6c}')
    @winrt_commethod(6)
    def get_PhotoSettings(self) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_commethod(7)
    def get_VideoSettings(self) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_commethod(8)
    def CaptureFileAsync(self, mode: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    PhotoSettings = property(get_PhotoSettings, None)
    VideoSettings = property(get_VideoSettings, None)
class ICameraCaptureUIFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Media.Capture.ICameraCaptureUIFactory'
    _iid_ = Guid('{2b49623d-5f22-5fee-991f-14f24592a3c2}')
    @winrt_commethod(6)
    def CreateInstance(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUI: ...
class ICameraCaptureUIPhotoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings'
    _iid_ = Guid('{19fe2155-d018-53fc-bbdc-5781a94687a0}')
    @winrt_commethod(6)
    def get_AllowCropping(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowCropping(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CroppedAspectRatio(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_CroppedAspectRatio(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(10)
    def get_CroppedSizeInPixels(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def put_CroppedSizeInPixels(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(12)
    def get_Format(self) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoFormat: ...
    @winrt_commethod(13)
    def put_Format(self, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIPhotoFormat) -> Void: ...
    @winrt_commethod(14)
    def get_MaxResolution(self) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution: ...
    @winrt_commethod(15)
    def put_MaxResolution(self, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution) -> Void: ...
    AllowCropping = property(get_AllowCropping, put_AllowCropping)
    CroppedAspectRatio = property(get_CroppedAspectRatio, put_CroppedAspectRatio)
    CroppedSizeInPixels = property(get_CroppedSizeInPixels, put_CroppedSizeInPixels)
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
class ICameraCaptureUIVideoCaptureSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings'
    _iid_ = Guid('{47dd74f6-83b7-5123-bbdf-d757201d1ee8}')
    @winrt_commethod(6)
    def get_AllowTrimming(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowTrimming(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Format(self) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoFormat: ...
    @winrt_commethod(9)
    def put_Format(self, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIVideoFormat) -> Void: ...
    @winrt_commethod(10)
    def get_MaxDurationInSeconds(self) -> Single: ...
    @winrt_commethod(11)
    def put_MaxDurationInSeconds(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_MaxResolution(self) -> win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution: ...
    @winrt_commethod(13)
    def put_MaxResolution(self, value: win32more.Microsoft.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution) -> Void: ...
    AllowTrimming = property(get_AllowTrimming, put_AllowTrimming)
    Format = property(get_Format, put_Format)
    MaxDurationInSeconds = property(get_MaxDurationInSeconds, put_MaxDurationInSeconds)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)


make_ready(__name__)
