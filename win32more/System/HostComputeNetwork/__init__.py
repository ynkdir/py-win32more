from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.HostComputeNetwork
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_HcnEnumerateNetworks():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnEnumerateNetworks', windll['computenetwork.dll']), ((1, 'Query'),(1, 'Networks'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnCreateNetwork', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Settings'),(1, 'Network'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnOpenNetwork', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Network'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcnModifyNetwork', windll['computenetwork.dll']), ((1, 'Network'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryNetworkProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnQueryNetworkProperties', windll['computenetwork.dll']), ((1, 'Network'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('HcnDeleteNetwork', windll['computenetwork.dll']), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseNetwork():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnCloseNetwork', windll['computenetwork.dll']), ((1, 'Network'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateNamespaces():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnEnumerateNamespaces', windll['computenetwork.dll']), ((1, 'Query'),(1, 'Namespaces'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnCreateNamespace', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Settings'),(1, 'Namespace'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnOpenNamespace', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Namespace'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcnModifyNamespace', windll['computenetwork.dll']), ((1, 'Namespace'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryNamespaceProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnQueryNamespaceProperties', windll['computenetwork.dll']), ((1, 'Namespace'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('HcnDeleteNamespace', windll['computenetwork.dll']), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnCloseNamespace', windll['computenetwork.dll']), ((1, 'Namespace'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateEndpoints():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnEnumerateEndpoints', windll['computenetwork.dll']), ((1, 'Query'),(1, 'Endpoints'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnCreateEndpoint', windll['computenetwork.dll']), ((1, 'Network'),(1, 'Id'),(1, 'Settings'),(1, 'Endpoint'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnOpenEndpoint', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Endpoint'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcnModifyEndpoint', windll['computenetwork.dll']), ((1, 'Endpoint'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryEndpointProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnQueryEndpointProperties', windll['computenetwork.dll']), ((1, 'Endpoint'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('HcnDeleteEndpoint', windll['computenetwork.dll']), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseEndpoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnCloseEndpoint', windll['computenetwork.dll']), ((1, 'Endpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateLoadBalancers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnEnumerateLoadBalancers', windll['computenetwork.dll']), ((1, 'Query'),(1, 'LoadBalancer'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnCreateLoadBalancer', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Settings'),(1, 'LoadBalancer'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnOpenLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnOpenLoadBalancer', windll['computenetwork.dll']), ((1, 'Id'),(1, 'LoadBalancer'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcnModifyLoadBalancer', windll['computenetwork.dll']), ((1, 'LoadBalancer'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnQueryLoadBalancerProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(('HcnQueryLoadBalancerProperties', windll['computenetwork.dll']), ((1, 'LoadBalancer'),(1, 'Query'),(1, 'Properties'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('HcnDeleteLoadBalancer', windll['computenetwork.dll']), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseLoadBalancer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnCloseLoadBalancer', windll['computenetwork.dll']), ((1, 'LoadBalancer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnRegisterServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK,c_void_p,POINTER(c_void_p))(('HcnRegisterServiceCallback', windll['computenetwork.dll']), ((1, 'Callback'),(1, 'Context'),(1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnUnregisterServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnUnregisterServiceCallback', windll['computenetwork.dll']), ((1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnRegisterGuestNetworkServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK,c_void_p,POINTER(c_void_p))(('HcnRegisterGuestNetworkServiceCallback', windll['computenetwork.dll']), ((1, 'GuestNetworkService'),(1, 'Callback'),(1, 'Context'),(1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnUnregisterGuestNetworkServiceCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnUnregisterGuestNetworkServiceCallback', windll['computenetwork.dll']), ((1, 'CallbackHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCreateGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(win32more.Foundation.PWSTR))(('HcnCreateGuestNetworkService', windll['computenetwork.dll']), ((1, 'Id'),(1, 'Settings'),(1, 'GuestNetworkService'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnCloseGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('HcnCloseGuestNetworkService', windll['computenetwork.dll']), ((1, 'GuestNetworkService'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnModifyGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcnModifyGuestNetworkService', windll['computenetwork.dll']), ((1, 'GuestNetworkService'),(1, 'Settings'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnDeleteGuestNetworkService():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('HcnDeleteGuestNetworkService', windll['computenetwork.dll']), ((1, 'Id'),(1, 'ErrorRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnReserveGuestNetworkServicePort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.HostComputeNetwork.HCN_PORT_PROTOCOL,win32more.System.HostComputeNetwork.HCN_PORT_ACCESS,UInt16,POINTER(win32more.Foundation.HANDLE))(('HcnReserveGuestNetworkServicePort', windll['computenetwork.dll']), ((1, 'GuestNetworkService'),(1, 'Protocol'),(1, 'Access'),(1, 'Port'),(1, 'PortReservationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnReserveGuestNetworkServicePortRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt16,POINTER(win32more.System.HostComputeNetwork.HCN_PORT_RANGE_RESERVATION_head),POINTER(win32more.Foundation.HANDLE))(('HcnReserveGuestNetworkServicePortRange', windll['computenetwork.dll']), ((1, 'GuestNetworkService'),(1, 'PortCount'),(1, 'PortRangeReservation'),(1, 'PortReservationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnReleaseGuestNetworkServicePortReservationHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('HcnReleaseGuestNetworkServicePortReservationHandle', windll['computenetwork.dll']), ((1, 'PortReservationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnEnumerateGuestNetworkPortReservations():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head)))(('HcnEnumerateGuestNetworkPortReservations', windll['computenetwork.dll']), ((1, 'ReturnCount'),(1, 'PortEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcnFreeGuestNetworkPortReservations():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head))(('HcnFreeGuestNetworkPortReservations', windll['computenetwork.dll']), ((1, 'PortEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HCN_NOTIFICATION_CALLBACK():
    return WINFUNCTYPE(Void,UInt32,c_void_p,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)
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
HCN_PORT_ACCESS = Int32
HCN_PORT_ACCESS_EXCLUSIVE = 1
HCN_PORT_ACCESS_SHARED = 2
HCN_PORT_PROTOCOL = Int32
HCN_PORT_PROTOCOL_TCP = 1
HCN_PORT_PROTOCOL_UDP = 2
HCN_PORT_PROTOCOL_BOTH = 3
def _define_HCN_PORT_RANGE_ENTRY_head():
    class HCN_PORT_RANGE_ENTRY(Structure):
        pass
    return HCN_PORT_RANGE_ENTRY
def _define_HCN_PORT_RANGE_ENTRY():
    HCN_PORT_RANGE_ENTRY = win32more.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY_head
    HCN_PORT_RANGE_ENTRY._fields_ = [
        ('OwningPartitionId', Guid),
        ('TargetPartitionId', Guid),
        ('Protocol', win32more.System.HostComputeNetwork.HCN_PORT_PROTOCOL),
        ('Priority', UInt64),
        ('ReservationType', UInt32),
        ('SharingFlags', UInt32),
        ('DeliveryMode', UInt32),
        ('StartingPort', UInt16),
        ('EndingPort', UInt16),
    ]
    return HCN_PORT_RANGE_ENTRY
def _define_HCN_PORT_RANGE_RESERVATION_head():
    class HCN_PORT_RANGE_RESERVATION(Structure):
        pass
    return HCN_PORT_RANGE_RESERVATION
def _define_HCN_PORT_RANGE_RESERVATION():
    HCN_PORT_RANGE_RESERVATION = win32more.System.HostComputeNetwork.HCN_PORT_RANGE_RESERVATION_head
    HCN_PORT_RANGE_RESERVATION._fields_ = [
        ('startingPort', UInt16),
        ('endingPort', UInt16),
    ]
    return HCN_PORT_RANGE_RESERVATION
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
