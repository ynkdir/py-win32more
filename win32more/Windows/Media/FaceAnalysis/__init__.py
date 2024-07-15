from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Media.FaceAnalysis
import win32more.Windows.Win32.System.WinRT
class DetectedFace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.FaceAnalysis.IDetectedFace
    _classid_ = 'Windows.Media.FaceAnalysis.DetectedFace'
    @winrt_mixinmethod
    def get_FaceBox(self: win32more.Windows.Media.FaceAnalysis.IDetectedFace) -> win32more.Windows.Graphics.Imaging.BitmapBounds: ...
    FaceBox = property(get_FaceBox, None)
class _FaceDetector_Meta_(ComPtr.__class__):
    pass
class FaceDetector(ComPtr, metaclass=_FaceDetector_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.FaceAnalysis.IFaceDetector
    _classid_ = 'Windows.Media.FaceAnalysis.FaceDetector'
    @winrt_mixinmethod
    def DetectFacesAsync(self: win32more.Windows.Media.FaceAnalysis.IFaceDetector, image: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_mixinmethod
    def DetectFacesWithSearchAreaAsync(self: win32more.Windows.Media.FaceAnalysis.IFaceDetector, image: win32more.Windows.Graphics.Imaging.SoftwareBitmap, searchArea: win32more.Windows.Graphics.Imaging.BitmapBounds) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_mixinmethod
    def get_MinDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceDetector) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MinDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceDetector, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceDetector) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MaxDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceDetector, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Media.FaceAnalysis.IFaceDetectorStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.FaceAnalysis.FaceDetector]: ...
    @winrt_classmethod
    def GetSupportedBitmapPixelFormats(cls: win32more.Windows.Media.FaceAnalysis.IFaceDetectorStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_classmethod
    def IsBitmapPixelFormatSupported(cls: win32more.Windows.Media.FaceAnalysis.IFaceDetectorStatics, bitmapPixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Windows.Media.FaceAnalysis.IFaceDetectorStatics) -> Boolean: ...
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
    _FaceDetector_Meta_.IsSupported = property(get_IsSupported, None)
class _FaceTracker_Meta_(ComPtr.__class__):
    pass
class FaceTracker(ComPtr, metaclass=_FaceTracker_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.FaceAnalysis.IFaceTracker
    _classid_ = 'Windows.Media.FaceAnalysis.FaceTracker'
    @winrt_mixinmethod
    def ProcessNextFrameAsync(self: win32more.Windows.Media.FaceAnalysis.IFaceTracker, videoFrame: win32more.Windows.Media.VideoFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_mixinmethod
    def get_MinDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceTracker) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MinDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceTracker, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceTracker) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MaxDetectableFaceSize(self: win32more.Windows.Media.FaceAnalysis.IFaceTracker, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Media.FaceAnalysis.IFaceTrackerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.FaceAnalysis.FaceTracker]: ...
    @winrt_classmethod
    def GetSupportedBitmapPixelFormats(cls: win32more.Windows.Media.FaceAnalysis.IFaceTrackerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_classmethod
    def IsBitmapPixelFormatSupported(cls: win32more.Windows.Media.FaceAnalysis.IFaceTrackerStatics, bitmapPixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Windows.Media.FaceAnalysis.IFaceTrackerStatics) -> Boolean: ...
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
    _FaceTracker_Meta_.IsSupported = property(get_IsSupported, None)
class IDetectedFace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IDetectedFace'
    _iid_ = Guid('{8200d454-66bc-34df-9410-e89400195414}')
    @winrt_commethod(6)
    def get_FaceBox(self) -> win32more.Windows.Graphics.Imaging.BitmapBounds: ...
    FaceBox = property(get_FaceBox, None)
class IFaceDetector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceDetector'
    _iid_ = Guid('{16b672dc-fe6f-3117-8d95-c3f04d51630c}')
    @winrt_commethod(6)
    def DetectFacesAsync(self, image: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_commethod(7)
    def DetectFacesWithSearchAreaAsync(self, image: win32more.Windows.Graphics.Imaging.SoftwareBitmap, searchArea: win32more.Windows.Graphics.Imaging.BitmapBounds) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_commethod(8)
    def get_MinDetectableFaceSize(self) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(9)
    def put_MinDetectableFaceSize(self, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_commethod(10)
    def get_MaxDetectableFaceSize(self) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(11)
    def put_MaxDetectableFaceSize(self, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
class IFaceDetectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceDetectorStatics'
    _iid_ = Guid('{bc042d67-9047-33f6-881b-6746c1b218b8}')
    @winrt_commethod(6)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.FaceAnalysis.FaceDetector]: ...
    @winrt_commethod(7)
    def GetSupportedBitmapPixelFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_commethod(8)
    def IsBitmapPixelFormatSupported(self, bitmapPixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class IFaceTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceTracker'
    _iid_ = Guid('{6ba67d8c-a841-4420-93e6-2420a1884fcf}')
    @winrt_commethod(6)
    def ProcessNextFrameAsync(self, videoFrame: win32more.Windows.Media.VideoFrame) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_commethod(7)
    def get_MinDetectableFaceSize(self) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(8)
    def put_MinDetectableFaceSize(self, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_commethod(9)
    def get_MaxDetectableFaceSize(self) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(10)
    def put_MaxDetectableFaceSize(self, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
class IFaceTrackerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceTrackerStatics'
    _iid_ = Guid('{e9629198-1801-3fa5-932e-31d767af6c4d}')
    @winrt_commethod(6)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.FaceAnalysis.FaceTracker]: ...
    @winrt_commethod(7)
    def GetSupportedBitmapPixelFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_commethod(8)
    def IsBitmapPixelFormatSupported(self, bitmapPixelFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)


make_ready(__name__)
