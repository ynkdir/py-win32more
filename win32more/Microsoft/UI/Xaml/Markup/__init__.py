from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Markup
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.Win32.System.WinRT
class IComponentConnector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IComponentConnector'
    _iid_ = Guid('{ad401812-b091-51d0-b915-2d682cd2af10}')
    @winrt_commethod(6)
    def Connect(self, connectionId: Int32, target: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def GetBindingConnector(self, connectionId: Int32, target: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Markup.IComponentConnector: ...
class IDataTemplateComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IDataTemplateComponent'
    _iid_ = Guid('{1743ddf7-38ba-58c9-a2a6-b0ae28713bee}')
    @winrt_commethod(6)
    def Recycle(self) -> Void: ...
    @winrt_commethod(7)
    def ProcessBindings(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, itemIndex: Int32, phase: Int32, nextPhase: POINTER(Int32)) -> Void: ...
class IMarkupExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IMarkupExtension'
    _iid_ = Guid('{c355371e-091d-5136-af4a-baf5e00616bd}')
class IMarkupExtensionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IMarkupExtensionFactory'
    _iid_ = Guid('{20651afa-5f3a-5f0c-adb1-b6551f53a6a0}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Markup.MarkupExtension: ...
class IMarkupExtensionOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IMarkupExtensionOverrides'
    _iid_ = Guid('{a12aa575-5d31-5b68-a30f-8495412a351d}')
    @winrt_commethod(6)
    def ProvideValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def ProvideValueWithIXamlServiceProvider(self, serviceProvider: win32more.Microsoft.UI.Xaml.IXamlServiceProvider) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IProvideValueTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IProvideValueTarget'
    _iid_ = Guid('{3f01ff68-3efd-591d-a506-de13fcaabd83}')
    @winrt_commethod(6)
    def get_TargetObject(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_TargetProperty(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    TargetObject = property(get_TargetObject, None)
    TargetProperty = property(get_TargetProperty, None)
class IProvideValueTargetProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IProvideValueTargetProperty'
    _iid_ = Guid('{ce777b1f-b42e-59d1-870d-12fdf0629133}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Type(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(8)
    def get_DeclaringType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    DeclaringType = property(get_DeclaringType, None)
    Name = property(get_Name, None)
    Type = property(get_Type, None)
class IRootObjectProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IRootObjectProvider'
    _iid_ = Guid('{13d63599-352f-5eb8-81c1-bc62fb12d6da}')
    @winrt_commethod(6)
    def get_RootObject(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    RootObject = property(get_RootObject, None)
class IUriContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IUriContext'
    _iid_ = Guid('{fb8605f6-8f05-52ee-a01c-3a9e118a6ea2}')
    @winrt_commethod(6)
    def get_BaseUri(self) -> win32more.Windows.Foundation.Uri: ...
    BaseUri = property(get_BaseUri, None)
class IXamlBinaryWriter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlBinaryWriter'
    _iid_ = Guid('{8fb45e3b-e689-55bf-aa11-d83b1c1cdda1}')
class IXamlBinaryWriterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlBinaryWriterStatics'
    _iid_ = Guid('{774907fc-c846-517f-abcc-c3f7e8c3ffc9}')
    @winrt_commethod(6)
    def Write(self, inputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], outputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider) -> win32more.Microsoft.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class IXamlBindScopeDiagnostics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlBindScopeDiagnostics'
    _iid_ = Guid('{3ea84e4e-fdfe-55a8-a561-edf5697846d7}')
    @winrt_commethod(6)
    def Disable(self, lineNumber: Int32, columnNumber: Int32) -> Void: ...
class IXamlBindingHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlBindingHelper'
    _iid_ = Guid('{607a9bf2-5a6d-5c89-a756-bb44f24f28f8}')
class IXamlBindingHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics'
    _iid_ = Guid('{93c7dad3-f9c2-5372-84dc-9e9c4661d083}')
    @winrt_commethod(6)
    def get_DataTemplateComponentProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetDataTemplateComponent(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Markup.IDataTemplateComponent: ...
    @winrt_commethod(8)
    def SetDataTemplateComponent(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Markup.IDataTemplateComponent) -> Void: ...
    @winrt_commethod(9)
    def SuspendRendering(self, target: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(10)
    def ResumeRendering(self, target: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(11)
    def ConvertValue(self, type: win32more.Windows.UI.Xaml.Interop.TypeName, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(12)
    def SetPropertyFromString(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def SetPropertyFromBoolean(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def SetPropertyFromChar16(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Char) -> Void: ...
    @winrt_commethod(15)
    def SetPropertyFromDateTime(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(16)
    def SetPropertyFromDouble(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Double) -> Void: ...
    @winrt_commethod(17)
    def SetPropertyFromInt32(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def SetPropertyFromUInt32(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def SetPropertyFromInt64(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Int64) -> Void: ...
    @winrt_commethod(20)
    def SetPropertyFromUInt64(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: UInt64) -> Void: ...
    @winrt_commethod(21)
    def SetPropertyFromSingle(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Single) -> Void: ...
    @winrt_commethod(22)
    def SetPropertyFromPoint(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(23)
    def SetPropertyFromRect(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(24)
    def SetPropertyFromSize(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(25)
    def SetPropertyFromTimeSpan(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(26)
    def SetPropertyFromByte(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Byte) -> Void: ...
    @winrt_commethod(27)
    def SetPropertyFromUri(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(28)
    def SetPropertyFromObject(self, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    DataTemplateComponentProperty = property(get_DataTemplateComponentProperty, None)
class IXamlMarkupHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlMarkupHelper'
    _iid_ = Guid('{cd677310-3b06-5a13-b31a-401849570858}')
class IXamlMarkupHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlMarkupHelperStatics'
    _iid_ = Guid('{d9a0f6e3-c6cc-5cb6-8999-85788701f339}')
    @winrt_commethod(6)
    def UnloadObject(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
class IXamlMember(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlMember'
    _iid_ = Guid('{bf3a2913-5c63-50ec-8660-61809be7b9b9}')
    @winrt_commethod(6)
    def get_IsAttachable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsDependencyProperty(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_TargetType(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(11)
    def get_Type(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlMetadataProvider'
    _iid_ = Guid('{a96251f0-2214-5d53-8746-ce99a2593cd7}')
    @winrt_commethod(6)
    def GetXamlType(self, type: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def GetXamlTypeByFullName(self, fullName: WinRT_String) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(8)
    def GetXmlnsDefinitions(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Markup.XmlnsDefinition]: ...
class IXamlReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlReader'
    _iid_ = Guid('{54ce54c8-38c6-50d9-ac98-4b03eddbde9f}')
class IXamlReaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlReaderStatics'
    _iid_ = Guid('{82a4cd9e-435e-5aeb-8c4f-300cece45cae}')
    @winrt_commethod(6)
    def Load(self, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def LoadWithInitialTemplateValidation(self, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IXamlType(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlType'
    _iid_ = Guid('{d24219df-7ec9-57f1-a27b-6af251d9c5bc}')
    @winrt_commethod(6)
    def get_BaseType(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(7)
    def get_ContentProperty(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlMember: ...
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
    def get_ItemType(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(16)
    def get_KeyType(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(17)
    def get_BoxedType(self) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_commethod(18)
    def get_UnderlyingType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(19)
    def ActivateInstance(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(20)
    def CreateFromString(self, value: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(21)
    def GetMember(self, name: WinRT_String) -> win32more.Microsoft.UI.Xaml.Markup.IXamlMember: ...
    @winrt_commethod(22)
    def AddToVector(self, instance: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(23)
    def AddToMap(self, instance: win32more.Windows.Win32.System.WinRT.IInspectable, key: win32more.Windows.Win32.System.WinRT.IInspectable, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(24)
    def RunInitializer(self) -> Void: ...
    BaseType = property(get_BaseType, None)
    BoxedType = property(get_BoxedType, None)
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
class IXamlTypeResolver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Markup.IXamlTypeResolver'
    _iid_ = Guid('{3fa15615-cacf-547f-b1ed-89dae8c67452}')
    @winrt_commethod(6)
    def Resolve(self, qualifiedTypeName: WinRT_String) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
class MarkupExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IMarkupExtension
    _classid_ = 'Microsoft.UI.Xaml.Markup.MarkupExtension'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Markup.MarkupExtension.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Markup.IMarkupExtensionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Markup.MarkupExtension: ...
    @winrt_mixinmethod
    def ProvideValue(self: win32more.Microsoft.UI.Xaml.Markup.IMarkupExtensionOverrides) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def ProvideValueWithIXamlServiceProvider(self: win32more.Microsoft.UI.Xaml.Markup.IMarkupExtensionOverrides, serviceProvider: win32more.Microsoft.UI.Xaml.IXamlServiceProvider) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class ProvideValueTargetProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IProvideValueTargetProperty
    _classid_ = 'Microsoft.UI.Xaml.Markup.ProvideValueTargetProperty'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Markup.ProvideValueTargetProperty.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Markup.ProvideValueTargetProperty: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.UI.Xaml.Markup.IProvideValueTargetProperty) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Microsoft.UI.Xaml.Markup.IProvideValueTargetProperty) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_DeclaringType(self: win32more.Microsoft.UI.Xaml.Markup.IProvideValueTargetProperty) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    DeclaringType = property(get_DeclaringType, None)
    Name = property(get_Name, None)
    Type = property(get_Type, None)
class XamlBinaryWriter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IXamlBinaryWriter
    _classid_ = 'Microsoft.UI.Xaml.Markup.XamlBinaryWriter'
    @winrt_classmethod
    def Write(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBinaryWriterStatics, inputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], outputStreams: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IRandomAccessStream], xamlMetadataProvider: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider) -> win32more.Microsoft.UI.Xaml.Markup.XamlBinaryWriterErrorInformation: ...
class XamlBinaryWriterErrorInformation(Structure):
    InputStreamIndex: UInt32
    LineNumber: UInt32
    LinePosition: UInt32
class _XamlBindingHelper_Meta_(ComPtr.__class__):
    pass
class XamlBindingHelper(ComPtr, metaclass=_XamlBindingHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelper
    _classid_ = 'Microsoft.UI.Xaml.Markup.XamlBindingHelper'
    @winrt_classmethod
    def get_DataTemplateComponentProperty(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetDataTemplateComponent(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Markup.IDataTemplateComponent: ...
    @winrt_classmethod
    def SetDataTemplateComponent(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Markup.IDataTemplateComponent) -> Void: ...
    @winrt_classmethod
    def SuspendRendering(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, target: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def ResumeRendering(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, target: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def ConvertValue(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, type: win32more.Windows.UI.Xaml.Interop.TypeName, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def SetPropertyFromString(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromBoolean(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Boolean) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromChar16(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Char) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromDateTime(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromDouble(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Double) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromInt32(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Int32) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUInt32(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: UInt32) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromInt64(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Int64) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUInt64(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: UInt64) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromSingle(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Single) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromPoint(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromRect(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromSize(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromTimeSpan(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromByte(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: Byte) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromUri(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def SetPropertyFromObject(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlBindingHelperStatics, dependencyObject: win32more.Windows.Win32.System.WinRT.IInspectable, propertyToSet: win32more.Microsoft.UI.Xaml.DependencyProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    _XamlBindingHelper_Meta_.DataTemplateComponentProperty = property(get_DataTemplateComponentProperty, None)
class XamlMarkupHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IXamlMarkupHelper
    _classid_ = 'Microsoft.UI.Xaml.Markup.XamlMarkupHelper'
    @winrt_classmethod
    def UnloadObject(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlMarkupHelperStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Void: ...
class XamlReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IXamlReader
    _classid_ = 'Microsoft.UI.Xaml.Markup.XamlReader'
    @winrt_classmethod
    def Load(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlReaderStatics, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def LoadWithInitialTemplateValidation(cls: win32more.Microsoft.UI.Xaml.Markup.IXamlReaderStatics, xaml: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class XmlnsDefinition(Structure):
    XmlNamespace: WinRT_String
    Namespace: WinRT_String


make_ready(__name__)
