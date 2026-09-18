from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Graphics.Imaging
import win32more.Microsoft.Windows.AI
import win32more.Microsoft.Windows.AI.Video
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Graphics.DirectX.Direct3D11
class IVideoScaler(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Video.IVideoScaler'
    _iid_ = Guid('{e5abe769-63cc-5498-a5e1-74205106bdfd}')
    @winrt_commethod(6)
    def Scale(self, input: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, output: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, options: win32more.Microsoft.Windows.AI.Video.VideoScalerOptions) -> win32more.Microsoft.Windows.AI.Video.VideoScalerResult: ...
    @winrt_commethod(7)
    def ScaleImageBuffer(self, input: win32more.Microsoft.Graphics.Imaging.ImageBuffer, output: win32more.Microsoft.Graphics.Imaging.ImageBuffer, options: win32more.Microsoft.Windows.AI.Video.VideoScalerOptions) -> win32more.Microsoft.Windows.AI.Video.VideoScalerResult: ...
class IVideoScalerOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Video.IVideoScalerOptions'
    _iid_ = Guid('{3a1427f8-ddad-519e-a028-7322bde4c4d2}')
    @winrt_commethod(6)
    def get_RegionsOfInterest(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.RectInt32]: ...
    RegionsOfInterest = property(get_RegionsOfInterest, None)
class IVideoScalerResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Video.IVideoScalerResult'
    _iid_ = Guid('{24a228fb-0af2-5a00-bb6d-52946d9460da}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.Video.VideoScalerStatus: ...
    Status = property(get_Status, None)
class IVideoScalerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Video.IVideoScalerStatics'
    _iid_ = Guid('{311dd8bb-b7ac-55a7-a3d3-1a6c84430f84}')
    @winrt_commethod(6)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(7)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_commethod(8)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Video.VideoScaler]: ...
class VideoScaler(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Video.IVideoScaler
    _classid_ = 'Microsoft.Windows.AI.Video.VideoScaler'
    @winrt_mixinmethod
    def Scale(self: win32more.Microsoft.Windows.AI.Video.IVideoScaler, input: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, output: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, options: win32more.Microsoft.Windows.AI.Video.VideoScalerOptions) -> win32more.Microsoft.Windows.AI.Video.VideoScalerResult: ...
    @winrt_mixinmethod
    def ScaleImageBuffer(self: win32more.Microsoft.Windows.AI.Video.IVideoScaler, input: win32more.Microsoft.Graphics.Imaging.ImageBuffer, output: win32more.Microsoft.Graphics.Imaging.ImageBuffer, options: win32more.Microsoft.Windows.AI.Video.VideoScalerOptions) -> win32more.Microsoft.Windows.AI.Video.VideoScalerResult: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Video.IVideoScalerStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Video.IVideoScalerStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Windows.AI.Video.IVideoScalerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Video.VideoScaler]: ...
class VideoScalerOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Video.IVideoScalerOptions
    _classid_ = 'Microsoft.Windows.AI.Video.VideoScalerOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.Video.VideoScalerOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.Video.VideoScalerOptions: ...
    @winrt_mixinmethod
    def get_RegionsOfInterest(self: win32more.Microsoft.Windows.AI.Video.IVideoScalerOptions) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.RectInt32]: ...
    RegionsOfInterest = property(get_RegionsOfInterest, None)
class VideoScalerResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Video.IVideoScalerResult
    _classid_ = 'Microsoft.Windows.AI.Video.VideoScalerResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.Video.IVideoScalerResult) -> win32more.Microsoft.Windows.AI.Video.VideoScalerStatus: ...
    Status = property(get_Status, None)
class VideoScalerStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.AI.Video.VideoScalerStatus'
    Success = 0
    InvalidInputFormat = 1
    InvalidOutputFormat = 2
    InvalidPlaneSize = 3
    InvalidFrameData = 4
    ModelNotAvailable = 5
    OutOfMemory = 6
    Failure = 7


make_ready(__name__)
