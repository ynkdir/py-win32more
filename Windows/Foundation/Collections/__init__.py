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
CollectionChange = Int32
CollectionChange_Reset: CollectionChange = 0
CollectionChange_ItemInserted: CollectionChange = 1
CollectionChange_ItemRemoved: CollectionChange = 2
CollectionChange_ItemChanged: CollectionChange = 3
class IIterable(Generic[T], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{faa585ea-6214-4217-afda-7f46de5869b3}')
    @winrt_commethod(6)
    def First(self) -> Windows.Foundation.Collections.IIterator[T]: ...
class IIterator(Generic[T], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6a79e863-4300-459a-9966-cbb660963ee1}')
    @winrt_commethod(6)
    def get_Current(self) -> T: ...
    @winrt_commethod(7)
    def get_HasCurrent(self) -> Boolean: ...
    @winrt_commethod(8)
    def MoveNext(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetMany(self, items: POINTER(T)) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class IKeyValuePair(Generic[K, V], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{02b51929-c1c4-4a7e-8940-0312b5c18500}')
    @winrt_commethod(6)
    def get_Key(self) -> K: ...
    @winrt_commethod(7)
    def get_Value(self) -> V: ...
    Key = property(get_Key, None)
    Value = property(get_Value, None)
class IMapChangedEventArgs(Generic[K], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9939f4df-050a-4c0f-aa60-77075f9c4777}')
    @winrt_commethod(6)
    def get_CollectionChange(self) -> Windows.Foundation.Collections.CollectionChange: ...
    @winrt_commethod(7)
    def get_Key(self) -> K: ...
    CollectionChange = property(get_CollectionChange, None)
    Key = property(get_Key, None)
class IMapView(Generic[K, V], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e480ce40-a338-4ada-adcf-272272e48cb9}')
    @winrt_commethod(6)
    def Lookup(self, key: K) -> V: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def HasKey(self, key: K) -> Boolean: ...
    @winrt_commethod(9)
    def Split(self, first: POINTER(Windows.Foundation.Collections.IMapView[K, V]), second: POINTER(Windows.Foundation.Collections.IMapView[K, V])) -> Void: ...
    Size = property(get_Size, None)
class IMap(Generic[K, V], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3c2925fe-8519-45c1-aa79-197b6718c1c1}')
    @winrt_commethod(6)
    def Lookup(self, key: K) -> V: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def HasKey(self, key: K) -> Boolean: ...
    @winrt_commethod(9)
    def GetView(self) -> Windows.Foundation.Collections.IMapView[K, V]: ...
    @winrt_commethod(10)
    def Insert(self, key: K, value: V) -> Boolean: ...
    @winrt_commethod(11)
    def Remove(self, key: K) -> Void: ...
    @winrt_commethod(12)
    def Clear(self) -> Void: ...
    Size = property(get_Size, None)
class IObservableMap(Generic[K, V], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{65df2bf5-bf39-41b5-aebc-5a9d865e472b}')
    @winrt_commethod(6)
    def add_MapChanged(self, vhnd: Windows.Foundation.Collections.MapChangedEventHandler[K, V]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MapChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IObservableVector(Generic[T], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5917eb53-50b4-4a0d-b309-65862b3f1dbc}')
    @winrt_commethod(6)
    def add_VectorChanged(self, vhnd: Windows.Foundation.Collections.VectorChangedEventHandler[T]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VectorChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8a43ed9f-f4e6-4421-acf9-1dab2986820c}')
class IVectorChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{575933df-34fe-4480-af15-07691f3d5d9b}')
    @winrt_commethod(6)
    def get_CollectionChange(self) -> Windows.Foundation.Collections.CollectionChange: ...
    @winrt_commethod(7)
    def get_Index(self) -> UInt32: ...
    CollectionChange = property(get_CollectionChange, None)
    Index = property(get_Index, None)
class IVectorView(Generic[T], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bbe1fa4c-b0e3-4583-baef-1f1b2e483e56}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> T: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_commethod(9)
    def GetMany(self, startIndex: UInt32, items: POINTER(T)) -> UInt32: ...
    Size = property(get_Size, None)
class IVector(Generic[T], ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{913337e9-11a1-4345-a3a2-4e7f956e222d}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> T: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetView(self) -> Windows.Foundation.Collections.IVectorView[T]: ...
    @winrt_commethod(9)
    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_commethod(10)
    def SetAt(self, index: UInt32, value: T) -> Void: ...
    @winrt_commethod(11)
    def InsertAt(self, index: UInt32, value: T) -> Void: ...
    @winrt_commethod(12)
    def RemoveAt(self, index: UInt32) -> Void: ...
    @winrt_commethod(13)
    def Append(self, value: T) -> Void: ...
    @winrt_commethod(14)
    def RemoveAtEnd(self) -> Void: ...
    @winrt_commethod(15)
    def Clear(self) -> Void: ...
    @winrt_commethod(16)
    def GetMany(self, startIndex: UInt32, items: POINTER(T)) -> UInt32: ...
    @winrt_commethod(17)
    def ReplaceAll(self, items: POINTER(T)) -> Void: ...
    Size = property(get_Size, None)
class MapChangedEventHandler(Generic[K, V], ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{179517f3-94ee-41f8-bddc-768a895544f3}')
    _classid_ = 'Windows.Foundation.Collections.MapChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Foundation.Collections.IObservableMap[K, V], event: Windows.Foundation.Collections.IMapChangedEventArgs[K]) -> Void: ...
class PropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Foundation.Collections.PropertySet'
    @winrt_activatemethod
    def New(cls) -> Windows.Foundation.Collections.PropertySet: ...
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
class StringMap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]
    _classid_ = 'Windows.Foundation.Collections.StringMap'
    @winrt_activatemethod
    def New(cls) -> Windows.Foundation.Collections.StringMap: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String, value: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, WinRT_String]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Size = property(get_Size, None)
class ValueSet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Foundation.Collections.ValueSet'
    @winrt_activatemethod
    def New(cls) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
class VectorChangedEventHandler(Generic[T], ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c051752-9fbf-4c70-aa0c-0e4c82d9a761}')
    _classid_ = 'Windows.Foundation.Collections.VectorChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Foundation.Collections.IObservableVector[T], event: Windows.Foundation.Collections.IVectorChangedEventArgs) -> Void: ...
make_head(_module, 'IIterable')
make_head(_module, 'IIterator')
make_head(_module, 'IKeyValuePair')
make_head(_module, 'IMapChangedEventArgs')
make_head(_module, 'IMapView')
make_head(_module, 'IMap')
make_head(_module, 'IObservableMap')
make_head(_module, 'IObservableVector')
make_head(_module, 'IPropertySet')
make_head(_module, 'IVectorChangedEventArgs')
make_head(_module, 'IVectorView')
make_head(_module, 'IVector')
make_head(_module, 'MapChangedEventHandler')
make_head(_module, 'PropertySet')
make_head(_module, 'StringMap')
make_head(_module, 'ValueSet')
make_head(_module, 'VectorChangedEventHandler')
