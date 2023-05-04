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
import Windows.ApplicationModel.Resources.Management
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IIndexedResourceCandidate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate'
    _iid_ = Guid('{0e619ef3-faec-4414-a9d7-54acd5953f29}')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.ApplicationModel.Resources.Management.IndexedResourceType: ...
    @winrt_commethod(7)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Metadata(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(9)
    def get_Qualifiers(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Management.IndexedResourceQualifier]: ...
    @winrt_commethod(10)
    def get_ValueAsString(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetQualifierValue(self, qualifierName: WinRT_String) -> WinRT_String: ...
    Type = property(get_Type, None)
    Uri = property(get_Uri, None)
    Metadata = property(get_Metadata, None)
    Qualifiers = property(get_Qualifiers, None)
    ValueAsString = property(get_ValueAsString, None)
class IIndexedResourceQualifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier'
    _iid_ = Guid('{dae3bb9b-d304-497f-a168-a340042c8adb}')
    @winrt_commethod(6)
    def get_QualifierName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_QualifierValue(self) -> WinRT_String: ...
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
class IResourceIndexer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IResourceIndexer'
    _iid_ = Guid('{2d4cf9a5-e32f-4ab2-8748-96350a016da3}')
    @winrt_commethod(6)
    def IndexFilePath(self, filePath: Windows.Foundation.Uri) -> Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate: ...
    @winrt_commethod(7)
    def IndexFileContentsAsync(self, file: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate]]: ...
class IResourceIndexerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory'
    _iid_ = Guid('{b8de3f09-31cd-4d97-bd30-8d39f742bc61}')
    @winrt_commethod(6)
    def CreateResourceIndexer(self, projectRoot: Windows.Foundation.Uri) -> Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
class IResourceIndexerFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory2'
    _iid_ = Guid('{6040f18d-d5e5-4b60-9201-cd279cbcfed9}')
    @winrt_commethod(6)
    def CreateResourceIndexerWithExtension(self, projectRoot: Windows.Foundation.Uri, extensionDllPath: Windows.Foundation.Uri) -> Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
class IndexedResourceCandidate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate'
    @winrt_mixinmethod
    def get_Type(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> Windows.ApplicationModel.Resources.Management.IndexedResourceType: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Metadata(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_Qualifiers(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Management.IndexedResourceQualifier]: ...
    @winrt_mixinmethod
    def get_ValueAsString(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetQualifierValue(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate, qualifierName: WinRT_String) -> WinRT_String: ...
    Type = property(get_Type, None)
    Uri = property(get_Uri, None)
    Metadata = property(get_Metadata, None)
    Qualifiers = property(get_Qualifiers, None)
    ValueAsString = property(get_ValueAsString, None)
class IndexedResourceQualifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IndexedResourceQualifier'
    @winrt_mixinmethod
    def get_QualifierName(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QualifierValue(self: Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier) -> WinRT_String: ...
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
IndexedResourceType = Int32
IndexedResourceType_String: IndexedResourceType = 0
IndexedResourceType_Path: IndexedResourceType = 1
IndexedResourceType_EmbeddedData: IndexedResourceType = 2
class ResourceIndexer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Resources.Management.IResourceIndexer
    _classid_ = 'Windows.ApplicationModel.Resources.Management.ResourceIndexer'
    @winrt_factorymethod
    def CreateResourceIndexerWithExtension(cls: Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory2, projectRoot: Windows.Foundation.Uri, extensionDllPath: Windows.Foundation.Uri) -> Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
    @winrt_factorymethod
    def CreateResourceIndexer(cls: Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory, projectRoot: Windows.Foundation.Uri) -> Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
    @winrt_mixinmethod
    def IndexFilePath(self: Windows.ApplicationModel.Resources.Management.IResourceIndexer, filePath: Windows.Foundation.Uri) -> Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate: ...
    @winrt_mixinmethod
    def IndexFileContentsAsync(self: Windows.ApplicationModel.Resources.Management.IResourceIndexer, file: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate]]: ...
ResourceIndexerContract: UInt32 = 131072
make_head(_module, 'IIndexedResourceCandidate')
make_head(_module, 'IIndexedResourceQualifier')
make_head(_module, 'IResourceIndexer')
make_head(_module, 'IResourceIndexerFactory')
make_head(_module, 'IResourceIndexerFactory2')
make_head(_module, 'IndexedResourceCandidate')
make_head(_module, 'IndexedResourceQualifier')
make_head(_module, 'ResourceIndexer')
