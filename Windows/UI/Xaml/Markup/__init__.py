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
class IComponentConnector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IComponentConnector'
    _iid_ = Guid('{f6790987-e6e5-47f2-92c6-eccce4ba159a}')
    @winrt_commethod(6)
    def Connect(self, connectionId: Int32, target: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class IComponentConnector2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IComponentConnector2'
    _iid_ = Guid('{dc8f368b-eccc-498e-b139-91142254d7ae}')
    @winrt_commethod(6)
    def GetBindingConnector(self, connectionId: Int32, target: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Markup.IComponentConnector: ...
class IDataTemplateComponent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IDataTemplateComponent'
    _iid_ = Guid('{08429dc8-8ab0-4747-aa9a-feadfc8da8e1}')
    @winrt_commethod(6)
    def Recycle(self) -> Void: ...
    @winrt_commethod(7)
    def ProcessBindings(self, item: Windows.Win32.System.WinRT.IInspectable_head, itemIndex: Int32, phase: Int32, nextPhase: POINTER(Int32)) -> Void: ...
class IMarkupExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IMarkupExtension'
    _iid_ = Guid('{1ee3416d-562b-486e-9ee5-0f0cbcc8048c}')
class IMarkupExtensionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IMarkupExtensionFactory'
    _iid_ = Guid('{65329c05-fb5a-4567-9d55-5cdfbada2739}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Markup.MarkupExtension: ...
class IMarkupExtensionOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IMarkupExtensionOverrides'
    _iid_ = Guid('{393779bf-b9c0-4ffb-a57f-58e7356e425f}')
    @winrt_commethod(6)
    def ProvideValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IXamlBinaryWriter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBinaryWriter'
    _iid_ = Guid('{829d2ad3-620a-46f6-845d-436a05927100}')
class IXamlBinaryWriterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBinaryWriterStatics'
    _iid_ = Guid('{0d8ed07a-9b82-4aa8-b68b-026f2de1cc86}')
    @winrt_commethod(6)
    def Write(self, inputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], outputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: Windows.UI.Xaml.Markup.IXamlMetadataProvider) -> Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class IXamlBindScopeDiagnostics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBindScopeDiagnostics'
    _iid_ = Guid('{f264a29d-bded-43aa-a5b0-26ac21a81eb8}')
    @winrt_commethod(6)
    def Disable(self, lineNumber: Int32, columnNumber: Int32) -> Void: ...
class IXamlBindingHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBindingHelper'
    _iid_ = Guid('{faa6fb06-8ab9-4ef7-8ae7-fbd30bbfd06d}')
class IXamlBindingHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBindingHelperStatics'
    _iid_ = Guid('{f65cfb71-c80c-4ffa-86ee-558754ee336d}')
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
class IXamlMarkupHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMarkupHelper'
    _iid_ = Guid('{d0e6673c-5342-44ef-85a7-ed327a739d9a}')
class IXamlMarkupHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMarkupHelperStatics'
    _iid_ = Guid('{c9bc3725-f34f-445c-81a2-6b72a5e8f072}')
    @winrt_commethod(6)
    def UnloadObject(self, element: Windows.UI.Xaml.DependencyObject) -> Void: ...
class IXamlMember(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMember'
    _iid_ = Guid('{c541f58c-43a9-4216-b718-e0b11b14e93e}')
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
class IXamlMetadataProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMetadataProvider'
    _iid_ = Guid('{b3765d69-68a5-4b32-8861-fdb90c1f5836}')
    @winrt_commethod(6)
    def GetXamlType(self, type: Windows.UI.Xaml.Interop.TypeName) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def GetXamlTypeByFullName(self, fullName: WinRT_String) -> Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(8)
    def GetXmlnsDefinitions(self) -> POINTER(Windows.UI.Xaml.Markup.XmlnsDefinition_head): ...
class IXamlReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlReader'
    _iid_ = Guid('{24374cf1-cceb-48bf-a514-41b0186f84c2}')
class IXamlReaderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlReaderStatics'
    _iid_ = Guid('{9891c6bd-534f-4955-b85a-8a8dc0dca602}')
    @winrt_commethod(6)
    def Load(self, xaml: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def LoadWithInitialTemplateValidation(self, xaml: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IXamlType(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlType'
    _iid_ = Guid('{7920eab1-a2e5-479a-bd50-6cef3c0b4970}')
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
class IXamlType2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlType2'
    _iid_ = Guid('{9f0c6e3b-433b-56ad-8f69-78a4dd3e64f9}')
    @winrt_commethod(6)
    def get_BoxedType(self) -> Windows.UI.Xaml.Markup.IXamlType: ...
    BoxedType = property(get_BoxedType, None)
class MarkupExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Markup.IMarkupExtension
    _classid_ = 'Windows.UI.Xaml.Markup.MarkupExtension'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Markup.IMarkupExtensionFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Markup.MarkupExtension: ...
    @winrt_mixinmethod
    def ProvideValue(self: Windows.UI.Xaml.Markup.IMarkupExtensionOverrides) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class XamlBinaryWriter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Markup.IXamlBinaryWriter
    _classid_ = 'Windows.UI.Xaml.Markup.XamlBinaryWriter'
    @winrt_classmethod
    def Write(cls: Windows.UI.Xaml.Markup.IXamlBinaryWriterStatics, inputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], outputStreams: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: Windows.UI.Xaml.Markup.IXamlMetadataProvider) -> Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class XamlBinaryWriterErrorInformation(EasyCastStructure):
    InputStreamIndex: UInt32
    LineNumber: UInt32
    LinePosition: UInt32
class XamlBindingHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Markup.IXamlBindingHelper
    _classid_ = 'Windows.UI.Xaml.Markup.XamlBindingHelper'
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
class XamlMarkupHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Markup.IXamlMarkupHelper
    _classid_ = 'Windows.UI.Xaml.Markup.XamlMarkupHelper'
    @winrt_classmethod
    def UnloadObject(cls: Windows.UI.Xaml.Markup.IXamlMarkupHelperStatics, element: Windows.UI.Xaml.DependencyObject) -> Void: ...
class XamlReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Markup.IXamlReader
    _classid_ = 'Windows.UI.Xaml.Markup.XamlReader'
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
