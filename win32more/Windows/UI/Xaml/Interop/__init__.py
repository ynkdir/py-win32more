from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class BindableVectorChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{624cd4e1-d007-43b1-9c03-af4d3e6258c4}')
    @winrt_commethod(3)
    def Invoke(self, vector: win32more.Windows.UI.Xaml.Interop.IBindableObservableVector, e: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IBindableIterable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.IBindableIterable'
    _iid_ = Guid('{036d2c08-df29-41af-8aa2-d774be62ba6f}')
    @winrt_commethod(6)
    def First(self) -> win32more.Windows.UI.Xaml.Interop.IBindableIterator: ...
class IBindableIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.IBindableIterator'
    _iid_ = Guid('{6a1d6c07-076d-49f2-8314-f52c9c9a8331}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_HasCurrent(self) -> Boolean: ...
    @winrt_commethod(8)
    def MoveNext(self) -> Boolean: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class IBindableObservableVector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.IBindableObservableVector'
    _iid_ = Guid('{fe1eb536-7e7f-4f90-ac9a-474984aae512}')
    @winrt_commethod(6)
    def add_VectorChanged(self, handler: win32more.Windows.UI.Xaml.Interop.BindableVectorChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VectorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    VectorChanged = event()
class IBindableVector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.IBindableVector'
    _iid_ = Guid('{393de7de-6fd0-4c0d-bb71-47244a113e93}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetView(self) -> win32more.Windows.UI.Xaml.Interop.IBindableVectorView: ...
    @winrt_commethod(9)
    def IndexOf(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_commethod(10)
    def SetAt(self, index: UInt32, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(11)
    def InsertAt(self, index: UInt32, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(12)
    def RemoveAt(self, index: UInt32) -> Void: ...
    @winrt_commethod(13)
    def Append(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(14)
    def RemoveAtEnd(self) -> Void: ...
    @winrt_commethod(15)
    def Clear(self) -> Void: ...
    Size = property(get_Size, None)
class IBindableVectorView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.IBindableVectorView'
    _iid_ = Guid('{346dd6e7-976e-4bc3-815d-ece243bc0f33}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def IndexOf(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, index: POINTER(UInt32)) -> Boolean: ...
    Size = property(get_Size, None)
class INotifyCollectionChanged(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.INotifyCollectionChanged'
    _iid_ = Guid('{28b167d5-1a31-465b-9b25-d5c3ae686c40}')
    @winrt_commethod(6)
    def add_CollectionChanged(self, handler: win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CollectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CollectionChanged = event()
class INotifyCollectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs'
    _iid_ = Guid('{4cf68d33-e3f2-4964-b85e-945b4f7e2f21}')
    @winrt_commethod(6)
    def get_Action(self) -> win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedAction: ...
    @winrt_commethod(7)
    def get_NewItems(self) -> win32more.Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(8)
    def get_OldItems(self) -> win32more.Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(9)
    def get_NewStartingIndex(self) -> Int32: ...
    @winrt_commethod(10)
    def get_OldStartingIndex(self) -> Int32: ...
    Action = property(get_Action, None)
    NewItems = property(get_NewItems, None)
    NewStartingIndex = property(get_NewStartingIndex, None)
    OldItems = property(get_OldItems, None)
    OldStartingIndex = property(get_OldStartingIndex, None)
class INotifyCollectionChangedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgsFactory'
    _iid_ = Guid('{b30c3e3a-df8d-44a5-9a38-7ac0d08ce63d}')
    @winrt_commethod(6)
    def CreateInstanceWithAllParameters(self, action: win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedAction, newItems: win32more.Windows.UI.Xaml.Interop.IBindableVector, oldItems: win32more.Windows.UI.Xaml.Interop.IBindableVector, newIndex: Int32, oldIndex: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs: ...
class NotifyCollectionChangedAction(Enum, Int32):
    Add = 0
    Remove = 1
    Replace = 2
    Move = 3
    Reset = 4
class NotifyCollectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs.CreateInstanceWithAllParameters(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithAllParameters(cls: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgsFactory, action: win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedAction, newItems: win32more.Windows.UI.Xaml.Interop.IBindableVector, oldItems: win32more.Windows.UI.Xaml.Interop.IBindableVector, newIndex: Int32, oldIndex: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedAction: ...
    @winrt_mixinmethod
    def get_NewItems(self: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> win32more.Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_mixinmethod
    def get_OldItems(self: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> win32more.Windows.UI.Xaml.Interop.IBindableVector: ...
    @winrt_mixinmethod
    def get_NewStartingIndex(self: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_OldStartingIndex(self: win32more.Windows.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> Int32: ...
    Action = property(get_Action, None)
    NewItems = property(get_NewItems, None)
    NewStartingIndex = property(get_NewStartingIndex, None)
    OldItems = property(get_OldItems, None)
    OldStartingIndex = property(get_OldStartingIndex, None)
class NotifyCollectionChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca10b37c-f382-4591-8557-5e24965279b0}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Interop.NotifyCollectionChangedEventArgs) -> Void: ...
class TypeKind(Enum, Int32):
    Primitive = 0
    Metadata = 1
    Custom = 2
class TypeName(Structure):
    Name: WinRT_String
    Kind: win32more.Windows.UI.Xaml.Interop.TypeKind


make_ready(__name__)
