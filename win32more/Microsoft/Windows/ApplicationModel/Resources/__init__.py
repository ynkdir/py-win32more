from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.ApplicationModel.Resources
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IKnownResourceQualifierNameStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics'
    _iid_ = Guid('{dd6cdedc-559b-50c8-ac53-82fe21f915f3}')
    @winrt_commethod(6)
    def get_Contrast(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Custom(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DeviceFamily(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_HomeRegion(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_LayoutDirection(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Scale(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_TargetSize(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Theme(self) -> WinRT_String: ...
    Contrast = property(get_Contrast, None)
    Custom = property(get_Custom, None)
    DeviceFamily = property(get_DeviceFamily, None)
    HomeRegion = property(get_HomeRegion, None)
    Language = property(get_Language, None)
    LayoutDirection = property(get_LayoutDirection, None)
    Scale = property(get_Scale, None)
    TargetSize = property(get_TargetSize, None)
    Theme = property(get_Theme, None)
class IResourceCandidate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceCandidate'
    _iid_ = Guid('{6c54bc0c-ef1e-57b8-b478-34fece737356}')
    @winrt_commethod(6)
    def get_ValueAsString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ValueAsBytes(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidateKind: ...
    @winrt_commethod(9)
    def get_QualifierValues(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    Kind = property(get_Kind, None)
    QualifierValues = property(get_QualifierValues, None)
    ValueAsBytes = property(get_ValueAsBytes, None)
    ValueAsString = property(get_ValueAsString, None)
class IResourceCandidateFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceCandidateFactory'
    _iid_ = Guid('{bb2b30f8-c19b-5f43-88d9-69ad728a32f4}')
    @winrt_commethod(6)
    def CreateInstance(self, kind: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidateKind, data: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_commethod(7)
    def CreateInstance2(self, data: PassArray[Byte]) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
class IResourceContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceContext'
    _iid_ = Guid('{96fb48dc-f77d-55ff-af12-34861e3d4939}')
    @winrt_commethod(6)
    def get_QualifierValues(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    QualifierValues = property(get_QualifierValues, None)
class IResourceContext2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceContext2'
    _iid_ = Guid('{7a3b1158-798c-5949-969d-03510b9ce6ca}')
class IResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceLoader'
    _iid_ = Guid('{bc3f76bf-da46-54cd-8715-8b8aaf16eaac}')
    @winrt_commethod(6)
    def GetString(self, resourceId: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetStringForUri(self, resourceUri: win32more.Windows.Foundation.Uri) -> WinRT_String: ...
class IResourceLoaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceLoaderFactory'
    _iid_ = Guid('{871f83aa-fb34-50d6-b9b9-2c35f3ffc004}')
    @winrt_commethod(6)
    def CreateInstance(self, fileName: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(7)
    def CreateInstance2(self, fileName: WinRT_String, resourceMap: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceLoaderStatics'
    _iid_ = Guid('{ec9c894a-1466-5f2f-8eee-a70cbd2b51bb}')
    @winrt_commethod(6)
    def GetDefaultResourceFilePath(self) -> WinRT_String: ...
class IResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceManager'
    _iid_ = Guid('{ac2291ef-81be-5c99-a0ae-bcee0180b8a8}')
    @winrt_commethod(6)
    def get_MainResourceMap(self) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceMap: ...
    @winrt_commethod(7)
    def CreateResourceContext(self) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext: ...
    @winrt_commethod(8)
    def add_ResourceNotFound(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager, win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceNotFoundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ResourceNotFound(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MainResourceMap = property(get_MainResourceMap, None)
    ResourceNotFound = event()
class IResourceManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceManager2'
    _iid_ = Guid('{7ec10160-a154-5c42-8268-30e306b1f585}')
class IResourceManagerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceManagerFactory'
    _iid_ = Guid('{d6acf18f-458a-535b-a5c4-ac2dc4e49099}')
    @winrt_commethod(6)
    def CreateInstance(self, fileName: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager: ...
class IResourceMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceMap'
    _iid_ = Guid('{4abbd9bc-df4e-5c7b-812c-7e7bb0c22377}')
    @winrt_commethod(6)
    def get_ResourceCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def GetSubtree(self, reference: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceMap: ...
    @winrt_commethod(8)
    def TryGetSubtree(self, reference: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceMap: ...
    @winrt_commethod(9)
    def GetValue(self, resource: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_commethod(10)
    def GetValueWithContext(self, resource: WinRT_String, context: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_commethod(11)
    def GetValueByIndex(self, index: UInt32) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate]: ...
    @winrt_commethod(12)
    def GetValueByIndexWithContext(self, index: UInt32, context: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate]: ...
    @winrt_commethod(13)
    def TryGetValue(self, resource: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_commethod(14)
    def TryGetValueWithContext(self, resource: WinRT_String, context: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    ResourceCount = property(get_ResourceCount, None)
class IResourceNotFoundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.IResourceNotFoundEventArgs'
    _iid_ = Guid('{64abb08b-e77d-5b26-830f-15941e0e8200}')
    @winrt_commethod(6)
    def get_Context(self) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetResolvedCandidate(self, candidate: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate) -> Void: ...
    Context = property(get_Context, None)
    Name = property(get_Name, None)
class _KnownResourceQualifierName_Meta_(ComPtr.__class__):
    pass
class KnownResourceQualifierName(ComPtr, metaclass=_KnownResourceQualifierName_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.KnownResourceQualifierName'
    @winrt_classmethod
    def get_Contrast(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Custom(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DeviceFamily(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HomeRegion(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Language(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_LayoutDirection(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Scale(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TargetSize(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Theme(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IKnownResourceQualifierNameStatics) -> WinRT_String: ...
    _KnownResourceQualifierName_Meta_.Contrast = property(get_Contrast, None)
    _KnownResourceQualifierName_Meta_.Custom = property(get_Custom, None)
    _KnownResourceQualifierName_Meta_.DeviceFamily = property(get_DeviceFamily, None)
    _KnownResourceQualifierName_Meta_.HomeRegion = property(get_HomeRegion, None)
    _KnownResourceQualifierName_Meta_.Language = property(get_Language, None)
    _KnownResourceQualifierName_Meta_.LayoutDirection = property(get_LayoutDirection, None)
    _KnownResourceQualifierName_Meta_.Scale = property(get_Scale, None)
    _KnownResourceQualifierName_Meta_.TargetSize = property(get_TargetSize, None)
    _KnownResourceQualifierName_Meta_.Theme = property(get_Theme, None)
MrtCoreContract: UInt32 = 131072
class ResourceCandidate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidate
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate.CreateInstance2(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidateFactory, data: PassArray[Byte]) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidateFactory, kind: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidateKind, data: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_mixinmethod
    def get_ValueAsString(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ValueAsBytes(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidate) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidate) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidateKind: ...
    @winrt_mixinmethod
    def get_QualifierValues(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceCandidate) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    Kind = property(get_Kind, None)
    QualifierValues = property(get_QualifierValues, None)
    ValueAsBytes = property(get_ValueAsBytes, None)
    ValueAsString = property(get_ValueAsString, None)
class ResourceCandidateKind(Enum, Int32):
    Unknown = 0
    String = 1
    FilePath = 2
    EmbeddedData = 3
class ResourceContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceContext
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.ResourceContext'
    @winrt_mixinmethod
    def get_QualifierValues(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceContext) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    QualifierValues = property(get_QualifierValues, None)
class ResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceLoader
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.ResourceLoader'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceLoaderFactory, fileName: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceLoaderFactory, fileName: WinRT_String, resourceMap: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_mixinmethod
    def GetString(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceLoader, resourceId: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetStringForUri(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceLoader, resourceUri: win32more.Windows.Foundation.Uri) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultResourceFilePath(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceLoaderStatics) -> WinRT_String: ...
class ResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceManager
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.ResourceManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceManagerFactory, fileName: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager: ...
    @winrt_mixinmethod
    def get_MainResourceMap(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceManager) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceMap: ...
    @winrt_mixinmethod
    def CreateResourceContext(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceManager) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext: ...
    @winrt_mixinmethod
    def add_ResourceNotFound(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceManager, win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceNotFoundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResourceNotFound(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MainResourceMap = property(get_MainResourceMap, None)
    ResourceNotFound = event()
class ResourceMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.ResourceMap'
    @winrt_mixinmethod
    def get_ResourceCount(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap) -> UInt32: ...
    @winrt_mixinmethod
    def GetSubtree(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, reference: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceMap: ...
    @winrt_mixinmethod
    def TryGetSubtree(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, reference: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceMap: ...
    @winrt_mixinmethod
    def GetValue(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, resource: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_mixinmethod
    def GetValueWithContext(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, resource: WinRT_String, context: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_mixinmethod
    def GetValueByIndex(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, index: UInt32) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate]: ...
    @winrt_mixinmethod
    def GetValueByIndexWithContext(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, index: UInt32, context: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate]: ...
    @winrt_mixinmethod
    def TryGetValue(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, resource: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    @winrt_mixinmethod
    def TryGetValueWithContext(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceMap, resource: WinRT_String, context: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate: ...
    ResourceCount = property(get_ResourceCount, None)
class ResourceNotFoundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceNotFoundEventArgs
    _classid_ = 'Microsoft.Windows.ApplicationModel.Resources.ResourceNotFoundEventArgs'
    @winrt_mixinmethod
    def get_Context(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceNotFoundEventArgs) -> win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceContext: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceNotFoundEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetResolvedCandidate(self: win32more.Microsoft.Windows.ApplicationModel.Resources.IResourceNotFoundEventArgs, candidate: win32more.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidate) -> Void: ...
    Context = property(get_Context, None)
    Name = property(get_Name, None)


make_ready(__name__)
