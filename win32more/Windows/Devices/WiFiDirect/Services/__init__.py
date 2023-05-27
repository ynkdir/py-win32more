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
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.WiFiDirect.Services
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Sockets
import win32more.Windows.Storage.Streams
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectService'
    _iid_ = Guid('{50aabbb8-5f71-45ec-84f1-a1e4fc7879a3}')
    @winrt_commethod(6)
    def get_RemoteServiceInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_SupportedConfigurationMethods(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_commethod(8)
    def get_PreferGroupOwnerMode(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_PreferGroupOwnerMode(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_SessionInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_SessionInfo(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(12)
    def get_ServiceError(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_commethod(13)
    def add_SessionDeferred(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectService, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionDeferredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_SessionDeferred(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def GetProvisioningInfoAsync(self, selectedConfigurationMethod: win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo]: ...
    @winrt_commethod(16)
    def ConnectAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_commethod(17)
    def ConnectAsyncWithPin(self, pin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    RemoteServiceInfo = property(get_RemoteServiceInfo, None)
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
    PreferGroupOwnerMode = property(get_PreferGroupOwnerMode, put_PreferGroupOwnerMode)
    SessionInfo = property(get_SessionInfo, put_SessionInfo)
    ServiceError = property(get_ServiceError, None)
class IWiFiDirectServiceAdvertiser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser'
    _iid_ = Guid('{a4aa1ee1-9d8f-4f4f-93ee-7ddea2e37f46}')
    @winrt_commethod(6)
    def get_ServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceNamePrefixes(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ServiceInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_ServiceInfo(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_AutoAcceptSession(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AutoAcceptSession(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_PreferGroupOwnerMode(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_PreferGroupOwnerMode(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PreferredConfigurationMethods(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_commethod(15)
    def get_ServiceStatus(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus: ...
    @winrt_commethod(16)
    def put_ServiceStatus(self, value: win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus) -> Void: ...
    @winrt_commethod(17)
    def get_CustomServiceStatusCode(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_CustomServiceStatusCode(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_DeferredSessionInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(20)
    def put_DeferredSessionInfo(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(21)
    def get_AdvertisementStatus(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertisementStatus: ...
    @winrt_commethod(22)
    def get_ServiceError(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_commethod(23)
    def add_SessionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_SessionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_AutoAcceptSessionConnected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_AutoAcceptSessionConnected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_AdvertisementStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_AdvertisementStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def ConnectAsync(self, deviceInfo: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_commethod(30)
    def ConnectAsyncWithPin(self, deviceInfo: win32more.Windows.Devices.Enumeration.DeviceInformation, pin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiserFactory'
    _iid_ = Guid('{3106ac0d-b446-4f13-9f9a-8ae925feba2b}')
    @winrt_commethod(6)
    def CreateWiFiDirectServiceAdvertiser(self, serviceName: WinRT_String) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser: ...
class IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs'
    _iid_ = Guid('{dcd9e01e-83df-43e5-8f43-cbe8479e84eb}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession: ...
    @winrt_commethod(7)
    def get_SessionInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Session = property(get_Session, None)
    SessionInfo = property(get_SessionInfo, None)
class IWiFiDirectServiceProvisioningInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceProvisioningInfo'
    _iid_ = Guid('{8bdb7cfe-97d9-45a2-8e99-db50910fb6a6}')
    @winrt_commethod(6)
    def get_SelectedConfigurationMethod(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod: ...
    @winrt_commethod(7)
    def get_IsGroupFormationNeeded(self) -> Boolean: ...
    SelectedConfigurationMethod = property(get_SelectedConfigurationMethod, None)
    IsGroupFormationNeeded = property(get_IsGroupFormationNeeded, None)
class IWiFiDirectServiceRemotePortAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceRemotePortAddedEventArgs'
    _iid_ = Guid('{d4cebac1-3fd3-4f0e-b7bd-782906f44411}')
    @winrt_commethod(6)
    def get_EndpointPairs(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceIPProtocol: ...
    EndpointPairs = property(get_EndpointPairs, None)
    Protocol = property(get_Protocol, None)
class IWiFiDirectServiceSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession'
    _iid_ = Guid('{81142163-e426-47cb-8640-e1b3588bf26f}')
    @winrt_commethod(6)
    def get_ServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionStatus: ...
    @winrt_commethod(8)
    def get_ErrorStatus(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionErrorStatus: ...
    @winrt_commethod(9)
    def get_SessionId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_AdvertisementId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_ServiceAddress(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_SessionAddress(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def GetConnectionEndpointPairs(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]: ...
    @winrt_commethod(14)
    def add_SessionStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SessionStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def AddStreamSocketListenerAsync(self, value: win32more.Windows.Networking.Sockets.StreamSocketListener) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def AddDatagramSocketAsync(self, value: win32more.Windows.Networking.Sockets.DatagramSocket) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def add_RemotePortAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceRemotePortAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_RemotePortAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ServiceName = property(get_ServiceName, None)
    Status = property(get_Status, None)
    ErrorStatus = property(get_ErrorStatus, None)
    SessionId = property(get_SessionId, None)
    AdvertisementId = property(get_AdvertisementId, None)
    ServiceAddress = property(get_ServiceAddress, None)
    SessionAddress = property(get_SessionAddress, None)
class IWiFiDirectServiceSessionDeferredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionDeferredEventArgs'
    _iid_ = Guid('{8dfc197f-1201-4f1f-b6f4-5df1b7b9fb2e}')
    @winrt_commethod(6)
    def get_DeferredSessionInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeferredSessionInfo = property(get_DeferredSessionInfo, None)
class IWiFiDirectServiceSessionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest'
    _iid_ = Guid('{a0e27c8b-50cb-4a58-9bcf-e472b99fba04}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_ProvisioningInfo(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo: ...
    @winrt_commethod(8)
    def get_SessionInfo(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeviceInformation = property(get_DeviceInformation, None)
    ProvisioningInfo = property(get_ProvisioningInfo, None)
    SessionInfo = property(get_SessionInfo, None)
class IWiFiDirectServiceSessionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequestedEventArgs'
    _iid_ = Guid('{74bdcc11-53d6-4999-b4f8-6c8ecc1771e7}')
    @winrt_commethod(6)
    def GetSessionRequest(self) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequest: ...
class IWiFiDirectServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics'
    _iid_ = Guid('{7db40045-fd74-4688-b725-5dce86acf233}')
    @winrt_commethod(6)
    def GetSelector(self, serviceName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetSelectorWithFilter(self, serviceName: WinRT_String, serviceInfoFilter: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectService]: ...
class WiFiDirectService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectService'
    @winrt_mixinmethod
    def get_RemoteServiceInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_SupportedConfigurationMethods(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_mixinmethod
    def get_PreferGroupOwnerMode(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> Boolean: ...
    @winrt_mixinmethod
    def put_PreferGroupOwnerMode(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_SessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceError(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_mixinmethod
    def add_SessionDeferred(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectService, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionDeferredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionDeferred(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetProvisioningInfoAsync(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService, selectedConfigurationMethod: win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo]: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_mixinmethod
    def ConnectAsyncWithPin(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectService, pin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_classmethod
    def GetSelector(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics, serviceName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetSelectorWithFilter(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics, serviceName: WinRT_String, serviceInfoFilter: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectService]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser'
    @winrt_factorymethod
    def CreateWiFiDirectServiceAdvertiser(cls: Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiserFactory, serviceName: WinRT_String) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser: ...
    @winrt_mixinmethod
    def get_ServiceName(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceNamePrefixes(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ServiceInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_ServiceInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_AutoAcceptSession(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoAcceptSession(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PreferGroupOwnerMode(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Boolean: ...
    @winrt_mixinmethod
    def put_PreferGroupOwnerMode(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredConfigurationMethods(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]: ...
    @winrt_mixinmethod
    def get_ServiceStatus(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus: ...
    @winrt_mixinmethod
    def put_ServiceStatus(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus) -> Void: ...
    @winrt_mixinmethod
    def get_CustomServiceStatusCode(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> UInt32: ...
    @winrt_mixinmethod
    def put_CustomServiceStatusCode(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DeferredSessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_DeferredSessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisementStatus(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertisementStatus: ...
    @winrt_mixinmethod
    def get_ServiceError(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError: ...
    @winrt_mixinmethod
    def add_SessionRequested(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionRequested(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AutoAcceptSessionConnected(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AutoAcceptSessionConnected(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AdvertisementStatusChanged(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertiser, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvertisementStatusChanged(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, deviceInfo: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_mixinmethod
    def ConnectAsyncWithPin(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser, deviceInfo: win32more.Windows.Devices.Enumeration.DeviceInformation, pin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession]: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAdvertiser) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAutoAcceptSessionConnectedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceProvisioningInfo
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo'
    @winrt_mixinmethod
    def get_SelectedConfigurationMethod(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceProvisioningInfo) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod: ...
    @winrt_mixinmethod
    def get_IsGroupFormationNeeded(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceProvisioningInfo) -> Boolean: ...
    SelectedConfigurationMethod = property(get_SelectedConfigurationMethod, None)
    IsGroupFormationNeeded = property(get_IsGroupFormationNeeded, None)
class WiFiDirectServiceRemotePortAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceRemotePortAddedEventArgs
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceRemotePortAddedEventArgs'
    @winrt_mixinmethod
    def get_EndpointPairs(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceRemotePortAddedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]: ...
    @winrt_mixinmethod
    def get_Protocol(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceRemotePortAddedEventArgs) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceIPProtocol: ...
    EndpointPairs = property(get_EndpointPairs, None)
    Protocol = property(get_Protocol, None)
class WiFiDirectServiceSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession'
    @winrt_mixinmethod
    def get_ServiceName(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionStatus: ...
    @winrt_mixinmethod
    def get_ErrorStatus(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionErrorStatus: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> UInt32: ...
    @winrt_mixinmethod
    def get_AdvertisementId(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> UInt32: ...
    @winrt_mixinmethod
    def get_ServiceAddress(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionAddress(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetConnectionEndpointPairs(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]: ...
    @winrt_mixinmethod
    def add_SessionStatusChanged(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionStatusChanged(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddStreamSocketListenerAsync(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, value: win32more.Windows.Networking.Sockets.StreamSocketListener) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def AddDatagramSocketAsync(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, value: win32more.Windows.Networking.Sockets.DatagramSocket) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_RemotePortAdded(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSession, win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceRemotePortAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RemotePortAdded(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ServiceName = property(get_ServiceName, None)
    Status = property(get_Status, None)
    ErrorStatus = property(get_ErrorStatus, None)
    SessionId = property(get_SessionId, None)
    AdvertisementId = property(get_AdvertisementId, None)
    ServiceAddress = property(get_ServiceAddress, None)
    SessionAddress = property(get_SessionAddress, None)
class WiFiDirectServiceSessionDeferredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionDeferredEventArgs
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionDeferredEventArgs'
    @winrt_mixinmethod
    def get_DeferredSessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionDeferredEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeferredSessionInfo = property(get_DeferredSessionInfo, None)
WiFiDirectServiceSessionErrorStatus = Int32
WiFiDirectServiceSessionErrorStatus_Ok: WiFiDirectServiceSessionErrorStatus = 0
WiFiDirectServiceSessionErrorStatus_Disassociated: WiFiDirectServiceSessionErrorStatus = 1
WiFiDirectServiceSessionErrorStatus_LocalClose: WiFiDirectServiceSessionErrorStatus = 2
WiFiDirectServiceSessionErrorStatus_RemoteClose: WiFiDirectServiceSessionErrorStatus = 3
WiFiDirectServiceSessionErrorStatus_SystemFailure: WiFiDirectServiceSessionErrorStatus = 4
WiFiDirectServiceSessionErrorStatus_NoResponseFromRemote: WiFiDirectServiceSessionErrorStatus = 5
class WiFiDirectServiceSessionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequest'
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_ProvisioningInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceProvisioningInfo: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequest) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    DeviceInformation = property(get_DeviceInformation, None)
    ProvisioningInfo = property(get_ProvisioningInfo, None)
    SessionInfo = property(get_SessionInfo, None)
class WiFiDirectServiceSessionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequestedEventArgs
    _classid_ = 'Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequestedEventArgs'
    @winrt_mixinmethod
    def GetSessionRequest(self: win32more.Windows.Devices.WiFiDirect.Services.IWiFiDirectServiceSessionRequestedEventArgs) -> win32more.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionRequest: ...
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
