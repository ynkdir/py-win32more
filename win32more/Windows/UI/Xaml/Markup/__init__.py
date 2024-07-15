from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.UI.Xaml.Markup
import win32more.Windows.Win32.System.WinRT
class IComponentConnector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IComponentConnector'
    _iid_ = Guid('{f6790987-e6e5-47f2-92c6-eccce4ba159a}')
    @winrt_commethod(6)
    def Connect(self, connectionId: Int32, target: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IComponentConnector2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IComponentConnector2'
    _iid_ = Guid('{dc8f368b-eccc-498e-b139-91142254d7ae}')
    @winrt_commethod(6)
    def GetBindingConnector(self, connectionId: Int32, target: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.Markup.IComponentConnector: ...
class IDataTemplateComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IDataTemplateComponent'
    _iid_ = Guid('{08429dc8-8ab0-4747-aa9a-feadfc8da8e1}')
    @winrt_commethod(6)
    def Recycle(self) -> Void: ...
    @winrt_commethod(7)
    def ProcessBindings(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, itemIndex: Int32, phase: Int32, nextPhase: POINTER(Int32)) -> Void: ...
class IMarkupExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IMarkupExtension'
    _iid_ = Guid('{1ee3416d-562b-486e-9ee5-0f0cbcc8048c}')
class IMarkupExtensionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IMarkupExtensionFactory'
    _iid_ = Guid('{65329c05-fb5a-4567-9d55-5cdfbada2739}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Markup.MarkupExtension: ...
class IMarkupExtensionOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IMarkupExtensionOverrides'
    _iid_ = Guid('{393779bf-b9c0-4ffb-a57f-58e7356e425f}')
    @winrt_commethod(6)
    def ProvideValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IXamlBinaryWriter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBinaryWriter'
    _iid_ = Guid('{829d2ad3-620a-46f6-845d-436a05927100}')
class IXamlBinaryWriterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBinaryWriterStatics'
    _iid_ = Guid('{0d8ed07a-9b82-4aa8-b68b-026f2de1cc86}')
    @winrt_commethod(6)
    def Write(self, inputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], outputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: win32more.Windows.UI.Xaml.Markup.IXamlMetadataProvider) -> win32more.Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class IXamlBindScopeDiagnostics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBindScopeDiagnostics'
    _iid_ = Guid('{f264a29d-bded-43aa-a5b0-26ac21a81eb8}')
    @winrt_commethod(6)
    def Disable(self, lineNumber: Int32, columnNumber: Int32) -> Void: ...
class IXamlBindingHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBindingHelper'
    _iid_ = Guid('{faa6fb06-8ab9-4ef7-8ae7-fbd30bbfd06d}')
class IXamlBindingHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlBindingHelperStatics'
    _iid_ = Guid('{f65cfb71-c80c-4ffa-86ee-558754ee336d}')
    @winrt_commethod(6)
    def get_DataTemplateComponentProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetDataTemplateComponent(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Markup.IDataTemplateComponent: ...
    @winrt_commethod(8)
    def SetDataTemplateComponent(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Markup.IDataTemplateComponent) -> Void: ...
    @winrt_commethod(9)
    def SuspendRendering(self, target: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def ResumeRendering(self, target: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(11)
    def ConvertValue(self, type: win32more.Windows.UI.Xaml.Interop.TypeName, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(12)
    def SetPropertyFromString(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def SetPropertyFromBoolean(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def SetPropertyFromChar16(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Char) -> Void: ...
    @winrt_commethod(15)
    def SetPropertyFromDateTime(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(16)
    def SetPropertyFromDouble(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Double) -> Void: ...
    @winrt_commethod(17)
    def SetPropertyFromInt32(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def SetPropertyFromUInt32(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def SetPropertyFromInt64(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Int64) -> Void: ...
    @winrt_commethod(20)
    def SetPropertyFromUInt64(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: UInt64) -> Void: ...
    @winrt_commethod(21)
    def SetPropertyFromSingle(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Single) -> Void: ...
    @winrt_commethod(22)
    def SetPropertyFromPoint(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(23)
    def SetPropertyFromRect(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(24)
    def SetPropertyFromSize(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(25)
    def SetPropertyFromTimeSpan(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(26)
    def SetPropertyFromByte(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Byte) -> Void: ...
    @winrt_commethod(27)
    def SetPropertyFromUri(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(28)
    def SetPropertyFromObject(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    DataTemplateComponentProperty = property(get_DataTemplateComponentProperty, None)
class IXamlMarkupHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMarkupHelper'
    _iid_ = Guid('{d0e6673c-5342-44ef-85a7-ed327a739d9a}')
class IXamlMarkupHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMarkupHelperStatics'
    _iid_ = Guid('{c9bc3725-f34f-445c-81a2-6b72a5e8f072}')
    @winrt_commethod(6)
    def UnloadObject(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
class IXamlMember(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_TargetType(self) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(11)
    def get_Type(self) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(12)
    def GetValue(self, instance: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def SetValue(self, instance: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    IsAttachable = property(get_IsAttachable, None)
    IsDependencyProperty = property(get_IsDependencyProperty, None)
    IsReadOnly = property(get_IsReadOnly, None)
    Name = property(get_Name, None)
    TargetType = property(get_TargetType, None)
    Type = property(get_Type, None)
class IXamlMetadataProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlMetadataProvider'
    _iid_ = Guid('{b3765d69-68a5-4b32-8861-fdb90c1f5836}')
    @winrt_commethod(6)
    def GetXamlType(self, type: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def GetXamlTypeByFullName(self, fullName: WinRT_String) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(8)
    def GetXmlnsDefinitions(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Markup.XmlnsDefinition]: ...
class IXamlReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlReader'
    _iid_ = Guid('{24374cf1-cceb-48bf-a514-41b0186f84c2}')
class IXamlReaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlReaderStatics'
    _iid_ = Guid('{9891c6bd-534f-4955-b85a-8a8dc0dca602}')
    @winrt_commethod(6)
    def Load(self, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def LoadWithInitialTemplateValidation(self, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IXamlType(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlType'
    _iid_ = Guid('{7920eab1-a2e5-479a-bd50-6cef3c0b4970}')
    @winrt_commethod(6)
    def get_BaseType(self) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def get_ContentProperty(self) -> win32more.Windows.UI.Xaml.Markup.IXamlMember: ...
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
    def get_ItemType(self) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(16)
    def get_KeyType(self) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(17)
    def get_UnderlyingType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(18)
    def ActivateInstance(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(19)
    def CreateFromString(self, value: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(20)
    def GetMember(self, name: WinRT_String) -> win32more.Windows.UI.Xaml.Markup.IXamlMember: ...
    @winrt_commethod(21)
    def AddToVector(self, instance: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(22)
    def AddToMap(self, instance: win32more.Windows.Win32.System.WinRT.IInspectable, key: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(23)
    def RunInitializer(self) -> Void: ...
    BaseType = property(get_BaseType, None)
    ContentProperty = property(get_ContentProperty, None)
    FullName = property(get_FullName, None)
    IsArray = property(get_IsArray, None)
    IsBindable = property(get_IsBindable, None)
    IsCollection = property(get_IsCollection, None)
    IsConstructible = property(get_IsConstructible, None)
    IsDictionary = property(get_IsDictionary, None)
    IsMarkupExtension = property(get_IsMarkupExtension, None)
    ItemType = property(get_ItemType, None)
    KeyType = property(get_KeyType, None)
    UnderlyingType = property(get_UnderlyingType, None)
class IXamlType2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Markup.IXamlType2'
    _iid_ = Guid('{9f0c6e3b-433b-56ad-8f69-78a4dd3e64f9}')
    @winrt_commethod(6)
    def get_BoxedType(self) -> win32more.Windows.UI.Xaml.Markup.IXamlType: ...
    BoxedType = property(get_BoxedType, None)
class MarkupExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Markup.IMarkupExtension
    _classid_ = 'Windows.UI.Xaml.Markup.MarkupExtension'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Markup.MarkupExtension.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Markup.IMarkupExtensionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Markup.MarkupExtension: ...
    @winrt_mixinmethod
    def ProvideValue(self: win32more.Windows.UI.Xaml.Markup.IMarkupExtensionOverrides) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class XamlBinaryWriter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Markup.IXamlBinaryWriter
    _classid_ = 'Windows.UI.Xaml.Markup.XamlBinaryWriter'
    @winrt_classmethod
    def Write(cls: win32more.Windows.UI.Xaml.Markup.IXamlBinaryWriterStatics, inputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], outputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: win32more.Windows.UI.Xaml.Markup.IXamlMetadataProvider) -> win32more.Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class XamlBinaryWriterErrorInformation(Structure):
    InputStreamIndex: UInt32
    LineNumber: UInt32
    LinePosition: UInt32
class _XamlBindingHelper_Meta_(ComPtr.__class__):
    pass
class XamlBindingHelper(ComPtr, metaclass=_XamlBindingHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelper
    _classid_ = 'Windows.UI.Xaml.Markup.XamlBindingHelper'
    @winrt_classmethod
    def get_DataTemplateComponentProperty(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetDataTemplateComponent(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Markup.IDataTemplateComponent: ...
    @winrt_classmethod
    def SetDataTemplateComponent(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Markup.IDataTemplateComponent) -> Void: ...
    @winrt_classmethod
    def SuspendRendering(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, target: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def ResumeRendering(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, target: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def ConvertValue(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, type: win32more.Windows.UI.Xaml.Interop.TypeName, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def SetPropertyFromString(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromBoolean(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Boolean) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromChar16(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Char) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromDateTime(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromDouble(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Double) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromInt32(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Int32) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUInt32(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: UInt32) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromInt64(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Int64) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUInt64(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: UInt64) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromSingle(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Single) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromPoint(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromRect(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromSize(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromTimeSpan(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromByte(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: Byte) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUri(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromObject(cls: win32more.Windows.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Windows.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    _XamlBindingHelper_Meta_.DataTemplateComponentProperty = property(get_DataTemplateComponentProperty, None)
class XamlMarkupHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Markup.IXamlMarkupHelper
    _classid_ = 'Windows.UI.Xaml.Markup.XamlMarkupHelper'
    @winrt_classmethod
    def UnloadObject(cls: win32more.Windows.UI.Xaml.Markup.IXamlMarkupHelperStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> Void: ...
class XamlReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Markup.IXamlReader
    _classid_ = 'Windows.UI.Xaml.Markup.XamlReader'
    @winrt_classmethod
    def Load(cls: win32more.Windows.UI.Xaml.Markup.IXamlReaderStatics, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def LoadWithInitialTemplateValidation(cls: win32more.Windows.UI.Xaml.Markup.IXamlReaderStatics, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class XmlnsDefinition(Structure):
    XmlNamespace: WinRT_String
    Namespace: WinRT_String


make_ready(__name__)
