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
import Windows.Foundation.Numerics
import Windows.Perception
import Windows.Perception.People
import Windows.Perception.Spatial
import Windows.UI.Input
import Windows.UI.Input.Spatial
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class EyesPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.People.IEyesPose
    _classid_ = 'Windows.Perception.People.EyesPose'
    @winrt_mixinmethod
    def get_IsCalibrationValid(self: Windows.Perception.People.IEyesPose) -> Boolean: ...
    @winrt_mixinmethod
    def get_Gaze(self: Windows.Perception.People.IEyesPose) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialRay]: ...
    @winrt_mixinmethod
    def get_UpdateTimestamp(self: Windows.Perception.People.IEyesPose) -> Windows.Perception.PerceptionTimestamp: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Perception.People.IEyesPoseStatics) -> Boolean: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Perception.People.IEyesPoseStatics) -> Windows.Foundation.IAsyncOperation[Windows.UI.Input.GazeInputAccessStatus]: ...
    IsCalibrationValid = property(get_IsCalibrationValid, None)
    Gaze = property(get_Gaze, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
HandJointKind = Int32
HandJointKind_Palm: HandJointKind = 0
HandJointKind_Wrist: HandJointKind = 1
HandJointKind_ThumbMetacarpal: HandJointKind = 2
HandJointKind_ThumbProximal: HandJointKind = 3
HandJointKind_ThumbDistal: HandJointKind = 4
HandJointKind_ThumbTip: HandJointKind = 5
HandJointKind_IndexMetacarpal: HandJointKind = 6
HandJointKind_IndexProximal: HandJointKind = 7
HandJointKind_IndexIntermediate: HandJointKind = 8
HandJointKind_IndexDistal: HandJointKind = 9
HandJointKind_IndexTip: HandJointKind = 10
HandJointKind_MiddleMetacarpal: HandJointKind = 11
HandJointKind_MiddleProximal: HandJointKind = 12
HandJointKind_MiddleIntermediate: HandJointKind = 13
HandJointKind_MiddleDistal: HandJointKind = 14
HandJointKind_MiddleTip: HandJointKind = 15
HandJointKind_RingMetacarpal: HandJointKind = 16
HandJointKind_RingProximal: HandJointKind = 17
HandJointKind_RingIntermediate: HandJointKind = 18
HandJointKind_RingDistal: HandJointKind = 19
HandJointKind_RingTip: HandJointKind = 20
HandJointKind_LittleMetacarpal: HandJointKind = 21
HandJointKind_LittleProximal: HandJointKind = 22
HandJointKind_LittleIntermediate: HandJointKind = 23
HandJointKind_LittleDistal: HandJointKind = 24
HandJointKind_LittleTip: HandJointKind = 25
class HandMeshObserver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.People.IHandMeshObserver
    _classid_ = 'Windows.Perception.People.HandMeshObserver'
    @winrt_mixinmethod
    def get_Source(self: Windows.Perception.People.IHandMeshObserver) -> Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_mixinmethod
    def get_TriangleIndexCount(self: Windows.Perception.People.IHandMeshObserver) -> UInt32: ...
    @winrt_mixinmethod
    def get_VertexCount(self: Windows.Perception.People.IHandMeshObserver) -> UInt32: ...
    @winrt_mixinmethod
    def GetTriangleIndices(self: Windows.Perception.People.IHandMeshObserver, indices: POINTER(UInt16)) -> Void: ...
    @winrt_mixinmethod
    def GetVertexStateForPose(self: Windows.Perception.People.IHandMeshObserver, handPose: Windows.Perception.People.HandPose) -> Windows.Perception.People.HandMeshVertexState: ...
    @winrt_mixinmethod
    def get_NeutralPose(self: Windows.Perception.People.IHandMeshObserver) -> Windows.Perception.People.HandPose: ...
    @winrt_mixinmethod
    def get_NeutralPoseVersion(self: Windows.Perception.People.IHandMeshObserver) -> Int32: ...
    @winrt_mixinmethod
    def get_ModelId(self: Windows.Perception.People.IHandMeshObserver) -> Int32: ...
    Source = property(get_Source, None)
    TriangleIndexCount = property(get_TriangleIndexCount, None)
    VertexCount = property(get_VertexCount, None)
    NeutralPose = property(get_NeutralPose, None)
    NeutralPoseVersion = property(get_NeutralPoseVersion, None)
    ModelId = property(get_ModelId, None)
class HandMeshVertex(EasyCastStructure):
    Position: Windows.Foundation.Numerics.Vector3
    Normal: Windows.Foundation.Numerics.Vector3
class HandMeshVertexState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.People.IHandMeshVertexState
    _classid_ = 'Windows.Perception.People.HandMeshVertexState'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Perception.People.IHandMeshVertexState) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def GetVertices(self: Windows.Perception.People.IHandMeshVertexState, vertices: POINTER(Windows.Perception.People.HandMeshVertex_head)) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateTimestamp(self: Windows.Perception.People.IHandMeshVertexState) -> Windows.Perception.PerceptionTimestamp: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class HandPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.People.IHandPose
    _classid_ = 'Windows.Perception.People.HandPose'
    @winrt_mixinmethod
    def TryGetJoint(self: Windows.Perception.People.IHandPose, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, joint: Windows.Perception.People.HandJointKind, jointPose: POINTER(Windows.Perception.People.JointPose_head)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetJoints(self: Windows.Perception.People.IHandPose, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, joints: POINTER(Windows.Perception.People.HandJointKind), jointPoses: POINTER(Windows.Perception.People.JointPose_head)) -> Boolean: ...
    @winrt_mixinmethod
    def GetRelativeJoint(self: Windows.Perception.People.IHandPose, joint: Windows.Perception.People.HandJointKind, referenceJoint: Windows.Perception.People.HandJointKind) -> Windows.Perception.People.JointPose: ...
    @winrt_mixinmethod
    def GetRelativeJoints(self: Windows.Perception.People.IHandPose, joints: POINTER(Windows.Perception.People.HandJointKind), referenceJoints: POINTER(Windows.Perception.People.HandJointKind), jointPoses: POINTER(Windows.Perception.People.JointPose_head)) -> Void: ...
class HeadPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.People.IHeadPose
    _classid_ = 'Windows.Perception.People.HeadPose'
    @winrt_mixinmethod
    def get_Position(self: Windows.Perception.People.IHeadPose) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ForwardDirection(self: Windows.Perception.People.IHeadPose) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_UpDirection(self: Windows.Perception.People.IHeadPose) -> Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    ForwardDirection = property(get_ForwardDirection, None)
    UpDirection = property(get_UpDirection, None)
class IEyesPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IEyesPose'
    _iid_ = Guid('{682a9b23-8a1e-5b86-a060-906ffacb62a4}')
    @winrt_commethod(6)
    def get_IsCalibrationValid(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Gaze(self) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialRay]: ...
    @winrt_commethod(8)
    def get_UpdateTimestamp(self) -> Windows.Perception.PerceptionTimestamp: ...
    IsCalibrationValid = property(get_IsCalibrationValid, None)
    Gaze = property(get_Gaze, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class IEyesPoseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IEyesPoseStatics'
    _iid_ = Guid('{1cff7413-b21f-54c0-80c1-e60d994ca58c}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.Input.GazeInputAccessStatus]: ...
class IHandMeshObserver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandMeshObserver'
    _iid_ = Guid('{85ae30cb-6fc3-55c4-a7b4-29e33896ca69}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_commethod(7)
    def get_TriangleIndexCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_VertexCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def GetTriangleIndices(self, indices: POINTER(UInt16)) -> Void: ...
    @winrt_commethod(10)
    def GetVertexStateForPose(self, handPose: Windows.Perception.People.HandPose) -> Windows.Perception.People.HandMeshVertexState: ...
    @winrt_commethod(11)
    def get_NeutralPose(self) -> Windows.Perception.People.HandPose: ...
    @winrt_commethod(12)
    def get_NeutralPoseVersion(self) -> Int32: ...
    @winrt_commethod(13)
    def get_ModelId(self) -> Int32: ...
    Source = property(get_Source, None)
    TriangleIndexCount = property(get_TriangleIndexCount, None)
    VertexCount = property(get_VertexCount, None)
    NeutralPose = property(get_NeutralPose, None)
    NeutralPoseVersion = property(get_NeutralPoseVersion, None)
    ModelId = property(get_ModelId, None)
class IHandMeshVertexState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandMeshVertexState'
    _iid_ = Guid('{046c5fef-1d8b-55de-ab2c-1cd424886d8f}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def GetVertices(self, vertices: POINTER(Windows.Perception.People.HandMeshVertex_head)) -> Void: ...
    @winrt_commethod(8)
    def get_UpdateTimestamp(self) -> Windows.Perception.PerceptionTimestamp: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class IHandPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandPose'
    _iid_ = Guid('{4d98e79a-bb08-5d09-91de-df0dd3fae46c}')
    @winrt_commethod(6)
    def TryGetJoint(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, joint: Windows.Perception.People.HandJointKind, jointPose: POINTER(Windows.Perception.People.JointPose_head)) -> Boolean: ...
    @winrt_commethod(7)
    def TryGetJoints(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, joints: POINTER(Windows.Perception.People.HandJointKind), jointPoses: POINTER(Windows.Perception.People.JointPose_head)) -> Boolean: ...
    @winrt_commethod(8)
    def GetRelativeJoint(self, joint: Windows.Perception.People.HandJointKind, referenceJoint: Windows.Perception.People.HandJointKind) -> Windows.Perception.People.JointPose: ...
    @winrt_commethod(9)
    def GetRelativeJoints(self, joints: POINTER(Windows.Perception.People.HandJointKind), referenceJoints: POINTER(Windows.Perception.People.HandJointKind), jointPoses: POINTER(Windows.Perception.People.JointPose_head)) -> Void: ...
class IHeadPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHeadPose'
    _iid_ = Guid('{7f5ac5a5-49db-379f-9429-32a2faf34fa6}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_ForwardDirection(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_UpDirection(self) -> Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    ForwardDirection = property(get_ForwardDirection, None)
    UpDirection = property(get_UpDirection, None)
class JointPose(EasyCastStructure):
    Orientation: Windows.Foundation.Numerics.Quaternion
    Position: Windows.Foundation.Numerics.Vector3
    Radius: Single
    Accuracy: Windows.Perception.People.JointPoseAccuracy
JointPoseAccuracy = Int32
JointPoseAccuracy_High: JointPoseAccuracy = 0
JointPoseAccuracy_Approximate: JointPoseAccuracy = 1
make_head(_module, 'EyesPose')
make_head(_module, 'HandMeshObserver')
make_head(_module, 'HandMeshVertex')
make_head(_module, 'HandMeshVertexState')
make_head(_module, 'HandPose')
make_head(_module, 'HeadPose')
make_head(_module, 'IEyesPose')
make_head(_module, 'IEyesPoseStatics')
make_head(_module, 'IHandMeshObserver')
make_head(_module, 'IHandMeshVertexState')
make_head(_module, 'IHandPose')
make_head(_module, 'IHeadPose')
make_head(_module, 'JointPose')
