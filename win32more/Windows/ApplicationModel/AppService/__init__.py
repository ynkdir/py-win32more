from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.AppService
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.System.RemoteSystems
import win32more.Windows.Win32.System.WinRT
class AppServiceCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceCatalog'
    @winrt_classmethod
    def FindAppServiceProvidersAsync(cls: win32more.Windows.ApplicationModel.AppService.IAppServiceCatalogStatics, appServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
class AppServiceClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceClosedEventArgs
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceClosedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.AppService.IAppServiceClosedEventArgs) -> win32more.Windows.ApplicationModel.AppService.AppServiceClosedStatus: ...
    Status = property(get_Status, None)
class AppServiceClosedStatus(Enum, Int32):
    Completed = 0
    Canceled = 1
    ResourceLimitsExceeded = 2
    Unknown = 3
class AppServiceConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceConnection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.AppService.AppServiceConnection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.AppService.AppServiceConnection: ...
    @winrt_mixinmethod
    def get_AppServiceName(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppServiceName(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PackageFamilyName(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def OpenAsync(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, message: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceResponse]: ...
    @winrt_mixinmethod
    def add_RequestReceived(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppService.AppServiceConnection, win32more.Windows.ApplicationModel.AppService.AppServiceRequestReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RequestReceived(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ServiceClosed(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppService.AppServiceConnection, win32more.Windows.ApplicationModel.AppService.AppServiceClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServiceClosed(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OpenRemoteAsync(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection2, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection2) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def put_User(self: win32more.Windows.ApplicationModel.AppService.IAppServiceConnection2, value: win32more.Windows.System.User) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def SendStatelessMessageAsync(cls: win32more.Windows.ApplicationModel.AppService.IAppServiceConnectionStatics, connection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection, connectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, message: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.StatelessAppServiceResponse]: ...
    AppServiceName = property(get_AppServiceName, put_AppServiceName)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
    User = property(get_User, put_User)
    RequestReceived = event()
    ServiceClosed = event()
class AppServiceConnectionStatus(Enum, Int32):
    Success = 0
    AppNotInstalled = 1
    AppUnavailable = 2
    AppServiceUnavailable = 3
    Unknown = 4
    RemoteSystemUnavailable = 5
    RemoteSystemNotSupportedByApp = 6
    NotAuthorized = 7
    AuthenticationError = 8
    NetworkNotAvailable = 9
    DisabledByPolicy = 10
    WebServiceUnavailable = 11
class AppServiceDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceDeferral
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.AppService.IAppServiceDeferral) -> Void: ...
class AppServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceRequest
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceRequest'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.AppService.IAppServiceRequest) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def SendResponseAsync(self: win32more.Windows.ApplicationModel.AppService.IAppServiceRequest, message: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceResponseStatus]: ...
    Message = property(get_Message, None)
class AppServiceRequestReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceRequestReceivedEventArgs
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceRequestReceivedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.AppService.IAppServiceRequestReceivedEventArgs) -> win32more.Windows.ApplicationModel.AppService.AppServiceRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.AppService.IAppServiceRequestReceivedEventArgs) -> win32more.Windows.ApplicationModel.AppService.AppServiceDeferral: ...
    Request = property(get_Request, None)
class AppServiceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceResponse
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceResponse'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.AppService.IAppServiceResponse) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.AppService.IAppServiceResponse) -> win32more.Windows.ApplicationModel.AppService.AppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
class AppServiceResponseStatus(Enum, Int32):
    Success = 0
    Failure = 1
    ResourceLimitsExceeded = 2
    Unknown = 3
    RemoteSystemUnavailable = 4
    MessageSizeTooLarge = 5
    AppUnavailable = 6
    AuthenticationError = 7
    NetworkNotAvailable = 8
    DisabledByPolicy = 9
    WebServiceUnavailable = 10
class AppServiceTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails
    _classid_ = 'Windows.ApplicationModel.AppService.AppServiceTriggerDetails'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppServiceConnection(self: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails) -> win32more.Windows.ApplicationModel.AppService.AppServiceConnection: ...
    @winrt_mixinmethod
    def get_IsRemoteSystemConnection(self: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def CheckCallerForCapabilityAsync(self: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails3, capabilityName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_CallerRemoteConnectionToken(self: win32more.Windows.ApplicationModel.AppService.IAppServiceTriggerDetails4) -> WinRT_String: ...
    AppServiceConnection = property(get_AppServiceConnection, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CallerRemoteConnectionToken = property(get_CallerRemoteConnectionToken, None)
    IsRemoteSystemConnection = property(get_IsRemoteSystemConnection, None)
    Name = property(get_Name, None)
class IAppServiceCatalogStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceCatalogStatics'
    _iid_ = Guid('{ef0d2507-d132-4c85-8395-3c31d5a1e941}')
    @winrt_commethod(6)
    def FindAppServiceProvidersAsync(self, appServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
class IAppServiceClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceClosedEventArgs'
    _iid_ = Guid('{de6016f6-cb03-4d35-ac8d-cc6303239731}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.AppService.AppServiceClosedStatus: ...
    Status = property(get_Status, None)
class IAppServiceConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceConnection'
    _iid_ = Guid('{9dd474a2-871f-4d52-89a9-9e090531bd27}')
    @winrt_commethod(6)
    def get_AppServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AppServiceName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_PackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def OpenAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_commethod(11)
    def SendMessageAsync(self, message: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceResponse]: ...
    @winrt_commethod(12)
    def add_RequestReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppService.AppServiceConnection, win32more.Windows.ApplicationModel.AppService.AppServiceRequestReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RequestReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ServiceClosed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppService.AppServiceConnection, win32more.Windows.ApplicationModel.AppService.AppServiceClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ServiceClosed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppServiceName = property(get_AppServiceName, put_AppServiceName)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
    RequestReceived = event()
    ServiceClosed = event()
class IAppServiceConnection2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceConnection2'
    _iid_ = Guid('{8bdfcd5f-2302-4fbd-8061-52511c2f8bf9}')
    @winrt_commethod(6)
    def OpenRemoteAsync(self, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(8)
    def put_User(self, value: win32more.Windows.System.User) -> Void: ...
    User = property(get_User, put_User)
class IAppServiceConnectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceConnectionStatics'
    _iid_ = Guid('{adc56ce9-d408-5673-8637-827a4b274168}')
    @winrt_commethod(6)
    def SendStatelessMessageAsync(self, connection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection, connectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, message: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.StatelessAppServiceResponse]: ...
class IAppServiceDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceDeferral'
    _iid_ = Guid('{7e1b5322-eab0-4248-ae04-fdf93838e472}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IAppServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceRequest'
    _iid_ = Guid('{20e58d9d-18de-4b01-80ba-90a76204e3c8}')
    @winrt_commethod(6)
    def get_Message(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def SendResponseAsync(self, message: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.AppService.AppServiceResponseStatus]: ...
    Message = property(get_Message, None)
class IAppServiceRequestReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceRequestReceivedEventArgs'
    _iid_ = Guid('{6e122360-ff65-44ae-9e45-857fe4180681}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.AppService.AppServiceRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.AppService.AppServiceDeferral: ...
    Request = property(get_Request, None)
class IAppServiceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceResponse'
    _iid_ = Guid('{8d503cec-9aa3-4e68-9559-9de63e372ce4}')
    @winrt_commethod(6)
    def get_Message(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.ApplicationModel.AppService.AppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
class IAppServiceTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceTriggerDetails'
    _iid_ = Guid('{88a2dcac-ad28-41b8-80bb-bdf1b2169e19}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppServiceConnection(self) -> win32more.Windows.ApplicationModel.AppService.AppServiceConnection: ...
    AppServiceConnection = property(get_AppServiceConnection, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Name = property(get_Name, None)
class IAppServiceTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceTriggerDetails2'
    _iid_ = Guid('{e83d54b2-28cc-43f2-b465-c0482e59e2dc}')
    @winrt_commethod(6)
    def get_IsRemoteSystemConnection(self) -> Boolean: ...
    IsRemoteSystemConnection = property(get_IsRemoteSystemConnection, None)
class IAppServiceTriggerDetails3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceTriggerDetails3'
    _iid_ = Guid('{fbd71e21-7939-4e68-9e3c-7780147aabb6}')
    @winrt_commethod(6)
    def CheckCallerForCapabilityAsync(self, capabilityName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IAppServiceTriggerDetails4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IAppServiceTriggerDetails4'
    _iid_ = Guid('{1185b180-8861-5e30-ab55-1cf4d08bbf6d}')
    @winrt_commethod(6)
    def get_CallerRemoteConnectionToken(self) -> WinRT_String: ...
    CallerRemoteConnectionToken = property(get_CallerRemoteConnectionToken, None)
class IStatelessAppServiceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppService.IStatelessAppServiceResponse'
    _iid_ = Guid('{43754af7-a9ec-52fe-82e7-939b68dc9388}')
    @winrt_commethod(6)
    def get_Message(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.ApplicationModel.AppService.StatelessAppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
class StatelessAppServiceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppService.IStatelessAppServiceResponse
    _classid_ = 'Windows.ApplicationModel.AppService.StatelessAppServiceResponse'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.AppService.IStatelessAppServiceResponse) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.AppService.IStatelessAppServiceResponse) -> win32more.Windows.ApplicationModel.AppService.StatelessAppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
class StatelessAppServiceResponseStatus(Enum, Int32):
    Success = 0
    AppNotInstalled = 1
    AppUnavailable = 2
    AppServiceUnavailable = 3
    RemoteSystemUnavailable = 4
    RemoteSystemNotSupportedByApp = 5
    NotAuthorized = 6
    ResourceLimitsExceeded = 7
    MessageSizeTooLarge = 8
    Failure = 9
    Unknown = 10
    AuthenticationError = 11
    NetworkNotAvailable = 12
    DisabledByPolicy = 13
    WebServiceUnavailable = 14


make_ready(__name__)
