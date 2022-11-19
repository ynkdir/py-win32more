from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.HostComputeNetwork

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
HCN_NOTIFICATIONS = Int32
HCN_NOTIFICATIONS_HcnNotificationInvalid = 0
HCN_NOTIFICATIONS_HcnNotificationNetworkPreCreate = 1
HCN_NOTIFICATIONS_HcnNotificationNetworkCreate = 2
HCN_NOTIFICATIONS_HcnNotificationNetworkPreDelete = 3
HCN_NOTIFICATIONS_HcnNotificationNetworkDelete = 4
HCN_NOTIFICATIONS_HcnNotificationNamespaceCreate = 5
HCN_NOTIFICATIONS_HcnNotificationNamespaceDelete = 6
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceCreate = 7
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceDelete = 8
HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointAttached = 9
HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointDetached = 16
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceStateChanged = 17
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceInterfaceStateChanged = 18
HCN_NOTIFICATIONS_HcnNotificationServiceDisconnect = 16777216
HCN_NOTIFICATIONS_HcnNotificationFlagsReserved = -268435456
def _define_HCN_NOTIFICATION_CALLBACK():
    return CFUNCTYPE(Void,UInt32,c_void_p,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)
HCN_PORT_PROTOCOL = Int32
HCN_PORT_PROTOCOL_TCP = 1
HCN_PORT_PROTOCOL_UDP = 2
HCN_PORT_PROTOCOL_BOTH = 3
HCN_PORT_ACCESS = Int32
HCN_PORT_ACCESS_EXCLUSIVE = 1
HCN_PORT_ACCESS_SHARED = 2
def _define_HCN_PORT_RANGE_RESERVATION_head():
    class HCN_PORT_RANGE_RESERVATION(Structure):
        pass
    return HCN_PORT_RANGE_RESERVATION
def _define_HCN_PORT_RANGE_RESERVATION():
    HCN_PORT_RANGE_RESERVATION = win32more.System.HostComputeNetwork.HCN_PORT_RANGE_RESERVATION_head
    HCN_PORT_RANGE_RESERVATION._fields_ = [
        ("startingPort", UInt16),
        ("endingPort", UInt16),
    ]
    return HCN_PORT_RANGE_RESERVATION
def _define_HCN_PORT_RANGE_ENTRY_head():
    class HCN_PORT_RANGE_ENTRY(Structure):
        pass
    return HCN_PORT_RANGE_ENTRY
def _define_HCN_PORT_RANGE_ENTRY():
    HCN_PORT_RANGE_ENTRY = win32more.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head
    HCN_PORT_RANGE_ENTRY._fields_ = [
        ("OwningPartitionId", Guid),
        ("TargetPartitionId", Guid),
        ("Protocol", win32more.System.HostComputeNetwork.HCN_PORT_PROTOCOL),
        ("Priority", UInt64),
        ("ReservationType", UInt32),
        ("SharingFlags", UInt32),
        ("DeliveryMode", UInt32),
        ("StartingPort", UInt16),
        ("EndingPort", UInt16),
    ]
    return HCN_PORT_RANGE_ENTRY
def _define_HcnEnumerateNetworks():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnEnumerateNetworks", windll["computenetwork"]), ((1, 'Query'),(1, 'Networks'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnCreateNetwork", windll["computenetwork"]), ((1, 'Id'),(1, 'Settings'),(1, 'Network'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnOpenNetwork", windll["computenetwork"]), ((1, 'Id'),(1, 'Network'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnModifyNetwork", windll["computenetwork"]), ((1, 'Network'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryNetworkProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnQueryNetworkProperties", windll["computenetwork"]), ((1, 'Network'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnDeleteNetwork", windll["computenetwork"]), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnCloseNetwork", windll["computenetwork"]), ((1, 'Network'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateNamespaces():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnEnumerateNamespaces", windll["computenetwork"]), ((1, 'Query'),(1, 'Namespaces'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnCreateNamespace", windll["computenetwork"]), ((1, 'Id'),(1, 'Settings'),(1, 'Namespace'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnOpenNamespace", windll["computenetwork"]), ((1, 'Id'),(1, 'Namespace'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnModifyNamespace", windll["computenetwork"]), ((1, 'Namespace'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryNamespaceProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnQueryNamespaceProperties", windll["computenetwork"]), ((1, 'Namespace'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnDeleteNamespace", windll["computenetwork"]), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnCloseNamespace", windll["computenetwork"]), ((1, 'Namespace'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateEndpoints():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnEnumerateEndpoints", windll["computenetwork"]), ((1, 'Query'),(1, 'Endpoints'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnCreateEndpoint", windll["computenetwork"]), ((1, 'Network'),(1, 'Id'),(1, 'Settings'),(1, 'Endpoint'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnOpenEndpoint", windll["computenetwork"]), ((1, 'Id'),(1, 'Endpoint'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnModifyEndpoint", windll["computenetwork"]), ((1, 'Endpoint'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryEndpointProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnQueryEndpointProperties", windll["computenetwork"]), ((1, 'Endpoint'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnDeleteEndpoint", windll["computenetwork"]), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnCloseEndpoint", windll["computenetwork"]), ((1, 'Endpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateLoadBalancers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnEnumerateLoadBalancers", windll["computenetwork"]), ((1, 'Query'),(1, 'LoadBalancer'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnCreateLoadBalancer", windll["computenetwork"]), ((1, 'Id'),(1, 'Settings'),(1, 'LoadBalancer'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnOpenLoadBalancer", windll["computenetwork"]), ((1, 'Id'),(1, 'LoadBalancer'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnModifyLoadBalancer", windll["computenetwork"]), ((1, 'LoadBalancer'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryLoadBalancerProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnQueryLoadBalancerProperties", windll["computenetwork"]), ((1, 'LoadBalancer'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnDeleteLoadBalancer", windll["computenetwork"]), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnCloseLoadBalancer", windll["computenetwork"]), ((1, 'LoadBalancer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnRegisterServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK,c_void_p,POINTER(c_void_p), use_last_error=False)(("HcnRegisterServiceCallback", windll["computenetwork"]), ((1, 'Callback'),(1, 'Context'),(1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnUnregisterServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnUnregisterServiceCallback", windll["computenetwork"]), ((1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnRegisterGuestNetworkServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK,c_void_p,POINTER(c_void_p), use_last_error=False)(("HcnRegisterGuestNetworkServiceCallback", windll["computenetwork"]), ((1, 'GuestNetworkService'),(1, 'Callback'),(1, 'Context'),(1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnUnregisterGuestNetworkServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnUnregisterGuestNetworkServiceCallback", windll["computenetwork"]), ((1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnCreateGuestNetworkService", windll["computenetwork"]), ((1, 'Id'),(1, 'Settings'),(1, 'GuestNetworkService'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("HcnCloseGuestNetworkService", windll["computenetwork"]), ((1, 'GuestNetworkService'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnModifyGuestNetworkService", windll["computenetwork"]), ((1, 'GuestNetworkService'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HcnDeleteGuestNetworkService", windll["computenetwork"]), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnReserveGuestNetworkServicePort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.HostComputeNetwork.HCN_PORT_PROTOCOL,win32more.System.HostComputeNetwork.HCN_PORT_ACCESS,UInt16,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("HcnReserveGuestNetworkServicePort", windll["computenetwork"]), ((1, 'GuestNetworkService'),(1, 'Protocol'),(1, 'Access'),(1, 'Port'),(1, 'PortReservationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnReserveGuestNetworkServicePortRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt16,POINTER(win32more.System.HostComputeNetwork.HCN_PORT_RANGE_RESERVATION_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("HcnReserveGuestNetworkServicePortRange", windll["computenetwork"]), ((1, 'GuestNetworkService'),(1, 'PortCount'),(1, 'PortRangeReservation'),(1, 'PortReservationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnReleaseGuestNetworkServicePortReservationHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(("HcnReleaseGuestNetworkServicePortReservationHandle", windll["computenetwork"]), ((1, 'PortReservationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateGuestNetworkPortReservations():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head)), use_last_error=False)(("HcnEnumerateGuestNetworkPortReservations", windll["computenetwork"]), ((1, 'ReturnCount'),(1, 'PortEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnFreeGuestNetworkPortReservations():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head), use_last_error=False)(("HcnFreeGuestNetworkPortReservations", windll["computenetwork"]), ((1, 'PortEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "HCN_NOTIFICATIONS",
    "HCN_NOTIFICATIONS_HcnNotificationInvalid",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkPreCreate",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkCreate",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkPreDelete",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkDelete",
    "HCN_NOTIFICATIONS_HcnNotificationNamespaceCreate",
    "HCN_NOTIFICATIONS_HcnNotificationNamespaceDelete",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceCreate",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceDelete",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointAttached",
    "HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointDetached",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceStateChanged",
    "HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceInterfaceStateChanged",
    "HCN_NOTIFICATIONS_HcnNotificationServiceDisconnect",
    "HCN_NOTIFICATIONS_HcnNotificationFlagsReserved",
    "HCN_NOTIFICATION_CALLBACK",
    "HCN_PORT_PROTOCOL",
    "HCN_PORT_PROTOCOL_TCP",
    "HCN_PORT_PROTOCOL_UDP",
    "HCN_PORT_PROTOCOL_BOTH",
    "HCN_PORT_ACCESS",
    "HCN_PORT_ACCESS_EXCLUSIVE",
    "HCN_PORT_ACCESS_SHARED",
    "HCN_PORT_RANGE_RESERVATION",
    "HCN_PORT_RANGE_ENTRY",
    "HcnEnumerateNetworks",
    "HcnCreateNetwork",
    "HcnOpenNetwork",
    "HcnModifyNetwork",
    "HcnQueryNetworkProperties",
    "HcnDeleteNetwork",
    "HcnCloseNetwork",
    "HcnEnumerateNamespaces",
    "HcnCreateNamespace",
    "HcnOpenNamespace",
    "HcnModifyNamespace",
    "HcnQueryNamespaceProperties",
    "HcnDeleteNamespace",
    "HcnCloseNamespace",
    "HcnEnumerateEndpoints",
    "HcnCreateEndpoint",
    "HcnOpenEndpoint",
    "HcnModifyEndpoint",
    "HcnQueryEndpointProperties",
    "HcnDeleteEndpoint",
    "HcnCloseEndpoint",
    "HcnEnumerateLoadBalancers",
    "HcnCreateLoadBalancer",
    "HcnOpenLoadBalancer",
    "HcnModifyLoadBalancer",
    "HcnQueryLoadBalancerProperties",
    "HcnDeleteLoadBalancer",
    "HcnCloseLoadBalancer",
    "HcnRegisterServiceCallback",
    "HcnUnregisterServiceCallback",
    "HcnRegisterGuestNetworkServiceCallback",
    "HcnUnregisterGuestNetworkServiceCallback",
    "HcnCreateGuestNetworkService",
    "HcnCloseGuestNetworkService",
    "HcnModifyGuestNetworkService",
    "HcnDeleteGuestNetworkService",
    "HcnReserveGuestNetworkServicePort",
    "HcnReserveGuestNetworkServicePortRange",
    "HcnReleaseGuestNetworkServicePortReservationHandle",
    "HcnEnumerateGuestNetworkPortReservations",
    "HcnFreeGuestNetworkPortReservations",
]
