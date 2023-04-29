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
import Windows.Foundation.Numerics
import Windows.Media.Devices.Core
import Windows.Media.MediaProperties
import Windows.Perception.Spatial
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CameraIntrinsics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.CameraIntrinsics'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Devices.Core.ICameraIntrinsicsFactory, focalLength: Windows.Foundation.Numerics.Vector2, principalPoint: Windows.Foundation.Numerics.Vector2, radialDistortion: Windows.Foundation.Numerics.Vector3, tangentialDistortion: Windows.Foundation.Numerics.Vector2, imageWidth: UInt32, imageHeight: UInt32) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def get_FocalLength(self: Windows.Media.Devices.Core.ICameraIntrinsics) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_PrincipalPoint(self: Windows.Media.Devices.Core.ICameraIntrinsics) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_RadialDistortion(self: Windows.Media.Devices.Core.ICameraIntrinsics) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_TangentialDistortion(self: Windows.Media.Devices.Core.ICameraIntrinsics) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_ImageWidth(self: Windows.Media.Devices.Core.ICameraIntrinsics) -> UInt32: ...
    @winrt_mixinmethod
    def get_ImageHeight(self: Windows.Media.Devices.Core.ICameraIntrinsics) -> UInt32: ...
    @winrt_mixinmethod
    def ProjectOntoFrame(self: Windows.Media.Devices.Core.ICameraIntrinsics, coordinate: Windows.Foundation.Numerics.Vector3) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def UnprojectAtUnitDepth(self: Windows.Media.Devices.Core.ICameraIntrinsics, pixelCoordinate: Windows.Foundation.Point) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def ProjectManyOntoFrame(self: Windows.Media.Devices.Core.ICameraIntrinsics, coordinates: POINTER(Windows.Foundation.Numerics.Vector3_head), results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_mixinmethod
    def UnprojectPixelsAtUnitDepth(self: Windows.Media.Devices.Core.ICameraIntrinsics, pixelCoordinates: POINTER(Windows.Foundation.Point_head), results: POINTER(Windows.Foundation.Numerics.Vector2_head)) -> Void: ...
    @winrt_mixinmethod
    def get_UndistortedProjectionTransform(self: Windows.Media.Devices.Core.ICameraIntrinsics2) -> Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def DistortPoint(self: Windows.Media.Devices.Core.ICameraIntrinsics2, input: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def DistortPoints(self: Windows.Media.Devices.Core.ICameraIntrinsics2, inputs: POINTER(Windows.Foundation.Point_head), results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_mixinmethod
    def UndistortPoint(self: Windows.Media.Devices.Core.ICameraIntrinsics2, input: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def UndistortPoints(self: Windows.Media.Devices.Core.ICameraIntrinsics2, inputs: POINTER(Windows.Foundation.Point_head), results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    FocalLength = property(get_FocalLength, None)
    PrincipalPoint = property(get_PrincipalPoint, None)
    RadialDistortion = property(get_RadialDistortion, None)
    TangentialDistortion = property(get_TangentialDistortion, None)
    ImageWidth = property(get_ImageWidth, None)
    ImageHeight = property(get_ImageHeight, None)
    UndistortedProjectionTransform = property(get_UndistortedProjectionTransform, None)
class DepthCorrelatedCoordinateMapper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.DepthCorrelatedCoordinateMapper'
    @winrt_mixinmethod
    def UnprojectPoint(self: Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoint: Windows.Foundation.Point, targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def UnprojectPoints(self: Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoints: POINTER(Windows.Foundation.Point_head), targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Void: ...
    @winrt_mixinmethod
    def MapPoint(self: Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoint: Windows.Foundation.Point, targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: Windows.Media.Devices.Core.CameraIntrinsics) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def MapPoints(self: Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoints: POINTER(Windows.Foundation.Point_head), targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: Windows.Media.Devices.Core.CameraIntrinsics, results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class FrameControlCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameControlCapabilities'
    @winrt_mixinmethod
    def get_Exposure(self: Windows.Media.Devices.Core.IFrameControlCapabilities) -> Windows.Media.Devices.Core.FrameExposureCapabilities: ...
    @winrt_mixinmethod
    def get_ExposureCompensation(self: Windows.Media.Devices.Core.IFrameControlCapabilities) -> Windows.Media.Devices.Core.FrameExposureCompensationCapabilities: ...
    @winrt_mixinmethod
    def get_IsoSpeed(self: Windows.Media.Devices.Core.IFrameControlCapabilities) -> Windows.Media.Devices.Core.FrameIsoSpeedCapabilities: ...
    @winrt_mixinmethod
    def get_Focus(self: Windows.Media.Devices.Core.IFrameControlCapabilities) -> Windows.Media.Devices.Core.FrameFocusCapabilities: ...
    @winrt_mixinmethod
    def get_PhotoConfirmationSupported(self: Windows.Media.Devices.Core.IFrameControlCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Flash(self: Windows.Media.Devices.Core.IFrameControlCapabilities2) -> Windows.Media.Devices.Core.FrameFlashCapabilities: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    IsoSpeed = property(get_IsoSpeed, None)
    Focus = property(get_Focus, None)
    PhotoConfirmationSupported = property(get_PhotoConfirmationSupported, None)
    Flash = property(get_Flash, None)
class FrameController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameController'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Devices.Core.FrameController: ...
    @winrt_mixinmethod
    def get_ExposureControl(self: Windows.Media.Devices.Core.IFrameController) -> Windows.Media.Devices.Core.FrameExposureControl: ...
    @winrt_mixinmethod
    def get_ExposureCompensationControl(self: Windows.Media.Devices.Core.IFrameController) -> Windows.Media.Devices.Core.FrameExposureCompensationControl: ...
    @winrt_mixinmethod
    def get_IsoSpeedControl(self: Windows.Media.Devices.Core.IFrameController) -> Windows.Media.Devices.Core.FrameIsoSpeedControl: ...
    @winrt_mixinmethod
    def get_FocusControl(self: Windows.Media.Devices.Core.IFrameController) -> Windows.Media.Devices.Core.FrameFocusControl: ...
    @winrt_mixinmethod
    def get_PhotoConfirmationEnabled(self: Windows.Media.Devices.Core.IFrameController) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_PhotoConfirmationEnabled(self: Windows.Media.Devices.Core.IFrameController, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_FlashControl(self: Windows.Media.Devices.Core.IFrameController2) -> Windows.Media.Devices.Core.FrameFlashControl: ...
    ExposureControl = property(get_ExposureControl, None)
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    FocusControl = property(get_FocusControl, None)
    PhotoConfirmationEnabled = property(get_PhotoConfirmationEnabled, put_PhotoConfirmationEnabled)
    FlashControl = property(get_FlashControl, None)
class FrameExposureCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameExposureCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.Core.IFrameExposureCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.Core.IFrameExposureCapabilities) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.Core.IFrameExposureCapabilities) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.Core.IFrameExposureCapabilities) -> Windows.Foundation.TimeSpan: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class FrameExposureCompensationCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameExposureCompensationCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Single: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Single: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Single: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class FrameExposureCompensationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameExposureCompensationControl'
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.Core.IFrameExposureCompensationControl) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.Core.IFrameExposureCompensationControl, value: Windows.Foundation.IReference[Single]) -> Void: ...
    Value = property(get_Value, put_Value)
class FrameExposureControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameExposureControl'
    @winrt_mixinmethod
    def get_Auto(self: Windows.Media.Devices.Core.IFrameExposureControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: Windows.Media.Devices.Core.IFrameExposureControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.Core.IFrameExposureControl) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.Core.IFrameExposureControl, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class FrameFlashCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameFlashCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.Core.IFrameFlashCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_RedEyeReductionSupported(self: Windows.Media.Devices.Core.IFrameFlashCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerSupported(self: Windows.Media.Devices.Core.IFrameFlashCapabilities) -> Boolean: ...
    Supported = property(get_Supported, None)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    PowerSupported = property(get_PowerSupported, None)
class FrameFlashControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameFlashControl'
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Devices.Core.IFrameFlashControl) -> Windows.Media.Devices.Core.FrameFlashMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Devices.Core.IFrameFlashControl, value: Windows.Media.Devices.Core.FrameFlashMode) -> Void: ...
    @winrt_mixinmethod
    def get_Auto(self: Windows.Media.Devices.Core.IFrameFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: Windows.Media.Devices.Core.IFrameFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RedEyeReduction(self: Windows.Media.Devices.Core.IFrameFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_RedEyeReduction(self: Windows.Media.Devices.Core.IFrameFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PowerPercent(self: Windows.Media.Devices.Core.IFrameFlashControl) -> Single: ...
    @winrt_mixinmethod
    def put_PowerPercent(self: Windows.Media.Devices.Core.IFrameFlashControl, value: Single) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Auto = property(get_Auto, put_Auto)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
FrameFlashMode = Int32
FrameFlashMode_Disable: FrameFlashMode = 0
FrameFlashMode_Enable: FrameFlashMode = 1
FrameFlashMode_Global: FrameFlashMode = 2
class FrameFocusCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameFocusCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.Core.IFrameFocusCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.Core.IFrameFocusCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.Core.IFrameFocusCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.Core.IFrameFocusCapabilities) -> UInt32: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class FrameFocusControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameFocusControl'
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.Core.IFrameFocusControl) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.Core.IFrameFocusControl, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    Value = property(get_Value, put_Value)
class FrameIsoSpeedCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameIsoSpeedCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> UInt32: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class FrameIsoSpeedControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.FrameIsoSpeedControl'
    @winrt_mixinmethod
    def get_Auto(self: Windows.Media.Devices.Core.IFrameIsoSpeedControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: Windows.Media.Devices.Core.IFrameIsoSpeedControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Devices.Core.IFrameIsoSpeedControl) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Media.Devices.Core.IFrameIsoSpeedControl, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class ICameraIntrinsics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0aa6ed32-6589-49da-af-de-59-42-70-ca-0a-ac')
    @winrt_commethod(6)
    def get_FocalLength(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def get_PrincipalPoint(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(8)
    def get_RadialDistortion(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_TangentialDistortion(self) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(10)
    def get_ImageWidth(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_ImageHeight(self) -> UInt32: ...
    @winrt_commethod(12)
    def ProjectOntoFrame(self, coordinate: Windows.Foundation.Numerics.Vector3) -> Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def UnprojectAtUnitDepth(self, pixelCoordinate: Windows.Foundation.Point) -> Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(14)
    def ProjectManyOntoFrame(self, coordinates: POINTER(Windows.Foundation.Numerics.Vector3_head), results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_commethod(15)
    def UnprojectPixelsAtUnitDepth(self, pixelCoordinates: POINTER(Windows.Foundation.Point_head), results: POINTER(Windows.Foundation.Numerics.Vector2_head)) -> Void: ...
    FocalLength = property(get_FocalLength, None)
    PrincipalPoint = property(get_PrincipalPoint, None)
    RadialDistortion = property(get_RadialDistortion, None)
    TangentialDistortion = property(get_TangentialDistortion, None)
    ImageWidth = property(get_ImageWidth, None)
    ImageHeight = property(get_ImageHeight, None)
class ICameraIntrinsics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0cdaa447-0798-4b4d-83-9f-c5-ec-41-4d-b2-7a')
    @winrt_commethod(6)
    def get_UndistortedProjectionTransform(self) -> Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(7)
    def DistortPoint(self, input: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def DistortPoints(self, inputs: POINTER(Windows.Foundation.Point_head), results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_commethod(9)
    def UndistortPoint(self, input: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def UndistortPoints(self, inputs: POINTER(Windows.Foundation.Point_head), results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    UndistortedProjectionTransform = property(get_UndistortedProjectionTransform, None)
class ICameraIntrinsicsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0ddc486-2132-4a34-a6-59-9b-fe-2a-05-57-12')
    @winrt_commethod(6)
    def Create(self, focalLength: Windows.Foundation.Numerics.Vector2, principalPoint: Windows.Foundation.Numerics.Vector2, radialDistortion: Windows.Foundation.Numerics.Vector3, tangentialDistortion: Windows.Foundation.Numerics.Vector2, imageWidth: UInt32, imageHeight: UInt32) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
class IDepthCorrelatedCoordinateMapper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f95d89fb-8af0-4cb0-92-6d-69-68-66-e5-04-6a')
    @winrt_commethod(6)
    def UnprojectPoint(self, sourcePoint: Windows.Foundation.Point, targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def UnprojectPoints(self, sourcePoints: POINTER(Windows.Foundation.Point_head), targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Void: ...
    @winrt_commethod(8)
    def MapPoint(self, sourcePoint: Windows.Foundation.Point, targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: Windows.Media.Devices.Core.CameraIntrinsics) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def MapPoints(self, sourcePoints: POINTER(Windows.Foundation.Point_head), targetCoordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: Windows.Media.Devices.Core.CameraIntrinsics, results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
class IFrameControlCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a8ffae60-4e9e-4377-a7-89-e2-4c-4a-e7-e5-44')
    @winrt_commethod(6)
    def get_Exposure(self) -> Windows.Media.Devices.Core.FrameExposureCapabilities: ...
    @winrt_commethod(7)
    def get_ExposureCompensation(self) -> Windows.Media.Devices.Core.FrameExposureCompensationCapabilities: ...
    @winrt_commethod(8)
    def get_IsoSpeed(self) -> Windows.Media.Devices.Core.FrameIsoSpeedCapabilities: ...
    @winrt_commethod(9)
    def get_Focus(self) -> Windows.Media.Devices.Core.FrameFocusCapabilities: ...
    @winrt_commethod(10)
    def get_PhotoConfirmationSupported(self) -> Boolean: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    IsoSpeed = property(get_IsoSpeed, None)
    Focus = property(get_Focus, None)
    PhotoConfirmationSupported = property(get_PhotoConfirmationSupported, None)
class IFrameControlCapabilities2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce9b0464-4730-440f-bd-3e-ef-e8-a8-f2-30-a8')
    @winrt_commethod(6)
    def get_Flash(self) -> Windows.Media.Devices.Core.FrameFlashCapabilities: ...
    Flash = property(get_Flash, None)
class IFrameController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c16459d9-baef-4052-91-77-48-af-f2-af-75-22')
    @winrt_commethod(6)
    def get_ExposureControl(self) -> Windows.Media.Devices.Core.FrameExposureControl: ...
    @winrt_commethod(7)
    def get_ExposureCompensationControl(self) -> Windows.Media.Devices.Core.FrameExposureCompensationControl: ...
    @winrt_commethod(8)
    def get_IsoSpeedControl(self) -> Windows.Media.Devices.Core.FrameIsoSpeedControl: ...
    @winrt_commethod(9)
    def get_FocusControl(self) -> Windows.Media.Devices.Core.FrameFocusControl: ...
    @winrt_commethod(10)
    def get_PhotoConfirmationEnabled(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(11)
    def put_PhotoConfirmationEnabled(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    ExposureControl = property(get_ExposureControl, None)
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    FocusControl = property(get_FocusControl, None)
    PhotoConfirmationEnabled = property(get_PhotoConfirmationEnabled, put_PhotoConfirmationEnabled)
class IFrameController2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00d3bc75-d87c-485b-8a-09-5c-35-85-68-b4-27')
    @winrt_commethod(6)
    def get_FlashControl(self) -> Windows.Media.Devices.Core.FrameFlashControl: ...
    FlashControl = property(get_FlashControl, None)
class IFrameExposureCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bdbe9ce3-3985-4e72-97-c2-05-90-d6-13-07-a1')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Max(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Step(self) -> Windows.Foundation.TimeSpan: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class IFrameExposureCompensationCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b988a823-8065-41ee-b0-4f-72-22-65-95-45-00')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> Single: ...
    @winrt_commethod(8)
    def get_Max(self) -> Single: ...
    @winrt_commethod(9)
    def get_Step(self) -> Single: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class IFrameExposureCompensationControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e95896c9-f7f9-48ca-85-91-a2-65-31-cb-15-78')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(7)
    def put_Value(self, value: Windows.Foundation.IReference[Single]) -> Void: ...
    Value = property(get_Value, put_Value)
class IFrameExposureControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b1605a61-ffaf-4752-b6-21-f5-b6-f1-17-f4-32')
    @winrt_commethod(6)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Auto(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def put_Value(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class IFrameFlashCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bb9341a2-5ebe-4f62-82-23-0e-2b-05-bf-bb-d0')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_RedEyeReductionSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_PowerSupported(self) -> Boolean: ...
    Supported = property(get_Supported, None)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    PowerSupported = property(get_PowerSupported, None)
class IFrameFlashControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('75d5f6c7-bd45-4fab-93-75-45-ac-04-b3-32-c2')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.Media.Devices.Core.FrameFlashMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.Media.Devices.Core.FrameFlashMode) -> Void: ...
    @winrt_commethod(8)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Auto(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_RedEyeReduction(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_RedEyeReduction(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_PowerPercent(self) -> Single: ...
    @winrt_commethod(13)
    def put_PowerPercent(self, value: Single) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    Auto = property(get_Auto, put_Auto)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
class IFrameFocusCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7b25cd58-01c0-4065-9c-40-c1-a7-21-42-5c-1a')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Step(self) -> UInt32: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class IFrameFocusControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('272df1d0-d912-4214-a6-7b-e3-8a-8d-48-d8-c6')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_Value(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    Value = property(get_Value, put_Value)
class IFrameIsoSpeedCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('16bdff61-6df6-4ac9-b9-2a-9f-6e-cd-1a-d2-fa')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Step(self) -> UInt32: ...
    Supported = property(get_Supported, None)
    Min = property(get_Min, None)
    Max = property(get_Max, None)
    Step = property(get_Step, None)
class IFrameIsoSpeedControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1a03efed-786a-4c75-a5-57-7a-b9-a8-5f-58-8c')
    @winrt_commethod(6)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Auto(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def put_Value(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class IVariablePhotoSequenceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7fbff880-ed8c-43fd-a7-c3-b3-58-09-e4-22-9a')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxPhotosPerSecond(self) -> Single: ...
    @winrt_commethod(8)
    def get_PhotosPerSecondLimit(self) -> Single: ...
    @winrt_commethod(9)
    def put_PhotosPerSecondLimit(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def GetHighestConcurrentFrameRate(self, captureProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(11)
    def GetCurrentFrameRate(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(12)
    def get_FrameCapabilities(self) -> Windows.Media.Devices.Core.FrameControlCapabilities: ...
    @winrt_commethod(13)
    def get_DesiredFrameControllers(self) -> Windows.Foundation.Collections.IVector[Windows.Media.Devices.Core.FrameController]: ...
    Supported = property(get_Supported, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    FrameCapabilities = property(get_FrameCapabilities, None)
    DesiredFrameControllers = property(get_DesiredFrameControllers, None)
class VariablePhotoSequenceController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Devices.Core.VariablePhotoSequenceController'
    @winrt_mixinmethod
    def get_Supported(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPhotosPerSecond(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Single: ...
    @winrt_mixinmethod
    def get_PhotosPerSecondLimit(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Single: ...
    @winrt_mixinmethod
    def put_PhotosPerSecondLimit(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def GetHighestConcurrentFrameRate(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController, captureProperties: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def GetCurrentFrameRate(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_FrameCapabilities(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Windows.Media.Devices.Core.FrameControlCapabilities: ...
    @winrt_mixinmethod
    def get_DesiredFrameControllers(self: Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Windows.Foundation.Collections.IVector[Windows.Media.Devices.Core.FrameController]: ...
    Supported = property(get_Supported, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    FrameCapabilities = property(get_FrameCapabilities, None)
    DesiredFrameControllers = property(get_DesiredFrameControllers, None)
make_head(_module, 'CameraIntrinsics')
make_head(_module, 'DepthCorrelatedCoordinateMapper')
make_head(_module, 'FrameControlCapabilities')
make_head(_module, 'FrameController')
make_head(_module, 'FrameExposureCapabilities')
make_head(_module, 'FrameExposureCompensationCapabilities')
make_head(_module, 'FrameExposureCompensationControl')
make_head(_module, 'FrameExposureControl')
make_head(_module, 'FrameFlashCapabilities')
make_head(_module, 'FrameFlashControl')
make_head(_module, 'FrameFocusCapabilities')
make_head(_module, 'FrameFocusControl')
make_head(_module, 'FrameIsoSpeedCapabilities')
make_head(_module, 'FrameIsoSpeedControl')
make_head(_module, 'ICameraIntrinsics')
make_head(_module, 'ICameraIntrinsics2')
make_head(_module, 'ICameraIntrinsicsFactory')
make_head(_module, 'IDepthCorrelatedCoordinateMapper')
make_head(_module, 'IFrameControlCapabilities')
make_head(_module, 'IFrameControlCapabilities2')
make_head(_module, 'IFrameController')
make_head(_module, 'IFrameController2')
make_head(_module, 'IFrameExposureCapabilities')
make_head(_module, 'IFrameExposureCompensationCapabilities')
make_head(_module, 'IFrameExposureCompensationControl')
make_head(_module, 'IFrameExposureControl')
make_head(_module, 'IFrameFlashCapabilities')
make_head(_module, 'IFrameFlashControl')
make_head(_module, 'IFrameFocusCapabilities')
make_head(_module, 'IFrameFocusControl')
make_head(_module, 'IFrameIsoSpeedCapabilities')
make_head(_module, 'IFrameIsoSpeedControl')
make_head(_module, 'IVariablePhotoSequenceController')
make_head(_module, 'VariablePhotoSequenceController')
