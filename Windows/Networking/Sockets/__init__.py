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
import Windows.ApplicationModel.Background
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Connectivity
import Windows.Networking.Sockets
import Windows.Security.Credentials
import Windows.Security.Cryptography.Certificates
import Windows.Storage.Streams
import Windows.Web
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BandwidthStatistics(EasyCastStructure):
    OutboundBitsPerSecond: UInt64
    InboundBitsPerSecond: UInt64
    OutboundBitsPerSecondInstability: UInt64
    InboundBitsPerSecondInstability: UInt64
    OutboundBandwidthPeaked: Boolean
    InboundBandwidthPeaked: Boolean
class ControlChannelTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IControlChannelTrigger
    _classid_ = 'Windows.Networking.Sockets.ControlChannelTrigger'
    @winrt_factorymethod
    def CreateControlChannelTrigger(cls: Windows.Networking.Sockets.IControlChannelTriggerFactory, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_factorymethod
    def CreateControlChannelTriggerEx(cls: Windows.Networking.Sockets.IControlChannelTriggerFactory, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32, resourceRequestType: Windows.Networking.Sockets.ControlChannelTriggerResourceType) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_mixinmethod
    def get_ControlChannelTriggerId(self: Windows.Networking.Sockets.IControlChannelTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerKeepAliveIntervalInMinutes(self: Windows.Networking.Sockets.IControlChannelTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def put_ServerKeepAliveIntervalInMinutes(self: Windows.Networking.Sockets.IControlChannelTrigger, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentKeepAliveIntervalInMinutes(self: Windows.Networking.Sockets.IControlChannelTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_TransportObject(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_KeepAliveTrigger(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_PushNotificationTrigger(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def UsingTransport(self: Windows.Networking.Sockets.IControlChannelTrigger, transport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def WaitForPushEnabled(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_mixinmethod
    def DecreaseNetworkKeepAliveInterval(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Void: ...
    @winrt_mixinmethod
    def FlushTransport(self: Windows.Networking.Sockets.IControlChannelTrigger) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_IsWakeFromLowPowerSupported(self: Windows.Networking.Sockets.IControlChannelTrigger2) -> Boolean: ...
    ControlChannelTriggerId = property(get_ControlChannelTriggerId, None)
    ServerKeepAliveIntervalInMinutes = property(get_ServerKeepAliveIntervalInMinutes, put_ServerKeepAliveIntervalInMinutes)
    CurrentKeepAliveIntervalInMinutes = property(get_CurrentKeepAliveIntervalInMinutes, None)
    TransportObject = property(get_TransportObject, None)
    KeepAliveTrigger = property(get_KeepAliveTrigger, None)
    PushNotificationTrigger = property(get_PushNotificationTrigger, None)
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
ControlChannelTriggerContract: UInt32 = 196608
ControlChannelTriggerResetReason = Int32
ControlChannelTriggerResetReason_FastUserSwitched: ControlChannelTriggerResetReason = 0
ControlChannelTriggerResetReason_LowPowerExit: ControlChannelTriggerResetReason = 1
ControlChannelTriggerResetReason_QuietHoursExit: ControlChannelTriggerResetReason = 2
ControlChannelTriggerResetReason_ApplicationRestart: ControlChannelTriggerResetReason = 3
ControlChannelTriggerResourceType = Int32
ControlChannelTriggerResourceType_RequestSoftwareSlot: ControlChannelTriggerResourceType = 0
ControlChannelTriggerResourceType_RequestHardwareSlot: ControlChannelTriggerResourceType = 1
ControlChannelTriggerStatus = Int32
ControlChannelTriggerStatus_HardwareSlotRequested: ControlChannelTriggerStatus = 0
ControlChannelTriggerStatus_SoftwareSlotAllocated: ControlChannelTriggerStatus = 1
ControlChannelTriggerStatus_HardwareSlotAllocated: ControlChannelTriggerStatus = 2
ControlChannelTriggerStatus_PolicyError: ControlChannelTriggerStatus = 3
ControlChannelTriggerStatus_SystemError: ControlChannelTriggerStatus = 4
ControlChannelTriggerStatus_TransportDisconnected: ControlChannelTriggerStatus = 5
ControlChannelTriggerStatus_ServiceUnavailable: ControlChannelTriggerStatus = 6
class DatagramSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IDatagramSocket
    _classid_ = 'Windows.Networking.Sockets.DatagramSocket'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IDatagramSocket) -> Windows.Networking.Sockets.DatagramSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IDatagramSocket) -> Windows.Networking.Sockets.DatagramSocketInformation: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IDatagramSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IDatagramSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAsync(self: Windows.Networking.Sockets.IDatagramSocket, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindServiceNameAsync(self: Windows.Networking.Sockets.IDatagramSocket, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindEndpointAsync(self: Windows.Networking.Sockets.IDatagramSocket, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def JoinMulticastGroup(self: Windows.Networking.Sockets.IDatagramSocket, host: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def GetOutputStreamAsync(self: Windows.Networking.Sockets.IDatagramSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_mixinmethod
    def GetOutputStreamWithEndpointPairAsync(self: Windows.Networking.Sockets.IDatagramSocket, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Networking.Sockets.IDatagramSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.DatagramSocket, Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Networking.Sockets.IDatagramSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def BindServiceNameAndAdapterAsync(self: Windows.Networking.Sockets.IDatagramSocket2, localServiceName: WinRT_String, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: Windows.Networking.Sockets.IDatagramSocket3) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: Windows.Networking.Sockets.IDatagramSocket3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: Windows.Networking.Sockets.IDatagramSocket3, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContextAndKeepAliveTime(self: Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def GetEndpointPairsAsync(cls: Windows.Networking.Sockets.IDatagramSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_classmethod
    def GetEndpointPairsWithSortOptionsAsync(cls: Windows.Networking.Sockets.IDatagramSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class DatagramSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IDatagramSocketControl
    _classid_ = 'Windows.Networking.Sockets.DatagramSocketControl'
    @winrt_mixinmethod
    def get_QualityOfService(self: Windows.Networking.Sockets.IDatagramSocketControl) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: Windows.Networking.Sockets.IDatagramSocketControl, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IDatagramSocketControl) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IDatagramSocketControl, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_InboundBufferSizeInBytes(self: Windows.Networking.Sockets.IDatagramSocketControl2) -> UInt32: ...
    @winrt_mixinmethod
    def put_InboundBufferSizeInBytes(self: Windows.Networking.Sockets.IDatagramSocketControl2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DontFragment(self: Windows.Networking.Sockets.IDatagramSocketControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_DontFragment(self: Windows.Networking.Sockets.IDatagramSocketControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MulticastOnly(self: Windows.Networking.Sockets.IDatagramSocketControl3) -> Boolean: ...
    @winrt_mixinmethod
    def put_MulticastOnly(self: Windows.Networking.Sockets.IDatagramSocketControl3, value: Boolean) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
    InboundBufferSizeInBytes = property(get_InboundBufferSizeInBytes, put_InboundBufferSizeInBytes)
    DontFragment = property(get_DontFragment, put_DontFragment)
    MulticastOnly = property(get_MulticastOnly, put_MulticastOnly)
class DatagramSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IDatagramSocketInformation
    _classid_ = 'Windows.Networking.Sockets.DatagramSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteAddress(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.Sockets.IDatagramSocketInformation) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
class DatagramSocketMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs
    _classid_ = 'Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_RemoteAddress(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def GetDataReader(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.DataReader: ...
    @winrt_mixinmethod
    def GetDataStream(self: Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.IInputStream: ...
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
    LocalAddress = property(get_LocalAddress, None)
class IControlChannelTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTrigger'
    _iid_ = Guid('{7d1431a7-ee96-40e8-a199-8703cd969ec3}')
    @winrt_commethod(6)
    def get_ControlChannelTriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServerKeepAliveIntervalInMinutes(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ServerKeepAliveIntervalInMinutes(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_CurrentKeepAliveIntervalInMinutes(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_TransportObject(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def get_KeepAliveTrigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(12)
    def get_PushNotificationTrigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(13)
    def UsingTransport(self, transport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(14)
    def WaitForPushEnabled(self) -> Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_commethod(15)
    def DecreaseNetworkKeepAliveInterval(self) -> Void: ...
    @winrt_commethod(16)
    def FlushTransport(self) -> Void: ...
    ControlChannelTriggerId = property(get_ControlChannelTriggerId, None)
    ServerKeepAliveIntervalInMinutes = property(get_ServerKeepAliveIntervalInMinutes, put_ServerKeepAliveIntervalInMinutes)
    CurrentKeepAliveIntervalInMinutes = property(get_CurrentKeepAliveIntervalInMinutes, None)
    TransportObject = property(get_TransportObject, None)
    KeepAliveTrigger = property(get_KeepAliveTrigger, None)
    PushNotificationTrigger = property(get_PushNotificationTrigger, None)
class IControlChannelTrigger2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTrigger2'
    _iid_ = Guid('{af00d237-51be-4514-9725-3556e1879580}')
    @winrt_commethod(6)
    def get_IsWakeFromLowPowerSupported(self) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class IControlChannelTriggerEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTriggerEventDetails'
    _iid_ = Guid('{1b36e047-89bb-4236-96ac-71d012bb4869}')
    @winrt_commethod(6)
    def get_ControlChannelTrigger(self) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    ControlChannelTrigger = property(get_ControlChannelTrigger, None)
class IControlChannelTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTriggerFactory'
    _iid_ = Guid('{da4b7cf0-8d71-446f-88c3-b95184a2d6cd}')
    @winrt_commethod(6)
    def CreateControlChannelTrigger(self, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_commethod(7)
    def CreateControlChannelTriggerEx(self, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32, resourceRequestType: Windows.Networking.Sockets.ControlChannelTriggerResourceType) -> Windows.Networking.Sockets.ControlChannelTrigger: ...
class IControlChannelTriggerResetEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTriggerResetEventDetails'
    _iid_ = Guid('{6851038e-8ec4-42fe-9bb2-21e91b7bfcb1}')
    @winrt_commethod(6)
    def get_ResetReason(self) -> Windows.Networking.Sockets.ControlChannelTriggerResetReason: ...
    @winrt_commethod(7)
    def get_HardwareSlotReset(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SoftwareSlotReset(self) -> Boolean: ...
    ResetReason = property(get_ResetReason, None)
    HardwareSlotReset = property(get_HardwareSlotReset, None)
    SoftwareSlotReset = property(get_SoftwareSlotReset, None)
class IDatagramSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocket'
    _iid_ = Guid('{7fe25bbb-c3bc-4677-8446-ca28a465a3af}')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.DatagramSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.DatagramSocketInformation: ...
    @winrt_commethod(8)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def ConnectAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ConnectWithEndpointPairAsync(self, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def BindServiceNameAsync(self, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def BindEndpointAsync(self, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def JoinMulticastGroup(self, host: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(14)
    def GetOutputStreamAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_commethod(15)
    def GetOutputStreamWithEndpointPairAsync(self, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IOutputStream]: ...
    @winrt_commethod(16)
    def add_MessageReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.DatagramSocket, Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class IDatagramSocket2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocket2'
    _iid_ = Guid('{d83ba354-9a9d-4185-a20a-1424c9c2a7cd}')
    @winrt_commethod(6)
    def BindServiceNameAndAdapterAsync(self, localServiceName: WinRT_String, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
class IDatagramSocket3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocket3'
    _iid_ = Guid('{37544f09-ab92-4306-9ac1-0c381283d9c6}')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_commethod(11)
    def TransferOwnershipWithContextAndKeepAliveTime(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
class IDatagramSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketControl'
    _iid_ = Guid('{52ac3f2e-349a-4135-bb58-b79b2647d390}')
    @winrt_commethod(6)
    def get_QualityOfService(self) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(7)
    def put_QualityOfService(self, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_commethod(8)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(9)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IDatagramSocketControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketControl2'
    _iid_ = Guid('{33ead5c2-979c-4415-82a1-3cfaf646c192}')
    @winrt_commethod(6)
    def get_InboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_InboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_DontFragment(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_DontFragment(self, value: Boolean) -> Void: ...
    InboundBufferSizeInBytes = property(get_InboundBufferSizeInBytes, put_InboundBufferSizeInBytes)
    DontFragment = property(get_DontFragment, put_DontFragment)
class IDatagramSocketControl3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketControl3'
    _iid_ = Guid('{d4eb8256-1f6d-4598-9b57-d42a001df349}')
    @winrt_commethod(6)
    def get_MulticastOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_MulticastOnly(self, value: Boolean) -> Void: ...
    MulticastOnly = property(get_MulticastOnly, put_MulticastOnly)
class IDatagramSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketInformation'
    _iid_ = Guid('{5f1a569a-55fb-48cd-9706-7a974f7b1585}')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_LocalPort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def get_RemotePort(self) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
class IDatagramSocketMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs'
    _iid_ = Guid('{9e2ddca2-1712-4ce4-b179-8c652c6d107e}')
    @winrt_commethod(6)
    def get_RemoteAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def GetDataReader(self) -> Windows.Storage.Streams.DataReader: ...
    @winrt_commethod(10)
    def GetDataStream(self) -> Windows.Storage.Streams.IInputStream: ...
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
    LocalAddress = property(get_LocalAddress, None)
class IDatagramSocketStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketStatics'
    _iid_ = Guid('{e9c62aee-1494-4a21-bb7e-8589fc751d9d}')
    @winrt_commethod(6)
    def GetEndpointPairsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_commethod(7)
    def GetEndpointPairsWithSortOptionsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
class IMessageWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocket'
    _iid_ = Guid('{33727d08-34d5-4746-ad7b-8dde5bc2ef88}')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.MessageWebSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.MessageWebSocketInformation: ...
    @winrt_commethod(8)
    def add_MessageReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class IMessageWebSocket2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocket2'
    _iid_ = Guid('{bed0cee7-f9c8-440a-9ad5-737281d9742e}')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMessageWebSocket3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocket3'
    _iid_ = Guid('{59d9defb-71af-4349-8487-911fcf681597}')
    @winrt_commethod(6)
    def SendNonfinalFrameAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(7)
    def SendFinalFrameAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
class IMessageWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketControl'
    _iid_ = Guid('{8118388a-c629-4f0a-80fb-81fc05538862}')
    @winrt_commethod(6)
    def get_MaxMessageSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MaxMessageSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_MessageType(self) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(9)
    def put_MessageType(self, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MaxMessageSize = property(get_MaxMessageSize, put_MaxMessageSize)
    MessageType = property(get_MessageType, put_MessageType)
class IMessageWebSocketControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketControl2'
    _iid_ = Guid('{e30fd791-080c-400a-a712-27dfa9e744d8}')
    @winrt_commethod(6)
    def get_DesiredUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DesiredUnsolicitedPongInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ActualUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ReceiveMode(self) -> Windows.Networking.Sockets.MessageWebSocketReceiveMode: ...
    @winrt_commethod(10)
    def put_ReceiveMode(self, value: Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> Void: ...
    @winrt_commethod(11)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(12)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ReceiveMode = property(get_ReceiveMode, put_ReceiveMode)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IMessageWebSocketMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs'
    _iid_ = Guid('{478c22ac-4c4b-42ed-9ed7-1ef9f94fa3d5}')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(7)
    def GetDataReader(self) -> Windows.Storage.Streams.DataReader: ...
    @winrt_commethod(8)
    def GetDataStream(self) -> Windows.Storage.Streams.IInputStream: ...
    MessageType = property(get_MessageType, None)
class IMessageWebSocketMessageReceivedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs2'
    _iid_ = Guid('{89ce06fd-dd6f-4a07-87f9-f9eb4d89d83d}')
    @winrt_commethod(6)
    def get_IsMessageComplete(self) -> Boolean: ...
    IsMessageComplete = property(get_IsMessageComplete, None)
class IServerMessageWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerMessageWebSocket'
    _iid_ = Guid('{e3ac9240-813b-5efd-7e11-ae2305fc77f1}')
    @winrt_commethod(6)
    def add_MessageReceived(self, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Control(self) -> Windows.Networking.Sockets.ServerMessageWebSocketControl: ...
    @winrt_commethod(9)
    def get_Information(self) -> Windows.Networking.Sockets.ServerMessageWebSocketInformation: ...
    @winrt_commethod(10)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(11)
    def add_Closed(self, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class IServerMessageWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerMessageWebSocketControl'
    _iid_ = Guid('{69c2f051-1c1f-587a-4519-2181610192b7}')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(7)
    def put_MessageType(self, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MessageType = property(get_MessageType, put_MessageType)
class IServerMessageWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerMessageWebSocketInformation'
    _iid_ = Guid('{fc32b45f-4448-5505-6cc9-09afa8915f5d}')
    @winrt_commethod(6)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class IServerStreamWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerStreamWebSocket'
    _iid_ = Guid('{2ced5bbf-74f6-55e4-79df-9132680dfee8}')
    @winrt_commethod(6)
    def get_Information(self) -> Windows.Networking.Sockets.ServerStreamWebSocketInformation: ...
    @winrt_commethod(7)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(8)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def add_Closed(self, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerStreamWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class IServerStreamWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerStreamWebSocketInformation'
    _iid_ = Guid('{fc32b45f-4448-5505-6cc9-09aba8915f5d}')
    @winrt_commethod(6)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class ISocketActivityContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityContext'
    _iid_ = Guid('{43b04d64-4c85-4396-a637-1d973f6ebd49}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
class ISocketActivityContextFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityContextFactory'
    _iid_ = Guid('{b99fc3c3-088c-4388-83ae-2525138e049a}')
    @winrt_commethod(6)
    def Create(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Networking.Sockets.SocketActivityContext: ...
class ISocketActivityInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityInformation'
    _iid_ = Guid('{8d8a42e4-a87e-4b74-9968-185b2511defe}')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SocketKind(self) -> Windows.Networking.Sockets.SocketActivityKind: ...
    @winrt_commethod(9)
    def get_Context(self) -> Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_commethod(10)
    def get_DatagramSocket(self) -> Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_commethod(11)
    def get_StreamSocket(self) -> Windows.Networking.Sockets.StreamSocket: ...
    @winrt_commethod(12)
    def get_StreamSocketListener(self) -> Windows.Networking.Sockets.StreamSocketListener: ...
    TaskId = property(get_TaskId, None)
    Id = property(get_Id, None)
    SocketKind = property(get_SocketKind, None)
    Context = property(get_Context, None)
    DatagramSocket = property(get_DatagramSocket, None)
    StreamSocket = property(get_StreamSocket, None)
    StreamSocketListener = property(get_StreamSocketListener, None)
class ISocketActivityInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityInformationStatics'
    _iid_ = Guid('{8570b47a-7e7d-4736-8041-1327a6543c56}')
    @winrt_commethod(6)
    def get_AllSockets(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Networking.Sockets.SocketActivityInformation]: ...
    AllSockets = property(get_AllSockets, None)
class ISocketActivityTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityTriggerDetails'
    _iid_ = Guid('{45f406a7-fc9f-4f81-acad-355fef51e67b}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Networking.Sockets.SocketActivityTriggerReason: ...
    @winrt_commethod(7)
    def get_SocketInformation(self) -> Windows.Networking.Sockets.SocketActivityInformation: ...
    Reason = property(get_Reason, None)
    SocketInformation = property(get_SocketInformation, None)
class ISocketErrorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketErrorStatics'
    _iid_ = Guid('{828337f4-7d56-4d8e-b7b4-a07dd7c1bca9}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> Windows.Networking.Sockets.SocketErrorStatus: ...
class IStreamSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocket'
    _iid_ = Guid('{69a22cf3-fc7b-4857-af38-f6e7de6a5b49}')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.StreamSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.StreamSocketInformation: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(9)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(10)
    def ConnectWithEndpointPairAsync(self, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ConnectAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ConnectWithEndpointPairAndProtectionLevelAsync(self, endpointPair: Windows.Networking.EndpointPair, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ConnectWithProtectionLevelAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def UpgradeToSslAsync(self, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, validationHostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncAction: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class IStreamSocket2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocket2'
    _iid_ = Guid('{29d0e575-f314-4d09-adf0-0fbd967fbd9f}')
    @winrt_commethod(6)
    def ConnectWithProtectionLevelAndAdapterAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
class IStreamSocket3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocket3'
    _iid_ = Guid('{3f430b00-9d28-4854-bac3-2301941ec223}')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_commethod(11)
    def TransferOwnershipWithContextAndKeepAliveTime(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
class IStreamSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl'
    _iid_ = Guid('{fe25adf1-92ab-4af3-9992-0f4c85e36cc4}')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_KeepAlive(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_KeepAlive(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_QualityOfService(self) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(13)
    def put_QualityOfService(self, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_commethod(14)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(15)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IStreamSocketControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl2'
    _iid_ = Guid('{c2d09a56-060f-44c1-b8e2-1fbf60bd62c5}')
    @winrt_commethod(6)
    def get_IgnorableServerCertificateErrors(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
class IStreamSocketControl3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl3'
    _iid_ = Guid('{c56a444c-4e74-403e-894c-b31cae5c7342}')
    @winrt_commethod(6)
    def get_SerializeConnectionAttempts(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SerializeConnectionAttempts(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    SerializeConnectionAttempts = property(get_SerializeConnectionAttempts, put_SerializeConnectionAttempts)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IStreamSocketControl4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl4'
    _iid_ = Guid('{964e2b3d-ec27-4888-b3ce-c74b418423ad}')
    @winrt_commethod(6)
    def get_MinProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(7)
    def put_MinProtectionLevel(self, value: Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    MinProtectionLevel = property(get_MinProtectionLevel, put_MinProtectionLevel)
class IStreamSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketInformation'
    _iid_ = Guid('{3b80ae30-5e68-4205-88f0-dc85d2e25ded}')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_LocalPort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def get_RemoteAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(10)
    def get_RemoteServiceName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_RoundTripTimeStatistics(self) -> Windows.Networking.Sockets.RoundTripTimeStatistics: ...
    @winrt_commethod(13)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(14)
    def get_ProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(15)
    def get_SessionKey(self) -> Windows.Storage.Streams.IBuffer: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemoteServiceName = property(get_RemoteServiceName, None)
    RemotePort = property(get_RemotePort, None)
    RoundTripTimeStatistics = property(get_RoundTripTimeStatistics, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    SessionKey = property(get_SessionKey, None)
class IStreamSocketInformation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketInformation2'
    _iid_ = Guid('{12c28452-4bdc-4ee4-976a-cf130e9d92e3}')
    @winrt_commethod(6)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(8)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IStreamSocketListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListener'
    _iid_ = Guid('{ff513437-df9f-4df0-bf82-0ec5d7b35aae}')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.StreamSocketListenerControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.StreamSocketListenerInformation: ...
    @winrt_commethod(8)
    def BindServiceNameAsync(self, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def BindEndpointAsync(self, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def add_ConnectionReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamSocketListener, Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ConnectionReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class IStreamSocketListener2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListener2'
    _iid_ = Guid('{658dc13e-bb3e-4458-b232-ed1088694b98}')
    @winrt_commethod(6)
    def BindServiceNameWithProtectionLevelAsync(self, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def BindServiceNameWithProtectionLevelAndAdapterAsync(self, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
class IStreamSocketListener3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListener3'
    _iid_ = Guid('{4798201c-bdf8-4919-8542-28d450e74507}')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
class IStreamSocketListenerConnectionReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs'
    _iid_ = Guid('{0c472ea9-373f-447b-85b1-ddd4548803ba}')
    @winrt_commethod(6)
    def get_Socket(self) -> Windows.Networking.Sockets.StreamSocket: ...
    Socket = property(get_Socket, None)
class IStreamSocketListenerControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerControl'
    _iid_ = Guid('{20d8c576-8d8a-4dba-9722-a16c4d984980}')
    @winrt_commethod(6)
    def get_QualityOfService(self) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(7)
    def put_QualityOfService(self, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
class IStreamSocketListenerControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerControl2'
    _iid_ = Guid('{948bb665-2c3e-404b-b8b0-8eb249a2b0a1}')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_KeepAlive(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_KeepAlive(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(13)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IStreamSocketListenerInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerInformation'
    _iid_ = Guid('{e62ba82f-a63a-430b-bf62-29e93e5633b4}')
    @winrt_commethod(6)
    def get_LocalPort(self) -> WinRT_String: ...
    LocalPort = property(get_LocalPort, None)
class IStreamSocketStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketStatics'
    _iid_ = Guid('{a420bc4a-6e2e-4af5-b556-355ae0cd4f29}')
    @winrt_commethod(6)
    def GetEndpointPairsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_commethod(7)
    def GetEndpointPairsWithSortOptionsAsync(self, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
class IStreamWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocket'
    _iid_ = Guid('{bd4a49d8-b289-45bb-97eb-c7525205a843}')
    @winrt_commethod(6)
    def get_Control(self) -> Windows.Networking.Sockets.StreamWebSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> Windows.Networking.Sockets.StreamWebSocketInformation: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
class IStreamWebSocket2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocket2'
    _iid_ = Guid('{aa4d08cb-93f5-4678-8236-57cce5417ed5}')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IStreamWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocketControl'
    _iid_ = Guid('{b4f478b1-a45a-48db-953a-645b7d964c07}')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
class IStreamWebSocketControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocketControl2'
    _iid_ = Guid('{215d9f7e-fa58-40da-9f11-a48dafe95037}')
    @winrt_commethod(6)
    def get_DesiredUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DesiredUnsolicitedPongInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ActualUnsolicitedPongInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(10)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocket'
    _iid_ = Guid('{f877396f-99b1-4e18-bc08-850c9adf156e}')
    @winrt_commethod(6)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(7)
    def ConnectAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def add_Closed(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.IWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    OutputStream = property(get_OutputStream, None)
class IWebSocketClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketClosedEventArgs'
    _iid_ = Guid('{ceb78d07-d0a8-4703-a091-c8c2c0915bc3}')
    @winrt_commethod(6)
    def get_Code(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Reason(self) -> WinRT_String: ...
    Code = property(get_Code, None)
    Reason = property(get_Reason, None)
class IWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketControl'
    _iid_ = Guid('{2ec4bdc3-d9a5-455a-9811-de24d45337e9}')
    @winrt_commethod(6)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_ServerCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(9)
    def put_ServerCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(10)
    def get_ProxyCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(11)
    def put_ProxyCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedProtocols(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
class IWebSocketControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketControl2'
    _iid_ = Guid('{79c3be03-f2ca-461e-af4e-9665bc2d0620}')
    @winrt_commethod(6)
    def get_IgnorableServerCertificateErrors(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
class IWebSocketErrorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketErrorStatics'
    _iid_ = Guid('{27cdf35b-1f61-4709-8e02-61283ada4e9d}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> Windows.Web.WebErrorStatus: ...
class IWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketInformation'
    _iid_ = Guid('{5e01e316-c92a-47a5-b25f-07847639d181}')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_BandwidthStatistics(self) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(8)
    def get_Protocol(self) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
class IWebSocketInformation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketInformation2'
    _iid_ = Guid('{ce1d39ce-a1b7-4d43-8269-8d5b981bd47a}')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IWebSocketServerCustomValidationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs'
    _iid_ = Guid('{ffeffe48-022a-4ab7-8b36-e10af4640e6b}')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(10)
    def Reject(self) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class MessageWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IMessageWebSocket
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocket'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Sockets.MessageWebSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IMessageWebSocket) -> Windows.Networking.Sockets.MessageWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IMessageWebSocket) -> Windows.Networking.Sockets.MessageWebSocketInformation: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Networking.Sockets.IMessageWebSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Networking.Sockets.IMessageWebSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IWebSocket, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.Sockets.IWebSocket, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IWebSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.IWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IWebSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IMessageWebSocket2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.MessageWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IMessageWebSocket2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SendNonfinalFrameAsync(self: Windows.Networking.Sockets.IMessageWebSocket3, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def SendFinalFrameAsync(self: Windows.Networking.Sockets.IMessageWebSocket3, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class MessageWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IMessageWebSocketControl
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocketControl'
    @winrt_mixinmethod
    def get_MaxMessageSize(self: Windows.Networking.Sockets.IMessageWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxMessageSize(self: Windows.Networking.Sockets.IMessageWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Sockets.IMessageWebSocketControl) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def put_MessageType(self: Windows.Networking.Sockets.IMessageWebSocketControl, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedProtocols(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketControl2) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IMessageWebSocketControl2, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ActualUnsolicitedPongInterval(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ReceiveMode(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Networking.Sockets.MessageWebSocketReceiveMode: ...
    @winrt_mixinmethod
    def put_ReceiveMode(self: Windows.Networking.Sockets.IMessageWebSocketControl2, value: Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> Void: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Networking.Sockets.IMessageWebSocketControl2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Networking.Sockets.IMessageWebSocketControl2, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    MaxMessageSize = property(get_MaxMessageSize, put_MaxMessageSize)
    MessageType = property(get_MessageType, put_MessageType)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ReceiveMode = property(get_ReceiveMode, put_ReceiveMode)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class MessageWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class MessageWebSocketMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def GetDataReader(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.DataReader: ...
    @winrt_mixinmethod
    def GetDataStream(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_IsMessageComplete(self: Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs2) -> Boolean: ...
    MessageType = property(get_MessageType, None)
    IsMessageComplete = property(get_IsMessageComplete, None)
MessageWebSocketReceiveMode = Int32
MessageWebSocketReceiveMode_FullMessage: MessageWebSocketReceiveMode = 0
MessageWebSocketReceiveMode_PartialMessage: MessageWebSocketReceiveMode = 1
class RoundTripTimeStatistics(EasyCastStructure):
    Variance: UInt32
    Max: UInt32
    Min: UInt32
    Sum: UInt32
class ServerMessageWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IServerMessageWebSocket
    _classid_ = 'Windows.Networking.Sockets.ServerMessageWebSocket'
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Networking.Sockets.IServerMessageWebSocket, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Networking.Sockets.IServerMessageWebSocket, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IServerMessageWebSocket) -> Windows.Networking.Sockets.ServerMessageWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IServerMessageWebSocket) -> Windows.Networking.Sockets.ServerMessageWebSocketInformation: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IServerMessageWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IServerMessageWebSocket, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerMessageWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IServerMessageWebSocket, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IServerMessageWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class ServerMessageWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IServerMessageWebSocketControl
    _classid_ = 'Windows.Networking.Sockets.ServerMessageWebSocketControl'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Networking.Sockets.IServerMessageWebSocketControl) -> Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def put_MessageType(self: Windows.Networking.Sockets.IServerMessageWebSocketControl, value: Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MessageType = property(get_MessageType, put_MessageType)
class ServerMessageWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IServerMessageWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.ServerMessageWebSocketInformation'
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class ServerStreamWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IServerStreamWebSocket
    _classid_ = 'Windows.Networking.Sockets.ServerStreamWebSocket'
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IServerStreamWebSocket) -> Windows.Networking.Sockets.ServerStreamWebSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Networking.Sockets.IServerStreamWebSocket) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IServerStreamWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IServerStreamWebSocket, value: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.ServerStreamWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IServerStreamWebSocket, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IServerStreamWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class ServerStreamWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IServerStreamWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.ServerStreamWebSocketInformation'
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
SocketActivityConnectedStandbyAction = Int32
SocketActivityConnectedStandbyAction_DoNotWake: SocketActivityConnectedStandbyAction = 0
SocketActivityConnectedStandbyAction_Wake: SocketActivityConnectedStandbyAction = 1
class SocketActivityContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.ISocketActivityContext
    _classid_ = 'Windows.Networking.Sockets.SocketActivityContext'
    @winrt_factorymethod
    def Create(cls: Windows.Networking.Sockets.ISocketActivityContextFactory, data: Windows.Storage.Streams.IBuffer) -> Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Networking.Sockets.ISocketActivityContext) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
class _SocketActivityInformation_Meta_(ComPtr.__class__):
    pass
class SocketActivityInformation(ComPtr, metaclass=_SocketActivityInformation_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.ISocketActivityInformation
    _classid_ = 'Windows.Networking.Sockets.SocketActivityInformation'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.Sockets.ISocketActivityInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SocketKind(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.SocketActivityKind: ...
    @winrt_mixinmethod
    def get_Context(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_mixinmethod
    def get_DatagramSocket(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_mixinmethod
    def get_StreamSocket(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_StreamSocketListener(self: Windows.Networking.Sockets.ISocketActivityInformation) -> Windows.Networking.Sockets.StreamSocketListener: ...
    @winrt_classmethod
    def get_AllSockets(cls: Windows.Networking.Sockets.ISocketActivityInformationStatics) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Networking.Sockets.SocketActivityInformation]: ...
    TaskId = property(get_TaskId, None)
    Id = property(get_Id, None)
    SocketKind = property(get_SocketKind, None)
    Context = property(get_Context, None)
    DatagramSocket = property(get_DatagramSocket, None)
    StreamSocket = property(get_StreamSocket, None)
    StreamSocketListener = property(get_StreamSocketListener, None)
    _SocketActivityInformation_Meta_.AllSockets = property(get_AllSockets.__wrapped__, None)
SocketActivityKind = Int32
SocketActivityKind_None: SocketActivityKind = 0
SocketActivityKind_StreamSocketListener: SocketActivityKind = 1
SocketActivityKind_DatagramSocket: SocketActivityKind = 2
SocketActivityKind_StreamSocket: SocketActivityKind = 3
class SocketActivityTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.ISocketActivityTriggerDetails
    _classid_ = 'Windows.Networking.Sockets.SocketActivityTriggerDetails'
    @winrt_mixinmethod
    def get_Reason(self: Windows.Networking.Sockets.ISocketActivityTriggerDetails) -> Windows.Networking.Sockets.SocketActivityTriggerReason: ...
    @winrt_mixinmethod
    def get_SocketInformation(self: Windows.Networking.Sockets.ISocketActivityTriggerDetails) -> Windows.Networking.Sockets.SocketActivityInformation: ...
    Reason = property(get_Reason, None)
    SocketInformation = property(get_SocketInformation, None)
SocketActivityTriggerReason = Int32
SocketActivityTriggerReason_None: SocketActivityTriggerReason = 0
SocketActivityTriggerReason_SocketActivity: SocketActivityTriggerReason = 1
SocketActivityTriggerReason_ConnectionAccepted: SocketActivityTriggerReason = 2
SocketActivityTriggerReason_KeepAliveTimerExpired: SocketActivityTriggerReason = 3
SocketActivityTriggerReason_SocketClosed: SocketActivityTriggerReason = 4
class SocketError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.SocketError'
    @winrt_classmethod
    def GetStatus(cls: Windows.Networking.Sockets.ISocketErrorStatics, hresult: Int32) -> Windows.Networking.Sockets.SocketErrorStatus: ...
SocketErrorStatus = Int32
SocketErrorStatus_Unknown: SocketErrorStatus = 0
SocketErrorStatus_OperationAborted: SocketErrorStatus = 1
SocketErrorStatus_HttpInvalidServerResponse: SocketErrorStatus = 2
SocketErrorStatus_ConnectionTimedOut: SocketErrorStatus = 3
SocketErrorStatus_AddressFamilyNotSupported: SocketErrorStatus = 4
SocketErrorStatus_SocketTypeNotSupported: SocketErrorStatus = 5
SocketErrorStatus_HostNotFound: SocketErrorStatus = 6
SocketErrorStatus_NoDataRecordOfRequestedType: SocketErrorStatus = 7
SocketErrorStatus_NonAuthoritativeHostNotFound: SocketErrorStatus = 8
SocketErrorStatus_ClassTypeNotFound: SocketErrorStatus = 9
SocketErrorStatus_AddressAlreadyInUse: SocketErrorStatus = 10
SocketErrorStatus_CannotAssignRequestedAddress: SocketErrorStatus = 11
SocketErrorStatus_ConnectionRefused: SocketErrorStatus = 12
SocketErrorStatus_NetworkIsUnreachable: SocketErrorStatus = 13
SocketErrorStatus_UnreachableHost: SocketErrorStatus = 14
SocketErrorStatus_NetworkIsDown: SocketErrorStatus = 15
SocketErrorStatus_NetworkDroppedConnectionOnReset: SocketErrorStatus = 16
SocketErrorStatus_SoftwareCausedConnectionAbort: SocketErrorStatus = 17
SocketErrorStatus_ConnectionResetByPeer: SocketErrorStatus = 18
SocketErrorStatus_HostIsDown: SocketErrorStatus = 19
SocketErrorStatus_NoAddressesFound: SocketErrorStatus = 20
SocketErrorStatus_TooManyOpenFiles: SocketErrorStatus = 21
SocketErrorStatus_MessageTooLong: SocketErrorStatus = 22
SocketErrorStatus_CertificateExpired: SocketErrorStatus = 23
SocketErrorStatus_CertificateUntrustedRoot: SocketErrorStatus = 24
SocketErrorStatus_CertificateCommonNameIsIncorrect: SocketErrorStatus = 25
SocketErrorStatus_CertificateWrongUsage: SocketErrorStatus = 26
SocketErrorStatus_CertificateRevoked: SocketErrorStatus = 27
SocketErrorStatus_CertificateNoRevocationCheck: SocketErrorStatus = 28
SocketErrorStatus_CertificateRevocationServerOffline: SocketErrorStatus = 29
SocketErrorStatus_CertificateIsInvalid: SocketErrorStatus = 30
SocketMessageType = Int32
SocketMessageType_Binary: SocketMessageType = 0
SocketMessageType_Utf8: SocketMessageType = 1
SocketProtectionLevel = Int32
SocketProtectionLevel_PlainSocket: SocketProtectionLevel = 0
SocketProtectionLevel_Ssl: SocketProtectionLevel = 1
SocketProtectionLevel_SslAllowNullEncryption: SocketProtectionLevel = 2
SocketProtectionLevel_BluetoothEncryptionAllowNullAuthentication: SocketProtectionLevel = 3
SocketProtectionLevel_BluetoothEncryptionWithAuthentication: SocketProtectionLevel = 4
SocketProtectionLevel_Ssl3AllowWeakEncryption: SocketProtectionLevel = 5
SocketProtectionLevel_Tls10: SocketProtectionLevel = 6
SocketProtectionLevel_Tls11: SocketProtectionLevel = 7
SocketProtectionLevel_Tls12: SocketProtectionLevel = 8
SocketProtectionLevel_Unspecified: SocketProtectionLevel = 9
SocketQualityOfService = Int32
SocketQualityOfService_Normal: SocketQualityOfService = 0
SocketQualityOfService_LowLatency: SocketQualityOfService = 1
SocketSslErrorSeverity = Int32
SocketSslErrorSeverity_None: SocketSslErrorSeverity = 0
SocketSslErrorSeverity_Ignorable: SocketSslErrorSeverity = 1
SocketSslErrorSeverity_Fatal: SocketSslErrorSeverity = 2
class StreamSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocket
    _classid_ = 'Windows.Networking.Sockets.StreamSocket'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Networking.Sockets.StreamSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Networking.Sockets.StreamSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IStreamSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAsync(self: Windows.Networking.Sockets.IStreamSocket, endpointPair: Windows.Networking.EndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IStreamSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAndProtectionLevelAsync(self: Windows.Networking.Sockets.IStreamSocket, endpointPair: Windows.Networking.EndpointPair, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithProtectionLevelAsync(self: Windows.Networking.Sockets.IStreamSocket, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpgradeToSslAsync(self: Windows.Networking.Sockets.IStreamSocket, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, validationHostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ConnectWithProtectionLevelAndAdapterAsync(self: Windows.Networking.Sockets.IStreamSocket2, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: Windows.Networking.Sockets.IStreamSocket3) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: Windows.Networking.Sockets.IStreamSocket3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: Windows.Networking.Sockets.IStreamSocket3, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContextAndKeepAliveTime(self: Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def GetEndpointPairsAsync(cls: Windows.Networking.Sockets.IStreamSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    @winrt_classmethod
    def GetEndpointPairsWithSortOptionsAsync(cls: Windows.Networking.Sockets.IStreamSocketStatics, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: Windows.Networking.HostNameSortOptions) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.EndpointPair]]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class StreamSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocketControl
    _classid_ = 'Windows.Networking.Sockets.StreamSocketControl'
    @winrt_mixinmethod
    def get_NoDelay(self: Windows.Networking.Sockets.IStreamSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: Windows.Networking.Sockets.IStreamSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketControl) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketControl, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketControl) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketControl, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Networking.Sockets.IStreamSocketControl2) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_SerializeConnectionAttempts(self: Windows.Networking.Sockets.IStreamSocketControl3) -> Boolean: ...
    @winrt_mixinmethod
    def put_SerializeConnectionAttempts(self: Windows.Networking.Sockets.IStreamSocketControl3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Networking.Sockets.IStreamSocketControl3) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Networking.Sockets.IStreamSocketControl3, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_MinProtectionLevel(self: Windows.Networking.Sockets.IStreamSocketControl4) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def put_MinProtectionLevel(self: Windows.Networking.Sockets.IStreamSocketControl4, value: Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    SerializeConnectionAttempts = property(get_SerializeConnectionAttempts, put_SerializeConnectionAttempts)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
    MinProtectionLevel = property(get_MinProtectionLevel, put_MinProtectionLevel)
class StreamSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocketInformation
    _classid_ = 'Windows.Networking.Sockets.StreamSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemoteAddress(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemoteServiceName(self: Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoundTripTimeStatistics(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.Sockets.RoundTripTimeStatistics: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def get_SessionKey(self: Windows.Networking.Sockets.IStreamSocketInformation) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IStreamSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemoteServiceName = property(get_RemoteServiceName, None)
    RemotePort = property(get_RemotePort, None)
    RoundTripTimeStatistics = property(get_RoundTripTimeStatistics, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    ProtectionLevel = property(get_ProtectionLevel, None)
    SessionKey = property(get_SessionKey, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class StreamSocketListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocketListener
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListener'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Sockets.StreamSocketListener: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IStreamSocketListener) -> Windows.Networking.Sockets.StreamSocketListenerControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IStreamSocketListener) -> Windows.Networking.Sockets.StreamSocketListenerInformation: ...
    @winrt_mixinmethod
    def BindServiceNameAsync(self: Windows.Networking.Sockets.IStreamSocketListener, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindEndpointAsync(self: Windows.Networking.Sockets.IStreamSocketListener, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_ConnectionReceived(self: Windows.Networking.Sockets.IStreamSocketListener, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamSocketListener, Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionReceived(self: Windows.Networking.Sockets.IStreamSocketListener, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def BindServiceNameWithProtectionLevelAsync(self: Windows.Networking.Sockets.IStreamSocketListener2, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindServiceNameWithProtectionLevelAndAdapterAsync(self: Windows.Networking.Sockets.IStreamSocketListener2, localServiceName: WinRT_String, protectionLevel: Windows.Networking.Sockets.SocketProtectionLevel, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: Windows.Networking.Sockets.IStreamSocketListener3) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: Windows.Networking.Sockets.IStreamSocketListener3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: Windows.Networking.Sockets.IStreamSocketListener3, taskId: Guid, connectedStandbyAction: Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: Windows.Networking.Sockets.IStreamSocketListener3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: Windows.Networking.Sockets.IStreamSocketListener3, socketId: WinRT_String, data: Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class StreamSocketListenerConnectionReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs'
    @winrt_mixinmethod
    def get_Socket(self: Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs) -> Windows.Networking.Sockets.StreamSocket: ...
    Socket = property(get_Socket, None)
class StreamSocketListenerControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocketListenerControl
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListenerControl'
    @winrt_mixinmethod
    def get_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketListenerControl) -> Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: Windows.Networking.Sockets.IStreamSocketListenerControl, value: Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_NoDelay(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepAlive(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Byte) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class StreamSocketListenerInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamSocketListenerInformation
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListenerInformation'
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.Sockets.IStreamSocketListenerInformation) -> WinRT_String: ...
    LocalPort = property(get_LocalPort, None)
class StreamWebSocket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamWebSocket
    _classid_ = 'Windows.Networking.Sockets.StreamWebSocket'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Sockets.StreamWebSocket: ...
    @winrt_mixinmethod
    def get_Control(self: Windows.Networking.Sockets.IStreamWebSocket) -> Windows.Networking.Sockets.StreamWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: Windows.Networking.Sockets.IStreamWebSocket) -> Windows.Networking.Sockets.StreamWebSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Networking.Sockets.IStreamWebSocket) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Networking.Sockets.IWebSocket) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Networking.Sockets.IWebSocket, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.Sockets.IWebSocket, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Networking.Sockets.IWebSocket, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.IWebSocket, Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Networking.Sockets.IWebSocket, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: Windows.Networking.Sockets.IWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IStreamWebSocket2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.Sockets.StreamWebSocket, Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: Windows.Networking.Sockets.IStreamWebSocket2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class StreamWebSocketControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IStreamWebSocketControl
    _classid_ = 'Windows.Networking.Sockets.StreamWebSocketControl'
    @winrt_mixinmethod
    def get_NoDelay(self: Windows.Networking.Sockets.IStreamWebSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: Windows.Networking.Sockets.IStreamWebSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: Windows.Networking.Sockets.IWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Networking.Sockets.IWebSocketControl, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedProtocols(self: Windows.Networking.Sockets.IWebSocketControl) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketControl2) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IStreamWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredUnsolicitedPongInterval(self: Windows.Networking.Sockets.IStreamWebSocketControl2, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ActualUnsolicitedPongInterval(self: Windows.Networking.Sockets.IStreamWebSocketControl2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Networking.Sockets.IStreamWebSocketControl2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Networking.Sockets.IStreamWebSocketControl2, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class StreamWebSocketInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.StreamWebSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: Windows.Networking.Sockets.IWebSocketInformation) -> Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Sockets.IWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IWebSocketInformation2) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class WebSocketClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IWebSocketClosedEventArgs
    _classid_ = 'Windows.Networking.Sockets.WebSocketClosedEventArgs'
    @winrt_mixinmethod
    def get_Code(self: Windows.Networking.Sockets.IWebSocketClosedEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Networking.Sockets.IWebSocketClosedEventArgs) -> WinRT_String: ...
    Code = property(get_Code, None)
    Reason = property(get_Reason, None)
class WebSocketError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.WebSocketError'
    @winrt_classmethod
    def GetStatus(cls: Windows.Networking.Sockets.IWebSocketErrorStatics, hresult: Int32) -> Windows.Web.WebErrorStatus: ...
class WebSocketKeepAlive(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTask
    _classid_ = 'Windows.Networking.Sockets.WebSocketKeepAlive'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.Sockets.WebSocketKeepAlive: ...
    @winrt_mixinmethod
    def Run(self: Windows.ApplicationModel.Background.IBackgroundTask, taskInstance: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class WebSocketServerCustomValidationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs
    _classid_ = 'Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Reject(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
make_head(_module, 'BandwidthStatistics')
make_head(_module, 'ControlChannelTrigger')
make_head(_module, 'DatagramSocket')
make_head(_module, 'DatagramSocketControl')
make_head(_module, 'DatagramSocketInformation')
make_head(_module, 'DatagramSocketMessageReceivedEventArgs')
make_head(_module, 'IControlChannelTrigger')
make_head(_module, 'IControlChannelTrigger2')
make_head(_module, 'IControlChannelTriggerEventDetails')
make_head(_module, 'IControlChannelTriggerFactory')
make_head(_module, 'IControlChannelTriggerResetEventDetails')
make_head(_module, 'IDatagramSocket')
make_head(_module, 'IDatagramSocket2')
make_head(_module, 'IDatagramSocket3')
make_head(_module, 'IDatagramSocketControl')
make_head(_module, 'IDatagramSocketControl2')
make_head(_module, 'IDatagramSocketControl3')
make_head(_module, 'IDatagramSocketInformation')
make_head(_module, 'IDatagramSocketMessageReceivedEventArgs')
make_head(_module, 'IDatagramSocketStatics')
make_head(_module, 'IMessageWebSocket')
make_head(_module, 'IMessageWebSocket2')
make_head(_module, 'IMessageWebSocket3')
make_head(_module, 'IMessageWebSocketControl')
make_head(_module, 'IMessageWebSocketControl2')
make_head(_module, 'IMessageWebSocketMessageReceivedEventArgs')
make_head(_module, 'IMessageWebSocketMessageReceivedEventArgs2')
make_head(_module, 'IServerMessageWebSocket')
make_head(_module, 'IServerMessageWebSocketControl')
make_head(_module, 'IServerMessageWebSocketInformation')
make_head(_module, 'IServerStreamWebSocket')
make_head(_module, 'IServerStreamWebSocketInformation')
make_head(_module, 'ISocketActivityContext')
make_head(_module, 'ISocketActivityContextFactory')
make_head(_module, 'ISocketActivityInformation')
make_head(_module, 'ISocketActivityInformationStatics')
make_head(_module, 'ISocketActivityTriggerDetails')
make_head(_module, 'ISocketErrorStatics')
make_head(_module, 'IStreamSocket')
make_head(_module, 'IStreamSocket2')
make_head(_module, 'IStreamSocket3')
make_head(_module, 'IStreamSocketControl')
make_head(_module, 'IStreamSocketControl2')
make_head(_module, 'IStreamSocketControl3')
make_head(_module, 'IStreamSocketControl4')
make_head(_module, 'IStreamSocketInformation')
make_head(_module, 'IStreamSocketInformation2')
make_head(_module, 'IStreamSocketListener')
make_head(_module, 'IStreamSocketListener2')
make_head(_module, 'IStreamSocketListener3')
make_head(_module, 'IStreamSocketListenerConnectionReceivedEventArgs')
make_head(_module, 'IStreamSocketListenerControl')
make_head(_module, 'IStreamSocketListenerControl2')
make_head(_module, 'IStreamSocketListenerInformation')
make_head(_module, 'IStreamSocketStatics')
make_head(_module, 'IStreamWebSocket')
make_head(_module, 'IStreamWebSocket2')
make_head(_module, 'IStreamWebSocketControl')
make_head(_module, 'IStreamWebSocketControl2')
make_head(_module, 'IWebSocket')
make_head(_module, 'IWebSocketClosedEventArgs')
make_head(_module, 'IWebSocketControl')
make_head(_module, 'IWebSocketControl2')
make_head(_module, 'IWebSocketErrorStatics')
make_head(_module, 'IWebSocketInformation')
make_head(_module, 'IWebSocketInformation2')
make_head(_module, 'IWebSocketServerCustomValidationRequestedEventArgs')
make_head(_module, 'MessageWebSocket')
make_head(_module, 'MessageWebSocketControl')
make_head(_module, 'MessageWebSocketInformation')
make_head(_module, 'MessageWebSocketMessageReceivedEventArgs')
make_head(_module, 'RoundTripTimeStatistics')
make_head(_module, 'ServerMessageWebSocket')
make_head(_module, 'ServerMessageWebSocketControl')
make_head(_module, 'ServerMessageWebSocketInformation')
make_head(_module, 'ServerStreamWebSocket')
make_head(_module, 'ServerStreamWebSocketInformation')
make_head(_module, 'SocketActivityContext')
make_head(_module, 'SocketActivityInformation')
make_head(_module, 'SocketActivityTriggerDetails')
make_head(_module, 'SocketError')
make_head(_module, 'StreamSocket')
make_head(_module, 'StreamSocketControl')
make_head(_module, 'StreamSocketInformation')
make_head(_module, 'StreamSocketListener')
make_head(_module, 'StreamSocketListenerConnectionReceivedEventArgs')
make_head(_module, 'StreamSocketListenerControl')
make_head(_module, 'StreamSocketListenerInformation')
make_head(_module, 'StreamWebSocket')
make_head(_module, 'StreamWebSocketControl')
make_head(_module, 'StreamWebSocketInformation')
make_head(_module, 'WebSocketClosedEventArgs')
make_head(_module, 'WebSocketError')
make_head(_module, 'WebSocketKeepAlive')
make_head(_module, 'WebSocketServerCustomValidationRequestedEventArgs')
