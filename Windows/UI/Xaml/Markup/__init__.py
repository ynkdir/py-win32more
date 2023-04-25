from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import Windows.UI.Xaml
import Windows.UI.Xaml.Interop
import Windows.UI.Xaml.Markup
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IComponentConnector(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f6790987-e6e5-47f2-92-c6-ec-cc-e4-ba-15-9a')
    @winrt_commethod(6)
    def Connect(self, connectionId: Int32, target: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class IComponentConnector2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dc8f368b-eccc-498e-b1-39-91-14-22-54-d7-ae')
    @winrt_commethod(6)
    def GetBindingConnector(self, connectionId: Int32, target: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Markup.IComponentConnector: ...
class IDataTemplateComponent(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('08429dc8-8ab0-4747-aa-9a-fe-ad-fc-8d-a8-e1')
    @winrt_commethod(6)
    def Recycle(self) -> Void: ...
    @winrt_commethod(7)
    def ProcessBindings(self, item: Windows.Win32.System.WinRT.IInspectable_head, itemIndex: Int32, phase: Int32, nextPhase: POINTER(Int32)) -> Void: ...
class IMarkupExtension(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1ee3416d-562b-486e-9e-e5-0f-0c-bc-c8-04-8c')
class IMarkupExtensionFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('65329c05-fb5a-4567-9d-55-5c-df-ba-da-27-39')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Markup.MarkupExtension: ...
class IMarkupExtensionOverrides(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('393779bf-b9c0-4ffb-a5-7f-58-e7-35-6e-42-5f')
    @winrt_commethod(6)
    def ProvideValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IXamlBinaryWriter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('829d2ad3-620a-46f6-84-5d-43-6a-05-92-71-00')
class IXamlBinaryWriterStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0d8ed07a-9b82-4aa8-b6-8b-02-6f-2d-e1-cc-86')
    @winrt_commethod(6)
    def Write(self, inputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], outputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: Windows.UI.Xaml.Markup.IXamlMetadataProvider) -> Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class IXamlBindScopeDiagnostics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f264a29d-bded-43aa-a5-b0-26-ac-21-a8-1e-b8')
    @winrt_commethod(6)
    def Disable(self, lineNumber: Int32, columnNumber: Int32) -> Void: ...
class IXamlBindingHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('faa6fb06-8ab9-4ef7-8a-e7-fb-d3-0b-bf-d0-6d')
class IXamlBindingHelperStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f65cfb71-c80c-4ffa-86-ee-55-87-54-ee-33-6d')
    @winrt_commethod(6)
    def get_DataTemplateComponentProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetDataTemplateComponent(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Markup.IDataTemplateComponent: ...
    @winrt_commethod(8)
    def SetDataTemplateComponent(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Markup.IDataTemplateComponent) -> Void: ...
    @winrt_commethod(9)
    def SuspendRendering(self, target: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def ResumeRendering(self, target: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(11)
    def ConvertValue(self, type: Windows.UI.Xaml.Interop.TypeName, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(12)
    def SetPropertyFromString(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def SetPropertyFromBoolean(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def SetPropertyFromChar16(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Char) -> Void: ...
    @winrt_commethod(15)
    def SetPropertyFromDateTime(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(16)
    def SetPropertyFromDouble(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Double) -> Void: ...
    @winrt_commethod(17)
    def SetPropertyFromInt32(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def SetPropertyFromUInt32(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def SetPropertyFromInt64(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Int64) -> Void: ...
    @winrt_commethod(20)
    def SetPropertyFromUInt64(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: UInt64) -> Void: ...
    @winrt_commethod(21)
    def SetPropertyFromSingle(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Single) -> Void: ...
    @winrt_commethod(22)
    def SetPropertyFromPoint(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(23)
    def SetPropertyFromRect(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(24)
    def SetPropertyFromSize(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(25)
    def SetPropertyFromTimeSpan(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(26)
    def SetPropertyFromByte(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Byte) -> Void: ...
    @winrt_commethod(27)
    def SetPropertyFromUri(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(28)
    def SetPropertyFromObject(self, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    DataTemplateComponentProperty = property(get_DataTemplateComponentProperty, None)
class IXamlMarkupHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d0e6673c-5342-44ef-85-a7-ed-32-7a-73-9d-9a')
class IXamlMarkupHelperStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c9bc3725-f34f-445c-81-a2-6b-72-a5-e8-f0-72')
    @winrt_commethod(6)
    def UnloadObject(self, element: Windows.UI.Xaml.DependencyObject) -> Void: ...
class IXamlMember(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c541f58c-43a9-4216-b7-18-e0-b1-1b-14-e9-3e')
    @winrt_commethod(6)
    def get_IsAttachable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsDependencyProperty(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_TargetType(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(11)
    def get_Type(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(12)
    def GetValue(self, instance: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def SetValue(self, instance: Windows.Win32.System.WinRT.IInspectable_head, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    IsAttachable = property(get_IsAttachable, None)
    IsDependencyProperty = property(get_IsDependencyProperty, None)
    IsReadOnly = property(get_IsReadOnly, None)
    Name = property(get_Name, None)
    TargetType = property(get_TargetType, None)
    Type = property(get_Type, None)
class IXamlMetadataProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b3765d69-68a5-4b32-88-61-fd-b9-0c-1f-58-36')
    @winrt_commethod(6)
    def GetXamlType(self, type: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def GetXamlTypeByFullName(self, fullName: WinRT_String) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(8)
    def GetXmlnsDefinitions(self) -> POINTER(Windows.UI.Xaml.Markup.XmlnsDefinition_head): ...
class IXamlReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('24374cf1-cceb-48bf-a5-14-41-b0-18-6f-84-c2')
class IXamlReaderStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9891c6bd-534f-4955-b8-5a-8a-8d-c0-dc-a6-02')
    @winrt_commethod(6)
    def Load(self, xaml: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def LoadWithInitialTemplateValidation(self, xaml: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IXamlType(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7920eab1-a2e5-479a-bd-50-6c-ef-3c-0b-49-70')
    @winrt_commethod(6)
    def get_BaseType(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def get_ContentProperty(self) -> Windows.UI.Xaml.Markup.IXamlMember: ...
    @winrt_commethod(8)
    def get_FullName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_IsArray(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsCollection(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsConstructible(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDictionary(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsMarkupExtension(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsBindable(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_ItemType(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(16)
    def get_KeyType(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(17)
    def get_UnderlyingType(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(18)
    def ActivateInstance(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(19)
    def CreateFromString(self, value: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(20)
    def GetMember(self, name: WinRT_String) -> Windows.UI.Xaml.Markup.IXamlMember: ...
    @winrt_commethod(21)
    def AddToVector(self, instance: Windows.Win32.System.WinRT.IInspectable_head, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(22)
    def AddToMap(self, instance: Windows.Win32.System.WinRT.IInspectable_head, key: Windows.Win32.System.WinRT.IInspectable_head, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(23)
    def RunInitializer(self) -> Void: ...
    BaseType = property(get_BaseType, None)
    ContentProperty = property(get_ContentProperty, None)
    FullName = property(get_FullName, None)
    IsArray = property(get_IsArray, None)
    IsCollection = property(get_IsCollection, None)
    IsConstructible = property(get_IsConstructible, None)
    IsDictionary = property(get_IsDictionary, None)
    IsMarkupExtension = property(get_IsMarkupExtension, None)
    IsBindable = property(get_IsBindable, None)
    ItemType = property(get_ItemType, None)
    KeyType = property(get_KeyType, None)
    UnderlyingType = property(get_UnderlyingType, None)
class IXamlType2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9f0c6e3b-433b-56ad-8f-69-78-a4-dd-3e-64-f9')
    @winrt_commethod(6)
    def get_BoxedType(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    BoxedType = property(get_BoxedType, None)
class MarkupExtension(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_commethod(6)
    def ProvideValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class XamlBinaryWriter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Markup.XamlBinaryWriter'
    @winrt_classmethod
    def Write(cls: Windows.UI.Xaml.Markup.IXamlBinaryWriterStatics, inputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], outputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: Windows.UI.Xaml.Markup.IXamlMetadataProvider) -> Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class XamlBinaryWriterErrorInformation(EasyCastStructure):
    InputStreamIndex: UInt32
    LineNumber: UInt32
    LinePosition: UInt32
class XamlBindingHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Markup.XamlBindingHelper'
    @winrt_classmethod
    def get_DataTemplateComponentProperty(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetDataTemplateComponent(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Markup.IDataTemplateComponent: ...
    @winrt_classmethod
    def SetDataTemplateComponent(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Markup.IDataTemplateComponent) -> Void: ...
    @winrt_classmethod
    def SuspendRendering(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, target: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def ResumeRendering(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, target: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def ConvertValue(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, type: Windows.UI.Xaml.Interop.TypeName, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def SetPropertyFromString(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromBoolean(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Boolean) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromChar16(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Char) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromDateTime(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromDouble(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Double) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromInt32(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Int32) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUInt32(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: UInt32) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromInt64(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Int64) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUInt64(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: UInt64) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromSingle(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Single) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromPoint(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromRect(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromSize(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromTimeSpan(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromByte(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Byte) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUri(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromObject(cls: Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: Windows.Win32.System.WinRT.IInspectable_head, propertyToSet: Windows.UI.Xaml.DependencyProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    DataTemplateComponentProperty = property(get_DataTemplateComponentProperty, None)
class XamlMarkupHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Markup.XamlMarkupHelper'
    @winrt_classmethod
    def UnloadObject(cls: Windows.UI.Xaml.Markup.IXamlMarkupHelperStatics, element: Windows.UI.Xaml.DependencyObject) -> Void: ...
class XamlReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Markup.XamlReader'
    @winrt_classmethod
    def Load(cls: Windows.UI.Xaml.Markup.IXamlReaderStatics, xaml: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def LoadWithInitialTemplateValidation(cls: Windows.UI.Xaml.Markup.IXamlReaderStatics, xaml: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class XmlnsDefinition(EasyCastStructure):
    XmlNamespace: WinRT_String
    Namespace: WinRT_String
make_head(_module, 'IComponentConnector')
make_head(_module, 'IComponentConnector2')
make_head(_module, 'IDataTemplateComponent')
make_head(_module, 'IMarkupExtension')
make_head(_module, 'IMarkupExtensionFactory')
make_head(_module, 'IMarkupExtensionOverrides')
make_head(_module, 'IXamlBinaryWriter')
make_head(_module, 'IXamlBinaryWriterStatics')
make_head(_module, 'IXamlBindScopeDiagnostics')
make_head(_module, 'IXamlBindingHelper')
make_head(_module, 'IXamlBindingHelperStatics')
make_head(_module, 'IXamlMarkupHelper')
make_head(_module, 'IXamlMarkupHelperStatics')
make_head(_module, 'IXamlMember')
make_head(_module, 'IXamlMetadataProvider')
make_head(_module, 'IXamlReader')
make_head(_module, 'IXamlReaderStatics')
make_head(_module, 'IXamlType')
make_head(_module, 'IXamlType2')
make_head(_module, 'MarkupExtension')
make_head(_module, 'XamlBinaryWriter')
make_head(_module, 'XamlBinaryWriterErrorInformation')
make_head(_module, 'XamlBindingHelper')
make_head(_module, 'XamlMarkupHelper')
make_head(_module, 'XamlReader')
make_head(_module, 'XmlnsDefinition')
