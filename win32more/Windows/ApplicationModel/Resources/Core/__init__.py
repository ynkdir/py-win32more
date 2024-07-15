from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Resources.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class INamedResource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.INamedResource'
    _iid_ = Guid('{1c98c219-0b13-4240-89a5-d495dc189a00}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Candidates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_commethod(8)
    def Resolve(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(9)
    def ResolveForContext(self, resourceContext: win32more.Windows.ApplicationModel.Resources.Core.ResourceContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(10)
    def ResolveAll(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_commethod(11)
    def ResolveAllForContext(self, resourceContext: win32more.Windows.ApplicationModel.Resources.Core.ResourceContext) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    Candidates = property(get_Candidates, None)
    Uri = property(get_Uri, None)
class IResourceCandidate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceCandidate'
    _iid_ = Guid('{af5207d9-c433-4764-b3fd-8fa6bfbcbadc}')
    @winrt_commethod(6)
    def get_Qualifiers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]: ...
    @winrt_commethod(7)
    def get_IsMatch(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsMatchAsDefault(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsDefault(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ValueAsString(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetValueAsFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(12)
    def GetQualifierValue(self, qualifierName: WinRT_String) -> WinRT_String: ...
    IsDefault = property(get_IsDefault, None)
    IsMatch = property(get_IsMatch, None)
    IsMatchAsDefault = property(get_IsMatchAsDefault, None)
    Qualifiers = property(get_Qualifiers, None)
    ValueAsString = property(get_ValueAsString, None)
class IResourceCandidate2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceCandidate2'
    _iid_ = Guid('{69e5b468-f6fc-4013-aaa2-d53f1757d3b5}')
    @winrt_commethod(6)
    def GetValueAsStreamAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
class IResourceCandidate3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceCandidate3'
    _iid_ = Guid('{08ae97f8-517a-4674-958c-4a3c7cd2cc6b}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidateKind: ...
    Kind = property(get_Kind, None)
class IResourceContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContext'
    _iid_ = Guid('{2fa22f4b-707e-4b27-ad0d-d0d8cd468fd2}')
    @winrt_commethod(6)
    def get_QualifierValues(self) -> win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(7)
    def Reset(self) -> Void: ...
    @winrt_commethod(8)
    def ResetQualifierValues(self, qualifierNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(9)
    def OverrideToMatch(self, result: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Void: ...
    @winrt_commethod(10)
    def Clone(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_commethod(11)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(12)
    def put_Languages(self, languages: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    Languages = property(get_Languages, put_Languages)
    QualifierValues = property(get_QualifierValues, None)
class IResourceContextStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics'
    _iid_ = Guid('{98be9d6c-6338-4b31-99df-b2b442f17149}')
    @winrt_commethod(6)
    def CreateMatchingContext(self, result: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
class IResourceContextStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics2'
    _iid_ = Guid('{41f752ef-12af-41b9-ab36-b1eb4b512460}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_commethod(7)
    def SetGlobalQualifierValue(self, key: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def ResetGlobalQualifierValues(self) -> Void: ...
    @winrt_commethod(9)
    def ResetGlobalQualifierValuesForSpecifiedQualifiers(self, qualifierNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(10)
    def GetForViewIndependentUse(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
class IResourceContextStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics3'
    _iid_ = Guid('{20cf492c-af0f-450b-9da6-106dd0c29a39}')
    @winrt_commethod(6)
    def SetGlobalQualifierValueWithPersistence(self, key: WinRT_String, value: WinRT_String, persistence: win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifierPersistence) -> Void: ...
class IResourceContextStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics4'
    _iid_ = Guid('{22eb9ccd-fb31-4bfa-b86b-df9d9d7bdc39}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: win32more.Windows.UI.UIContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
class IResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceManager'
    _iid_ = Guid('{f744d97b-9988-44fb-abd6-5378844cfa8b}')
    @winrt_commethod(6)
    def get_MainResourceMap(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_commethod(7)
    def get_AllResourceMaps(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_commethod(8)
    def get_DefaultContext(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_commethod(9)
    def LoadPriFiles(self, files: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageFile]) -> Void: ...
    @winrt_commethod(10)
    def UnloadPriFiles(self, files: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageFile]) -> Void: ...
    AllResourceMaps = property(get_AllResourceMaps, None)
    DefaultContext = property(get_DefaultContext, None)
    MainResourceMap = property(get_MainResourceMap, None)
class IResourceManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceManager2'
    _iid_ = Guid('{9d66fe6c-a4d7-4c23-9e85-675f304c252d}')
    @winrt_commethod(6)
    def GetAllNamedResourcesForPackage(self, packageName: WinRT_String, resourceLayoutInfo: win32more.Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.NamedResource]: ...
    @winrt_commethod(7)
    def GetAllSubtreesForPackage(self, packageName: WinRT_String, resourceLayoutInfo: win32more.Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
class IResourceManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceManagerStatics'
    _iid_ = Guid('{1cc0fdfc-69ee-4e43-9901-47f12687baf7}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceManager: ...
    @winrt_commethod(7)
    def IsResourceReference(self, resourceReference: WinRT_String) -> Boolean: ...
    Current = property(get_Current, None)
class IResourceMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceMap'
    _iid_ = Guid('{72284824-db8c-42f8-b08c-53ff357dad82}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def GetValue(self, resource: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(8)
    def GetValueForContext(self, resource: WinRT_String, context: win32more.Windows.ApplicationModel.Resources.Core.ResourceContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(9)
    def GetSubtree(self, reference: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    Uri = property(get_Uri, None)
class IResourceQualifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceQualifier'
    _iid_ = Guid('{785da5b2-4afd-4376-a888-c5f9a6b7a05c}')
    @winrt_commethod(6)
    def get_QualifierName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_QualifierValue(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsDefault(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsMatch(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Score(self) -> Double: ...
    IsDefault = property(get_IsDefault, None)
    IsMatch = property(get_IsMatch, None)
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
    Score = property(get_Score, None)
class NamedResource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Core.INamedResource
    _classid_ = 'Windows.ApplicationModel.Resources.Core.NamedResource'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Resources.Core.INamedResource) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Candidates(self: win32more.Windows.ApplicationModel.Resources.Core.INamedResource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_mixinmethod
    def Resolve(self: win32more.Windows.ApplicationModel.Resources.Core.INamedResource) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def ResolveForContext(self: win32more.Windows.ApplicationModel.Resources.Core.INamedResource, resourceContext: win32more.Windows.ApplicationModel.Resources.Core.ResourceContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def ResolveAll(self: win32more.Windows.ApplicationModel.Resources.Core.INamedResource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_mixinmethod
    def ResolveAllForContext(self: win32more.Windows.ApplicationModel.Resources.Core.INamedResource, resourceContext: win32more.Windows.ApplicationModel.Resources.Core.ResourceContext) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    Candidates = property(get_Candidates, None)
    Uri = property(get_Uri, None)
class ResourceCandidate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceCandidate'
    @winrt_mixinmethod
    def get_Qualifiers(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]: ...
    @winrt_mixinmethod
    def get_IsMatch(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMatchAsDefault(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDefault(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValueAsString(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetValueAsFileAsync(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetQualifierValue(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate, qualifierName: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetValueAsStreamAsync(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceCandidate3) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidateKind: ...
    IsDefault = property(get_IsDefault, None)
    IsMatch = property(get_IsMatch, None)
    IsMatchAsDefault = property(get_IsMatchAsDefault, None)
    Kind = property(get_Kind, None)
    Qualifiers = property(get_Qualifiers, None)
    ValueAsString = property(get_ValueAsString, None)
class ResourceCandidateKind(Enum, Int32):
    String = 0
    File = 1
    EmbeddedData = 2
class ResourceCandidateVectorView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]]
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceCandidateVectorView'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate], index: UInt32) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate], value: win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate], startIndex: UInt32, items: FillArray[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    Size = property(get_Size, None)
class ResourceContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceContext'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Resources.Core.ResourceContext.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_mixinmethod
    def get_QualifierValues(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext) -> win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext) -> Void: ...
    @winrt_mixinmethod
    def ResetQualifierValues(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext, qualifierNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def OverrideToMatch(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext, result: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Void: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def put_Languages(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceContext, languages: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics4, context: win32more.Windows.UI.UIContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_classmethod
    def SetGlobalQualifierValueWithPersistence(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics3, key: WinRT_String, value: WinRT_String, persistence: win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifierPersistence) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics2) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_classmethod
    def SetGlobalQualifierValue(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics2, key: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def ResetGlobalQualifierValues(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics2) -> Void: ...
    @winrt_classmethod
    def ResetGlobalQualifierValuesForSpecifiedQualifiers(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics2, qualifierNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_classmethod
    def GetForViewIndependentUse(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics2) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_classmethod
    def CreateMatchingContext(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceContextStatics, result: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    Languages = property(get_Languages, put_Languages)
    QualifierValues = property(get_QualifierValues, None)
class ResourceContextLanguagesVectorView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[WinRT_String]]
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceContextLanguagesVectorView'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], index: UInt32) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], value: WinRT_String, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], startIndex: UInt32, items: FillArray[WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.Collections.IIterator[WinRT_String]: ...
    Size = property(get_Size, None)
class ResourceLayoutInfo(Structure):
    MajorVersion: UInt32
    MinorVersion: UInt32
    ResourceSubtreeCount: UInt32
    NamedResourceCount: UInt32
    Checksum: Int32
class _ResourceManager_Meta_(ComPtr.__class__):
    pass
class ResourceManager(ComPtr, metaclass=_ResourceManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceManager'
    @winrt_mixinmethod
    def get_MainResourceMap(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_mixinmethod
    def get_AllResourceMaps(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_mixinmethod
    def get_DefaultContext(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_mixinmethod
    def LoadPriFiles(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager, files: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageFile]) -> Void: ...
    @winrt_mixinmethod
    def UnloadPriFiles(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager, files: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageFile]) -> Void: ...
    @winrt_mixinmethod
    def GetAllNamedResourcesForPackage(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager2, packageName: WinRT_String, resourceLayoutInfo: win32more.Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.NamedResource]: ...
    @winrt_mixinmethod
    def GetAllSubtreesForPackage(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceManager2, packageName: WinRT_String, resourceLayoutInfo: win32more.Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceManagerStatics) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceManager: ...
    @winrt_classmethod
    def IsResourceReference(cls: win32more.Windows.ApplicationModel.Resources.Core.IResourceManagerStatics, resourceReference: WinRT_String) -> Boolean: ...
    AllResourceMaps = property(get_AllResourceMaps, None)
    DefaultContext = property(get_DefaultContext, None)
    MainResourceMap = property(get_MainResourceMap, None)
    _ResourceManager_Meta_.Current = property(get_Current, None)
class ResourceMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]
    default_interface: win32more.Windows.ApplicationModel.Resources.Core.IResourceMap
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMap'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceMap) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetValue(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceMap, resource: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def GetValueForContext(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceMap, resource: WinRT_String, context: win32more.Windows.ApplicationModel.Resources.Core.ResourceContext) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def GetSubtree(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceMap, reference: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource], key: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.Core.NamedResource: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource], first: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource])) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]: ...
    Size = property(get_Size, None)
    Uri = property(get_Uri, None)
class ResourceMapIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMapIterator'
    @winrt_mixinmethod
    def get_Current(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]], items: FillArray[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.NamedResource]]) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class ResourceMapMapView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]
    default_interface: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMapMapView'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap], key: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap], first: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap])) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]: ...
    Size = property(get_Size, None)
class ResourceMapMapViewIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMapMapViewIterator'
    @winrt_mixinmethod
    def get_Current(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]], items: FillArray[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class ResourceQualifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Core.IResourceQualifier
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifier'
    @winrt_mixinmethod
    def get_QualifierName(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QualifierValue(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsDefault(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMatch(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> Boolean: ...
    @winrt_mixinmethod
    def get_Score(self: win32more.Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> Double: ...
    IsDefault = property(get_IsDefault, None)
    IsMatch = property(get_IsMatch, None)
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
    Score = property(get_Score, None)
class ResourceQualifierMapView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, WinRT_String]]
    default_interface: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifierMapView'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], first: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String])) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    Size = property(get_Size, None)
class ResourceQualifierObservableMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, WinRT_String]]
    default_interface: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifierObservableMap'
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String, value: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    Size = property(get_Size, None)
    MapChanged = event()
class ResourceQualifierPersistence(Enum, Int32):
    None_ = 0
    LocalMachine = 1
class ResourceQualifierVectorView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]]
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifierVectorView'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier], index: UInt32) -> win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier], value: win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier], startIndex: UInt32, items: FillArray[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.ApplicationModel.Resources.Core.ResourceQualifier]: ...
    Size = property(get_Size, None)


make_ready(__name__)
