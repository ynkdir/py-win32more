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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception
import win32more.Windows.Perception.People
import win32more.Windows.Perception.Spatial
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Spatial
class EyesPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.People.IEyesPose
    _classid_ = 'Windows.Perception.People.EyesPose'
    @winrt_mixinmethod
    def get_IsCalibrationValid(self: win32more.Windows.Perception.People.IEyesPose) -> Boolean: ...
    @winrt_mixinmethod
    def get_Gaze(self: win32more.Windows.Perception.People.IEyesPose) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialRay]: ...
    @winrt_mixinmethod
    def get_UpdateTimestamp(self: win32more.Windows.Perception.People.IEyesPose) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Perception.People.IEyesPoseStatics) -> Boolean: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Perception.People.IEyesPoseStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Input.GazeInputAccessStatus]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.People.IHandMeshObserver
    _classid_ = 'Windows.Perception.People.HandMeshObserver'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Perception.People.IHandMeshObserver) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_mixinmethod
    def get_TriangleIndexCount(self: win32more.Windows.Perception.People.IHandMeshObserver) -> UInt32: ...
    @winrt_mixinmethod
    def get_VertexCount(self: win32more.Windows.Perception.People.IHandMeshObserver) -> UInt32: ...
    @winrt_mixinmethod
    def GetTriangleIndices(self: win32more.Windows.Perception.People.IHandMeshObserver, indices: Annotated[SZArray[UInt16], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def GetVertexStateForPose(self: win32more.Windows.Perception.People.IHandMeshObserver, handPose: win32more.Windows.Perception.People.HandPose) -> win32more.Windows.Perception.People.HandMeshVertexState: ...
    @winrt_mixinmethod
    def get_NeutralPose(self: win32more.Windows.Perception.People.IHandMeshObserver) -> win32more.Windows.Perception.People.HandPose: ...
    @winrt_mixinmethod
    def get_NeutralPoseVersion(self: win32more.Windows.Perception.People.IHandMeshObserver) -> Int32: ...
    @winrt_mixinmethod
    def get_ModelId(self: win32more.Windows.Perception.People.IHandMeshObserver) -> Int32: ...
    Source = property(get_Source, None)
    TriangleIndexCount = property(get_TriangleIndexCount, None)
    VertexCount = property(get_VertexCount, None)
    NeutralPose = property(get_NeutralPose, None)
    NeutralPoseVersion = property(get_NeutralPoseVersion, None)
    ModelId = property(get_ModelId, None)
class HandMeshVertex(EasyCastStructure):
    Position: win32more.Windows.Foundation.Numerics.Vector3
    Normal: win32more.Windows.Foundation.Numerics.Vector3
class HandMeshVertexState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.People.IHandMeshVertexState
    _classid_ = 'Windows.Perception.People.HandMeshVertexState'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.People.IHandMeshVertexState) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def GetVertices(self: win32more.Windows.Perception.People.IHandMeshVertexState, vertices: Annotated[SZArray[win32more.Windows.Perception.People.HandMeshVertex], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateTimestamp(self: win32more.Windows.Perception.People.IHandMeshVertexState) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class HandPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.People.IHandPose
    _classid_ = 'Windows.Perception.People.HandPose'
    @winrt_mixinmethod
    def TryGetJoint(self: win32more.Windows.Perception.People.IHandPose, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, joint: win32more.Windows.Perception.People.HandJointKind, jointPose: POINTER(win32more.Windows.Perception.People.JointPose)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetJoints(self: win32more.Windows.Perception.People.IHandPose, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, joints: Annotated[SZArray[win32more.Windows.Perception.People.HandJointKind], 'In'], jointPoses: Annotated[SZArray[win32more.Windows.Perception.People.JointPose], 'Out']) -> Boolean: ...
    @winrt_mixinmethod
    def GetRelativeJoint(self: win32more.Windows.Perception.People.IHandPose, joint: win32more.Windows.Perception.People.HandJointKind, referenceJoint: win32more.Windows.Perception.People.HandJointKind) -> win32more.Windows.Perception.People.JointPose: ...
    @winrt_mixinmethod
    def GetRelativeJoints(self: win32more.Windows.Perception.People.IHandPose, joints: Annotated[SZArray[win32more.Windows.Perception.People.HandJointKind], 'In'], referenceJoints: Annotated[SZArray[win32more.Windows.Perception.People.HandJointKind], 'In'], jointPoses: Annotated[SZArray[win32more.Windows.Perception.People.JointPose], 'Out']) -> Void: ...
class HeadPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.People.IHeadPose
    _classid_ = 'Windows.Perception.People.HeadPose'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Perception.People.IHeadPose) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ForwardDirection(self: win32more.Windows.Perception.People.IHeadPose) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_UpDirection(self: win32more.Windows.Perception.People.IHeadPose) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    ForwardDirection = property(get_ForwardDirection, None)
    UpDirection = property(get_UpDirection, None)
class IEyesPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IEyesPose'
    _iid_ = Guid('{682a9b23-8a1e-5b86-a060-906ffacb62a4}')
    @winrt_commethod(6)
    def get_IsCalibrationValid(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Gaze(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialRay]: ...
    @winrt_commethod(8)
    def get_UpdateTimestamp(self) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    IsCalibrationValid = property(get_IsCalibrationValid, None)
    Gaze = property(get_Gaze, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class IEyesPoseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IEyesPoseStatics'
    _iid_ = Guid('{1cff7413-b21f-54c0-80c1-e60d994ca58c}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Input.GazeInputAccessStatus]: ...
class IHandMeshObserver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandMeshObserver'
    _iid_ = Guid('{85ae30cb-6fc3-55c4-a7b4-29e33896ca69}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_commethod(7)
    def get_TriangleIndexCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_VertexCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def GetTriangleIndices(self, indices: Annotated[SZArray[UInt16], 'Out']) -> Void: ...
    @winrt_commethod(10)
    def GetVertexStateForPose(self, handPose: win32more.Windows.Perception.People.HandPose) -> win32more.Windows.Perception.People.HandMeshVertexState: ...
    @winrt_commethod(11)
    def get_NeutralPose(self) -> win32more.Windows.Perception.People.HandPose: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandMeshVertexState'
    _iid_ = Guid('{046c5fef-1d8b-55de-ab2c-1cd424886d8f}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def GetVertices(self, vertices: Annotated[SZArray[win32more.Windows.Perception.People.HandMeshVertex], 'Out']) -> Void: ...
    @winrt_commethod(8)
    def get_UpdateTimestamp(self) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class IHandPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandPose'
    _iid_ = Guid('{4d98e79a-bb08-5d09-91de-df0dd3fae46c}')
    @winrt_commethod(6)
    def TryGetJoint(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, joint: win32more.Windows.Perception.People.HandJointKind, jointPose: POINTER(win32more.Windows.Perception.People.JointPose)) -> Boolean: ...
    @winrt_commethod(7)
    def TryGetJoints(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, joints: Annotated[SZArray[win32more.Windows.Perception.People.HandJointKind], 'In'], jointPoses: Annotated[SZArray[win32more.Windows.Perception.People.JointPose], 'Out']) -> Boolean: ...
    @winrt_commethod(8)
    def GetRelativeJoint(self, joint: win32more.Windows.Perception.People.HandJointKind, referenceJoint: win32more.Windows.Perception.People.HandJointKind) -> win32more.Windows.Perception.People.JointPose: ...
    @winrt_commethod(9)
    def GetRelativeJoints(self, joints: Annotated[SZArray[win32more.Windows.Perception.People.HandJointKind], 'In'], referenceJoints: Annotated[SZArray[win32more.Windows.Perception.People.HandJointKind], 'In'], jointPoses: Annotated[SZArray[win32more.Windows.Perception.People.JointPose], 'Out']) -> Void: ...
class IHeadPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHeadPose'
    _iid_ = Guid('{7f5ac5a5-49db-379f-9429-32a2faf34fa6}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_ForwardDirection(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_UpDirection(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    ForwardDirection = property(get_ForwardDirection, None)
    UpDirection = property(get_UpDirection, None)
class JointPose(EasyCastStructure):
    Orientation: win32more.Windows.Foundation.Numerics.Quaternion
    Position: win32more.Windows.Foundation.Numerics.Vector3
    Radius: Single
    Accuracy: win32more.Windows.Perception.People.JointPoseAccuracy
JointPoseAccuracy = Int32
JointPoseAccuracy_High: JointPoseAccuracy = 0
JointPoseAccuracy_Approximate: JointPoseAccuracy = 1
make_ready(__name__)
