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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Connectivity
import Windows.Networking.ServiceDiscovery.Dnssd
import Windows.Networking.Sockets
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DnssdRegistrationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationStatus: ...
    @winrt_mixinmethod
    def get_IPAddress(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_HasInstanceNameChanged(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult) -> Boolean: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Status = property(get_Status, None)
    IPAddress = property(get_IPAddress, None)
    HasInstanceNameChanged = property(get_HasInstanceNameChanged, None)
DnssdRegistrationStatus = Int32
DnssdRegistrationStatus_Success: DnssdRegistrationStatus = 0
DnssdRegistrationStatus_InvalidServiceName: DnssdRegistrationStatus = 1
DnssdRegistrationStatus_ServerError: DnssdRegistrationStatus = 2
DnssdRegistrationStatus_SecurityError: DnssdRegistrationStatus = 3
class DnssdServiceInstance(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance'
    @winrt_factorymethod
    def Create(cls: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstanceFactory, dnssdServiceInstanceName: WinRT_String, hostName: Windows.Networking.HostName, port: UInt16) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance: ...
    @winrt_mixinmethod
    def get_DnssdServiceInstanceName(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DnssdServiceInstanceName(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HostName(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_HostName(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_Port(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> UInt16: ...
    @winrt_mixinmethod
    def put_Port(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_Priority(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> UInt16: ...
    @winrt_mixinmethod
    def put_Priority(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_Weight(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> UInt16: ...
    @winrt_mixinmethod
    def put_Weight(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_TextAttributes(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def RegisterStreamSocketListenerAsync1(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: Windows.Networking.Sockets.StreamSocketListener) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def RegisterStreamSocketListenerAsync2(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: Windows.Networking.Sockets.StreamSocketListener, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def RegisterDatagramSocketAsync1(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: Windows.Networking.Sockets.DatagramSocket) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def RegisterDatagramSocketAsync2(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: Windows.Networking.Sockets.DatagramSocket, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    DnssdServiceInstanceName = property(get_DnssdServiceInstanceName, put_DnssdServiceInstanceName)
    HostName = property(get_HostName, put_HostName)
    Port = property(get_Port, put_Port)
    Priority = property(get_Priority, put_Priority)
    Weight = property(get_Weight, put_Weight)
    TextAttributes = property(get_TextAttributes, None)
class DnssdServiceInstanceCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstanceCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance], index: UInt32) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance], value: Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance], startIndex: UInt32, items: POINTER(Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> Windows.Foundation.Collections.IIterator[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]: ...
    Size = property(get_Size, None)
class DnssdServiceWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher'
    @winrt_mixinmethod
    def add_Added(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher) -> Void: ...
    Status = property(get_Status, None)
DnssdServiceWatcherStatus = Int32
DnssdServiceWatcherStatus_Created: DnssdServiceWatcherStatus = 0
DnssdServiceWatcherStatus_Started: DnssdServiceWatcherStatus = 1
DnssdServiceWatcherStatus_EnumerationCompleted: DnssdServiceWatcherStatus = 2
DnssdServiceWatcherStatus_Stopping: DnssdServiceWatcherStatus = 3
DnssdServiceWatcherStatus_Stopped: DnssdServiceWatcherStatus = 4
DnssdServiceWatcherStatus_Aborted: DnssdServiceWatcherStatus = 5
class IDnssdRegistrationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d786ad2-e606-5350-73-ea-7e-97-f0-66-16-2f')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationStatus: ...
    @winrt_commethod(7)
    def get_IPAddress(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def get_HasInstanceNameChanged(self) -> Boolean: ...
    Status = property(get_Status, None)
    IPAddress = property(get_IPAddress, None)
    HasInstanceNameChanged = property(get_HasInstanceNameChanged, None)
class IDnssdServiceInstance(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e246db7e-98a5-4ca1-b9-e4-c2-53-d3-3c-35-ff')
    @winrt_commethod(6)
    def get_DnssdServiceInstanceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DnssdServiceInstanceName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_HostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def put_HostName(self, value: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(10)
    def get_Port(self) -> UInt16: ...
    @winrt_commethod(11)
    def put_Port(self, value: UInt16) -> Void: ...
    @winrt_commethod(12)
    def get_Priority(self) -> UInt16: ...
    @winrt_commethod(13)
    def put_Priority(self, value: UInt16) -> Void: ...
    @winrt_commethod(14)
    def get_Weight(self) -> UInt16: ...
    @winrt_commethod(15)
    def put_Weight(self, value: UInt16) -> Void: ...
    @winrt_commethod(16)
    def get_TextAttributes(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(17)
    def RegisterStreamSocketListenerAsync1(self, socket: Windows.Networking.Sockets.StreamSocketListener) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_commethod(18)
    def RegisterStreamSocketListenerAsync2(self, socket: Windows.Networking.Sockets.StreamSocketListener, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_commethod(19)
    def RegisterDatagramSocketAsync1(self, socket: Windows.Networking.Sockets.DatagramSocket) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_commethod(20)
    def RegisterDatagramSocketAsync2(self, socket: Windows.Networking.Sockets.DatagramSocket, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Foundation.IAsyncOperation[Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    DnssdServiceInstanceName = property(get_DnssdServiceInstanceName, put_DnssdServiceInstanceName)
    HostName = property(get_HostName, put_HostName)
    Port = property(get_Port, put_Port)
    Priority = property(get_Priority, put_Priority)
    Weight = property(get_Weight, put_Weight)
    TextAttributes = property(get_TextAttributes, None)
class IDnssdServiceInstanceFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6cb061a1-c478-4331-96-84-4a-f2-18-6c-0a-2b')
    @winrt_commethod(6)
    def Create(self, dnssdServiceInstanceName: WinRT_String, hostName: Windows.Networking.HostName, port: UInt16) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance: ...
class IDnssdServiceWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cc34d9c1-db7d-4b69-98-3d-c6-f8-3f-20-56-82')
    @winrt_commethod(6)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Status(self) -> Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcherStatus: ...
    @winrt_commethod(13)
    def Start(self) -> Void: ...
    @winrt_commethod(14)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
make_head(_module, 'DnssdRegistrationResult')
make_head(_module, 'DnssdServiceInstance')
make_head(_module, 'DnssdServiceInstanceCollection')
make_head(_module, 'DnssdServiceWatcher')
make_head(_module, 'IDnssdRegistrationResult')
make_head(_module, 'IDnssdServiceInstance')
make_head(_module, 'IDnssdServiceInstanceFactory')
make_head(_module, 'IDnssdServiceWatcher')
