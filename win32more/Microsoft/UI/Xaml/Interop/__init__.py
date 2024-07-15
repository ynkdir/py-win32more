from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Xaml.Interop
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class BindableVectorChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{624cd4e1-d007-43b1-9c03-af4d3e6258c4}')
    @winrt_commethod(3)
    def Invoke(self, vector: win32more.Microsoft.UI.Xaml.Interop.IBindableObservableVector, e: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IBindableIterable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Interop.IBindableIterable'
    _iid_ = Guid('{036d2c08-df29-41af-8aa2-d774be62ba6f}')
    @winrt_commethod(6)
    def First(self) -> win32more.Microsoft.UI.Xaml.Interop.IBindableIterator: ...
class IBindableIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Interop.IBindableIterator'
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
    _classid_ = 'Microsoft.UI.Xaml.Interop.IBindableObservableVector'
    _iid_ = Guid('{fe1eb536-7e7f-4f90-ac9a-474984aae512}')
    @winrt_commethod(6)
    def add_VectorChanged(self, handler: win32more.Microsoft.UI.Xaml.Interop.BindableVectorChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VectorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    VectorChanged = event()
class IBindableVector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Interop.IBindableVector'
    _iid_ = Guid('{393de7de-6fd0-4c0d-bb71-47244a113e93}')
    @winrt_commethod(6)
    def GetAt(self, index: UInt32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetView(self) -> win32more.Microsoft.UI.Xaml.Interop.IBindableVectorView: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Interop.IBindableVectorView'
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
    _classid_ = 'Microsoft.UI.Xaml.Interop.INotifyCollectionChanged'
    _iid_ = Guid('{530155e1-28a5-5693-87ce-30724d95a06d}')
    @winrt_commethod(6)
    def add_CollectionChanged(self, handler: win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CollectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CollectionChanged = event()
class INotifyCollectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs'
    _iid_ = Guid('{da049ff2-d2e0-5fe8-8c7b-f87f26060b6f}')
    @winrt_commethod(6)
    def get_Action(self) -> win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedAction: ...
    @winrt_commethod(7)
    def get_NewItems(self) -> win32more.Microsoft.UI.Xaml.Interop.IBindableVector: ...
    @winrt_commethod(8)
    def get_OldItems(self) -> win32more.Microsoft.UI.Xaml.Interop.IBindableVector: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgsFactory'
    _iid_ = Guid('{5108eba4-4892-5a20-8374-a96815e0fd27}')
    @winrt_commethod(6)
    def CreateInstanceWithAllParameters(self, action: win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedAction, newItems: win32more.Microsoft.UI.Xaml.Interop.IBindableVector, oldItems: win32more.Microsoft.UI.Xaml.Interop.IBindableVector, newIndex: Int32, oldIndex: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedEventArgs: ...
class NotifyCollectionChangedAction(Enum, Int32):
    Add = 0
    Remove = 1
    Replace = 2
    Move = 3
    Reset = 4
class NotifyCollectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Interop.NotifyCollectionChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 5:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedEventArgs.CreateInstanceWithAllParameters(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithAllParameters(cls: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgsFactory, action: win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedAction, newItems: win32more.Microsoft.UI.Xaml.Interop.IBindableVector, oldItems: win32more.Microsoft.UI.Xaml.Interop.IBindableVector, newIndex: Int32, oldIndex: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedAction: ...
    @winrt_mixinmethod
    def get_NewItems(self: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> win32more.Microsoft.UI.Xaml.Interop.IBindableVector: ...
    @winrt_mixinmethod
    def get_OldItems(self: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> win32more.Microsoft.UI.Xaml.Interop.IBindableVector: ...
    @winrt_mixinmethod
    def get_NewStartingIndex(self: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_OldStartingIndex(self: win32more.Microsoft.UI.Xaml.Interop.INotifyCollectionChangedEventArgs) -> Int32: ...
    Action = property(get_Action, None)
    NewItems = property(get_NewItems, None)
    NewStartingIndex = property(get_NewStartingIndex, None)
    OldItems = property(get_OldItems, None)
    OldStartingIndex = property(get_OldStartingIndex, None)
class NotifyCollectionChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8b0909dc-2005-5d93-bf8a-725f017baa8d}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Interop.NotifyCollectionChangedEventArgs) -> Void: ...


make_ready(__name__)
