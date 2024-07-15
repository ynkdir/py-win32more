from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception
import win32more.Windows.Perception.Spatial
import win32more.Windows.Storage.Streams
import win32more.Windows.System.RemoteSystems
import win32more.Windows.Win32.System.WinRT
class ISpatialAnchor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchor'
    _iid_ = Guid('{0529e5ce-1d34-3702-bcec-eabff578a869}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def get_RawCoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(8)
    def add_RawCoordinateSystemAdjusted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialAnchor, win32more.Windows.Perception.Spatial.SpatialAnchorRawCoordinateSystemAdjustedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RawCoordinateSystemAdjusted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    RawCoordinateSystem = property(get_RawCoordinateSystem, None)
    RawCoordinateSystemAdjusted = event()
class ISpatialAnchor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchor2'
    _iid_ = Guid('{ed17c908-a695-4cf6-92fd-97263ba71047}')
    @winrt_commethod(6)
    def get_RemovedByUser(self) -> Boolean: ...
    RemovedByUser = property(get_RemovedByUser, None)
class ISpatialAnchorExportSufficiency(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorExportSufficiency'
    _iid_ = Guid('{77c25b2b-3409-4088-b91b-fdfd05d1648f}')
    @winrt_commethod(6)
    def get_IsMinimallySufficient(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SufficiencyLevel(self) -> Double: ...
    @winrt_commethod(8)
    def get_RecommendedSufficiencyLevel(self) -> Double: ...
    IsMinimallySufficient = property(get_IsMinimallySufficient, None)
    RecommendedSufficiencyLevel = property(get_RecommendedSufficiencyLevel, None)
    SufficiencyLevel = property(get_SufficiencyLevel, None)
class ISpatialAnchorExporter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorExporter'
    _iid_ = Guid('{9a2a4338-24fb-4269-89c5-88304aeef20f}')
    @winrt_commethod(6)
    def GetAnchorExportSufficiencyAsync(self, anchor: win32more.Windows.Perception.Spatial.SpatialAnchor, purpose: win32more.Windows.Perception.Spatial.SpatialAnchorExportPurpose) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialAnchorExportSufficiency]: ...
    @winrt_commethod(7)
    def TryExportAnchorAsync(self, anchor: win32more.Windows.Perception.Spatial.SpatialAnchor, purpose: win32more.Windows.Perception.Spatial.SpatialAnchorExportPurpose, stream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISpatialAnchorExporterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorExporterStatics'
    _iid_ = Guid('{ed2507b8-2475-439c-85ff-7fed341fdc88}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Perception.Spatial.SpatialAnchorExporter: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class ISpatialAnchorManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorManagerStatics'
    _iid_ = Guid('{88e30eab-f3b7-420b-b086-8a80c07d910d}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialAnchorStore]: ...
class ISpatialAnchorRawCoordinateSystemAdjustedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorRawCoordinateSystemAdjustedEventArgs'
    _iid_ = Guid('{a1e81eb8-56c7-3117-a2e4-81e0fcf28e00}')
    @winrt_commethod(6)
    def get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform(self) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    OldRawCoordinateSystemToNewRawCoordinateSystemTransform = property(get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform, None)
class ISpatialAnchorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorStatics'
    _iid_ = Guid('{a9928642-0174-311c-ae79-0e5107669f16}')
    @winrt_commethod(6)
    def TryCreateRelativeTo(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_commethod(7)
    def TryCreateWithPositionRelativeTo(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_commethod(8)
    def TryCreateWithPositionAndOrientationRelativeTo(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
class ISpatialAnchorStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorStore'
    _iid_ = Guid('{b0bc3636-486a-3cb0-9e6f-1245165c4db6}')
    @winrt_commethod(6)
    def GetAllSavedAnchors(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Perception.Spatial.SpatialAnchor]: ...
    @winrt_commethod(7)
    def TrySave(self, id: WinRT_String, anchor: win32more.Windows.Perception.Spatial.SpatialAnchor) -> Boolean: ...
    @winrt_commethod(8)
    def Remove(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def Clear(self) -> Void: ...
class ISpatialAnchorTransferManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics'
    _iid_ = Guid('{03bbf9b9-12d8-4bce-8835-c5df3ac0adab}')
    @winrt_commethod(6)
    def TryImportAnchorsAsync(self, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Perception.Spatial.SpatialAnchor]]: ...
    @winrt_commethod(7)
    def TryExportAnchorsAsync(self, anchors: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Perception.Spatial.SpatialAnchor]], stream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class ISpatialBoundingVolume(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialBoundingVolume'
    _iid_ = Guid('{fb2065da-68c3-33df-b7af-4c787207999c}')
class ISpatialBoundingVolumeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialBoundingVolumeStatics'
    _iid_ = Guid('{05889117-b3e1-36d8-b017-566181a5b196}')
    @winrt_commethod(6)
    def FromBox(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, box: win32more.Windows.Perception.Spatial.SpatialBoundingBox) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_commethod(7)
    def FromOrientedBox(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, box: win32more.Windows.Perception.Spatial.SpatialBoundingOrientedBox) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_commethod(8)
    def FromSphere(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, sphere: win32more.Windows.Perception.Spatial.SpatialBoundingSphere) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_commethod(9)
    def FromFrustum(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, frustum: win32more.Windows.Perception.Spatial.SpatialBoundingFrustum) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
class ISpatialCoordinateSystem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialCoordinateSystem'
    _iid_ = Guid('{69ebca4b-60a3-3586-a653-59a7bd676d07}')
    @winrt_commethod(6)
    def TryGetTransformTo(self, target: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Matrix4x4]: ...
class ISpatialEntity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntity'
    _iid_ = Guid('{166de955-e1eb-454c-ba08-e6c0668ddc65}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Anchor(self) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Anchor = property(get_Anchor, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class ISpatialEntityAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityAddedEventArgs'
    _iid_ = Guid('{a397f49b-156a-4707-ac2c-d31d570ed399}')
    @winrt_commethod(6)
    def get_Entity(self) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class ISpatialEntityFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityFactory'
    _iid_ = Guid('{e1f1e325-349f-4225-a2f3-4b01c15fe056}')
    @winrt_commethod(6)
    def CreateWithSpatialAnchor(self, spatialAnchor: win32more.Windows.Perception.Spatial.SpatialAnchor) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    @winrt_commethod(7)
    def CreateWithSpatialAnchorAndProperties(self, spatialAnchor: win32more.Windows.Perception.Spatial.SpatialAnchor, propertySet: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
class ISpatialEntityRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityRemovedEventArgs'
    _iid_ = Guid('{91741800-536d-4e9f-abf6-415b5444d651}')
    @winrt_commethod(6)
    def get_Entity(self) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class ISpatialEntityStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityStore'
    _iid_ = Guid('{329788ba-e513-4f06-889d-1be30ecf43e6}')
    @winrt_commethod(6)
    def SaveAsync(self, entity: win32more.Windows.Perception.Spatial.SpatialEntity) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RemoveAsync(self, entity: win32more.Windows.Perception.Spatial.SpatialEntity) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def CreateEntityWatcher(self) -> win32more.Windows.Perception.Spatial.SpatialEntityWatcher: ...
class ISpatialEntityStoreStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityStoreStatics'
    _iid_ = Guid('{6b4b389e-7c50-4e92-8a62-4d1d4b7ccd3e}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryGetForRemoteSystemSession(self, session: win32more.Windows.System.RemoteSystems.RemoteSystemSession) -> win32more.Windows.Perception.Spatial.SpatialEntityStore: ...
    IsSupported = property(get_IsSupported, None)
class ISpatialEntityUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityUpdatedEventArgs'
    _iid_ = Guid('{e5671766-627b-43cb-a49f-b3be6d47deed}')
    @winrt_commethod(6)
    def get_Entity(self) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class ISpatialEntityWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialEntityWatcher'
    _iid_ = Guid('{b3b85fa0-6d5e-4bbc-805d-5fe5b9ba1959}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Perception.Spatial.SpatialEntityWatcherStatus: ...
    @winrt_commethod(7)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Perception.Spatial.SpatialEntityAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Perception.Spatial.SpatialEntityUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Perception.Spatial.SpatialEntityRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Updated = event()
    Removed = event()
    EnumerationCompleted = event()
class ISpatialLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocation'
    _iid_ = Guid('{1d81d29d-24a1-37d5-8fa1-39b4f9ad67e2}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_Orientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(8)
    def get_AbsoluteLinearVelocity(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_AbsoluteLinearAcceleration(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(10)
    def get_AbsoluteAngularVelocity(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(11)
    def get_AbsoluteAngularAcceleration(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    AbsoluteAngularAcceleration = property(get_AbsoluteAngularAcceleration, None)
    AbsoluteAngularVelocity = property(get_AbsoluteAngularVelocity, None)
    AbsoluteLinearAcceleration = property(get_AbsoluteLinearAcceleration, None)
    AbsoluteLinearVelocity = property(get_AbsoluteLinearVelocity, None)
    Orientation = property(get_Orientation, None)
    Position = property(get_Position, None)
class ISpatialLocation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocation2'
    _iid_ = Guid('{117f2416-38a7-4a18-b404-ab8fabe1d78b}')
    @winrt_commethod(6)
    def get_AbsoluteAngularVelocityAxisAngle(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_AbsoluteAngularAccelerationAxisAngle(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    AbsoluteAngularAccelerationAxisAngle = property(get_AbsoluteAngularAccelerationAxisAngle, None)
    AbsoluteAngularVelocityAxisAngle = property(get_AbsoluteAngularVelocityAxisAngle, None)
class ISpatialLocator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocator'
    _iid_ = Guid('{f6478925-9e0c-3bb6-997e-b64ecca24cf4}')
    @winrt_commethod(6)
    def get_Locatability(self) -> win32more.Windows.Perception.Spatial.SpatialLocatability: ...
    @winrt_commethod(7)
    def add_LocatabilityChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialLocator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_LocatabilityChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PositionalTrackingDeactivating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialLocator, win32more.Windows.Perception.Spatial.SpatialLocatorPositionalTrackingDeactivatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PositionalTrackingDeactivating(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def TryLocateAtTimestamp(self, timestamp: win32more.Windows.Perception.PerceptionTimestamp, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.SpatialLocation: ...
    @winrt_commethod(12)
    def CreateAttachedFrameOfReferenceAtCurrentHeading(self) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(13)
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPosition(self, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(14)
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientation(self, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(15)
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientationAndRelativeHeading(self, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_commethod(16)
    def CreateStationaryFrameOfReferenceAtCurrentLocation(self) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_commethod(17)
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPosition(self, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_commethod(18)
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientation(self, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_commethod(19)
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientationAndRelativeHeading(self, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    Locatability = property(get_Locatability, None)
    LocatabilityChanged = event()
    PositionalTrackingDeactivating = event()
class ISpatialLocatorAttachedFrameOfReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference'
    _iid_ = Guid('{e1774ef6-1f4f-499c-9625-ef5e6ed7a048}')
    @winrt_commethod(6)
    def get_RelativePosition(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def put_RelativePosition(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(8)
    def get_RelativeOrientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(9)
    def put_RelativeOrientation(self, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(10)
    def AdjustHeading(self, headingOffsetInRadians: Double) -> Void: ...
    @winrt_commethod(11)
    def GetStationaryCoordinateSystemAtTimestamp(self, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(12)
    def TryGetRelativeHeadingAtTimestamp(self, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.Foundation.IReference[Double]: ...
    RelativeOrientation = property(get_RelativeOrientation, put_RelativeOrientation)
    RelativePosition = property(get_RelativePosition, put_RelativePosition)
class ISpatialLocatorPositionalTrackingDeactivatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs'
    _iid_ = Guid('{b8a84063-e3f4-368b-9061-9ea9d1d6cc16}')
    @winrt_commethod(6)
    def get_Canceled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Canceled(self, value: Boolean) -> Void: ...
    Canceled = property(get_Canceled, put_Canceled)
class ISpatialLocatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialLocatorStatics'
    _iid_ = Guid('{b76e3340-a7c2-361b-bb82-56e93b89b1bb}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...
class ISpatialStageFrameOfReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialStageFrameOfReference'
    _iid_ = Guid('{7a8a3464-ad0d-4590-ab86-33062b674926}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def get_MovementRange(self) -> win32more.Windows.Perception.Spatial.SpatialMovementRange: ...
    @winrt_commethod(8)
    def get_LookDirectionRange(self) -> win32more.Windows.Perception.Spatial.SpatialLookDirectionRange: ...
    @winrt_commethod(9)
    def GetCoordinateSystemAtCurrentLocation(self, locator: win32more.Windows.Perception.Spatial.SpatialLocator) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(10)
    def TryGetMovementBounds(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> ReceiveArray[win32more.Windows.Foundation.Numerics.Vector3]: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    LookDirectionRange = property(get_LookDirectionRange, None)
    MovementRange = property(get_MovementRange, None)
class ISpatialStageFrameOfReferenceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics'
    _iid_ = Guid('{f78d5c4d-a0a4-499c-8d91-a8c965d40654}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Perception.Spatial.SpatialStageFrameOfReference: ...
    @winrt_commethod(7)
    def add_CurrentChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CurrentChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def RequestNewStageAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialStageFrameOfReference]: ...
    Current = property(get_Current, None)
    CurrentChanged = event()
class ISpatialStationaryFrameOfReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.ISpatialStationaryFrameOfReference'
    _iid_ = Guid('{09dbccb9-bcf8-3e7f-be7e-7edccbb178a8}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
class SpatialAnchor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialAnchor
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchor'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.Spatial.ISpatialAnchor) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_RawCoordinateSystem(self: win32more.Windows.Perception.Spatial.ISpatialAnchor) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def add_RawCoordinateSystemAdjusted(self: win32more.Windows.Perception.Spatial.ISpatialAnchor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialAnchor, win32more.Windows.Perception.Spatial.SpatialAnchorRawCoordinateSystemAdjustedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RawCoordinateSystemAdjusted(self: win32more.Windows.Perception.Spatial.ISpatialAnchor, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_RemovedByUser(self: win32more.Windows.Perception.Spatial.ISpatialAnchor2) -> Boolean: ...
    @winrt_classmethod
    def TryCreateRelativeTo(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_classmethod
    def TryCreateWithPositionRelativeTo(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_classmethod
    def TryCreateWithPositionAndOrientationRelativeTo(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    RawCoordinateSystem = property(get_RawCoordinateSystem, None)
    RemovedByUser = property(get_RemovedByUser, None)
    RawCoordinateSystemAdjusted = event()
class SpatialAnchorExportPurpose(Enum, Int32):
    Relocalization = 0
    Sharing = 1
class SpatialAnchorExportSufficiency(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialAnchorExportSufficiency
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorExportSufficiency'
    @winrt_mixinmethod
    def get_IsMinimallySufficient(self: win32more.Windows.Perception.Spatial.ISpatialAnchorExportSufficiency) -> Boolean: ...
    @winrt_mixinmethod
    def get_SufficiencyLevel(self: win32more.Windows.Perception.Spatial.ISpatialAnchorExportSufficiency) -> Double: ...
    @winrt_mixinmethod
    def get_RecommendedSufficiencyLevel(self: win32more.Windows.Perception.Spatial.ISpatialAnchorExportSufficiency) -> Double: ...
    IsMinimallySufficient = property(get_IsMinimallySufficient, None)
    RecommendedSufficiencyLevel = property(get_RecommendedSufficiencyLevel, None)
    SufficiencyLevel = property(get_SufficiencyLevel, None)
class SpatialAnchorExporter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialAnchorExporter
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorExporter'
    @winrt_mixinmethod
    def GetAnchorExportSufficiencyAsync(self: win32more.Windows.Perception.Spatial.ISpatialAnchorExporter, anchor: win32more.Windows.Perception.Spatial.SpatialAnchor, purpose: win32more.Windows.Perception.Spatial.SpatialAnchorExportPurpose) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialAnchorExportSufficiency]: ...
    @winrt_mixinmethod
    def TryExportAnchorAsync(self: win32more.Windows.Perception.Spatial.ISpatialAnchorExporter, anchor: win32more.Windows.Perception.Spatial.SpatialAnchor, purpose: win32more.Windows.Perception.Spatial.SpatialAnchorExportPurpose, stream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorExporterStatics) -> win32more.Windows.Perception.Spatial.SpatialAnchorExporter: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorExporterStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class SpatialAnchorManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorManager'
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialAnchorStore]: ...
class SpatialAnchorRawCoordinateSystemAdjustedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialAnchorRawCoordinateSystemAdjustedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorRawCoordinateSystemAdjustedEventArgs'
    @winrt_mixinmethod
    def get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform(self: win32more.Windows.Perception.Spatial.ISpatialAnchorRawCoordinateSystemAdjustedEventArgs) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    OldRawCoordinateSystemToNewRawCoordinateSystemTransform = property(get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform, None)
class SpatialAnchorStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialAnchorStore
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorStore'
    @winrt_mixinmethod
    def GetAllSavedAnchors(self: win32more.Windows.Perception.Spatial.ISpatialAnchorStore) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Perception.Spatial.SpatialAnchor]: ...
    @winrt_mixinmethod
    def TrySave(self: win32more.Windows.Perception.Spatial.ISpatialAnchorStore, id: WinRT_String, anchor: win32more.Windows.Perception.Spatial.SpatialAnchor) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Perception.Spatial.ISpatialAnchorStore, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Perception.Spatial.ISpatialAnchorStore) -> Void: ...
class SpatialAnchorTransferManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.SpatialAnchorTransferManager'
    @winrt_classmethod
    def TryImportAnchorsAsync(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Perception.Spatial.SpatialAnchor]]: ...
    @winrt_classmethod
    def TryExportAnchorsAsync(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics, anchors: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Perception.Spatial.SpatialAnchor]], stream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Perception.Spatial.ISpatialAnchorTransferManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class SpatialBoundingBox(Structure):
    Center: win32more.Windows.Foundation.Numerics.Vector3
    Extents: win32more.Windows.Foundation.Numerics.Vector3
class SpatialBoundingFrustum(Structure):
    Near: win32more.Windows.Foundation.Numerics.Plane
    Far: win32more.Windows.Foundation.Numerics.Plane
    Right: win32more.Windows.Foundation.Numerics.Plane
    Left: win32more.Windows.Foundation.Numerics.Plane
    Top: win32more.Windows.Foundation.Numerics.Plane
    Bottom: win32more.Windows.Foundation.Numerics.Plane
class SpatialBoundingOrientedBox(Structure):
    Center: win32more.Windows.Foundation.Numerics.Vector3
    Extents: win32more.Windows.Foundation.Numerics.Vector3
    Orientation: win32more.Windows.Foundation.Numerics.Quaternion
class SpatialBoundingSphere(Structure):
    Center: win32more.Windows.Foundation.Numerics.Vector3
    Radius: Single
class SpatialBoundingVolume(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialBoundingVolume
    _classid_ = 'Windows.Perception.Spatial.SpatialBoundingVolume'
    @winrt_classmethod
    def FromBox(cls: win32more.Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, box: win32more.Windows.Perception.Spatial.SpatialBoundingBox) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_classmethod
    def FromOrientedBox(cls: win32more.Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, box: win32more.Windows.Perception.Spatial.SpatialBoundingOrientedBox) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_classmethod
    def FromSphere(cls: win32more.Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, sphere: win32more.Windows.Perception.Spatial.SpatialBoundingSphere) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
    @winrt_classmethod
    def FromFrustum(cls: win32more.Windows.Perception.Spatial.ISpatialBoundingVolumeStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, frustum: win32more.Windows.Perception.Spatial.SpatialBoundingFrustum) -> win32more.Windows.Perception.Spatial.SpatialBoundingVolume: ...
class SpatialCoordinateSystem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialCoordinateSystem
    _classid_ = 'Windows.Perception.Spatial.SpatialCoordinateSystem'
    @winrt_mixinmethod
    def TryGetTransformTo(self: win32more.Windows.Perception.Spatial.ISpatialCoordinateSystem, target: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Matrix4x4]: ...
class SpatialEntity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialEntity
    _classid_ = 'Windows.Perception.Spatial.SpatialEntity'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Perception.Spatial.SpatialEntity.CreateWithSpatialAnchor(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Perception.Spatial.SpatialEntity.CreateWithSpatialAnchorAndProperties(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithSpatialAnchor(cls: win32more.Windows.Perception.Spatial.ISpatialEntityFactory, spatialAnchor: win32more.Windows.Perception.Spatial.SpatialAnchor) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    @winrt_factorymethod
    def CreateWithSpatialAnchorAndProperties(cls: win32more.Windows.Perception.Spatial.ISpatialEntityFactory, spatialAnchor: win32more.Windows.Perception.Spatial.SpatialAnchor, propertySet: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Perception.Spatial.ISpatialEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Anchor(self: win32more.Windows.Perception.Spatial.ISpatialEntity) -> win32more.Windows.Perception.Spatial.SpatialAnchor: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Perception.Spatial.ISpatialEntity) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Anchor = property(get_Anchor, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class SpatialEntityAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialEntityAddedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityAddedEventArgs'
    @winrt_mixinmethod
    def get_Entity(self: win32more.Windows.Perception.Spatial.ISpatialEntityAddedEventArgs) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class SpatialEntityRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialEntityRemovedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityRemovedEventArgs'
    @winrt_mixinmethod
    def get_Entity(self: win32more.Windows.Perception.Spatial.ISpatialEntityRemovedEventArgs) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class _SpatialEntityStore_Meta_(ComPtr.__class__):
    pass
class SpatialEntityStore(ComPtr, metaclass=_SpatialEntityStore_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialEntityStore
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityStore'
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Perception.Spatial.ISpatialEntityStore, entity: win32more.Windows.Perception.Spatial.SpatialEntity) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveAsync(self: win32more.Windows.Perception.Spatial.ISpatialEntityStore, entity: win32more.Windows.Perception.Spatial.SpatialEntity) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateEntityWatcher(self: win32more.Windows.Perception.Spatial.ISpatialEntityStore) -> win32more.Windows.Perception.Spatial.SpatialEntityWatcher: ...
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Windows.Perception.Spatial.ISpatialEntityStoreStatics) -> Boolean: ...
    @winrt_classmethod
    def TryGetForRemoteSystemSession(cls: win32more.Windows.Perception.Spatial.ISpatialEntityStoreStatics, session: win32more.Windows.System.RemoteSystems.RemoteSystemSession) -> win32more.Windows.Perception.Spatial.SpatialEntityStore: ...
    _SpatialEntityStore_Meta_.IsSupported = property(get_IsSupported, None)
class SpatialEntityUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialEntityUpdatedEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Entity(self: win32more.Windows.Perception.Spatial.ISpatialEntityUpdatedEventArgs) -> win32more.Windows.Perception.Spatial.SpatialEntity: ...
    Entity = property(get_Entity, None)
class SpatialEntityWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher
    _classid_ = 'Windows.Perception.Spatial.SpatialEntityWatcher'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher) -> win32more.Windows.Perception.Spatial.SpatialEntityWatcherStatus: ...
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Perception.Spatial.SpatialEntityAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Perception.Spatial.SpatialEntityUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Perception.Spatial.SpatialEntityRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialEntityWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Perception.Spatial.ISpatialEntityWatcher) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Updated = event()
    Removed = event()
    EnumerationCompleted = event()
class SpatialEntityWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopping = 3
    Stopped = 4
    Aborted = 5
class SpatialLocatability(Enum, Int32):
    Unavailable = 0
    OrientationOnly = 1
    PositionalTrackingActivating = 2
    PositionalTrackingActive = 3
    PositionalTrackingInhibited = 4
class SpatialLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialLocation
    _classid_ = 'Windows.Perception.Spatial.SpatialLocation'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Perception.Spatial.ISpatialLocation) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Perception.Spatial.ISpatialLocation) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_AbsoluteLinearVelocity(self: win32more.Windows.Perception.Spatial.ISpatialLocation) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_AbsoluteLinearAcceleration(self: win32more.Windows.Perception.Spatial.ISpatialLocation) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularVelocity(self: win32more.Windows.Perception.Spatial.ISpatialLocation) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularAcceleration(self: win32more.Windows.Perception.Spatial.ISpatialLocation) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularVelocityAxisAngle(self: win32more.Windows.Perception.Spatial.ISpatialLocation2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_AbsoluteAngularAccelerationAxisAngle(self: win32more.Windows.Perception.Spatial.ISpatialLocation2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    AbsoluteAngularAcceleration = property(get_AbsoluteAngularAcceleration, None)
    AbsoluteAngularAccelerationAxisAngle = property(get_AbsoluteAngularAccelerationAxisAngle, None)
    AbsoluteAngularVelocity = property(get_AbsoluteAngularVelocity, None)
    AbsoluteAngularVelocityAxisAngle = property(get_AbsoluteAngularVelocityAxisAngle, None)
    AbsoluteLinearAcceleration = property(get_AbsoluteLinearAcceleration, None)
    AbsoluteLinearVelocity = property(get_AbsoluteLinearVelocity, None)
    Orientation = property(get_Orientation, None)
    Position = property(get_Position, None)
class SpatialLocator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialLocator
    _classid_ = 'Windows.Perception.Spatial.SpatialLocator'
    @winrt_mixinmethod
    def get_Locatability(self: win32more.Windows.Perception.Spatial.ISpatialLocator) -> win32more.Windows.Perception.Spatial.SpatialLocatability: ...
    @winrt_mixinmethod
    def add_LocatabilityChanged(self: win32more.Windows.Perception.Spatial.ISpatialLocator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialLocator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LocatabilityChanged(self: win32more.Windows.Perception.Spatial.ISpatialLocator, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PositionalTrackingDeactivating(self: win32more.Windows.Perception.Spatial.ISpatialLocator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.SpatialLocator, win32more.Windows.Perception.Spatial.SpatialLocatorPositionalTrackingDeactivatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PositionalTrackingDeactivating(self: win32more.Windows.Perception.Spatial.ISpatialLocator, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryLocateAtTimestamp(self: win32more.Windows.Perception.Spatial.ISpatialLocator, timestamp: win32more.Windows.Perception.PerceptionTimestamp, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.SpatialLocation: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeading(self: win32more.Windows.Perception.Spatial.ISpatialLocator) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPosition(self: win32more.Windows.Perception.Spatial.ISpatialLocator, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientation(self: win32more.Windows.Perception.Spatial.ISpatialLocator, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientationAndRelativeHeading(self: win32more.Windows.Perception.Spatial.ISpatialLocator, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> win32more.Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocation(self: win32more.Windows.Perception.Spatial.ISpatialLocator) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPosition(self: win32more.Windows.Perception.Spatial.ISpatialLocator, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientation(self: win32more.Windows.Perception.Spatial.ISpatialLocator, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_mixinmethod
    def CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientationAndRelativeHeading(self: win32more.Windows.Perception.Spatial.ISpatialLocator, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion, relativeHeadingInRadians: Double) -> win32more.Windows.Perception.Spatial.SpatialStationaryFrameOfReference: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Perception.Spatial.ISpatialLocatorStatics) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...
    Locatability = property(get_Locatability, None)
    LocatabilityChanged = event()
    PositionalTrackingDeactivating = event()
class SpatialLocatorAttachedFrameOfReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference
    _classid_ = 'Windows.Perception.Spatial.SpatialLocatorAttachedFrameOfReference'
    @winrt_mixinmethod
    def get_RelativePosition(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RelativePosition(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeOrientation(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_RelativeOrientation(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def AdjustHeading(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, headingOffsetInRadians: Double) -> Void: ...
    @winrt_mixinmethod
    def GetStationaryCoordinateSystemAtTimestamp(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def TryGetRelativeHeadingAtTimestamp(self: win32more.Windows.Perception.Spatial.ISpatialLocatorAttachedFrameOfReference, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.Foundation.IReference[Double]: ...
    RelativeOrientation = property(get_RelativeOrientation, put_RelativeOrientation)
    RelativePosition = property(get_RelativePosition, put_RelativePosition)
class SpatialLocatorPositionalTrackingDeactivatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs
    _classid_ = 'Windows.Perception.Spatial.SpatialLocatorPositionalTrackingDeactivatingEventArgs'
    @winrt_mixinmethod
    def get_Canceled(self: win32more.Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Canceled(self: win32more.Windows.Perception.Spatial.ISpatialLocatorPositionalTrackingDeactivatingEventArgs, value: Boolean) -> Void: ...
    Canceled = property(get_Canceled, put_Canceled)
class SpatialLookDirectionRange(Enum, Int32):
    ForwardOnly = 0
    Omnidirectional = 1
class SpatialMovementRange(Enum, Int32):
    NoMovement = 0
    Bounded = 1
class SpatialPerceptionAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    DeniedByUser = 2
    DeniedBySystem = 3
class SpatialRay(Structure):
    Origin: win32more.Windows.Foundation.Numerics.Vector3
    Direction: win32more.Windows.Foundation.Numerics.Vector3
class _SpatialStageFrameOfReference_Meta_(ComPtr.__class__):
    pass
class SpatialStageFrameOfReference(ComPtr, metaclass=_SpatialStageFrameOfReference_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReference
    _classid_ = 'Windows.Perception.Spatial.SpatialStageFrameOfReference'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReference) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_MovementRange(self: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReference) -> win32more.Windows.Perception.Spatial.SpatialMovementRange: ...
    @winrt_mixinmethod
    def get_LookDirectionRange(self: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReference) -> win32more.Windows.Perception.Spatial.SpatialLookDirectionRange: ...
    @winrt_mixinmethod
    def GetCoordinateSystemAtCurrentLocation(self: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReference, locator: win32more.Windows.Perception.Spatial.SpatialLocator) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def TryGetMovementBounds(self: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReference, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> ReceiveArray[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics) -> win32more.Windows.Perception.Spatial.SpatialStageFrameOfReference: ...
    @winrt_classmethod
    def add_CurrentChanged(cls: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CurrentChanged(cls: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestNewStageAsync(cls: win32more.Windows.Perception.Spatial.ISpatialStageFrameOfReferenceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialStageFrameOfReference]: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    LookDirectionRange = property(get_LookDirectionRange, None)
    MovementRange = property(get_MovementRange, None)
    _SpatialStageFrameOfReference_Meta_.Current = property(get_Current, None)
class SpatialStationaryFrameOfReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.ISpatialStationaryFrameOfReference
    _classid_ = 'Windows.Perception.Spatial.SpatialStationaryFrameOfReference'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.Spatial.ISpatialStationaryFrameOfReference) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    CoordinateSystem = property(get_CoordinateSystem, None)


make_ready(__name__)
