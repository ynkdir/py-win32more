from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Media.Devices.Core
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Perception.Spatial
import win32more.Windows.Win32.System.WinRT
class CameraIntrinsics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.ICameraIntrinsics
    _classid_ = 'Windows.Media.Devices.Core.CameraIntrinsics'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 6:
            super().__init__(move=win32more.Windows.Media.Devices.Core.CameraIntrinsics.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Devices.Core.ICameraIntrinsicsFactory, focalLength: win32more.Windows.Foundation.Numerics.Vector2, principalPoint: win32more.Windows.Foundation.Numerics.Vector2, radialDistortion: win32more.Windows.Foundation.Numerics.Vector3, tangentialDistortion: win32more.Windows.Foundation.Numerics.Vector2, imageWidth: UInt32, imageHeight: UInt32) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def get_FocalLength(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_PrincipalPoint(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_RadialDistortion(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_TangentialDistortion(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_ImageWidth(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics) -> UInt32: ...
    @winrt_mixinmethod
    def get_ImageHeight(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics) -> UInt32: ...
    @winrt_mixinmethod
    def ProjectOntoFrame(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics, coordinate: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def UnprojectAtUnitDepth(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics, pixelCoordinate: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def ProjectManyOntoFrame(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics, coordinates: PassArray[win32more.Windows.Foundation.Numerics.Vector3], results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def UnprojectPixelsAtUnitDepth(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics, pixelCoordinates: PassArray[win32more.Windows.Foundation.Point], results: FillArray[win32more.Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_mixinmethod
    def get_UndistortedProjectionTransform(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics2) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def DistortPoint(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics2, input: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def DistortPoints(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics2, inputs: PassArray[win32more.Windows.Foundation.Point], results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def UndistortPoint(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics2, input: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def UndistortPoints(self: win32more.Windows.Media.Devices.Core.ICameraIntrinsics2, inputs: PassArray[win32more.Windows.Foundation.Point], results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    FocalLength = property(get_FocalLength, None)
    ImageHeight = property(get_ImageHeight, None)
    ImageWidth = property(get_ImageWidth, None)
    PrincipalPoint = property(get_PrincipalPoint, None)
    RadialDistortion = property(get_RadialDistortion, None)
    TangentialDistortion = property(get_TangentialDistortion, None)
    UndistortedProjectionTransform = property(get_UndistortedProjectionTransform, None)
class DepthCorrelatedCoordinateMapper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper
    _classid_ = 'Windows.Media.Devices.Core.DepthCorrelatedCoordinateMapper'
    @winrt_mixinmethod
    def UnprojectPoint(self: win32more.Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoint: win32more.Windows.Foundation.Point, targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def UnprojectPoints(self: win32more.Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoints: PassArray[win32more.Windows.Foundation.Point], targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def MapPoint(self: win32more.Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoint: win32more.Windows.Foundation.Point, targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: win32more.Windows.Media.Devices.Core.CameraIntrinsics) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def MapPoints(self: win32more.Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper, sourcePoints: PassArray[win32more.Windows.Foundation.Point], targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: win32more.Windows.Media.Devices.Core.CameraIntrinsics, results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class FrameControlCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities
    _classid_ = 'Windows.Media.Devices.Core.FrameControlCapabilities'
    @winrt_mixinmethod
    def get_Exposure(self: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities) -> win32more.Windows.Media.Devices.Core.FrameExposureCapabilities: ...
    @winrt_mixinmethod
    def get_ExposureCompensation(self: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities) -> win32more.Windows.Media.Devices.Core.FrameExposureCompensationCapabilities: ...
    @winrt_mixinmethod
    def get_IsoSpeed(self: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities) -> win32more.Windows.Media.Devices.Core.FrameIsoSpeedCapabilities: ...
    @winrt_mixinmethod
    def get_Focus(self: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities) -> win32more.Windows.Media.Devices.Core.FrameFocusCapabilities: ...
    @winrt_mixinmethod
    def get_PhotoConfirmationSupported(self: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Flash(self: win32more.Windows.Media.Devices.Core.IFrameControlCapabilities2) -> win32more.Windows.Media.Devices.Core.FrameFlashCapabilities: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    Flash = property(get_Flash, None)
    Focus = property(get_Focus, None)
    IsoSpeed = property(get_IsoSpeed, None)
    PhotoConfirmationSupported = property(get_PhotoConfirmationSupported, None)
class FrameController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameController
    _classid_ = 'Windows.Media.Devices.Core.FrameController'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Devices.Core.FrameController.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Devices.Core.FrameController: ...
    @winrt_mixinmethod
    def get_ExposureControl(self: win32more.Windows.Media.Devices.Core.IFrameController) -> win32more.Windows.Media.Devices.Core.FrameExposureControl: ...
    @winrt_mixinmethod
    def get_ExposureCompensationControl(self: win32more.Windows.Media.Devices.Core.IFrameController) -> win32more.Windows.Media.Devices.Core.FrameExposureCompensationControl: ...
    @winrt_mixinmethod
    def get_IsoSpeedControl(self: win32more.Windows.Media.Devices.Core.IFrameController) -> win32more.Windows.Media.Devices.Core.FrameIsoSpeedControl: ...
    @winrt_mixinmethod
    def get_FocusControl(self: win32more.Windows.Media.Devices.Core.IFrameController) -> win32more.Windows.Media.Devices.Core.FrameFocusControl: ...
    @winrt_mixinmethod
    def get_PhotoConfirmationEnabled(self: win32more.Windows.Media.Devices.Core.IFrameController) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_PhotoConfirmationEnabled(self: win32more.Windows.Media.Devices.Core.IFrameController, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_FlashControl(self: win32more.Windows.Media.Devices.Core.IFrameController2) -> win32more.Windows.Media.Devices.Core.FrameFlashControl: ...
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    ExposureControl = property(get_ExposureControl, None)
    FlashControl = property(get_FlashControl, None)
    FocusControl = property(get_FocusControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    PhotoConfirmationEnabled = property(get_PhotoConfirmationEnabled, put_PhotoConfirmationEnabled)
class FrameExposureCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameExposureCapabilities
    _classid_ = 'Windows.Media.Devices.Core.FrameExposureCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.Core.IFrameExposureCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.Core.IFrameExposureCapabilities) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.Core.IFrameExposureCapabilities) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.Core.IFrameExposureCapabilities) -> win32more.Windows.Foundation.TimeSpan: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class FrameExposureCompensationCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities
    _classid_ = 'Windows.Media.Devices.Core.FrameExposureCompensationCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Single: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Single: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities) -> Single: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class FrameExposureCompensationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationControl
    _classid_ = 'Windows.Media.Devices.Core.FrameExposureCompensationControl'
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationControl) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.Core.IFrameExposureCompensationControl, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    Value = property(get_Value, put_Value)
class FrameExposureControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameExposureControl
    _classid_ = 'Windows.Media.Devices.Core.FrameExposureControl'
    @winrt_mixinmethod
    def get_Auto(self: win32more.Windows.Media.Devices.Core.IFrameExposureControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: win32more.Windows.Media.Devices.Core.IFrameExposureControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.Core.IFrameExposureControl) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.Core.IFrameExposureControl, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class FrameFlashCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameFlashCapabilities
    _classid_ = 'Windows.Media.Devices.Core.FrameFlashCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.Core.IFrameFlashCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_RedEyeReductionSupported(self: win32more.Windows.Media.Devices.Core.IFrameFlashCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerSupported(self: win32more.Windows.Media.Devices.Core.IFrameFlashCapabilities) -> Boolean: ...
    PowerSupported = property(get_PowerSupported, None)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    Supported = property(get_Supported, None)
class FrameFlashControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameFlashControl
    _classid_ = 'Windows.Media.Devices.Core.FrameFlashControl'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl) -> win32more.Windows.Media.Devices.Core.FrameFlashMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl, value: win32more.Windows.Media.Devices.Core.FrameFlashMode) -> Void: ...
    @winrt_mixinmethod
    def get_Auto(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RedEyeReduction(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_RedEyeReduction(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PowerPercent(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl) -> Single: ...
    @winrt_mixinmethod
    def put_PowerPercent(self: win32more.Windows.Media.Devices.Core.IFrameFlashControl, value: Single) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Mode = property(get_Mode, put_Mode)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
class FrameFlashMode(Enum, Int32):
    Disable = 0
    Enable = 1
    Global = 2
class FrameFocusCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameFocusCapabilities
    _classid_ = 'Windows.Media.Devices.Core.FrameFocusCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.Core.IFrameFocusCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.Core.IFrameFocusCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.Core.IFrameFocusCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.Core.IFrameFocusCapabilities) -> UInt32: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class FrameFocusControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameFocusControl
    _classid_ = 'Windows.Media.Devices.Core.FrameFocusControl'
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.Core.IFrameFocusControl) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.Core.IFrameFocusControl, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    Value = property(get_Value, put_Value)
class FrameIsoSpeedCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities
    _classid_ = 'Windows.Media.Devices.Core.FrameIsoSpeedCapabilities'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_Step(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities) -> UInt32: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class FrameIsoSpeedControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedControl
    _classid_ = 'Windows.Media.Devices.Core.FrameIsoSpeedControl'
    @winrt_mixinmethod
    def get_Auto(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_Auto(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedControl) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Media.Devices.Core.IFrameIsoSpeedControl, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class ICameraIntrinsics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.ICameraIntrinsics'
    _iid_ = Guid('{0aa6ed32-6589-49da-afde-594270ca0aac}')
    @winrt_commethod(6)
    def get_FocalLength(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def get_PrincipalPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(8)
    def get_RadialDistortion(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_TangentialDistortion(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(10)
    def get_ImageWidth(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_ImageHeight(self) -> UInt32: ...
    @winrt_commethod(12)
    def ProjectOntoFrame(self, coordinate: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def UnprojectAtUnitDepth(self, pixelCoordinate: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(14)
    def ProjectManyOntoFrame(self, coordinates: PassArray[win32more.Windows.Foundation.Numerics.Vector3], results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(15)
    def UnprojectPixelsAtUnitDepth(self, pixelCoordinates: PassArray[win32more.Windows.Foundation.Point], results: FillArray[win32more.Windows.Foundation.Numerics.Vector2]) -> Void: ...
    FocalLength = property(get_FocalLength, None)
    ImageHeight = property(get_ImageHeight, None)
    ImageWidth = property(get_ImageWidth, None)
    PrincipalPoint = property(get_PrincipalPoint, None)
    RadialDistortion = property(get_RadialDistortion, None)
    TangentialDistortion = property(get_TangentialDistortion, None)
class ICameraIntrinsics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.ICameraIntrinsics2'
    _iid_ = Guid('{0cdaa447-0798-4b4d-839f-c5ec414db27a}')
    @winrt_commethod(6)
    def get_UndistortedProjectionTransform(self) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(7)
    def DistortPoint(self, input: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def DistortPoints(self, inputs: PassArray[win32more.Windows.Foundation.Point], results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(9)
    def UndistortPoint(self, input: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def UndistortPoints(self, inputs: PassArray[win32more.Windows.Foundation.Point], results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    UndistortedProjectionTransform = property(get_UndistortedProjectionTransform, None)
class ICameraIntrinsicsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.ICameraIntrinsicsFactory'
    _iid_ = Guid('{c0ddc486-2132-4a34-a659-9bfe2a055712}')
    @winrt_commethod(6)
    def Create(self, focalLength: win32more.Windows.Foundation.Numerics.Vector2, principalPoint: win32more.Windows.Foundation.Numerics.Vector2, radialDistortion: win32more.Windows.Foundation.Numerics.Vector3, tangentialDistortion: win32more.Windows.Foundation.Numerics.Vector2, imageWidth: UInt32, imageHeight: UInt32) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
class IDepthCorrelatedCoordinateMapper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Devices.Core.IDepthCorrelatedCoordinateMapper'
    _iid_ = Guid('{f95d89fb-8af0-4cb0-926d-696866e5046a}')
    @winrt_commethod(6)
    def UnprojectPoint(self, sourcePoint: win32more.Windows.Foundation.Point, targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def UnprojectPoints(self, sourcePoints: PassArray[win32more.Windows.Foundation.Point], targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(8)
    def MapPoint(self, sourcePoint: win32more.Windows.Foundation.Point, targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: win32more.Windows.Media.Devices.Core.CameraIntrinsics) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def MapPoints(self, sourcePoints: PassArray[win32more.Windows.Foundation.Point], targetCoordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, targetCameraIntrinsics: win32more.Windows.Media.Devices.Core.CameraIntrinsics, results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
class IFrameControlCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameControlCapabilities'
    _iid_ = Guid('{a8ffae60-4e9e-4377-a789-e24c4ae7e544}')
    @winrt_commethod(6)
    def get_Exposure(self) -> win32more.Windows.Media.Devices.Core.FrameExposureCapabilities: ...
    @winrt_commethod(7)
    def get_ExposureCompensation(self) -> win32more.Windows.Media.Devices.Core.FrameExposureCompensationCapabilities: ...
    @winrt_commethod(8)
    def get_IsoSpeed(self) -> win32more.Windows.Media.Devices.Core.FrameIsoSpeedCapabilities: ...
    @winrt_commethod(9)
    def get_Focus(self) -> win32more.Windows.Media.Devices.Core.FrameFocusCapabilities: ...
    @winrt_commethod(10)
    def get_PhotoConfirmationSupported(self) -> Boolean: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    Focus = property(get_Focus, None)
    IsoSpeed = property(get_IsoSpeed, None)
    PhotoConfirmationSupported = property(get_PhotoConfirmationSupported, None)
class IFrameControlCapabilities2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameControlCapabilities2'
    _iid_ = Guid('{ce9b0464-4730-440f-bd3e-efe8a8f230a8}')
    @winrt_commethod(6)
    def get_Flash(self) -> win32more.Windows.Media.Devices.Core.FrameFlashCapabilities: ...
    Flash = property(get_Flash, None)
class IFrameController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameController'
    _iid_ = Guid('{c16459d9-baef-4052-9177-48aff2af7522}')
    @winrt_commethod(6)
    def get_ExposureControl(self) -> win32more.Windows.Media.Devices.Core.FrameExposureControl: ...
    @winrt_commethod(7)
    def get_ExposureCompensationControl(self) -> win32more.Windows.Media.Devices.Core.FrameExposureCompensationControl: ...
    @winrt_commethod(8)
    def get_IsoSpeedControl(self) -> win32more.Windows.Media.Devices.Core.FrameIsoSpeedControl: ...
    @winrt_commethod(9)
    def get_FocusControl(self) -> win32more.Windows.Media.Devices.Core.FrameFocusControl: ...
    @winrt_commethod(10)
    def get_PhotoConfirmationEnabled(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(11)
    def put_PhotoConfirmationEnabled(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    ExposureCompensationControl = property(get_ExposureCompensationControl, None)
    ExposureControl = property(get_ExposureControl, None)
    FocusControl = property(get_FocusControl, None)
    IsoSpeedControl = property(get_IsoSpeedControl, None)
    PhotoConfirmationEnabled = property(get_PhotoConfirmationEnabled, put_PhotoConfirmationEnabled)
class IFrameController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameController2'
    _iid_ = Guid('{00d3bc75-d87c-485b-8a09-5c358568b427}')
    @winrt_commethod(6)
    def get_FlashControl(self) -> win32more.Windows.Media.Devices.Core.FrameFlashControl: ...
    FlashControl = property(get_FlashControl, None)
class IFrameExposureCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameExposureCapabilities'
    _iid_ = Guid('{bdbe9ce3-3985-4e72-97c2-0590d61307a1}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_Max(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Step(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class IFrameExposureCompensationCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameExposureCompensationCapabilities'
    _iid_ = Guid('{b988a823-8065-41ee-b04f-722265954500}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> Single: ...
    @winrt_commethod(8)
    def get_Max(self) -> Single: ...
    @winrt_commethod(9)
    def get_Step(self) -> Single: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class IFrameExposureCompensationControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameExposureCompensationControl'
    _iid_ = Guid('{e95896c9-f7f9-48ca-8591-a26531cb1578}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    Value = property(get_Value, put_Value)
class IFrameExposureControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameExposureControl'
    _iid_ = Guid('{b1605a61-ffaf-4752-b621-f5b6f117f432}')
    @winrt_commethod(6)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Auto(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class IFrameFlashCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameFlashCapabilities'
    _iid_ = Guid('{bb9341a2-5ebe-4f62-8223-0e2b05bfbbd0}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_RedEyeReductionSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_PowerSupported(self) -> Boolean: ...
    PowerSupported = property(get_PowerSupported, None)
    RedEyeReductionSupported = property(get_RedEyeReductionSupported, None)
    Supported = property(get_Supported, None)
class IFrameFlashControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameFlashControl'
    _iid_ = Guid('{75d5f6c7-bd45-4fab-9375-45ac04b332c2}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.Media.Devices.Core.FrameFlashMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.Media.Devices.Core.FrameFlashMode) -> Void: ...
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
    Auto = property(get_Auto, put_Auto)
    Mode = property(get_Mode, put_Mode)
    PowerPercent = property(get_PowerPercent, put_PowerPercent)
    RedEyeReduction = property(get_RedEyeReduction, put_RedEyeReduction)
class IFrameFocusCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameFocusCapabilities'
    _iid_ = Guid('{7b25cd58-01c0-4065-9c40-c1a721425c1a}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Step(self) -> UInt32: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class IFrameFocusControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameFocusControl'
    _iid_ = Guid('{272df1d0-d912-4214-a67b-e38a8d48d8c6}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_Value(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    Value = property(get_Value, put_Value)
class IFrameIsoSpeedCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameIsoSpeedCapabilities'
    _iid_ = Guid('{16bdff61-6df6-4ac9-b92a-9f6ecd1ad2fa}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Min(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Max(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Step(self) -> UInt32: ...
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Step = property(get_Step, None)
    Supported = property(get_Supported, None)
class IFrameIsoSpeedControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IFrameIsoSpeedControl'
    _iid_ = Guid('{1a03efed-786a-4c75-a557-7ab9a85f588c}')
    @winrt_commethod(6)
    def get_Auto(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Auto(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    Auto = property(get_Auto, put_Auto)
    Value = property(get_Value, put_Value)
class IVariablePhotoSequenceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Devices.Core.IVariablePhotoSequenceController'
    _iid_ = Guid('{7fbff880-ed8c-43fd-a7c3-b35809e4229a}')
    @winrt_commethod(6)
    def get_Supported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxPhotosPerSecond(self) -> Single: ...
    @winrt_commethod(8)
    def get_PhotosPerSecondLimit(self) -> Single: ...
    @winrt_commethod(9)
    def put_PhotosPerSecondLimit(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def GetHighestConcurrentFrameRate(self, captureProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(11)
    def GetCurrentFrameRate(self) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(12)
    def get_FrameCapabilities(self) -> win32more.Windows.Media.Devices.Core.FrameControlCapabilities: ...
    @winrt_commethod(13)
    def get_DesiredFrameControllers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Devices.Core.FrameController]: ...
    DesiredFrameControllers = property(get_DesiredFrameControllers, None)
    FrameCapabilities = property(get_FrameCapabilities, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    Supported = property(get_Supported, None)
class VariablePhotoSequenceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController
    _classid_ = 'Windows.Media.Devices.Core.VariablePhotoSequenceController'
    @winrt_mixinmethod
    def get_Supported(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPhotosPerSecond(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Single: ...
    @winrt_mixinmethod
    def get_PhotosPerSecondLimit(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> Single: ...
    @winrt_mixinmethod
    def put_PhotosPerSecondLimit(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def GetHighestConcurrentFrameRate(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController, captureProperties: win32more.Windows.Media.MediaProperties.IMediaEncodingProperties) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def GetCurrentFrameRate(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_FrameCapabilities(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> win32more.Windows.Media.Devices.Core.FrameControlCapabilities: ...
    @winrt_mixinmethod
    def get_DesiredFrameControllers(self: win32more.Windows.Media.Devices.Core.IVariablePhotoSequenceController) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Devices.Core.FrameController]: ...
    DesiredFrameControllers = property(get_DesiredFrameControllers, None)
    FrameCapabilities = property(get_FrameCapabilities, None)
    MaxPhotosPerSecond = property(get_MaxPhotosPerSecond, None)
    PhotosPerSecondLimit = property(get_PhotosPerSecondLimit, put_PhotosPerSecondLimit)
    Supported = property(get_Supported, None)


make_ready(__name__)
