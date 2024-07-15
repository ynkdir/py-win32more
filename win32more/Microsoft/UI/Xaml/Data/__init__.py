from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Data
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class Binding(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Data.BindingBase
    default_interface: win32more.Microsoft.UI.Xaml.Data.IBinding
    _classid_ = 'Microsoft.UI.Xaml.Data.Binding'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.Binding.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.IBindingFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.Binding: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Microsoft.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Microsoft.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Microsoft.UI.Xaml.Data.BindingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Microsoft.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeSource(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Microsoft.UI.Xaml.Data.RelativeSource: ...
    @winrt_mixinmethod
    def put_RelativeSource(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Microsoft.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_mixinmethod
    def get_ElementName(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ElementName(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Converter(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Microsoft.UI.Xaml.Data.IValueConverter: ...
    @winrt_mixinmethod
    def put_Converter(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Microsoft.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_mixinmethod
    def get_ConverterParameter(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ConverterParameter(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_ConverterLanguage(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ConverterLanguage(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackValue(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_FallbackValue(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_TargetNullValue(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_TargetNullValue(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateSourceTrigger(self: win32more.Microsoft.UI.Xaml.Data.IBinding) -> win32more.Microsoft.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_mixinmethod
    def put_UpdateSourceTrigger(self: win32more.Microsoft.UI.Xaml.Data.IBinding, value: win32more.Microsoft.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
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
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Data.IBindingBase
    _classid_ = 'Microsoft.UI.Xaml.Data.BindingBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.BindingBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.IBindingBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.BindingBase: ...
class BindingExpression(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Data.BindingExpressionBase
    default_interface: win32more.Microsoft.UI.Xaml.Data.IBindingExpression
    _classid_ = 'Microsoft.UI.Xaml.Data.BindingExpression'
    @winrt_mixinmethod
    def get_DataItem(self: win32more.Microsoft.UI.Xaml.Data.IBindingExpression) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_ParentBinding(self: win32more.Microsoft.UI.Xaml.Data.IBindingExpression) -> win32more.Microsoft.UI.Xaml.Data.Binding: ...
    @winrt_mixinmethod
    def UpdateSource(self: win32more.Microsoft.UI.Xaml.Data.IBindingExpression) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class BindingExpressionBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Data.IBindingExpressionBase
    _classid_ = 'Microsoft.UI.Xaml.Data.BindingExpressionBase'
class BindingMode(Enum, Int32):
    OneWay = 1
    OneTime = 2
    TwoWay = 3
class BindingOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Data.IBindingOperations
    _classid_ = 'Microsoft.UI.Xaml.Data.BindingOperations'
    @winrt_classmethod
    def SetBinding(cls: win32more.Microsoft.UI.Xaml.Data.IBindingOperationsStatics, target: win32more.Microsoft.UI.Xaml.DependencyObject, dp: win32more.Microsoft.UI.Xaml.DependencyProperty, binding: win32more.Microsoft.UI.Xaml.Data.BindingBase) -> Void: ...
class _CollectionViewSource_Meta_(ComPtr.__class__):
    pass
class CollectionViewSource(ComPtr, metaclass=_CollectionViewSource_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource
    _classid_ = 'Microsoft.UI.Xaml.Data.CollectionViewSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.CollectionViewSource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Data.CollectionViewSource: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_View(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource) -> win32more.Microsoft.UI.Xaml.Data.ICollectionView: ...
    @winrt_mixinmethod
    def get_IsSourceGrouped(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSourceGrouped(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ItemsPath(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource) -> win32more.Microsoft.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_ItemsPath(self: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSource, value: win32more.Microsoft.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_classmethod
    def get_SourceProperty(cls: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewProperty(cls: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsSourceGroupedProperty(cls: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsPathProperty(cls: win32more.Microsoft.UI.Xaml.Data.ICollectionViewSourceStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    default_interface: win32more.Microsoft.UI.Xaml.Data.ICurrentChangingEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Data.CurrentChangingEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs.CreateWithCancelableParameter(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.ICurrentChangingEventArgsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_factorymethod
    def CreateWithCancelableParameter(cls: win32more.Microsoft.UI.Xaml.Data.ICurrentChangingEventArgsFactory, isCancelable: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.UI.Xaml.Data.ICurrentChangingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.UI.Xaml.Data.ICurrentChangingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCancelable(self: win32more.Microsoft.UI.Xaml.Data.ICurrentChangingEventArgs) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    IsCancelable = property(get_IsCancelable, None)
class CurrentChangingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d2a98dd-95b3-5fd5-93b4-a1a2599f225c}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs) -> Void: ...
class DataErrorsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Data.IDataErrorsChangedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Data.DataErrorsChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.DataErrorsChangedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.IDataErrorsChangedEventArgsFactory, name: WinRT_String) -> win32more.Microsoft.UI.Xaml.Data.DataErrorsChangedEventArgs: ...
    @winrt_mixinmethod
    def get_PropertyName(self: win32more.Microsoft.UI.Xaml.Data.IDataErrorsChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PropertyName(self: win32more.Microsoft.UI.Xaml.Data.IDataErrorsChangedEventArgs, value: WinRT_String) -> Void: ...
    PropertyName = property(get_PropertyName, put_PropertyName)
class IBinding(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBinding'
    _iid_ = Guid('{501ea0e8-edd4-59de-8845-76af2eabbe00}')
    @winrt_commethod(6)
    def get_Path(self) -> win32more.Microsoft.UI.Xaml.PropertyPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: win32more.Microsoft.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> win32more.Microsoft.UI.Xaml.Data.BindingMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: win32more.Microsoft.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_commethod(10)
    def get_Source(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def put_Source(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(12)
    def get_RelativeSource(self) -> win32more.Microsoft.UI.Xaml.Data.RelativeSource: ...
    @winrt_commethod(13)
    def put_RelativeSource(self, value: win32more.Microsoft.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_commethod(14)
    def get_ElementName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ElementName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Converter(self) -> win32more.Microsoft.UI.Xaml.Data.IValueConverter: ...
    @winrt_commethod(17)
    def put_Converter(self, value: win32more.Microsoft.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_commethod(18)
    def get_ConverterParameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(19)
    def put_ConverterParameter(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(20)
    def get_ConverterLanguage(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_ConverterLanguage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_FallbackValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(23)
    def put_FallbackValue(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(24)
    def get_TargetNullValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(25)
    def put_TargetNullValue(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(26)
    def get_UpdateSourceTrigger(self) -> win32more.Microsoft.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_commethod(27)
    def put_UpdateSourceTrigger(self, value: win32more.Microsoft.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
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
class IBindingBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingBase'
    _iid_ = Guid('{91ddd141-5944-50ef-b85e-218e463f7a73}')
class IBindingBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingBaseFactory'
    _iid_ = Guid('{c8a866c5-f6f3-5f7a-9592-d385af48bd8f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.BindingBase: ...
class IBindingExpression(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingExpression'
    _iid_ = Guid('{4c023916-37bc-5b07-bc9d-15c547bd9b26}')
    @winrt_commethod(6)
    def get_DataItem(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_ParentBinding(self) -> win32more.Microsoft.UI.Xaml.Data.Binding: ...
    @winrt_commethod(8)
    def UpdateSource(self) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class IBindingExpressionBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingExpressionBase'
    _iid_ = Guid('{8825e5a9-d9a3-5e87-bcd8-c63133d29029}')
class IBindingExpressionBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingExpressionBaseFactory'
    _iid_ = Guid('{41d643b9-2629-5451-a716-596c0848b5dc}')
class IBindingExpressionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingExpressionFactory'
    _iid_ = Guid('{086cae14-81a1-588b-b619-05ee84c0f089}')
class IBindingFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingFactory'
    _iid_ = Guid('{cb2de749-b115-5f67-b64a-797d54885d5c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.Binding: ...
class IBindingOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingOperations'
    _iid_ = Guid('{9a319b95-aabe-5075-b227-8eb07e443d8b}')
class IBindingOperationsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IBindingOperationsStatics'
    _iid_ = Guid('{1e1bdbd3-fca5-5c85-b87d-b504cd8fa8ac}')
    @winrt_commethod(6)
    def SetBinding(self, target: win32more.Microsoft.UI.Xaml.DependencyObject, dp: win32more.Microsoft.UI.Xaml.DependencyProperty, binding: win32more.Microsoft.UI.Xaml.Data.BindingBase) -> Void: ...
class ICollectionView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Win32.System.WinRT.IInspectable]]
    _classid_ = 'Microsoft.UI.Xaml.Data.ICollectionView'
    _iid_ = Guid('{f8bb90d8-e008-5d65-8c97-7bb790a4230c}')
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
    def add_CurrentChanging(self, handler: win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    def LoadMoreItemsAsync(self, count: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Data.LoadMoreItemsResult]: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Data.ICollectionViewFactory'
    _iid_ = Guid('{d971f795-5728-5bef-9602-43f2c4250e56}')
    @winrt_commethod(6)
    def CreateView(self) -> win32more.Microsoft.UI.Xaml.Data.ICollectionView: ...
class ICollectionViewGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ICollectionViewGroup'
    _iid_ = Guid('{96a08da8-be38-5ae0-903d-6fb6111e61f5}')
    @winrt_commethod(6)
    def get_Group(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_GroupItems(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Group = property(get_Group, None)
    GroupItems = property(get_GroupItems, None)
class ICollectionViewSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ICollectionViewSource'
    _iid_ = Guid('{a45e3b3a-f31e-5bbb-8a7c-70cf5c64bc3f}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_Source(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_View(self) -> win32more.Microsoft.UI.Xaml.Data.ICollectionView: ...
    @winrt_commethod(9)
    def get_IsSourceGrouped(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsSourceGrouped(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_ItemsPath(self) -> win32more.Microsoft.UI.Xaml.PropertyPath: ...
    @winrt_commethod(12)
    def put_ItemsPath(self, value: win32more.Microsoft.UI.Xaml.PropertyPath) -> Void: ...
    IsSourceGrouped = property(get_IsSourceGrouped, put_IsSourceGrouped)
    ItemsPath = property(get_ItemsPath, put_ItemsPath)
    Source = property(get_Source, put_Source)
    View = property(get_View, None)
class ICollectionViewSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ICollectionViewSourceStatics'
    _iid_ = Guid('{e282f10f-d4b1-5769-8a11-30f739e6113b}')
    @winrt_commethod(6)
    def get_SourceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ViewProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsSourceGroupedProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ItemsPathProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsSourceGroupedProperty = property(get_IsSourceGroupedProperty, None)
    ItemsPathProperty = property(get_ItemsPathProperty, None)
    SourceProperty = property(get_SourceProperty, None)
    ViewProperty = property(get_ViewProperty, None)
class ICurrentChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ICurrentChangingEventArgs'
    _iid_ = Guid('{63e42ed6-e14a-51ea-9cb1-72f9c907dc80}')
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
    _classid_ = 'Microsoft.UI.Xaml.Data.ICurrentChangingEventArgsFactory'
    _iid_ = Guid('{3670f48a-ac2c-5352-8a4b-6b977a08e5f8}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_commethod(7)
    def CreateWithCancelableParameter(self, isCancelable: Boolean, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.CurrentChangingEventArgs: ...
class ICustomProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ICustomProperty'
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
    _classid_ = 'Microsoft.UI.Xaml.Data.ICustomPropertyProvider'
    _iid_ = Guid('{7c925755-3e48-42b4-8677-76372267033f}')
    @winrt_commethod(6)
    def GetCustomProperty(self, name: WinRT_String) -> win32more.Microsoft.UI.Xaml.Data.ICustomProperty: ...
    @winrt_commethod(7)
    def GetIndexedProperty(self, name: WinRT_String, type: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Microsoft.UI.Xaml.Data.ICustomProperty: ...
    @winrt_commethod(8)
    def GetStringRepresentation(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Type(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Type = property(get_Type, None)
class IDataErrorsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IDataErrorsChangedEventArgs'
    _iid_ = Guid('{d026dd64-5f26-5f15-a86a-0dec8a431796}')
    @winrt_commethod(6)
    def get_PropertyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_PropertyName(self, value: WinRT_String) -> Void: ...
    PropertyName = property(get_PropertyName, put_PropertyName)
class IDataErrorsChangedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IDataErrorsChangedEventArgsFactory'
    _iid_ = Guid('{62d0bd1e-b85f-5fcc-842a-7cb0dda37fe5}')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String) -> win32more.Microsoft.UI.Xaml.Data.DataErrorsChangedEventArgs: ...
class IItemIndexRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IItemIndexRange'
    _iid_ = Guid('{eba09846-2554-5b86-ac17-614f05105fa2}')
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
    _classid_ = 'Microsoft.UI.Xaml.Data.IItemIndexRangeFactory'
    _iid_ = Guid('{9fc73213-eda0-5238-aa2c-401c9921f0f9}')
    @winrt_commethod(6)
    def CreateInstance(self, firstIndex: Int32, length: UInt32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.ItemIndexRange: ...
class IItemsRangeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.UI.Xaml.Data.IItemsRangeInfo'
    _iid_ = Guid('{b8376d08-85fb-563b-8273-39ef2d138256}')
    @winrt_commethod(6)
    def RangesChanged(self, visibleRange: win32more.Microsoft.UI.Xaml.Data.ItemIndexRange, trackedItems: win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Data.ItemIndexRange]) -> Void: ...
class INotifyDataErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.INotifyDataErrorInfo'
    _iid_ = Guid('{0ee6c2cc-273e-567d-bc0a-1dd87ee51eba}')
    @winrt_commethod(6)
    def get_HasErrors(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_ErrorsChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Data.DataErrorsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ErrorsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def GetErrors(self, propertyName: WinRT_String) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    HasErrors = property(get_HasErrors, None)
    ErrorsChanged = event()
class INotifyPropertyChanged(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.INotifyPropertyChanged'
    _iid_ = Guid('{90b17601-b065-586e-83d9-9adc3a695284}')
    @winrt_commethod(6)
    def add_PropertyChanged(self, handler: win32more.Microsoft.UI.Xaml.Data.PropertyChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PropertyChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PropertyChanged = event()
class IPropertyChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IPropertyChangedEventArgs'
    _iid_ = Guid('{63d0c952-396b-54f4-af8c-ba8724a427bf}')
    @winrt_commethod(6)
    def get_PropertyName(self) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class IPropertyChangedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IPropertyChangedEventArgsFactory'
    _iid_ = Guid('{7c0c27a8-0b41-5070-b160-fc9ae960a36c}')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.PropertyChangedEventArgs: ...
class IRelativeSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IRelativeSource'
    _iid_ = Guid('{7ffc8126-5dd8-58bb-b686-c71eddea07b2}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Microsoft.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Microsoft.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class IRelativeSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IRelativeSourceFactory'
    _iid_ = Guid('{8518522c-85e3-5ae1-b9e9-28ea43c2051e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.RelativeSource: ...
class ISelectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ISelectionInfo'
    _iid_ = Guid('{1b84c26b-9532-5803-935b-a03bf7e875dc}')
    @winrt_commethod(6)
    def SelectRange(self, itemIndexRange: win32more.Microsoft.UI.Xaml.Data.ItemIndexRange) -> Void: ...
    @winrt_commethod(7)
    def DeselectRange(self, itemIndexRange: win32more.Microsoft.UI.Xaml.Data.ItemIndexRange) -> Void: ...
    @winrt_commethod(8)
    def IsSelected(self, index: Int32) -> Boolean: ...
    @winrt_commethod(9)
    def GetSelectedRanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Data.ItemIndexRange]: ...
class ISupportIncrementalLoading(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.ISupportIncrementalLoading'
    _iid_ = Guid('{d8f9b586-a64a-5ff8-868e-204e144f2cf4}')
    @winrt_commethod(6)
    def LoadMoreItemsAsync(self, count: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.UI.Xaml.Data.LoadMoreItemsResult]: ...
    @winrt_commethod(7)
    def get_HasMoreItems(self) -> Boolean: ...
    HasMoreItems = property(get_HasMoreItems, None)
class IValueConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Data.IValueConverter'
    _iid_ = Guid('{afdd2bff-10f5-5173-b7c0-3590bd96cb35}')
    @winrt_commethod(6)
    def Convert(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def ConvertBack(self, value: win32more.Windows.Win32.System.WinRT.IInspectable, targetType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, language: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class ItemIndexRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Data.IItemIndexRange
    _classid_ = 'Microsoft.UI.Xaml.Data.ItemIndexRange'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.ItemIndexRange.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.IItemIndexRangeFactory, firstIndex: Int32, length: UInt32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.ItemIndexRange: ...
    @winrt_mixinmethod
    def get_FirstIndex(self: win32more.Microsoft.UI.Xaml.Data.IItemIndexRange) -> Int32: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Microsoft.UI.Xaml.Data.IItemIndexRange) -> UInt32: ...
    @winrt_mixinmethod
    def get_LastIndex(self: win32more.Microsoft.UI.Xaml.Data.IItemIndexRange) -> Int32: ...
    FirstIndex = property(get_FirstIndex, None)
    LastIndex = property(get_LastIndex, None)
    Length = property(get_Length, None)
class LoadMoreItemsResult(Structure):
    Count: UInt32
class PropertyChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Data.IPropertyChangedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Data.PropertyChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.PropertyChangedEventArgs.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.IPropertyChangedEventArgsFactory, name: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.PropertyChangedEventArgs: ...
    @winrt_mixinmethod
    def get_PropertyName(self: win32more.Microsoft.UI.Xaml.Data.IPropertyChangedEventArgs) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class PropertyChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e3de52f6-1e32-5da6-bb2d-b5b6096c962d}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Data.PropertyChangedEventArgs) -> Void: ...
class RelativeSource(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Data.IRelativeSource
    _classid_ = 'Microsoft.UI.Xaml.Data.RelativeSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Data.RelativeSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Data.IRelativeSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Data.RelativeSource: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Microsoft.UI.Xaml.Data.IRelativeSource) -> win32more.Microsoft.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Microsoft.UI.Xaml.Data.IRelativeSource, value: win32more.Microsoft.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
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
