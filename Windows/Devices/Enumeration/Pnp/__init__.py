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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Enumeration
import Windows.Devices.Enumeration.Pnp
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPnpObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObject'
    _iid_ = Guid('{95c66258-733b-4a8f-93a3-db078ac870c1}')
    @winrt_commethod(6)
    def get_Type(self: Windows.Devices.Enumeration.Pnp.IPnpObject) -> Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_commethod(7)
    def get_Id(self: Windows.Devices.Enumeration.Pnp.IPnpObject) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Properties(self: Windows.Devices.Enumeration.Pnp.IPnpObject) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(9)
    def Update(self: Windows.Devices.Enumeration.Pnp.IPnpObject, updateInfo: Windows.Devices.Enumeration.Pnp.PnpObjectUpdate) -> Void: ...
    Type = property(get_Type, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class IPnpObjectStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObjectStatics'
    _iid_ = Guid('{b3c32a3d-d168-4660-bbf3-a733b14b6e01}')
    @winrt_commethod(6)
    def CreateFromIdAsync(self: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, id: WinRT_String, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.Pnp.PnpObject]: ...
    @winrt_commethod(7)
    def FindAllAsync(self: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_commethod(8)
    def FindAllAsyncAqsFilter(self: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_commethod(9)
    def CreateWatcher(self: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
    @winrt_commethod(10)
    def CreateWatcherAqsFilter(self: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
class IPnpObjectUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate'
    _iid_ = Guid('{6f59e812-001e-4844-bcc6-432886856a17}')
    @winrt_commethod(6)
    def get_Type(self: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_commethod(7)
    def get_Id(self: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Properties(self: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Type = property(get_Type, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class IPnpObjectWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher'
    _iid_ = Guid('{83c95ca8-4772-4a7a-aca8-e48c42a89c44}')
    @winrt_commethod(6)
    def add_Added(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Devices.Enumeration.Pnp.PnpObject]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Updated(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Updated(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Removed(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Removed(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Void: ...
    @winrt_commethod(18)
    def Stop(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Void: ...
    Status = property(get_Status, None)
class PnpObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Enumeration.Pnp.IPnpObject
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObject'
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Enumeration.Pnp.IPnpObject) -> Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Enumeration.Pnp.IPnpObject) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Enumeration.Pnp.IPnpObject) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Update(self: Windows.Devices.Enumeration.Pnp.IPnpObject, updateInfo: Windows.Devices.Enumeration.Pnp.PnpObjectUpdate) -> Void: ...
    @winrt_classmethod
    def CreateFromIdAsync(cls: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, id: WinRT_String, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.Pnp.PnpObject]: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_classmethod
    def FindAllAsyncAqsFilter(cls: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.Pnp.PnpObjectCollection]: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
    @winrt_classmethod
    def CreateWatcherAqsFilter(cls: Windows.Devices.Enumeration.Pnp.IPnpObjectStatics, type: Windows.Devices.Enumeration.Pnp.PnpObjectType, requestedProperties: Windows.Foundation.Collections.IIterable[WinRT_String], aqsFilter: WinRT_String) -> Windows.Devices.Enumeration.Pnp.PnpObjectWatcher: ...
    Type = property(get_Type, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class PnpObjectCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.Pnp.PnpObject]
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObjectCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.Pnp.PnpObject], index: UInt32) -> Windows.Devices.Enumeration.Pnp.PnpObject: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.Pnp.PnpObject]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.Pnp.PnpObject], value: Windows.Devices.Enumeration.Pnp.PnpObject, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Devices.Enumeration.Pnp.PnpObject], startIndex: UInt32, items: POINTER(Windows.Devices.Enumeration.Pnp.PnpObject)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Devices.Enumeration.Pnp.PnpObject]) -> Windows.Foundation.Collections.IIterator[Windows.Devices.Enumeration.Pnp.PnpObject]: ...
    Size = property(get_Size, None)
PnpObjectType = Int32
PnpObjectType_Unknown: PnpObjectType = 0
PnpObjectType_DeviceInterface: PnpObjectType = 1
PnpObjectType_DeviceContainer: PnpObjectType = 2
PnpObjectType_Device: PnpObjectType = 3
PnpObjectType_DeviceInterfaceClass: PnpObjectType = 4
PnpObjectType_AssociationEndpoint: PnpObjectType = 5
PnpObjectType_AssociationEndpointContainer: PnpObjectType = 6
PnpObjectType_AssociationEndpointService: PnpObjectType = 7
PnpObjectType_DevicePanel: PnpObjectType = 8
class PnpObjectUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObjectUpdate'
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> Windows.Devices.Enumeration.Pnp.PnpObjectType: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Enumeration.Pnp.IPnpObjectUpdate) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Type = property(get_Type, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class PnpObjectWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher
    _classid_ = 'Windows.Devices.Enumeration.Pnp.PnpObjectWatcher'
    @winrt_mixinmethod
    def add_Added(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Devices.Enumeration.Pnp.PnpObject]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Devices.Enumeration.Pnp.PnpObjectUpdate]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Enumeration.Pnp.PnpObjectWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Enumeration.Pnp.IPnpObjectWatcher) -> Void: ...
    Status = property(get_Status, None)
make_head(_module, 'IPnpObject')
make_head(_module, 'IPnpObjectStatics')
make_head(_module, 'IPnpObjectUpdate')
make_head(_module, 'IPnpObjectWatcher')
make_head(_module, 'PnpObject')
make_head(_module, 'PnpObjectCollection')
make_head(_module, 'PnpObjectUpdate')
make_head(_module, 'PnpObjectWatcher')
