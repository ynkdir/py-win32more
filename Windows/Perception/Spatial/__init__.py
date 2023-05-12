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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Perception
import Windows.Perception.Spatial
import Windows.Storage.Streams
import Windows.System.RemoteSystems
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISpatialAnchor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchor'
    _iid_ = Guid('{0529e5ce-1d34-3702-bcec-eabff578a869}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def get_RawCoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(8)
    def add_RawCoordinateSystemAdjusted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialAnchor, Windows.Perception.Spatial.SpatialAnchorRawCoordinateSystemAdjustedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RawCoordinateSystemAdjusted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    RawCoordinateSystem = property(get_RawCoordinateSystem, None)
class ISpatialAnchor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchor2'
    _iid_ = Guid('{ed17c908-a695-4cf6-92fd-97263ba71047}')
    @winrt_commethod(6)
    def get_RemovedByUser(self) -> Boolean: ...
    RemovedByUser = property(get_RemovedByUser, None)
class ISpatialAnchorExportSufficiency(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorExportSufficiency'
    _iid_ = Guid('{77c25b2b-3409-4088-b91b-fdfd05d1648f}')
    @winrt_commethod(6)
    def get_IsMinimallySufficient(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SufficiencyLevel(self) -> Double: ...
    @winrt_commethod(8)
    def get_RecommendedSufficiencyLevel(self) -> Double: ...
    IsMinimallySufficient = property(get_IsMinimallySufficient, None)
    SufficiencyLevel = property(get_SufficiencyLevel, None)
    RecommendedSufficiencyLevel = property(get_RecommendedSufficiencyLevel, None)
class ISpatialAnchorExporter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorExporter'
    _iid_ = Guid('{9a2a4338-24fb-4269-89c5-88304aeef20f}')
    @winrt_commethod(6)
    def GetAnchorExportSufficiencyAsync(self, anchor: Windows.Perception.Spatial.SpatialAnchor, purpose: Windows.Perception.Spatial.SpatialAnchorExportPurpose) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialAnchorExportSufficiency]: ...
    @winrt_commethod(7)
    def TryExportAnchorAsync(self, anchor: Windows.Perception.Spatial.SpatialAnchor, purpose: Windows.Perception.Spatial.SpatialAnchorExportPurpose, stream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISpatialAnchorExporterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorExporterStatics'
    _iid_ = Guid('{ed2507b8-2475-439c-85ff-7fed341fdc88}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Perception.Spatial.SpatialAnchorExporter: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class ISpatialAnchorManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorManagerStatics'
    _iid_ = Guid('{88e30eab-f3b7-420b-b086-8a80c07d910d}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialAnchorStore]: ...
class ISpatialAnchorRawCoordinateSystemAdjustedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorRawCoordinateSystemAdjustedEventArgs'
    _iid_ = Guid('{a1e81eb8-56c7-3117-a2e4-81e0fcf28e00}')
    @winrt_commethod(6)
    def get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform(self) -> Windows.Foundation.Numerics.Matrix4x4: ...
    OldRawCoordinateSystemToNewRawCoordinateSystemTransform = property(get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform, None)
class ISpatialAnchorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorStatics'
    _iid_ = Guid('{a9928642-0174-311c-ae79-0e5107669f16}')
    @winrt_commethod(6)
    def TryCreateRelativeTo(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_commethod(7)
    def TryCreateWithPositionRelativeTo(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3) -> Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_commethod(8)
    def TryCreateWithPositionAndOrientationRelativeTo(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Perception.Spatial.SpatialAnchor: ...
class ISpatialAnchorStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorStore'
    _iid_ = Guid('{b0bc3636-486a-3cb0-9e6f-1245165c4db6}')
    @winrt_commethod(6)
    def GetAllSavedAnchors(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Perception.Spatial.SpatialAnchor]: ...
    @winrt_commethod(7)
    def TrySave(self, id: WinRT_String, anchor: Windows.Perception.Spatial.SpatialAnchor) -> Boolean: ...
    @winrt_commethod(8)
    def Remove(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def Clear(self) -> Void: ...
class ISpatialAnchorTransferManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics'
    _iid_ = Guid('{03bbf9b9-12d8-4bce-8835-c5df3ac0adab}')
    @winrt_commethod(6)
    def TryImportAnchorsAsync(self, stream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Perception.Spatial.SpatialAnchor]]: ...
    @winrt_commethod(7)
    def TryExportAnchorsAsync(self, anchors: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Perception.Spatial.SpatialAnchor]], stream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class ISpatialBoundingVolume(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialBoundingVolume'
    _iid_ = Guid('{fb2065da-68c3-33df-b7af-4c787207999c}')
class ISpatialBoundingVolumeStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialBoundingVolumeStatics'
    _iid_ = Guid('{05889117-b3e1-36d8-b017-566181a5b196}')
    @winrt_commethod(6)
    def FromBox(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, box: Windows.Perception.Spatial.SpatialBoundingBox) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_commethod(7)
    def FromOrientedBox(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, box: Windows.Perception.Spatial.SpatialBoundingOrientedBox) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_commethod(8)
    def FromSphere(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, sphere: Windows.Perception.Spatial.SpatialBoundingSphere) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_commethod(9)
    def FromFrustum(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, frustum: Windows.Perception.Spatial.SpatialBoundingFrustum) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
class ISpatialCoordinateSystem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialCoordinateSystem'
    _iid_ = Guid('{69ebca4b-60a3-3586-a653-59a7bd676d07}')
    @winrt_commethod(6)
    def TryGetTransformTo(self, target: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Matrix4x4]: ...
class ISpatialEntity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntity'
    _iid_ = Guid('{166de955-e1eb-454c-ba08-e6c0668ddc65}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Anchor(self) -> Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.Foundation.Collections.ValueSet: ...
    Id = property(get_Id, None)
    Anchor = property(get_Anchor, None)
    Properties = property(get_Properties, None)
class ISpatialEntityAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityAddedEventArgs'
    _iid_ = Guid('{a397f49b-156a-4707-ac2c-d31d570ed399}')
    @winrt_commethod(6)
    def get_Entity(self) -> Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class ISpatialEntityFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityFactory'
    _iid_ = Guid('{e1f1e325-349f-4225-a2f3-4b01c15fe056}')
    @winrt_commethod(6)
    def CreateWithSpatialAnchor(self, spatialAnchor: Windows.Perception.Spatial.SpatialAnchor) -> Windows.Perception.Spatial.SpatialEntity: ...
    @winrt_commethod(7)
    def CreateWithSpatialAnchorAndProperties(self, spatialAnchor: Windows.Perception.Spatial.SpatialAnchor, propertySet: Windows.Foundation.Collections.ValueSet) -> Windows.Perception.Spatial.SpatialEntity: ...
class ISpatialEntityRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityRemovedEventArgs'
    _iid_ = Guid('{91741800-536d-4e9f-abf6-415b5444d651}')
    @winrt_commethod(6)
    def get_Entity(self) -> Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class ISpatialEntityStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityStore'
    _iid_ = Guid('{329788ba-e513-4f06-889d-1be30ecf43e6}')
    @winrt_commethod(6)
    def SaveAsync(self, entity: Windows.Perception.Spatial.SpatialEntity) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RemoveAsync(self, entity: Windows.Perception.Spatial.SpatialEntity) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def CreateEntityWatcher(self) -> Windows.Perception.Spatial.SpatialEntityWatcher: ...
class ISpatialEntityStoreStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityStoreStatics'
    _iid_ = Guid('{6b4b389e-7c50-4e92-8a62-4d1d4b7ccd3e}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryGetForRemoteSystemSession(self, session: Windows.System.RemoteSystems.RemoteSystemSession) -> Windows.Perception.Spatial.SpatialEntityStore: ...
    IsSupported = property(get_IsSupported, None)
class ISpatialEntityUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityUpdatedEventArgs'
    _iid_ = Guid('{e5671766-627b-43cb-a49f-b3be6d47deed}')
    @winrt_commethod(6)
    def get_Entity(self) -> Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class ISpatialEntityWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityWatcher'
    _iid_ = Guid('{b3b85fa0-6d5e-4bbc-805d-5fe5b9ba1959}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Perception.Spatial.SpatialEntityWatcherStatus: ...
    @winrt_commethod(7)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Perception.Spatial.SpatialEntityAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Perception.Spatial.SpatialEntityUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Perception.Spatial.SpatialEntityRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class ISpatialLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocation'
    _iid_ = Guid('{1d81d29d-24a1-37d5-8fa1-39b4f9ad67e2}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_Orientation(self) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(8)
    def get_AbsoluteLinearVelocity(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_AbsoluteLinearAcceleration(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(10)
    def get_AbsoluteAngularVelocity(self) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(11)
    def get_AbsoluteAngularAcceleration(self) -> Windows.Foundation.Numerics.Quaternion: ...
    Position = property(get_Position, None)
    Orientation = property(get_Orientation, None)
    AbsoluteLinearVelocity = property(get_AbsoluteLinearVelocity, None)
    AbsoluteLinearAcceleration = property(get_AbsoluteLinearAcceleration, None)
    AbsoluteAngularVelocity = property(get_AbsoluteAngularVelocity, None)
    AbsoluteAngularAcceleration = property(get_AbsoluteAngularAcceleration, None)
class ISpatialLocation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocation2'
    _iid_ = Guid('{117f2416-38a7-4a18-b404-ab8fabe1d78b}')
    @winrt_commethod(6)
    def get_AbsoluteAngularVelocityAxisAngle(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_AbsoluteAngularAccelerationAxisAngle(self) -> Windows.Foundation.Numerics.Vector3: ...
    AbsoluteAngularVelocityAxisAngle = property(get_AbsoluteAngularVelocityAxisAngle, None)
    AbsoluteAngularAccelerationAxisAngle = property(get_AbsoluteAngularAccelerationAxisAngle, None)
class ISpatialLocator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocator'
    _iid_ = Guid('{f6478925-9e0c-3bb6-997e-b64ecca24cf4}')
    @winrt_commethod(6)
    def get_Locatability(self) -> Windows.Perception.Spatial.SpatialLocatability: ...
    @winrt_commethod(7)
    def add_LocatabilityChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialLocator, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_LocatabilityChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PositionalTrackingDeactivating(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialLocator, Windows.Perception.Spatial.SpatialLocatorPositionalTrackingDeactivatingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PositionalTrackingDeactivating(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def TryLocateAtTimestamp(self, timestamp: Windows.Perception.PerceptionTimestamp, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Perception.Spatial.SpatialLocation: ...
    @winrt_commethod(12)
    def CreateAttachedFrameOfReferenceAtCurrentHeading(self) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(13)
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPosition(self, relativePosition: Windows.Foundation.Numerics.Vector3) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(14)
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientation(self, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(15)
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientationAndRelativeHeading(self, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(16)
    def CreateStationaryFrameOfReferenceAtCurrentLocation(self) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_commethod(17)
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPosition(self, relativePosition: Windows.Foundation.Numerics.Vector3) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_commethod(18)
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientation(self, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_commethod(19)
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientationAndRelativeHeading(self, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    Locatability = property(get_Locatability, None)
class ISpatialLocatorAttachedFrameOfReference(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference'
    _iid_ = Guid('{e1774ef6-1f4f-499c-9625-ef5e6ed7a048}')
    @winrt_commethod(6)
    def get_RelativePosition(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def put_RelativePosition(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(8)
    def get_RelativeOrientation(self) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(9)
    def put_RelativeOrientation(self, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(10)
    def AdjustHeading(self, headingOffsetInRadians: Double) -> Void: ...
    @winrt_commethod(11)
    def GetStationaryCoordinateSystemAtTimestamp(self, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(12)
    def TryGetRelativeHeadingAtTimestamp(self, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.Foundation.IReference[Double]: ...
    RelativePosition = property(get_RelativePosition, put_RelativePosition)
    RelativeOrientation = property(get_RelativeOrientation, put_RelativeOrientation)
class ISpatialLocatorPositionalTrackingDeactivatingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs'
    _iid_ = Guid('{b8a84063-e3f4-368b-9061-9ea9d1d6cc16}')
    @winrt_commethod(6)
    def get_Canceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Canceled(self, value: Boolean) -> Void: ...
    Canceled = property(get_Canceled, put_Canceled)
class ISpatialLocatorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocatorStatics'
    _iid_ = Guid('{b76e3340-a7c2-361b-bb82-56e93b89b1bb}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Perception.Spatial.SpatialLocator: ...
class ISpatialStageFrameOfReference(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialStageFrameOfReference'
    _iid_ = Guid('{7a8a3464-ad0d-4590-ab86-33062b674926}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def get_MovementRange(self) -> Windows.Perception.Spatial.SpatialMovementRange: ...
    @winrt_commethod(8)
    def get_LookDirectionRange(self) -> Windows.Perception.Spatial.SpatialLookDirectionRange: ...
    @winrt_commethod(9)
    def GetCoordinateSystemAtCurrentLocation(self, locator: Windows.Perception.Spatial.SpatialLocator) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(10)
    def TryGetMovementBounds(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> POINTER(Windows.Foundation.Numerics.Vector3_head): ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    MovementRange = property(get_MovementRange, None)
    LookDirectionRange = property(get_LookDirectionRange, None)
class ISpatialStageFrameOfReferenceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics'
    _iid_ = Guid('{f78d5c4d-a0a4-499c-8d91-a8c965d40654}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.Perception.Spatial.SpatialStageFrameOfReference: ...
    @winrt_commethod(7)
    def add_CurrentChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CurrentChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def RequestNewStageAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialStageFrameOfReference]: ...
    Current = property(get_Current, None)
class ISpatialStationaryFrameOfReference(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialStationaryFrameOfReference'
    _iid_ = Guid('{09dbccb9-bcf8-3e7f-be7e-7edccbb178a8}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
class SpatialAnchor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialAnchor
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchor'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Perception.Spatial.ISpatialAnchor) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_RawCoordinateSystem(self: Windows.Perception.Spatial.ISpatialAnchor) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def add_RawCoordinateSystemAdjusted(self: Windows.Perception.Spatial.ISpatialAnchor, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialAnchor, Windows.Perception.Spatial.SpatialAnchorRawCoordinateSystemAdjustedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RawCoordinateSystemAdjusted(self: Windows.Perception.Spatial.ISpatialAnchor, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_RemovedByUser(self: Windows.Perception.Spatial.ISpatialAnchor2) -> Boolean: ...
    @winrt_classmethod
    def TryCreateRelativeTo(cls: Windows.Perception.Spatial.ISpatialAnchorStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_classmethod
    def TryCreateWithPositionRelativeTo(cls: Windows.Perception.Spatial.ISpatialAnchorStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3) -> Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_classmethod
    def TryCreateWithPositionAndOrientationRelativeTo(cls: Windows.Perception.Spatial.ISpatialAnchorStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Perception.Spatial.SpatialAnchor: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    RawCoordinateSystem = property(get_RawCoordinateSystem, None)
    RemovedByUser = property(get_RemovedByUser, None)
SpatialAnchorExportPurpose = Int32
SpatialAnchorExportPurpose_Relocalization: SpatialAnchorExportPurpose = 0
SpatialAnchorExportPurpose_Sharing: SpatialAnchorExportPurpose = 1
class SpatialAnchorExportSufficiency(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialAnchorExportSufficiency
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorExportSufficiency'
    @winrt_mixinmethod
    def get_IsMinimallySufficient(self: Windows.Perception.Spatial.ISpatialAnchorExportSufficiency) -> Boolean: ...
    @winrt_mixinmethod
    def get_SufficiencyLevel(self: Windows.Perception.Spatial.ISpatialAnchorExportSufficiency) -> Double: ...
    @winrt_mixinmethod
    def get_RecommendedSufficiencyLevel(self: Windows.Perception.Spatial.ISpatialAnchorExportSufficiency) -> Double: ...
    IsMinimallySufficient = property(get_IsMinimallySufficient, None)
    SufficiencyLevel = property(get_SufficiencyLevel, None)
    RecommendedSufficiencyLevel = property(get_RecommendedSufficiencyLevel, None)
class SpatialAnchorExporter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialAnchorExporter
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorExporter'
    @winrt_mixinmethod
    def GetAnchorExportSufficiencyAsync(self: Windows.Perception.Spatial.ISpatialAnchorExporter, anchor: Windows.Perception.Spatial.SpatialAnchor, purpose: Windows.Perception.Spatial.SpatialAnchorExportPurpose) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialAnchorExportSufficiency]: ...
    @winrt_mixinmethod
    def TryExportAnchorAsync(self: Windows.Perception.Spatial.ISpatialAnchorExporter, anchor: Windows.Perception.Spatial.SpatialAnchor, purpose: Windows.Perception.Spatial.SpatialAnchorExportPurpose, stream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Perception.Spatial.ISpatialAnchorExporterStatics) -> Windows.Perception.Spatial.SpatialAnchorExporter: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Perception.Spatial.ISpatialAnchorExporterStatics) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class SpatialAnchorManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorManager'
    @winrt_classmethod
    def RequestStoreAsync(cls: Windows.Perception.Spatial.ISpatialAnchorManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialAnchorStore]: ...
class SpatialAnchorRawCoordinateSystemAdjustedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialAnchorRawCoordinateSystemAdjustedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorRawCoordinateSystemAdjustedEventArgs'
    @winrt_mixinmethod
    def get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform(self: Windows.Perception.Spatial.ISpatialAnchorRawCoordinateSystemAdjustedEventArgs) -> Windows.Foundation.Numerics.Matrix4x4: ...
    OldRawCoordinateSystemToNewRawCoordinateSystemTransform = property(get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform, None)
class SpatialAnchorStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialAnchorStore
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorStore'
    @winrt_mixinmethod
    def GetAllSavedAnchors(self: Windows.Perception.Spatial.ISpatialAnchorStore) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Perception.Spatial.SpatialAnchor]: ...
    @winrt_mixinmethod
    def TrySave(self: Windows.Perception.Spatial.ISpatialAnchorStore, id: WinRT_String, anchor: Windows.Perception.Spatial.SpatialAnchor) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Perception.Spatial.ISpatialAnchorStore, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Perception.Spatial.ISpatialAnchorStore) -> Void: ...
class SpatialAnchorTransferManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorTransferManager'
    @winrt_classmethod
    def TryImportAnchorsAsync(cls: Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics, stream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Perception.Spatial.SpatialAnchor]]: ...
    @winrt_classmethod
    def TryExportAnchorsAsync(cls: Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics, anchors: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Perception.Spatial.SpatialAnchor]], stream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class SpatialBoundingBox(EasyCastStructure):
    Center: Windows.Foundation.Numerics.Vector3
    Extents: Windows.Foundation.Numerics.Vector3
class SpatialBoundingFrustum(EasyCastStructure):
    Near: Windows.Foundation.Numerics.Plane
    Far: Windows.Foundation.Numerics.Plane
    Right: Windows.Foundation.Numerics.Plane
    Left: Windows.Foundation.Numerics.Plane
    Top: Windows.Foundation.Numerics.Plane
    Bottom: Windows.Foundation.Numerics.Plane
class SpatialBoundingOrientedBox(EasyCastStructure):
    Center: Windows.Foundation.Numerics.Vector3
    Extents: Windows.Foundation.Numerics.Vector3
    Orientation: Windows.Foundation.Numerics.Quaternion
class SpatialBoundingSphere(EasyCastStructure):
    Center: Windows.Foundation.Numerics.Vector3
    Radius: Single
class SpatialBoundingVolume(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialBoundingVolume
    _classid_ = 'Windows.Perception.Spatial.SpatialBoundingVolume'
    @winrt_classmethod
    def FromBox(cls: Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, box: Windows.Perception.Spatial.SpatialBoundingBox) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_classmethod
    def FromOrientedBox(cls: Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, box: Windows.Perception.Spatial.SpatialBoundingOrientedBox) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_classmethod
    def FromSphere(cls: Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, sphere: Windows.Perception.Spatial.SpatialBoundingSphere) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_classmethod
    def FromFrustum(cls: Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, frustum: Windows.Perception.Spatial.SpatialBoundingFrustum) -> Windows.Perception.Spatial.SpatialBoundingVolume: ...
class SpatialCoordinateSystem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialCoordinateSystem
    _classid_ = 'Windows.Perception.Spatial.SpatialCoordinateSystem'
    @winrt_mixinmethod
    def TryGetTransformTo(self: Windows.Perception.Spatial.ISpatialCoordinateSystem, target: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Matrix4x4]: ...
class SpatialEntity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialEntity
    _classid_ = 'Windows.Perception.Spatial.SpatialEntity'
    @winrt_factorymethod
    def CreateWithSpatialAnchor(cls: Windows.Perception.Spatial.ISpatialEntityFactory, spatialAnchor: Windows.Perception.Spatial.SpatialAnchor) -> Windows.Perception.Spatial.SpatialEntity: ...
    @winrt_factorymethod
    def CreateWithSpatialAnchorAndProperties(cls: Windows.Perception.Spatial.ISpatialEntityFactory, spatialAnchor: Windows.Perception.Spatial.SpatialAnchor, propertySet: Windows.Foundation.Collections.ValueSet) -> Windows.Perception.Spatial.SpatialEntity: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Perception.Spatial.ISpatialEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Anchor(self: Windows.Perception.Spatial.ISpatialEntity) -> Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Perception.Spatial.ISpatialEntity) -> Windows.Foundation.Collections.ValueSet: ...
    Id = property(get_Id, None)
    Anchor = property(get_Anchor, None)
    Properties = property(get_Properties, None)
class SpatialEntityAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialEntityAddedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityAddedEventArgs'
    @winrt_mixinmethod
    def get_Entity(self: Windows.Perception.Spatial.ISpatialEntityAddedEventArgs) -> Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class SpatialEntityRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialEntityRemovedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityRemovedEventArgs'
    @winrt_mixinmethod
    def get_Entity(self: Windows.Perception.Spatial.ISpatialEntityRemovedEventArgs) -> Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class _SpatialEntityStore_Meta_(ComPtr.__class__):
    pass
class SpatialEntityStore(ComPtr, metaclass=_SpatialEntityStore_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialEntityStore
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityStore'
    @winrt_mixinmethod
    def SaveAsync(self: Windows.Perception.Spatial.ISpatialEntityStore, entity: Windows.Perception.Spatial.SpatialEntity) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveAsync(self: Windows.Perception.Spatial.ISpatialEntityStore, entity: Windows.Perception.Spatial.SpatialEntity) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateEntityWatcher(self: Windows.Perception.Spatial.ISpatialEntityStore) -> Windows.Perception.Spatial.SpatialEntityWatcher: ...
    @winrt_classmethod
    def get_IsSupported(cls: Windows.Perception.Spatial.ISpatialEntityStoreStatics) -> Boolean: ...
    @winrt_classmethod
    def TryGetForRemoteSystemSession(cls: Windows.Perception.Spatial.ISpatialEntityStoreStatics, session: Windows.System.RemoteSystems.RemoteSystemSession) -> Windows.Perception.Spatial.SpatialEntityStore: ...
    _SpatialEntityStore_Meta_.IsSupported = property(get_IsSupported.__wrapped__, None)
class SpatialEntityUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialEntityUpdatedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Entity(self: Windows.Perception.Spatial.ISpatialEntityUpdatedEventArgs) -> Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class SpatialEntityWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialEntityWatcher
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityWatcher'
    @winrt_mixinmethod
    def get_Status(self: Windows.Perception.Spatial.ISpatialEntityWatcher) -> Windows.Perception.Spatial.SpatialEntityWatcherStatus: ...
    @winrt_mixinmethod
    def add_Added(self: Windows.Perception.Spatial.ISpatialEntityWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Perception.Spatial.SpatialEntityAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Perception.Spatial.ISpatialEntityWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Perception.Spatial.ISpatialEntityWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Perception.Spatial.SpatialEntityUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Perception.Spatial.ISpatialEntityWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Perception.Spatial.ISpatialEntityWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Perception.Spatial.SpatialEntityRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Perception.Spatial.ISpatialEntityWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Perception.Spatial.ISpatialEntityWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialEntityWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Perception.Spatial.ISpatialEntityWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Perception.Spatial.ISpatialEntityWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Perception.Spatial.ISpatialEntityWatcher) -> Void: ...
    Status = property(get_Status, None)
SpatialEntityWatcherStatus = Int32
SpatialEntityWatcherStatus_Created: SpatialEntityWatcherStatus = 0
SpatialEntityWatcherStatus_Started: SpatialEntityWatcherStatus = 1
SpatialEntityWatcherStatus_EnumerationCompleted: SpatialEntityWatcherStatus = 2
SpatialEntityWatcherStatus_Stopping: SpatialEntityWatcherStatus = 3
SpatialEntityWatcherStatus_Stopped: SpatialEntityWatcherStatus = 4
SpatialEntityWatcherStatus_Aborted: SpatialEntityWatcherStatus = 5
SpatialLocatability = Int32
SpatialLocatability_Unavailable: SpatialLocatability = 0
SpatialLocatability_OrientationOnly: SpatialLocatability = 1
SpatialLocatability_PositionalTrackingActivating: SpatialLocatability = 2
SpatialLocatability_PositionalTrackingActive: SpatialLocatability = 3
SpatialLocatability_PositionalTrackingInhibited: SpatialLocatability = 4
class SpatialLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialLocation
    _classid_ = 'Windows.Perception.Spatial.SpatialLocation'
    @winrt_mixinmethod
    def get_Position(self: Windows.Perception.Spatial.ISpatialLocation) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Perception.Spatial.ISpatialLocation) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_AbsoluteLinearVelocity(self: Windows.Perception.Spatial.ISpatialLocation) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_AbsoluteLinearAcceleration(self: Windows.Perception.Spatial.ISpatialLocation) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularVelocity(self: Windows.Perception.Spatial.ISpatialLocation) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularAcceleration(self: Windows.Perception.Spatial.ISpatialLocation) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularVelocityAxisAngle(self: Windows.Perception.Spatial.ISpatialLocation2) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularAccelerationAxisAngle(self: Windows.Perception.Spatial.ISpatialLocation2) -> Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    Orientation = property(get_Orientation, None)
    AbsoluteLinearVelocity = property(get_AbsoluteLinearVelocity, None)
    AbsoluteLinearAcceleration = property(get_AbsoluteLinearAcceleration, None)
    AbsoluteAngularVelocity = property(get_AbsoluteAngularVelocity, None)
    AbsoluteAngularAcceleration = property(get_AbsoluteAngularAcceleration, None)
    AbsoluteAngularVelocityAxisAngle = property(get_AbsoluteAngularVelocityAxisAngle, None)
    AbsoluteAngularAccelerationAxisAngle = property(get_AbsoluteAngularAccelerationAxisAngle, None)
class SpatialLocator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialLocator
    _classid_ = 'Windows.Perception.Spatial.SpatialLocator'
    @winrt_mixinmethod
    def get_Locatability(self: Windows.Perception.Spatial.ISpatialLocator) -> Windows.Perception.Spatial.SpatialLocatability: ...
    @winrt_mixinmethod
    def add_LocatabilityChanged(self: Windows.Perception.Spatial.ISpatialLocator, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialLocator, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LocatabilityChanged(self: Windows.Perception.Spatial.ISpatialLocator, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PositionalTrackingDeactivating(self: Windows.Perception.Spatial.ISpatialLocator, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.SpatialLocator, Windows.Perception.Spatial.SpatialLocatorPositionalTrackingDeactivatingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PositionalTrackingDeactivating(self: Windows.Perception.Spatial.ISpatialLocator, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryLocateAtTimestamp(self: Windows.Perception.Spatial.ISpatialLocator, timestamp: Windows.Perception.PerceptionTimestamp, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Perception.Spatial.SpatialLocation: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeading(self: Windows.Perception.Spatial.ISpatialLocator) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPosition(self: Windows.Perception.Spatial.ISpatialLocator, relativePosition: Windows.Foundation.Numerics.Vector3) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientation(self: Windows.Perception.Spatial.ISpatialLocator, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientationAndRelativeHeading(self: Windows.Perception.Spatial.ISpatialLocator, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocation(self: Windows.Perception.Spatial.ISpatialLocator) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPosition(self: Windows.Perception.Spatial.ISpatialLocator, relativePosition: Windows.Foundation.Numerics.Vector3) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientation(self: Windows.Perception.Spatial.ISpatialLocator, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientationAndRelativeHeading(self: Windows.Perception.Spatial.ISpatialLocator, relativePosition: Windows.Foundation.Numerics.Vector3, relativeOrientation: Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Perception.Spatial.ISpatialLocatorStatics) -> Windows.Perception.Spatial.SpatialLocator: ...
    Locatability = property(get_Locatability, None)
class SpatialLocatorAttachedFrameOfReference(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference
    _classid_ = 'Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference'
    @winrt_mixinmethod
    def get_RelativePosition(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RelativePosition(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeOrientation(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_RelativeOrientation(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def AdjustHeading(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, headingOffsetInRadians: Double) -> Void: ...
    @winrt_mixinmethod
    def GetStationaryCoordinateSystemAtTimestamp(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def TryGetRelativeHeadingAtTimestamp(self: Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.Foundation.IReference[Double]: ...
    RelativePosition = property(get_RelativePosition, put_RelativePosition)
    RelativeOrientation = property(get_RelativeOrientation, put_RelativeOrientation)
class SpatialLocatorPositionalTrackingDeactivatingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialLocatorPositionalTrackingDeactivatingEventArgs'
    @winrt_mixinmethod
    def get_Canceled(self: Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Canceled(self: Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs, value: Boolean) -> Void: ...
    Canceled = property(get_Canceled, put_Canceled)
SpatialLookDirectionRange = Int32
SpatialLookDirectionRange_ForwardOnly: SpatialLookDirectionRange = 0
SpatialLookDirectionRange_Omnidirectional: SpatialLookDirectionRange = 1
SpatialMovementRange = Int32
SpatialMovementRange_NoMovement: SpatialMovementRange = 0
SpatialMovementRange_Bounded: SpatialMovementRange = 1
SpatialPerceptionAccessStatus = Int32
SpatialPerceptionAccessStatus_Unspecified: SpatialPerceptionAccessStatus = 0
SpatialPerceptionAccessStatus_Allowed: SpatialPerceptionAccessStatus = 1
SpatialPerceptionAccessStatus_DeniedByUser: SpatialPerceptionAccessStatus = 2
SpatialPerceptionAccessStatus_DeniedBySystem: SpatialPerceptionAccessStatus = 3
class SpatialRay(EasyCastStructure):
    Origin: Windows.Foundation.Numerics.Vector3
    Direction: Windows.Foundation.Numerics.Vector3
class _SpatialStageFrameOfReference_Meta_(ComPtr.__class__):
    pass
class SpatialStageFrameOfReference(ComPtr, metaclass=_SpatialStageFrameOfReference_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialStageFrameOfReference
    _classid_ = 'Windows.Perception.Spatial.SpatialStageFrameOfReference'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Perception.Spatial.ISpatialStageFrameOfReference) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_MovementRange(self: Windows.Perception.Spatial.ISpatialStageFrameOfReference) -> Windows.Perception.Spatial.SpatialMovementRange: ...
    @winrt_mixinmethod
    def get_LookDirectionRange(self: Windows.Perception.Spatial.ISpatialStageFrameOfReference) -> Windows.Perception.Spatial.SpatialLookDirectionRange: ...
    @winrt_mixinmethod
    def GetCoordinateSystemAtCurrentLocation(self: Windows.Perception.Spatial.ISpatialStageFrameOfReference, locator: Windows.Perception.Spatial.SpatialLocator) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def TryGetMovementBounds(self: Windows.Perception.Spatial.ISpatialStageFrameOfReference, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> POINTER(Windows.Foundation.Numerics.Vector3_head): ...
    @winrt_classmethod
    def get_Current(cls: Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics) -> Windows.Perception.Spatial.SpatialStageFrameOfReference: ...
    @winrt_classmethod
    def add_CurrentChanged(cls: Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CurrentChanged(cls: Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestNewStageAsync(cls: Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialStageFrameOfReference]: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    MovementRange = property(get_MovementRange, None)
    LookDirectionRange = property(get_LookDirectionRange, None)
    _SpatialStageFrameOfReference_Meta_.Current = property(get_Current.__wrapped__, None)
class SpatialStationaryFrameOfReference(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.ISpatialStationaryFrameOfReference
    _classid_ = 'Windows.Perception.Spatial.SpatialStationaryFrameOfReference'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Perception.Spatial.ISpatialStationaryFrameOfReference) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
make_head(_module, 'ISpatialAnchor')
make_head(_module, 'ISpatialAnchor2')
make_head(_module, 'ISpatialAnchorExportSufficiency')
make_head(_module, 'ISpatialAnchorExporter')
make_head(_module, 'ISpatialAnchorExporterStatics')
make_head(_module, 'ISpatialAnchorManagerStatics')
make_head(_module, 'ISpatialAnchorRawCoordinateSystemAdjustedEventArgs')
make_head(_module, 'ISpatialAnchorStatics')
make_head(_module, 'ISpatialAnchorStore')
make_head(_module, 'ISpatialAnchorTransferManagerStatics')
make_head(_module, 'ISpatialBoundingVolume')
make_head(_module, 'ISpatialBoundingVolumeStatics')
make_head(_module, 'ISpatialCoordinateSystem')
make_head(_module, 'ISpatialEntity')
make_head(_module, 'ISpatialEntityAddedEventArgs')
make_head(_module, 'ISpatialEntityFactory')
make_head(_module, 'ISpatialEntityRemovedEventArgs')
make_head(_module, 'ISpatialEntityStore')
make_head(_module, 'ISpatialEntityStoreStatics')
make_head(_module, 'ISpatialEntityUpdatedEventArgs')
make_head(_module, 'ISpatialEntityWatcher')
make_head(_module, 'ISpatialLocation')
make_head(_module, 'ISpatialLocation2')
make_head(_module, 'ISpatialLocator')
make_head(_module, 'ISpatialLocatorAttachedFrameOfReference')
make_head(_module, 'ISpatialLocatorPositionalTrackingDeactivatingEventArgs')
make_head(_module, 'ISpatialLocatorStatics')
make_head(_module, 'ISpatialStageFrameOfReference')
make_head(_module, 'ISpatialStageFrameOfReferenceStatics')
make_head(_module, 'ISpatialStationaryFrameOfReference')
make_head(_module, 'SpatialAnchor')
make_head(_module, 'SpatialAnchorExportSufficiency')
make_head(_module, 'SpatialAnchorExporter')
make_head(_module, 'SpatialAnchorManager')
make_head(_module, 'SpatialAnchorRawCoordinateSystemAdjustedEventArgs')
make_head(_module, 'SpatialAnchorStore')
make_head(_module, 'SpatialAnchorTransferManager')
make_head(_module, 'SpatialBoundingBox')
make_head(_module, 'SpatialBoundingFrustum')
make_head(_module, 'SpatialBoundingOrientedBox')
make_head(_module, 'SpatialBoundingSphere')
make_head(_module, 'SpatialBoundingVolume')
make_head(_module, 'SpatialCoordinateSystem')
make_head(_module, 'SpatialEntity')
make_head(_module, 'SpatialEntityAddedEventArgs')
make_head(_module, 'SpatialEntityRemovedEventArgs')
make_head(_module, 'SpatialEntityStore')
make_head(_module, 'SpatialEntityUpdatedEventArgs')
make_head(_module, 'SpatialEntityWatcher')
make_head(_module, 'SpatialLocation')
make_head(_module, 'SpatialLocator')
make_head(_module, 'SpatialLocatorAttachedFrameOfReference')
make_head(_module, 'SpatialLocatorPositionalTrackingDeactivatingEventArgs')
make_head(_module, 'SpatialRay')
make_head(_module, 'SpatialStageFrameOfReference')
make_head(_module, 'SpatialStationaryFrameOfReference')
