from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import FillArray, Generic, K, MulticastDelegate, PassArray, ReceiveArray, T, TProgress, TResult, TSender, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.AllJoyn
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.Networking.Sockets
import win32more.Windows.Security.Credentials
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Win32.System.WinRT
class AllJoynAboutData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAboutData'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultAppName(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultAppName(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppNames(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_DateOfManufacture(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DateOfManufacture(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultDescription(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultDescription(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Descriptions(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_DefaultManufacturer(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultManufacturer(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Manufacturers(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_ModelNumber(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ModelNumber(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SoftwareVersion(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SoftwareVersion(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SupportUrl(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_SupportUrl(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData) -> Guid: ...
    @winrt_mixinmethod
    def put_AppId(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutData, value: Guid) -> Void: ...
    AppId = property(get_AppId, put_AppId)
    AppNames = property(get_AppNames, None)
    DateOfManufacture = property(get_DateOfManufacture, put_DateOfManufacture)
    DefaultAppName = property(get_DefaultAppName, put_DefaultAppName)
    DefaultDescription = property(get_DefaultDescription, put_DefaultDescription)
    DefaultManufacturer = property(get_DefaultManufacturer, put_DefaultManufacturer)
    Descriptions = property(get_Descriptions, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Manufacturers = property(get_Manufacturers, None)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    SoftwareVersion = property(get_SoftwareVersion, put_SoftwareVersion)
    SupportUrl = property(get_SupportUrl, put_SupportUrl)
class AllJoynAboutDataView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAboutDataView'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Int32: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_AJSoftwareVersion(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> Guid: ...
    @winrt_mixinmethod
    def get_DateOfManufacture(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_DefaultLanguage(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> win32more.Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HardwareVersion(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelNumber(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SoftwareVersion(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedLanguages(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    @winrt_mixinmethod
    def get_SupportUrl(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AppName(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceName(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataView) -> WinRT_String: ...
    @winrt_classmethod
    def GetDataBySessionPortAsync(cls: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics, uniqueName: WinRT_String, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_classmethod
    def GetDataBySessionPortWithLanguageAsync(cls: win32more.Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics, uniqueName: WinRT_String, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    AJSoftwareVersion = property(get_AJSoftwareVersion, None)
    AppId = property(get_AppId, None)
    AppName = property(get_AppName, None)
    DateOfManufacture = property(get_DateOfManufacture, None)
    DefaultLanguage = property(get_DefaultLanguage, None)
    Description = property(get_Description, None)
    DeviceId = property(get_DeviceId, None)
    DeviceName = property(get_DeviceName, None)
    HardwareVersion = property(get_HardwareVersion, None)
    Manufacturer = property(get_Manufacturer, None)
    ModelNumber = property(get_ModelNumber, None)
    Properties = property(get_Properties, None)
    SoftwareVersion = property(get_SoftwareVersion, None)
    Status = property(get_Status, None)
    SupportUrl = property(get_SupportUrl, None)
    SupportedLanguages = property(get_SupportedLanguages, None)
class AllJoynAcceptSessionJoinerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 5:
            return win32more.Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgsFactory, uniqueName: WinRT_String, sessionPort: UInt16, trafficType: win32more.Windows.Devices.AllJoyn.AllJoynTrafficType, proximity: Byte, acceptSessionJoiner: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner) -> win32more.Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionPort(self: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_TrafficType(self: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynTrafficType: ...
    @winrt_mixinmethod
    def get_SamePhysicalNode(self: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SameNetwork(self: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def Accept(self: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs) -> Void: ...
    SameNetwork = property(get_SameNetwork, None)
    SamePhysicalNode = property(get_SamePhysicalNode, None)
    SessionPort = property(get_SessionPort, None)
    TrafficType = property(get_TrafficType, None)
    UniqueName = property(get_UniqueName, None)
class AllJoynAuthenticationCompleteEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynAuthenticationCompleteEventArgs'
    @winrt_mixinmethod
    def get_AuthenticationMechanism(self: win32more.Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_mixinmethod
    def get_PeerUniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs) -> Boolean: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    Succeeded = property(get_Succeeded, None)
class AllJoynAuthenticationMechanism(Enum, Int32):
    None_ = 0
    SrpAnonymous = 1
    SrpLogon = 2
    EcdheNull = 3
    EcdhePsk = 4
    EcdheEcdsa = 5
    EcdheSpeke = 6
class AllJoynBusAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusAttachment'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment.CreateInstance(*args)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachmentFactory, connectionSpecification: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_mixinmethod
    def get_AboutData(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> win32more.Windows.Devices.AllJoyn.AllJoynAboutData: ...
    @winrt_mixinmethod
    def get_ConnectionSpecification(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_mixinmethod
    def get_UniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> WinRT_String: ...
    @winrt_mixinmethod
    def PingAsync(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, uniqueName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def Connect(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Void: ...
    @winrt_mixinmethod
    def Disconnect(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynBusAttachmentStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AuthenticationMechanisms(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]: ...
    @winrt_mixinmethod
    def add_CredentialsRequested(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynCredentialsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CredentialsRequested(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CredentialsVerificationRequested(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynCredentialsVerificationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CredentialsVerificationRequested(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AuthenticationComplete(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationCompleteEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AuthenticationComplete(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAboutDataAsync(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment2, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_mixinmethod
    def GetAboutDataWithLanguageAsync(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment2, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_mixinmethod
    def add_AcceptSessionJoinerRequested(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceptSessionJoinerRequested(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionJoined(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionJoined(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachment2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_classmethod
    def GetWatcher(cls: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics, requiredInterfaces: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
    AboutData = property(get_AboutData, None)
    AuthenticationMechanisms = property(get_AuthenticationMechanisms, None)
    ConnectionSpecification = property(get_ConnectionSpecification, None)
    State = property(get_State, None)
    UniqueName = property(get_UniqueName, None)
    StateChanged = event()
    CredentialsRequested = event()
    CredentialsVerificationRequested = event()
    AuthenticationComplete = event()
    AcceptSessionJoinerRequested = event()
    SessionJoined = event()
class AllJoynBusAttachmentState(Enum, Int32):
    Disconnected = 0
    Connecting = 1
    Connected = 2
    Disconnecting = 3
class AllJoynBusAttachmentStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusAttachmentStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs) -> Int32: ...
    State = property(get_State, None)
    Status = property(get_Status, None)
class AllJoynBusObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusObject'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Devices.AllJoyn.AllJoynBusObject.CreateInstance(*args)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynBusObject.Create(*args)
        elif len(args) == 2:
            return win32more.Windows.Devices.AllJoyn.AllJoynBusObject.CreateWithBusAttachment(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynBusObjectFactory, objectPath: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_factorymethod
    def CreateWithBusAttachment(cls: win32more.Windows.Devices.AllJoyn.IAllJoynBusObjectFactory, objectPath: WinRT_String, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject) -> Void: ...
    @winrt_mixinmethod
    def AddProducer(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject, producer: win32more.Windows.Devices.AllJoyn.IAllJoynProducer) -> Void: ...
    @winrt_mixinmethod
    def get_BusAttachment(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject) -> win32more.Windows.Devices.AllJoyn.AllJoynSession: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusObject, win32more.Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObject, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BusAttachment = property(get_BusAttachment, None)
    Session = property(get_Session, None)
    Stopped = event()
class AllJoynBusObjectStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgsFactory, status: Int32) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class AllJoynCredentials(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynCredentials'
    @winrt_mixinmethod
    def get_AuthenticationMechanism(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials) -> win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_mixinmethod
    def get_Certificate(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_Certificate(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_PasswordCredential(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_PasswordCredential(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Timeout(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Timeout(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentials, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    Certificate = property(get_Certificate, put_Certificate)
    PasswordCredential = property(get_PasswordCredential, put_PasswordCredential)
    Timeout = property(get_Timeout, put_Timeout)
class AllJoynCredentialsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynCredentialsRequestedEventArgs'
    @winrt_mixinmethod
    def get_AttemptCount(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_Credentials(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynCredentials: ...
    @winrt_mixinmethod
    def get_PeerUniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RequestedUserName(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    AttemptCount = property(get_AttemptCount, None)
    Credentials = property(get_Credentials, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    RequestedUserName = property(get_RequestedUserName, None)
class AllJoynCredentialsVerificationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynCredentialsVerificationRequestedEventArgs'
    @winrt_mixinmethod
    def get_AuthenticationMechanism(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_mixinmethod
    def get_PeerUniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PeerCertificate(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_PeerCertificateErrorSeverity(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_PeerCertificateErrors(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_PeerIntermediateCertificates(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Accept(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerCertificate = property(get_PeerCertificate, None)
    PeerCertificateErrorSeverity = property(get_PeerCertificateErrorSeverity, None)
    PeerCertificateErrors = property(get_PeerCertificateErrors, None)
    PeerIntermediateCertificates = property(get_PeerIntermediateCertificates, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
class AllJoynMessageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynMessageInfo
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynMessageInfo'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynMessageInfo.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynMessageInfoFactory, senderUniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynMessageInfo: ...
    @winrt_mixinmethod
    def get_SenderUniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynMessageInfo) -> WinRT_String: ...
    SenderUniqueName = property(get_SenderUniqueName, None)
class AllJoynProducerStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgsFactory, status: Int32) -> win32more.Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class AllJoynServiceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfo
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynServiceInfo'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 3:
            return win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfoFactory, uniqueName: WinRT_String, objectPath: WinRT_String, sessionPort: UInt16) -> win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo: ...
    @winrt_mixinmethod
    def get_UniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ObjectPath(self: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionPort(self: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfo) -> UInt16: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfoStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo]: ...
    ObjectPath = property(get_ObjectPath, None)
    SessionPort = property(get_SessionPort, None)
    UniqueName = property(get_UniqueName, None)
class AllJoynServiceInfoRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgsFactory, uniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class AllJoynSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynSession
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSession'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession) -> Int32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession) -> Int32: ...
    @winrt_mixinmethod
    def RemoveMemberAsync(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, uniqueName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_mixinmethod
    def add_MemberAdded(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynSession, win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MemberAdded(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MemberRemoved(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynSession, win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MemberRemoved(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Lost(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynSession, win32more.Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Lost(self: win32more.Windows.Devices.AllJoyn.IAllJoynSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetFromServiceInfoAsync(cls: win32more.Windows.Devices.AllJoyn.IAllJoynSessionStatics, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynSession]: ...
    @winrt_classmethod
    def GetFromServiceInfoAndBusAttachmentAsync(cls: win32more.Windows.Devices.AllJoyn.IAllJoynSessionStatics, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynSession]: ...
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    MemberAdded = event()
    MemberRemoved = event()
    Lost = event()
class AllJoynSessionJoinedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgsFactory, session: win32more.Windows.Devices.AllJoyn.AllJoynSession) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynSession: ...
    Session = property(get_Session, None)
class AllJoynSessionLostEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgsFactory, reason: win32more.Windows.Devices.AllJoyn.AllJoynSessionLostReason) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionLostReason: ...
    Reason = property(get_Reason, None)
class AllJoynSessionLostReason(Enum, Int32):
    None_ = 0
    ProducerLeftSession = 1
    ProducerClosedAbruptly = 2
    RemovedByProducer = 3
    LinkTimeout = 4
    Other = 5
class AllJoynSessionMemberAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgsFactory, uniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class AllJoynSessionMemberRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgsFactory, uniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs: ...
    @winrt_mixinmethod
    def get_UniqueName(self: win32more.Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class _AllJoynStatus_Meta_(ComPtr.__class__):
    pass
class AllJoynStatus(ComPtr, metaclass=_AllJoynStatus_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynStatus'
    @winrt_classmethod
    def get_Ok(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_Fail(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_OperationTimedOut(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_OtherEndClosed(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_ConnectionRefused(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_AuthenticationFailed(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_AuthenticationRejectedByUser(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_SslConnectFailed(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_SslIdentityVerificationFailed(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InsufficientSecurity(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument1(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument2(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument3(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument4(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument5(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument6(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument7(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    @winrt_classmethod
    def get_InvalidArgument8(cls: win32more.Windows.Devices.AllJoyn.IAllJoynStatusStatics) -> Int32: ...
    _AllJoynStatus_Meta_.AuthenticationFailed = property(get_AuthenticationFailed, None)
    _AllJoynStatus_Meta_.AuthenticationRejectedByUser = property(get_AuthenticationRejectedByUser, None)
    _AllJoynStatus_Meta_.ConnectionRefused = property(get_ConnectionRefused, None)
    _AllJoynStatus_Meta_.Fail = property(get_Fail, None)
    _AllJoynStatus_Meta_.InsufficientSecurity = property(get_InsufficientSecurity, None)
    _AllJoynStatus_Meta_.InvalidArgument1 = property(get_InvalidArgument1, None)
    _AllJoynStatus_Meta_.InvalidArgument2 = property(get_InvalidArgument2, None)
    _AllJoynStatus_Meta_.InvalidArgument3 = property(get_InvalidArgument3, None)
    _AllJoynStatus_Meta_.InvalidArgument4 = property(get_InvalidArgument4, None)
    _AllJoynStatus_Meta_.InvalidArgument5 = property(get_InvalidArgument5, None)
    _AllJoynStatus_Meta_.InvalidArgument6 = property(get_InvalidArgument6, None)
    _AllJoynStatus_Meta_.InvalidArgument7 = property(get_InvalidArgument7, None)
    _AllJoynStatus_Meta_.InvalidArgument8 = property(get_InvalidArgument8, None)
    _AllJoynStatus_Meta_.Ok = property(get_Ok, None)
    _AllJoynStatus_Meta_.OperationTimedOut = property(get_OperationTimedOut, None)
    _AllJoynStatus_Meta_.OtherEndClosed = property(get_OtherEndClosed, None)
    _AllJoynStatus_Meta_.SslConnectFailed = property(get_SslConnectFailed, None)
    _AllJoynStatus_Meta_.SslIdentityVerificationFailed = property(get_SslIdentityVerificationFailed, None)
class AllJoynTrafficType(Enum, Int32):
    Unknown = 0
    Messages = 1
    RawUnreliable = 2
    RawReliable = 4
class AllJoynWatcherStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs
    _classid_ = 'Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgsFactory, status: Int32) -> win32more.Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynAboutData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAboutData'
    _iid_ = Guid('{e5a9bf00-1fa2-4839-93ef-f9df404890f7}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultAppName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DefaultAppName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AppNames(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(11)
    def get_DateOfManufacture(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(12)
    def put_DateOfManufacture(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(13)
    def get_DefaultDescription(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_DefaultDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Descriptions(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(16)
    def get_DefaultManufacturer(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_DefaultManufacturer(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_Manufacturers(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(19)
    def get_ModelNumber(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_ModelNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_SoftwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def put_SoftwareVersion(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(23)
    def get_SupportUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(24)
    def put_SupportUrl(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(25)
    def get_AppId(self) -> Guid: ...
    @winrt_commethod(26)
    def put_AppId(self, value: Guid) -> Void: ...
    AppId = property(get_AppId, put_AppId)
    AppNames = property(get_AppNames, None)
    DateOfManufacture = property(get_DateOfManufacture, put_DateOfManufacture)
    DefaultAppName = property(get_DefaultAppName, put_DefaultAppName)
    DefaultDescription = property(get_DefaultDescription, put_DefaultDescription)
    DefaultManufacturer = property(get_DefaultManufacturer, put_DefaultManufacturer)
    Descriptions = property(get_Descriptions, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Manufacturers = property(get_Manufacturers, None)
    ModelNumber = property(get_ModelNumber, put_ModelNumber)
    SoftwareVersion = property(get_SoftwareVersion, put_SoftwareVersion)
    SupportUrl = property(get_SupportUrl, put_SupportUrl)
class IAllJoynAboutDataView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAboutDataView'
    _iid_ = Guid('{6823111f-6212-4934-9c48-e19ca4984288}')
    @winrt_commethod(6)
    def get_Status(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(8)
    def get_AJSoftwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AppId(self) -> Guid: ...
    @winrt_commethod(10)
    def get_DateOfManufacture(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def get_DefaultLanguage(self) -> win32more.Windows.Globalization.Language: ...
    @winrt_commethod(12)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_HardwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_ModelNumber(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_SoftwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_SupportedLanguages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    @winrt_commethod(17)
    def get_SupportUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(18)
    def get_AppName(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_DeviceName(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Manufacturer(self) -> WinRT_String: ...
    AJSoftwareVersion = property(get_AJSoftwareVersion, None)
    AppId = property(get_AppId, None)
    AppName = property(get_AppName, None)
    DateOfManufacture = property(get_DateOfManufacture, None)
    DefaultLanguage = property(get_DefaultLanguage, None)
    Description = property(get_Description, None)
    DeviceId = property(get_DeviceId, None)
    DeviceName = property(get_DeviceName, None)
    HardwareVersion = property(get_HardwareVersion, None)
    Manufacturer = property(get_Manufacturer, None)
    ModelNumber = property(get_ModelNumber, None)
    Properties = property(get_Properties, None)
    SoftwareVersion = property(get_SoftwareVersion, None)
    Status = property(get_Status, None)
    SupportUrl = property(get_SupportUrl, None)
    SupportedLanguages = property(get_SupportedLanguages, None)
class IAllJoynAboutDataViewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAboutDataViewStatics'
    _iid_ = Guid('{57edb688-0c5e-416e-88b5-39b32d25c47d}')
    @winrt_commethod(6)
    def GetDataBySessionPortAsync(self, uniqueName: WinRT_String, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_commethod(7)
    def GetDataBySessionPortWithLanguageAsync(self, uniqueName: WinRT_String, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, sessionPort: UInt16, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
class IAllJoynAcceptSessionJoiner(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner'
    _iid_ = Guid('{4da817d2-cd1d-4023-a7c4-16def89c28df}')
    @winrt_commethod(6)
    def Accept(self) -> Void: ...
class IAllJoynAcceptSessionJoinerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgs'
    _iid_ = Guid('{4efb5365-3e8a-4257-8f10-539ce0d56c0f}')
    @winrt_commethod(6)
    def get_UniqueName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SessionPort(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_TrafficType(self) -> win32more.Windows.Devices.AllJoyn.AllJoynTrafficType: ...
    @winrt_commethod(9)
    def get_SamePhysicalNode(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_SameNetwork(self) -> Boolean: ...
    @winrt_commethod(11)
    def Accept(self) -> Void: ...
    SameNetwork = property(get_SameNetwork, None)
    SamePhysicalNode = property(get_SamePhysicalNode, None)
    SessionPort = property(get_SessionPort, None)
    TrafficType = property(get_TrafficType, None)
    UniqueName = property(get_UniqueName, None)
class IAllJoynAcceptSessionJoinerEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoinerEventArgsFactory'
    _iid_ = Guid('{b4435bc0-6145-429e-84db-d5bfe772b14f}')
    @winrt_commethod(6)
    def Create(self, uniqueName: WinRT_String, sessionPort: UInt16, trafficType: win32more.Windows.Devices.AllJoyn.AllJoynTrafficType, proximity: Byte, acceptSessionJoiner: win32more.Windows.Devices.AllJoyn.IAllJoynAcceptSessionJoiner) -> win32more.Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs: ...
class IAllJoynAuthenticationCompleteEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynAuthenticationCompleteEventArgs'
    _iid_ = Guid('{97b4701c-15dc-4b53-b6a4-7d134300d7bf}')
    @winrt_commethod(6)
    def get_AuthenticationMechanism(self) -> win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_commethod(7)
    def get_PeerUniqueName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    Succeeded = property(get_Succeeded, None)
class IAllJoynBusAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachment'
    _iid_ = Guid('{f309f153-1eed-42c3-a20e-436d41fe62f6}')
    @winrt_commethod(6)
    def get_AboutData(self) -> win32more.Windows.Devices.AllJoyn.AllJoynAboutData: ...
    @winrt_commethod(7)
    def get_ConnectionSpecification(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_commethod(9)
    def get_UniqueName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def PingAsync(self, uniqueName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(11)
    def Connect(self) -> Void: ...
    @winrt_commethod(12)
    def Disconnect(self) -> Void: ...
    @winrt_commethod(13)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynBusAttachmentStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def get_AuthenticationMechanisms(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]: ...
    @winrt_commethod(16)
    def add_CredentialsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynCredentialsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_CredentialsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_CredentialsVerificationRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynCredentialsVerificationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_CredentialsVerificationRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_AuthenticationComplete(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationCompleteEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_AuthenticationComplete(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AboutData = property(get_AboutData, None)
    AuthenticationMechanisms = property(get_AuthenticationMechanisms, None)
    ConnectionSpecification = property(get_ConnectionSpecification, None)
    State = property(get_State, None)
    UniqueName = property(get_UniqueName, None)
    StateChanged = event()
    CredentialsRequested = event()
    CredentialsVerificationRequested = event()
    AuthenticationComplete = event()
class IAllJoynBusAttachment2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachment2'
    _iid_ = Guid('{3474cb1e-2368-43b2-b43e-6a3ac1278d98}')
    @winrt_commethod(6)
    def GetAboutDataAsync(self, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_commethod(7)
    def GetAboutDataWithLanguageAsync(self, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynAboutDataView]: ...
    @winrt_commethod(8)
    def add_AcceptSessionJoinerRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynAcceptSessionJoinerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AcceptSessionJoinerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SessionJoined(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment, win32more.Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SessionJoined(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AcceptSessionJoinerRequested = event()
    SessionJoined = event()
class IAllJoynBusAttachmentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachmentFactory'
    _iid_ = Guid('{642ef1a4-ad85-4ddf-90ae-604452b22288}')
    @winrt_commethod(6)
    def Create(self, connectionSpecification: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
class IAllJoynBusAttachmentStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachmentStateChangedEventArgs'
    _iid_ = Guid('{d82e75f4-c02a-41ec-a8d5-eab1558953aa}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachmentState: ...
    @winrt_commethod(7)
    def get_Status(self) -> Int32: ...
    State = property(get_State, None)
    Status = property(get_Status, None)
class IAllJoynBusAttachmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusAttachmentStatics'
    _iid_ = Guid('{839d4d3d-1051-40d7-872a-8d0141115b1f}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_commethod(7)
    def GetWatcher(self, requiredInterfaces: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Enumeration.DeviceWatcher: ...
class IAllJoynBusObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObject'
    _iid_ = Guid('{e8fd825e-f73a-490c-8804-04e026643047}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def AddProducer(self, producer: win32more.Windows.Devices.AllJoyn.IAllJoynProducer) -> Void: ...
    @winrt_commethod(9)
    def get_BusAttachment(self) -> win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment: ...
    @winrt_commethod(10)
    def get_Session(self) -> win32more.Windows.Devices.AllJoyn.AllJoynSession: ...
    @winrt_commethod(11)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynBusObject, win32more.Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BusAttachment = property(get_BusAttachment, None)
    Session = property(get_Session, None)
    Stopped = event()
class IAllJoynBusObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObjectFactory'
    _iid_ = Guid('{2c2f9f0b-8e02-4f9c-ac27-ea6dad5d3b50}')
    @winrt_commethod(6)
    def Create(self, objectPath: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObject: ...
    @winrt_commethod(7)
    def CreateWithBusAttachment(self, objectPath: WinRT_String, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObject: ...
class IAllJoynBusObjectStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgs'
    _iid_ = Guid('{de102115-ef8e-4d42-b93b-a2ae74519766}')
    @winrt_commethod(6)
    def get_Status(self) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynBusObjectStoppedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynBusObjectStoppedEventArgsFactory'
    _iid_ = Guid('{6b22fd48-d0a3-4255-953a-4772b4028073}')
    @winrt_commethod(6)
    def Create(self, status: Int32) -> win32more.Windows.Devices.AllJoyn.AllJoynBusObjectStoppedEventArgs: ...
class IAllJoynCredentials(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynCredentials'
    _iid_ = Guid('{824650f2-a190-40b1-abab-349ec244dfaa}')
    @winrt_commethod(6)
    def get_AuthenticationMechanism(self) -> win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_commethod(7)
    def get_Certificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(8)
    def put_Certificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(9)
    def get_PasswordCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(10)
    def put_PasswordCredential(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(11)
    def get_Timeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def put_Timeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    Certificate = property(get_Certificate, put_Certificate)
    PasswordCredential = property(get_PasswordCredential, put_PasswordCredential)
    Timeout = property(get_Timeout, put_Timeout)
class IAllJoynCredentialsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynCredentialsRequestedEventArgs'
    _iid_ = Guid('{6a87e34e-b069-4b80-9e1a-41bc837c65d2}')
    @winrt_commethod(6)
    def get_AttemptCount(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Credentials(self) -> win32more.Windows.Devices.AllJoyn.AllJoynCredentials: ...
    @winrt_commethod(8)
    def get_PeerUniqueName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_RequestedUserName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    AttemptCount = property(get_AttemptCount, None)
    Credentials = property(get_Credentials, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
    RequestedUserName = property(get_RequestedUserName, None)
class IAllJoynCredentialsVerificationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynCredentialsVerificationRequestedEventArgs'
    _iid_ = Guid('{800a7612-b805-44af-a2e1-792ab655a2d0}')
    @winrt_commethod(6)
    def get_AuthenticationMechanism(self) -> win32more.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism: ...
    @winrt_commethod(7)
    def get_PeerUniqueName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PeerCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def get_PeerCertificateErrorSeverity(self) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(10)
    def get_PeerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(11)
    def get_PeerIntermediateCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(12)
    def Accept(self) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    AuthenticationMechanism = property(get_AuthenticationMechanism, None)
    PeerCertificate = property(get_PeerCertificate, None)
    PeerCertificateErrorSeverity = property(get_PeerCertificateErrorSeverity, None)
    PeerCertificateErrors = property(get_PeerCertificateErrors, None)
    PeerIntermediateCertificates = property(get_PeerIntermediateCertificates, None)
    PeerUniqueName = property(get_PeerUniqueName, None)
class IAllJoynMessageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynMessageInfo'
    _iid_ = Guid('{ff2b0127-2c12-4859-aa3a-c74461ee814c}')
    @winrt_commethod(6)
    def get_SenderUniqueName(self) -> WinRT_String: ...
    SenderUniqueName = property(get_SenderUniqueName, None)
class IAllJoynMessageInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynMessageInfoFactory'
    _iid_ = Guid('{34664c2a-8289-43d4-b4a8-3f4de359f043}')
    @winrt_commethod(6)
    def Create(self, senderUniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynMessageInfo: ...
class IAllJoynProducer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynProducer'
    _iid_ = Guid('{9d084679-469b-495a-a710-ac50f123069f}')
    @winrt_commethod(6)
    def SetBusObject(self, busObject: win32more.Windows.Devices.AllJoyn.AllJoynBusObject) -> Void: ...
class IAllJoynProducerStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgs'
    _iid_ = Guid('{51309770-4937-492d-8080-236439987ceb}')
    @winrt_commethod(6)
    def get_Status(self) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynProducerStoppedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynProducerStoppedEventArgsFactory'
    _iid_ = Guid('{56529961-b219-4d6e-9f78-fa3f99fa8fe5}')
    @winrt_commethod(6)
    def Create(self, status: Int32) -> win32more.Windows.Devices.AllJoyn.AllJoynProducerStoppedEventArgs: ...
class IAllJoynServiceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfo'
    _iid_ = Guid('{4cbe8209-b93e-4182-999b-ddd000f9c575}')
    @winrt_commethod(6)
    def get_UniqueName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ObjectPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SessionPort(self) -> UInt16: ...
    ObjectPath = property(get_ObjectPath, None)
    SessionPort = property(get_SessionPort, None)
    UniqueName = property(get_UniqueName, None)
class IAllJoynServiceInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoFactory'
    _iid_ = Guid('{7581dabd-fe03-4f4b-94a4-f02fdcbd11b8}')
    @winrt_commethod(6)
    def Create(self, uniqueName: WinRT_String, objectPath: WinRT_String, sessionPort: UInt16) -> win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo: ...
class IAllJoynServiceInfoRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgs'
    _iid_ = Guid('{3057a95f-1d3f-41f3-8969-e32792627396}')
    @winrt_commethod(6)
    def get_UniqueName(self) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class IAllJoynServiceInfoRemovedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoRemovedEventArgsFactory'
    _iid_ = Guid('{0dbf8627-9aff-4955-9227-6953baf41569}')
    @winrt_commethod(6)
    def Create(self, uniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynServiceInfoRemovedEventArgs: ...
class IAllJoynServiceInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynServiceInfoStatics'
    _iid_ = Guid('{5678570a-603a-49fc-b750-0ef13609213c}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo]: ...
class IAllJoynSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSession'
    _iid_ = Guid('{e8d11b0c-c0d4-406c-88a9-a93efa85d4b1}')
    @winrt_commethod(6)
    def get_Id(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Status(self) -> Int32: ...
    @winrt_commethod(8)
    def RemoveMemberAsync(self, uniqueName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Int32]: ...
    @winrt_commethod(9)
    def add_MemberAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynSession, win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_MemberAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_MemberRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynSession, win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_MemberRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Lost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.AllJoyn.AllJoynSession, win32more.Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Lost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    MemberAdded = event()
    MemberRemoved = event()
    Lost = event()
class IAllJoynSessionJoinedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgs'
    _iid_ = Guid('{9e9f5bd0-b5d7-47c5-8dab-b040cc192871}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Devices.AllJoyn.AllJoynSession: ...
    Session = property(get_Session, None)
class IAllJoynSessionJoinedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionJoinedEventArgsFactory'
    _iid_ = Guid('{6824d689-d6cb-4d9e-a09e-35806870b17f}')
    @winrt_commethod(6)
    def Create(self, session: win32more.Windows.Devices.AllJoyn.AllJoynSession) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionJoinedEventArgs: ...
class IAllJoynSessionLostEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgs'
    _iid_ = Guid('{e766a48a-8bb8-4954-ae67-d2fa43d1f96b}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionLostReason: ...
    Reason = property(get_Reason, None)
class IAllJoynSessionLostEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionLostEventArgsFactory'
    _iid_ = Guid('{13bbfd32-d2f4-49c9-980e-2805e13586b1}')
    @winrt_commethod(6)
    def Create(self, reason: win32more.Windows.Devices.AllJoyn.AllJoynSessionLostReason) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionLostEventArgs: ...
class IAllJoynSessionMemberAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgs'
    _iid_ = Guid('{49a2798a-0dd1-46c1-9cd6-27190e503a5e}')
    @winrt_commethod(6)
    def get_UniqueName(self) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class IAllJoynSessionMemberAddedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberAddedEventArgsFactory'
    _iid_ = Guid('{341de352-1d33-40a1-a1d3-e5777020e1f1}')
    @winrt_commethod(6)
    def Create(self, uniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberAddedEventArgs: ...
class IAllJoynSessionMemberRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgs'
    _iid_ = Guid('{409a219f-aa4a-4893-b430-baa1b63c6219}')
    @winrt_commethod(6)
    def get_UniqueName(self) -> WinRT_String: ...
    UniqueName = property(get_UniqueName, None)
class IAllJoynSessionMemberRemovedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionMemberRemovedEventArgsFactory'
    _iid_ = Guid('{c4d355e8-42b8-4b67-b757-d0cfcad59280}')
    @winrt_commethod(6)
    def Create(self, uniqueName: WinRT_String) -> win32more.Windows.Devices.AllJoyn.AllJoynSessionMemberRemovedEventArgs: ...
class IAllJoynSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynSessionStatics'
    _iid_ = Guid('{9e05d604-a06c-46d4-b46c-0b0b54105b44}')
    @winrt_commethod(6)
    def GetFromServiceInfoAsync(self, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynSession]: ...
    @winrt_commethod(7)
    def GetFromServiceInfoAndBusAttachmentAsync(self, serviceInfo: win32more.Windows.Devices.AllJoyn.AllJoynServiceInfo, busAttachment: win32more.Windows.Devices.AllJoyn.AllJoynBusAttachment) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.AllJoyn.AllJoynSession]: ...
class IAllJoynStatusStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynStatusStatics'
    _iid_ = Guid('{d0b7a17e-0d29-4da9-8ac6-54c554bedbc5}')
    @winrt_commethod(6)
    def get_Ok(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Fail(self) -> Int32: ...
    @winrt_commethod(8)
    def get_OperationTimedOut(self) -> Int32: ...
    @winrt_commethod(9)
    def get_OtherEndClosed(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ConnectionRefused(self) -> Int32: ...
    @winrt_commethod(11)
    def get_AuthenticationFailed(self) -> Int32: ...
    @winrt_commethod(12)
    def get_AuthenticationRejectedByUser(self) -> Int32: ...
    @winrt_commethod(13)
    def get_SslConnectFailed(self) -> Int32: ...
    @winrt_commethod(14)
    def get_SslIdentityVerificationFailed(self) -> Int32: ...
    @winrt_commethod(15)
    def get_InsufficientSecurity(self) -> Int32: ...
    @winrt_commethod(16)
    def get_InvalidArgument1(self) -> Int32: ...
    @winrt_commethod(17)
    def get_InvalidArgument2(self) -> Int32: ...
    @winrt_commethod(18)
    def get_InvalidArgument3(self) -> Int32: ...
    @winrt_commethod(19)
    def get_InvalidArgument4(self) -> Int32: ...
    @winrt_commethod(20)
    def get_InvalidArgument5(self) -> Int32: ...
    @winrt_commethod(21)
    def get_InvalidArgument6(self) -> Int32: ...
    @winrt_commethod(22)
    def get_InvalidArgument7(self) -> Int32: ...
    @winrt_commethod(23)
    def get_InvalidArgument8(self) -> Int32: ...
    AuthenticationFailed = property(get_AuthenticationFailed, None)
    AuthenticationRejectedByUser = property(get_AuthenticationRejectedByUser, None)
    ConnectionRefused = property(get_ConnectionRefused, None)
    Fail = property(get_Fail, None)
    InsufficientSecurity = property(get_InsufficientSecurity, None)
    InvalidArgument1 = property(get_InvalidArgument1, None)
    InvalidArgument2 = property(get_InvalidArgument2, None)
    InvalidArgument3 = property(get_InvalidArgument3, None)
    InvalidArgument4 = property(get_InvalidArgument4, None)
    InvalidArgument5 = property(get_InvalidArgument5, None)
    InvalidArgument6 = property(get_InvalidArgument6, None)
    InvalidArgument7 = property(get_InvalidArgument7, None)
    InvalidArgument8 = property(get_InvalidArgument8, None)
    Ok = property(get_Ok, None)
    OperationTimedOut = property(get_OperationTimedOut, None)
    OtherEndClosed = property(get_OtherEndClosed, None)
    SslConnectFailed = property(get_SslConnectFailed, None)
    SslIdentityVerificationFailed = property(get_SslIdentityVerificationFailed, None)
class IAllJoynWatcherStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgs'
    _iid_ = Guid('{c9fca03b-701d-4aa8-97dd-a2bb0a8f5fa3}')
    @winrt_commethod(6)
    def get_Status(self) -> Int32: ...
    Status = property(get_Status, None)
class IAllJoynWatcherStoppedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.AllJoyn.IAllJoynWatcherStoppedEventArgsFactory'
    _iid_ = Guid('{878fa5a8-2d50-47e1-904a-20bf0d48c782}')
    @winrt_commethod(6)
    def Create(self, status: Int32) -> win32more.Windows.Devices.AllJoyn.AllJoynWatcherStoppedEventArgs: ...


make_ready(__name__)
