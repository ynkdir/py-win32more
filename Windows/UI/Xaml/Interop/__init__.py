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
import Windows.UI.Xaml.Interop
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BindableVectorChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('624cd4e1-d007-43b1-9c-03-af-4d-3e-62-58-c4')
    ClassId = 'Windows.UI.Xaml.Interop.BindableVectorChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, vector: Windows.UI.Xaml.Interop.IBindableObservableVector, e: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class IBindableIterable(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('036d2c08-df29-41af-8a-a2-d7-74-be-62-ba-6f')
    @winrt_commethod(6)
    def First(self) -> Windows.UI.Xaml.Interop.IBindableIterator: ...
class IBindableIterator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6a1d6c07-076d-49f2-83-14-f5-2c-9c-9a-83-31')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_HasCurrent(self) -> Boolean: ...
    @winrt_commethod(8)
    def MoveNext(self) -> Boolean: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class IBindableObservableVector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe1eb536-7e7f-4f90-ac-9a-47-49-84-aa-e5-12')
    @winrt_commethod(6)
    def add_VectorChanged(self, handler: Windows.UI.Xaml.Interop.BindableVectorChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VectorChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IBindableVector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('393de7de-6fd0-4c0d-bb-71-47-24-4a-11-3e-93')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetView(self) -> Windows.UI.Xaml.Interop.IBindableVectorView: ...
    @winrt_commethod(9)
    def IndexOf(self, value: Windows.Win32.System.WinRT.IInspectable_head, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_commethod(10)
    def SetAt(self, index: UInt32, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(11)
    def InsertAt(self, index: UInt32, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(12)
    def RemoveAt(self, index: UInt32) -> Void: ...
    @winrt_commethod(13)
    def Append(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(14)
    def RemoveAtEnd(self) -> Void: ...
    @winrt_commethod(15)
    def Clear(self) -> Void: ...
    Size = property(get_Size, None)
class IBindableVectorView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('346dd6e7-976e-4bc3-81-5d-ec-e2-43-bc-0f-33')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def IndexOf(self, value: Windows.Win32.System.WinRT.IInspectable_head, index: POINTER(UInt32)) -> Boolean: ...
    Size = property(get_Size, None)
class INotifyCollectionChanged(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('28b167d5-1a31-465b-9b-25-d5-c3-ae-68-6c-40')
    @winrt_commethod(6)
    def add_CollectionChanged(self, handler: Windows.UI.Xaml.Interop.NotifyCollectionChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CollectionChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class INotifyCollectionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4cf68d33-e3f2-4964-b8-5e-94-5b-4f-7e-2f-21')
    @winrt_commethod(6)
    def get_Action(self) -> Windows.UI.Xaml.Interop.NotifyCollectionChangedAction: ...
    @winrt_commethod(7)
    def get_NewItems(self) -> Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(8)
    def get_OldItems(self) -> Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(9)
    def get_NewStartingIndex(self) -> Int32: ...
    @winrt_commethod(10)
    def get_OldStartingIndex(self) -> Int32: ...
    Action = property(get_Action, None)
    NewItems = property(get_NewItems, None)
    OldItems = property(get_OldItems, None)
    NewStartingIndex = property(get_NewStartingIndex, None)
    OldStartingIndex = property(get_OldStartingIndex, None)
class INotifyCollectionChangedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b30c3e3a-df8d-44a5-9a-38-7a-c0-d0-8c-e6-3d')
    @winrt_commethod(6)
    def CreateInstanceWithAllParameters(self, action: Windows.UI.Xaml.Interop.NotifyCollectionChangedAction, newItems: Windows.UI.Xaml.Interop.IBindableVector, oldItems: Windows.UI.Xaml.Interop.IBindableVector, newIndex: Int32, oldIndex: Int32, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs: ...
NotifyCollectionChangedAction = Int32
NotifyCollectionChangedAction_Add: NotifyCollectionChangedAction = 0
NotifyCollectionChangedAction_Remove: NotifyCollectionChangedAction = 1
NotifyCollectionChangedAction_Replace: NotifyCollectionChangedAction = 2
NotifyCollectionChangedAction_Move: NotifyCollectionChangedAction = 3
NotifyCollectionChangedAction_Reset: NotifyCollectionChangedAction = 4
class NotifyCollectionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_commethod(6)
    def get_Action(self) -> Windows.UI.Xaml.Interop.NotifyCollectionChangedAction: ...
    @winrt_commethod(7)
    def get_NewItems(self) -> Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(8)
    def get_OldItems(self) -> Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(9)
    def get_NewStartingIndex(self) -> Int32: ...
    @winrt_commethod(10)
    def get_OldStartingIndex(self) -> Int32: ...
    Action = property(get_Action, None)
    NewItems = property(get_NewItems, None)
    OldItems = property(get_OldItems, None)
    NewStartingIndex = property(get_NewStartingIndex, None)
    OldStartingIndex = property(get_OldStartingIndex, None)
class NotifyCollectionChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ca10b37c-f382-4591-85-57-5e-24-96-52-79-b0')
    ClassId = 'Windows.UI.Xaml.Interop.NotifyCollectionChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs) -> Void: ...
TypeKind = Int32
TypeKind_Primitive: TypeKind = 0
TypeKind_Metadata: TypeKind = 1
TypeKind_Custom: TypeKind = 2
class TypeName(EasyCastStructure):
    Name: WinRT_String
    Kind: Windows.UI.Xaml.Interop.TypeKind
make_head(_module, 'BindableVectorChangedEventHandler')
make_head(_module, 'IBindableIterable')
make_head(_module, 'IBindableIterator')
make_head(_module, 'IBindableObservableVector')
make_head(_module, 'IBindableVector')
make_head(_module, 'IBindableVectorView')
make_head(_module, 'INotifyCollectionChanged')
make_head(_module, 'INotifyCollectionChangedEventArgs')
make_head(_module, 'INotifyCollectionChangedEventArgsFactory')
make_head(_module, 'NotifyCollectionChangedEventArgs')
make_head(_module, 'NotifyCollectionChangedEventHandler')
make_head(_module, 'TypeName')
