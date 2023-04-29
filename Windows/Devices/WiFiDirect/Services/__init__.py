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
import Windows.Devices.Enumeration
import Windows.Devices.WiFiDirect.Services
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Sockets
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWiFiDirectService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('50aabbb8-5f71-45ec-84-f1-a1-e4-fc-78-79-a3')
    @winrt_commethod(6)
    def get_RemoteServiceInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_SupportedConfigurationMethods(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_commethod(8)
    def get_PreferGroupOwnerMode(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_PreferGroupOwnerMode(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_SessionInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_SessionInfo(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(12)
    def get_ServiceError(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_commethod(13)
    def add_SessionDeferred(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectService, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionDeferredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_SessionDeferred(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def GetProvisioningInfoAsync(self, selectedConfigurationMethod: Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo]: ...
    @winrt_commethod(16)
    def ConnectAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_commethod(17)
    def ConnectAsyncWithPin(self, pin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    RemoteServiceInfo = property(get_RemoteServiceInfo, None)
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
    PreferGroupOwnerMode = property(get_PreferGroupOwnerMode, put_PreferGroupOwnerMode)
    SessionInfo = property(get_SessionInfo, put_SessionInfo)
    ServiceError = property(get_ServiceError, None)
class IWiFiDirectServiceAdvertiser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a4aa1ee1-9d8f-4f4f-93-ee-7d-de-a2-e3-7f-46')
    @winrt_commethod(6)
    def get_ServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceNamePrefixes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ServiceInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_ServiceInfo(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_AutoAcceptSession(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AutoAcceptSession(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_PreferGroupOwnerMode(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_PreferGroupOwnerMode(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PreferredConfigurationMethods(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_commethod(15)
    def get_ServiceStatus(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus: ...
    @winrt_commethod(16)
    def put_ServiceStatus(self, value: Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus) -> Void: ...
    @winrt_commethod(17)
    def get_CustomServiceStatusCode(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_CustomServiceStatusCode(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_DeferredSessionInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(20)
    def put_DeferredSessionInfo(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(21)
    def get_AdvertisementStatus(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertisementStatus: ...
    @winrt_commethod(22)
    def get_ServiceError(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_commethod(23)
    def add_SessionRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_SessionRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_AutoAcceptSessionConnected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_AutoAcceptSessionConnected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_AdvertisementStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_AdvertisementStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def ConnectAsync(self, deviceInfo: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_commethod(30)
    def ConnectAsyncWithPin(self, deviceInfo: Windows.Devices.Enumeration.DeviceInformation, pin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_commethod(31)
    def Start(self) -> Void: ...
    @winrt_commethod(32)
    def Stop(self) -> Void: ...
    ServiceName = property(get_ServiceName, None)
    ServiceNamePrefixes = property(get_ServiceNamePrefixes, None)
    ServiceInfo = property(get_ServiceInfo, put_ServiceInfo)
    AutoAcceptSession = property(get_AutoAcceptSession, put_AutoAcceptSession)
    PreferGroupOwnerMode = property(get_PreferGroupOwnerMode, put_PreferGroupOwnerMode)
    PreferredConfigurationMethods = property(get_PreferredConfigurationMethods, None)
    ServiceStatus = property(get_ServiceStatus, put_ServiceStatus)
    CustomServiceStatusCode = property(get_CustomServiceStatusCode, put_CustomServiceStatusCode)
    DeferredSessionInfo = property(get_DeferredSessionInfo, put_DeferredSessionInfo)
    AdvertisementStatus = property(get_AdvertisementStatus, None)
    ServiceError = property(get_ServiceError, None)
class IWiFiDirectServiceAdvertiserFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3106ac0d-b446-4f13-9f-9a-8a-e9-25-fe-ba-2b')
    @winrt_commethod(6)
    def CreateWiFiDirectServiceAdvertiser(self, serviceName: WinRT_String) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser: ...
class IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dcd9e01e-83df-43e5-8f-43-cb-e8-47-9e-84-eb')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession: ...
    @winrt_commethod(7)
    def get_SessionInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    Session = property(get_Session, None)
    SessionInfo = property(get_SessionInfo, None)
class IWiFiDirectServiceProvisioningInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8bdb7cfe-97d9-45a2-8e-99-db-50-91-0f-b6-a6')
    @winrt_commethod(6)
    def get_SelectedConfigurationMethod(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod: ...
    @winrt_commethod(7)
    def get_IsGroupFormationNeeded(self) -> Boolean: ...
    SelectedConfigurationMethod = property(get_SelectedConfigurationMethod, None)
    IsGroupFormationNeeded = property(get_IsGroupFormationNeeded, None)
class IWiFiDirectServiceRemotePortAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d4cebac1-3fd3-4f0e-b7-bd-78-29-06-f4-44-11')
    @winrt_commethod(6)
    def get_EndpointPairs(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceIPProtocol: ...
    EndpointPairs = property(get_EndpointPairs, None)
    Protocol = property(get_Protocol, None)
class IWiFiDirectServiceSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('81142163-e426-47cb-86-40-e1-b3-58-8b-f2-6f')
    @winrt_commethod(6)
    def get_ServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionStatus: ...
    @winrt_commethod(8)
    def get_ErrorStatus(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionErrorStatus: ...
    @winrt_commethod(9)
    def get_SessionId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_AdvertisementId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_ServiceAddress(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_SessionAddress(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def GetConnectionEndpointPairs(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_commethod(14)
    def add_SessionStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SessionStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def AddStreamSocketListenerAsync(self, value: Windows.Networking.Sockets.StreamSocketListener) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def AddDatagramSocketAsync(self, value: Windows.Networking.Sockets.DatagramSocket) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def add_RemotePortAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceRemotePortAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_RemotePortAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ServiceName = property(get_ServiceName, None)
    Status = property(get_Status, None)
    ErrorStatus = property(get_ErrorStatus, None)
    SessionId = property(get_SessionId, None)
    AdvertisementId = property(get_AdvertisementId, None)
    ServiceAddress = property(get_ServiceAddress, None)
    SessionAddress = property(get_SessionAddress, None)
class IWiFiDirectServiceSessionDeferredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8dfc197f-1201-4f1f-b6-f4-5d-f1-b7-b9-fb-2e')
    @winrt_commethod(6)
    def get_DeferredSessionInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    DeferredSessionInfo = property(get_DeferredSessionInfo, None)
class IWiFiDirectServiceSessionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a0e27c8b-50cb-4a58-9b-cf-e4-72-b9-9f-ba-04')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_ProvisioningInfo(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo: ...
    @winrt_commethod(8)
    def get_SessionInfo(self) -> Windows.Storage.Streams.IBuffer: ...
    DeviceInformation = property(get_DeviceInformation, None)
    ProvisioningInfo = property(get_ProvisioningInfo, None)
    SessionInfo = property(get_SessionInfo, None)
class IWiFiDirectServiceSessionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('74bdcc11-53d6-4999-b4-f8-6c-8e-cc-17-71-e7')
    @winrt_commethod(6)
    def GetSessionRequest(self) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequest: ...
class IWiFiDirectServiceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7db40045-fd74-4688-b7-25-5d-ce-86-ac-f2-33')
    @winrt_commethod(6)
    def GetSelector(self, serviceName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetSelectorWithFilter(self, serviceName: WinRT_String, serviceInfoFilter: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectService]: ...
class WiFiDirectService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectService'
    @winrt_mixinmethod
    def get_RemoteServiceInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_SupportedConfigurationMethods(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_mixinmethod
    def get_PreferGroupOwnerMode(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Boolean: ...
    @winrt_mixinmethod
    def put_PreferGroupOwnerMode(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_SessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceError(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_mixinmethod
    def add_SessionDeferred(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectService, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionDeferredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionDeferred(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetProvisioningInfoAsync(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService, selectedConfigurationMethod: Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo]: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_mixinmethod
    def ConnectAsyncWithPin(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectService, pin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_classmethod
    def GetSelector(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics, serviceName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetSelectorWithFilter(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics, serviceName: WinRT_String, serviceInfoFilter: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectService]: ...
    RemoteServiceInfo = property(get_RemoteServiceInfo, None)
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
    PreferGroupOwnerMode = property(get_PreferGroupOwnerMode, put_PreferGroupOwnerMode)
    SessionInfo = property(get_SessionInfo, put_SessionInfo)
    ServiceError = property(get_ServiceError, None)
WiFiDirectServiceAdvertisementStatus = Int32
WiFiDirectServiceAdvertisementStatus_Created: WiFiDirectServiceAdvertisementStatus = 0
WiFiDirectServiceAdvertisementStatus_Started: WiFiDirectServiceAdvertisementStatus = 1
WiFiDirectServiceAdvertisementStatus_Stopped: WiFiDirectServiceAdvertisementStatus = 2
WiFiDirectServiceAdvertisementStatus_Aborted: WiFiDirectServiceAdvertisementStatus = 3
class WiFiDirectServiceAdvertiser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser'
    @winrt_factorymethod
    def CreateWiFiDirectServiceAdvertiser(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiserFactory, serviceName: WinRT_String) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser: ...
    @winrt_mixinmethod
    def get_ServiceName(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceNamePrefixes(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ServiceInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_ServiceInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_AutoAcceptSession(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoAcceptSession(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PreferGroupOwnerMode(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Boolean: ...
    @winrt_mixinmethod
    def put_PreferGroupOwnerMode(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredConfigurationMethods(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Foundation.Collections.IVector[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_mixinmethod
    def get_ServiceStatus(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus: ...
    @winrt_mixinmethod
    def put_ServiceStatus(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus) -> Void: ...
    @winrt_mixinmethod
    def get_CustomServiceStatusCode(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomServiceStatusCode(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DeferredSessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_DeferredSessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisementStatus(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertisementStatus: ...
    @winrt_mixinmethod
    def get_ServiceError(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_mixinmethod
    def add_SessionRequested(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionRequested(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AutoAcceptSessionConnected(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AutoAcceptSessionConnected(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AdvertisementStatusChanged(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvertisementStatusChanged(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, deviceInfo: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_mixinmethod
    def ConnectAsyncWithPin(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, deviceInfo: Windows.Devices.Enumeration.DeviceInformation, pin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Void: ...
    ServiceName = property(get_ServiceName, None)
    ServiceNamePrefixes = property(get_ServiceNamePrefixes, None)
    ServiceInfo = property(get_ServiceInfo, put_ServiceInfo)
    AutoAcceptSession = property(get_AutoAcceptSession, put_AutoAcceptSession)
    PreferGroupOwnerMode = property(get_PreferGroupOwnerMode, put_PreferGroupOwnerMode)
    PreferredConfigurationMethods = property(get_PreferredConfigurationMethods, None)
    ServiceStatus = property(get_ServiceStatus, put_ServiceStatus)
    CustomServiceStatusCode = property(get_CustomServiceStatusCode, put_CustomServiceStatusCode)
    DeferredSessionInfo = property(get_DeferredSessionInfo, put_DeferredSessionInfo)
    AdvertisementStatus = property(get_AdvertisementStatus, None)
    ServiceError = property(get_ServiceError, None)
class WiFiDirectServiceAutoAcceptSessionConnectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    Session = property(get_Session, None)
    SessionInfo = property(get_SessionInfo, None)
WiFiDirectServiceConfigurationMethod = Int32
WiFiDirectServiceConfigurationMethod_Default: WiFiDirectServiceConfigurationMethod = 0
WiFiDirectServiceConfigurationMethod_PinDisplay: WiFiDirectServiceConfigurationMethod = 1
WiFiDirectServiceConfigurationMethod_PinEntry: WiFiDirectServiceConfigurationMethod = 2
WiFiDirectServiceError = Int32
WiFiDirectServiceError_Success: WiFiDirectServiceError = 0
WiFiDirectServiceError_RadioNotAvailable: WiFiDirectServiceError = 1
WiFiDirectServiceError_ResourceInUse: WiFiDirectServiceError = 2
WiFiDirectServiceError_UnsupportedHardware: WiFiDirectServiceError = 3
WiFiDirectServiceError_NoHardware: WiFiDirectServiceError = 4
WiFiDirectServiceIPProtocol = Int32
WiFiDirectServiceIPProtocol_Tcp: WiFiDirectServiceIPProtocol = 6
WiFiDirectServiceIPProtocol_Udp: WiFiDirectServiceIPProtocol = 17
class WiFiDirectServiceProvisioningInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo'
    @winrt_mixinmethod
    def get_SelectedConfigurationMethod(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceProvisioningInfo) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod: ...
    @winrt_mixinmethod
    def get_IsGroupFormationNeeded(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceProvisioningInfo) -> Boolean: ...
    SelectedConfigurationMethod = property(get_SelectedConfigurationMethod, None)
    IsGroupFormationNeeded = property(get_IsGroupFormationNeeded, None)
class WiFiDirectServiceRemotePortAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceRemotePortAddedEventArgs'
    @winrt_mixinmethod
    def get_EndpointPairs(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceRemotePortAddedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceRemotePortAddedEventArgs) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceIPProtocol: ...
    EndpointPairs = property(get_EndpointPairs, None)
    Protocol = property(get_Protocol, None)
class WiFiDirectServiceSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession'
    @winrt_mixinmethod
    def get_ServiceName(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionStatus: ...
    @winrt_mixinmethod
    def get_ErrorStatus(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionErrorStatus: ...
    @winrt_mixinmethod
    def get_SessionId(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> UInt32: ...
    @winrt_mixinmethod
    def get_AdvertisementId(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> UInt32: ...
    @winrt_mixinmethod
    def get_ServiceAddress(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionAddress(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetConnectionEndpointPairs(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]: ...
    @winrt_mixinmethod
    def add_SessionStatusChanged(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionStatusChanged(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddStreamSocketListenerAsync(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, value: Windows.Networking.Sockets.StreamSocketListener) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def AddDatagramSocketAsync(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, value: Windows.Networking.Sockets.DatagramSocket) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_RemotePortAdded(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, Windows.Devices.WiFiDirect.Services.WiFiDirectServiceRemotePortAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemotePortAdded(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    ServiceName = property(get_ServiceName, None)
    Status = property(get_Status, None)
    ErrorStatus = property(get_ErrorStatus, None)
    SessionId = property(get_SessionId, None)
    AdvertisementId = property(get_AdvertisementId, None)
    ServiceAddress = property(get_ServiceAddress, None)
    SessionAddress = property(get_SessionAddress, None)
class WiFiDirectServiceSessionDeferredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionDeferredEventArgs'
    @winrt_mixinmethod
    def get_DeferredSessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionDeferredEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    DeferredSessionInfo = property(get_DeferredSessionInfo, None)
WiFiDirectServiceSessionErrorStatus = Int32
WiFiDirectServiceSessionErrorStatus_Ok: WiFiDirectServiceSessionErrorStatus = 0
WiFiDirectServiceSessionErrorStatus_Disassociated: WiFiDirectServiceSessionErrorStatus = 1
WiFiDirectServiceSessionErrorStatus_LocalClose: WiFiDirectServiceSessionErrorStatus = 2
WiFiDirectServiceSessionErrorStatus_RemoteClose: WiFiDirectServiceSessionErrorStatus = 3
WiFiDirectServiceSessionErrorStatus_SystemFailure: WiFiDirectServiceSessionErrorStatus = 4
WiFiDirectServiceSessionErrorStatus_NoResponseFromRemote: WiFiDirectServiceSessionErrorStatus = 5
class WiFiDirectServiceSessionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequest'
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_ProvisioningInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DeviceInformation = property(get_DeviceInformation, None)
    ProvisioningInfo = property(get_ProvisioningInfo, None)
    SessionInfo = property(get_SessionInfo, None)
class WiFiDirectServiceSessionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequestedEventArgs'
    @winrt_mixinmethod
    def GetSessionRequest(self: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequestedEventArgs) -> Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequest: ...
WiFiDirectServiceSessionStatus = Int32
WiFiDirectServiceSessionStatus_Closed: WiFiDirectServiceSessionStatus = 0
WiFiDirectServiceSessionStatus_Initiated: WiFiDirectServiceSessionStatus = 1
WiFiDirectServiceSessionStatus_Requested: WiFiDirectServiceSessionStatus = 2
WiFiDirectServiceSessionStatus_Open: WiFiDirectServiceSessionStatus = 3
WiFiDirectServiceStatus = Int32
WiFiDirectServiceStatus_Available: WiFiDirectServiceStatus = 0
WiFiDirectServiceStatus_Busy: WiFiDirectServiceStatus = 1
WiFiDirectServiceStatus_Custom: WiFiDirectServiceStatus = 2
make_head(_module, 'IWiFiDirectService')
make_head(_module, 'IWiFiDirectServiceAdvertiser')
make_head(_module, 'IWiFiDirectServiceAdvertiserFactory')
make_head(_module, 'IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs')
make_head(_module, 'IWiFiDirectServiceProvisioningInfo')
make_head(_module, 'IWiFiDirectServiceRemotePortAddedEventArgs')
make_head(_module, 'IWiFiDirectServiceSession')
make_head(_module, 'IWiFiDirectServiceSessionDeferredEventArgs')
make_head(_module, 'IWiFiDirectServiceSessionRequest')
make_head(_module, 'IWiFiDirectServiceSessionRequestedEventArgs')
make_head(_module, 'IWiFiDirectServiceStatics')
make_head(_module, 'WiFiDirectService')
make_head(_module, 'WiFiDirectServiceAdvertiser')
make_head(_module, 'WiFiDirectServiceAutoAcceptSessionConnectedEventArgs')
make_head(_module, 'WiFiDirectServiceProvisioningInfo')
make_head(_module, 'WiFiDirectServiceRemotePortAddedEventArgs')
make_head(_module, 'WiFiDirectServiceSession')
make_head(_module, 'WiFiDirectServiceSessionDeferredEventArgs')
make_head(_module, 'WiFiDirectServiceSessionRequest')
make_head(_module, 'WiFiDirectServiceSessionRequestedEventArgs')
