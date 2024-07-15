from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception
import win32more.Windows.Perception.People
import win32more.Windows.Perception.Spatial
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Spatial
import win32more.Windows.Win32.System.WinRT
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
    Gaze = property(get_Gaze, None)
    IsCalibrationValid = property(get_IsCalibrationValid, None)
    UpdateTimestamp = property(get_UpdateTimestamp, None)
class HandJointKind(Enum, Int32):
    Palm = 0
    Wrist = 1
    ThumbMetacarpal = 2
    ThumbProximal = 3
    ThumbDistal = 4
    ThumbTip = 5
    IndexMetacarpal = 6
    IndexProximal = 7
    IndexIntermediate = 8
    IndexDistal = 9
    IndexTip = 10
    MiddleMetacarpal = 11
    MiddleProximal = 12
    MiddleIntermediate = 13
    MiddleDistal = 14
    MiddleTip = 15
    RingMetacarpal = 16
    RingProximal = 17
    RingIntermediate = 18
    RingDistal = 19
    RingTip = 20
    LittleMetacarpal = 21
    LittleProximal = 22
    LittleIntermediate = 23
    LittleDistal = 24
    LittleTip = 25
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
    def GetTriangleIndices(self: win32more.Windows.Perception.People.IHandMeshObserver, indices: FillArray[UInt16]) -> Void: ...
    @winrt_mixinmethod
    def GetVertexStateForPose(self: win32more.Windows.Perception.People.IHandMeshObserver, handPose: win32more.Windows.Perception.People.HandPose) -> win32more.Windows.Perception.People.HandMeshVertexState: ...
    @winrt_mixinmethod
    def get_NeutralPose(self: win32more.Windows.Perception.People.IHandMeshObserver) -> win32more.Windows.Perception.People.HandPose: ...
    @winrt_mixinmethod
    def get_NeutralPoseVersion(self: win32more.Windows.Perception.People.IHandMeshObserver) -> Int32: ...
    @winrt_mixinmethod
    def get_ModelId(self: win32more.Windows.Perception.People.IHandMeshObserver) -> Int32: ...
    ModelId = property(get_ModelId, None)
    NeutralPose = property(get_NeutralPose, None)
    NeutralPoseVersion = property(get_NeutralPoseVersion, None)
    Source = property(get_Source, None)
    TriangleIndexCount = property(get_TriangleIndexCount, None)
    VertexCount = property(get_VertexCount, None)
class HandMeshVertex(Structure):
    Position: win32more.Windows.Foundation.Numerics.Vector3
    Normal: win32more.Windows.Foundation.Numerics.Vector3
class HandMeshVertexState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.People.IHandMeshVertexState
    _classid_ = 'Windows.Perception.People.HandMeshVertexState'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.People.IHandMeshVertexState) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def GetVertices(self: win32more.Windows.Perception.People.IHandMeshVertexState, vertices: FillArray[win32more.Windows.Perception.People.HandMeshVertex]) -> Void: ...
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
    def TryGetJoints(self: win32more.Windows.Perception.People.IHandPose, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, joints: PassArray[win32more.Windows.Perception.People.HandJointKind], jointPoses: FillArray[win32more.Windows.Perception.People.JointPose]) -> Boolean: ...
    @winrt_mixinmethod
    def GetRelativeJoint(self: win32more.Windows.Perception.People.IHandPose, joint: win32more.Windows.Perception.People.HandJointKind, referenceJoint: win32more.Windows.Perception.People.HandJointKind) -> win32more.Windows.Perception.People.JointPose: ...
    @winrt_mixinmethod
    def GetRelativeJoints(self: win32more.Windows.Perception.People.IHandPose, joints: PassArray[win32more.Windows.Perception.People.HandJointKind], referenceJoints: PassArray[win32more.Windows.Perception.People.HandJointKind], jointPoses: FillArray[win32more.Windows.Perception.People.JointPose]) -> Void: ...
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
    ForwardDirection = property(get_ForwardDirection, None)
    Position = property(get_Position, None)
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
    Gaze = property(get_Gaze, None)
    IsCalibrationValid = property(get_IsCalibrationValid, None)
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
    def GetTriangleIndices(self, indices: FillArray[UInt16]) -> Void: ...
    @winrt_commethod(10)
    def GetVertexStateForPose(self, handPose: win32more.Windows.Perception.People.HandPose) -> win32more.Windows.Perception.People.HandMeshVertexState: ...
    @winrt_commethod(11)
    def get_NeutralPose(self) -> win32more.Windows.Perception.People.HandPose: ...
    @winrt_commethod(12)
    def get_NeutralPoseVersion(self) -> Int32: ...
    @winrt_commethod(13)
    def get_ModelId(self) -> Int32: ...
    ModelId = property(get_ModelId, None)
    NeutralPose = property(get_NeutralPose, None)
    NeutralPoseVersion = property(get_NeutralPoseVersion, None)
    Source = property(get_Source, None)
    TriangleIndexCount = property(get_TriangleIndexCount, None)
    VertexCount = property(get_VertexCount, None)
class IHandMeshVertexState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.People.IHandMeshVertexState'
    _iid_ = Guid('{046c5fef-1d8b-55de-ab2c-1cd424886d8f}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def GetVertices(self, vertices: FillArray[win32more.Windows.Perception.People.HandMeshVertex]) -> Void: ...
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
    def TryGetJoints(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, joints: PassArray[win32more.Windows.Perception.People.HandJointKind], jointPoses: FillArray[win32more.Windows.Perception.People.JointPose]) -> Boolean: ...
    @winrt_commethod(8)
    def GetRelativeJoint(self, joint: win32more.Windows.Perception.People.HandJointKind, referenceJoint: win32more.Windows.Perception.People.HandJointKind) -> win32more.Windows.Perception.People.JointPose: ...
    @winrt_commethod(9)
    def GetRelativeJoints(self, joints: PassArray[win32more.Windows.Perception.People.HandJointKind], referenceJoints: PassArray[win32more.Windows.Perception.People.HandJointKind], jointPoses: FillArray[win32more.Windows.Perception.People.JointPose]) -> Void: ...
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
    ForwardDirection = property(get_ForwardDirection, None)
    Position = property(get_Position, None)
    UpDirection = property(get_UpDirection, None)
class JointPose(Structure):
    Orientation: win32more.Windows.Foundation.Numerics.Quaternion
    Position: win32more.Windows.Foundation.Numerics.Vector3
    Radius: Single
    Accuracy: win32more.Windows.Perception.People.JointPoseAccuracy
class JointPoseAccuracy(Enum, Int32):
    High = 0
    Approximate = 1


make_ready(__name__)
