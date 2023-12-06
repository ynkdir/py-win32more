from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Connectivity
import win32more.Windows.Networking.Sockets
import win32more.Windows.Security.Credentials
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Storage.Streams
import win32more.Windows.Web
class BandwidthStatistics(EasyCastStructure):
    OutboundBitsPerSecond: UInt64
    InboundBitsPerSecond: UInt64
    OutboundBitsPerSecondInstability: UInt64
    InboundBitsPerSecondInstability: UInt64
    OutboundBandwidthPeaked: Boolean
    InboundBandwidthPeaked: Boolean
class ControlChannelTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IControlChannelTrigger
    _classid_ = 'Windows.Networking.Sockets.ControlChannelTrigger'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 2:
            instance = win32more.Windows.Networking.Sockets.ControlChannelTrigger.CreateControlChannelTrigger(*args)
        elif len(args) == 3:
            instance = win32more.Windows.Networking.Sockets.ControlChannelTrigger.CreateControlChannelTriggerEx(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateControlChannelTrigger(cls: win32more.Windows.Networking.Sockets.IControlChannelTriggerFactory, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32) -> win32more.Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_factorymethod
    def CreateControlChannelTriggerEx(cls: win32more.Windows.Networking.Sockets.IControlChannelTriggerFactory, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32, resourceRequestType: win32more.Windows.Networking.Sockets.ControlChannelTriggerResourceType) -> win32more.Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_mixinmethod
    def get_ControlChannelTriggerId(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerKeepAliveIntervalInMinutes(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def put_ServerKeepAliveIntervalInMinutes(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentKeepAliveIntervalInMinutes(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_TransportObject(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_KeepAliveTrigger(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_PushNotificationTrigger(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def UsingTransport(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger, transport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def WaitForPushEnabled(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> win32more.Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_mixinmethod
    def DecreaseNetworkKeepAliveInterval(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> Void: ...
    @winrt_mixinmethod
    def FlushTransport(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_IsWakeFromLowPowerSupported(self: win32more.Windows.Networking.Sockets.IControlChannelTrigger2) -> Boolean: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IDatagramSocket
    _classid_ = 'Windows.Networking.Sockets.DatagramSocket'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.Sockets.DatagramSocket.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.Networking.Sockets.IDatagramSocket) -> win32more.Windows.Networking.Sockets.DatagramSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IDatagramSocket) -> win32more.Windows.Networking.Sockets.DatagramSocketInformation: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Networking.Sockets.IDatagramSocket) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket, endpointPair: win32more.Windows.Networking.EndpointPair) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindServiceNameAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindEndpointAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket, localHostName: win32more.Windows.Networking.HostName, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def JoinMulticastGroup(self: win32more.Windows.Networking.Sockets.IDatagramSocket, host: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def GetOutputStreamAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IOutputStream]: ...
    @winrt_mixinmethod
    def GetOutputStreamWithEndpointPairAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket, endpointPair: win32more.Windows.Networking.EndpointPair) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IOutputStream]: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: win32more.Windows.Networking.Sockets.IDatagramSocket, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.DatagramSocket, win32more.Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: win32more.Windows.Networking.Sockets.IDatagramSocket, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def BindServiceNameAndAdapterAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket2, localServiceName: WinRT_String, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: win32more.Windows.Networking.Sockets.IDatagramSocket3) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: win32more.Windows.Networking.Sockets.IDatagramSocket3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: win32more.Windows.Networking.Sockets.IDatagramSocket3, taskId: Guid, connectedStandbyAction: win32more.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: win32more.Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: win32more.Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContextAndKeepAliveTime(self: win32more.Windows.Networking.Sockets.IDatagramSocket3, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def GetEndpointPairsAsync(cls: win32more.Windows.Networking.Sockets.IDatagramSocketStatics, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
    @winrt_classmethod
    def GetEndpointPairsWithSortOptionsAsync(cls: win32more.Windows.Networking.Sockets.IDatagramSocketStatics, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: win32more.Windows.Networking.HostNameSortOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class DatagramSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IDatagramSocketControl
    _classid_ = 'Windows.Networking.Sockets.DatagramSocketControl'
    @winrt_mixinmethod
    def get_QualityOfService(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl) -> win32more.Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl, value: win32more.Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_InboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl2) -> UInt32: ...
    @winrt_mixinmethod
    def put_InboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DontFragment(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_DontFragment(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MulticastOnly(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl3) -> Boolean: ...
    @winrt_mixinmethod
    def put_MulticastOnly(self: win32more.Windows.Networking.Sockets.IDatagramSocketControl3, value: Boolean) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
    InboundBufferSizeInBytes = property(get_InboundBufferSizeInBytes, put_InboundBufferSizeInBytes)
    DontFragment = property(get_DontFragment, put_DontFragment)
    MulticastOnly = property(get_MulticastOnly, put_MulticastOnly)
class DatagramSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IDatagramSocketInformation
    _classid_ = 'Windows.Networking.Sockets.DatagramSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IDatagramSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: win32more.Windows.Networking.Sockets.IDatagramSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteAddress(self: win32more.Windows.Networking.Sockets.IDatagramSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: win32more.Windows.Networking.Sockets.IDatagramSocketInformation) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
class DatagramSocketMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs
    _classid_ = 'Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_RemoteAddress(self: win32more.Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: win32more.Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def GetDataReader(self: win32more.Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> win32more.Windows.Storage.Streams.DataReader: ...
    @winrt_mixinmethod
    def GetDataStream(self: win32more.Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs) -> win32more.Windows.Storage.Streams.IInputStream: ...
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
    LocalAddress = property(get_LocalAddress, None)
class IControlChannelTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_TransportObject(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def get_KeepAliveTrigger(self) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(12)
    def get_PushNotificationTrigger(self) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(13)
    def UsingTransport(self, transport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(14)
    def WaitForPushEnabled(self) -> win32more.Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTrigger2'
    _iid_ = Guid('{af00d237-51be-4514-9725-3556e1879580}')
    @winrt_commethod(6)
    def get_IsWakeFromLowPowerSupported(self) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class IControlChannelTriggerEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTriggerEventDetails'
    _iid_ = Guid('{1b36e047-89bb-4236-96ac-71d012bb4869}')
    @winrt_commethod(6)
    def get_ControlChannelTrigger(self) -> win32more.Windows.Networking.Sockets.ControlChannelTrigger: ...
    ControlChannelTrigger = property(get_ControlChannelTrigger, None)
class IControlChannelTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTriggerFactory'
    _iid_ = Guid('{da4b7cf0-8d71-446f-88c3-b95184a2d6cd}')
    @winrt_commethod(6)
    def CreateControlChannelTrigger(self, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32) -> win32more.Windows.Networking.Sockets.ControlChannelTrigger: ...
    @winrt_commethod(7)
    def CreateControlChannelTriggerEx(self, channelId: WinRT_String, serverKeepAliveIntervalInMinutes: UInt32, resourceRequestType: win32more.Windows.Networking.Sockets.ControlChannelTriggerResourceType) -> win32more.Windows.Networking.Sockets.ControlChannelTrigger: ...
class IControlChannelTriggerResetEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IControlChannelTriggerResetEventDetails'
    _iid_ = Guid('{6851038e-8ec4-42fe-9bb2-21e91b7bfcb1}')
    @winrt_commethod(6)
    def get_ResetReason(self) -> win32more.Windows.Networking.Sockets.ControlChannelTriggerResetReason: ...
    @winrt_commethod(7)
    def get_HardwareSlotReset(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SoftwareSlotReset(self) -> Boolean: ...
    ResetReason = property(get_ResetReason, None)
    HardwareSlotReset = property(get_HardwareSlotReset, None)
    SoftwareSlotReset = property(get_SoftwareSlotReset, None)
class IDatagramSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocket'
    _iid_ = Guid('{7fe25bbb-c3bc-4677-8446-ca28a465a3af}')
    @winrt_commethod(6)
    def get_Control(self) -> win32more.Windows.Networking.Sockets.DatagramSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.DatagramSocketInformation: ...
    @winrt_commethod(8)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def ConnectAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ConnectWithEndpointPairAsync(self, endpointPair: win32more.Windows.Networking.EndpointPair) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def BindServiceNameAsync(self, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def BindEndpointAsync(self, localHostName: win32more.Windows.Networking.HostName, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def JoinMulticastGroup(self, host: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(14)
    def GetOutputStreamAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IOutputStream]: ...
    @winrt_commethod(15)
    def GetOutputStreamWithEndpointPairAsync(self, endpointPair: win32more.Windows.Networking.EndpointPair) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IOutputStream]: ...
    @winrt_commethod(16)
    def add_MessageReceived(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.DatagramSocket, win32more.Windows.Networking.Sockets.DatagramSocketMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MessageReceived(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class IDatagramSocket2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocket2'
    _iid_ = Guid('{d83ba354-9a9d-4185-a20a-1424c9c2a7cd}')
    @winrt_commethod(6)
    def BindServiceNameAndAdapterAsync(self, localServiceName: WinRT_String, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
class IDatagramSocket3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocket3'
    _iid_ = Guid('{37544f09-ab92-4306-9ac1-0c381283d9c6}')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: win32more.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_commethod(11)
    def TransferOwnershipWithContextAndKeepAliveTime(self, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: win32more.Windows.Foundation.TimeSpan) -> Void: ...
class IDatagramSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketControl'
    _iid_ = Guid('{52ac3f2e-349a-4135-bb58-b79b2647d390}')
    @winrt_commethod(6)
    def get_QualityOfService(self) -> win32more.Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(7)
    def put_QualityOfService(self, value: win32more.Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_commethod(8)
    def get_OutboundUnicastHopLimit(self) -> Byte: ...
    @winrt_commethod(9)
    def put_OutboundUnicastHopLimit(self, value: Byte) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class IDatagramSocketControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketControl3'
    _iid_ = Guid('{d4eb8256-1f6d-4598-9b57-d42a001df349}')
    @winrt_commethod(6)
    def get_MulticastOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_MulticastOnly(self, value: Boolean) -> Void: ...
    MulticastOnly = property(get_MulticastOnly, put_MulticastOnly)
class IDatagramSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketInformation'
    _iid_ = Guid('{5f1a569a-55fb-48cd-9706-7a974f7b1585}')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_LocalPort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def get_RemotePort(self) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    LocalPort = property(get_LocalPort, None)
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
class IDatagramSocketMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketMessageReceivedEventArgs'
    _iid_ = Guid('{9e2ddca2-1712-4ce4-b179-8c652c6d107e}')
    @winrt_commethod(6)
    def get_RemoteAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def GetDataReader(self) -> win32more.Windows.Storage.Streams.DataReader: ...
    @winrt_commethod(10)
    def GetDataStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    RemoteAddress = property(get_RemoteAddress, None)
    RemotePort = property(get_RemotePort, None)
    LocalAddress = property(get_LocalAddress, None)
class IDatagramSocketStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IDatagramSocketStatics'
    _iid_ = Guid('{e9c62aee-1494-4a21-bb7e-8589fc751d9d}')
    @winrt_commethod(6)
    def GetEndpointPairsAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
    @winrt_commethod(7)
    def GetEndpointPairsWithSortOptionsAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: win32more.Windows.Networking.HostNameSortOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
class IMessageWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocket'
    _iid_ = Guid('{33727d08-34d5-4746-ad7b-8dde5bc2ef88}')
    @winrt_commethod(6)
    def get_Control(self) -> win32more.Windows.Networking.Sockets.MessageWebSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.MessageWebSocketInformation: ...
    @winrt_commethod(8)
    def add_MessageReceived(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.MessageWebSocket, win32more.Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageReceived(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class IMessageWebSocket2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocket2'
    _iid_ = Guid('{bed0cee7-f9c8-440a-9ad5-737281d9742e}')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.MessageWebSocket, win32more.Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMessageWebSocket3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocket3'
    _iid_ = Guid('{59d9defb-71af-4349-8487-911fcf681597}')
    @winrt_commethod(6)
    def SendNonfinalFrameAsync(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(7)
    def SendFinalFrameAsync(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
class IMessageWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketControl'
    _iid_ = Guid('{8118388a-c629-4f0a-80fb-81fc05538862}')
    @winrt_commethod(6)
    def get_MaxMessageSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MaxMessageSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_MessageType(self) -> win32more.Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(9)
    def put_MessageType(self, value: win32more.Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MaxMessageSize = property(get_MaxMessageSize, put_MaxMessageSize)
    MessageType = property(get_MessageType, put_MessageType)
class IMessageWebSocketControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketControl2'
    _iid_ = Guid('{e30fd791-080c-400a-a712-27dfa9e744d8}')
    @winrt_commethod(6)
    def get_DesiredUnsolicitedPongInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DesiredUnsolicitedPongInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ActualUnsolicitedPongInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ReceiveMode(self) -> win32more.Windows.Networking.Sockets.MessageWebSocketReceiveMode: ...
    @winrt_commethod(10)
    def put_ReceiveMode(self, value: win32more.Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> Void: ...
    @winrt_commethod(11)
    def get_ClientCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(12)
    def put_ClientCertificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ReceiveMode = property(get_ReceiveMode, put_ReceiveMode)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IMessageWebSocketMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs'
    _iid_ = Guid('{478c22ac-4c4b-42ed-9ed7-1ef9f94fa3d5}')
    @winrt_commethod(6)
    def get_MessageType(self) -> win32more.Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(7)
    def GetDataReader(self) -> win32more.Windows.Storage.Streams.DataReader: ...
    @winrt_commethod(8)
    def GetDataStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    MessageType = property(get_MessageType, None)
class IMessageWebSocketMessageReceivedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs2'
    _iid_ = Guid('{89ce06fd-dd6f-4a07-87f9-f9eb4d89d83d}')
    @winrt_commethod(6)
    def get_IsMessageComplete(self) -> Boolean: ...
    IsMessageComplete = property(get_IsMessageComplete, None)
class IServerMessageWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerMessageWebSocket'
    _iid_ = Guid('{e3ac9240-813b-5efd-7e11-ae2305fc77f1}')
    @winrt_commethod(6)
    def add_MessageReceived(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.ServerMessageWebSocket, win32more.Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Control(self) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocketControl: ...
    @winrt_commethod(9)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocketInformation: ...
    @winrt_commethod(10)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(11)
    def add_Closed(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.ServerMessageWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class IServerMessageWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerMessageWebSocketControl'
    _iid_ = Guid('{69c2f051-1c1f-587a-4519-2181610192b7}')
    @winrt_commethod(6)
    def get_MessageType(self) -> win32more.Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_commethod(7)
    def put_MessageType(self, value: win32more.Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MessageType = property(get_MessageType, put_MessageType)
class IServerMessageWebSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerMessageWebSocketInformation'
    _iid_ = Guid('{fc32b45f-4448-5505-6cc9-09afa8915f5d}')
    @winrt_commethod(6)
    def get_BandwidthStatistics(self) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> win32more.Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class IServerStreamWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerStreamWebSocket'
    _iid_ = Guid('{2ced5bbf-74f6-55e4-79df-9132680dfee8}')
    @winrt_commethod(6)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.ServerStreamWebSocketInformation: ...
    @winrt_commethod(7)
    def get_InputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(8)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def add_Closed(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.ServerStreamWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class IServerStreamWebSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IServerStreamWebSocketInformation'
    _iid_ = Guid('{fc32b45f-4448-5505-6cc9-09aba8915f5d}')
    @winrt_commethod(6)
    def get_BandwidthStatistics(self) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(7)
    def get_Protocol(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalAddress(self) -> win32more.Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class ISocketActivityContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityContext'
    _iid_ = Guid('{43b04d64-4c85-4396-a637-1d973f6ebd49}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
class ISocketActivityContextFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityContextFactory'
    _iid_ = Guid('{b99fc3c3-088c-4388-83ae-2525138e049a}')
    @winrt_commethod(6)
    def Create(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Networking.Sockets.SocketActivityContext: ...
class ISocketActivityInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityInformation'
    _iid_ = Guid('{8d8a42e4-a87e-4b74-9968-185b2511defe}')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SocketKind(self) -> win32more.Windows.Networking.Sockets.SocketActivityKind: ...
    @winrt_commethod(9)
    def get_Context(self) -> win32more.Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_commethod(10)
    def get_DatagramSocket(self) -> win32more.Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_commethod(11)
    def get_StreamSocket(self) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_commethod(12)
    def get_StreamSocketListener(self) -> win32more.Windows.Networking.Sockets.StreamSocketListener: ...
    TaskId = property(get_TaskId, None)
    Id = property(get_Id, None)
    SocketKind = property(get_SocketKind, None)
    Context = property(get_Context, None)
    DatagramSocket = property(get_DatagramSocket, None)
    StreamSocket = property(get_StreamSocket, None)
    StreamSocketListener = property(get_StreamSocketListener, None)
class ISocketActivityInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityInformationStatics'
    _iid_ = Guid('{8570b47a-7e7d-4736-8041-1327a6543c56}')
    @winrt_commethod(6)
    def get_AllSockets(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Networking.Sockets.SocketActivityInformation]: ...
    AllSockets = property(get_AllSockets, None)
class ISocketActivityTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketActivityTriggerDetails'
    _iid_ = Guid('{45f406a7-fc9f-4f81-acad-355fef51e67b}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Networking.Sockets.SocketActivityTriggerReason: ...
    @winrt_commethod(7)
    def get_SocketInformation(self) -> win32more.Windows.Networking.Sockets.SocketActivityInformation: ...
    Reason = property(get_Reason, None)
    SocketInformation = property(get_SocketInformation, None)
class ISocketErrorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.ISocketErrorStatics'
    _iid_ = Guid('{828337f4-7d56-4d8e-b7b4-a07dd7c1bca9}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> win32more.Windows.Networking.Sockets.SocketErrorStatus: ...
class IStreamSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocket'
    _iid_ = Guid('{69a22cf3-fc7b-4857-af38-f6e7de6a5b49}')
    @winrt_commethod(6)
    def get_Control(self) -> win32more.Windows.Networking.Sockets.StreamSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.StreamSocketInformation: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(9)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(10)
    def ConnectWithEndpointPairAsync(self, endpointPair: win32more.Windows.Networking.EndpointPair) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ConnectAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ConnectWithEndpointPairAndProtectionLevelAsync(self, endpointPair: win32more.Windows.Networking.EndpointPair, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ConnectWithProtectionLevelAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def UpgradeToSslAsync(self, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel, validationHostName: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncAction: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class IStreamSocket2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocket2'
    _iid_ = Guid('{29d0e575-f314-4d09-adf0-0fbd967fbd9f}')
    @winrt_commethod(6)
    def ConnectWithProtectionLevelAndAdapterAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
class IStreamSocket3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocket3'
    _iid_ = Guid('{3f430b00-9d28-4854-bac3-2301941ec223}')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: win32more.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_commethod(11)
    def TransferOwnershipWithContextAndKeepAliveTime(self, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: win32more.Windows.Foundation.TimeSpan) -> Void: ...
class IStreamSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_QualityOfService(self) -> win32more.Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(13)
    def put_QualityOfService(self, value: win32more.Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl2'
    _iid_ = Guid('{c2d09a56-060f-44c1-b8e2-1fbf60bd62c5}')
    @winrt_commethod(6)
    def get_IgnorableServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
class IStreamSocketControl3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl3'
    _iid_ = Guid('{c56a444c-4e74-403e-894c-b31cae5c7342}')
    @winrt_commethod(6)
    def get_SerializeConnectionAttempts(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SerializeConnectionAttempts(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ClientCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def put_ClientCertificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    SerializeConnectionAttempts = property(get_SerializeConnectionAttempts, put_SerializeConnectionAttempts)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IStreamSocketControl4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketControl4'
    _iid_ = Guid('{964e2b3d-ec27-4888-b3ce-c74b418423ad}')
    @winrt_commethod(6)
    def get_MinProtectionLevel(self) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(7)
    def put_MinProtectionLevel(self, value: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    MinProtectionLevel = property(get_MinProtectionLevel, put_MinProtectionLevel)
class IStreamSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketInformation'
    _iid_ = Guid('{3b80ae30-5e68-4205-88f0-dc85d2e25ded}')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_LocalPort(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def get_RemoteAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(10)
    def get_RemoteServiceName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_RoundTripTimeStatistics(self) -> win32more.Windows.Networking.Sockets.RoundTripTimeStatistics: ...
    @winrt_commethod(13)
    def get_BandwidthStatistics(self) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(14)
    def get_ProtectionLevel(self) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(15)
    def get_SessionKey(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketInformation2'
    _iid_ = Guid('{12c28452-4bdc-4ee4-976a-cf130e9d92e3}')
    @winrt_commethod(6)
    def get_ServerCertificateErrorSeverity(self) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(8)
    def get_ServerCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IStreamSocketListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListener'
    _iid_ = Guid('{ff513437-df9f-4df0-bf82-0ec5d7b35aae}')
    @winrt_commethod(6)
    def get_Control(self) -> win32more.Windows.Networking.Sockets.StreamSocketListenerControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.StreamSocketListenerInformation: ...
    @winrt_commethod(8)
    def BindServiceNameAsync(self, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def BindEndpointAsync(self, localHostName: win32more.Windows.Networking.HostName, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def add_ConnectionReceived(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.StreamSocketListener, win32more.Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ConnectionReceived(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class IStreamSocketListener2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListener2'
    _iid_ = Guid('{658dc13e-bb3e-4458-b232-ed1088694b98}')
    @winrt_commethod(6)
    def BindServiceNameWithProtectionLevelAsync(self, localServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def BindServiceNameWithProtectionLevelAndAdapterAsync(self, localServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
class IStreamSocketListener3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListener3'
    _iid_ = Guid('{4798201c-bdf8-4919-8542-28d450e74507}')
    @winrt_commethod(6)
    def CancelIOAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def EnableTransferOwnership(self, taskId: Guid) -> Void: ...
    @winrt_commethod(8)
    def EnableTransferOwnershipWithConnectedStandbyAction(self, taskId: Guid, connectedStandbyAction: win32more.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_commethod(9)
    def TransferOwnership(self, socketId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def TransferOwnershipWithContext(self, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
class IStreamSocketListenerConnectionReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs'
    _iid_ = Guid('{0c472ea9-373f-447b-85b1-ddd4548803ba}')
    @winrt_commethod(6)
    def get_Socket(self) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    Socket = property(get_Socket, None)
class IStreamSocketListenerControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerControl'
    _iid_ = Guid('{20d8c576-8d8a-4dba-9722-a16c4d984980}')
    @winrt_commethod(6)
    def get_QualityOfService(self) -> win32more.Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_commethod(7)
    def put_QualityOfService(self, value: win32more.Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
class IStreamSocketListenerControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketListenerInformation'
    _iid_ = Guid('{e62ba82f-a63a-430b-bf62-29e93e5633b4}')
    @winrt_commethod(6)
    def get_LocalPort(self) -> WinRT_String: ...
    LocalPort = property(get_LocalPort, None)
class IStreamSocketStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamSocketStatics'
    _iid_ = Guid('{a420bc4a-6e2e-4af5-b556-355ae0cd4f29}')
    @winrt_commethod(6)
    def GetEndpointPairsAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
    @winrt_commethod(7)
    def GetEndpointPairsWithSortOptionsAsync(self, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: win32more.Windows.Networking.HostNameSortOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
class IStreamWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocket'
    _iid_ = Guid('{bd4a49d8-b289-45bb-97eb-c7525205a843}')
    @winrt_commethod(6)
    def get_Control(self) -> win32more.Windows.Networking.Sockets.StreamWebSocketControl: ...
    @winrt_commethod(7)
    def get_Information(self) -> win32more.Windows.Networking.Sockets.StreamWebSocketInformation: ...
    @winrt_commethod(8)
    def get_InputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
class IStreamWebSocket2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocket2'
    _iid_ = Guid('{aa4d08cb-93f5-4678-8236-57cce5417ed5}')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.StreamWebSocket, win32more.Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IStreamWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocketControl'
    _iid_ = Guid('{b4f478b1-a45a-48db-953a-645b7d964c07}')
    @winrt_commethod(6)
    def get_NoDelay(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_NoDelay(self, value: Boolean) -> Void: ...
    NoDelay = property(get_NoDelay, put_NoDelay)
class IStreamWebSocketControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IStreamWebSocketControl2'
    _iid_ = Guid('{215d9f7e-fa58-40da-9f11-a48dafe95037}')
    @winrt_commethod(6)
    def get_DesiredUnsolicitedPongInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DesiredUnsolicitedPongInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ActualUnsolicitedPongInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_ClientCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(10)
    def put_ClientCertificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    DesiredUnsolicitedPongInterval = property(get_DesiredUnsolicitedPongInterval, put_DesiredUnsolicitedPongInterval)
    ActualUnsolicitedPongInterval = property(get_ActualUnsolicitedPongInterval, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
class IWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocket'
    _iid_ = Guid('{f877396f-99b1-4e18-bc08-850c9adf156e}')
    @winrt_commethod(6)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(7)
    def ConnectAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def add_Closed(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.IWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Closed(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def CloseWithStatus(self, code: UInt16, reason: WinRT_String) -> Void: ...
    OutputStream = property(get_OutputStream, None)
class IWebSocketClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketClosedEventArgs'
    _iid_ = Guid('{ceb78d07-d0a8-4703-a091-c8c2c0915bc3}')
    @winrt_commethod(6)
    def get_Code(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Reason(self) -> WinRT_String: ...
    Code = property(get_Code, None)
    Reason = property(get_Reason, None)
class IWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketControl'
    _iid_ = Guid('{2ec4bdc3-d9a5-455a-9811-de24d45337e9}')
    @winrt_commethod(6)
    def get_OutboundBufferSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_OutboundBufferSizeInBytes(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_ServerCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(9)
    def put_ServerCredential(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(10)
    def get_ProxyCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(11)
    def put_ProxyCredential(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedProtocols(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    SupportedProtocols = property(get_SupportedProtocols, None)
class IWebSocketControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketControl2'
    _iid_ = Guid('{79c3be03-f2ca-461e-af4e-9665bc2d0620}')
    @winrt_commethod(6)
    def get_IgnorableServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
class IWebSocketErrorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketErrorStatics'
    _iid_ = Guid('{27cdf35b-1f61-4709-8e02-61283ada4e9d}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
class IWebSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketInformation'
    _iid_ = Guid('{5e01e316-c92a-47a5-b25f-07847639d181}')
    @winrt_commethod(6)
    def get_LocalAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def get_BandwidthStatistics(self) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_commethod(8)
    def get_Protocol(self) -> WinRT_String: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
class IWebSocketInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketInformation2'
    _iid_ = Guid('{ce1d39ce-a1b7-4d43-8269-8d5b981bd47a}')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IWebSocketServerCustomValidationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs'
    _iid_ = Guid('{ffeffe48-022a-4ab7-8b36-e10af4640e6b}')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(10)
    def Reject(self) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class MessageWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IMessageWebSocket
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocket'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.Sockets.MessageWebSocket.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Sockets.MessageWebSocket: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.Networking.Sockets.IMessageWebSocket) -> win32more.Windows.Networking.Sockets.MessageWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IMessageWebSocket) -> win32more.Windows.Networking.Sockets.MessageWebSocketInformation: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: win32more.Windows.Networking.Sockets.IMessageWebSocket, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.MessageWebSocket, win32more.Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: win32more.Windows.Networking.Sockets.IMessageWebSocket, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Networking.Sockets.IWebSocket) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Networking.Sockets.IWebSocket, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Networking.Sockets.IWebSocket, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Networking.Sockets.IWebSocket, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.IWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Networking.Sockets.IWebSocket, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: win32more.Windows.Networking.Sockets.IWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: win32more.Windows.Networking.Sockets.IMessageWebSocket2, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.MessageWebSocket, win32more.Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: win32more.Windows.Networking.Sockets.IMessageWebSocket2, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SendNonfinalFrameAsync(self: win32more.Windows.Networking.Sockets.IMessageWebSocket3, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def SendFinalFrameAsync(self: win32more.Windows.Networking.Sockets.IMessageWebSocket3, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class MessageWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IMessageWebSocketControl
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocketControl'
    @winrt_mixinmethod
    def get_MaxMessageSize(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxMessageSize(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl) -> win32more.Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def put_MessageType(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl, value: win32more.Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedProtocols(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IWebSocketControl2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_DesiredUnsolicitedPongInterval(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredUnsolicitedPongInterval(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ActualUnsolicitedPongInterval(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ReceiveMode(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2) -> win32more.Windows.Networking.Sockets.MessageWebSocketReceiveMode: ...
    @winrt_mixinmethod
    def put_ReceiveMode(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2, value: win32more.Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> Void: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: win32more.Windows.Networking.Sockets.IMessageWebSocketControl2, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IWebSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: win32more.Windows.Networking.Sockets.IWebSocketInformation) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: win32more.Windows.Networking.Sockets.IWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class MessageWebSocketMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs
    _classid_ = 'Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> win32more.Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def GetDataReader(self: win32more.Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> win32more.Windows.Storage.Streams.DataReader: ...
    @winrt_mixinmethod
    def GetDataStream(self: win32more.Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_IsMessageComplete(self: win32more.Windows.Networking.Sockets.IMessageWebSocketMessageReceivedEventArgs2) -> Boolean: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IServerMessageWebSocket
    _classid_ = 'Windows.Networking.Sockets.ServerMessageWebSocket'
    @winrt_mixinmethod
    def add_MessageReceived(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.ServerMessageWebSocket, win32more.Windows.Networking.Sockets.MessageWebSocketMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocketInformation: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.ServerMessageWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    OutputStream = property(get_OutputStream, None)
class ServerMessageWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IServerMessageWebSocketControl
    _classid_ = 'Windows.Networking.Sockets.ServerMessageWebSocketControl'
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocketControl) -> win32more.Windows.Networking.Sockets.SocketMessageType: ...
    @winrt_mixinmethod
    def put_MessageType(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocketControl, value: win32more.Windows.Networking.Sockets.SocketMessageType) -> Void: ...
    MessageType = property(get_MessageType, put_MessageType)
class ServerMessageWebSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IServerMessageWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.ServerMessageWebSocketInformation'
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IServerMessageWebSocketInformation) -> win32more.Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
class ServerStreamWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IServerStreamWebSocket
    _classid_ = 'Windows.Networking.Sockets.ServerStreamWebSocket'
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocket) -> win32more.Windows.Networking.Sockets.ServerStreamWebSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocket) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocket) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocket, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.ServerStreamWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocket, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class ServerStreamWebSocketInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IServerStreamWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.ServerStreamWebSocketInformation'
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IServerStreamWebSocketInformation) -> win32more.Windows.Networking.HostName: ...
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    LocalAddress = property(get_LocalAddress, None)
SocketActivityConnectedStandbyAction = Int32
SocketActivityConnectedStandbyAction_DoNotWake: SocketActivityConnectedStandbyAction = 0
SocketActivityConnectedStandbyAction_Wake: SocketActivityConnectedStandbyAction = 1
class SocketActivityContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.ISocketActivityContext
    _classid_ = 'Windows.Networking.Sockets.SocketActivityContext'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Networking.Sockets.SocketActivityContext.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Networking.Sockets.ISocketActivityContextFactory, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Networking.Sockets.ISocketActivityContext) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
class _SocketActivityInformation_Meta_(ComPtr.__class__):
    pass
class SocketActivityInformation(ComPtr, metaclass=_SocketActivityInformation_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.ISocketActivityInformation
    _classid_ = 'Windows.Networking.Sockets.SocketActivityInformation'
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SocketKind(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> win32more.Windows.Networking.Sockets.SocketActivityKind: ...
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> win32more.Windows.Networking.Sockets.SocketActivityContext: ...
    @winrt_mixinmethod
    def get_DatagramSocket(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> win32more.Windows.Networking.Sockets.DatagramSocket: ...
    @winrt_mixinmethod
    def get_StreamSocket(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_StreamSocketListener(self: win32more.Windows.Networking.Sockets.ISocketActivityInformation) -> win32more.Windows.Networking.Sockets.StreamSocketListener: ...
    @winrt_classmethod
    def get_AllSockets(cls: win32more.Windows.Networking.Sockets.ISocketActivityInformationStatics) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Networking.Sockets.SocketActivityInformation]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.ISocketActivityTriggerDetails
    _classid_ = 'Windows.Networking.Sockets.SocketActivityTriggerDetails'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Networking.Sockets.ISocketActivityTriggerDetails) -> win32more.Windows.Networking.Sockets.SocketActivityTriggerReason: ...
    @winrt_mixinmethod
    def get_SocketInformation(self: win32more.Windows.Networking.Sockets.ISocketActivityTriggerDetails) -> win32more.Windows.Networking.Sockets.SocketActivityInformation: ...
    Reason = property(get_Reason, None)
    SocketInformation = property(get_SocketInformation, None)
SocketActivityTriggerReason = Int32
SocketActivityTriggerReason_None: SocketActivityTriggerReason = 0
SocketActivityTriggerReason_SocketActivity: SocketActivityTriggerReason = 1
SocketActivityTriggerReason_ConnectionAccepted: SocketActivityTriggerReason = 2
SocketActivityTriggerReason_KeepAliveTimerExpired: SocketActivityTriggerReason = 3
SocketActivityTriggerReason_SocketClosed: SocketActivityTriggerReason = 4
class SocketError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.SocketError'
    @winrt_classmethod
    def GetStatus(cls: win32more.Windows.Networking.Sockets.ISocketErrorStatics, hresult: Int32) -> win32more.Windows.Networking.Sockets.SocketErrorStatus: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocket
    _classid_ = 'Windows.Networking.Sockets.StreamSocket'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.Sockets.StreamSocket.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.Networking.Sockets.IStreamSocket) -> win32more.Windows.Networking.Sockets.StreamSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IStreamSocket) -> win32more.Windows.Networking.Sockets.StreamSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: win32more.Windows.Networking.Sockets.IStreamSocket) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Networking.Sockets.IStreamSocket) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket, endpointPair: win32more.Windows.Networking.EndpointPair) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithEndpointPairAndProtectionLevelAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket, endpointPair: win32more.Windows.Networking.EndpointPair, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConnectWithProtectionLevelAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpgradeToSslAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel, validationHostName: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ConnectWithProtectionLevelAndAdapterAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket2, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: win32more.Windows.Networking.Sockets.IStreamSocket3) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: win32more.Windows.Networking.Sockets.IStreamSocket3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: win32more.Windows.Networking.Sockets.IStreamSocket3, taskId: Guid, connectedStandbyAction: win32more.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: win32more.Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: win32more.Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContextAndKeepAliveTime(self: win32more.Windows.Networking.Sockets.IStreamSocket3, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext, keepAliveTime: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def GetEndpointPairsAsync(cls: win32more.Windows.Networking.Sockets.IStreamSocketStatics, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
    @winrt_classmethod
    def GetEndpointPairsWithSortOptionsAsync(cls: win32more.Windows.Networking.Sockets.IStreamSocketStatics, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String, sortOptions: win32more.Windows.Networking.HostNameSortOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]]: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class StreamSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocketControl
    _classid_ = 'Windows.Networking.Sockets.StreamSocketControl'
    @winrt_mixinmethod
    def get_NoDelay(self: win32more.Windows.Networking.Sockets.IStreamSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: win32more.Windows.Networking.Sockets.IStreamSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepAlive(self: win32more.Windows.Networking.Sockets.IStreamSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepAlive(self: win32more.Windows.Networking.Sockets.IStreamSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IStreamSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IStreamSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_QualityOfService(self: win32more.Windows.Networking.Sockets.IStreamSocketControl) -> win32more.Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: win32more.Windows.Networking.Sockets.IStreamSocketControl, value: win32more.Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: win32more.Windows.Networking.Sockets.IStreamSocketControl) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: win32more.Windows.Networking.Sockets.IStreamSocketControl, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IStreamSocketControl2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_SerializeConnectionAttempts(self: win32more.Windows.Networking.Sockets.IStreamSocketControl3) -> Boolean: ...
    @winrt_mixinmethod
    def put_SerializeConnectionAttempts(self: win32more.Windows.Networking.Sockets.IStreamSocketControl3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: win32more.Windows.Networking.Sockets.IStreamSocketControl3) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: win32more.Windows.Networking.Sockets.IStreamSocketControl3, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_MinProtectionLevel(self: win32more.Windows.Networking.Sockets.IStreamSocketControl4) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def put_MinProtectionLevel(self: win32more.Windows.Networking.Sockets.IStreamSocketControl4, value: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocketInformation
    _classid_ = 'Windows.Networking.Sockets.StreamSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemoteAddress(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemoteServiceName(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemotePort(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoundTripTimeStatistics(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Networking.Sockets.RoundTripTimeStatistics: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def get_SessionKey(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation2) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: win32more.Windows.Networking.Sockets.IStreamSocketInformation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocketListener
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListener'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.Sockets.StreamSocketListener.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Sockets.StreamSocketListener: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.Networking.Sockets.IStreamSocketListener) -> win32more.Windows.Networking.Sockets.StreamSocketListenerControl: ...
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IStreamSocketListener) -> win32more.Windows.Networking.Sockets.StreamSocketListenerInformation: ...
    @winrt_mixinmethod
    def BindServiceNameAsync(self: win32more.Windows.Networking.Sockets.IStreamSocketListener, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindEndpointAsync(self: win32more.Windows.Networking.Sockets.IStreamSocketListener, localHostName: win32more.Windows.Networking.HostName, localServiceName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_ConnectionReceived(self: win32more.Windows.Networking.Sockets.IStreamSocketListener, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.StreamSocketListener, win32more.Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionReceived(self: win32more.Windows.Networking.Sockets.IStreamSocketListener, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def BindServiceNameWithProtectionLevelAsync(self: win32more.Windows.Networking.Sockets.IStreamSocketListener2, localServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def BindServiceNameWithProtectionLevelAndAdapterAsync(self: win32more.Windows.Networking.Sockets.IStreamSocketListener2, localServiceName: WinRT_String, protectionLevel: win32more.Windows.Networking.Sockets.SocketProtectionLevel, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CancelIOAsync(self: win32more.Windows.Networking.Sockets.IStreamSocketListener3) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableTransferOwnership(self: win32more.Windows.Networking.Sockets.IStreamSocketListener3, taskId: Guid) -> Void: ...
    @winrt_mixinmethod
    def EnableTransferOwnershipWithConnectedStandbyAction(self: win32more.Windows.Networking.Sockets.IStreamSocketListener3, taskId: Guid, connectedStandbyAction: win32more.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnership(self: win32more.Windows.Networking.Sockets.IStreamSocketListener3, socketId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TransferOwnershipWithContext(self: win32more.Windows.Networking.Sockets.IStreamSocketListener3, socketId: WinRT_String, data: win32more.Windows.Networking.Sockets.SocketActivityContext) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
class StreamSocketListenerConnectionReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListenerConnectionReceivedEventArgs'
    @winrt_mixinmethod
    def get_Socket(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerConnectionReceivedEventArgs) -> win32more.Windows.Networking.Sockets.StreamSocket: ...
    Socket = property(get_Socket, None)
class StreamSocketListenerControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListenerControl'
    @winrt_mixinmethod
    def get_QualityOfService(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl) -> win32more.Windows.Networking.Sockets.SocketQualityOfService: ...
    @winrt_mixinmethod
    def put_QualityOfService(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl, value: win32more.Windows.Networking.Sockets.SocketQualityOfService) -> Void: ...
    @winrt_mixinmethod
    def get_NoDelay(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepAlive(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepAlive(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundUnicastHopLimit(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2) -> Byte: ...
    @winrt_mixinmethod
    def put_OutboundUnicastHopLimit(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerControl2, value: Byte) -> Void: ...
    QualityOfService = property(get_QualityOfService, put_QualityOfService)
    NoDelay = property(get_NoDelay, put_NoDelay)
    KeepAlive = property(get_KeepAlive, put_KeepAlive)
    OutboundBufferSizeInBytes = property(get_OutboundBufferSizeInBytes, put_OutboundBufferSizeInBytes)
    OutboundUnicastHopLimit = property(get_OutboundUnicastHopLimit, put_OutboundUnicastHopLimit)
class StreamSocketListenerInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamSocketListenerInformation
    _classid_ = 'Windows.Networking.Sockets.StreamSocketListenerInformation'
    @winrt_mixinmethod
    def get_LocalPort(self: win32more.Windows.Networking.Sockets.IStreamSocketListenerInformation) -> WinRT_String: ...
    LocalPort = property(get_LocalPort, None)
class StreamWebSocket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamWebSocket
    _classid_ = 'Windows.Networking.Sockets.StreamWebSocket'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.Sockets.StreamWebSocket.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Sockets.StreamWebSocket: ...
    @winrt_mixinmethod
    def get_Control(self: win32more.Windows.Networking.Sockets.IStreamWebSocket) -> win32more.Windows.Networking.Sockets.StreamWebSocketControl: ...
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Networking.Sockets.IStreamWebSocket) -> win32more.Windows.Networking.Sockets.StreamWebSocketInformation: ...
    @winrt_mixinmethod
    def get_InputStream(self: win32more.Windows.Networking.Sockets.IStreamWebSocket) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Networking.Sockets.IWebSocket) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Networking.Sockets.IWebSocket, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Networking.Sockets.IWebSocket, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Networking.Sockets.IWebSocket, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.IWebSocket, win32more.Windows.Networking.Sockets.WebSocketClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Networking.Sockets.IWebSocket, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CloseWithStatus(self: win32more.Windows.Networking.Sockets.IWebSocket, code: UInt16, reason: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: win32more.Windows.Networking.Sockets.IStreamWebSocket2, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Sockets.StreamWebSocket, win32more.Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: win32more.Windows.Networking.Sockets.IStreamWebSocket2, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Control = property(get_Control, None)
    Information = property(get_Information, None)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class StreamWebSocketControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IStreamWebSocketControl
    _classid_ = 'Windows.Networking.Sockets.StreamWebSocketControl'
    @winrt_mixinmethod
    def get_NoDelay(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_NoDelay(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> UInt32: ...
    @winrt_mixinmethod
    def put_OutboundBufferSizeInBytes(self: win32more.Windows.Networking.Sockets.IWebSocketControl, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: win32more.Windows.Networking.Sockets.IWebSocketControl, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedProtocols(self: win32more.Windows.Networking.Sockets.IWebSocketControl) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IWebSocketControl2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_DesiredUnsolicitedPongInterval(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DesiredUnsolicitedPongInterval(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl2, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ActualUnsolicitedPongInterval(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: win32more.Windows.Networking.Sockets.IStreamWebSocketControl2, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IWebSocketInformation
    _classid_ = 'Windows.Networking.Sockets.StreamWebSocketInformation'
    @winrt_mixinmethod
    def get_LocalAddress(self: win32more.Windows.Networking.Sockets.IWebSocketInformation) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_BandwidthStatistics(self: win32more.Windows.Networking.Sockets.IWebSocketInformation) -> win32more.Windows.Networking.Sockets.BandwidthStatistics: ...
    @winrt_mixinmethod
    def get_Protocol(self: win32more.Windows.Networking.Sockets.IWebSocketInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: win32more.Windows.Networking.Sockets.IWebSocketInformation2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    LocalAddress = property(get_LocalAddress, None)
    BandwidthStatistics = property(get_BandwidthStatistics, None)
    Protocol = property(get_Protocol, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class WebSocketClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IWebSocketClosedEventArgs
    _classid_ = 'Windows.Networking.Sockets.WebSocketClosedEventArgs'
    @winrt_mixinmethod
    def get_Code(self: win32more.Windows.Networking.Sockets.IWebSocketClosedEventArgs) -> UInt16: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Networking.Sockets.IWebSocketClosedEventArgs) -> WinRT_String: ...
    Code = property(get_Code, None)
    Reason = property(get_Reason, None)
class WebSocketError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Sockets.WebSocketError'
    @winrt_classmethod
    def GetStatus(cls: win32more.Windows.Networking.Sockets.IWebSocketErrorStatics, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
class WebSocketKeepAlive(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTask
    _classid_ = 'Windows.Networking.Sockets.WebSocketKeepAlive'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.Sockets.WebSocketKeepAlive.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Sockets.WebSocketKeepAlive: ...
    @winrt_mixinmethod
    def Run(self: win32more.Windows.ApplicationModel.Background.IBackgroundTask, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class WebSocketServerCustomValidationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs
    _classid_ = 'Windows.Networking.Sockets.WebSocketServerCustomValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Reject(self: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Networking.Sockets.IWebSocketServerCustomValidationRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
make_ready(__name__)
