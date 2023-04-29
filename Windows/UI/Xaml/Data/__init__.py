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
    @winrt_commethod(30)
    def get_Path(self) -> Windows.UI.Xaml.PropertyPath: ...
    @winrt_commethod(31)
    def put_Path(self, value: Windows.UI.Xaml.PropertyPath) -> Void: ...
    @winrt_commethod(32)
    def get_Mode(self) -> Windows.UI.Xaml.Data.BindingMode: ...
    @winrt_commethod(33)
    def put_Mode(self, value: Windows.UI.Xaml.Data.BindingMode) -> Void: ...
    @winrt_commethod(34)
    def get_Source(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(35)
    def put_Source(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(36)
    def get_RelativeSource(self) -> Windows.UI.Xaml.Data.RelativeSource: ...
    @winrt_commethod(37)
    def put_RelativeSource(self, value: Windows.UI.Xaml.Data.RelativeSource) -> Void: ...
    @winrt_commethod(38)
    def get_ElementName(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def put_ElementName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(40)
    def get_Converter(self) -> Windows.UI.Xaml.Data.IValueConverter: ...
    @winrt_commethod(41)
    def put_Converter(self, value: Windows.UI.Xaml.Data.IValueConverter) -> Void: ...
    @winrt_commethod(42)
    def get_ConverterParameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(43)
    def put_ConverterParameter(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(44)
    def get_ConverterLanguage(self) -> WinRT_String: ...
    @winrt_commethod(45)
    def put_ConverterLanguage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(46)
    def get_FallbackValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(47)
    def put_FallbackValue(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(48)
    def get_TargetNullValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(49)
    def put_TargetNullValue(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(50)
    def get_UpdateSourceTrigger(self) -> Windows.UI.Xaml.Data.UpdateSourceTrigger: ...
    @winrt_commethod(51)
    def put_UpdateSourceTrigger(self, value: Windows.UI.Xaml.Data.UpdateSourceTrigger) -> Void: ...
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
class BindingExpression(ComPtr):
    extends: Windows.UI.Xaml.Data.BindingExpressionBase
    @winrt_commethod(9)
    def get_DataItem(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def get_ParentBinding(self) -> Windows.UI.Xaml.Data.Binding: ...
    @winrt_commethod(11)
    def UpdateSource(self) -> Void: ...
    DataItem = property(get_DataItem, None)
    ParentBinding = property(get_ParentBinding, None)
class BindingExpressionBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
BindingMode = Int32
BindingMode_OneWay: BindingMode = 1
BindingMode_OneTime: BindingMode = 2
BindingMode_TwoWay: BindingMode = 3
class BindingOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Data.BindingOperations'
    @winrt_classmethod
    def SetBinding(cls: Windows.UI.Xaml.Data.IBindingOperationsStatics, target: Windows.UI.Xaml.DependencyObject, dp: Windows.UI.Xaml.DependencyProperty, binding: Windows.UI.Xaml.Data.BindingBase) -> Void: ...
class CollectionViewSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Data.CollectionViewSource'
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
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsCancelable(self) -> Boolean: ...
    Cancel = property(get_Cancel, put_Cancel)
    IsCancelable = property(get_IsCancelable, None)
class CurrentChangingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f3888db8-139f-4dce-8d-c9-f7-f1-44-4d-11-85')
    ClassId = 'Windows.UI.Xaml.Data.CurrentChangingEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Data.CurrentChangingEventArgs) -> Void: ...
class IBinding(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3f7a0c6b-d00f-4730-8c-1d-48-e1-6c-46-f9-ca')
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
    Guid = Guid('34f96fcb-0406-48b3-9e-82-f3-33-ec-4c-69-10')
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
    Guid = Guid('1589a2ab-3d15-49bc-a4-47-8a-54-48-e5-88-70')
class IBindingBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('22dafc3a-7701-4666-a1-ba-98-59-bd-cf-ec-34')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.BindingBase: ...
class IBindingExpression(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('516a19a5-c2fd-4a9e-9f-d3-9a-a4-2f-99-5a-3c')
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
    Guid = Guid('fded3154-e954-4f67-8f-b6-6e-d7-9b-3a-1c-b3')
class IBindingExpressionBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ea7116a7-c2d9-4375-b4-71-66-b9-c4-8c-79-30')
class IBindingExpressionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1cb55cd9-db72-40b3-a2-b5-24-ee-6e-a5-c3-28')
class IBindingFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ff42bb08-c39e-4f7e-84-34-a1-56-90-83-88-3c')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.Binding: ...
class IBindingOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6fffd738-9839-419c-a1-7a-4b-36-04-e1-52-4e')
class IBindingOperationsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e155ef73-95a0-4aab-8c-7d-2a-47-da-07-3c-79')
    @winrt_commethod(6)
    def SetBinding(self, target: Windows.UI.Xaml.DependencyObject, dp: Windows.UI.Xaml.DependencyProperty, binding: Windows.UI.Xaml.Data.BindingBase) -> Void: ...
class ICollectionView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8be8bfe4-dbef-44df-81-26-a3-1a-89-12-1d-dc')
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
    Guid = Guid('34d4aaf4-8e72-4950-91-92-ec-d0-7d-39-9d-0a')
    @winrt_commethod(6)
    def CreateView(self) -> Windows.UI.Xaml.Data.ICollectionView: ...
class ICollectionViewGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e01b9d8-d7b5-48b6-b3-1c-5b-b5-bd-f5-f0-9b')
    @winrt_commethod(6)
    def get_Group(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_GroupItems(self) -> Windows.Foundation.Collections.IObservableVector[Windows.Win32.System.WinRT.IInspectable_head]: ...
    Group = property(get_Group, None)
    GroupItems = property(get_GroupItems, None)
class ICollectionViewSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a66a1146-d2fb-4ead-be-9f-35-78-a4-66-dc-fe')
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
    Guid = Guid('173a0710-46af-4c0c-81-8b-21-b6-ef-81-bf-65')
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
    Guid = Guid('f9891e29-51cc-47dd-a5-b9-35-dc-49-14-af-69')
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
    Guid = Guid('153bbeee-62f3-48cf-81-83-8b-e2-6d-e3-a6-6e')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
    @winrt_commethod(7)
    def CreateWithCancelableParameter(self, isCancelable: Boolean, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.CurrentChangingEventArgs: ...
class ICustomProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('30da92c0-23e8-42a0-ae-7c-73-4a-0e-5d-27-82')
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
    Guid = Guid('7c925755-3e48-42b4-86-77-76-37-22-67-03-3f')
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
    Guid = Guid('83b834be-0583-4a26-9b-64-8b-f4-a2-f6-57-04')
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
    Guid = Guid('86e2c440-2e7a-4c7d-a6-64-e8-ab-f0-7b-fc-7e')
    @winrt_commethod(6)
    def CreateInstance(self, firstIndex: Int32, length: UInt32, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.ItemIndexRange: ...
class IItemsRangeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f05f5665-71fd-45a2-be-13-a0-81-d2-94-a6-8d')
    @winrt_commethod(6)
    def RangesChanged(self, visibleRange: Windows.UI.Xaml.Data.ItemIndexRange, trackedItems: Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Data.ItemIndexRange]) -> Void: ...
class INotifyPropertyChanged(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cf75d69c-f2f4-486b-b3-02-bb-4c-09-ba-eb-fa')
    @winrt_commethod(6)
    def add_PropertyChanged(self, handler: Windows.UI.Xaml.Data.PropertyChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PropertyChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPropertyChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4f33a9a0-5cf4-47a4-b1-6f-d7-fa-af-17-45-7e')
    @winrt_commethod(6)
    def get_PropertyName(self) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class IPropertyChangedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6dcc9c03-e0c7-4eee-8e-a9-37-e3-40-6e-eb-1c')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.PropertyChangedEventArgs: ...
class IRelativeSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2397ce84-2822-483a-b4-99-d0-f0-31-e0-6c-6b')
    @winrt_commethod(6)
    def get_Mode(self) -> Windows.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: Windows.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
    Mode = property(get_Mode, put_Mode)
class IRelativeSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef8392cd-446e-4f93-aa-cb-9b-12-55-57-74-60')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Data.RelativeSource: ...
class ISelectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2e12ca86-e1ed-4245-be-49-20-7e-42-ae-c5-24')
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
    Guid = Guid('7f5ee992-7694-4e6c-a5-1b-e3-4b-f4-3d-e7-43')
    @winrt_commethod(6)
    def LoadMoreItemsAsync(self, count: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Data.LoadMoreItemsResult]: ...
    @winrt_commethod(7)
    def get_HasMoreItems(self) -> Boolean: ...
    HasMoreItems = property(get_HasMoreItems, None)
class IValueConverter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e6f2fef0-0712-487f-b3-13-f3-00-b8-d7-9a-a1')
    @winrt_commethod(6)
    def Convert(self, value: Windows.Win32.System.WinRT.IInspectable_head, targetType: Windows.UI.Xaml.Interop.TypeName, parameter: Windows.Win32.System.WinRT.IInspectable_head, language: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def ConvertBack(self, value: Windows.Win32.System.WinRT.IInspectable_head, targetType: Windows.UI.Xaml.Interop.TypeName, parameter: Windows.Win32.System.WinRT.IInspectable_head, language: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class ItemIndexRange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_commethod(6)
    def get_FirstIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Length(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_LastIndex(self) -> Int32: ...
    FirstIndex = property(get_FirstIndex, None)
    Length = property(get_Length, None)
    LastIndex = property(get_LastIndex, None)
class LoadMoreItemsResult(EasyCastStructure):
    Count: UInt32
class PropertyChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_commethod(6)
    def get_PropertyName(self) -> WinRT_String: ...
    PropertyName = property(get_PropertyName, None)
class PropertyChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('50f19c16-0a22-4d8e-a0-89-1e-a9-95-16-57-d2')
    ClassId = 'Windows.UI.Xaml.Data.PropertyChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Data.PropertyChangedEventArgs) -> Void: ...
class RelativeSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(9)
    def get_Mode(self) -> Windows.UI.Xaml.Data.RelativeSourceMode: ...
    @winrt_commethod(10)
    def put_Mode(self, value: Windows.UI.Xaml.Data.RelativeSourceMode) -> Void: ...
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
