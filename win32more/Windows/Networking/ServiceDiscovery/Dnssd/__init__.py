from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Connectivity
import win32more.Windows.Networking.ServiceDiscovery.Dnssd
import win32more.Windows.Networking.Sockets
import win32more.Windows.Win32.System.WinRT
class DnssdRegistrationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationStatus: ...
    @winrt_mixinmethod
    def get_IPAddress(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_HasInstanceNameChanged(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult) -> Boolean: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    HasInstanceNameChanged = property(get_HasInstanceNameChanged, None)
    IPAddress = property(get_IPAddress, None)
    Status = property(get_Status, None)
class DnssdRegistrationStatus(Enum, Int32):
    Success = 0
    InvalidServiceName = 1
    ServerError = 2
    SecurityError = 3
class DnssdServiceInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstanceFactory, dnssdServiceInstanceName: WinRT_String, hostName: win32more.Windows.Networking.HostName, port: UInt16) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance: ...
    @winrt_mixinmethod
    def get_DnssdServiceInstanceName(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DnssdServiceInstanceName(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HostName(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_HostName(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_Port(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> UInt16: ...
    @winrt_mixinmethod
    def put_Port(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> UInt16: ...
    @winrt_mixinmethod
    def put_Priority(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_Weight(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> UInt16: ...
    @winrt_mixinmethod
    def put_Weight(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_TextAttributes(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def RegisterStreamSocketListenerAsync1(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: win32more.Windows.Networking.Sockets.StreamSocketListener) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def RegisterStreamSocketListenerAsync2(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: win32more.Windows.Networking.Sockets.StreamSocketListener, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def RegisterDatagramSocketAsync1(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: win32more.Windows.Networking.Sockets.DatagramSocket) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def RegisterDatagramSocketAsync2(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance, socket: win32more.Windows.Networking.Sockets.DatagramSocket, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    DnssdServiceInstanceName = property(get_DnssdServiceInstanceName, put_DnssdServiceInstanceName)
    HostName = property(get_HostName, put_HostName)
    Port = property(get_Port, put_Port)
    Priority = property(get_Priority, put_Priority)
    TextAttributes = property(get_TextAttributes, None)
    Weight = property(get_Weight, put_Weight)
class DnssdServiceInstanceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]]
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstanceCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance], index: UInt32) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance], value: win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance], startIndex: UInt32, items: FillArray[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]: ...
    Size = property(get_Size, None)
class DnssdServiceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher'
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    EnumerationCompleted = event()
    Stopped = event()
class DnssdServiceWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopping = 3
    Stopped = 4
    Aborted = 5
class IDnssdRegistrationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.IDnssdRegistrationResult'
    _iid_ = Guid('{3d786ad2-e606-5350-73ea-7e97f066162f}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationStatus: ...
    @winrt_commethod(7)
    def get_IPAddress(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def get_HasInstanceNameChanged(self) -> Boolean: ...
    HasInstanceNameChanged = property(get_HasInstanceNameChanged, None)
    IPAddress = property(get_IPAddress, None)
    Status = property(get_Status, None)
class IDnssdServiceInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstance'
    _iid_ = Guid('{e246db7e-98a5-4ca1-b9e4-c253d33c35ff}')
    @winrt_commethod(6)
    def get_DnssdServiceInstanceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DnssdServiceInstanceName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_HostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(9)
    def put_HostName(self, value: win32more.Windows.Networking.HostName) -> Void: ...
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
    def get_TextAttributes(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(17)
    def RegisterStreamSocketListenerAsync1(self, socket: win32more.Windows.Networking.Sockets.StreamSocketListener) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_commethod(18)
    def RegisterStreamSocketListenerAsync2(self, socket: win32more.Windows.Networking.Sockets.StreamSocketListener, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_commethod(19)
    def RegisterDatagramSocketAsync1(self, socket: win32more.Windows.Networking.Sockets.DatagramSocket) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    @winrt_commethod(20)
    def RegisterDatagramSocketAsync2(self, socket: win32more.Windows.Networking.Sockets.DatagramSocket, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationResult]: ...
    DnssdServiceInstanceName = property(get_DnssdServiceInstanceName, put_DnssdServiceInstanceName)
    HostName = property(get_HostName, put_HostName)
    Port = property(get_Port, put_Port)
    Priority = property(get_Priority, put_Priority)
    TextAttributes = property(get_TextAttributes, None)
    Weight = property(get_Weight, put_Weight)
class IDnssdServiceInstanceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceInstanceFactory'
    _iid_ = Guid('{6cb061a1-c478-4331-9684-4af2186c0a2b}')
    @winrt_commethod(6)
    def Create(self, dnssdServiceInstanceName: WinRT_String, hostName: win32more.Windows.Networking.HostName, port: UInt16) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance: ...
class IDnssdServiceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.ServiceDiscovery.Dnssd.IDnssdServiceWatcher'
    _iid_ = Guid('{cc34d9c1-db7d-4b69-983d-c6f83f205682}')
    @winrt_commethod(6)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceInstance]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Status(self) -> win32more.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcherStatus: ...
    @winrt_commethod(13)
    def Start(self) -> Void: ...
    @winrt_commethod(14)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    EnumerationCompleted = event()
    Stopped = event()


make_ready(__name__)
