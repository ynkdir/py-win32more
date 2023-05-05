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
import Windows.UI.Xaml
import Windows.UI.Xaml.Data
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
class Binding(ComPtr):
    extends: Windows.UI.Xaml.Data.BindingBase
    default_interface: Windows.UI.Xaml.Data.IBinding
    _classid_ = 'Windows.UI.Xaml.Data.Binding'
    @winrt_mixinmethod
    def get_Path(self: Windows.UI.Xaml.Data.IBinding) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.UI.Xaml.Data.IBinding, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Xaml.Data.IBinding) -> Windows.UI.Xaml.Data.BindingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.UI.Xaml.Data.IBinding, value: Windows.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Xaml.Data.IBinding) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.UI.Xaml.Data.IBinding, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeSource(self: Windows.UI.Xaml.Data.IBinding) -> Windows.UI.Xaml.Data.RelativeSource: ...
    @winrt_mixinmethod
    def put_RelativeSource(self: Windows.UI.Xaml.Data.IBinding, value: Windows.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_mixinmethod
    def get_ElementName(self: Windows.UI.Xaml.Data.IBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ElementName(self: Windows.UI.Xaml.Data.IBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Converter(self: Windows.UI.Xaml.Data.IBinding) -> Windows.UI.Xaml.Data.IValueConverter: ...
    @winrt_mixinmethod
    def put_Converter(self: Windows.UI.Xaml.Data.IBinding, value: Windows.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_mixinmethod
    def get_ConverterParameter(self: Windows.UI.Xaml.Data.IBinding) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_ConverterParameter(self: Windows.UI.Xaml.Data.IBinding, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_ConverterLanguage(self: Windows.UI.Xaml.Data.IBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ConverterLanguage(self: Windows.UI.Xaml.Data.IBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackValue(self: Windows.UI.Xaml.Data.IBinding2) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_FallbackValue(self: Windows.UI.Xaml.Data.IBinding2, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_TargetNullValue(self: Windows.UI.Xaml.Data.IBinding2) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_TargetNullValue(self: Windows.UI.Xaml.Data.IBinding2, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateSourceTrigger(self: Windows.UI.Xaml.Data.IBinding2) -> Windows.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_mixinmethod
    def put_UpdateSourceTrigger(self: Windows.UI.Xaml.Data.IBinding2, value: Windows.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
    Path = property(get_Path, put_Path)
    Mode = property(get_Mode, put_Mode)
    Source = property(get_Source, put_Source)
    RelativeSource = property(get_RelativeSource, put_RelativeSource)
    ElementName = property(get_ElementName, put_ElementName)
    Converter = property(get_Converter, put_Converter)
    ConverterParameter = property(get_ConverterParameter, put_ConverterParameter)
    ConverterLanguage = property(get_ConverterLanguage, put_ConverterLanguage)
    FallbackValue = property(get_FallbackValue, put_FallbackValue)
    TargetNullValue = property(get_TargetNullValue, put_TargetNullValue)
    UpdateSourceTrigger = property(get_UpdateSourceTrigger, put_UpdateSourceTrigger)
class BindingBase(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Data.IBindingBase
    _classid_ = 'Windows.UI.Xaml.Data.BindingBase'
class BindingExpression(ComPtr):
    extends: Windows.UI.Xaml.Data.BindingExpressionBase
    default_interface: Windows.UI.Xaml.Data.IBindingExpression
    _classid_ = 'Windows.UI.Xaml.Data.BindingExpression'
    @winrt_mixinmethod
    def get_DataItem(self: Windows.UI.Xaml.Data.IBindingExpression) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_ParentBinding(self: Windows.UI.Xaml.Data.IBindingExpression) -> Windows.UI.Xaml.Data.Binding: ...
    @winrt_mixinmethod
    def UpdateSource(self: Windows.UI.Xaml.Data.IBindingExpression) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class BindingExpressionBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Data.IBindingExpressionBase
    _classid_ = 'Windows.UI.Xaml.Data.BindingExpressionBase'
BindingMode = Int32
BindingMode_OneWay: BindingMode = 1
BindingMode_OneTime: BindingMode = 2
BindingMode_TwoWay: BindingMode = 3
class BindingOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Data.IBindingOperations
    _classid_ = 'Windows.UI.Xaml.Data.BindingOperations'
    @winrt_classmethod
    def SetBinding(cls: Windows.UI.Xaml.Data.IBindingOperationsStatics, target: Windows.UI.Xaml.DependencyObject, dp: Windows.UI.Xaml.DependencyProperty, binding: Windows.UI.Xaml.Data.BindingBase) -> Void: ...
class CollectionViewSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Data.ICollectionViewSource
    _classid_ = 'Windows.UI.Xaml.Data.CollectionViewSource'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Data.CollectionViewSource: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Xaml.Data.ICollectionViewSource) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.UI.Xaml.Data.ICollectionViewSource, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_View(self: Windows.UI.Xaml.Data.ICollectionViewSource) -> Windows.UI.Xaml.Data.ICollectionView: ...
    @winrt_mixinmethod
    def get_IsSourceGrouped(self: Windows.UI.Xaml.Data.ICollectionViewSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSourceGrouped(self: Windows.UI.Xaml.Data.ICollectionViewSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ItemsPath(self: Windows.UI.Xaml.Data.ICollectionViewSource) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_mixinmethod
    def put_ItemsPath(self: Windows.UI.Xaml.Data.ICollectionViewSource, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_classmethod
    def get_SourceProperty(cls: Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewProperty(cls: Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsSourceGroupedProperty(cls: Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsPathProperty(cls: Windows.UI.Xaml.Data.ICollectionViewSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Source = property(get_Source, put_Source)
    View = property(get_View, None)
    IsSourceGrouped = property(get_IsSourceGrouped, put_IsSourceGrouped)
    ItemsPath = property(get_ItemsPath, put_ItemsPath)
    SourceProperty = property(get_SourceProperty, None)
    ViewProperty = property(get_ViewProperty, None)
    IsSourceGroupedProperty = property(get_IsSourceGroupedProperty, None)
    ItemsPathProperty = property(get_ItemsPathProperty, None)
class CurrentChangingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Data.ICurrentChangingEventArgs
    _classid_ = 'Windows.UI.Xaml.Data.CurrentChangingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.Xaml.Data.ICurrentChangingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.Xaml.Data.ICurrentChangingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCancelable(self: Windows.UI.Xaml.Data.ICurrentChangingEventArgs) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    IsCancelable = property(get_IsCancelable, None)
class CurrentChangingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Data.CurrentChangingEventHandler'
    _iid_ = Guid('{f3888db8-139f-4dce-8dc9-f7f1444d1185}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Data.CurrentChangingEventArgs) -> Void: ...
class IBinding(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBinding'
    _iid_ = Guid('{3f7a0c6b-d00f-4730-8c1d-48e16c46f9ca}')
    @winrt_commethod(6)
    def get_Path(self) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_commethod(8)
    def get_Mode(self) -> Windows.UI.Xaml.Data.BindingMode: ...
    @winrt_commethod(9)
    def put_Mode(self, value: Windows.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_commethod(10)
    def get_Source(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def put_Source(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(12)
    def get_RelativeSource(self) -> Windows.UI.Xaml.Data.RelativeSource: ...
    @winrt_commethod(13)
    def put_RelativeSource(self, value: Windows.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_commethod(14)
    def get_ElementName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ElementName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Converter(self) -> Windows.UI.Xaml.Data.IValueConverter: ...
    @winrt_commethod(17)
    def put_Converter(self, value: Windows.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_commethod(18)
    def get_ConverterParameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(19)
    def put_ConverterParameter(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(20)
    def get_ConverterLanguage(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_ConverterLanguage(self, value: WinRT_String) -> Void: ...
    Path = property(get_Path, put_Path)
    Mode = property(get_Mode, put_Mode)
    Source = property(get_Source, put_Source)
    RelativeSource = property(get_RelativeSource, put_RelativeSource)
    ElementName = property(get_ElementName, put_ElementName)
    Converter = property(get_Converter, put_Converter)
    ConverterParameter = property(get_ConverterParameter, put_ConverterParameter)
    ConverterLanguage = property(get_ConverterLanguage, put_ConverterLanguage)
class IBinding2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBinding2'
    _iid_ = Guid('{34f96fcb-0406-48b3-9e82-f333ec4c6910}')
    @winrt_commethod(6)
    def get_FallbackValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_FallbackValue(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def get_TargetNullValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def put_TargetNullValue(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(10)
    def get_UpdateSourceTrigger(self) -> Windows.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_commethod(11)
    def put_UpdateSourceTrigger(self, value: Windows.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
    FallbackValue = property(get_FallbackValue, put_FallbackValue)
    TargetNullValue = property(get_TargetNullValue, put_TargetNullValue)
    UpdateSourceTrigger = property(get_UpdateSourceTrigger, put_UpdateSourceTrigger)
class IBindingBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingBase'
    _iid_ = Guid('{1589a2ab-3d15-49bc-a447-8a5448e58870}')
class IBindingBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingBaseFactory'
    _iid_ = Guid('{22dafc3a-7701-4666-a1ba-9859bdcfec34}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.BindingBase: ...
class IBindingExpression(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpression'
    _iid_ = Guid('{516a19a5-c2fd-4a9e-9fd3-9aa42f995a3c}')
    @winrt_commethod(6)
    def get_DataItem(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_ParentBinding(self) -> Windows.UI.Xaml.Data.Binding: ...
    @winrt_commethod(8)
    def UpdateSource(self) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class IBindingExpressionBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpressionBase'
    _iid_ = Guid('{fded3154-e954-4f67-8fb6-6ed79b3a1cb3}')
class IBindingExpressionBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpressionBaseFactory'
    _iid_ = Guid('{ea7116a7-c2d9-4375-b471-66b9c48c7930}')
class IBindingExpressionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingExpressionFactory'
    _iid_ = Guid('{1cb55cd9-db72-40b3-a2b5-24ee6ea5c328}')
class IBindingFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingFactory'
    _iid_ = Guid('{ff42bb08-c39e-4f7e-8434-a1569083883c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.Binding: ...
class IBindingOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingOperations'
    _iid_ = Guid('{6fffd738-9839-419c-a17a-4b3604e1524e}')
class IBindingOperationsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IBindingOperationsStatics'
    _iid_ = Guid('{e155ef73-95a0-4aab-8c7d-2a47da073c79}')
    @winrt_commethod(6)
    def SetBinding(self, target: Windows.UI.Xaml.DependencyObject, dp: Windows.UI.Xaml.DependencyProperty, binding: Windows.UI.Xaml.Data.BindingBase) -> Void: ...
class ICollectionView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionView'
    _iid_ = Guid('{8be8bfe4-dbef-44df-8126-a31a89121ddc}')
    @winrt_commethod(6)
    def get_CurrentItem(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_CurrentPosition(self) -> Int32: ...
    @winrt_commethod(8)
    def get_IsCurrentAfterLast(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsCurrentBeforeFirst(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CollectionGroups(self) -> Windows.Foundation.Collections.IObservableVector[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(11)
    def get_HasMoreItems(self) -> Boolean: ...
    @winrt_commethod(12)
    def add_CurrentChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CurrentChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CurrentChanging(self, handler: Windows.UI.Xaml.Data.CurrentChangingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CurrentChanging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def MoveCurrentTo(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
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
    def LoadMoreItemsAsync(self, count: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Data.LoadMoreItemsResult]: ...
    CurrentItem = property(get_CurrentItem, None)
    CurrentPosition = property(get_CurrentPosition, None)
    IsCurrentAfterLast = property(get_IsCurrentAfterLast, None)
    IsCurrentBeforeFirst = property(get_IsCurrentBeforeFirst, None)
    CollectionGroups = property(get_CollectionGroups, None)
    HasMoreItems = property(get_HasMoreItems, None)
class ICollectionViewFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewFactory'
    _iid_ = Guid('{34d4aaf4-8e72-4950-9192-ecd07d399d0a}')
    @winrt_commethod(6)
    def CreateView(self) -> Windows.UI.Xaml.Data.ICollectionView: ...
class ICollectionViewGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewGroup'
    _iid_ = Guid('{7e01b9d8-d7b5-48b6-b31c-5bb5bdf5f09b}')
    @winrt_commethod(6)
    def get_Group(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_GroupItems(self) -> Windows.Foundation.Collections.IObservableVector[Windows.Win32.System.WinRT.IInspectable_head]: ...
    Group = property(get_Group, None)
    GroupItems = property(get_GroupItems, None)
class ICollectionViewSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewSource'
    _iid_ = Guid('{a66a1146-d2fb-4ead-be9f-3578a466dcfe}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_Source(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def get_View(self) -> Windows.UI.Xaml.Data.ICollectionView: ...
    @winrt_commethod(9)
    def get_IsSourceGrouped(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsSourceGrouped(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_ItemsPath(self) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(12)
    def put_ItemsPath(self, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    Source = property(get_Source, put_Source)
    View = property(get_View, None)
    IsSourceGrouped = property(get_IsSourceGrouped, put_IsSourceGrouped)
    ItemsPath = property(get_ItemsPath, put_ItemsPath)
class ICollectionViewSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICollectionViewSourceStatics'
    _iid_ = Guid('{173a0710-46af-4c0c-818b-21b6ef81bf65}')
    @winrt_commethod(6)
    def get_SourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ViewProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsSourceGroupedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ItemsPathProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    SourceProperty = property(get_SourceProperty, None)
    ViewProperty = property(get_ViewProperty, None)
    IsSourceGroupedProperty = property(get_IsSourceGroupedProperty, None)
    ItemsPathProperty = property(get_ItemsPathProperty, None)
class ICurrentChangingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICurrentChangingEventArgsFactory'
    _iid_ = Guid('{153bbeee-62f3-48cf-8183-8be26de3a66e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_commethod(7)
    def CreateWithCancelableParameter(self, isCancelable: Boolean, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
class ICustomProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICustomProperty'
    _iid_ = Guid('{30da92c0-23e8-42a0-ae7c-734a0e5d2782}')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetValue(self, target: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def SetValue(self, target: Windows.Win32.System.WinRT.IInspectable_head, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(10)
    def GetIndexedValue(self, target: Windows.Win32.System.WinRT.IInspectable_head, index: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def SetIndexedValue(self, target: Windows.Win32.System.WinRT.IInspectable_head, value: Windows.Win32.System.WinRT.IInspectable_head, index: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(12)
    def get_CanWrite(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_CanRead(self) -> Boolean: ...
    Type = property(get_Type, None)
    Name = property(get_Name, None)
    CanWrite = property(get_CanWrite, None)
    CanRead = property(get_CanRead, None)
class ICustomPropertyProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ICustomPropertyProvider'
    _iid_ = Guid('{7c925755-3e48-42b4-8677-76372267033f}')
    @winrt_commethod(6)
    def GetCustomProperty(self, name: WinRT_String) -> Windows.UI.Xaml.Data.ICustomProperty: ...
    @winrt_commethod(7)
    def GetIndexedProperty(self, name: WinRT_String, type: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.Data.ICustomProperty: ...
    @winrt_commethod(8)
    def GetStringRepresentation(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Type(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    Type = property(get_Type, None)
class IItemIndexRange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IItemIndexRange'
    _iid_ = Guid('{83b834be-0583-4a26-9b64-8bf4a2f65704}')
    @winrt_commethod(6)
    def get_FirstIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Length(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_LastIndex(self) -> Int32: ...
    FirstIndex = property(get_FirstIndex, None)
    Length = property(get_Length, None)
    LastIndex = property(get_LastIndex, None)
class IItemIndexRangeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IItemIndexRangeFactory'
    _iid_ = Guid('{86e2c440-2e7a-4c7d-a664-e8abf07bfc7e}')
    @winrt_commethod(6)
    def CreateInstance(self, firstIndex: Int32, length: UInt32, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.ItemIndexRange: ...
class IItemsRangeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IItemsRangeInfo'
    _iid_ = Guid('{f05f5665-71fd-45a2-be13-a081d294a68d}')
    @winrt_commethod(6)
    def RangesChanged(self, visibleRange: Windows.UI.Xaml.Data.ItemIndexRange, trackedItems: Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Data.ItemIndexRange]) -> Void: ...
class INotifyPropertyChanged(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.INotifyPropertyChanged'
    _iid_ = Guid('{cf75d69c-f2f4-486b-b302-bb4c09baebfa}')
    @winrt_commethod(6)
    def add_PropertyChanged(self, handler: Windows.UI.Xaml.Data.PropertyChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PropertyChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPropertyChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IPropertyChangedEventArgs'
    _iid_ = Guid('{4f33a9a0-5cf4-47a4-b16f-d7faaf17457e}')
    @winrt_commethod(6)
    def get_PropertyName(self) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class IPropertyChangedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IPropertyChangedEventArgsFactory'
    _iid_ = Guid('{6dcc9c03-e0c7-4eee-8ea9-37e3406eeb1c}')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.PropertyChangedEventArgs: ...
class IRelativeSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IRelativeSource'
    _iid_ = Guid('{2397ce84-2822-483a-b499-d0f031e06c6b}')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class IRelativeSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IRelativeSourceFactory'
    _iid_ = Guid('{ef8392cd-446e-4f93-aacb-9b1255577460}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.RelativeSource: ...
class ISelectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ISelectionInfo'
    _iid_ = Guid('{2e12ca86-e1ed-4245-be49-207e42aec524}')
    @winrt_commethod(6)
    def SelectRange(self, itemIndexRange: Windows.UI.Xaml.Data.ItemIndexRange) -> Void: ...
    @winrt_commethod(7)
    def DeselectRange(self, itemIndexRange: Windows.UI.Xaml.Data.ItemIndexRange) -> Void: ...
    @winrt_commethod(8)
    def IsSelected(self, index: Int32) -> Boolean: ...
    @winrt_commethod(9)
    def GetSelectedRanges(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Data.ItemIndexRange]: ...
class ISupportIncrementalLoading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.ISupportIncrementalLoading'
    _iid_ = Guid('{7f5ee992-7694-4e6c-a51b-e34bf43de743}')
    @winrt_commethod(6)
    def LoadMoreItemsAsync(self, count: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Data.LoadMoreItemsResult]: ...
    @winrt_commethod(7)
    def get_HasMoreItems(self) -> Boolean: ...
    HasMoreItems = property(get_HasMoreItems, None)
class IValueConverter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Data.IValueConverter'
    _iid_ = Guid('{e6f2fef0-0712-487f-b313-f300b8d79aa1}')
    @winrt_commethod(6)
    def Convert(self, value: Windows.Win32.System.WinRT.IInspectable_head, targetType: Windows.UI.Xaml.Interop.TypeName, parameter: Windows.Win32.System.WinRT.IInspectable_head, language: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def ConvertBack(self, value: Windows.Win32.System.WinRT.IInspectable_head, targetType: Windows.UI.Xaml.Interop.TypeName, parameter: Windows.Win32.System.WinRT.IInspectable_head, language: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class ItemIndexRange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Data.IItemIndexRange
    _classid_ = 'Windows.UI.Xaml.Data.ItemIndexRange'
    @winrt_mixinmethod
    def get_FirstIndex(self: Windows.UI.Xaml.Data.IItemIndexRange) -> Int32: ...
    @winrt_mixinmethod
    def get_Length(self: Windows.UI.Xaml.Data.IItemIndexRange) -> UInt32: ...
    @winrt_mixinmethod
    def get_LastIndex(self: Windows.UI.Xaml.Data.IItemIndexRange) -> Int32: ...
    FirstIndex = property(get_FirstIndex, None)
    Length = property(get_Length, None)
    LastIndex = property(get_LastIndex, None)
class LoadMoreItemsResult(EasyCastStructure):
    Count: UInt32
class PropertyChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Data.IPropertyChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Data.PropertyChangedEventArgs'
    @winrt_mixinmethod
    def get_PropertyName(self: Windows.UI.Xaml.Data.IPropertyChangedEventArgs) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class PropertyChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Data.PropertyChangedEventHandler'
    _iid_ = Guid('{50f19c16-0a22-4d8e-a089-1ea9951657d2}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Data.PropertyChangedEventArgs) -> Void: ...
class RelativeSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Data.IRelativeSource
    _classid_ = 'Windows.UI.Xaml.Data.RelativeSource'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Xaml.Data.IRelativeSource) -> Windows.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.UI.Xaml.Data.IRelativeSource, value: Windows.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
RelativeSourceMode = Int32
RelativeSourceMode_None: RelativeSourceMode = 0
RelativeSourceMode_TemplatedParent: RelativeSourceMode = 1
RelativeSourceMode_Self: RelativeSourceMode = 2
UpdateSourceTrigger = Int32
UpdateSourceTrigger_Default: UpdateSourceTrigger = 0
UpdateSourceTrigger_PropertyChanged: UpdateSourceTrigger = 1
UpdateSourceTrigger_Explicit: UpdateSourceTrigger = 2
UpdateSourceTrigger_LostFocus: UpdateSourceTrigger = 3
make_head(_module, 'Binding')
make_head(_module, 'BindingBase')
make_head(_module, 'BindingExpression')
make_head(_module, 'BindingExpressionBase')
make_head(_module, 'BindingOperations')
make_head(_module, 'CollectionViewSource')
make_head(_module, 'CurrentChangingEventArgs')
make_head(_module, 'CurrentChangingEventHandler')
make_head(_module, 'IBinding')
make_head(_module, 'IBinding2')
make_head(_module, 'IBindingBase')
make_head(_module, 'IBindingBaseFactory')
make_head(_module, 'IBindingExpression')
make_head(_module, 'IBindingExpressionBase')
make_head(_module, 'IBindingExpressionBaseFactory')
make_head(_module, 'IBindingExpressionFactory')
make_head(_module, 'IBindingFactory')
make_head(_module, 'IBindingOperations')
make_head(_module, 'IBindingOperationsStatics')
make_head(_module, 'ICollectionView')
make_head(_module, 'ICollectionViewFactory')
make_head(_module, 'ICollectionViewGroup')
make_head(_module, 'ICollectionViewSource')
make_head(_module, 'ICollectionViewSourceStatics')
make_head(_module, 'ICurrentChangingEventArgs')
make_head(_module, 'ICurrentChangingEventArgsFactory')
make_head(_module, 'ICustomProperty')
make_head(_module, 'ICustomPropertyProvider')
make_head(_module, 'IItemIndexRange')
make_head(_module, 'IItemIndexRangeFactory')
make_head(_module, 'IItemsRangeInfo')
make_head(_module, 'INotifyPropertyChanged')
make_head(_module, 'IPropertyChangedEventArgs')
make_head(_module, 'IPropertyChangedEventArgsFactory')
make_head(_module, 'IRelativeSource')
make_head(_module, 'IRelativeSourceFactory')
make_head(_module, 'ISelectionInfo')
make_head(_module, 'ISupportIncrementalLoading')
make_head(_module, 'IValueConverter')
make_head(_module, 'ItemIndexRange')
make_head(_module, 'LoadMoreItemsResult')
make_head(_module, 'PropertyChangedEventArgs')
make_head(_module, 'PropertyChangedEventHandler')
make_head(_module, 'RelativeSource')
