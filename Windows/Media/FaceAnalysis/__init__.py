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
import Windows.Graphics.Imaging
import Windows.Media
import Windows.Media.FaceAnalysis
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DetectedFace(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.FaceAnalysis.IDetectedFace
    _classid_ = 'Windows.Media.FaceAnalysis.DetectedFace'
    @winrt_mixinmethod
    def get_FaceBox(self: Windows.Media.FaceAnalysis.IDetectedFace) -> Windows.Graphics.Imaging.BitmapBounds: ...
    FaceBox = property(get_FaceBox, None)
class _FaceDetector_Meta_(ComPtr.__class__):
    pass
class FaceDetector(ComPtr, metaclass=_FaceDetector_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.FaceAnalysis.IFaceDetector
    _classid_ = 'Windows.Media.FaceAnalysis.FaceDetector'
    @winrt_mixinmethod
    def DetectFacesAsync(self: Windows.Media.FaceAnalysis.IFaceDetector, image: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_mixinmethod
    def DetectFacesWithSearchAreaAsync(self: Windows.Media.FaceAnalysis.IFaceDetector, image: Windows.Graphics.Imaging.SoftwareBitmap, searchArea: Windows.Graphics.Imaging.BitmapBounds) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_mixinmethod
    def get_MinDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceDetector) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MinDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceDetector, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceDetector) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MaxDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceDetector, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Media.FaceAnalysis.IFaceDetectorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Media.FaceAnalysis.FaceDetector]: ...
    @winrt_classmethod
    def GetSupportedBitmapPixelFormats(cls: Windows.Media.FaceAnalysis.IFaceDetectorStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_classmethod
    def IsBitmapPixelFormatSupported(cls: Windows.Media.FaceAnalysis.IFaceDetectorStatics, bitmapPixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_classmethod
    def get_IsSupported(cls: Windows.Media.FaceAnalysis.IFaceDetectorStatics) -> Boolean: ...
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
    _FaceDetector_Meta_.IsSupported = property(get_IsSupported.__wrapped__, None)
class _FaceTracker_Meta_(ComPtr.__class__):
    pass
class FaceTracker(ComPtr, metaclass=_FaceTracker_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.FaceAnalysis.IFaceTracker
    _classid_ = 'Windows.Media.FaceAnalysis.FaceTracker'
    @winrt_mixinmethod
    def ProcessNextFrameAsync(self: Windows.Media.FaceAnalysis.IFaceTracker, videoFrame: Windows.Media.VideoFrame) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_mixinmethod
    def get_MinDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceTracker) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MinDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceTracker, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceTracker) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_MaxDetectableFaceSize(self: Windows.Media.FaceAnalysis.IFaceTracker, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Media.FaceAnalysis.IFaceTrackerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Media.FaceAnalysis.FaceTracker]: ...
    @winrt_classmethod
    def GetSupportedBitmapPixelFormats(cls: Windows.Media.FaceAnalysis.IFaceTrackerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_classmethod
    def IsBitmapPixelFormatSupported(cls: Windows.Media.FaceAnalysis.IFaceTrackerStatics, bitmapPixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_classmethod
    def get_IsSupported(cls: Windows.Media.FaceAnalysis.IFaceTrackerStatics) -> Boolean: ...
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
    _FaceTracker_Meta_.IsSupported = property(get_IsSupported.__wrapped__, None)
class IDetectedFace(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IDetectedFace'
    _iid_ = Guid('{8200d454-66bc-34df-9410-e89400195414}')
    @winrt_commethod(6)
    def get_FaceBox(self) -> Windows.Graphics.Imaging.BitmapBounds: ...
    FaceBox = property(get_FaceBox, None)
class IFaceDetector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceDetector'
    _iid_ = Guid('{16b672dc-fe6f-3117-8d95-c3f04d51630c}')
    @winrt_commethod(6)
    def DetectFacesAsync(self, image: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_commethod(7)
    def DetectFacesWithSearchAreaAsync(self, image: Windows.Graphics.Imaging.SoftwareBitmap, searchArea: Windows.Graphics.Imaging.BitmapBounds) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_commethod(8)
    def get_MinDetectableFaceSize(self) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(9)
    def put_MinDetectableFaceSize(self, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_commethod(10)
    def get_MaxDetectableFaceSize(self) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(11)
    def put_MaxDetectableFaceSize(self, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
class IFaceDetectorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceDetectorStatics'
    _iid_ = Guid('{bc042d67-9047-33f6-881b-6746c1b218b8}')
    @winrt_commethod(6)
    def CreateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.FaceAnalysis.FaceDetector]: ...
    @winrt_commethod(7)
    def GetSupportedBitmapPixelFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_commethod(8)
    def IsBitmapPixelFormatSupported(self, bitmapPixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class IFaceTracker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceTracker'
    _iid_ = Guid('{6ba67d8c-a841-4420-93e6-2420a1884fcf}')
    @winrt_commethod(6)
    def ProcessNextFrameAsync(self, videoFrame: Windows.Media.VideoFrame) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.Media.FaceAnalysis.DetectedFace]]: ...
    @winrt_commethod(7)
    def get_MinDetectableFaceSize(self) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(8)
    def put_MinDetectableFaceSize(self, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_commethod(9)
    def get_MaxDetectableFaceSize(self) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(10)
    def put_MaxDetectableFaceSize(self, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    MinDetectableFaceSize = property(get_MinDetectableFaceSize, put_MinDetectableFaceSize)
    MaxDetectableFaceSize = property(get_MaxDetectableFaceSize, put_MaxDetectableFaceSize)
class IFaceTrackerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.FaceAnalysis.IFaceTrackerStatics'
    _iid_ = Guid('{e9629198-1801-3fa5-932e-31d767af6c4d}')
    @winrt_commethod(6)
    def CreateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.FaceAnalysis.FaceTracker]: ...
    @winrt_commethod(7)
    def GetSupportedBitmapPixelFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_commethod(8)
    def IsBitmapPixelFormatSupported(self, bitmapPixelFormat: Windows.Graphics.Imaging.BitmapPixelFormat) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
make_head(_module, 'DetectedFace')
make_head(_module, 'FaceDetector')
make_head(_module, 'FaceTracker')
make_head(_module, 'IDetectedFace')
make_head(_module, 'IFaceDetector')
make_head(_module, 'IFaceDetectorStatics')
make_head(_module, 'IFaceTracker')
make_head(_module, 'IFaceTrackerStatics')
