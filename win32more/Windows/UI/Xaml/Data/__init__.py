from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Data
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class Binding(ComPtr):
    extends: win32more.Windows.UI.Xaml.Data.BindingBase
    default_interface: win32more.Windows.UI.Xaml.Data.IBinding
    _classid_ = 'Windows.UI.Xaml.Data.Binding'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.Binding.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Data.IBindingFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.Binding: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.UI.Xaml.Data.IBinding) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.UI.Xaml.Data.IBinding, value: win32more.Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Xaml.Data.IBinding) -> win32more.Windows.UI.Xaml.Data.BindingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.UI.Xaml.Data.IBinding, value: win32more.Windows.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Xaml.Data.IBinding) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.UI.Xaml.Data.IBinding, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeSource(self: win32more.Windows.UI.Xaml.Data.IBinding) -> win32more.Windows.UI.Xaml.Data.RelativeSource: ...
    @winrt_mixinmethod
    def put_RelativeSource(self: win32more.Windows.UI.Xaml.Data.IBinding, value: win32more.Windows.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_mixinmethod
    def get_ElementName(self: win32more.Windows.UI.Xaml.Data.IBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ElementName(self: win32more.Windows.UI.Xaml.Data.IBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Converter(self: win32more.Windows.UI.Xaml.Data.IBinding) -> win32more.Windows.UI.Xaml.Data.IValueConverter: ...
    @winrt_mixinmethod
    def put_Converter(self: win32more.Windows.UI.Xaml.Data.IBinding, value: win32more.Windows.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_mixinmethod
    def get_ConverterParameter(self: win32more.Windows.UI.Xaml.Data.IBinding) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ConverterParameter(self: win32more.Windows.UI.Xaml.Data.IBinding, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_ConverterLanguage(self: win32more.Windows.UI.Xaml.Data.IBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ConverterLanguage(self: win32more.Windows.UI.Xaml.Data.IBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackValue(self: win32more.Windows.UI.Xaml.Data.IBinding2) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_FallbackValue(self: win32more.Windows.UI.Xaml.Data.IBinding2, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_TargetNullValue(self: win32more.Windows.UI.Xaml.Data.IBinding2) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_TargetNullValue(self: win32more.Windows.UI.Xaml.Data.IBinding2, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateSourceTrigger(self: win32more.Windows.UI.Xaml.Data.IBinding2) -> win32more.Windows.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_mixinmethod
    def put_UpdateSourceTrigger(self: win32more.Windows.UI.Xaml.Data.IBinding2, value: win32more.Windows.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
    Converter = property(get_Converter, put_Converter)
    ConverterLanguage = property(get_ConverterLanguage, put_ConverterLanguage)
    ConverterParameter = property(get_ConverterParameter, put_ConverterParameter)
    ElementName = property(get_ElementName, put_ElementName)
    FallbackValue = property(get_FallbackValue, put_FallbackValue)
    Mode = property(get_Mode, put_Mode)
    Path = property(get_Path, put_Path)
    RelativeSource = property(get_RelativeSource, put_RelativeSource)
    Source = property(get_Source, put_Source)
    TargetNullValue = property(get_TargetNullValue, put_TargetNullValue)
    UpdateSourceTrigger = property(get_UpdateSourceTrigger, put_UpdateSourceTrigger)
class BindingBase(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Data.IBindingBase
    _classid_ = 'Windows.UI.Xaml.Data.BindingBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.BindingBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Data.IBindingBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.BindingBase: ...
class BindingExpression(ComPtr):
    extends: win32more.Windows.UI.Xaml.Data.BindingExpressionBase
    default_interface: win32more.Windows.UI.Xaml.Data.IBindingExpression
    _classid_ = 'Windows.UI.Xaml.Data.BindingExpression'
    @winrt_mixinmethod
    def get_DataItem(self: win32more.Windows.UI.Xaml.Data.IBindingExpression) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_ParentBinding(self: win32more.Windows.UI.Xaml.Data.IBindingExpression) -> win32more.Windows.UI.Xaml.Data.Binding: ...
    @winrt_mixinmethod
    def UpdateSource(self: win32more.Windows.UI.Xaml.Data.IBindingExpression) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class BindingExpressionBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Data.IBindingExpressionBase
    _classid_ = 'Windows.UI.Xaml.Data.BindingExpressionBase'
class BindingMode(Enum, Int32):
    OneWay = 1
    OneTime = 2
    TwoWay = 3
class BindingOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Data.IBindingOperations
    _classid_ = 'Windows.UI.Xaml.Data.BindingOperations'
    @winrt_classmethod
    def SetBinding(cls: win32more.Windows.UI.Xaml.Data.IBindingOperationsStatics, target: win32more.Windows.UI.Xaml.DependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty, binding: win32more.Windows.UI.Xaml.Data.BindingBase) -> Void: ...
class _CollectionViewSource_Meta_(ComPtr.__class__):
    pass
class CollectionViewSource(ComPtr, metaclass=_CollectionViewSource_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Data.ICollectionViewSource
    _classid_ = 'Windows.UI.Xaml.Data.CollectionViewSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.CollectionViewSource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Data.CollectionViewSource: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_View(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource) -> win32more.Windows.UI.Xaml.Data.ICollectionView: ...
    @winrt_mixinmethod
    def get_IsSourceGrouped(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSourceGrouped(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ItemsPath(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_ItemsPath(self: win32more.Windows.UI.Xaml.Data.ICollectionViewSource, value: win32more.Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_classmethod
    def get_SourceProperty(cls: win32more.Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewProperty(cls: win32more.Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsSourceGroupedProperty(cls: win32more.Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsPathProperty(cls: win32more.Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsSourceGrouped = property(get_IsSourceGrouped, put_IsSourceGrouped)
    ItemsPath = property(get_ItemsPath, put_ItemsPath)
    Source = property(get_Source, put_Source)
    View = property(get_View, None)
    _CollectionViewSource_Meta_.IsSourceGroupedProperty = property(get_IsSourceGroupedProperty, None)
    _CollectionViewSource_Meta_.ItemsPathProperty = property(get_ItemsPathProperty, None)
    _CollectionViewSource_Meta_.SourceProperty = property(get_SourceProperty, None)
    _CollectionViewSource_Meta_.ViewProperty = property(get_ViewProperty, None)
class CurrentChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Data.ICurrentChangingEventArgs
    _classid_ = 'Windows.UI.Xaml.Data.CurrentChangingEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs.CreateWithCancelableParameter(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Data.ICurrentChangingEventArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_factorymethod
    def CreateWithCancelableParameter(cls: win32more.Windows.UI.Xaml.Data.ICurrentChangingEventArgsFactory, isCancelable: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Xaml.Data.ICurrentChangingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Xaml.Data.ICurrentChangingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCancelable(self: win32more.Windows.UI.Xaml.Data.ICurrentChangingEventArgs) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    IsCancelable = property(get_IsCancelable, None)
class CurrentChangingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f3888db8-139f-4dce-8dc9-f7f1444d1185}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs) -> Void: ...
class IBinding(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBinding'
    _iid_ = Guid('{3f7a0c6b-d00f-4730-8c1d-48e16c46f9ca}')
    @winrt_commethod(6)
    def get_Path(self) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: win32more.Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Windows.UI.Xaml.Data.BindingMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Windows.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_commethod(10)
    def get_Source(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def put_Source(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(12)
    def get_RelativeSource(self) -> win32more.Windows.UI.Xaml.Data.RelativeSource: ...
    @winrt_commethod(13)
    def put_RelativeSource(self, value: win32more.Windows.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_commethod(14)
    def get_ElementName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ElementName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Converter(self) -> win32more.Windows.UI.Xaml.Data.IValueConverter: ...
    @winrt_commethod(17)
    def put_Converter(self, value: win32more.Windows.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_commethod(18)
    def get_ConverterParameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(19)
    def put_ConverterParameter(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(20)
    def get_ConverterLanguage(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_ConverterLanguage(self, value: WinRT_String) -> Void: ...
    Converter = property(get_Converter, put_Converter)
    ConverterLanguage = property(get_ConverterLanguage, put_ConverterLanguage)
    ConverterParameter = property(get_ConverterParameter, put_ConverterParameter)
    ElementName = property(get_ElementName, put_ElementName)
    Mode = property(get_Mode, put_Mode)
    Path = property(get_Path, put_Path)
    RelativeSource = property(get_RelativeSource, put_RelativeSource)
    Source = property(get_Source, put_Source)
class IBinding2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBinding2'
    _iid_ = Guid('{34f96fcb-0406-48b3-9e82-f333ec4c6910}')
    @winrt_commethod(6)
    def get_FallbackValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_FallbackValue(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_TargetNullValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def put_TargetNullValue(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(10)
    def get_UpdateSourceTrigger(self) -> win32more.Windows.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_commethod(11)
    def put_UpdateSourceTrigger(self, value: win32more.Windows.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
    FallbackValue = property(get_FallbackValue, put_FallbackValue)
    TargetNullValue = property(get_TargetNullValue, put_TargetNullValue)
    UpdateSourceTrigger = property(get_UpdateSourceTrigger, put_UpdateSourceTrigger)
class IBindingBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingBase'
    _iid_ = Guid('{1589a2ab-3d15-49bc-a447-8a5448e58870}')
class IBindingBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingBaseFactory'
    _iid_ = Guid('{22dafc3a-7701-4666-a1ba-9859bdcfec34}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.BindingBase: ...
class IBindingExpression(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpression'
    _iid_ = Guid('{516a19a5-c2fd-4a9e-9fd3-9aa42f995a3c}')
    @winrt_commethod(6)
    def get_DataItem(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_ParentBinding(self) -> win32more.Windows.UI.Xaml.Data.Binding: ...
    @winrt_commethod(8)
    def UpdateSource(self) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class IBindingExpressionBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpressionBase'
    _iid_ = Guid('{fded3154-e954-4f67-8fb6-6ed79b3a1cb3}')
class IBindingExpressionBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpressionBaseFactory'
    _iid_ = Guid('{ea7116a7-c2d9-4375-b471-66b9c48c7930}')
class IBindingExpressionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpressionFactory'
    _iid_ = Guid('{1cb55cd9-db72-40b3-a2b5-24ee6ea5c328}')
class IBindingFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingFactory'
    _iid_ = Guid('{ff42bb08-c39e-4f7e-8434-a1569083883c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.Binding: ...
class IBindingOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingOperations'
    _iid_ = Guid('{6fffd738-9839-419c-a17a-4b3604e1524e}')
class IBindingOperationsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingOperationsStatics'
    _iid_ = Guid('{e155ef73-95a0-4aab-8c7d-2a47da073c79}')
    @winrt_commethod(6)
    def SetBinding(self, target: win32more.Windows.UI.Xaml.DependencyObject, dp: win32more.Windows.UI.Xaml.DependencyProperty, binding: win32more.Windows.UI.Xaml.Data.BindingBase) -> Void: ...
class ICollectionView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Win32.System.WinRT.IInspectable]]
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionView'
    _iid_ = Guid('{8be8bfe4-dbef-44df-8126-a31a89121ddc}')
    @winrt_commethod(6)
    def get_CurrentItem(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_CurrentPosition(self) -> Int32: ...
    @winrt_commethod(8)
    def get_IsCurrentAfterLast(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsCurrentBeforeFirst(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CollectionGroups(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(11)
    def get_HasMoreItems(self) -> Boolean: ...
    @winrt_commethod(12)
    def add_CurrentChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CurrentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CurrentChanging(self, handler: win32more.Windows.UI.Xaml.Data.CurrentChangingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CurrentChanging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def MoveCurrentTo(self, item: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_commethod(17)
    def MoveCurrentToPosition(self, index: Int32) -> Boolean: ...
    @winrt_commethod(18)
    def MoveCurrentToFirst(self) -> Boolean: ...
    @winrt_commethod(19)
    def MoveCurrentToLast(self) -> Boolean: ...
    @winrt_commethod(20)
    def MoveCurrentToNext(self) -> Boolean: ...
    @winrt_commethod(21)
    def MoveCurrentToPrevious(self) -> Boolean: ...
    @winrt_commethod(22)
    def LoadMoreItemsAsync(self, count: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Data.LoadMoreItemsResult]: ...
    CollectionGroups = property(get_CollectionGroups, None)
    CurrentItem = property(get_CurrentItem, None)
    CurrentPosition = property(get_CurrentPosition, None)
    HasMoreItems = property(get_HasMoreItems, None)
    IsCurrentAfterLast = property(get_IsCurrentAfterLast, None)
    IsCurrentBeforeFirst = property(get_IsCurrentBeforeFirst, None)
    CurrentChanged = event()
    CurrentChanging = event()
class ICollectionViewFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewFactory'
    _iid_ = Guid('{34d4aaf4-8e72-4950-9192-ecd07d399d0a}')
    @winrt_commethod(6)
    def CreateView(self) -> win32more.Windows.UI.Xaml.Data.ICollectionView: ...
class ICollectionViewGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewGroup'
    _iid_ = Guid('{7e01b9d8-d7b5-48b6-b31c-5bb5bdf5f09b}')
    @winrt_commethod(6)
    def get_Group(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_GroupItems(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Group = property(get_Group, None)
    GroupItems = property(get_GroupItems, None)
class ICollectionViewSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewSource'
    _iid_ = Guid('{a66a1146-d2fb-4ead-be9f-3578a466dcfe}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_Source(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_View(self) -> win32more.Windows.UI.Xaml.Data.ICollectionView: ...
    @winrt_commethod(9)
    def get_IsSourceGrouped(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsSourceGrouped(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_ItemsPath(self) -> win32more.Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(12)
    def put_ItemsPath(self, value: win32more.Windows.UI.Xaml.PropertyPath) -> Void: ...
    IsSourceGrouped = property(get_IsSourceGrouped, put_IsSourceGrouped)
    ItemsPath = property(get_ItemsPath, put_ItemsPath)
    Source = property(get_Source, put_Source)
    View = property(get_View, None)
class ICollectionViewSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewSourceStatics'
    _iid_ = Guid('{173a0710-46af-4c0c-818b-21b6ef81bf65}')
    @winrt_commethod(6)
    def get_SourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ViewProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsSourceGroupedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ItemsPathProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsSourceGroupedProperty = property(get_IsSourceGroupedProperty, None)
    ItemsPathProperty = property(get_ItemsPathProperty, None)
    SourceProperty = property(get_SourceProperty, None)
    ViewProperty = property(get_ViewProperty, None)
class ICurrentChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICurrentChangingEventArgs'
    _iid_ = Guid('{f9891e29-51cc-47dd-a5b9-35dc4914af69}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsCancelable(self) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    IsCancelable = property(get_IsCancelable, None)
class ICurrentChangingEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICurrentChangingEventArgsFactory'
    _iid_ = Guid('{153bbeee-62f3-48cf-8183-8be26de3a66e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_commethod(7)
    def CreateWithCancelableParameter(self, isCancelable: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
class ICustomProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICustomProperty'
    _iid_ = Guid('{30da92c0-23e8-42a0-ae7c-734a0e5d2782}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetValue(self, target: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def SetValue(self, target: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(10)
    def GetIndexedValue(self, target: win32more.Windows.Win32.System.WinRT.IInspectable, index: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def SetIndexedValue(self, target: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable, index: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(12)
    def get_CanWrite(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_CanRead(self) -> Boolean: ...
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    Name = property(get_Name, None)
    Type = property(get_Type, None)
class ICustomPropertyProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICustomPropertyProvider'
    _iid_ = Guid('{7c925755-3e48-42b4-8677-76372267033f}')
    @winrt_commethod(6)
    def GetCustomProperty(self, name: WinRT_String) -> win32more.Windows.UI.Xaml.Data.ICustomProperty: ...
    @winrt_commethod(7)
    def GetIndexedProperty(self, name: WinRT_String, type: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Windows.UI.Xaml.Data.ICustomProperty: ...
    @winrt_commethod(8)
    def GetStringRepresentation(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Type(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Type = property(get_Type, None)
class IItemIndexRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IItemIndexRange'
    _iid_ = Guid('{83b834be-0583-4a26-9b64-8bf4a2f65704}')
    @winrt_commethod(6)
    def get_FirstIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Length(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_LastIndex(self) -> Int32: ...
    FirstIndex = property(get_FirstIndex, None)
    LastIndex = property(get_LastIndex, None)
    Length = property(get_Length, None)
class IItemIndexRangeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IItemIndexRangeFactory'
    _iid_ = Guid('{86e2c440-2e7a-4c7d-a664-e8abf07bfc7e}')
    @winrt_commethod(6)
    def CreateInstance(self, firstIndex: Int32, length: UInt32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.ItemIndexRange: ...
class IItemsRangeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.UI.Xaml.Data.IItemsRangeInfo'
    _iid_ = Guid('{f05f5665-71fd-45a2-be13-a081d294a68d}')
    @winrt_commethod(6)
    def RangesChanged(self, visibleRange: win32more.Windows.UI.Xaml.Data.ItemIndexRange, trackedItems: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Data.ItemIndexRange]) -> Void: ...
class INotifyPropertyChanged(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.INotifyPropertyChanged'
    _iid_ = Guid('{cf75d69c-f2f4-486b-b302-bb4c09baebfa}')
    @winrt_commethod(6)
    def add_PropertyChanged(self, handler: win32more.Windows.UI.Xaml.Data.PropertyChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PropertyChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PropertyChanged = event()
class IPropertyChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IPropertyChangedEventArgs'
    _iid_ = Guid('{4f33a9a0-5cf4-47a4-b16f-d7faaf17457e}')
    @winrt_commethod(6)
    def get_PropertyName(self) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class IPropertyChangedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IPropertyChangedEventArgsFactory'
    _iid_ = Guid('{6dcc9c03-e0c7-4eee-8ea9-37e3406eeb1c}')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.PropertyChangedEventArgs: ...
class IRelativeSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IRelativeSource'
    _iid_ = Guid('{2397ce84-2822-483a-b499-d0f031e06c6b}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class IRelativeSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IRelativeSourceFactory'
    _iid_ = Guid('{ef8392cd-446e-4f93-aacb-9b1255577460}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.RelativeSource: ...
class ISelectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ISelectionInfo'
    _iid_ = Guid('{2e12ca86-e1ed-4245-be49-207e42aec524}')
    @winrt_commethod(6)
    def SelectRange(self, itemIndexRange: win32more.Windows.UI.Xaml.Data.ItemIndexRange) -> Void: ...
    @winrt_commethod(7)
    def DeselectRange(self, itemIndexRange: win32more.Windows.UI.Xaml.Data.ItemIndexRange) -> Void: ...
    @winrt_commethod(8)
    def IsSelected(self, index: Int32) -> Boolean: ...
    @winrt_commethod(9)
    def GetSelectedRanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Data.ItemIndexRange]: ...
class ISupportIncrementalLoading(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ISupportIncrementalLoading'
    _iid_ = Guid('{7f5ee992-7694-4e6c-a51b-e34bf43de743}')
    @winrt_commethod(6)
    def LoadMoreItemsAsync(self, count: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Data.LoadMoreItemsResult]: ...
    @winrt_commethod(7)
    def get_HasMoreItems(self) -> Boolean: ...
    HasMoreItems = property(get_HasMoreItems, None)
class IValueConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IValueConverter'
    _iid_ = Guid('{e6f2fef0-0712-487f-b313-f300b8d79aa1}')
    @winrt_commethod(6)
    def Convert(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def ConvertBack(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class ItemIndexRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Data.IItemIndexRange
    _classid_ = 'Windows.UI.Xaml.Data.ItemIndexRange'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.ItemIndexRange.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Data.IItemIndexRangeFactory, firstIndex: Int32, length: UInt32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.ItemIndexRange: ...
    @winrt_mixinmethod
    def get_FirstIndex(self: win32more.Windows.UI.Xaml.Data.IItemIndexRange) -> Int32: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.UI.Xaml.Data.IItemIndexRange) -> UInt32: ...
    @winrt_mixinmethod
    def get_LastIndex(self: win32more.Windows.UI.Xaml.Data.IItemIndexRange) -> Int32: ...
    FirstIndex = property(get_FirstIndex, None)
    LastIndex = property(get_LastIndex, None)
    Length = property(get_Length, None)
class LoadMoreItemsResult(Structure):
    Count: UInt32
class PropertyChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Data.IPropertyChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Data.PropertyChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.PropertyChangedEventArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Data.IPropertyChangedEventArgsFactory, name: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.PropertyChangedEventArgs: ...
    @winrt_mixinmethod
    def get_PropertyName(self: win32more.Windows.UI.Xaml.Data.IPropertyChangedEventArgs) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class PropertyChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50f19c16-0a22-4d8e-a089-1ea9951657d2}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Data.PropertyChangedEventArgs) -> Void: ...
class RelativeSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Data.IRelativeSource
    _classid_ = 'Windows.UI.Xaml.Data.RelativeSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Data.RelativeSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Data.IRelativeSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Data.RelativeSource: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Xaml.Data.IRelativeSource) -> win32more.Windows.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.UI.Xaml.Data.IRelativeSource, value: win32more.Windows.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class RelativeSourceMode(Enum, Int32):
    None_ = 0
    TemplatedParent = 1
    Self = 2
class UpdateSourceTrigger(Enum, Int32):
    Default = 0
    PropertyChanged = 1
    Explicit = 2
    LostFocus = 3


make_ready(__name__)
