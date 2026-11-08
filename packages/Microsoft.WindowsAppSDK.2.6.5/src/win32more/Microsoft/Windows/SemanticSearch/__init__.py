from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.SemanticSearch
class EmbeddingVector(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.SemanticSearch.IEmbeddingVector
    _classid_ = 'Microsoft.Windows.SemanticSearch.EmbeddingVector'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Windows.SemanticSearch.EmbeddingVector.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.SemanticSearch.IEmbeddingVectorFactory, data: PassArray[Single], vectorSpaceID: Guid) -> win32more.Microsoft.Windows.SemanticSearch.EmbeddingVector: ...
    @winrt_mixinmethod
    def GetValues(self: win32more.Microsoft.Windows.SemanticSearch.IEmbeddingVector, values: FillArray[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_Count(self: win32more.Microsoft.Windows.SemanticSearch.IEmbeddingVector) -> UInt32: ...
    @winrt_mixinmethod
    def get_VectorSpaceId(self: win32more.Microsoft.Windows.SemanticSearch.IEmbeddingVector) -> Guid: ...
    Count = property(get_Count, None)
    VectorSpaceId = property(get_VectorSpaceId, None)
class IEmbeddingVector(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.SemanticSearch.IEmbeddingVector'
    _iid_ = Guid('{f80248aa-68e7-5de0-9166-b26e58935d34}')
    @winrt_commethod(6)
    def GetValues(self, values: FillArray[Single]) -> Void: ...
    @winrt_commethod(7)
    def get_Count(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_VectorSpaceId(self) -> Guid: ...
    Count = property(get_Count, None)
    VectorSpaceId = property(get_VectorSpaceId, None)
class IEmbeddingVectorFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.SemanticSearch.IEmbeddingVectorFactory'
    _iid_ = Guid('{3a31ead7-1f01-5a4c-9c2e-9acfa6495cdd}')
    @winrt_commethod(6)
    def CreateInstance(self, data: PassArray[Single], vectorSpaceID: Guid) -> win32more.Microsoft.Windows.SemanticSearch.EmbeddingVector: ...
SemanticSearchContract: UInt32 = 65536


make_ready(__name__)
