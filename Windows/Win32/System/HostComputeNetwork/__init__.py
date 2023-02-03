from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.HostComputeNetwork
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('computenetwork.dll')
def HcnEnumerateNetworks(Query: Windows.Win32.Foundation.PWSTR, Networks: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateNetwork(Id: POINTER(Guid), Settings: Windows.Win32.Foundation.PWSTR, Network: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenNetwork(Id: POINTER(Guid), Network: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyNetwork(Network: c_void_p, Settings: Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryNetworkProperties(Network: c_void_p, Query: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteNetwork(Id: POINTER(Guid), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseNetwork(Network: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateNamespaces(Query: Windows.Win32.Foundation.PWSTR, Namespaces: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateNamespace(Id: POINTER(Guid), Settings: Windows.Win32.Foundation.PWSTR, Namespace: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenNamespace(Id: POINTER(Guid), Namespace: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyNamespace(Namespace: c_void_p, Settings: Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryNamespaceProperties(Namespace: c_void_p, Query: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteNamespace(Id: POINTER(Guid), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseNamespace(Namespace: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateEndpoints(Query: Windows.Win32.Foundation.PWSTR, Endpoints: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateEndpoint(Network: c_void_p, Id: POINTER(Guid), Settings: Windows.Win32.Foundation.PWSTR, Endpoint: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenEndpoint(Id: POINTER(Guid), Endpoint: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyEndpoint(Endpoint: c_void_p, Settings: Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryEndpointProperties(Endpoint: c_void_p, Query: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteEndpoint(Id: POINTER(Guid), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseEndpoint(Endpoint: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateLoadBalancers(Query: Windows.Win32.Foundation.PWSTR, LoadBalancer: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateLoadBalancer(Id: POINTER(Guid), Settings: Windows.Win32.Foundation.PWSTR, LoadBalancer: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenLoadBalancer(Id: POINTER(Guid), LoadBalancer: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyLoadBalancer(LoadBalancer: c_void_p, Settings: Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryLoadBalancerProperties(LoadBalancer: c_void_p, Query: Windows.Win32.Foundation.PWSTR, Properties: POINTER(Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteLoadBalancer(Id: POINTER(Guid), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseLoadBalancer(LoadBalancer: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnRegisterServiceCallback(Callback: Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK, Context: c_void_p, CallbackHandle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnUnregisterServiceCallback(CallbackHandle: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnRegisterGuestNetworkServiceCallback(GuestNetworkService: c_void_p, Callback: Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK, Context: c_void_p, CallbackHandle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnUnregisterGuestNetworkServiceCallback(CallbackHandle: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateGuestNetworkService(Id: POINTER(Guid), Settings: Windows.Win32.Foundation.PWSTR, GuestNetworkService: POINTER(c_void_p), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseGuestNetworkService(GuestNetworkService: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyGuestNetworkService(GuestNetworkService: c_void_p, Settings: Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteGuestNetworkService(Id: POINTER(Guid), ErrorRecord: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnReserveGuestNetworkServicePort(GuestNetworkService: c_void_p, Protocol: Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL, Access: Windows.Win32.System.HostComputeNetwork.HCN_PORT_ACCESS, Port: UInt16, PortReservationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnReserveGuestNetworkServicePortRange(GuestNetworkService: c_void_p, PortCount: UInt16, PortRangeReservation: POINTER(Windows.Win32.System.HostComputeNetwork.HCN_PORT_RANGE_RESERVATION_head), PortReservationHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnReleaseGuestNetworkServicePortReservationHandle(PortReservationHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateGuestNetworkPortReservations(ReturnCount: POINTER(UInt32), PortEntries: POINTER(POINTER(Windows.Win32.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnFreeGuestNetworkPortReservations(PortEntries: POINTER(Windows.Win32.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head)) -> Void: ...
HCN_NOTIFICATIONS = Int32
HCN_NOTIFICATIONS_HcnNotificationInvalid: HCN_NOTIFICATIONS = 0
HCN_NOTIFICATIONS_HcnNotificationNetworkPreCreate: HCN_NOTIFICATIONS = 1
HCN_NOTIFICATIONS_HcnNotificationNetworkCreate: HCN_NOTIFICATIONS = 2
HCN_NOTIFICATIONS_HcnNotificationNetworkPreDelete: HCN_NOTIFICATIONS = 3
HCN_NOTIFICATIONS_HcnNotificationNetworkDelete: HCN_NOTIFICATIONS = 4
HCN_NOTIFICATIONS_HcnNotificationNamespaceCreate: HCN_NOTIFICATIONS = 5
HCN_NOTIFICATIONS_HcnNotificationNamespaceDelete: HCN_NOTIFICATIONS = 6
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceCreate: HCN_NOTIFICATIONS = 7
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceDelete: HCN_NOTIFICATIONS = 8
HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointAttached: HCN_NOTIFICATIONS = 9
HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointDetached: HCN_NOTIFICATIONS = 16
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceStateChanged: HCN_NOTIFICATIONS = 17
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceInterfaceStateChanged: HCN_NOTIFICATIONS = 18
HCN_NOTIFICATIONS_HcnNotificationServiceDisconnect: HCN_NOTIFICATIONS = 16777216
HCN_NOTIFICATIONS_HcnNotificationFlagsReserved: HCN_NOTIFICATIONS = -268435456
@winfunctype_pointer
def HCN_NOTIFICATION_CALLBACK(NotificationType: UInt32, Context: c_void_p, NotificationStatus: Windows.Win32.Foundation.HRESULT, NotificationData: Windows.Win32.Foundation.PWSTR) -> Void: ...
HCN_PORT_ACCESS = Int32
HCN_PORT_ACCESS_EXCLUSIVE: HCN_PORT_ACCESS = 1
HCN_PORT_ACCESS_SHARED: HCN_PORT_ACCESS = 2
HCN_PORT_PROTOCOL = Int32
HCN_PORT_PROTOCOL_TCP: HCN_PORT_PROTOCOL = 1
HCN_PORT_PROTOCOL_UDP: HCN_PORT_PROTOCOL = 2
HCN_PORT_PROTOCOL_BOTH: HCN_PORT_PROTOCOL = 3
class HCN_PORT_RANGE_ENTRY(Structure):
    OwningPartitionId: Guid
    TargetPartitionId: Guid
    Protocol: Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL
    Priority: UInt64
    ReservationType: UInt32
    SharingFlags: UInt32
    DeliveryMode: UInt32
    StartingPort: UInt16
    EndingPort: UInt16
class HCN_PORT_RANGE_RESERVATION(Structure):
    startingPort: UInt16
    endingPort: UInt16
make_head(_module, 'HCN_NOTIFICATION_CALLBACK')
make_head(_module, 'HCN_PORT_RANGE_ENTRY')
make_head(_module, 'HCN_PORT_RANGE_RESERVATION')
__all__ = [
    "HCN_NOTIFICATIONS",
    "HCN_NOTIFICATIONS_HcnNotificationFlagsReserved",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceCreate",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceDelete",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceInterfaceStateChanged",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceStateChanged",
    "HCN_NOTIFICATIONS_HcnNotificationInvalid",
    "HCN_NOTIFICATIONS_HcnNotificationNamespaceCreate",
    "HCN_NOTIFICATIONS_HcnNotificationNamespaceDelete",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkCreate",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkDelete",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointAttached",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointDetached",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkPreCreate",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkPreDelete",
    "HCN_NOTIFICATIONS_HcnNotificationServiceDisconnect",
    "HCN_NOTIFICATION_CALLBACK",
    "HCN_PORT_ACCESS",
    "HCN_PORT_ACCESS_EXCLUSIVE",
    "HCN_PORT_ACCESS_SHARED",
    "HCN_PORT_PROTOCOL",
    "HCN_PORT_PROTOCOL_BOTH",
    "HCN_PORT_PROTOCOL_TCP",
    "HCN_PORT_PROTOCOL_UDP",
    "HCN_PORT_RANGE_ENTRY",
    "HCN_PORT_RANGE_RESERVATION",
    "HcnCloseEndpoint",
    "HcnCloseGuestNetworkService",
    "HcnCloseLoadBalancer",
    "HcnCloseNamespace",
    "HcnCloseNetwork",
    "HcnCreateEndpoint",
    "HcnCreateGuestNetworkService",
    "HcnCreateLoadBalancer",
    "HcnCreateNamespace",
    "HcnCreateNetwork",
    "HcnDeleteEndpoint",
    "HcnDeleteGuestNetworkService",
    "HcnDeleteLoadBalancer",
    "HcnDeleteNamespace",
    "HcnDeleteNetwork",
    "HcnEnumerateEndpoints",
    "HcnEnumerateGuestNetworkPortReservations",
    "HcnEnumerateLoadBalancers",
    "HcnEnumerateNamespaces",
    "HcnEnumerateNetworks",
    "HcnFreeGuestNetworkPortReservations",
    "HcnModifyEndpoint",
    "HcnModifyGuestNetworkService",
    "HcnModifyLoadBalancer",
    "HcnModifyNamespace",
    "HcnModifyNetwork",
    "HcnOpenEndpoint",
    "HcnOpenLoadBalancer",
    "HcnOpenNamespace",
    "HcnOpenNetwork",
    "HcnQueryEndpointProperties",
    "HcnQueryLoadBalancerProperties",
    "HcnQueryNamespaceProperties",
    "HcnQueryNetworkProperties",
    "HcnRegisterGuestNetworkServiceCallback",
    "HcnRegisterServiceCallback",
    "HcnReleaseGuestNetworkServicePortReservationHandle",
    "HcnReserveGuestNetworkServicePort",
    "HcnReserveGuestNetworkServicePortRange",
    "HcnUnregisterGuestNetworkServiceCallback",
    "HcnUnregisterServiceCallback",
]
_arch_optional = [
]
