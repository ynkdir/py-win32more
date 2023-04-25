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
import Windows.ApplicationModel
import Windows.ApplicationModel.AppService
import Windows.Foundation
import Windows.Foundation.Collections
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
class AppServiceCatalog(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceCatalog'
    @winrt_classmethod
    def FindAppServiceProvidersAsync(cls: Windows.ApplicationModel.AppService.IAppServiceCatalogStatics, appServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
class AppServiceClosedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceClosedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.AppService.IAppServiceClosedEventArgs) -> Windows.ApplicationModel.AppService.AppServiceClosedStatus: ...
    Status = property(get_Status, None)
AppServiceClosedStatus = Int32
AppServiceClosedStatus_Completed: AppServiceClosedStatus = 0
AppServiceClosedStatus_Canceled: AppServiceClosedStatus = 1
AppServiceClosedStatus_ResourceLimitsExceeded: AppServiceClosedStatus = 2
AppServiceClosedStatus_Unknown: AppServiceClosedStatus = 3
class AppServiceConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceConnection'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.AppService.AppServiceConnection: ...
    @winrt_mixinmethod
    def get_AppServiceName(self: Windows.ApplicationModel.AppService.IAppServiceConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppServiceName(self: Windows.ApplicationModel.AppService.IAppServiceConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.ApplicationModel.AppService.IAppServiceConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PackageFamilyName(self: Windows.ApplicationModel.AppService.IAppServiceConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def OpenAsync(self: Windows.ApplicationModel.AppService.IAppServiceConnection) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: Windows.ApplicationModel.AppService.IAppServiceConnection, message: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceResponse]: ...
    @winrt_mixinmethod
    def add_RequestReceived(self: Windows.ApplicationModel.AppService.IAppServiceConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppService.AppServiceConnection, Windows.ApplicationModel.AppService.AppServiceRequestReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RequestReceived(self: Windows.ApplicationModel.AppService.IAppServiceConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ServiceClosed(self: Windows.ApplicationModel.AppService.IAppServiceConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppService.AppServiceConnection, Windows.ApplicationModel.AppService.AppServiceClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServiceClosed(self: Windows.ApplicationModel.AppService.IAppServiceConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OpenRemoteAsync(self: Windows.ApplicationModel.AppService.IAppServiceConnection2, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.AppService.IAppServiceConnection2) -> Windows.System.User: ...
    @winrt_mixinmethod
    def put_User(self: Windows.ApplicationModel.AppService.IAppServiceConnection2, value: Windows.System.User) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def SendStatelessMessageAsync(cls: Windows.ApplicationModel.AppService.IAppServiceConnectionStatics, connection: Windows.ApplicationModel.AppService.AppServiceConnection, connectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, message: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.StatelessAppServiceResponse]: ...
    AppServiceName = property(get_AppServiceName, put_AppServiceName)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
    User = property(get_User, put_User)
AppServiceConnectionStatus = Int32
AppServiceConnectionStatus_Success: AppServiceConnectionStatus = 0
AppServiceConnectionStatus_AppNotInstalled: AppServiceConnectionStatus = 1
AppServiceConnectionStatus_AppUnavailable: AppServiceConnectionStatus = 2
AppServiceConnectionStatus_AppServiceUnavailable: AppServiceConnectionStatus = 3
AppServiceConnectionStatus_Unknown: AppServiceConnectionStatus = 4
AppServiceConnectionStatus_RemoteSystemUnavailable: AppServiceConnectionStatus = 5
AppServiceConnectionStatus_RemoteSystemNotSupportedByApp: AppServiceConnectionStatus = 6
AppServiceConnectionStatus_NotAuthorized: AppServiceConnectionStatus = 7
AppServiceConnectionStatus_AuthenticationError: AppServiceConnectionStatus = 8
AppServiceConnectionStatus_NetworkNotAvailable: AppServiceConnectionStatus = 9
AppServiceConnectionStatus_DisabledByPolicy: AppServiceConnectionStatus = 10
AppServiceConnectionStatus_WebServiceUnavailable: AppServiceConnectionStatus = 11
class AppServiceDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.AppService.IAppServiceDeferral) -> Void: ...
class AppServiceRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceRequest'
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.AppService.IAppServiceRequest) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def SendResponseAsync(self: Windows.ApplicationModel.AppService.IAppServiceRequest, message: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceResponseStatus]: ...
    Message = property(get_Message, None)
class AppServiceRequestReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceRequestReceivedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.AppService.IAppServiceRequestReceivedEventArgs) -> Windows.ApplicationModel.AppService.AppServiceRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.AppService.IAppServiceRequestReceivedEventArgs) -> Windows.ApplicationModel.AppService.AppServiceDeferral: ...
    Request = property(get_Request, None)
class AppServiceResponse(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceResponse'
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.AppService.IAppServiceResponse) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.AppService.IAppServiceResponse) -> Windows.ApplicationModel.AppService.AppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
AppServiceResponseStatus = Int32
AppServiceResponseStatus_Success: AppServiceResponseStatus = 0
AppServiceResponseStatus_Failure: AppServiceResponseStatus = 1
AppServiceResponseStatus_ResourceLimitsExceeded: AppServiceResponseStatus = 2
AppServiceResponseStatus_Unknown: AppServiceResponseStatus = 3
AppServiceResponseStatus_RemoteSystemUnavailable: AppServiceResponseStatus = 4
AppServiceResponseStatus_MessageSizeTooLarge: AppServiceResponseStatus = 5
AppServiceResponseStatus_AppUnavailable: AppServiceResponseStatus = 6
AppServiceResponseStatus_AuthenticationError: AppServiceResponseStatus = 7
AppServiceResponseStatus_NetworkNotAvailable: AppServiceResponseStatus = 8
AppServiceResponseStatus_DisabledByPolicy: AppServiceResponseStatus = 9
AppServiceResponseStatus_WebServiceUnavailable: AppServiceResponseStatus = 10
class AppServiceTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.AppServiceTriggerDetails'
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.AppService.IAppServiceTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.AppService.IAppServiceTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppServiceConnection(self: Windows.ApplicationModel.AppService.IAppServiceTriggerDetails) -> Windows.ApplicationModel.AppService.AppServiceConnection: ...
    @winrt_mixinmethod
    def get_IsRemoteSystemConnection(self: Windows.ApplicationModel.AppService.IAppServiceTriggerDetails2) -> Boolean: ...
    @winrt_mixinmethod
    def CheckCallerForCapabilityAsync(self: Windows.ApplicationModel.AppService.IAppServiceTriggerDetails3, capabilityName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_CallerRemoteConnectionToken(self: Windows.ApplicationModel.AppService.IAppServiceTriggerDetails4) -> WinRT_String: ...
    Name = property(get_Name, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    AppServiceConnection = property(get_AppServiceConnection, None)
    IsRemoteSystemConnection = property(get_IsRemoteSystemConnection, None)
    CallerRemoteConnectionToken = property(get_CallerRemoteConnectionToken, None)
class IAppServiceCatalogStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef0d2507-d132-4c85-83-95-3c-31-d5-a1-e9-41')
    @winrt_commethod(6)
    def FindAppServiceProvidersAsync(self, appServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
class IAppServiceClosedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('de6016f6-cb03-4d35-ac-8d-cc-63-03-23-97-31')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.AppService.AppServiceClosedStatus: ...
    Status = property(get_Status, None)
class IAppServiceConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9dd474a2-871f-4d52-89-a9-9e-09-05-31-bd-27')
    @winrt_commethod(6)
    def get_AppServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AppServiceName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_PackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def OpenAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_commethod(11)
    def SendMessageAsync(self, message: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceResponse]: ...
    @winrt_commethod(12)
    def add_RequestReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppService.AppServiceConnection, Windows.ApplicationModel.AppService.AppServiceRequestReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RequestReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ServiceClosed(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppService.AppServiceConnection, Windows.ApplicationModel.AppService.AppServiceClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ServiceClosed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppServiceName = property(get_AppServiceName, put_AppServiceName)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
class IAppServiceConnection2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8bdfcd5f-2302-4fbd-80-61-52-51-1c-2f-8b-f9')
    @winrt_commethod(6)
    def OpenRemoteAsync(self, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceConnectionStatus]: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(8)
    def put_User(self, value: Windows.System.User) -> Void: ...
    User = property(get_User, put_User)
class IAppServiceConnectionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('adc56ce9-d408-5673-86-37-82-7a-4b-27-41-68')
    @winrt_commethod(6)
    def SendStatelessMessageAsync(self, connection: Windows.ApplicationModel.AppService.AppServiceConnection, connectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, message: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.StatelessAppServiceResponse]: ...
class IAppServiceDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e1b5322-eab0-4248-ae-04-fd-f9-38-38-e4-72')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IAppServiceRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20e58d9d-18de-4b01-80-ba-90-a7-62-04-e3-c8')
    @winrt_commethod(6)
    def get_Message(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def SendResponseAsync(self, message: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.AppService.AppServiceResponseStatus]: ...
    Message = property(get_Message, None)
class IAppServiceRequestReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6e122360-ff65-44ae-9e-45-85-7f-e4-18-06-81')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.AppService.AppServiceRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.ApplicationModel.AppService.AppServiceDeferral: ...
    Request = property(get_Request, None)
class IAppServiceResponse(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8d503cec-9aa3-4e68-95-59-9d-e6-3e-37-2c-e4')
    @winrt_commethod(6)
    def get_Message(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.ApplicationModel.AppService.AppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
class IAppServiceTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88a2dcac-ad28-41b8-80-bb-bd-f1-b2-16-9e-19')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppServiceConnection(self) -> Windows.ApplicationModel.AppService.AppServiceConnection: ...
    Name = property(get_Name, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    AppServiceConnection = property(get_AppServiceConnection, None)
class IAppServiceTriggerDetails2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e83d54b2-28cc-43f2-b4-65-c0-48-2e-59-e2-dc')
    @winrt_commethod(6)
    def get_IsRemoteSystemConnection(self) -> Boolean: ...
    IsRemoteSystemConnection = property(get_IsRemoteSystemConnection, None)
class IAppServiceTriggerDetails3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbd71e21-7939-4e68-9e-3c-77-80-14-7a-ab-b6')
    @winrt_commethod(6)
    def CheckCallerForCapabilityAsync(self, capabilityName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IAppServiceTriggerDetails4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1185b180-8861-5e30-ab-55-1c-f4-d0-8b-bf-6d')
    @winrt_commethod(6)
    def get_CallerRemoteConnectionToken(self) -> WinRT_String: ...
    CallerRemoteConnectionToken = property(get_CallerRemoteConnectionToken, None)
class IStatelessAppServiceResponse(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('43754af7-a9ec-52fe-82-e7-93-9b-68-dc-93-88')
    @winrt_commethod(6)
    def get_Message(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.ApplicationModel.AppService.StatelessAppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
class StatelessAppServiceResponse(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppService.StatelessAppServiceResponse'
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.AppService.IStatelessAppServiceResponse) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.AppService.IStatelessAppServiceResponse) -> Windows.ApplicationModel.AppService.StatelessAppServiceResponseStatus: ...
    Message = property(get_Message, None)
    Status = property(get_Status, None)
StatelessAppServiceResponseStatus = Int32
StatelessAppServiceResponseStatus_Success: StatelessAppServiceResponseStatus = 0
StatelessAppServiceResponseStatus_AppNotInstalled: StatelessAppServiceResponseStatus = 1
StatelessAppServiceResponseStatus_AppUnavailable: StatelessAppServiceResponseStatus = 2
StatelessAppServiceResponseStatus_AppServiceUnavailable: StatelessAppServiceResponseStatus = 3
StatelessAppServiceResponseStatus_RemoteSystemUnavailable: StatelessAppServiceResponseStatus = 4
StatelessAppServiceResponseStatus_RemoteSystemNotSupportedByApp: StatelessAppServiceResponseStatus = 5
StatelessAppServiceResponseStatus_NotAuthorized: StatelessAppServiceResponseStatus = 6
StatelessAppServiceResponseStatus_ResourceLimitsExceeded: StatelessAppServiceResponseStatus = 7
StatelessAppServiceResponseStatus_MessageSizeTooLarge: StatelessAppServiceResponseStatus = 8
StatelessAppServiceResponseStatus_Failure: StatelessAppServiceResponseStatus = 9
StatelessAppServiceResponseStatus_Unknown: StatelessAppServiceResponseStatus = 10
StatelessAppServiceResponseStatus_AuthenticationError: StatelessAppServiceResponseStatus = 11
StatelessAppServiceResponseStatus_NetworkNotAvailable: StatelessAppServiceResponseStatus = 12
StatelessAppServiceResponseStatus_DisabledByPolicy: StatelessAppServiceResponseStatus = 13
StatelessAppServiceResponseStatus_WebServiceUnavailable: StatelessAppServiceResponseStatus = 14
make_head(_module, 'AppServiceCatalog')
make_head(_module, 'AppServiceClosedEventArgs')
make_head(_module, 'AppServiceConnection')
make_head(_module, 'AppServiceDeferral')
make_head(_module, 'AppServiceRequest')
make_head(_module, 'AppServiceRequestReceivedEventArgs')
make_head(_module, 'AppServiceResponse')
make_head(_module, 'AppServiceTriggerDetails')
make_head(_module, 'IAppServiceCatalogStatics')
make_head(_module, 'IAppServiceClosedEventArgs')
make_head(_module, 'IAppServiceConnection')
make_head(_module, 'IAppServiceConnection2')
make_head(_module, 'IAppServiceConnectionStatics')
make_head(_module, 'IAppServiceDeferral')
make_head(_module, 'IAppServiceRequest')
make_head(_module, 'IAppServiceRequestReceivedEventArgs')
make_head(_module, 'IAppServiceResponse')
make_head(_module, 'IAppServiceTriggerDetails')
make_head(_module, 'IAppServiceTriggerDetails2')
make_head(_module, 'IAppServiceTriggerDetails3')
make_head(_module, 'IAppServiceTriggerDetails4')
make_head(_module, 'IStatelessAppServiceResponse')
make_head(_module, 'StatelessAppServiceResponse')
