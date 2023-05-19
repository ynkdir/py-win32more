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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.XboxLive
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
class IXboxLiveDeviceAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveDeviceAddress'
    _iid_ = Guid('{f5bbd279-3c86-4b57-a31a-b9462408fd01}')
    @winrt_commethod(6)
    def add_SnapshotChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.XboxLive.XboxLiveDeviceAddress, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SnapshotChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetSnapshotAsBase64(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetSnapshotAsBuffer(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def GetSnapshotAsBytes(self, buffer: POINTER(Byte), bytesWritten: POINTER(UInt32)) -> Void: ...
    @winrt_commethod(11)
    def Compare(self, otherDeviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Int32: ...
    @winrt_commethod(12)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsLocal(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_NetworkAccessKind(self) -> Windows.Networking.XboxLive.XboxLiveNetworkAccessKind: ...
    IsValid = property(get_IsValid, None)
    IsLocal = property(get_IsLocal, None)
    NetworkAccessKind = property(get_NetworkAccessKind, None)
class IXboxLiveDeviceAddressStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics'
    _iid_ = Guid('{5954a819-4a79-4931-827c-7f503e963263}')
    @winrt_commethod(6)
    def CreateFromSnapshotBase64(self, base64: WinRT_String) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(7)
    def CreateFromSnapshotBuffer(self, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(8)
    def CreateFromSnapshotBytes(self, buffer: POINTER(Byte)) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(9)
    def GetLocal(self) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(10)
    def get_MaxSnapshotBytesSize(self) -> UInt32: ...
    MaxSnapshotBytesSize = property(get_MaxSnapshotBytesSize, None)
class IXboxLiveEndpointPair(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPair'
    _iid_ = Guid('{1e9a839b-813e-44e0-b87f-c87a093475e4}')
    @winrt_commethod(6)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.XboxLive.XboxLiveEndpointPair, Windows.Networking.XboxLive.XboxLiveEndpointPairStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def DeleteAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def GetRemoteSocketAddressBytes(self, socketAddress: POINTER(Byte)) -> Void: ...
    @winrt_commethod(10)
    def GetLocalSocketAddressBytes(self, socketAddress: POINTER(Byte)) -> Void: ...
    @winrt_commethod(11)
    def get_State(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_commethod(12)
    def get_Template(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_commethod(13)
    def get_RemoteDeviceAddress(self) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(14)
    def get_RemoteHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(15)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_LocalHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(17)
    def get_LocalPort(self) -> WinRT_String: ...
    State = property(get_State, None)
    Template = property(get_Template, None)
    RemoteDeviceAddress = property(get_RemoteDeviceAddress, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemotePort = property(get_RemotePort, None)
    LocalHostName = property(get_LocalHostName, None)
    LocalPort = property(get_LocalPort, None)
class IXboxLiveEndpointPairCreationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult'
    _iid_ = Guid('{d9a8bb95-2aab-4d1e-9794-33ecc0dcf0fe}')
    @winrt_commethod(6)
    def get_DeviceAddress(self) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPairCreationStatus: ...
    @winrt_commethod(8)
    def get_IsExistingPathEvaluation(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_EndpointPair(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    DeviceAddress = property(get_DeviceAddress, None)
    Status = property(get_Status, None)
    IsExistingPathEvaluation = property(get_IsExistingPathEvaluation, None)
    EndpointPair = property(get_EndpointPair, None)
class IXboxLiveEndpointPairStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs'
    _iid_ = Guid('{592e3b55-de08-44e7-ac3b-b9b9a169583a}')
    @winrt_commethod(6)
    def get_OldState(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_commethod(7)
    def get_NewState(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    OldState = property(get_OldState, None)
    NewState = property(get_NewState, None)
class IXboxLiveEndpointPairStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairStatics'
    _iid_ = Guid('{64316b30-217a-4243-8ee1-6729281d27db}')
    @winrt_commethod(6)
    def FindEndpointPairBySocketAddressBytes(self, localSocketAddress: POINTER(Byte), remoteSocketAddress: POINTER(Byte)) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    @winrt_commethod(7)
    def FindEndpointPairByHostNamesAndPorts(self, localHostName: Windows.Networking.HostName, localPort: WinRT_String, remoteHostName: Windows.Networking.HostName, remotePort: WinRT_String) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
class IXboxLiveEndpointPairTemplate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate'
    _iid_ = Guid('{6b286ecf-3457-40ce-b9a1-c0cfe0213ea7}')
    @winrt_commethod(6)
    def add_InboundEndpointPairCreated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate, Windows.Networking.XboxLive.XboxLiveInboundEndpointPairCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_InboundEndpointPairCreated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CreateEndpointPairDefaultAsync(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(9)
    def CreateEndpointPairWithBehaviorsAsync(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, behaviors: Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(10)
    def CreateEndpointPairForPortsDefaultAsync(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(11)
    def CreateEndpointPairForPortsWithBehaviorsAsync(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String, behaviors: Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(12)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_SocketKind(self) -> Windows.Networking.XboxLive.XboxLiveSocketKind: ...
    @winrt_commethod(14)
    def get_InitiatorBoundPortRangeLower(self) -> UInt16: ...
    @winrt_commethod(15)
    def get_InitiatorBoundPortRangeUpper(self) -> UInt16: ...
    @winrt_commethod(16)
    def get_AcceptorBoundPortRangeLower(self) -> UInt16: ...
    @winrt_commethod(17)
    def get_AcceptorBoundPortRangeUpper(self) -> UInt16: ...
    @winrt_commethod(18)
    def get_EndpointPairs(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveEndpointPair]: ...
    Name = property(get_Name, None)
    SocketKind = property(get_SocketKind, None)
    InitiatorBoundPortRangeLower = property(get_InitiatorBoundPortRangeLower, None)
    InitiatorBoundPortRangeUpper = property(get_InitiatorBoundPortRangeUpper, None)
    AcceptorBoundPortRangeLower = property(get_AcceptorBoundPortRangeLower, None)
    AcceptorBoundPortRangeUpper = property(get_AcceptorBoundPortRangeUpper, None)
    EndpointPairs = property(get_EndpointPairs, None)
class IXboxLiveEndpointPairTemplateStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplateStatics'
    _iid_ = Guid('{1e13137b-737b-4a23-bc64-0870f75655ba}')
    @winrt_commethod(6)
    def GetTemplateByName(self, name: WinRT_String) -> Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_commethod(7)
    def get_Templates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate]: ...
    Templates = property(get_Templates, None)
class IXboxLiveInboundEndpointPairCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveInboundEndpointPairCreatedEventArgs'
    _iid_ = Guid('{dc183b62-22ba-48d2-80de-c23968bd198b}')
    @winrt_commethod(6)
    def get_EndpointPair(self) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    EndpointPair = property(get_EndpointPair, None)
class IXboxLiveQualityOfServiceMeasurement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement'
    _iid_ = Guid('{4d682bce-a5d6-47e6-a236-cfde5fbdf2ed}')
    @winrt_commethod(6)
    def MeasureAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def GetMetricResultsForDevice(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_commethod(8)
    def GetMetricResultsForMetric(self, metric: Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_commethod(9)
    def GetMetricResult(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, metric: Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult: ...
    @winrt_commethod(10)
    def GetPrivatePayloadResult(self, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult: ...
    @winrt_commethod(11)
    def get_Metrics(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric]: ...
    @winrt_commethod(12)
    def get_DeviceAddresses(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.XboxLive.XboxLiveDeviceAddress]: ...
    @winrt_commethod(13)
    def get_ShouldRequestPrivatePayloads(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_ShouldRequestPrivatePayloads(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_TimeoutInMilliseconds(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_TimeoutInMilliseconds(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_NumberOfProbesToAttempt(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_NumberOfProbesToAttempt(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_NumberOfResultsPending(self) -> UInt32: ...
    @winrt_commethod(20)
    def get_MetricResults(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_commethod(21)
    def get_PrivatePayloadResults(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult]: ...
    Metrics = property(get_Metrics, None)
    DeviceAddresses = property(get_DeviceAddresses, None)
    ShouldRequestPrivatePayloads = property(get_ShouldRequestPrivatePayloads, put_ShouldRequestPrivatePayloads)
    TimeoutInMilliseconds = property(get_TimeoutInMilliseconds, put_TimeoutInMilliseconds)
    NumberOfProbesToAttempt = property(get_NumberOfProbesToAttempt, put_NumberOfProbesToAttempt)
    NumberOfResultsPending = property(get_NumberOfResultsPending, None)
    MetricResults = property(get_MetricResults, None)
    PrivatePayloadResults = property(get_PrivatePayloadResults, None)
class IXboxLiveQualityOfServiceMeasurementStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics'
    _iid_ = Guid('{6e352dca-23cf-440a-b077-5e30857a8234}')
    @winrt_commethod(6)
    def PublishPrivatePayloadBytes(self, payload: POINTER(Byte)) -> Void: ...
    @winrt_commethod(7)
    def ClearPrivatePayload(self) -> Void: ...
    @winrt_commethod(8)
    def get_MaxSimultaneousProbeConnections(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_MaxSimultaneousProbeConnections(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_IsSystemOutboundBandwidthConstrained(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsSystemOutboundBandwidthConstrained(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsSystemInboundBandwidthConstrained(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsSystemInboundBandwidthConstrained(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PublishedPrivatePayload(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(15)
    def put_PublishedPrivatePayload(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(16)
    def get_MaxPrivatePayloadSize(self) -> UInt32: ...
    MaxSimultaneousProbeConnections = property(get_MaxSimultaneousProbeConnections, put_MaxSimultaneousProbeConnections)
    IsSystemOutboundBandwidthConstrained = property(get_IsSystemOutboundBandwidthConstrained, put_IsSystemOutboundBandwidthConstrained)
    IsSystemInboundBandwidthConstrained = property(get_IsSystemInboundBandwidthConstrained, put_IsSystemInboundBandwidthConstrained)
    PublishedPrivatePayload = property(get_PublishedPrivatePayload, put_PublishedPrivatePayload)
    MaxPrivatePayloadSize = property(get_MaxPrivatePayloadSize, None)
class IXboxLiveQualityOfServiceMetricResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult'
    _iid_ = Guid('{aeec53d1-3561-4782-b0cf-d3ae29d9fa87}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_commethod(7)
    def get_DeviceAddress(self) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(8)
    def get_Metric(self) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric: ...
    @winrt_commethod(9)
    def get_Value(self) -> UInt64: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Metric = property(get_Metric, None)
    Value = property(get_Value, None)
class IXboxLiveQualityOfServicePrivatePayloadResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult'
    _iid_ = Guid('{5a6302ae-6f38-41c0-9fcc-ea6cb978cafc}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_commethod(7)
    def get_DeviceAddress(self) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Value = property(get_Value, None)
class _XboxLiveDeviceAddress_Meta_(ComPtr.__class__):
    pass
class XboxLiveDeviceAddress(ComPtr, metaclass=_XboxLiveDeviceAddress_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveDeviceAddress
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveDeviceAddress'
    @winrt_mixinmethod
    def add_SnapshotChanged(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.XboxLive.XboxLiveDeviceAddress, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SnapshotChanged(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetSnapshotAsBase64(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetSnapshotAsBuffer(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def GetSnapshotAsBytes(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress, buffer: POINTER(Byte), bytesWritten: POINTER(UInt32)) -> Void: ...
    @winrt_mixinmethod
    def Compare(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress, otherDeviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Int32: ...
    @winrt_mixinmethod
    def get_IsValid(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLocal(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> Boolean: ...
    @winrt_mixinmethod
    def get_NetworkAccessKind(self: Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> Windows.Networking.XboxLive.XboxLiveNetworkAccessKind: ...
    @winrt_classmethod
    def CreateFromSnapshotBase64(cls: Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics, base64: WinRT_String) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def CreateFromSnapshotBuffer(cls: Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def CreateFromSnapshotBytes(cls: Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics, buffer: POINTER(Byte)) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def GetLocal(cls: Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def get_MaxSnapshotBytesSize(cls: Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics) -> UInt32: ...
    IsValid = property(get_IsValid, None)
    IsLocal = property(get_IsLocal, None)
    NetworkAccessKind = property(get_NetworkAccessKind, None)
    _XboxLiveDeviceAddress_Meta_.MaxSnapshotBytesSize = property(get_MaxSnapshotBytesSize.__wrapped__, None)
class XboxLiveEndpointPair(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveEndpointPair
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPair'
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.XboxLive.XboxLiveEndpointPair, Windows.Networking.XboxLive.XboxLiveEndpointPairStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetRemoteSocketAddressBytes(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair, socketAddress: POINTER(Byte)) -> Void: ...
    @winrt_mixinmethod
    def GetLocalSocketAddressBytes(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair, socketAddress: POINTER(Byte)) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_mixinmethod
    def get_Template(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_mixinmethod
    def get_RemoteDeviceAddress(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalHostName(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> WinRT_String: ...
    @winrt_classmethod
    def FindEndpointPairBySocketAddressBytes(cls: Windows.Networking.XboxLive.IXboxLiveEndpointPairStatics, localSocketAddress: POINTER(Byte), remoteSocketAddress: POINTER(Byte)) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    @winrt_classmethod
    def FindEndpointPairByHostNamesAndPorts(cls: Windows.Networking.XboxLive.IXboxLiveEndpointPairStatics, localHostName: Windows.Networking.HostName, localPort: WinRT_String, remoteHostName: Windows.Networking.HostName, remotePort: WinRT_String) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    State = property(get_State, None)
    Template = property(get_Template, None)
    RemoteDeviceAddress = property(get_RemoteDeviceAddress, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemotePort = property(get_RemotePort, None)
    LocalHostName = property(get_LocalHostName, None)
    LocalPort = property(get_LocalPort, None)
XboxLiveEndpointPairCreationBehaviors = UInt32
XboxLiveEndpointPairCreationBehaviors_None: XboxLiveEndpointPairCreationBehaviors = 0
XboxLiveEndpointPairCreationBehaviors_ReevaluatePath: XboxLiveEndpointPairCreationBehaviors = 1
class XboxLiveEndpointPairCreationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult'
    @winrt_mixinmethod
    def get_DeviceAddress(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> Windows.Networking.XboxLive.XboxLiveEndpointPairCreationStatus: ...
    @winrt_mixinmethod
    def get_IsExistingPathEvaluation(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_EndpointPair(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    DeviceAddress = property(get_DeviceAddress, None)
    Status = property(get_Status, None)
    IsExistingPathEvaluation = property(get_IsExistingPathEvaluation, None)
    EndpointPair = property(get_EndpointPair, None)
XboxLiveEndpointPairCreationStatus = Int32
XboxLiveEndpointPairCreationStatus_Succeeded: XboxLiveEndpointPairCreationStatus = 0
XboxLiveEndpointPairCreationStatus_NoLocalNetworks: XboxLiveEndpointPairCreationStatus = 1
XboxLiveEndpointPairCreationStatus_NoCompatibleNetworkPaths: XboxLiveEndpointPairCreationStatus = 2
XboxLiveEndpointPairCreationStatus_LocalSystemNotAuthorized: XboxLiveEndpointPairCreationStatus = 3
XboxLiveEndpointPairCreationStatus_Canceled: XboxLiveEndpointPairCreationStatus = 4
XboxLiveEndpointPairCreationStatus_TimedOut: XboxLiveEndpointPairCreationStatus = 5
XboxLiveEndpointPairCreationStatus_RemoteSystemNotAuthorized: XboxLiveEndpointPairCreationStatus = 6
XboxLiveEndpointPairCreationStatus_RefusedDueToConfiguration: XboxLiveEndpointPairCreationStatus = 7
XboxLiveEndpointPairCreationStatus_UnexpectedInternalError: XboxLiveEndpointPairCreationStatus = 8
XboxLiveEndpointPairState = Int32
XboxLiveEndpointPairState_Invalid: XboxLiveEndpointPairState = 0
XboxLiveEndpointPairState_CreatingOutbound: XboxLiveEndpointPairState = 1
XboxLiveEndpointPairState_CreatingInbound: XboxLiveEndpointPairState = 2
XboxLiveEndpointPairState_Ready: XboxLiveEndpointPairState = 3
XboxLiveEndpointPairState_DeletingLocally: XboxLiveEndpointPairState = 4
XboxLiveEndpointPairState_RemoteEndpointTerminating: XboxLiveEndpointPairState = 5
XboxLiveEndpointPairState_Deleted: XboxLiveEndpointPairState = 6
class XboxLiveEndpointPairStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPairStateChangedEventArgs'
    @winrt_mixinmethod
    def get_OldState(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs) -> Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_mixinmethod
    def get_NewState(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs) -> Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    OldState = property(get_OldState, None)
    NewState = property(get_NewState, None)
class _XboxLiveEndpointPairTemplate_Meta_(ComPtr.__class__):
    pass
class XboxLiveEndpointPairTemplate(ComPtr, metaclass=_XboxLiveEndpointPairTemplate_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate'
    @winrt_mixinmethod
    def add_InboundEndpointPairCreated(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate, Windows.Networking.XboxLive.XboxLiveInboundEndpointPairCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InboundEndpointPairCreated(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateEndpointPairDefaultAsync(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def CreateEndpointPairWithBehaviorsAsync(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, behaviors: Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def CreateEndpointPairForPortsDefaultAsync(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def CreateEndpointPairForPortsWithBehaviorsAsync(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String, behaviors: Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> Windows.Foundation.IAsyncOperation[Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SocketKind(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> Windows.Networking.XboxLive.XboxLiveSocketKind: ...
    @winrt_mixinmethod
    def get_InitiatorBoundPortRangeLower(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_InitiatorBoundPortRangeUpper(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_AcceptorBoundPortRangeLower(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_AcceptorBoundPortRangeUpper(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_EndpointPairs(self: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveEndpointPair]: ...
    @winrt_classmethod
    def GetTemplateByName(cls: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplateStatics, name: WinRT_String) -> Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_classmethod
    def get_Templates(cls: Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplateStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate]: ...
    Name = property(get_Name, None)
    SocketKind = property(get_SocketKind, None)
    InitiatorBoundPortRangeLower = property(get_InitiatorBoundPortRangeLower, None)
    InitiatorBoundPortRangeUpper = property(get_InitiatorBoundPortRangeUpper, None)
    AcceptorBoundPortRangeLower = property(get_AcceptorBoundPortRangeLower, None)
    AcceptorBoundPortRangeUpper = property(get_AcceptorBoundPortRangeUpper, None)
    EndpointPairs = property(get_EndpointPairs, None)
    _XboxLiveEndpointPairTemplate_Meta_.Templates = property(get_Templates.__wrapped__, None)
class XboxLiveInboundEndpointPairCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveInboundEndpointPairCreatedEventArgs
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveInboundEndpointPairCreatedEventArgs'
    @winrt_mixinmethod
    def get_EndpointPair(self: Windows.Networking.XboxLive.IXboxLiveInboundEndpointPairCreatedEventArgs) -> Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    EndpointPair = property(get_EndpointPair, None)
XboxLiveNetworkAccessKind = Int32
XboxLiveNetworkAccessKind_Open: XboxLiveNetworkAccessKind = 0
XboxLiveNetworkAccessKind_Moderate: XboxLiveNetworkAccessKind = 1
XboxLiveNetworkAccessKind_Strict: XboxLiveNetworkAccessKind = 2
class _XboxLiveQualityOfServiceMeasurement_Meta_(ComPtr.__class__):
    pass
class XboxLiveQualityOfServiceMeasurement(ComPtr, metaclass=_XboxLiveQualityOfServiceMeasurement_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurement'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurement: ...
    @winrt_mixinmethod
    def MeasureAsync(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMetricResultsForDevice(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_mixinmethod
    def GetMetricResultsForMetric(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, metric: Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_mixinmethod
    def GetMetricResult(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress, metric: Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult: ...
    @winrt_mixinmethod
    def GetPrivatePayloadResult(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, deviceAddress: Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult: ...
    @winrt_mixinmethod
    def get_Metrics(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Windows.Foundation.Collections.IVector[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric]: ...
    @winrt_mixinmethod
    def get_DeviceAddresses(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Windows.Foundation.Collections.IVector[Windows.Networking.XboxLive.XboxLiveDeviceAddress]: ...
    @winrt_mixinmethod
    def get_ShouldRequestPrivatePayloads(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldRequestPrivatePayloads(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TimeoutInMilliseconds(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> UInt32: ...
    @winrt_mixinmethod
    def put_TimeoutInMilliseconds(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberOfProbesToAttempt(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> UInt32: ...
    @winrt_mixinmethod
    def put_NumberOfProbesToAttempt(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberOfResultsPending(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> UInt32: ...
    @winrt_mixinmethod
    def get_MetricResults(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_mixinmethod
    def get_PrivatePayloadResults(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult]: ...
    @winrt_classmethod
    def PublishPrivatePayloadBytes(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, payload: POINTER(Byte)) -> Void: ...
    @winrt_classmethod
    def ClearPrivatePayload(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Void: ...
    @winrt_classmethod
    def get_MaxSimultaneousProbeConnections(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> UInt32: ...
    @winrt_classmethod
    def put_MaxSimultaneousProbeConnections(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: UInt32) -> Void: ...
    @winrt_classmethod
    def get_IsSystemOutboundBandwidthConstrained(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Boolean: ...
    @winrt_classmethod
    def put_IsSystemOutboundBandwidthConstrained(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsSystemInboundBandwidthConstrained(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Boolean: ...
    @winrt_classmethod
    def put_IsSystemInboundBandwidthConstrained(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_PublishedPrivatePayload(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def put_PublishedPrivatePayload(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_classmethod
    def get_MaxPrivatePayloadSize(cls: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> UInt32: ...
    Metrics = property(get_Metrics, None)
    DeviceAddresses = property(get_DeviceAddresses, None)
    ShouldRequestPrivatePayloads = property(get_ShouldRequestPrivatePayloads, put_ShouldRequestPrivatePayloads)
    TimeoutInMilliseconds = property(get_TimeoutInMilliseconds, put_TimeoutInMilliseconds)
    NumberOfProbesToAttempt = property(get_NumberOfProbesToAttempt, put_NumberOfProbesToAttempt)
    NumberOfResultsPending = property(get_NumberOfResultsPending, None)
    MetricResults = property(get_MetricResults, None)
    PrivatePayloadResults = property(get_PrivatePayloadResults, None)
    _XboxLiveQualityOfServiceMeasurement_Meta_.MaxSimultaneousProbeConnections = property(get_MaxSimultaneousProbeConnections.__wrapped__, put_MaxSimultaneousProbeConnections.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.IsSystemOutboundBandwidthConstrained = property(get_IsSystemOutboundBandwidthConstrained.__wrapped__, put_IsSystemOutboundBandwidthConstrained.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.IsSystemInboundBandwidthConstrained = property(get_IsSystemInboundBandwidthConstrained.__wrapped__, put_IsSystemInboundBandwidthConstrained.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.PublishedPrivatePayload = property(get_PublishedPrivatePayload.__wrapped__, put_PublishedPrivatePayload.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.MaxPrivatePayloadSize = property(get_MaxPrivatePayloadSize.__wrapped__, None)
XboxLiveQualityOfServiceMeasurementStatus = Int32
XboxLiveQualityOfServiceMeasurementStatus_NotStarted: XboxLiveQualityOfServiceMeasurementStatus = 0
XboxLiveQualityOfServiceMeasurementStatus_InProgress: XboxLiveQualityOfServiceMeasurementStatus = 1
XboxLiveQualityOfServiceMeasurementStatus_InProgressWithProvisionalResults: XboxLiveQualityOfServiceMeasurementStatus = 2
XboxLiveQualityOfServiceMeasurementStatus_Succeeded: XboxLiveQualityOfServiceMeasurementStatus = 3
XboxLiveQualityOfServiceMeasurementStatus_NoLocalNetworks: XboxLiveQualityOfServiceMeasurementStatus = 4
XboxLiveQualityOfServiceMeasurementStatus_NoCompatibleNetworkPaths: XboxLiveQualityOfServiceMeasurementStatus = 5
XboxLiveQualityOfServiceMeasurementStatus_LocalSystemNotAuthorized: XboxLiveQualityOfServiceMeasurementStatus = 6
XboxLiveQualityOfServiceMeasurementStatus_Canceled: XboxLiveQualityOfServiceMeasurementStatus = 7
XboxLiveQualityOfServiceMeasurementStatus_TimedOut: XboxLiveQualityOfServiceMeasurementStatus = 8
XboxLiveQualityOfServiceMeasurementStatus_RemoteSystemNotAuthorized: XboxLiveQualityOfServiceMeasurementStatus = 9
XboxLiveQualityOfServiceMeasurementStatus_RefusedDueToConfiguration: XboxLiveQualityOfServiceMeasurementStatus = 10
XboxLiveQualityOfServiceMeasurementStatus_UnexpectedInternalError: XboxLiveQualityOfServiceMeasurementStatus = 11
XboxLiveQualityOfServiceMetric = Int32
XboxLiveQualityOfServiceMetric_AverageLatencyInMilliseconds: XboxLiveQualityOfServiceMetric = 0
XboxLiveQualityOfServiceMetric_MinLatencyInMilliseconds: XboxLiveQualityOfServiceMetric = 1
XboxLiveQualityOfServiceMetric_MaxLatencyInMilliseconds: XboxLiveQualityOfServiceMetric = 2
XboxLiveQualityOfServiceMetric_AverageOutboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 3
XboxLiveQualityOfServiceMetric_MinOutboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 4
XboxLiveQualityOfServiceMetric_MaxOutboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 5
XboxLiveQualityOfServiceMetric_AverageInboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 6
XboxLiveQualityOfServiceMetric_MinInboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 7
XboxLiveQualityOfServiceMetric_MaxInboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 8
class XboxLiveQualityOfServiceMetricResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_mixinmethod
    def get_DeviceAddress(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_Metric(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> UInt64: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Metric = property(get_Metric, None)
    Value = property(get_Value, None)
class XboxLiveQualityOfServicePrivatePayloadResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult) -> Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_mixinmethod
    def get_DeviceAddress(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult) -> Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Value = property(get_Value, None)
XboxLiveSecureSocketsContract: UInt32 = 65536
XboxLiveSocketKind = Int32
XboxLiveSocketKind_None: XboxLiveSocketKind = 0
XboxLiveSocketKind_Datagram: XboxLiveSocketKind = 1
XboxLiveSocketKind_Stream: XboxLiveSocketKind = 2
make_head(_module, 'IXboxLiveDeviceAddress')
make_head(_module, 'IXboxLiveDeviceAddressStatics')
make_head(_module, 'IXboxLiveEndpointPair')
make_head(_module, 'IXboxLiveEndpointPairCreationResult')
make_head(_module, 'IXboxLiveEndpointPairStateChangedEventArgs')
make_head(_module, 'IXboxLiveEndpointPairStatics')
make_head(_module, 'IXboxLiveEndpointPairTemplate')
make_head(_module, 'IXboxLiveEndpointPairTemplateStatics')
make_head(_module, 'IXboxLiveInboundEndpointPairCreatedEventArgs')
make_head(_module, 'IXboxLiveQualityOfServiceMeasurement')
make_head(_module, 'IXboxLiveQualityOfServiceMeasurementStatics')
make_head(_module, 'IXboxLiveQualityOfServiceMetricResult')
make_head(_module, 'IXboxLiveQualityOfServicePrivatePayloadResult')
make_head(_module, 'XboxLiveDeviceAddress')
make_head(_module, 'XboxLiveEndpointPair')
make_head(_module, 'XboxLiveEndpointPairCreationResult')
make_head(_module, 'XboxLiveEndpointPairStateChangedEventArgs')
make_head(_module, 'XboxLiveEndpointPairTemplate')
make_head(_module, 'XboxLiveInboundEndpointPairCreatedEventArgs')
make_head(_module, 'XboxLiveQualityOfServiceMeasurement')
make_head(_module, 'XboxLiveQualityOfServiceMetricResult')
make_head(_module, 'XboxLiveQualityOfServicePrivatePayloadResult')
