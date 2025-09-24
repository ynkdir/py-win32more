from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.AI.Foundation
AIFoundationContract: UInt32 = 65536
class EmbeddingVector(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Foundation.IEmbeddingVector
    _classid_ = 'Microsoft.Windows.AI.Foundation.EmbeddingVector'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.Foundation.IEmbeddingVectorFactory, data: PassArray[Single], vectorSpaceID: Guid) -> win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector: ...
    @winrt_mixinmethod
    def GetValues(self: win32more.Microsoft.Windows.AI.Foundation.IEmbeddingVector, values: FillArray[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Microsoft.Windows.AI.Foundation.IEmbeddingVector) -> UInt32: ...
    @winrt_mixinmethod
    def get_VectorSpaceId(self: win32more.Microsoft.Windows.AI.Foundation.IEmbeddingVector) -> Guid: ...
    Size = property(get_Size, None)
    VectorSpaceId = property(get_VectorSpaceId, None)
class IEmbeddingVector(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Foundation.IEmbeddingVector'
    _iid_ = Guid('{07bdaa90-b3d2-5701-97d1-c390ec62799c}')
    @winrt_commethod(6)
    def GetValues(self, values: FillArray[Single]) -> Void: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_VectorSpaceId(self) -> Guid: ...
    Size = property(get_Size, None)
    VectorSpaceId = property(get_VectorSpaceId, None)
class IEmbeddingVectorFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Foundation.IEmbeddingVectorFactory'
    _iid_ = Guid('{16b72758-2b69-5e97-b865-6a6a71683dd0}')
    @winrt_commethod(6)
    def CreateInstance(self, data: PassArray[Single], vectorSpaceID: Guid) -> win32more.Microsoft.Windows.AI.Foundation.EmbeddingVector: ...


make_ready(__name__)
