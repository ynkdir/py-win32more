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
import Windows.ApplicationModel.Resources.Core
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import Windows.Storage.Streams
import Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class INamedResource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.INamedResource'
    _iid_ = Guid('{1c98c219-0b13-4240-89a5-d495dc189a00}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Candidates(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_commethod(8)
    def Resolve(self) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(9)
    def ResolveForContext(self, resourceContext: Windows.ApplicationModel.Resources.Core.ResourceContext) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(10)
    def ResolveAll(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_commethod(11)
    def ResolveAllForContext(self, resourceContext: Windows.ApplicationModel.Resources.Core.ResourceContext) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    Uri = property(get_Uri, None)
    Candidates = property(get_Candidates, None)
class IResourceCandidate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceCandidate'
    _iid_ = Guid('{af5207d9-c433-4764-b3fd-8fa6bfbcbadc}')
    @winrt_commethod(6)
    def get_Qualifiers(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier]: ...
    @winrt_commethod(7)
    def get_IsMatch(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsMatchAsDefault(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsDefault(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ValueAsString(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetValueAsFileAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(12)
    def GetQualifierValue(self, qualifierName: WinRT_String) -> WinRT_String: ...
    Qualifiers = property(get_Qualifiers, None)
    IsMatch = property(get_IsMatch, None)
    IsMatchAsDefault = property(get_IsMatchAsDefault, None)
    IsDefault = property(get_IsDefault, None)
    ValueAsString = property(get_ValueAsString, None)
class IResourceCandidate2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceCandidate2'
    _iid_ = Guid('{69e5b468-f6fc-4013-aaa2-d53f1757d3b5}')
    @winrt_commethod(6)
    def GetValueAsStreamAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
class IResourceCandidate3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceCandidate3'
    _iid_ = Guid('{08ae97f8-517a-4674-958c-4a3c7cd2cc6b}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.ApplicationModel.Resources.Core.ResourceCandidateKind: ...
    Kind = property(get_Kind, None)
class IResourceContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContext'
    _iid_ = Guid('{2fa22f4b-707e-4b27-ad0d-d0d8cd468fd2}')
    @winrt_commethod(6)
    def get_QualifierValues(self) -> Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(7)
    def Reset(self) -> Void: ...
    @winrt_commethod(8)
    def ResetQualifierValues(self, qualifierNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(9)
    def OverrideToMatch(self, result: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Void: ...
    @winrt_commethod(10)
    def Clone(self) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_commethod(11)
    def get_Languages(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(12)
    def put_Languages(self, languages: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    QualifierValues = property(get_QualifierValues, None)
    Languages = property(get_Languages, put_Languages)
class IResourceContextStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics'
    _iid_ = Guid('{98be9d6c-6338-4b31-99df-b2b442f17149}')
    @winrt_commethod(6)
    def CreateMatchingContext(self, result: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
class IResourceContextStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics2'
    _iid_ = Guid('{41f752ef-12af-41b9-ab36-b1eb4b512460}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_commethod(7)
    def SetGlobalQualifierValue(self, key: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def ResetGlobalQualifierValues(self) -> Void: ...
    @winrt_commethod(9)
    def ResetGlobalQualifierValuesForSpecifiedQualifiers(self, qualifierNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(10)
    def GetForViewIndependentUse(self) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
class IResourceContextStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics3'
    _iid_ = Guid('{20cf492c-af0f-450b-9da6-106dd0c29a39}')
    @winrt_commethod(6)
    def SetGlobalQualifierValueWithPersistence(self, key: WinRT_String, value: WinRT_String, persistence: Windows.ApplicationModel.Resources.Core.ResourceQualifierPersistence) -> Void: ...
class IResourceContextStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceContextStatics4'
    _iid_ = Guid('{22eb9ccd-fb31-4bfa-b86b-df9d9d7bdc39}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: Windows.UI.UIContext) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
class IResourceManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceManager'
    _iid_ = Guid('{f744d97b-9988-44fb-abd6-5378844cfa8b}')
    @winrt_commethod(6)
    def get_MainResourceMap(self) -> Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_commethod(7)
    def get_AllResourceMaps(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_commethod(8)
    def get_DefaultContext(self) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_commethod(9)
    def LoadPriFiles(self, files: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageFile]) -> Void: ...
    @winrt_commethod(10)
    def UnloadPriFiles(self, files: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageFile]) -> Void: ...
    MainResourceMap = property(get_MainResourceMap, None)
    AllResourceMaps = property(get_AllResourceMaps, None)
    DefaultContext = property(get_DefaultContext, None)
class IResourceManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceManager2'
    _iid_ = Guid('{9d66fe6c-a4d7-4c23-9e85-675f304c252d}')
    @winrt_commethod(6)
    def GetAllNamedResourcesForPackage(self, packageName: WinRT_String, resourceLayoutInfo: Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.NamedResource]: ...
    @winrt_commethod(7)
    def GetAllSubtreesForPackage(self, packageName: WinRT_String, resourceLayoutInfo: Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
class IResourceManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceManagerStatics'
    _iid_ = Guid('{1cc0fdfc-69ee-4e43-9901-47f12687baf7}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.ApplicationModel.Resources.Core.ResourceManager: ...
    @winrt_commethod(7)
    def IsResourceReference(self, resourceReference: WinRT_String) -> Boolean: ...
    Current = property(get_Current, None)
class IResourceMap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Core.IResourceMap'
    _iid_ = Guid('{72284824-db8c-42f8-b08c-53ff357dad82}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def GetValue(self, resource: WinRT_String) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(8)
    def GetValueForContext(self, resource: WinRT_String, context: Windows.ApplicationModel.Resources.Core.ResourceContext) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_commethod(9)
    def GetSubtree(self, reference: WinRT_String) -> Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    Uri = property(get_Uri, None)
class IResourceQualifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
    IsDefault = property(get_IsDefault, None)
    IsMatch = property(get_IsMatch, None)
    Score = property(get_Score, None)
class NamedResource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Core.INamedResource
    _classid_ = 'Windows.ApplicationModel.Resources.Core.NamedResource'
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Resources.Core.INamedResource) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Candidates(self: Windows.ApplicationModel.Resources.Core.INamedResource) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_mixinmethod
    def Resolve(self: Windows.ApplicationModel.Resources.Core.INamedResource) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def ResolveForContext(self: Windows.ApplicationModel.Resources.Core.INamedResource, resourceContext: Windows.ApplicationModel.Resources.Core.ResourceContext) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def ResolveAll(self: Windows.ApplicationModel.Resources.Core.INamedResource) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    @winrt_mixinmethod
    def ResolveAllForContext(self: Windows.ApplicationModel.Resources.Core.INamedResource, resourceContext: Windows.ApplicationModel.Resources.Core.ResourceContext) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    Uri = property(get_Uri, None)
    Candidates = property(get_Candidates, None)
class ResourceCandidate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Core.IResourceCandidate
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceCandidate'
    @winrt_mixinmethod
    def get_Qualifiers(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier]: ...
    @winrt_mixinmethod
    def get_IsMatch(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMatchAsDefault(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDefault(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValueAsString(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetValueAsFileAsync(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetQualifierValue(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate, qualifierName: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetValueAsStreamAsync(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate2) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Resources.Core.IResourceCandidate3) -> Windows.ApplicationModel.Resources.Core.ResourceCandidateKind: ...
    Qualifiers = property(get_Qualifiers, None)
    IsMatch = property(get_IsMatch, None)
    IsMatchAsDefault = property(get_IsMatchAsDefault, None)
    IsDefault = property(get_IsDefault, None)
    ValueAsString = property(get_ValueAsString, None)
    Kind = property(get_Kind, None)
ResourceCandidateKind = Int32
ResourceCandidateKind_String: ResourceCandidateKind = 0
ResourceCandidateKind_File: ResourceCandidateKind = 1
ResourceCandidateKind_EmbeddedData: ResourceCandidateKind = 2
class ResourceCandidateVectorView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceCandidateVectorView'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate], index: UInt32) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate], value: Windows.ApplicationModel.Resources.Core.ResourceCandidate, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceCandidate], startIndex: UInt32, items: POINTER(Windows.ApplicationModel.Resources.Core.ResourceCandidate)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Resources.Core.ResourceCandidate]) -> Windows.Foundation.Collections.IIterator[Windows.ApplicationModel.Resources.Core.ResourceCandidate]: ...
    Size = property(get_Size, None)
class ResourceContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Core.IResourceContext
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceContext'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_mixinmethod
    def get_QualifierValues(self: Windows.ApplicationModel.Resources.Core.IResourceContext) -> Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Reset(self: Windows.ApplicationModel.Resources.Core.IResourceContext) -> Void: ...
    @winrt_mixinmethod
    def ResetQualifierValues(self: Windows.ApplicationModel.Resources.Core.IResourceContext, qualifierNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def OverrideToMatch(self: Windows.ApplicationModel.Resources.Core.IResourceContext, result: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Void: ...
    @winrt_mixinmethod
    def Clone(self: Windows.ApplicationModel.Resources.Core.IResourceContext) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_mixinmethod
    def get_Languages(self: Windows.ApplicationModel.Resources.Core.IResourceContext) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def put_Languages(self: Windows.ApplicationModel.Resources.Core.IResourceContext, languages: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics4, context: Windows.UI.UIContext) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_classmethod
    def SetGlobalQualifierValueWithPersistence(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics3, key: WinRT_String, value: WinRT_String, persistence: Windows.ApplicationModel.Resources.Core.ResourceQualifierPersistence) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics2) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_classmethod
    def SetGlobalQualifierValue(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics2, key: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def ResetGlobalQualifierValues(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics2) -> Void: ...
    @winrt_classmethod
    def ResetGlobalQualifierValuesForSpecifiedQualifiers(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics2, qualifierNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_classmethod
    def GetForViewIndependentUse(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics2) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_classmethod
    def CreateMatchingContext(cls: Windows.ApplicationModel.Resources.Core.IResourceContextStatics, result: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    QualifierValues = property(get_QualifierValues, None)
    Languages = property(get_Languages, put_Languages)
class ResourceContextLanguagesVectorView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVectorView[WinRT_String]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceContextLanguagesVectorView'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[WinRT_String], index: UInt32) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[WinRT_String], value: WinRT_String, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[WinRT_String], startIndex: UInt32, items: POINTER(WinRT_String)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.Collections.IIterator[WinRT_String]: ...
    Size = property(get_Size, None)
class ResourceLayoutInfo(EasyCastStructure):
    MajorVersion: UInt32
    MinorVersion: UInt32
    ResourceSubtreeCount: UInt32
    NamedResourceCount: UInt32
    Checksum: Int32
class ResourceManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Core.IResourceManager
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceManager'
    @winrt_mixinmethod
    def get_MainResourceMap(self: Windows.ApplicationModel.Resources.Core.IResourceManager) -> Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_mixinmethod
    def get_AllResourceMaps(self: Windows.ApplicationModel.Resources.Core.IResourceManager) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_mixinmethod
    def get_DefaultContext(self: Windows.ApplicationModel.Resources.Core.IResourceManager) -> Windows.ApplicationModel.Resources.Core.ResourceContext: ...
    @winrt_mixinmethod
    def LoadPriFiles(self: Windows.ApplicationModel.Resources.Core.IResourceManager, files: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageFile]) -> Void: ...
    @winrt_mixinmethod
    def UnloadPriFiles(self: Windows.ApplicationModel.Resources.Core.IResourceManager, files: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageFile]) -> Void: ...
    @winrt_mixinmethod
    def GetAllNamedResourcesForPackage(self: Windows.ApplicationModel.Resources.Core.IResourceManager2, packageName: WinRT_String, resourceLayoutInfo: Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.NamedResource]: ...
    @winrt_mixinmethod
    def GetAllSubtreesForPackage(self: Windows.ApplicationModel.Resources.Core.IResourceManager2, packageName: WinRT_String, resourceLayoutInfo: Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.ApplicationModel.Resources.Core.IResourceManagerStatics) -> Windows.ApplicationModel.Resources.Core.ResourceManager: ...
    @winrt_classmethod
    def IsResourceReference(cls: Windows.ApplicationModel.Resources.Core.IResourceManagerStatics, resourceReference: WinRT_String) -> Boolean: ...
    MainResourceMap = property(get_MainResourceMap, None)
    AllResourceMaps = property(get_AllResourceMaps, None)
    DefaultContext = property(get_DefaultContext, None)
    Current = property(get_Current, None)
class ResourceMap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Core.IResourceMap
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMap'
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Resources.Core.IResourceMap) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetValue(self: Windows.ApplicationModel.Resources.Core.IResourceMap, resource: WinRT_String) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def GetValueForContext(self: Windows.ApplicationModel.Resources.Core.IResourceMap, resource: WinRT_String, context: Windows.ApplicationModel.Resources.Core.ResourceContext) -> Windows.ApplicationModel.Resources.Core.ResourceCandidate: ...
    @winrt_mixinmethod
    def GetSubtree(self: Windows.ApplicationModel.Resources.Core.IResourceMap, reference: WinRT_String) -> Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource], key: WinRT_String) -> Windows.ApplicationModel.Resources.Core.NamedResource: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource], first: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]), second: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource])) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]]: ...
    Uri = property(get_Uri, None)
    Size = property(get_Size, None)
class ResourceMapIterator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMapIterator'
    @winrt_mixinmethod
    def get_Current(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]]) -> Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource]], items: POINTER(Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.NamedResource])) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class ResourceMapMapView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMapMapView'
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap], key: WinRT_String) -> Windows.ApplicationModel.Resources.Core.ResourceMap: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap], first: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]), second: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap])) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]]: ...
    Size = property(get_Size, None)
class ResourceMapMapViewIterator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceMapMapViewIterator'
    @winrt_mixinmethod
    def get_Current(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap]], items: POINTER(Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.ApplicationModel.Resources.Core.ResourceMap])) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class ResourceQualifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Core.IResourceQualifier
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifier'
    @winrt_mixinmethod
    def get_QualifierName(self: Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QualifierValue(self: Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsDefault(self: Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMatch(self: Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> Boolean: ...
    @winrt_mixinmethod
    def get_Score(self: Windows.ApplicationModel.Resources.Core.IResourceQualifier) -> Double: ...
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
    IsDefault = property(get_IsDefault, None)
    IsMatch = property(get_IsMatch, None)
    Score = property(get_Score, None)
class ResourceQualifierMapView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifierMapView'
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], first: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]), second: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String])) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    Size = property(get_Size, None)
class ResourceQualifierObservableMap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifierObservableMap'
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, WinRT_String]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, WinRT_String], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String, value: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    Size = property(get_Size, None)
ResourceQualifierPersistence = Int32
ResourceQualifierPersistence_None: ResourceQualifierPersistence = 0
ResourceQualifierPersistence_LocalMachine: ResourceQualifierPersistence = 1
class ResourceQualifierVectorView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier]
    _classid_ = 'Windows.ApplicationModel.Resources.Core.ResourceQualifierVectorView'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier], index: UInt32) -> Windows.ApplicationModel.Resources.Core.ResourceQualifier: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier], value: Windows.ApplicationModel.Resources.Core.ResourceQualifier, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Core.ResourceQualifier], startIndex: UInt32, items: POINTER(Windows.ApplicationModel.Resources.Core.ResourceQualifier)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Resources.Core.ResourceQualifier]) -> Windows.Foundation.Collections.IIterator[Windows.ApplicationModel.Resources.Core.ResourceQualifier]: ...
    Size = property(get_Size, None)
make_head(_module, 'INamedResource')
make_head(_module, 'IResourceCandidate')
make_head(_module, 'IResourceCandidate2')
make_head(_module, 'IResourceCandidate3')
make_head(_module, 'IResourceContext')
make_head(_module, 'IResourceContextStatics')
make_head(_module, 'IResourceContextStatics2')
make_head(_module, 'IResourceContextStatics3')
make_head(_module, 'IResourceContextStatics4')
make_head(_module, 'IResourceManager')
make_head(_module, 'IResourceManager2')
make_head(_module, 'IResourceManagerStatics')
make_head(_module, 'IResourceMap')
make_head(_module, 'IResourceQualifier')
make_head(_module, 'NamedResource')
make_head(_module, 'ResourceCandidate')
make_head(_module, 'ResourceCandidateVectorView')
make_head(_module, 'ResourceContext')
make_head(_module, 'ResourceContextLanguagesVectorView')
make_head(_module, 'ResourceLayoutInfo')
make_head(_module, 'ResourceManager')
make_head(_module, 'ResourceMap')
make_head(_module, 'ResourceMapIterator')
make_head(_module, 'ResourceMapMapView')
make_head(_module, 'ResourceMapMapViewIterator')
make_head(_module, 'ResourceQualifier')
make_head(_module, 'ResourceQualifierMapView')
make_head(_module, 'ResourceQualifierObservableMap')
make_head(_module, 'ResourceQualifierVectorView')
