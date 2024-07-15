from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Enumeration.Pnp
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IPnpObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObject'
    _iid_ = Guid('{95c66258-733b-4a8f-93a3-db078ac870c1}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(9)
    def Update(self, updateInfo: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectUpdate) -> Void: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
class IPnpObjectStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObjectStatics'
    _iid_ = Guid('{b3c32a3d-d168-4660-bbf3-a733b14b6e01}')
    @winrt_commethod(6)
    def CreateFromIdAsync(self, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, id: WinRT_String, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]: ...
    @winrt_commethod(7)
    def FindAllAsync(self, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_commethod(8)
    def FindAllAsyncAqsFilter(self, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_commethod(9)
    def CreateWatcher(self, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
    @winrt_commethod(10)
    def CreateWatcherAqsFilter(self, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
class IPnpObjectUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate'
    _iid_ = Guid('{6f59e812-001e-4844-bcc6-432886856a17}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
class IPnpObjectWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher'
    _iid_ = Guid('{83c95ca8-4772-4a7a-aca8-e48c42a89c44}')
    @winrt_commethod(6)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Devices.Enumeration.Pnp.PnpObject]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Updated = event()
    Removed = event()
    EnumerationCompleted = event()
    Stopped = event()
class PnpObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.Pnp.IPnpObject
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObject'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObject) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObject) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObject) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Update(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObject, updateInfo: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectUpdate) -> Void: ...
    @winrt_classmethod
    def CreateFromIdAsync(cls: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, id: WinRT_String, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_classmethod
    def FindAllAsyncAqsFilter(cls: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
    @winrt_classmethod
    def CreateWatcherAqsFilter(cls: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
class PnpObjectCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]]
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObjectCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.Pnp.PnpObject], index: UInt32) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObject: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.Pnp.PnpObject], value: win32more.Windows.Devices.Enumeration.Pnp.PnpObject, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Enumeration.Pnp.PnpObject], startIndex: UInt32, items: FillArray[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Devices.Enumeration.Pnp.PnpObject]: ...
    Size = property(get_Size, None)
class PnpObjectType(Enum, Int32):
    Unknown = 0
    DeviceInterface = 1
    DeviceContainer = 2
    Device = 3
    DeviceInterfaceClass = 4
    AssociationEndpoint = 5
    AssociationEndpointContainer = 6
    AssociationEndpointService = 7
    DevicePanel = 8
    AssociationEndpointProtocol = 9
class PnpObjectUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObjectUpdate'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> win32more.Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
class PnpObjectWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObjectWatcher'
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Devices.Enumeration.Pnp.PnpObject]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Updated = event()
    Removed = event()
    EnumerationCompleted = event()
    Stopped = event()


make_ready(__name__)
