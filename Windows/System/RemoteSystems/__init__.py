from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.AppService
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Security.Credentials
import Windows.System
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
class IKnownRemoteSystemCapabilitiesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8108e380-7f8a-44e4-92-cd-03-b6-46-9b-94-a3')
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
class IRemoteSystem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ed5838cd-1e10-4a8c-b4-a6-4e-5f-d6-f9-77-21')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Status(self) -> Windows.System.RemoteSystems.RemoteSystemStatus: ...
    @winrt_commethod(10)
    def get_IsAvailableByProximity(self) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    Status = property(get_Status, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
class IRemoteSystem2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('09dfe4ec-fb8b-4a08-a7-58-68-76-43-5d-76-9e')
    @winrt_commethod(6)
    def get_IsAvailableBySpatialProximity(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetCapabilitySupportedAsync(self, capabilityName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
class IRemoteSystem3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72b4b495-b7c6-40be-83-1b-73-56-2f-12-ff-a8')
    @winrt_commethod(6)
    def get_ManufacturerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ModelDisplayName(self) -> WinRT_String: ...
    ManufacturerDisplayName = property(get_ManufacturerDisplayName, None)
    ModelDisplayName = property(get_ModelDisplayName, None)
class IRemoteSystem4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f164ffe5-b987-4ca5-99-26-fa-04-38-be-62-73')
    @winrt_commethod(6)
    def get_Platform(self) -> Windows.System.RemoteSystems.RemoteSystemPlatform: ...
    Platform = property(get_Platform, None)
class IRemoteSystem5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb2ad723-e5e2-4ae2-a7-a7-a1-09-7a-09-8e-90')
    @winrt_commethod(6)
    def get_Apps(self) -> Windows.Foundation.Collections.IVectorView[Windows.System.RemoteSystems.RemoteSystemApp]: ...
    Apps = property(get_Apps, None)
class IRemoteSystem6(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d4cda942-c027-533e-93-84-3a-19-b4-f7-ee-f3')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IRemoteSystemAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8f39560f-e534-4697-88-36-7a-be-a1-51-51-6e')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('80e5bcbd-d54d-41b1-9b-16-68-10-a8-71-ed-4f')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsAvailableByProximity(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsAvailableBySpatialProximity(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Attributes(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
    Attributes = property(get_Attributes, None)
class IRemoteSystemApp2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6369bf15-0a96-577a-8f-f6-c3-59-04-df-a8-f3')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(7)
    def get_ConnectionToken(self) -> WinRT_String: ...
    User = property(get_User, None)
    ConnectionToken = property(get_ConnectionToken, None)
class IRemoteSystemAppRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b47947b5-7035-4a5a-b8-df-96-2d-8f-84-31-f4')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(7)
    def get_Attributes(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(8)
    def SaveAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    User = property(get_User, None)
    Attributes = property(get_Attributes, None)
class IRemoteSystemAppRegistrationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('01b99840-cfd2-453f-ae-25-c2-53-9f-08-6a-fd')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
class IRemoteSystemAuthorizationKindFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b0dde8e-04d0-40f4-a2-7f-c2-ac-bb-d6-b7-34')
    @winrt_commethod(6)
    def get_RemoteSystemAuthorizationKind(self) -> Windows.System.RemoteSystems.RemoteSystemAuthorizationKind: ...
    RemoteSystemAuthorizationKind = property(get_RemoteSystemAuthorizationKind, None)
class IRemoteSystemAuthorizationKindFilterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ad65df4d-b66a-45a4-81-77-8c-ae-d7-5d-9e-5a')
    @winrt_commethod(6)
    def Create(self, remoteSystemAuthorizationKind: Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> Windows.System.RemoteSystems.RemoteSystemAuthorizationKindFilter: ...
class IRemoteSystemConnectionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('23278bc3-0d09-52cb-9c-6a-ee-d2-94-0b-ee-43')
    @winrt_commethod(6)
    def get_IsProximal(self) -> Boolean: ...
    IsProximal = property(get_IsProximal, None)
class IRemoteSystemConnectionInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ac831e2d-66c5-56d7-a4-ce-70-5d-94-92-5a-d6')
    @winrt_commethod(6)
    def TryCreateFromAppServiceConnection(self, connection: Windows.ApplicationModel.AppService.AppServiceConnection) -> Windows.System.RemoteSystems.RemoteSystemConnectionInfo: ...
class IRemoteSystemConnectionRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('84ed4104-8d5e-4d72-82-38-76-21-57-6c-7a-67')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemConnectionRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12df6d6f-bffc-483a-8a-be-d3-4a-6c-19-f9-2b')
    @winrt_commethod(6)
    def get_RemoteSystemApp(self) -> Windows.System.RemoteSystems.RemoteSystemApp: ...
    RemoteSystemApp = property(get_RemoteSystemApp, None)
class IRemoteSystemConnectionRequest3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('de86c3e7-c9cc-5a50-b8-d9-ba-7b-34-bb-8d-0e')
    @winrt_commethod(6)
    def get_ConnectionToken(self) -> WinRT_String: ...
    ConnectionToken = property(get_ConnectionToken, None)
class IRemoteSystemConnectionRequestFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa0a0a20-baeb-4575-b5-30-81-0b-b9-78-63-34')
    @winrt_commethod(6)
    def Create(self, remoteSystem: Windows.System.RemoteSystems.RemoteSystem) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
class IRemoteSystemConnectionRequestStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('86ca143d-8214-425c-89-32-db-49-03-2d-13-06')
    @winrt_commethod(6)
    def CreateForApp(self, remoteSystemApp: Windows.System.RemoteSystems.RemoteSystemApp) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
class IRemoteSystemConnectionRequestStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('460f1027-64ec-598e-a8-00-4f-2e-e5-8d-ef-19')
    @winrt_commethod(6)
    def CreateFromConnectionToken(self, connectionToken: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_commethod(7)
    def CreateFromConnectionTokenForUser(self, user: Windows.System.User, connectionToken: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
class IRemoteSystemDiscoveryTypeFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('42d9041f-ee5a-43da-ac-6a-6f-ee-25-46-07-41')
    @winrt_commethod(6)
    def get_RemoteSystemDiscoveryType(self) -> Windows.System.RemoteSystems.RemoteSystemDiscoveryType: ...
    RemoteSystemDiscoveryType = property(get_RemoteSystemDiscoveryType, None)
class IRemoteSystemDiscoveryTypeFilterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9f9eb993-c260-4161-92-f2-9c-02-1f-23-fe-5d')
    @winrt_commethod(6)
    def Create(self, discoveryType: Windows.System.RemoteSystems.RemoteSystemDiscoveryType) -> Windows.System.RemoteSystems.RemoteSystemDiscoveryTypeFilter: ...
class IRemoteSystemEnumerationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c6e83d5f-4030-4354-a0-60-14-f1-b2-2c-54-5d')
class IRemoteSystemFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4a3ba9e4-99eb-45eb-ba-16-03-67-72-8f-f3-74')
class IRemoteSystemKindFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('38e1c9ec-22c3-4ef6-90-1a-bb-b1-c7-aa-d4-ed')
    @winrt_commethod(6)
    def get_RemoteSystemKinds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    RemoteSystemKinds = property(get_RemoteSystemKinds, None)
class IRemoteSystemKindFilterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a1fb18ee-99ea-40bc-9a-39-c6-70-aa-80-4a-28')
    @winrt_commethod(6)
    def Create(self, remoteSystemKinds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.System.RemoteSystems.RemoteSystemKindFilter: ...
class IRemoteSystemKindStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f6317633-ab14-41d0-95-53-79-6a-ad-b8-82-db')
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
class IRemoteSystemKindStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b9e3a3d0-0466-4749-91-e8-65-f9-d1-9a-96-a5')
    @winrt_commethod(6)
    def get_Iot(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Tablet(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Laptop(self) -> WinRT_String: ...
    Iot = property(get_Iot, None)
    Tablet = property(get_Tablet, None)
    Laptop = property(get_Laptop, None)
class IRemoteSystemRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8b3d16bb-7306-49ea-b7-df-67-d5-71-4c-b0-13')
    @winrt_commethod(6)
    def get_RemoteSystemId(self) -> WinRT_String: ...
    RemoteSystemId = property(get_RemoteSystemId, None)
class IRemoteSystemSession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69476a01-9ada-490f-95-49-d3-1c-b1-4c-9e-95')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ControllerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def add_Disconnected(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSession, Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Disconnected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CreateParticipantWatcher(self) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher: ...
    @winrt_commethod(12)
    def SendInvitationAsync(self, invitee: Windows.System.RemoteSystems.RemoteSystem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class IRemoteSystemSessionAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d585d754-bc97-4c39-99-b4-be-ca-76-e0-4c-3f')
    @winrt_commethod(6)
    def get_SessionInfo(self) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e48b2dd2-6820-4867-b4-25-d8-9c-0a-3e-f7-ba')
    @winrt_commethod(6)
    def add_JoinRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionController, Windows.System.RemoteSystems.RemoteSystemSessionJoinRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_JoinRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def RemoveParticipantAsync(self, pParticipant: Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def CreateSessionAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystemSessionCreationResult]: ...
class IRemoteSystemSessionControllerFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bfcc2f6b-ac3d-4199-82-cd-66-70-a7-73-ef-2e')
    @winrt_commethod(6)
    def CreateController(self, displayName: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemSessionController: ...
    @winrt_commethod(7)
    def CreateControllerWithSessionOptions(self, displayName: WinRT_String, options: Windows.System.RemoteSystems.RemoteSystemSessionOptions) -> Windows.System.RemoteSystems.RemoteSystemSessionController: ...
class IRemoteSystemSessionCreationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a79812c2-37de-448c-8b-83-a3-0a-a3-c4-ea-d6')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.System.RemoteSystems.RemoteSystemSessionCreationStatus: ...
    @winrt_commethod(7)
    def get_Session(self) -> Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
class IRemoteSystemSessionDisconnectedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('de0bc69b-77c5-461c-82-09-7c-6c-5d-31-11-ab')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedReason: ...
    Reason = property(get_Reason, None)
class IRemoteSystemSessionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ff4df648-8b0a-4e9a-99-05-69-e4-b8-41-c5-88')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ControllerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def JoinAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystemSessionJoinResult]: ...
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class IRemoteSystemSessionInvitation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3e32cc91-51d7-4766-a1-21-25-51-6c-3b-82-94')
    @winrt_commethod(6)
    def get_Sender(self) -> Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_commethod(7)
    def get_SessionInfo(self) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    Sender = property(get_Sender, None)
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionInvitationListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('08f4003f-bc71-49e1-87-4a-31-dd-ff-9a-27-b9')
    @winrt_commethod(6)
    def add_InvitationReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener, Windows.System.RemoteSystems.RemoteSystemSessionInvitationReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_InvitationReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRemoteSystemSessionInvitationReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5e964a2d-a10d-4edb-8d-ea-54-d2-0a-c1-95-43')
    @winrt_commethod(6)
    def get_Invitation(self) -> Windows.System.RemoteSystems.RemoteSystemSessionInvitation: ...
    Invitation = property(get_Invitation, None)
class IRemoteSystemSessionJoinRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20600068-7994-4331-86-d1-d8-9d-88-25-85-ee')
    @winrt_commethod(6)
    def get_Participant(self) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_commethod(7)
    def Accept(self) -> Void: ...
    Participant = property(get_Participant, None)
class IRemoteSystemSessionJoinRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dbca4fc3-82b9-4816-9c-24-e4-0e-61-77-4b-d8')
    @winrt_commethod(6)
    def get_JoinRequest(self) -> Windows.System.RemoteSystems.RemoteSystemSessionJoinRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    JoinRequest = property(get_JoinRequest, None)
class IRemoteSystemSessionJoinResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce7b1f04-a03e-41a4-90-0b-1e-79-32-8c-12-67')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.System.RemoteSystems.RemoteSystemSessionJoinStatus: ...
    @winrt_commethod(7)
    def get_Session(self) -> Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
class IRemoteSystemSessionMessageChannel(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9524d12a-73d9-4c10-b7-51-c2-67-84-43-71-27')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.System.RemoteSystems.RemoteSystemSession: ...
    @winrt_commethod(7)
    def BroadcastValueSetAsync(self, messageData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def SendValueSetAsync(self, messageData: Windows.Foundation.Collections.ValueSet, participant: Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def SendValueSetToParticipantsAsync(self, messageData: Windows.Foundation.Collections.ValueSet, participants: Windows.Foundation.Collections.IIterable[Windows.System.RemoteSystems.RemoteSystemSessionParticipant]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def add_ValueSetReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel, Windows.System.RemoteSystems.RemoteSystemSessionValueSetReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ValueSetReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
class IRemoteSystemSessionMessageChannelFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('295e1c4a-bd16-4298-b7-ce-41-54-82-b0-e1-1d')
    @winrt_commethod(6)
    def Create(self, session: Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
    @winrt_commethod(7)
    def CreateWithReliability(self, session: Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String, reliability: Windows.System.RemoteSystems.RemoteSystemSessionMessageChannelReliability) -> Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
class IRemoteSystemSessionOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('740ed755-8418-4f01-93-53-e2-1c-9e-cc-6c-fc')
    @winrt_commethod(6)
    def get_IsInviteOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsInviteOnly(self, value: Boolean) -> Void: ...
    IsInviteOnly = property(get_IsInviteOnly, put_IsInviteOnly)
class IRemoteSystemSessionParticipant(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e90058c-acf9-4729-8a-17-44-e7-ba-ed-5d-cc')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_commethod(7)
    def GetHostNames(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemSessionParticipantAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d35a57d8-c9a1-4bb7-b6-b0-79-bb-91-ad-f9-3d')
    @winrt_commethod(6)
    def get_Participant(self) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class IRemoteSystemSessionParticipantRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('866ef088-de68-4abf-88-a1-f9-0d-16-27-41-92')
    @winrt_commethod(6)
    def get_Participant(self) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class IRemoteSystemSessionParticipantWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dcdd02cc-aa87-4d79-b6-cc-44-59-b3-e9-20-75')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcherStatus: ...
    @winrt_commethod(9)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, Windows.System.RemoteSystems.RemoteSystemSessionParticipantAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, Windows.System.RemoteSystems.RemoteSystemSessionParticipantRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IRemoteSystemSessionRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('af82914e-39a1-4dea-9d-63-43-79-8d-5b-bb-d0')
    @winrt_commethod(6)
    def get_SessionInfo(self) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8524899f-fd20-44e3-95-65-e7-5a-3b-14-c6-6e')
    @winrt_commethod(6)
    def CreateWatcher(self) -> Windows.System.RemoteSystems.RemoteSystemSessionWatcher: ...
class IRemoteSystemSessionUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('16875069-231e-4c91-8e-c8-b3-a3-9d-9e-55-a3')
    @winrt_commethod(6)
    def get_SessionInfo(self) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class IRemoteSystemSessionValueSetReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('06f31785-2da5-4e58-a7-8f-9e-8d-07-84-ee-25')
    @winrt_commethod(6)
    def get_Sender(self) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_commethod(7)
    def get_Message(self) -> Windows.Foundation.Collections.ValueSet: ...
    Sender = property(get_Sender, None)
    Message = property(get_Message, None)
class IRemoteSystemSessionWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8003e340-0c41-4a62-b6-d7-bd-be-2b-19-be-2d')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.System.RemoteSystems.RemoteSystemSessionWatcherStatus: ...
    @winrt_commethod(9)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionWatcher, Windows.System.RemoteSystems.RemoteSystemSessionAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionWatcher, Windows.System.RemoteSystems.RemoteSystemSessionUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionWatcher, Windows.System.RemoteSystems.RemoteSystemSessionRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IRemoteSystemStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a485b392-ff2b-4b47-be-62-74-3f-2f-14-0f-30')
    @winrt_commethod(6)
    def FindByHostNameAsync(self, hostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystem]: ...
    @winrt_commethod(7)
    def CreateWatcher(self) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_commethod(8)
    def CreateWatcherWithFilters(self, filters: Windows.Foundation.Collections.IIterable[Windows.System.RemoteSystems.IRemoteSystemFilter]) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystemAccessStatus]: ...
class IRemoteSystemStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c98edca-6f99-4c52-a2-72-ea-4f-36-47-17-44')
    @winrt_commethod(6)
    def IsAuthorizationKindEnabled(self, kind: Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> Boolean: ...
class IRemoteSystemStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9995f16f-0b3c-5ac5-b3-25-cc-73-f4-37-df-cd')
    @winrt_commethod(6)
    def CreateWatcherForUser(self, user: Windows.System.User) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_commethod(7)
    def CreateWatcherWithFiltersForUser(self, user: Windows.System.User, filters: Windows.Foundation.Collections.IIterable[Windows.System.RemoteSystems.IRemoteSystemFilter]) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
class IRemoteSystemStatusTypeFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c39514e-cbb6-4777-85-34-2e-0c-52-1a-ff-a2')
    @winrt_commethod(6)
    def get_RemoteSystemStatusType(self) -> Windows.System.RemoteSystems.RemoteSystemStatusType: ...
    RemoteSystemStatusType = property(get_RemoteSystemStatusType, None)
class IRemoteSystemStatusTypeFilterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33cf78fa-d724-4125-ac-7a-8d-28-1e-44-c9-49')
    @winrt_commethod(6)
    def Create(self, remoteSystemStatusType: Windows.System.RemoteSystems.RemoteSystemStatusType) -> Windows.System.RemoteSystems.RemoteSystemStatusTypeFilter: ...
class IRemoteSystemUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7502ff0e-dbcb-4155-b4-ca-b3-0a-04-f2-76-27')
    @winrt_commethod(6)
    def get_RemoteSystem(self) -> Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class IRemoteSystemWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d600c7e-2c07-48c5-88-9c-45-5d-2b-09-97-71')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def add_RemoteSystemAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RemoteSystemAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_RemoteSystemUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_RemoteSystemUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_RemoteSystemRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RemoteSystemRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRemoteSystemWatcher2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('73436700-19ca-48f9-a4-cd-78-0f-7a-d5-8c-71')
    @winrt_commethod(6)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemEnumerationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ErrorOccurred(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemWatcherErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ErrorOccurred(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IRemoteSystemWatcher3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f79c0fcf-a913-55d3-84-13-41-8f-cf-15-ba-54')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IRemoteSystemWatcherErrorOccurredEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('74c5c6af-5114-4426-92-16-20-d8-1f-85-19-ae')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.System.RemoteSystems.RemoteSystemWatcherError: ...
    Error = property(get_Error, None)
class IRemoteSystemWebAccountFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3fb75873-87c8-5d8f-97-7e-f6-9f-96-d6-72-38')
    @winrt_commethod(6)
    def get_Account(self) -> Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
class IRemoteSystemWebAccountFilterFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('348a2709-5f4d-5127-b4-a7-bf-99-d5-25-2b-1b')
    @winrt_commethod(6)
    def Create(self, account: Windows.Security.Credentials.WebAccount) -> Windows.System.RemoteSystems.RemoteSystemWebAccountFilter: ...
class KnownRemoteSystemCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.KnownRemoteSystemCapabilities'
    @winrt_classmethod
    def get_AppService(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_LaunchUri(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RemoteSession(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SpatialEntity(cls: Windows.System.RemoteSystems.IKnownRemoteSystemCapabilitiesStatics) -> WinRT_String: ...
    AppService = property(get_AppService, None)
    LaunchUri = property(get_LaunchUri, None)
    RemoteSession = property(get_RemoteSession, None)
    SpatialEntity = property(get_SpatialEntity, None)
class RemoteSystem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystem'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.System.RemoteSystems.IRemoteSystem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.System.RemoteSystems.IRemoteSystem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.System.RemoteSystems.IRemoteSystem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.System.RemoteSystems.IRemoteSystem) -> Windows.System.RemoteSystems.RemoteSystemStatus: ...
    @winrt_mixinmethod
    def get_IsAvailableByProximity(self: Windows.System.RemoteSystems.IRemoteSystem) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAvailableBySpatialProximity(self: Windows.System.RemoteSystems.IRemoteSystem2) -> Boolean: ...
    @winrt_mixinmethod
    def GetCapabilitySupportedAsync(self: Windows.System.RemoteSystems.IRemoteSystem2, capabilityName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ManufacturerDisplayName(self: Windows.System.RemoteSystems.IRemoteSystem3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelDisplayName(self: Windows.System.RemoteSystems.IRemoteSystem3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Platform(self: Windows.System.RemoteSystems.IRemoteSystem4) -> Windows.System.RemoteSystems.RemoteSystemPlatform: ...
    @winrt_mixinmethod
    def get_Apps(self: Windows.System.RemoteSystems.IRemoteSystem5) -> Windows.Foundation.Collections.IVectorView[Windows.System.RemoteSystems.RemoteSystemApp]: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.RemoteSystems.IRemoteSystem6) -> Windows.System.User: ...
    @winrt_classmethod
    def CreateWatcherForUser(cls: Windows.System.RemoteSystems.IRemoteSystemStatics3, user: Windows.System.User) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def CreateWatcherWithFiltersForUser(cls: Windows.System.RemoteSystems.IRemoteSystemStatics3, user: Windows.System.User, filters: Windows.Foundation.Collections.IIterable[Windows.System.RemoteSystems.IRemoteSystemFilter]) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def IsAuthorizationKindEnabled(cls: Windows.System.RemoteSystems.IRemoteSystemStatics2, kind: Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> Boolean: ...
    @winrt_classmethod
    def FindByHostNameAsync(cls: Windows.System.RemoteSystems.IRemoteSystemStatics, hostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystem]: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.System.RemoteSystems.IRemoteSystemStatics) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def CreateWatcherWithFilters(cls: Windows.System.RemoteSystems.IRemoteSystemStatics, filters: Windows.Foundation.Collections.IIterable[Windows.System.RemoteSystems.IRemoteSystemFilter]) -> Windows.System.RemoteSystems.RemoteSystemWatcher: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.System.RemoteSystems.IRemoteSystemStatics) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystemAccessStatus]: ...
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
class RemoteSystemAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemAddedEventArgs'
    @winrt_mixinmethod
    def get_RemoteSystem(self: Windows.System.RemoteSystems.IRemoteSystemAddedEventArgs) -> Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class RemoteSystemApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemApp'
    @winrt_mixinmethod
    def get_Id(self: Windows.System.RemoteSystems.IRemoteSystemApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.System.RemoteSystems.IRemoteSystemApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsAvailableByProximity(self: Windows.System.RemoteSystems.IRemoteSystemApp) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAvailableBySpatialProximity(self: Windows.System.RemoteSystems.IRemoteSystemApp) -> Boolean: ...
    @winrt_mixinmethod
    def get_Attributes(self: Windows.System.RemoteSystems.IRemoteSystemApp) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.RemoteSystems.IRemoteSystemApp2) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_ConnectionToken(self: Windows.System.RemoteSystems.IRemoteSystemApp2) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    IsAvailableByProximity = property(get_IsAvailableByProximity, None)
    IsAvailableBySpatialProximity = property(get_IsAvailableBySpatialProximity, None)
    Attributes = property(get_Attributes, None)
    User = property(get_User, None)
    ConnectionToken = property(get_ConnectionToken, None)
class RemoteSystemAppRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemAppRegistration'
    @winrt_mixinmethod
    def get_User(self: Windows.System.RemoteSystems.IRemoteSystemAppRegistration) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_Attributes(self: Windows.System.RemoteSystems.IRemoteSystemAppRegistration) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.System.RemoteSystems.IRemoteSystemAppRegistration) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.RemoteSystems.IRemoteSystemAppRegistrationStatics) -> Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.System.RemoteSystems.IRemoteSystemAppRegistrationStatics, user: Windows.System.User) -> Windows.System.RemoteSystems.RemoteSystemAppRegistration: ...
    User = property(get_User, None)
    Attributes = property(get_Attributes, None)
RemoteSystemAuthorizationKind = Int32
RemoteSystemAuthorizationKind_SameUser: RemoteSystemAuthorizationKind = 0
RemoteSystemAuthorizationKind_Anonymous: RemoteSystemAuthorizationKind = 1
class RemoteSystemAuthorizationKindFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemAuthorizationKindFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilterFactory, remoteSystemAuthorizationKind: Windows.System.RemoteSystems.RemoteSystemAuthorizationKind) -> Windows.System.RemoteSystems.RemoteSystemAuthorizationKindFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemAuthorizationKind(self: Windows.System.RemoteSystems.IRemoteSystemAuthorizationKindFilter) -> Windows.System.RemoteSystems.RemoteSystemAuthorizationKind: ...
    RemoteSystemAuthorizationKind = property(get_RemoteSystemAuthorizationKind, None)
class RemoteSystemConnectionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemConnectionInfo'
    @winrt_mixinmethod
    def get_IsProximal(self: Windows.System.RemoteSystems.IRemoteSystemConnectionInfo) -> Boolean: ...
    @winrt_classmethod
    def TryCreateFromAppServiceConnection(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionInfoStatics, connection: Windows.ApplicationModel.AppService.AppServiceConnection) -> Windows.System.RemoteSystems.RemoteSystemConnectionInfo: ...
    IsProximal = property(get_IsProximal, None)
class RemoteSystemConnectionRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemConnectionRequest'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestFactory, remoteSystem: Windows.System.RemoteSystems.RemoteSystem) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_mixinmethod
    def get_RemoteSystem(self: Windows.System.RemoteSystems.IRemoteSystemConnectionRequest) -> Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_mixinmethod
    def get_RemoteSystemApp(self: Windows.System.RemoteSystems.IRemoteSystemConnectionRequest2) -> Windows.System.RemoteSystems.RemoteSystemApp: ...
    @winrt_mixinmethod
    def get_ConnectionToken(self: Windows.System.RemoteSystems.IRemoteSystemConnectionRequest3) -> WinRT_String: ...
    @winrt_classmethod
    def CreateFromConnectionToken(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics2, connectionToken: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_classmethod
    def CreateFromConnectionTokenForUser(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics2, user: Windows.System.User, connectionToken: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    @winrt_classmethod
    def CreateForApp(cls: Windows.System.RemoteSystems.IRemoteSystemConnectionRequestStatics, remoteSystemApp: Windows.System.RemoteSystems.RemoteSystemApp) -> Windows.System.RemoteSystems.RemoteSystemConnectionRequest: ...
    RemoteSystem = property(get_RemoteSystem, None)
    RemoteSystemApp = property(get_RemoteSystemApp, None)
    ConnectionToken = property(get_ConnectionToken, None)
RemoteSystemDiscoveryType = Int32
RemoteSystemDiscoveryType_Any: RemoteSystemDiscoveryType = 0
RemoteSystemDiscoveryType_Proximal: RemoteSystemDiscoveryType = 1
RemoteSystemDiscoveryType_Cloud: RemoteSystemDiscoveryType = 2
RemoteSystemDiscoveryType_SpatiallyProximal: RemoteSystemDiscoveryType = 3
class RemoteSystemDiscoveryTypeFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemDiscoveryTypeFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilterFactory, discoveryType: Windows.System.RemoteSystems.RemoteSystemDiscoveryType) -> Windows.System.RemoteSystems.RemoteSystemDiscoveryTypeFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemDiscoveryType(self: Windows.System.RemoteSystems.IRemoteSystemDiscoveryTypeFilter) -> Windows.System.RemoteSystems.RemoteSystemDiscoveryType: ...
    RemoteSystemDiscoveryType = property(get_RemoteSystemDiscoveryType, None)
class RemoteSystemEnumerationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemEnumerationCompletedEventArgs'
class RemoteSystemKindFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemKindFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemKindFilterFactory, remoteSystemKinds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.System.RemoteSystems.RemoteSystemKindFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemKinds(self: Windows.System.RemoteSystems.IRemoteSystemKindFilter) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    RemoteSystemKinds = property(get_RemoteSystemKinds, None)
class RemoteSystemKinds(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemKinds'
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
    Iot = property(get_Iot, None)
    Tablet = property(get_Tablet, None)
    Laptop = property(get_Laptop, None)
    Phone = property(get_Phone, None)
    Hub = property(get_Hub, None)
    Holographic = property(get_Holographic, None)
    Desktop = property(get_Desktop, None)
    Xbox = property(get_Xbox, None)
RemoteSystemPlatform = Int32
RemoteSystemPlatform_Unknown: RemoteSystemPlatform = 0
RemoteSystemPlatform_Windows: RemoteSystemPlatform = 1
RemoteSystemPlatform_Android: RemoteSystemPlatform = 2
RemoteSystemPlatform_Ios: RemoteSystemPlatform = 3
RemoteSystemPlatform_Linux: RemoteSystemPlatform = 4
class RemoteSystemRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemRemovedEventArgs'
    @winrt_mixinmethod
    def get_RemoteSystemId(self: Windows.System.RemoteSystems.IRemoteSystemRemovedEventArgs) -> WinRT_String: ...
    RemoteSystemId = property(get_RemoteSystemId, None)
class RemoteSystemSession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSession'
    @winrt_mixinmethod
    def get_Id(self: Windows.System.RemoteSystems.IRemoteSystemSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.System.RemoteSystems.IRemoteSystemSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ControllerDisplayName(self: Windows.System.RemoteSystems.IRemoteSystemSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_Disconnected(self: Windows.System.RemoteSystems.IRemoteSystemSession, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSession, Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disconnected(self: Windows.System.RemoteSystems.IRemoteSystemSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateParticipantWatcher(self: Windows.System.RemoteSystems.IRemoteSystemSession) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher: ...
    @winrt_mixinmethod
    def SendInvitationAsync(self: Windows.System.RemoteSystems.IRemoteSystemSession, invitee: Windows.System.RemoteSystems.RemoteSystem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.System.RemoteSystems.IRemoteSystemSessionStatics) -> Windows.System.RemoteSystems.RemoteSystemSessionWatcher: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class RemoteSystemSessionAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionAddedEventArgs'
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.System.RemoteSystems.IRemoteSystemSessionAddedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionController'
    @winrt_factorymethod
    def CreateController(cls: Windows.System.RemoteSystems.IRemoteSystemSessionControllerFactory, displayName: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemSessionController: ...
    @winrt_factorymethod
    def CreateController(cls: Windows.System.RemoteSystems.IRemoteSystemSessionControllerFactory, displayName: WinRT_String, options: Windows.System.RemoteSystems.RemoteSystemSessionOptions) -> Windows.System.RemoteSystems.RemoteSystemSessionController: ...
    @winrt_mixinmethod
    def add_JoinRequested(self: Windows.System.RemoteSystems.IRemoteSystemSessionController, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionController, Windows.System.RemoteSystems.RemoteSystemSessionJoinRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_JoinRequested(self: Windows.System.RemoteSystems.IRemoteSystemSessionController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RemoveParticipantAsync(self: Windows.System.RemoteSystems.IRemoteSystemSessionController, pParticipant: Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def CreateSessionAsync(self: Windows.System.RemoteSystems.IRemoteSystemSessionController) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystemSessionCreationResult]: ...
class RemoteSystemSessionCreationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionCreationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.System.RemoteSystems.IRemoteSystemSessionCreationResult) -> Windows.System.RemoteSystems.RemoteSystemSessionCreationStatus: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.System.RemoteSystems.IRemoteSystemSessionCreationResult) -> Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
RemoteSystemSessionCreationStatus = Int32
RemoteSystemSessionCreationStatus_Success: RemoteSystemSessionCreationStatus = 0
RemoteSystemSessionCreationStatus_SessionLimitsExceeded: RemoteSystemSessionCreationStatus = 1
RemoteSystemSessionCreationStatus_OperationAborted: RemoteSystemSessionCreationStatus = 2
class RemoteSystemSessionDisconnectedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.System.RemoteSystems.IRemoteSystemSessionDisconnectedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedReason: ...
    Reason = property(get_Reason, None)
RemoteSystemSessionDisconnectedReason = Int32
RemoteSystemSessionDisconnectedReason_SessionUnavailable: RemoteSystemSessionDisconnectedReason = 0
RemoteSystemSessionDisconnectedReason_RemovedByController: RemoteSystemSessionDisconnectedReason = 1
RemoteSystemSessionDisconnectedReason_SessionClosed: RemoteSystemSessionDisconnectedReason = 2
class RemoteSystemSessionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.System.RemoteSystems.IRemoteSystemSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ControllerDisplayName(self: Windows.System.RemoteSystems.IRemoteSystemSessionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def JoinAsync(self: Windows.System.RemoteSystems.IRemoteSystemSessionInfo) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteSystems.RemoteSystemSessionJoinResult]: ...
    DisplayName = property(get_DisplayName, None)
    ControllerDisplayName = property(get_ControllerDisplayName, None)
class RemoteSystemSessionInvitation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionInvitation'
    @winrt_mixinmethod
    def get_Sender(self: Windows.System.RemoteSystems.IRemoteSystemSessionInvitation) -> Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.System.RemoteSystems.IRemoteSystemSessionInvitation) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    Sender = property(get_Sender, None)
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionInvitationListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener'
    @winrt_activatemethod
    def New(cls) -> Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener: ...
    @winrt_mixinmethod
    def add_InvitationReceived(self: Windows.System.RemoteSystems.IRemoteSystemSessionInvitationListener, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionInvitationListener, Windows.System.RemoteSystems.RemoteSystemSessionInvitationReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InvitationReceived(self: Windows.System.RemoteSystems.IRemoteSystemSessionInvitationListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class RemoteSystemSessionInvitationReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionInvitationReceivedEventArgs'
    @winrt_mixinmethod
    def get_Invitation(self: Windows.System.RemoteSystems.IRemoteSystemSessionInvitationReceivedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionInvitation: ...
    Invitation = property(get_Invitation, None)
class RemoteSystemSessionJoinRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionJoinRequest'
    @winrt_mixinmethod
    def get_Participant(self: Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequest) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_mixinmethod
    def Accept(self: Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequest) -> Void: ...
    Participant = property(get_Participant, None)
class RemoteSystemSessionJoinRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionJoinRequestedEventArgs'
    @winrt_mixinmethod
    def get_JoinRequest(self: Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequestedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionJoinRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.System.RemoteSystems.IRemoteSystemSessionJoinRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    JoinRequest = property(get_JoinRequest, None)
class RemoteSystemSessionJoinResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionJoinResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.System.RemoteSystems.IRemoteSystemSessionJoinResult) -> Windows.System.RemoteSystems.RemoteSystemSessionJoinStatus: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.System.RemoteSystems.IRemoteSystemSessionJoinResult) -> Windows.System.RemoteSystems.RemoteSystemSession: ...
    Status = property(get_Status, None)
    Session = property(get_Session, None)
RemoteSystemSessionJoinStatus = Int32
RemoteSystemSessionJoinStatus_Success: RemoteSystemSessionJoinStatus = 0
RemoteSystemSessionJoinStatus_SessionLimitsExceeded: RemoteSystemSessionJoinStatus = 1
RemoteSystemSessionJoinStatus_OperationAborted: RemoteSystemSessionJoinStatus = 2
RemoteSystemSessionJoinStatus_SessionUnavailable: RemoteSystemSessionJoinStatus = 3
RemoteSystemSessionJoinStatus_RejectedByController: RemoteSystemSessionJoinStatus = 4
class RemoteSystemSessionMessageChannel(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannelFactory, session: Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String) -> Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannelFactory, session: Windows.System.RemoteSystems.RemoteSystemSession, channelName: WinRT_String, reliability: Windows.System.RemoteSystems.RemoteSystemSessionMessageChannelReliability) -> Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel) -> Windows.System.RemoteSystems.RemoteSystemSession: ...
    @winrt_mixinmethod
    def BroadcastValueSetAsync(self: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, messageData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SendValueSetAsync(self: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, messageData: Windows.Foundation.Collections.ValueSet, participant: Windows.System.RemoteSystems.RemoteSystemSessionParticipant) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SendValueSetToParticipantsAsync(self: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, messageData: Windows.Foundation.Collections.ValueSet, participants: Windows.Foundation.Collections.IIterable[Windows.System.RemoteSystems.RemoteSystemSessionParticipant]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_ValueSetReceived(self: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionMessageChannel, Windows.System.RemoteSystems.RemoteSystemSessionValueSetReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueSetReceived(self: Windows.System.RemoteSystems.IRemoteSystemSessionMessageChannel, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
RemoteSystemSessionMessageChannelReliability = Int32
RemoteSystemSessionMessageChannelReliability_Reliable: RemoteSystemSessionMessageChannelReliability = 0
RemoteSystemSessionMessageChannelReliability_Unreliable: RemoteSystemSessionMessageChannelReliability = 1
class RemoteSystemSessionOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.System.RemoteSystems.RemoteSystemSessionOptions: ...
    @winrt_mixinmethod
    def get_IsInviteOnly(self: Windows.System.RemoteSystems.IRemoteSystemSessionOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInviteOnly(self: Windows.System.RemoteSystems.IRemoteSystemSessionOptions, value: Boolean) -> Void: ...
    IsInviteOnly = property(get_IsInviteOnly, put_IsInviteOnly)
class RemoteSystemSessionParticipant(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipant'
    @winrt_mixinmethod
    def get_RemoteSystem(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipant) -> Windows.System.RemoteSystems.RemoteSystem: ...
    @winrt_mixinmethod
    def GetHostNames(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipant) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    RemoteSystem = property(get_RemoteSystem, None)
class RemoteSystemSessionParticipantAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipantAddedEventArgs'
    @winrt_mixinmethod
    def get_Participant(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantAddedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class RemoteSystemSessionParticipantRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipantRemovedEventArgs'
    @winrt_mixinmethod
    def get_Participant(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantRemovedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    Participant = property(get_Participant, None)
class RemoteSystemSessionParticipantWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher'
    @winrt_mixinmethod
    def Start(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcherStatus: ...
    @winrt_mixinmethod
    def add_Added(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, Windows.System.RemoteSystems.RemoteSystemSessionParticipantAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, Windows.System.RemoteSystems.RemoteSystemSessionParticipantRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.System.RemoteSystems.IRemoteSystemSessionParticipantWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
RemoteSystemSessionParticipantWatcherStatus = Int32
RemoteSystemSessionParticipantWatcherStatus_Created: RemoteSystemSessionParticipantWatcherStatus = 0
RemoteSystemSessionParticipantWatcherStatus_Started: RemoteSystemSessionParticipantWatcherStatus = 1
RemoteSystemSessionParticipantWatcherStatus_EnumerationCompleted: RemoteSystemSessionParticipantWatcherStatus = 2
RemoteSystemSessionParticipantWatcherStatus_Stopping: RemoteSystemSessionParticipantWatcherStatus = 3
RemoteSystemSessionParticipantWatcherStatus_Stopped: RemoteSystemSessionParticipantWatcherStatus = 4
RemoteSystemSessionParticipantWatcherStatus_Aborted: RemoteSystemSessionParticipantWatcherStatus = 5
class RemoteSystemSessionRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionRemovedEventArgs'
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.System.RemoteSystems.IRemoteSystemSessionRemovedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionUpdatedEventArgs'
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.System.RemoteSystems.IRemoteSystemSessionUpdatedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionInfo: ...
    SessionInfo = property(get_SessionInfo, None)
class RemoteSystemSessionValueSetReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionValueSetReceivedEventArgs'
    @winrt_mixinmethod
    def get_Sender(self: Windows.System.RemoteSystems.IRemoteSystemSessionValueSetReceivedEventArgs) -> Windows.System.RemoteSystems.RemoteSystemSessionParticipant: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.System.RemoteSystems.IRemoteSystemSessionValueSetReceivedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    Sender = property(get_Sender, None)
    Message = property(get_Message, None)
class RemoteSystemSessionWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemSessionWatcher'
    @winrt_mixinmethod
    def Start(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher) -> Windows.System.RemoteSystems.RemoteSystemSessionWatcherStatus: ...
    @winrt_mixinmethod
    def add_Added(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionWatcher, Windows.System.RemoteSystems.RemoteSystemSessionAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionWatcher, Windows.System.RemoteSystems.RemoteSystemSessionUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemSessionWatcher, Windows.System.RemoteSystems.RemoteSystemSessionRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.System.RemoteSystems.IRemoteSystemSessionWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
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
class RemoteSystemStatusTypeFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemStatusTypeFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilterFactory, remoteSystemStatusType: Windows.System.RemoteSystems.RemoteSystemStatusType) -> Windows.System.RemoteSystems.RemoteSystemStatusTypeFilter: ...
    @winrt_mixinmethod
    def get_RemoteSystemStatusType(self: Windows.System.RemoteSystems.IRemoteSystemStatusTypeFilter) -> Windows.System.RemoteSystems.RemoteSystemStatusType: ...
    RemoteSystemStatusType = property(get_RemoteSystemStatusType, None)
class RemoteSystemUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemUpdatedEventArgs'
    @winrt_mixinmethod
    def get_RemoteSystem(self: Windows.System.RemoteSystems.IRemoteSystemUpdatedEventArgs) -> Windows.System.RemoteSystems.RemoteSystem: ...
    RemoteSystem = property(get_RemoteSystem, None)
class RemoteSystemWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemWatcher'
    @winrt_mixinmethod
    def Start(self: Windows.System.RemoteSystems.IRemoteSystemWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.RemoteSystems.IRemoteSystemWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteSystemAdded(self: Windows.System.RemoteSystems.IRemoteSystemWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteSystemAdded(self: Windows.System.RemoteSystems.IRemoteSystemWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteSystemUpdated(self: Windows.System.RemoteSystems.IRemoteSystemWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteSystemUpdated(self: Windows.System.RemoteSystems.IRemoteSystemWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RemoteSystemRemoved(self: Windows.System.RemoteSystems.IRemoteSystemWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemoteSystemRemoved(self: Windows.System.RemoteSystems.IRemoteSystemWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.System.RemoteSystems.IRemoteSystemWatcher2, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemEnumerationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.System.RemoteSystems.IRemoteSystemWatcher2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: Windows.System.RemoteSystems.IRemoteSystemWatcher2, handler: Windows.Foundation.TypedEventHandler[Windows.System.RemoteSystems.RemoteSystemWatcher, Windows.System.RemoteSystems.RemoteSystemWatcherErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: Windows.System.RemoteSystems.IRemoteSystemWatcher2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.RemoteSystems.IRemoteSystemWatcher3) -> Windows.System.User: ...
    User = property(get_User, None)
RemoteSystemWatcherError = Int32
RemoteSystemWatcherError_Unknown: RemoteSystemWatcherError = 0
RemoteSystemWatcherError_InternetNotAvailable: RemoteSystemWatcherError = 1
RemoteSystemWatcherError_AuthenticationError: RemoteSystemWatcherError = 2
class RemoteSystemWatcherErrorOccurredEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemWatcherErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.System.RemoteSystems.IRemoteSystemWatcherErrorOccurredEventArgs) -> Windows.System.RemoteSystems.RemoteSystemWatcherError: ...
    Error = property(get_Error, None)
class RemoteSystemWebAccountFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteSystems.RemoteSystemWebAccountFilter'
    @winrt_factorymethod
    def Create(cls: Windows.System.RemoteSystems.IRemoteSystemWebAccountFilterFactory, account: Windows.Security.Credentials.WebAccount) -> Windows.System.RemoteSystems.RemoteSystemWebAccountFilter: ...
    @winrt_mixinmethod
    def get_Account(self: Windows.System.RemoteSystems.IRemoteSystemWebAccountFilter) -> Windows.Security.Credentials.WebAccount: ...
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
