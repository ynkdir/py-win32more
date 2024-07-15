from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Networking
import win32more.Windows.Networking.Connectivity
import win32more.Windows.Win32.System.WinRT
class DomainNameType(Enum, Int32):
    Suffix = 0
    FullyQualified = 1
class EndpointPair(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.IEndpointPair
    _classid_ = 'Windows.Networking.EndpointPair'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Networking.EndpointPair.CreateEndpointPair(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateEndpointPair(cls: win32more.Windows.Networking.IEndpointPairFactory, localHostName: win32more.Windows.Networking.HostName, localServiceName: WinRT_String, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Networking.EndpointPair: ...
    @winrt_mixinmethod
    def get_LocalHostName(self: win32more.Windows.Networking.IEndpointPair) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_LocalHostName(self: win32more.Windows.Networking.IEndpointPair, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_LocalServiceName(self: win32more.Windows.Networking.IEndpointPair) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocalServiceName(self: win32more.Windows.Networking.IEndpointPair, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: win32more.Windows.Networking.IEndpointPair) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_RemoteHostName(self: win32more.Windows.Networking.IEndpointPair, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteServiceName(self: win32more.Windows.Networking.IEndpointPair) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteServiceName(self: win32more.Windows.Networking.IEndpointPair, value: WinRT_String) -> Void: ...
    LocalHostName = property(get_LocalHostName, put_LocalHostName)
    LocalServiceName = property(get_LocalServiceName, put_LocalServiceName)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
    RemoteServiceName = property(get_RemoteServiceName, put_RemoteServiceName)
class HostName(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.IHostName
    _classid_ = 'Windows.Networking.HostName'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.HostName.CreateHostName(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateHostName(cls: win32more.Windows.Networking.IHostNameFactory, hostName: WinRT_String) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_IPInformation(self: win32more.Windows.Networking.IHostName) -> win32more.Windows.Networking.Connectivity.IPInformation: ...
    @winrt_mixinmethod
    def get_RawName(self: win32more.Windows.Networking.IHostName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Networking.IHostName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanonicalName(self: win32more.Windows.Networking.IHostName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Networking.IHostName) -> win32more.Windows.Networking.HostNameType: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Networking.IHostName, hostName: win32more.Windows.Networking.HostName) -> Boolean: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def Compare(cls: win32more.Windows.Networking.IHostNameStatics, value1: WinRT_String, value2: WinRT_String) -> Int32: ...
    CanonicalName = property(get_CanonicalName, None)
    DisplayName = property(get_DisplayName, None)
    IPInformation = property(get_IPInformation, None)
    RawName = property(get_RawName, None)
    Type = property(get_Type, None)
class HostNameSortOptions(Enum, UInt32):
    None_ = 0
    OptimizeForLongConnections = 2
class HostNameType(Enum, Int32):
    DomainName = 0
    Ipv4 = 1
    Ipv6 = 2
    Bluetooth = 3
class IEndpointPair(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.IEndpointPair'
    _iid_ = Guid('{33a0aa36-f8fa-4b30-b856-76517c3bd06d}')
    @winrt_commethod(6)
    def get_LocalHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def put_LocalHostName(self, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(8)
    def get_LocalServiceName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_LocalServiceName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RemoteHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(11)
    def put_RemoteHostName(self, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(12)
    def get_RemoteServiceName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_RemoteServiceName(self, value: WinRT_String) -> Void: ...
    LocalHostName = property(get_LocalHostName, put_LocalHostName)
    LocalServiceName = property(get_LocalServiceName, put_LocalServiceName)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
    RemoteServiceName = property(get_RemoteServiceName, put_RemoteServiceName)
class IEndpointPairFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.IEndpointPairFactory'
    _iid_ = Guid('{b609d971-64e0-442b-aa6f-cc8c8f181f78}')
    @winrt_commethod(6)
    def CreateEndpointPair(self, localHostName: win32more.Windows.Networking.HostName, localServiceName: WinRT_String, remoteHostName: win32more.Windows.Networking.HostName, remoteServiceName: WinRT_String) -> win32more.Windows.Networking.EndpointPair: ...
class IHostName(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.IHostName'
    _iid_ = Guid('{bf8ecaad-ed96-49a7-9084-d416cae88dcb}')
    @winrt_commethod(6)
    def get_IPInformation(self) -> win32more.Windows.Networking.Connectivity.IPInformation: ...
    @winrt_commethod(7)
    def get_RawName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CanonicalName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Type(self) -> win32more.Windows.Networking.HostNameType: ...
    @winrt_commethod(11)
    def IsEqual(self, hostName: win32more.Windows.Networking.HostName) -> Boolean: ...
    CanonicalName = property(get_CanonicalName, None)
    DisplayName = property(get_DisplayName, None)
    IPInformation = property(get_IPInformation, None)
    RawName = property(get_RawName, None)
    Type = property(get_Type, None)
class IHostNameFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.IHostNameFactory'
    _iid_ = Guid('{458c23ed-712f-4576-adf1-c20b2c643558}')
    @winrt_commethod(6)
    def CreateHostName(self, hostName: WinRT_String) -> win32more.Windows.Networking.HostName: ...
class IHostNameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.IHostNameStatics'
    _iid_ = Guid('{f68cd4bf-a388-4e8b-91ea-54dd6dd901c0}')
    @winrt_commethod(6)
    def Compare(self, value1: WinRT_String, value2: WinRT_String) -> Int32: ...


make_ready(__name__)
