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
import Windows.Devices.AllJoyn
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization
import Windows.Networking.Sockets
import Windows.Security.Credentials
import Windows.Security.Cryptography.Certificates
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AllJoynAboutData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynAboutData
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAboutData'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultAppName(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultAppName(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppNames(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_DateOfManufacture(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DateOfManufacture(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultDescription(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultDescription(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Descriptions(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_DefaultManufacturer(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultManufacturer(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Manufacturers(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_ModelNumber(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ModelNumber(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SupportUrl(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_SupportUrl(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AppId(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Guid: ...
    @winrt_mixinmethod
    def put_AppId(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Guid) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    DefaultAppName = property(get_DefaultAppName, put_DefaultAppName)
    AppNames = property(get_AppNames, None)
    DateOfManufacture = property(get_DateOfManufacture, put_DateOfManufacture)
    DefaultDescription = property(get_DefaultDescription, put_DefaultDescription)
    Descriptions = property(get_Descriptions, None)
    DefaultManufacturer = property(get_DefaultManufacturer, put_DefaultManufacturer)
    Manufacturers = property(get_Manufacturers, None)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    SoftwareVersion = property(get_SoftwareVersion, put_SoftwareVersion)
    SupportUrl = property(get_SupportUrl, put_SupportUrl)
    AppId = property(get_AppId, put_AppId)
class AllJoynAboutDataView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynAboutDataView
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAboutDataView'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Int32: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_AJSoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Guid: ...
    @winrt_mixinmethod
    def get_DateOfManufacture(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_DefaultLanguage(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HardwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelNumber(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedLanguages(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    @winrt_mixinmethod
    def get_SupportUrl(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AppName(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceName(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_classmethod
    def GetDataBySessionPortAsync(cls: Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics, uniqueName: WinRT_String, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_classmethod
    def GetDataBySessionPortWithLanguageAsync(cls: Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics, uniqueName: WinRT_String, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16, language: Windows.Globalization.Language) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    Status = property(get_Status, None)
    Properties = property(get_Properties, None)
    AJSoftwareVersion = property(get_AJSoftwareVersion, None)
    AppId = property(get_AppId, None)
    DateOfManufacture = property(get_DateOfManufacture, None)
    DefaultLanguage = property(get_DefaultLanguage, None)
    DeviceId = property(get_DeviceId, None)
    HardwareVersion = property(get_HardwareVersion, None)
    ModelNumber = property(get_ModelNumber, None)
    SoftwareVersion = property(get_SoftwareVersion, None)
    SupportedLanguages = property(get_SupportedLanguages, None)
    SupportUrl = property(get_SupportUrl, None)
    AppName = property(get_AppName, None)
    Description = property(get_Description, None)
    DeviceName = property(get_DeviceName, None)
    Manufacturer = property(get_Manufacturer, None)
class AllJoynAcceptSessionJoinerEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgsFactory, uniqueName: WinRT_String, sessionPort: UInt16, trafficType: Windows.Devices.AllJoyn.AllJoynTrafficType, proximity: Byte, acceptSessionJoiner: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner) -> Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionPort(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_TrafficType(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Windows.Devices.AllJoyn.AllJoynTrafficType: ...
    @winrt_mixinmethod
    def get_SamePhysicalNode(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SameNetwork(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def Accept(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Void: ...
    UniqueName = property(get_UniqueName, None)
    SessionPort = property(get_SessionPort, None)
    TrafficType = property(get_TrafficType, None)
    SamePhysicalNode = property(get_SamePhysicalNode, None)
    SameNetwork = property(get_SameNetwork, None)
class AllJoynAuthenticationCompleteEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAuthenticationCompleteEventArgs'
    @winrt_mixinmethod
    def get_AuthenticationMechanism(self: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_mixinmethod
    def get_PeerUniqueName(self: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> Boolean: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    Succeeded = property(get_Succeeded, None)
AllJoynAuthenticationMechanism = Int32
AllJoynAuthenticationMechanism_None: AllJoynAuthenticationMechanism = 0
AllJoynAuthenticationMechanism_SrpAnonymous: AllJoynAuthenticationMechanism = 1
AllJoynAuthenticationMechanism_SrpLogon: AllJoynAuthenticationMechanism = 2
AllJoynAuthenticationMechanism_EcdheNull: AllJoynAuthenticationMechanism = 3
AllJoynAuthenticationMechanism_EcdhePsk: AllJoynAuthenticationMechanism = 4
AllJoynAuthenticationMechanism_EcdheEcdsa: AllJoynAuthenticationMechanism = 5
AllJoynAuthenticationMechanism_EcdheSpeke: AllJoynAuthenticationMechanism = 6
class AllJoynBusAttachment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynBusAttachment
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusAttachment'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynBusAttachmentFactory, connectionSpecification: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_mixinmethod
    def get_AboutData(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Windows.Devices.AllJoyn.AllJoynAboutData: ...
    @winrt_mixinmethod
    def get_ConnectionSpecification(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_mixinmethod
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def PingAsync(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, uniqueName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def Connect(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Void: ...
    @winrt_mixinmethod
    def Disconnect(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynBusAttachmentStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AuthenticationMechanisms(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Windows.Foundation.Collections.IVector[Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]: ...
    @winrt_mixinmethod
    def add_CredentialsRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynCredentialsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CredentialsRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CredentialsVerificationRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynCredentialsVerificationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CredentialsVerificationRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AuthenticationComplete(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynAuthenticationCompleteEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AuthenticationComplete(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAboutDataAsync(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_mixinmethod
    def GetAboutDataWithLanguageAsync(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo, language: Windows.Globalization.Language) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_mixinmethod
    def add_AcceptSessionJoinerRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceptSessionJoinerRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionJoined(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionJoined(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_classmethod
    def GetWatcher(cls: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics, requiredInterfaces: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Enumeration.DeviceWatcher: ...
    AboutData = property(get_AboutData, None)
    ConnectionSpecification = property(get_ConnectionSpecification, None)
    State = property(get_State, None)
    UniqueName = property(get_UniqueName, None)
    AuthenticationMechanisms = property(get_AuthenticationMechanisms, None)
AllJoynBusAttachmentState = Int32
AllJoynBusAttachmentState_Disconnected: AllJoynBusAttachmentState = 0
AllJoynBusAttachmentState_Connecting: AllJoynBusAttachmentState = 1
AllJoynBusAttachmentState_Connected: AllJoynBusAttachmentState = 2
AllJoynBusAttachmentState_Disconnecting: AllJoynBusAttachmentState = 3
class AllJoynBusAttachmentStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusAttachmentStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs) -> Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs) -> Int32: ...
    State = property(get_State, None)
    Status = property(get_Status, None)
class AllJoynBusObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynBusObject
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusObject'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynBusObjectFactory, objectPath: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_factorymethod
    def CreateWithBusAttachment(cls: Windows.Devices.AllJoyn.IAllJoynBusObjectFactory, objectPath: WinRT_String, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment) -> Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Void: ...
    @winrt_mixinmethod
    def AddProducer(self: Windows.Devices.AllJoyn.IAllJoynBusObject, producer: Windows.Devices.AllJoyn.IAllJoynProducer) -> Void: ...
    @winrt_mixinmethod
    def get_BusAttachment(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Windows.Devices.AllJoyn.AllJoynSession: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.AllJoyn.IAllJoynBusObject, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusObject, Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.AllJoyn.IAllJoynBusObject, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    BusAttachment = property(get_BusAttachment, None)
    Session = property(get_Session, None)
class AllJoynBusObjectStoppedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgsFactory, status: Int32) -> Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class AllJoynCredentials(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynCredentials
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynCredentials'
    @winrt_mixinmethod
    def get_AuthenticationMechanism(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_mixinmethod
    def get_Certificate(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_Certificate(self: Windows.Devices.AllJoyn.IAllJoynCredentials, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_PasswordCredential(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_PasswordCredential(self: Windows.Devices.AllJoyn.IAllJoynCredentials, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Timeout(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Timeout(self: Windows.Devices.AllJoyn.IAllJoynCredentials, value: Windows.Foundation.TimeSpan) -> Void: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    Certificate = property(get_Certificate, put_Certificate)
    PasswordCredential = property(get_PasswordCredential, put_PasswordCredential)
    Timeout = property(get_Timeout, put_Timeout)
class AllJoynCredentialsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynCredentialsRequestedEventArgs'
    @winrt_mixinmethod
    def get_AttemptCount(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_Credentials(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> Windows.Devices.AllJoyn.AllJoynCredentials: ...
    @winrt_mixinmethod
    def get_PeerUniqueName(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RequestedUserName(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    AttemptCount = property(get_AttemptCount, None)
    Credentials = property(get_Credentials, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    RequestedUserName = property(get_RequestedUserName, None)
class AllJoynCredentialsVerificationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynCredentialsVerificationRequestedEventArgs'
    @winrt_mixinmethod
    def get_AuthenticationMechanism(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_mixinmethod
    def get_PeerUniqueName(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PeerCertificate(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_PeerCertificateErrorSeverity(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_PeerCertificateErrors(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_PeerIntermediateCertificates(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Accept(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    PeerCertificate = property(get_PeerCertificate, None)
    PeerCertificateErrorSeverity = property(get_PeerCertificateErrorSeverity, None)
    PeerCertificateErrors = property(get_PeerCertificateErrors, None)
    PeerIntermediateCertificates = property(get_PeerIntermediateCertificates, None)
class AllJoynMessageInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynMessageInfo
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynMessageInfo'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynMessageInfoFactory, senderUniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynMessageInfo: ...
    @winrt_mixinmethod
    def get_SenderUniqueName(self: Windows.Devices.AllJoyn.IAllJoynMessageInfo) -> WinRT_String: ...
    SenderUniqueName = property(get_SenderUniqueName, None)
class AllJoynProducerStoppedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgsFactory, status: Int32) -> Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class AllJoynServiceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynServiceInfo
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynServiceInfo'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynServiceInfoFactory, uniqueName: WinRT_String, objectPath: WinRT_String, sessionPort: UInt16) -> Windows.Devices.AllJoyn.AllJoynServiceInfo: ...
    @winrt_mixinmethod
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ObjectPath(self: Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionPort(self: Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> UInt16: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.AllJoyn.IAllJoynServiceInfoStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynServiceInfo]: ...
    UniqueName = property(get_UniqueName, None)
    ObjectPath = property(get_ObjectPath, None)
    SessionPort = property(get_SessionPort, None)
class AllJoynServiceInfoRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgsFactory, uniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class AllJoynSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynSession
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSession'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.AllJoyn.IAllJoynSession) -> Int32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynSession) -> Int32: ...
    @winrt_mixinmethod
    def RemoveMemberAsync(self: Windows.Devices.AllJoyn.IAllJoynSession, uniqueName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def add_MemberAdded(self: Windows.Devices.AllJoyn.IAllJoynSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynSession, Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MemberAdded(self: Windows.Devices.AllJoyn.IAllJoynSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MemberRemoved(self: Windows.Devices.AllJoyn.IAllJoynSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynSession, Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MemberRemoved(self: Windows.Devices.AllJoyn.IAllJoynSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Lost(self: Windows.Devices.AllJoyn.IAllJoynSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynSession, Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Lost(self: Windows.Devices.AllJoyn.IAllJoynSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetFromServiceInfoAsync(cls: Windows.Devices.AllJoyn.IAllJoynSessionStatics, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynSession]: ...
    @winrt_classmethod
    def GetFromServiceInfoAndBusAttachmentAsync(cls: Windows.Devices.AllJoyn.IAllJoynSessionStatics, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynSession]: ...
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class AllJoynSessionJoinedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgsFactory, session: Windows.Devices.AllJoyn.AllJoynSession) -> Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs) -> Windows.Devices.AllJoyn.AllJoynSession: ...
    Session = property(get_Session, None)
class AllJoynSessionLostEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgsFactory, reason: Windows.Devices.AllJoyn.AllJoynSessionLostReason) -> Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs) -> Windows.Devices.AllJoyn.AllJoynSessionLostReason: ...
    Reason = property(get_Reason, None)
AllJoynSessionLostReason = Int32
AllJoynSessionLostReason_None: AllJoynSessionLostReason = 0
AllJoynSessionLostReason_ProducerLeftSession: AllJoynSessionLostReason = 1
AllJoynSessionLostReason_ProducerClosedAbruptly: AllJoynSessionLostReason = 2
AllJoynSessionLostReason_RemovedByProducer: AllJoynSessionLostReason = 3
AllJoynSessionLostReason_LinkTimeout: AllJoynSessionLostReason = 4
AllJoynSessionLostReason_Other: AllJoynSessionLostReason = 5
class AllJoynSessionMemberAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgsFactory, uniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class AllJoynSessionMemberRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgsFactory, uniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class _AllJoynStatus_Meta_(ComPtr.__class__):
    pass
class AllJoynStatus(ComPtr, metaclass=_AllJoynStatus_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynStatus'
    @winrt_classmethod
    def get_Ok(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_Fail(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_OperationTimedOut(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_OtherEndClosed(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_ConnectionRefused(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_AuthenticationFailed(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_AuthenticationRejectedByUser(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_SslConnectFailed(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_SslIdentityVerificationFailed(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InsufficientSecurity(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument1(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument2(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument3(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument4(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument5(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument6(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument7(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument8(cls: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    _AllJoynStatus_Meta_.Ok = property(get_Ok.__wrapped__, None)
    _AllJoynStatus_Meta_.Fail = property(get_Fail.__wrapped__, None)
    _AllJoynStatus_Meta_.OperationTimedOut = property(get_OperationTimedOut.__wrapped__, None)
    _AllJoynStatus_Meta_.OtherEndClosed = property(get_OtherEndClosed.__wrapped__, None)
    _AllJoynStatus_Meta_.ConnectionRefused = property(get_ConnectionRefused.__wrapped__, None)
    _AllJoynStatus_Meta_.AuthenticationFailed = property(get_AuthenticationFailed.__wrapped__, None)
    _AllJoynStatus_Meta_.AuthenticationRejectedByUser = property(get_AuthenticationRejectedByUser.__wrapped__, None)
    _AllJoynStatus_Meta_.SslConnectFailed = property(get_SslConnectFailed.__wrapped__, None)
    _AllJoynStatus_Meta_.SslIdentityVerificationFailed = property(get_SslIdentityVerificationFailed.__wrapped__, None)
    _AllJoynStatus_Meta_.InsufficientSecurity = property(get_InsufficientSecurity.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument1 = property(get_InvalidArgument1.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument2 = property(get_InvalidArgument2.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument3 = property(get_InvalidArgument3.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument4 = property(get_InvalidArgument4.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument5 = property(get_InvalidArgument5.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument6 = property(get_InvalidArgument6.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument7 = property(get_InvalidArgument7.__wrapped__, None)
    _AllJoynStatus_Meta_.InvalidArgument8 = property(get_InvalidArgument8.__wrapped__, None)
AllJoynTrafficType = Int32
AllJoynTrafficType_Unknown: AllJoynTrafficType = 0
AllJoynTrafficType_Messages: AllJoynTrafficType = 1
AllJoynTrafficType_RawUnreliable: AllJoynTrafficType = 2
AllJoynTrafficType_RawReliable: AllJoynTrafficType = 4
class AllJoynWatcherStoppedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgsFactory, status: Int32) -> Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynAboutData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAboutData'
    _iid_ = Guid('{e5a9bf00-1fa2-4839-93ef-f9df404890f7}')
    @winrt_commethod(6)
    def get_IsEnabled(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultAppName(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DefaultAppName(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AppNames(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(11)
    def get_DateOfManufacture(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(12)
    def put_DateOfManufacture(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(13)
    def get_DefaultDescription(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_DefaultDescription(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Descriptions(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(16)
    def get_DefaultManufacturer(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_DefaultManufacturer(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_Manufacturers(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(19)
    def get_ModelNumber(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_ModelNumber(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_SoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_commethod(22)
    def put_SoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_commethod(23)
    def get_SupportUrl(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Windows.Foundation.Uri: ...
    @winrt_commethod(24)
    def put_SupportUrl(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(25)
    def get_AppId(self: Windows.Devices.AllJoyn.IAllJoynAboutData) -> Guid: ...
    @winrt_commethod(26)
    def put_AppId(self: Windows.Devices.AllJoyn.IAllJoynAboutData, value: Guid) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    DefaultAppName = property(get_DefaultAppName, put_DefaultAppName)
    AppNames = property(get_AppNames, None)
    DateOfManufacture = property(get_DateOfManufacture, put_DateOfManufacture)
    DefaultDescription = property(get_DefaultDescription, put_DefaultDescription)
    Descriptions = property(get_Descriptions, None)
    DefaultManufacturer = property(get_DefaultManufacturer, put_DefaultManufacturer)
    Manufacturers = property(get_Manufacturers, None)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    SoftwareVersion = property(get_SoftwareVersion, put_SoftwareVersion)
    SupportUrl = property(get_SupportUrl, put_SupportUrl)
    AppId = property(get_AppId, put_AppId)
class IAllJoynAboutDataView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAboutDataView'
    _iid_ = Guid('{6823111f-6212-4934-9c48-e19ca4984288}')
    @winrt_commethod(6)
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Int32: ...
    @winrt_commethod(7)
    def get_Properties(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(8)
    def get_AJSoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AppId(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Guid: ...
    @winrt_commethod(10)
    def get_DateOfManufacture(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def get_DefaultLanguage(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Globalization.Language: ...
    @winrt_commethod(12)
    def get_DeviceId(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_HardwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_ModelNumber(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_SoftwareVersion(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_SupportedLanguages(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    @winrt_commethod(17)
    def get_SupportUrl(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Windows.Foundation.Uri: ...
    @winrt_commethod(18)
    def get_AppName(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Description(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_DeviceName(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Manufacturer(self: Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    Status = property(get_Status, None)
    Properties = property(get_Properties, None)
    AJSoftwareVersion = property(get_AJSoftwareVersion, None)
    AppId = property(get_AppId, None)
    DateOfManufacture = property(get_DateOfManufacture, None)
    DefaultLanguage = property(get_DefaultLanguage, None)
    DeviceId = property(get_DeviceId, None)
    HardwareVersion = property(get_HardwareVersion, None)
    ModelNumber = property(get_ModelNumber, None)
    SoftwareVersion = property(get_SoftwareVersion, None)
    SupportedLanguages = property(get_SupportedLanguages, None)
    SupportUrl = property(get_SupportUrl, None)
    AppName = property(get_AppName, None)
    Description = property(get_Description, None)
    DeviceName = property(get_DeviceName, None)
    Manufacturer = property(get_Manufacturer, None)
class IAllJoynAboutDataViewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics'
    _iid_ = Guid('{57edb688-0c5e-416e-88b5-39b32d25c47d}')
    @winrt_commethod(6)
    def GetDataBySessionPortAsync(self: Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics, uniqueName: WinRT_String, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_commethod(7)
    def GetDataBySessionPortWithLanguageAsync(self: Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics, uniqueName: WinRT_String, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16, language: Windows.Globalization.Language) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
class IAllJoynAcceptSessionJoiner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner'
    _iid_ = Guid('{4da817d2-cd1d-4023-a7c4-16def89c28df}')
    @winrt_commethod(6)
    def Accept(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner) -> Void: ...
class IAllJoynAcceptSessionJoinerEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs'
    _iid_ = Guid('{4efb5365-3e8a-4257-8f10-539ce0d56c0f}')
    @winrt_commethod(6)
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SessionPort(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> UInt16: ...
    @winrt_commethod(8)
    def get_TrafficType(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Windows.Devices.AllJoyn.AllJoynTrafficType: ...
    @winrt_commethod(9)
    def get_SamePhysicalNode(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Boolean: ...
    @winrt_commethod(10)
    def get_SameNetwork(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Boolean: ...
    @winrt_commethod(11)
    def Accept(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Void: ...
    UniqueName = property(get_UniqueName, None)
    SessionPort = property(get_SessionPort, None)
    TrafficType = property(get_TrafficType, None)
    SamePhysicalNode = property(get_SamePhysicalNode, None)
    SameNetwork = property(get_SameNetwork, None)
class IAllJoynAcceptSessionJoinerEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgsFactory'
    _iid_ = Guid('{b4435bc0-6145-429e-84db-d5bfe772b14f}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgsFactory, uniqueName: WinRT_String, sessionPort: UInt16, trafficType: Windows.Devices.AllJoyn.AllJoynTrafficType, proximity: Byte, acceptSessionJoiner: Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner) -> Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs: ...
class IAllJoynAuthenticationCompleteEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs'
    _iid_ = Guid('{97b4701c-15dc-4b53-b6a4-7d134300d7bf}')
    @winrt_commethod(6)
    def get_AuthenticationMechanism(self: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_commethod(7)
    def get_PeerUniqueName(self: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Succeeded(self: Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> Boolean: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    Succeeded = property(get_Succeeded, None)
class IAllJoynBusAttachment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachment'
    _iid_ = Guid('{f309f153-1eed-42c3-a20e-436d41fe62f6}')
    @winrt_commethod(6)
    def get_AboutData(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Windows.Devices.AllJoyn.AllJoynAboutData: ...
    @winrt_commethod(7)
    def get_ConnectionSpecification(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_State(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_commethod(9)
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> WinRT_String: ...
    @winrt_commethod(10)
    def PingAsync(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, uniqueName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(11)
    def Connect(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Void: ...
    @winrt_commethod(12)
    def Disconnect(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Void: ...
    @winrt_commethod(13)
    def add_StateChanged(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynBusAttachmentStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_StateChanged(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def get_AuthenticationMechanisms(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Windows.Foundation.Collections.IVector[Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]: ...
    @winrt_commethod(16)
    def add_CredentialsRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynCredentialsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_CredentialsRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_CredentialsVerificationRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynCredentialsVerificationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_CredentialsVerificationRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_AuthenticationComplete(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynAuthenticationCompleteEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_AuthenticationComplete(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AboutData = property(get_AboutData, None)
    ConnectionSpecification = property(get_ConnectionSpecification, None)
    State = property(get_State, None)
    UniqueName = property(get_UniqueName, None)
    AuthenticationMechanisms = property(get_AuthenticationMechanisms, None)
class IAllJoynBusAttachment2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachment2'
    _iid_ = Guid('{3474cb1e-2368-43b2-b43e-6a3ac1278d98}')
    @winrt_commethod(6)
    def GetAboutDataAsync(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_commethod(7)
    def GetAboutDataWithLanguageAsync(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo, language: Windows.Globalization.Language) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_commethod(8)
    def add_AcceptSessionJoinerRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AcceptSessionJoinerRequested(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SessionJoined(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusAttachment, Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SessionJoined(self: Windows.Devices.AllJoyn.IAllJoynBusAttachment2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IAllJoynBusAttachmentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachmentFactory'
    _iid_ = Guid('{642ef1a4-ad85-4ddf-90ae-604452b22288}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentFactory, connectionSpecification: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
class IAllJoynBusAttachmentStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs'
    _iid_ = Guid('{d82e75f4-c02a-41ec-a8d5-eab1558953aa}')
    @winrt_commethod(6)
    def get_State(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs) -> Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_commethod(7)
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs) -> Int32: ...
    State = property(get_State, None)
    Status = property(get_Status, None)
class IAllJoynBusAttachmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics'
    _iid_ = Guid('{839d4d3d-1051-40d7-872a-8d0141115b1f}')
    @winrt_commethod(6)
    def GetDefault(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_commethod(7)
    def GetWatcher(self: Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics, requiredInterfaces: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Enumeration.DeviceWatcher: ...
class IAllJoynBusObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObject'
    _iid_ = Guid('{e8fd825e-f73a-490c-8804-04e026643047}')
    @winrt_commethod(6)
    def Start(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Void: ...
    @winrt_commethod(7)
    def Stop(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Void: ...
    @winrt_commethod(8)
    def AddProducer(self: Windows.Devices.AllJoyn.IAllJoynBusObject, producer: Windows.Devices.AllJoyn.IAllJoynProducer) -> Void: ...
    @winrt_commethod(9)
    def get_BusAttachment(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_commethod(10)
    def get_Session(self: Windows.Devices.AllJoyn.IAllJoynBusObject) -> Windows.Devices.AllJoyn.AllJoynSession: ...
    @winrt_commethod(11)
    def add_Stopped(self: Windows.Devices.AllJoyn.IAllJoynBusObject, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynBusObject, Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Stopped(self: Windows.Devices.AllJoyn.IAllJoynBusObject, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    BusAttachment = property(get_BusAttachment, None)
    Session = property(get_Session, None)
class IAllJoynBusObjectFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObjectFactory'
    _iid_ = Guid('{2c2f9f0b-8e02-4f9c-ac27-ea6dad5d3b50}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynBusObjectFactory, objectPath: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_commethod(7)
    def CreateWithBusAttachment(self: Windows.Devices.AllJoyn.IAllJoynBusObjectFactory, objectPath: WinRT_String, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment) -> Windows.Devices.AllJoyn.AllJoynBusObject: ...
class IAllJoynBusObjectStoppedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs'
    _iid_ = Guid('{de102115-ef8e-4d42-b93b-a2ae74519766}')
    @winrt_commethod(6)
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynBusObjectStoppedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgsFactory'
    _iid_ = Guid('{6b22fd48-d0a3-4255-953a-4772b4028073}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgsFactory, status: Int32) -> Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs: ...
class IAllJoynCredentials(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynCredentials'
    _iid_ = Guid('{824650f2-a190-40b1-abab-349ec244dfaa}')
    @winrt_commethod(6)
    def get_AuthenticationMechanism(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_commethod(7)
    def get_Certificate(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(8)
    def put_Certificate(self: Windows.Devices.AllJoyn.IAllJoynCredentials, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(9)
    def get_PasswordCredential(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(10)
    def put_PasswordCredential(self: Windows.Devices.AllJoyn.IAllJoynCredentials, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(11)
    def get_Timeout(self: Windows.Devices.AllJoyn.IAllJoynCredentials) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def put_Timeout(self: Windows.Devices.AllJoyn.IAllJoynCredentials, value: Windows.Foundation.TimeSpan) -> Void: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    Certificate = property(get_Certificate, put_Certificate)
    PasswordCredential = property(get_PasswordCredential, put_PasswordCredential)
    Timeout = property(get_Timeout, put_Timeout)
class IAllJoynCredentialsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs'
    _iid_ = Guid('{6a87e34e-b069-4b80-9e1a-41bc837c65d2}')
    @winrt_commethod(6)
    def get_AttemptCount(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> UInt16: ...
    @winrt_commethod(7)
    def get_Credentials(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> Windows.Devices.AllJoyn.AllJoynCredentials: ...
    @winrt_commethod(8)
    def get_PeerUniqueName(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_RequestedUserName(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeferral(self: Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    AttemptCount = property(get_AttemptCount, None)
    Credentials = property(get_Credentials, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    RequestedUserName = property(get_RequestedUserName, None)
class IAllJoynCredentialsVerificationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs'
    _iid_ = Guid('{800a7612-b805-44af-a2e1-792ab655a2d0}')
    @winrt_commethod(6)
    def get_AuthenticationMechanism(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_commethod(7)
    def get_PeerUniqueName(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PeerCertificate(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def get_PeerCertificateErrorSeverity(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(10)
    def get_PeerCertificateErrors(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(11)
    def get_PeerIntermediateCertificates(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(12)
    def Accept(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self: Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    PeerCertificate = property(get_PeerCertificate, None)
    PeerCertificateErrorSeverity = property(get_PeerCertificateErrorSeverity, None)
    PeerCertificateErrors = property(get_PeerCertificateErrors, None)
    PeerIntermediateCertificates = property(get_PeerIntermediateCertificates, None)
class IAllJoynMessageInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynMessageInfo'
    _iid_ = Guid('{ff2b0127-2c12-4859-aa3a-c74461ee814c}')
    @winrt_commethod(6)
    def get_SenderUniqueName(self: Windows.Devices.AllJoyn.IAllJoynMessageInfo) -> WinRT_String: ...
    SenderUniqueName = property(get_SenderUniqueName, None)
class IAllJoynMessageInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynMessageInfoFactory'
    _iid_ = Guid('{34664c2a-8289-43d4-b4a8-3f4de359f043}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynMessageInfoFactory, senderUniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynMessageInfo: ...
class IAllJoynProducer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynProducer'
    _iid_ = Guid('{9d084679-469b-495a-a710-ac50f123069f}')
    @winrt_commethod(6)
    def SetBusObject(self: Windows.Devices.AllJoyn.IAllJoynProducer, busObject: Windows.Devices.AllJoyn.AllJoynBusObject) -> Void: ...
class IAllJoynProducerStoppedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs'
    _iid_ = Guid('{51309770-4937-492d-8080-236439987ceb}')
    @winrt_commethod(6)
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynProducerStoppedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgsFactory'
    _iid_ = Guid('{56529961-b219-4d6e-9f78-fa3f99fa8fe5}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgsFactory, status: Int32) -> Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs: ...
class IAllJoynServiceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfo'
    _iid_ = Guid('{4cbe8209-b93e-4182-999b-ddd000f9c575}')
    @winrt_commethod(6)
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ObjectPath(self: Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SessionPort(self: Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> UInt16: ...
    UniqueName = property(get_UniqueName, None)
    ObjectPath = property(get_ObjectPath, None)
    SessionPort = property(get_SessionPort, None)
class IAllJoynServiceInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoFactory'
    _iid_ = Guid('{7581dabd-fe03-4f4b-94a4-f02fdcbd11b8}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynServiceInfoFactory, uniqueName: WinRT_String, objectPath: WinRT_String, sessionPort: UInt16) -> Windows.Devices.AllJoyn.AllJoynServiceInfo: ...
class IAllJoynServiceInfoRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs'
    _iid_ = Guid('{3057a95f-1d3f-41f3-8969-e32792627396}')
    @winrt_commethod(6)
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class IAllJoynServiceInfoRemovedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgsFactory'
    _iid_ = Guid('{0dbf8627-9aff-4955-9227-6953baf41569}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgsFactory, uniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs: ...
class IAllJoynServiceInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoStatics'
    _iid_ = Guid('{5678570a-603a-49fc-b750-0ef13609213c}')
    @winrt_commethod(6)
    def FromIdAsync(self: Windows.Devices.AllJoyn.IAllJoynServiceInfoStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynServiceInfo]: ...
class IAllJoynSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSession'
    _iid_ = Guid('{e8d11b0c-c0d4-406c-88a9-a93efa85d4b1}')
    @winrt_commethod(6)
    def get_Id(self: Windows.Devices.AllJoyn.IAllJoynSession) -> Int32: ...
    @winrt_commethod(7)
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynSession) -> Int32: ...
    @winrt_commethod(8)
    def RemoveMemberAsync(self: Windows.Devices.AllJoyn.IAllJoynSession, uniqueName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(9)
    def add_MemberAdded(self: Windows.Devices.AllJoyn.IAllJoynSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynSession, Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_MemberAdded(self: Windows.Devices.AllJoyn.IAllJoynSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_MemberRemoved(self: Windows.Devices.AllJoyn.IAllJoynSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynSession, Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_MemberRemoved(self: Windows.Devices.AllJoyn.IAllJoynSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Lost(self: Windows.Devices.AllJoyn.IAllJoynSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.AllJoyn.AllJoynSession, Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Lost(self: Windows.Devices.AllJoyn.IAllJoynSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class IAllJoynSessionJoinedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs'
    _iid_ = Guid('{9e9f5bd0-b5d7-47c5-8dab-b040cc192871}')
    @winrt_commethod(6)
    def get_Session(self: Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs) -> Windows.Devices.AllJoyn.AllJoynSession: ...
    Session = property(get_Session, None)
class IAllJoynSessionJoinedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgsFactory'
    _iid_ = Guid('{6824d689-d6cb-4d9e-a09e-35806870b17f}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgsFactory, session: Windows.Devices.AllJoyn.AllJoynSession) -> Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs: ...
class IAllJoynSessionLostEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs'
    _iid_ = Guid('{e766a48a-8bb8-4954-ae67-d2fa43d1f96b}')
    @winrt_commethod(6)
    def get_Reason(self: Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs) -> Windows.Devices.AllJoyn.AllJoynSessionLostReason: ...
    Reason = property(get_Reason, None)
class IAllJoynSessionLostEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgsFactory'
    _iid_ = Guid('{13bbfd32-d2f4-49c9-980e-2805e13586b1}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgsFactory, reason: Windows.Devices.AllJoyn.AllJoynSessionLostReason) -> Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs: ...
class IAllJoynSessionMemberAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs'
    _iid_ = Guid('{49a2798a-0dd1-46c1-9cd6-27190e503a5e}')
    @winrt_commethod(6)
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class IAllJoynSessionMemberAddedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgsFactory'
    _iid_ = Guid('{341de352-1d33-40a1-a1d3-e5777020e1f1}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgsFactory, uniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs: ...
class IAllJoynSessionMemberRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs'
    _iid_ = Guid('{409a219f-aa4a-4893-b430-baa1b63c6219}')
    @winrt_commethod(6)
    def get_UniqueName(self: Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class IAllJoynSessionMemberRemovedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgsFactory'
    _iid_ = Guid('{c4d355e8-42b8-4b67-b757-d0cfcad59280}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgsFactory, uniqueName: WinRT_String) -> Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs: ...
class IAllJoynSessionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionStatics'
    _iid_ = Guid('{9e05d604-a06c-46d4-b46c-0b0b54105b44}')
    @winrt_commethod(6)
    def GetFromServiceInfoAsync(self: Windows.Devices.AllJoyn.IAllJoynSessionStatics, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynSession]: ...
    @winrt_commethod(7)
    def GetFromServiceInfoAndBusAttachmentAsync(self: Windows.Devices.AllJoyn.IAllJoynSessionStatics, serviceInfo: Windows.Devices.AllJoyn.AllJoynServiceInfo, busAttachment: Windows.Devices.AllJoyn.AllJoynBusAttachment) -> Windows.Foundation.IAsyncOperation[Windows.Devices.AllJoyn.AllJoynSession]: ...
class IAllJoynStatusStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynStatusStatics'
    _iid_ = Guid('{d0b7a17e-0d29-4da9-8ac6-54c554bedbc5}')
    @winrt_commethod(6)
    def get_Ok(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(7)
    def get_Fail(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(8)
    def get_OperationTimedOut(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(9)
    def get_OtherEndClosed(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(10)
    def get_ConnectionRefused(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(11)
    def get_AuthenticationFailed(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(12)
    def get_AuthenticationRejectedByUser(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(13)
    def get_SslConnectFailed(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(14)
    def get_SslIdentityVerificationFailed(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(15)
    def get_InsufficientSecurity(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(16)
    def get_InvalidArgument1(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(17)
    def get_InvalidArgument2(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(18)
    def get_InvalidArgument3(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(19)
    def get_InvalidArgument4(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(20)
    def get_InvalidArgument5(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(21)
    def get_InvalidArgument6(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(22)
    def get_InvalidArgument7(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_commethod(23)
    def get_InvalidArgument8(self: Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    Ok = property(get_Ok, None)
    Fail = property(get_Fail, None)
    OperationTimedOut = property(get_OperationTimedOut, None)
    OtherEndClosed = property(get_OtherEndClosed, None)
    ConnectionRefused = property(get_ConnectionRefused, None)
    AuthenticationFailed = property(get_AuthenticationFailed, None)
    AuthenticationRejectedByUser = property(get_AuthenticationRejectedByUser, None)
    SslConnectFailed = property(get_SslConnectFailed, None)
    SslIdentityVerificationFailed = property(get_SslIdentityVerificationFailed, None)
    InsufficientSecurity = property(get_InsufficientSecurity, None)
    InvalidArgument1 = property(get_InvalidArgument1, None)
    InvalidArgument2 = property(get_InvalidArgument2, None)
    InvalidArgument3 = property(get_InvalidArgument3, None)
    InvalidArgument4 = property(get_InvalidArgument4, None)
    InvalidArgument5 = property(get_InvalidArgument5, None)
    InvalidArgument6 = property(get_InvalidArgument6, None)
    InvalidArgument7 = property(get_InvalidArgument7, None)
    InvalidArgument8 = property(get_InvalidArgument8, None)
class IAllJoynWatcherStoppedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs'
    _iid_ = Guid('{c9fca03b-701d-4aa8-97dd-a2bb0a8f5fa3}')
    @winrt_commethod(6)
    def get_Status(self: Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynWatcherStoppedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgsFactory'
    _iid_ = Guid('{878fa5a8-2d50-47e1-904a-20bf0d48c782}')
    @winrt_commethod(6)
    def Create(self: Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgsFactory, status: Int32) -> Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs: ...
make_head(_module, 'AllJoynAboutData')
make_head(_module, 'AllJoynAboutDataView')
make_head(_module, 'AllJoynAcceptSessionJoinerEventArgs')
make_head(_module, 'AllJoynAuthenticationCompleteEventArgs')
make_head(_module, 'AllJoynBusAttachment')
make_head(_module, 'AllJoynBusAttachmentStateChangedEventArgs')
make_head(_module, 'AllJoynBusObject')
make_head(_module, 'AllJoynBusObjectStoppedEventArgs')
make_head(_module, 'AllJoynCredentials')
make_head(_module, 'AllJoynCredentialsRequestedEventArgs')
make_head(_module, 'AllJoynCredentialsVerificationRequestedEventArgs')
make_head(_module, 'AllJoynMessageInfo')
make_head(_module, 'AllJoynProducerStoppedEventArgs')
make_head(_module, 'AllJoynServiceInfo')
make_head(_module, 'AllJoynServiceInfoRemovedEventArgs')
make_head(_module, 'AllJoynSession')
make_head(_module, 'AllJoynSessionJoinedEventArgs')
make_head(_module, 'AllJoynSessionLostEventArgs')
make_head(_module, 'AllJoynSessionMemberAddedEventArgs')
make_head(_module, 'AllJoynSessionMemberRemovedEventArgs')
make_head(_module, 'AllJoynStatus')
make_head(_module, 'AllJoynWatcherStoppedEventArgs')
make_head(_module, 'IAllJoynAboutData')
make_head(_module, 'IAllJoynAboutDataView')
make_head(_module, 'IAllJoynAboutDataViewStatics')
make_head(_module, 'IAllJoynAcceptSessionJoiner')
make_head(_module, 'IAllJoynAcceptSessionJoinerEventArgs')
make_head(_module, 'IAllJoynAcceptSessionJoinerEventArgsFactory')
make_head(_module, 'IAllJoynAuthenticationCompleteEventArgs')
make_head(_module, 'IAllJoynBusAttachment')
make_head(_module, 'IAllJoynBusAttachment2')
make_head(_module, 'IAllJoynBusAttachmentFactory')
make_head(_module, 'IAllJoynBusAttachmentStateChangedEventArgs')
make_head(_module, 'IAllJoynBusAttachmentStatics')
make_head(_module, 'IAllJoynBusObject')
make_head(_module, 'IAllJoynBusObjectFactory')
make_head(_module, 'IAllJoynBusObjectStoppedEventArgs')
make_head(_module, 'IAllJoynBusObjectStoppedEventArgsFactory')
make_head(_module, 'IAllJoynCredentials')
make_head(_module, 'IAllJoynCredentialsRequestedEventArgs')
make_head(_module, 'IAllJoynCredentialsVerificationRequestedEventArgs')
make_head(_module, 'IAllJoynMessageInfo')
make_head(_module, 'IAllJoynMessageInfoFactory')
make_head(_module, 'IAllJoynProducer')
make_head(_module, 'IAllJoynProducerStoppedEventArgs')
make_head(_module, 'IAllJoynProducerStoppedEventArgsFactory')
make_head(_module, 'IAllJoynServiceInfo')
make_head(_module, 'IAllJoynServiceInfoFactory')
make_head(_module, 'IAllJoynServiceInfoRemovedEventArgs')
make_head(_module, 'IAllJoynServiceInfoRemovedEventArgsFactory')
make_head(_module, 'IAllJoynServiceInfoStatics')
make_head(_module, 'IAllJoynSession')
make_head(_module, 'IAllJoynSessionJoinedEventArgs')
make_head(_module, 'IAllJoynSessionJoinedEventArgsFactory')
make_head(_module, 'IAllJoynSessionLostEventArgs')
make_head(_module, 'IAllJoynSessionLostEventArgsFactory')
make_head(_module, 'IAllJoynSessionMemberAddedEventArgs')
make_head(_module, 'IAllJoynSessionMemberAddedEventArgsFactory')
make_head(_module, 'IAllJoynSessionMemberRemovedEventArgs')
make_head(_module, 'IAllJoynSessionMemberRemovedEventArgsFactory')
make_head(_module, 'IAllJoynSessionStatics')
make_head(_module, 'IAllJoynStatusStatics')
make_head(_module, 'IAllJoynWatcherStoppedEventArgs')
make_head(_module, 'IAllJoynWatcherStoppedEventArgsFactory')
