from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Resources.Management
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IIndexedResourceCandidate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate'
    _iid_ = Guid('{0e619ef3-faec-4414-a9d7-54acd5953f29}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceType: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Metadata(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(9)
    def get_Qualifiers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceQualifier]: ...
    @winrt_commethod(10)
    def get_ValueAsString(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetQualifierValue(self, qualifierName: WinRT_String) -> WinRT_String: ...
    Metadata = property(get_Metadata, None)
    Qualifiers = property(get_Qualifiers, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, None)
    ValueAsString = property(get_ValueAsString, None)
class IIndexedResourceQualifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier'
    _iid_ = Guid('{dae3bb9b-d304-497f-a168-a340042c8adb}')
    @winrt_commethod(6)
    def get_QualifierName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_QualifierValue(self) -> WinRT_String: ...
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
class IResourceIndexer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IResourceIndexer'
    _iid_ = Guid('{2d4cf9a5-e32f-4ab2-8748-96350a016da3}')
    @winrt_commethod(6)
    def IndexFilePath(self, filePath: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate: ...
    @winrt_commethod(7)
    def IndexFileContentsAsync(self, file: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate]]: ...
class IResourceIndexerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory'
    _iid_ = Guid('{b8de3f09-31cd-4d97-bd30-8d39f742bc61}')
    @winrt_commethod(6)
    def CreateResourceIndexer(self, projectRoot: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
class IResourceIndexerFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory2'
    _iid_ = Guid('{6040f18d-d5e5-4b60-9201-cd279cbcfed9}')
    @winrt_commethod(6)
    def CreateResourceIndexerWithExtension(self, projectRoot: win32more.Windows.Foundation.Uri, extensionDllPath: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
class IndexedResourceCandidate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceType: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Metadata(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_Qualifiers(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceQualifier]: ...
    @winrt_mixinmethod
    def get_ValueAsString(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetQualifierValue(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceCandidate, qualifierName: WinRT_String) -> WinRT_String: ...
    Metadata = property(get_Metadata, None)
    Qualifiers = property(get_Qualifiers, None)
    Type = property(get_Type, None)
    Uri = property(get_Uri, None)
    ValueAsString = property(get_ValueAsString, None)
class IndexedResourceQualifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier
    _classid_ = 'Windows.ApplicationModel.Resources.Management.IndexedResourceQualifier'
    @winrt_mixinmethod
    def get_QualifierName(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QualifierValue(self: win32more.Windows.ApplicationModel.Resources.Management.IIndexedResourceQualifier) -> WinRT_String: ...
    QualifierName = property(get_QualifierName, None)
    QualifierValue = property(get_QualifierValue, None)
class IndexedResourceType(Enum, Int32):
    String = 0
    Path = 1
    EmbeddedData = 2
class ResourceIndexer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.Management.IResourceIndexer
    _classid_ = 'Windows.ApplicationModel.Resources.Management.ResourceIndexer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Resources.Management.ResourceIndexer.CreateResourceIndexer(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Resources.Management.ResourceIndexer.CreateResourceIndexerWithExtension(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateResourceIndexer(cls: win32more.Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory, projectRoot: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
    @winrt_factorymethod
    def CreateResourceIndexerWithExtension(cls: win32more.Windows.ApplicationModel.Resources.Management.IResourceIndexerFactory2, projectRoot: win32more.Windows.Foundation.Uri, extensionDllPath: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Resources.Management.ResourceIndexer: ...
    @winrt_mixinmethod
    def IndexFilePath(self: win32more.Windows.ApplicationModel.Resources.Management.IResourceIndexer, filePath: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate: ...
    @winrt_mixinmethod
    def IndexFileContentsAsync(self: win32more.Windows.ApplicationModel.Resources.Management.IResourceIndexer, file: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Resources.Management.IndexedResourceCandidate]]: ...
ResourceIndexerContract: UInt32 = 131072


make_ready(__name__)
