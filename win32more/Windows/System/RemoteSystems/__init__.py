from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.AppService
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Security.Credentials
import win32more.Windows.System
import win32more.Windows.System.RemoteSystems
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IKnownRemoteSystemCapabilitiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics'
    _iid_ = Guid('{8108e380-7f8a-44e4-92cd-03b6469b94a3}')
    @winrt_commethod(6)
    def get_AppService(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LaunchUri(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteSession(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SpatialEntity(self) -> WinRT_String: ...
    AppService = property(get_AppService, None)
    LaunchUri = property(get_LaunchUri, None)
    RemoteSession = property(get_RemoteSession, None)
    SpatialEntity = property(get_SpatialEntity, None)
class IRemoteSystem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystem'
    _iid_ = Guid('{ed5838cd-1e10-4a8c-b4a6-4e5fd6f97721}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Status(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemStatus: ...
    @winrt_commethod(10)
    def get_IsAvailableByProximity(self) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    Status = property(get_Status, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
class IRemoteSystem2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystem2'
    _iid_ = Guid('{09dfe4ec-fb8b-4a08-a758-6876435d769e}')
    @winrt_commethod(6)
    def get_IsAvailableBySpatialProximity(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetCapabilitySupportedAsync(self, capabilityName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
class IRemoteSystem3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystem3'
    _iid_ = Guid('{72b4b495-b7c6-40be-831b-73562f12ffa8}')
    @winrt_commethod(6)
    def get_ManufacturerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ModelDisplayName(self) -> WinRT_String: ...
    ManufacturerDisplayName = property(get_ManufacturerDisplayName, None)
    ModelDisplayName = property(get_ModelDisplayName, None)
class IRemoteSystem4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystem4'
    _iid_ = Guid('{f164ffe5-b987-4ca5-9926-fa0438be6273}')
    @winrt_commethod(6)
    def get_Platform(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemPlatform: ...
    Platform = property(get_Platform, None)
class IRemoteSystem5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystem5'
    _iid_ = Guid('{eb2ad723-e5e2-4ae2-a7a7-a1097a098e90}')
    @winrt_commethod(6)
    def get_Apps(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.RemoteSystems.RemoteSystemApp]: ...
    Apps = property(get_Apps, None)
class IRemoteSystem6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystem6'
    _iid_ = Guid('{d4cda942-c027-533e-9384-3a19b4f7eef3}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IRemoteSystemAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemAddedEventArgs'
    _iid_ = Guid('{8f39560f-e534-4697-8836-7abea151516e}')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemApp'
    _iid_ = Guid('{80e5bcbd-d54d-41b1-9b16-6810a871ed4f}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsAvailableByProximity(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsAvailableBySpatialProximity(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Attributes(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
    Attributes = property(get_Attributes, None)
class IRemoteSystemApp2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemApp2'
    _iid_ = Guid('{6369bf15-0a96-577a-8ff6-c35904dfa8f3}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def get_ConnectionToken(self) -> WinRT_String: ...
    User = property(get_User, None)
    ConnectionToken = property(get_ConnectionToken, None)
class IRemoteSystemAppRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemAppRegistration'
    _iid_ = Guid('{b47947b5-7035-4a5a-b8df-962d8f8431f4}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def get_Attributes(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(8)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    User = property(get_User, None)
    Attributes = property(get_Attributes, None)
class IRemoteSystemAppRegistrationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemAppRegistrationStatics'
    _iid_ = Guid('{01b99840-cfd2-453f-ae25-c2539f086afd}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
class IRemoteSystemAuthorizationKindFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilter'
    _iid_ = Guid('{6b0dde8e-04d0-40f4-a27f-c2acbbd6b734}')
    @winrt_commethod(6)
    def get_RemoteSystemAuthorizationKind(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind: ...
    RemoteSystemAuthorizationKind = property(get_RemoteSystemAuthorizationKind, None)
class IRemoteSystemAuthorizationKindFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilterFactory'
    _iid_ = Guid('{ad65df4d-b66a-45a4-8177-8caed75d9e5a}')
    @winrt_commethod(6)
    def Create(self, remoteSystemAuthorizationKind: win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKindFilter: ...
class IRemoteSystemConnectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionInfo'
    _iid_ = Guid('{23278bc3-0d09-52cb-9c6a-eed2940bee43}')
    @winrt_commethod(6)
    def get_IsProximal(self) -> Boolean: ...
    IsProximal = property(get_IsProximal, None)
class IRemoteSystemConnectionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionInfoStatics'
    _iid_ = Guid('{ac831e2d-66c5-56d7-a4ce-705d94925ad6}')
    @winrt_commethod(6)
    def TryCreateFromAppServiceConnection(self, connection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionInfo: ...
class IRemoteSystemConnectionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionRequest'
    _iid_ = Guid('{84ed4104-8d5e-4d72-8238-7621576c7a67}')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemConnectionRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionRequest2'
    _iid_ = Guid('{12df6d6f-bffc-483a-8abe-d34a6c19f92b}')
    @winrt_commethod(6)
    def get_RemoteSystemApp(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemApp: ...
    RemoteSystemApp = property(get_RemoteSystemApp, None)
class IRemoteSystemConnectionRequest3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionRequest3'
    _iid_ = Guid('{de86c3e7-c9cc-5a50-b8d9-ba7b34bb8d0e}')
    @winrt_commethod(6)
    def get_ConnectionToken(self) -> WinRT_String: ...
    ConnectionToken = property(get_ConnectionToken, None)
class IRemoteSystemConnectionRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionRequestFactory'
    _iid_ = Guid('{aa0a0a20-baeb-4575-b530-810bb9786334}')
    @winrt_commethod(6)
    def Create(self, remoteSystem: win32more.Windows.System.RemoteSystems.RemoteSystem) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
class IRemoteSystemConnectionRequestStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics'
    _iid_ = Guid('{86ca143d-8214-425c-8932-db49032d1306}')
    @winrt_commethod(6)
    def CreateForApp(self, remoteSystemApp: win32more.Windows.System.RemoteSystems.RemoteSystemApp) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
class IRemoteSystemConnectionRequestStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics2'
    _iid_ = Guid('{460f1027-64ec-598e-a800-4f2ee58def19}')
    @winrt_commethod(6)
    def CreateFromConnectionToken(self, connectionToken: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_commethod(7)
    def CreateFromConnectionTokenForUser(self, user: win32more.Windows.System.User, connectionToken: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
class IRemoteSystemDiscoveryTypeFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilter'
    _iid_ = Guid('{42d9041f-ee5a-43da-ac6a-6fee25460741}')
    @winrt_commethod(6)
    def get_RemoteSystemDiscoveryType(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemDiscoveryType: ...
    RemoteSystemDiscoveryType = property(get_RemoteSystemDiscoveryType, None)
class IRemoteSystemDiscoveryTypeFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilterFactory'
    _iid_ = Guid('{9f9eb993-c260-4161-92f2-9c021f23fe5d}')
    @winrt_commethod(6)
    def Create(self, discoveryType: win32more.Windows.System.RemoteSystems.RemoteSystemDiscoveryType) -> win32more.Windows.System.RemoteSystems.RemoteSystemDiscoveryTypeFilter: ...
class IRemoteSystemEnumerationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemEnumerationCompletedEventArgs'
    _iid_ = Guid('{c6e83d5f-4030-4354-a060-14f1b22c545d}')
class IRemoteSystemFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemFilter'
    _iid_ = Guid('{4a3ba9e4-99eb-45eb-ba16-0367728ff374}')
class IRemoteSystemKindFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemKindFilter'
    _iid_ = Guid('{38e1c9ec-22c3-4ef6-901a-bbb1c7aad4ed}')
    @winrt_commethod(6)
    def get_RemoteSystemKinds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    RemoteSystemKinds = property(get_RemoteSystemKinds, None)
class IRemoteSystemKindFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemKindFilterFactory'
    _iid_ = Guid('{a1fb18ee-99ea-40bc-9a39-c670aa804a28}')
    @winrt_commethod(6)
    def Create(self, remoteSystemKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.System.RemoteSystems.RemoteSystemKindFilter: ...
class IRemoteSystemKindStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemKindStatics'
    _iid_ = Guid('{f6317633-ab14-41d0-9553-796aadb882db}')
    @winrt_commethod(6)
    def get_Phone(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Hub(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Holographic(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Desktop(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Xbox(self) -> WinRT_String: ...
    Phone = property(get_Phone, None)
    Hub = property(get_Hub, None)
    Holographic = property(get_Holographic, None)
    Desktop = property(get_Desktop, None)
    Xbox = property(get_Xbox, None)
class IRemoteSystemKindStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemKindStatics2'
    _iid_ = Guid('{b9e3a3d0-0466-4749-91e8-65f9d19a96a5}')
    @winrt_commethod(6)
    def get_Iot(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Tablet(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Laptop(self) -> WinRT_String: ...
    Iot = property(get_Iot, None)
    Tablet = property(get_Tablet, None)
    Laptop = property(get_Laptop, None)
class IRemoteSystemRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemRemovedEventArgs'
    _iid_ = Guid('{8b3d16bb-7306-49ea-b7df-67d5714cb013}')
    @winrt_commethod(6)
    def get_RemoteSystemId(self) -> WinRT_String: ...
    RemoteSystemId = property(get_RemoteSystemId, None)
class IRemoteSystemSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSession'
    _iid_ = Guid('{69476a01-9ada-490f-9549-d31cb14c9e95}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ControllerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def add_Disconnected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSession, win32more.Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Disconnected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CreateParticipantWatcher(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher: ...
    @winrt_commethod(12)
    def SendInvitationAsync(self, invitee: win32more.Windows.System.RemoteSystems.RemoteSystem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class IRemoteSystemSessionAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionAddedEventArgs'
    _iid_ = Guid('{d585d754-bc97-4c39-99b4-beca76e04c3f}')
    @winrt_commethod(6)
    def get_SessionInfo(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionController'
    _iid_ = Guid('{e48b2dd2-6820-4867-b425-d89c0a3ef7ba}')
    @winrt_commethod(6)
    def add_JoinRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionController, win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_JoinRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def RemoveParticipantAsync(self, pParticipant: win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def CreateSessionAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystemSessionCreationResult]: ...
class IRemoteSystemSessionControllerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionControllerFactory'
    _iid_ = Guid('{bfcc2f6b-ac3d-4199-82cd-6670a773ef2e}')
    @winrt_commethod(6)
    def CreateController(self, displayName: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionController: ...
    @winrt_commethod(7)
    def CreateControllerWithSessionOptions(self, displayName: WinRT_String, options: win32more.Windows.System.RemoteSystems.RemoteSystemSessionOptions) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionController: ...
class IRemoteSystemSessionCreationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionCreationResult'
    _iid_ = Guid('{a79812c2-37de-448c-8b83-a30aa3c4ead6}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionCreationStatus: ...
    @winrt_commethod(7)
    def get_Session(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
class IRemoteSystemSessionDisconnectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionDisconnectedEventArgs'
    _iid_ = Guid('{de0bc69b-77c5-461c-8209-7c6c5d3111ab}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedReason: ...
    Reason = property(get_Reason, None)
class IRemoteSystemSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionInfo'
    _iid_ = Guid('{ff4df648-8b0a-4e9a-9905-69e4b841c588}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ControllerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def JoinAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinResult]: ...
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class IRemoteSystemSessionInvitation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionInvitation'
    _iid_ = Guid('{3e32cc91-51d7-4766-a121-25516c3b8294}')
    @winrt_commethod(6)
    def get_Sender(self) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_commethod(7)
    def get_SessionInfo(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    Sender = property(get_Sender, None)
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionInvitationListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionInvitationListener'
    _iid_ = Guid('{08f4003f-bc71-49e1-874a-31ddff9a27b9}')
    @winrt_commethod(6)
    def add_InvitationReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener, win32more.Windows.System.RemoteSystems.RemoteSystemSessionInvitationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_InvitationReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRemoteSystemSessionInvitationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionInvitationReceivedEventArgs'
    _iid_ = Guid('{5e964a2d-a10d-4edb-8dea-54d20ac19543}')
    @winrt_commethod(6)
    def get_Invitation(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInvitation: ...
    Invitation = property(get_Invitation, None)
class IRemoteSystemSessionJoinRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequest'
    _iid_ = Guid('{20600068-7994-4331-86d1-d89d882585ee}')
    @winrt_commethod(6)
    def get_Participant(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_commethod(7)
    def Accept(self) -> Void: ...
    Participant = property(get_Participant, None)
class IRemoteSystemSessionJoinRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequestedEventArgs'
    _iid_ = Guid('{dbca4fc3-82b9-4816-9c24-e40e61774bd8}')
    @winrt_commethod(6)
    def get_JoinRequest(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    JoinRequest = property(get_JoinRequest, None)
class IRemoteSystemSessionJoinResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionJoinResult'
    _iid_ = Guid('{ce7b1f04-a03e-41a4-900b-1e79328c1267}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinStatus: ...
    @winrt_commethod(7)
    def get_Session(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
class IRemoteSystemSessionMessageChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel'
    _iid_ = Guid('{9524d12a-73d9-4c10-b751-c26784437127}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSession: ...
    @winrt_commethod(7)
    def BroadcastValueSetAsync(self, messageData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def SendValueSetAsync(self, messageData: win32more.Windows.Foundation.Collections.ValueSet, participant: win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def SendValueSetToParticipantsAsync(self, messageData: win32more.Windows.Foundation.Collections.ValueSet, participants: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def add_ValueSetReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel, win32more.Windows.System.RemoteSystems.RemoteSystemSessionValueSetReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ValueSetReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
class IRemoteSystemSessionMessageChannelFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannelFactory'
    _iid_ = Guid('{295e1c4a-bd16-4298-b7ce-415482b0e11d}')
    @winrt_commethod(6)
    def Create(self, session: win32more.Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
    @winrt_commethod(7)
    def CreateWithReliability(self, session: win32more.Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String, reliability: win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannelReliability) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
class IRemoteSystemSessionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionOptions'
    _iid_ = Guid('{740ed755-8418-4f01-9353-e21c9ecc6cfc}')
    @winrt_commethod(6)
    def get_IsInviteOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsInviteOnly(self, value: Boolean) -> Void: ...
    IsInviteOnly = property(get_IsInviteOnly, put_IsInviteOnly)
class IRemoteSystemSessionParticipant(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionParticipant'
    _iid_ = Guid('{7e90058c-acf9-4729-8a17-44e7baed5dcc}')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_commethod(7)
    def GetHostNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemSessionParticipantAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionParticipantAddedEventArgs'
    _iid_ = Guid('{d35a57d8-c9a1-4bb7-b6b0-79bb91adf93d}')
    @winrt_commethod(6)
    def get_Participant(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class IRemoteSystemSessionParticipantRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionParticipantRemovedEventArgs'
    _iid_ = Guid('{866ef088-de68-4abf-88a1-f90d16274192}')
    @winrt_commethod(6)
    def get_Participant(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class IRemoteSystemSessionParticipantWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher'
    _iid_ = Guid('{dcdd02cc-aa87-4d79-b6cc-4459b3e92075}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcherStatus: ...
    @winrt_commethod(9)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IRemoteSystemSessionRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionRemovedEventArgs'
    _iid_ = Guid('{af82914e-39a1-4dea-9d63-43798d5bbbd0}')
    @winrt_commethod(6)
    def get_SessionInfo(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionStatics'
    _iid_ = Guid('{8524899f-fd20-44e3-9565-e75a3b14c66e}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher: ...
class IRemoteSystemSessionUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionUpdatedEventArgs'
    _iid_ = Guid('{16875069-231e-4c91-8ec8-b3a39d9e55a3}')
    @winrt_commethod(6)
    def get_SessionInfo(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionValueSetReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionValueSetReceivedEventArgs'
    _iid_ = Guid('{06f31785-2da5-4e58-a78f-9e8d0784ee25}')
    @winrt_commethod(6)
    def get_Sender(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_commethod(7)
    def get_Message(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Sender = property(get_Sender, None)
    Message = property(get_Message, None)
class IRemoteSystemSessionWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemSessionWatcher'
    _iid_ = Guid('{8003e340-0c41-4a62-b6d7-bdbe2b19be2d}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcherStatus: ...
    @winrt_commethod(9)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IRemoteSystemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemStatics'
    _iid_ = Guid('{a485b392-ff2b-4b47-be62-743f2f140f30}')
    @winrt_commethod(6)
    def FindByHostNameAsync(self, hostName: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystem]: ...
    @winrt_commethod(7)
    def CreateWatcher(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_commethod(8)
    def CreateWatcherWithFilters(self, filters: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.RemoteSystems.IRemoteSystemFilter]) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystemAccessStatus]: ...
class IRemoteSystemStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemStatics2'
    _iid_ = Guid('{0c98edca-6f99-4c52-a272-ea4f36471744}')
    @winrt_commethod(6)
    def IsAuthorizationKindEnabled(self, kind: win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> Boolean: ...
class IRemoteSystemStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemStatics3'
    _iid_ = Guid('{9995f16f-0b3c-5ac5-b325-cc73f437dfcd}')
    @winrt_commethod(6)
    def CreateWatcherForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_commethod(7)
    def CreateWatcherWithFiltersForUser(self, user: win32more.Windows.System.User, filters: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.RemoteSystems.IRemoteSystemFilter]) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
class IRemoteSystemStatusTypeFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilter'
    _iid_ = Guid('{0c39514e-cbb6-4777-8534-2e0c521affa2}')
    @winrt_commethod(6)
    def get_RemoteSystemStatusType(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemStatusType: ...
    RemoteSystemStatusType = property(get_RemoteSystemStatusType, None)
class IRemoteSystemStatusTypeFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilterFactory'
    _iid_ = Guid('{33cf78fa-d724-4125-ac7a-8d281e44c949}')
    @winrt_commethod(6)
    def Create(self, remoteSystemStatusType: win32more.Windows.System.RemoteSystems.RemoteSystemStatusType) -> win32more.Windows.System.RemoteSystems.RemoteSystemStatusTypeFilter: ...
class IRemoteSystemUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemUpdatedEventArgs'
    _iid_ = Guid('{7502ff0e-dbcb-4155-b4ca-b30a04f27627}')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemWatcher'
    _iid_ = Guid('{5d600c7e-2c07-48c5-889c-455d2b099771}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def add_RemoteSystemAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RemoteSystemAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_RemoteSystemUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_RemoteSystemUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_RemoteSystemRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RemoteSystemRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRemoteSystemWatcher2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemWatcher2'
    _iid_ = Guid('{73436700-19ca-48f9-a4cd-780f7ad58c71}')
    @winrt_commethod(6)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemEnumerationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ErrorOccurred(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemWatcherErrorOccurredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ErrorOccurred(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRemoteSystemWatcher3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemWatcher3'
    _iid_ = Guid('{f79c0fcf-a913-55d3-8413-418fcf15ba54}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IRemoteSystemWatcherErrorOccurredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemWatcherErrorOccurredEventArgs'
    _iid_ = Guid('{74c5c6af-5114-4426-9216-20d81f8519ae}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcherError: ...
    Error = property(get_Error, None)
class IRemoteSystemWebAccountFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemWebAccountFilter'
    _iid_ = Guid('{3fb75873-87c8-5d8f-977e-f69f96d67238}')
    @winrt_commethod(6)
    def get_Account(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
class IRemoteSystemWebAccountFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.IRemoteSystemWebAccountFilterFactory'
    _iid_ = Guid('{348a2709-5f4d-5127-b4a7-bf99d5252b1b}')
    @winrt_commethod(6)
    def Create(self, account: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.System.RemoteSystems.RemoteSystemWebAccountFilter: ...
class _KnownRemoteSystemCapabilities_Meta_(ComPtr.__class__):
    pass
class KnownRemoteSystemCapabilities(ComPtr, metaclass=_KnownRemoteSystemCapabilities_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.KnownRemoteSystemCapabilities'
    @winrt_classmethod
    def get_AppService(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_LaunchUri(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RemoteSession(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SpatialEntity(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    _KnownRemoteSystemCapabilities_Meta_.AppService = property(get_AppService.__wrapped__, None)
    _KnownRemoteSystemCapabilities_Meta_.LaunchUri = property(get_LaunchUri.__wrapped__, None)
    _KnownRemoteSystemCapabilities_Meta_.RemoteSession = property(get_RemoteSession.__wrapped__, None)
    _KnownRemoteSystemCapabilities_Meta_.SpatialEntity = property(get_SpatialEntity.__wrapped__, None)
class RemoteSystem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystem
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystem'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.RemoteSystems.IRemoteSystem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.System.RemoteSystems.IRemoteSystem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.RemoteSystems.IRemoteSystem) -> win32more.Windows.System.RemoteSystems.RemoteSystemStatus: ...
    @winrt_mixinmethod
    def get_IsAvailableByProximity(self: win32more.Windows.System.RemoteSystems.IRemoteSystem) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAvailableBySpatialProximity(self: win32more.Windows.System.RemoteSystems.IRemoteSystem2) -> Boolean: ...
    @winrt_mixinmethod
    def GetCapabilitySupportedAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystem2, capabilityName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ManufacturerDisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystem3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelDisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystem3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Platform(self: win32more.Windows.System.RemoteSystems.IRemoteSystem4) -> win32more.Windows.System.RemoteSystems.RemoteSystemPlatform: ...
    @winrt_mixinmethod
    def get_Apps(self: win32more.Windows.System.RemoteSystems.IRemoteSystem5) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.RemoteSystems.RemoteSystemApp]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.RemoteSystems.IRemoteSystem6) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def CreateWatcherForUser(cls: Windows.System.RemoteSystems.IRemoteSystemStatics3, user: win32more.Windows.System.User) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def CreateWatcherWithFiltersForUser(cls: Windows.System.RemoteSystems.IRemoteSystemStatics3, user: win32more.Windows.System.User, filters: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.RemoteSystems.IRemoteSystemFilter]) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def IsAuthorizationKindEnabled(cls: Windows.System.RemoteSystems.IRemoteSystemStatics2, kind: win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> Boolean: ...
    @winrt_classmethod
    def FindByHostNameAsync(cls: Windows.System.RemoteSystems.IRemoteSystemStatics, hostName: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystem]: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.System.RemoteSystems.IRemoteSystemStatics) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def CreateWatcherWithFilters(cls: Windows.System.RemoteSystems.IRemoteSystemStatics, filters: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.RemoteSystems.IRemoteSystemFilter]) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.System.RemoteSystems.IRemoteSystemStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystemAccessStatus]: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    Status = property(get_Status, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
    ManufacturerDisplayName = property(get_ManufacturerDisplayName, None)
    ModelDisplayName = property(get_ModelDisplayName, None)
    Platform = property(get_Platform, None)
    Apps = property(get_Apps, None)
    User = property(get_User, None)
RemoteSystemAccessStatus = Int32
RemoteSystemAccessStatus_Unspecified: RemoteSystemAccessStatus = 0
RemoteSystemAccessStatus_Allowed: RemoteSystemAccessStatus = 1
RemoteSystemAccessStatus_DeniedByUser: RemoteSystemAccessStatus = 2
RemoteSystemAccessStatus_DeniedBySystem: RemoteSystemAccessStatus = 3
class RemoteSystemAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemAddedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemAddedEventArgs'
    @winrt_mixinmethod
    def get_RemoteSystem(self: win32more.Windows.System.RemoteSystems.IRemoteSystemAddedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class RemoteSystemApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemApp
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemApp'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsAvailableByProximity(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAvailableBySpatialProximity(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp) -> Boolean: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp2) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ConnectionToken(self: win32more.Windows.System.RemoteSystems.IRemoteSystemApp2) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
    Attributes = property(get_Attributes, None)
    User = property(get_User, None)
    ConnectionToken = property(get_ConnectionToken, None)
class RemoteSystemAppRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemAppRegistration
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemAppRegistration'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.RemoteSystems.IRemoteSystemAppRegistration) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.System.RemoteSystems.IRemoteSystemAppRegistration) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemAppRegistration) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.RemoteSystems.IRemoteSystemAppRegistrationStatics) -> win32more.Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.System.RemoteSystems.IRemoteSystemAppRegistrationStatics, user: win32more.Windows.System.User) -> win32more.Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
    User = property(get_User, None)
    Attributes = property(get_Attributes, None)
RemoteSystemAuthorizationKind = Int32
RemoteSystemAuthorizationKind_SameUser: RemoteSystemAuthorizationKind = 0
RemoteSystemAuthorizationKind_Anonymous: RemoteSystemAuthorizationKind = 1
class RemoteSystemAuthorizationKindFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilter
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemAuthorizationKindFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilterFactory, remoteSystemAuthorizationKind: win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKindFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemAuthorizationKind(self: win32more.Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilter) -> win32more.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind: ...
    RemoteSystemAuthorizationKind = property(get_RemoteSystemAuthorizationKind, None)
class RemoteSystemConnectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemConnectionInfo
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemConnectionInfo'
    @winrt_mixinmethod
    def get_IsProximal(self: win32more.Windows.System.RemoteSystems.IRemoteSystemConnectionInfo) -> Boolean: ...
    @winrt_classmethod
    def TryCreateFromAppServiceConnection(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionInfoStatics, connection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionInfo: ...
    IsProximal = property(get_IsProximal, None)
class RemoteSystemConnectionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemConnectionRequest
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemConnectionRequest'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestFactory, remoteSystem: win32more.Windows.System.RemoteSystems.RemoteSystem) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_mixinmethod
    def get_RemoteSystem(self: win32more.Windows.System.RemoteSystems.IRemoteSystemConnectionRequest) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_mixinmethod
    def get_RemoteSystemApp(self: win32more.Windows.System.RemoteSystems.IRemoteSystemConnectionRequest2) -> win32more.Windows.System.RemoteSystems.RemoteSystemApp: ...
    @winrt_mixinmethod
    def get_ConnectionToken(self: win32more.Windows.System.RemoteSystems.IRemoteSystemConnectionRequest3) -> WinRT_String: ...
    @winrt_classmethod
    def CreateFromConnectionToken(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics2, connectionToken: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_classmethod
    def CreateFromConnectionTokenForUser(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics2, user: win32more.Windows.System.User, connectionToken: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_classmethod
    def CreateForApp(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics, remoteSystemApp: win32more.Windows.System.RemoteSystems.RemoteSystemApp) -> win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    RemoteSystem = property(get_RemoteSystem, None)
    RemoteSystemApp = property(get_RemoteSystemApp, None)
    ConnectionToken = property(get_ConnectionToken, None)
RemoteSystemDiscoveryType = Int32
RemoteSystemDiscoveryType_Any: RemoteSystemDiscoveryType = 0
RemoteSystemDiscoveryType_Proximal: RemoteSystemDiscoveryType = 1
RemoteSystemDiscoveryType_Cloud: RemoteSystemDiscoveryType = 2
RemoteSystemDiscoveryType_SpatiallyProximal: RemoteSystemDiscoveryType = 3
class RemoteSystemDiscoveryTypeFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilter
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemDiscoveryTypeFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilterFactory, discoveryType: win32more.Windows.System.RemoteSystems.RemoteSystemDiscoveryType) -> win32more.Windows.System.RemoteSystems.RemoteSystemDiscoveryTypeFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemDiscoveryType(self: win32more.Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilter) -> win32more.Windows.System.RemoteSystems.RemoteSystemDiscoveryType: ...
    RemoteSystemDiscoveryType = property(get_RemoteSystemDiscoveryType, None)
class RemoteSystemEnumerationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemEnumerationCompletedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemEnumerationCompletedEventArgs'
class RemoteSystemKindFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemKindFilter
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemKindFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemKindFilterFactory, remoteSystemKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.System.RemoteSystems.RemoteSystemKindFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemKinds(self: win32more.Windows.System.RemoteSystems.IRemoteSystemKindFilter) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    RemoteSystemKinds = property(get_RemoteSystemKinds, None)
class _RemoteSystemKinds_Meta_(ComPtr.__class__):
    pass
class RemoteSystemKinds(ComPtr, metaclass=_RemoteSystemKinds_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemKinds'
    @winrt_classmethod
    def get_Iot(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Tablet(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Laptop(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Phone(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Hub(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Holographic(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Desktop(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Xbox(cls: Windows.System.RemoteSystems.IRemoteSystemKindStatics) -> WinRT_String: ...
    _RemoteSystemKinds_Meta_.Iot = property(get_Iot.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Tablet = property(get_Tablet.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Laptop = property(get_Laptop.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Phone = property(get_Phone.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Hub = property(get_Hub.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Holographic = property(get_Holographic.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Desktop = property(get_Desktop.__wrapped__, None)
    _RemoteSystemKinds_Meta_.Xbox = property(get_Xbox.__wrapped__, None)
RemoteSystemPlatform = Int32
RemoteSystemPlatform_Unknown: RemoteSystemPlatform = 0
RemoteSystemPlatform_Windows: RemoteSystemPlatform = 1
RemoteSystemPlatform_Android: RemoteSystemPlatform = 2
RemoteSystemPlatform_Ios: RemoteSystemPlatform = 3
RemoteSystemPlatform_Linux: RemoteSystemPlatform = 4
class RemoteSystemRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemRemovedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemRemovedEventArgs'
    @winrt_mixinmethod
    def get_RemoteSystemId(self: win32more.Windows.System.RemoteSystems.IRemoteSystemRemovedEventArgs) -> WinRT_String: ...
    RemoteSystemId = property(get_RemoteSystemId, None)
class RemoteSystemSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSession
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSession'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ControllerDisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_Disconnected(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSession, win32more.Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disconnected(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateParticipantWatcher(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher: ...
    @winrt_mixinmethod
    def SendInvitationAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSession, invitee: win32more.Windows.System.RemoteSystems.RemoteSystem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.System.RemoteSystems.IRemoteSystemSessionStatics) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class RemoteSystemSessionAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionAddedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionAddedEventArgs'
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionAddedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionController
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionController'
    @winrt_factorymethod
    def CreateController(cls: Windows.System.RemoteSystems.IRemoteSystemSessionControllerFactory, displayName: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionController: ...
    @winrt_factorymethod
    def CreateController(cls: Windows.System.RemoteSystems.IRemoteSystemSessionControllerFactory, displayName: WinRT_String, options: win32more.Windows.System.RemoteSystems.RemoteSystemSessionOptions) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionController: ...
    @winrt_mixinmethod
    def add_JoinRequested(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionController, win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_JoinRequested(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RemoveParticipantAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionController, pParticipant: win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def CreateSessionAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionController) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystemSessionCreationResult]: ...
class RemoteSystemSessionCreationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionCreationResult
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionCreationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionCreationResult) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionCreationStatus: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionCreationResult) -> win32more.Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
RemoteSystemSessionCreationStatus = Int32
RemoteSystemSessionCreationStatus_Success: RemoteSystemSessionCreationStatus = 0
RemoteSystemSessionCreationStatus_SessionLimitsExceeded: RemoteSystemSessionCreationStatus = 1
RemoteSystemSessionCreationStatus_OperationAborted: RemoteSystemSessionCreationStatus = 2
class RemoteSystemSessionDisconnectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionDisconnectedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionDisconnectedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedReason: ...
    Reason = property(get_Reason, None)
RemoteSystemSessionDisconnectedReason = Int32
RemoteSystemSessionDisconnectedReason_SessionUnavailable: RemoteSystemSessionDisconnectedReason = 0
RemoteSystemSessionDisconnectedReason_RemovedByController: RemoteSystemSessionDisconnectedReason = 1
RemoteSystemSessionDisconnectedReason_SessionClosed: RemoteSystemSessionDisconnectedReason = 2
class RemoteSystemSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInfo
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ControllerDisplayName(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def JoinAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinResult]: ...
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class RemoteSystemSessionInvitation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitation
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionInvitation'
    @winrt_mixinmethod
    def get_Sender(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitation) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitation) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    Sender = property(get_Sender, None)
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionInvitationListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitationListener
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener: ...
    @winrt_mixinmethod
    def add_InvitationReceived(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitationListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener, win32more.Windows.System.RemoteSystems.RemoteSystemSessionInvitationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InvitationReceived(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitationListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class RemoteSystemSessionInvitationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitationReceivedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionInvitationReceivedEventArgs'
    @winrt_mixinmethod
    def get_Invitation(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionInvitationReceivedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInvitation: ...
    Invitation = property(get_Invitation, None)
class RemoteSystemSessionJoinRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequest
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionJoinRequest'
    @winrt_mixinmethod
    def get_Participant(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequest) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_mixinmethod
    def Accept(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequest) -> Void: ...
    Participant = property(get_Participant, None)
class RemoteSystemSessionJoinRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequestedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionJoinRequestedEventArgs'
    @winrt_mixinmethod
    def get_JoinRequest(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequestedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    JoinRequest = property(get_JoinRequest, None)
class RemoteSystemSessionJoinResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinResult
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionJoinResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinResult) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionJoinStatus: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionJoinResult) -> win32more.Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
RemoteSystemSessionJoinStatus = Int32
RemoteSystemSessionJoinStatus_Success: RemoteSystemSessionJoinStatus = 0
RemoteSystemSessionJoinStatus_SessionLimitsExceeded: RemoteSystemSessionJoinStatus = 1
RemoteSystemSessionJoinStatus_OperationAborted: RemoteSystemSessionJoinStatus = 2
RemoteSystemSessionJoinStatus_SessionUnavailable: RemoteSystemSessionJoinStatus = 3
RemoteSystemSessionJoinStatus_RejectedByController: RemoteSystemSessionJoinStatus = 4
class RemoteSystemSessionMessageChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannelFactory, session: win32more.Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannelFactory, session: win32more.Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String, reliability: win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannelReliability) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel) -> win32more.Windows.System.RemoteSystems.RemoteSystemSession: ...
    @winrt_mixinmethod
    def BroadcastValueSetAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, messageData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SendValueSetAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, messageData: win32more.Windows.Foundation.Collections.ValueSet, participant: win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SendValueSetToParticipantsAsync(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, messageData: win32more.Windows.Foundation.Collections.ValueSet, participants: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_ValueSetReceived(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel, win32more.Windows.System.RemoteSystems.RemoteSystemSessionValueSetReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueSetReceived(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
RemoteSystemSessionMessageChannelReliability = Int32
RemoteSystemSessionMessageChannelReliability_Reliable: RemoteSystemSessionMessageChannelReliability = 0
RemoteSystemSessionMessageChannelReliability_Unreliable: RemoteSystemSessionMessageChannelReliability = 1
class RemoteSystemSessionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionOptions
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.System.RemoteSystems.RemoteSystemSessionOptions: ...
    @winrt_mixinmethod
    def get_IsInviteOnly(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInviteOnly(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionOptions, value: Boolean) -> Void: ...
    IsInviteOnly = property(get_IsInviteOnly, put_IsInviteOnly)
class RemoteSystemSessionParticipant(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipant
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipant'
    @winrt_mixinmethod
    def get_RemoteSystem(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipant) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_mixinmethod
    def GetHostNames(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipant) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    RemoteSystem = property(get_RemoteSystem, None)
class RemoteSystemSessionParticipantAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantAddedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipantAddedEventArgs'
    @winrt_mixinmethod
    def get_Participant(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantAddedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class RemoteSystemSessionParticipantRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantRemovedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipantRemovedEventArgs'
    @winrt_mixinmethod
    def get_Participant(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantRemovedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class RemoteSystemSessionParticipantWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcherStatus: ...
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
RemoteSystemSessionParticipantWatcherStatus = Int32
RemoteSystemSessionParticipantWatcherStatus_Created: RemoteSystemSessionParticipantWatcherStatus = 0
RemoteSystemSessionParticipantWatcherStatus_Started: RemoteSystemSessionParticipantWatcherStatus = 1
RemoteSystemSessionParticipantWatcherStatus_EnumerationCompleted: RemoteSystemSessionParticipantWatcherStatus = 2
RemoteSystemSessionParticipantWatcherStatus_Stopping: RemoteSystemSessionParticipantWatcherStatus = 3
RemoteSystemSessionParticipantWatcherStatus_Stopped: RemoteSystemSessionParticipantWatcherStatus = 4
RemoteSystemSessionParticipantWatcherStatus_Aborted: RemoteSystemSessionParticipantWatcherStatus = 5
class RemoteSystemSessionRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionRemovedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionRemovedEventArgs'
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionRemovedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionUpdatedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionUpdatedEventArgs'
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionUpdatedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionValueSetReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionValueSetReceivedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionValueSetReceivedEventArgs'
    @winrt_mixinmethod
    def get_Sender(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionValueSetReceivedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionValueSetReceivedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Sender = property(get_Sender, None)
    Message = property(get_Message, None)
class RemoteSystemSessionWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemSessionWatcher'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher) -> win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcherStatus: ...
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemSessionWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemSessionRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
RemoteSystemSessionWatcherStatus = Int32
RemoteSystemSessionWatcherStatus_Created: RemoteSystemSessionWatcherStatus = 0
RemoteSystemSessionWatcherStatus_Started: RemoteSystemSessionWatcherStatus = 1
RemoteSystemSessionWatcherStatus_EnumerationCompleted: RemoteSystemSessionWatcherStatus = 2
RemoteSystemSessionWatcherStatus_Stopping: RemoteSystemSessionWatcherStatus = 3
RemoteSystemSessionWatcherStatus_Stopped: RemoteSystemSessionWatcherStatus = 4
RemoteSystemSessionWatcherStatus_Aborted: RemoteSystemSessionWatcherStatus = 5
RemoteSystemStatus = Int32
RemoteSystemStatus_Unavailable: RemoteSystemStatus = 0
RemoteSystemStatus_DiscoveringAvailability: RemoteSystemStatus = 1
RemoteSystemStatus_Available: RemoteSystemStatus = 2
RemoteSystemStatus_Unknown: RemoteSystemStatus = 3
RemoteSystemStatusType = Int32
RemoteSystemStatusType_Any: RemoteSystemStatusType = 0
RemoteSystemStatusType_Available: RemoteSystemStatusType = 1
class RemoteSystemStatusTypeFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilter
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemStatusTypeFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilterFactory, remoteSystemStatusType: win32more.Windows.System.RemoteSystems.RemoteSystemStatusType) -> win32more.Windows.System.RemoteSystems.RemoteSystemStatusTypeFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemStatusType(self: win32more.Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilter) -> win32more.Windows.System.RemoteSystems.RemoteSystemStatusType: ...
    RemoteSystemStatusType = property(get_RemoteSystemStatusType, None)
class RemoteSystemUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemUpdatedEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemUpdatedEventArgs'
    @winrt_mixinmethod
    def get_RemoteSystem(self: win32more.Windows.System.RemoteSystems.IRemoteSystemUpdatedEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class RemoteSystemWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemWatcher'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteSystemAdded(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteSystemAdded(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteSystemUpdated(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteSystemUpdated(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteSystemRemoved(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteSystemRemoved(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemEnumerationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteSystems.RemoteSystemWatcher, win32more.Windows.System.RemoteSystems.RemoteSystemWatcherErrorOccurredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcher3) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
RemoteSystemWatcherError = Int32
RemoteSystemWatcherError_Unknown: RemoteSystemWatcherError = 0
RemoteSystemWatcherError_InternetNotAvailable: RemoteSystemWatcherError = 1
RemoteSystemWatcherError_AuthenticationError: RemoteSystemWatcherError = 2
class RemoteSystemWatcherErrorOccurredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcherErrorOccurredEventArgs
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemWatcherErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWatcherErrorOccurredEventArgs) -> win32more.Windows.System.RemoteSystems.RemoteSystemWatcherError: ...
    Error = property(get_Error, None)
class RemoteSystemWebAccountFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteSystems.IRemoteSystemWebAccountFilter
    _classid_ = 'Windows.System.RemoteSystems.RemoteSystemWebAccountFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemWebAccountFilterFactory, account: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.System.RemoteSystems.RemoteSystemWebAccountFilter: ...
    @winrt_mixinmethod
    def get_Account(self: win32more.Windows.System.RemoteSystems.IRemoteSystemWebAccountFilter) -> win32more.Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
make_head(_module, 'IKnownRemoteSystemCapabilitiesStatics')
make_head(_module, 'IRemoteSystem')
make_head(_module, 'IRemoteSystem2')
make_head(_module, 'IRemoteSystem3')
make_head(_module, 'IRemoteSystem4')
make_head(_module, 'IRemoteSystem5')
make_head(_module, 'IRemoteSystem6')
make_head(_module, 'IRemoteSystemAddedEventArgs')
make_head(_module, 'IRemoteSystemApp')
make_head(_module, 'IRemoteSystemApp2')
make_head(_module, 'IRemoteSystemAppRegistration')
make_head(_module, 'IRemoteSystemAppRegistrationStatics')
make_head(_module, 'IRemoteSystemAuthorizationKindFilter')
make_head(_module, 'IRemoteSystemAuthorizationKindFilterFactory')
make_head(_module, 'IRemoteSystemConnectionInfo')
make_head(_module, 'IRemoteSystemConnectionInfoStatics')
make_head(_module, 'IRemoteSystemConnectionRequest')
make_head(_module, 'IRemoteSystemConnectionRequest2')
make_head(_module, 'IRemoteSystemConnectionRequest3')
make_head(_module, 'IRemoteSystemConnectionRequestFactory')
make_head(_module, 'IRemoteSystemConnectionRequestStatics')
make_head(_module, 'IRemoteSystemConnectionRequestStatics2')
make_head(_module, 'IRemoteSystemDiscoveryTypeFilter')
make_head(_module, 'IRemoteSystemDiscoveryTypeFilterFactory')
make_head(_module, 'IRemoteSystemEnumerationCompletedEventArgs')
make_head(_module, 'IRemoteSystemFilter')
make_head(_module, 'IRemoteSystemKindFilter')
make_head(_module, 'IRemoteSystemKindFilterFactory')
make_head(_module, 'IRemoteSystemKindStatics')
make_head(_module, 'IRemoteSystemKindStatics2')
make_head(_module, 'IRemoteSystemRemovedEventArgs')
make_head(_module, 'IRemoteSystemSession')
make_head(_module, 'IRemoteSystemSessionAddedEventArgs')
make_head(_module, 'IRemoteSystemSessionController')
make_head(_module, 'IRemoteSystemSessionControllerFactory')
make_head(_module, 'IRemoteSystemSessionCreationResult')
make_head(_module, 'IRemoteSystemSessionDisconnectedEventArgs')
make_head(_module, 'IRemoteSystemSessionInfo')
make_head(_module, 'IRemoteSystemSessionInvitation')
make_head(_module, 'IRemoteSystemSessionInvitationListener')
make_head(_module, 'IRemoteSystemSessionInvitationReceivedEventArgs')
make_head(_module, 'IRemoteSystemSessionJoinRequest')
make_head(_module, 'IRemoteSystemSessionJoinRequestedEventArgs')
make_head(_module, 'IRemoteSystemSessionJoinResult')
make_head(_module, 'IRemoteSystemSessionMessageChannel')
make_head(_module, 'IRemoteSystemSessionMessageChannelFactory')
make_head(_module, 'IRemoteSystemSessionOptions')
make_head(_module, 'IRemoteSystemSessionParticipant')
make_head(_module, 'IRemoteSystemSessionParticipantAddedEventArgs')
make_head(_module, 'IRemoteSystemSessionParticipantRemovedEventArgs')
make_head(_module, 'IRemoteSystemSessionParticipantWatcher')
make_head(_module, 'IRemoteSystemSessionRemovedEventArgs')
make_head(_module, 'IRemoteSystemSessionStatics')
make_head(_module, 'IRemoteSystemSessionUpdatedEventArgs')
make_head(_module, 'IRemoteSystemSessionValueSetReceivedEventArgs')
make_head(_module, 'IRemoteSystemSessionWatcher')
make_head(_module, 'IRemoteSystemStatics')
make_head(_module, 'IRemoteSystemStatics2')
make_head(_module, 'IRemoteSystemStatics3')
make_head(_module, 'IRemoteSystemStatusTypeFilter')
make_head(_module, 'IRemoteSystemStatusTypeFilterFactory')
make_head(_module, 'IRemoteSystemUpdatedEventArgs')
make_head(_module, 'IRemoteSystemWatcher')
make_head(_module, 'IRemoteSystemWatcher2')
make_head(_module, 'IRemoteSystemWatcher3')
make_head(_module, 'IRemoteSystemWatcherErrorOccurredEventArgs')
make_head(_module, 'IRemoteSystemWebAccountFilter')
make_head(_module, 'IRemoteSystemWebAccountFilterFactory')
make_head(_module, 'KnownRemoteSystemCapabilities')
make_head(_module, 'RemoteSystem')
make_head(_module, 'RemoteSystemAddedEventArgs')
make_head(_module, 'RemoteSystemApp')
make_head(_module, 'RemoteSystemAppRegistration')
make_head(_module, 'RemoteSystemAuthorizationKindFilter')
make_head(_module, 'RemoteSystemConnectionInfo')
make_head(_module, 'RemoteSystemConnectionRequest')
make_head(_module, 'RemoteSystemDiscoveryTypeFilter')
make_head(_module, 'RemoteSystemEnumerationCompletedEventArgs')
make_head(_module, 'RemoteSystemKindFilter')
make_head(_module, 'RemoteSystemKinds')
make_head(_module, 'RemoteSystemRemovedEventArgs')
make_head(_module, 'RemoteSystemSession')
make_head(_module, 'RemoteSystemSessionAddedEventArgs')
make_head(_module, 'RemoteSystemSessionController')
make_head(_module, 'RemoteSystemSessionCreationResult')
make_head(_module, 'RemoteSystemSessionDisconnectedEventArgs')
make_head(_module, 'RemoteSystemSessionInfo')
make_head(_module, 'RemoteSystemSessionInvitation')
make_head(_module, 'RemoteSystemSessionInvitationListener')
make_head(_module, 'RemoteSystemSessionInvitationReceivedEventArgs')
make_head(_module, 'RemoteSystemSessionJoinRequest')
make_head(_module, 'RemoteSystemSessionJoinRequestedEventArgs')
make_head(_module, 'RemoteSystemSessionJoinResult')
make_head(_module, 'RemoteSystemSessionMessageChannel')
make_head(_module, 'RemoteSystemSessionOptions')
make_head(_module, 'RemoteSystemSessionParticipant')
make_head(_module, 'RemoteSystemSessionParticipantAddedEventArgs')
make_head(_module, 'RemoteSystemSessionParticipantRemovedEventArgs')
make_head(_module, 'RemoteSystemSessionParticipantWatcher')
make_head(_module, 'RemoteSystemSessionRemovedEventArgs')
make_head(_module, 'RemoteSystemSessionUpdatedEventArgs')
make_head(_module, 'RemoteSystemSessionValueSetReceivedEventArgs')
make_head(_module, 'RemoteSystemSessionWatcher')
make_head(_module, 'RemoteSystemStatusTypeFilter')
make_head(_module, 'RemoteSystemUpdatedEventArgs')
make_head(_module, 'RemoteSystemWatcher')
make_head(_module, 'RemoteSystemWatcherErrorOccurredEventArgs')
make_head(_module, 'RemoteSystemWebAccountFilter')
