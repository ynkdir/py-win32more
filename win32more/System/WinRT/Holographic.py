from win32more import *
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.WinRT
import win32more.System.WinRT.Holographic

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IHolographicCameraInterop_head():
    class IHolographicCameraInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('7cc1f9c5-6d02-41fa-9500-e1809eb48eec')
    return IHolographicCameraInterop
def _define_IHolographicCameraInterop():
    IHolographicCameraInterop = win32more.System.WinRT.Holographic.IHolographicCameraInterop_head
    IHolographicCameraInterop.CreateDirect3D12BackBufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,POINTER(win32more.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head),POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head), use_last_error=False)(6, 'CreateDirect3D12BackBufferResource', ((1, 'pDevice'),(1, 'pTexture2DDesc'),(1, 'ppCreatedTexture2DResource'),)))
    IHolographicCameraInterop.CreateDirect3D12HardwareProtectedBackBufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,POINTER(win32more.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head),win32more.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head,POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head), use_last_error=False)(7, 'CreateDirect3D12HardwareProtectedBackBufferResource', ((1, 'pDevice'),(1, 'pTexture2DDesc'),(1, 'pProtectedResourceSession'),(1, 'ppCreatedTexture2DResource'),)))
    IHolographicCameraInterop.AcquireDirect3D12BufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head, use_last_error=False)(8, 'AcquireDirect3D12BufferResource', ((1, 'pResourceToAcquire'),(1, 'pCommandQueue'),)))
    IHolographicCameraInterop.AcquireDirect3D12BufferResourceWithTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head,UInt64, use_last_error=False)(9, 'AcquireDirect3D12BufferResourceWithTimeout', ((1, 'pResourceToAcquire'),(1, 'pCommandQueue'),(1, 'duration'),)))
    IHolographicCameraInterop.UnacquireDirect3D12BufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head, use_last_error=False)(10, 'UnacquireDirect3D12BufferResource', ((1, 'pResourceToUnacquire'),)))
    win32more.System.WinRT.IInspectable
    return IHolographicCameraInterop
def _define_IHolographicCameraRenderingParametersInterop_head():
    class IHolographicCameraRenderingParametersInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('f75b68d6-d1fd-4707-aafd-fa6f4c0e3bf4')
    return IHolographicCameraRenderingParametersInterop
def _define_IHolographicCameraRenderingParametersInterop():
    IHolographicCameraRenderingParametersInterop = win32more.System.WinRT.Holographic.IHolographicCameraRenderingParametersInterop_head
    IHolographicCameraRenderingParametersInterop.CommitDirect3D12Resource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12Fence_head,UInt64, use_last_error=False)(6, 'CommitDirect3D12Resource', ((1, 'pColorResourceToCommit'),(1, 'pColorResourceFence'),(1, 'colorResourceFenceSignalValue'),)))
    IHolographicCameraRenderingParametersInterop.CommitDirect3D12ResourceWithDepthData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12Fence_head,UInt64,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12Fence_head,UInt64, use_last_error=False)(7, 'CommitDirect3D12ResourceWithDepthData', ((1, 'pColorResourceToCommit'),(1, 'pColorResourceFence'),(1, 'colorResourceFenceSignalValue'),(1, 'pDepthResourceToCommit'),(1, 'pDepthResourceFence'),(1, 'depthResourceFenceSignalValue'),)))
    win32more.System.WinRT.IInspectable
    return IHolographicCameraRenderingParametersInterop
def _define_IHolographicQuadLayerInterop_head():
    class IHolographicQuadLayerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('cfa688f0-639e-4a47-83d7-6b7f5ebf7fed')
    return IHolographicQuadLayerInterop
def _define_IHolographicQuadLayerInterop():
    IHolographicQuadLayerInterop = win32more.System.WinRT.Holographic.IHolographicQuadLayerInterop_head
    IHolographicQuadLayerInterop.CreateDirect3D12ContentBufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,POINTER(win32more.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head),POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head), use_last_error=False)(6, 'CreateDirect3D12ContentBufferResource', ((1, 'pDevice'),(1, 'pTexture2DDesc'),(1, 'ppTexture2DResource'),)))
    IHolographicQuadLayerInterop.CreateDirect3D12HardwareProtectedContentBufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,POINTER(win32more.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head),win32more.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head,POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head), use_last_error=False)(7, 'CreateDirect3D12HardwareProtectedContentBufferResource', ((1, 'pDevice'),(1, 'pTexture2DDesc'),(1, 'pProtectedResourceSession'),(1, 'ppCreatedTexture2DResource'),)))
    IHolographicQuadLayerInterop.AcquireDirect3D12BufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head, use_last_error=False)(8, 'AcquireDirect3D12BufferResource', ((1, 'pResourceToAcquire'),(1, 'pCommandQueue'),)))
    IHolographicQuadLayerInterop.AcquireDirect3D12BufferResourceWithTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head,UInt64, use_last_error=False)(9, 'AcquireDirect3D12BufferResourceWithTimeout', ((1, 'pResourceToAcquire'),(1, 'pCommandQueue'),(1, 'duration'),)))
    IHolographicQuadLayerInterop.UnacquireDirect3D12BufferResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head, use_last_error=False)(10, 'UnacquireDirect3D12BufferResource', ((1, 'pResourceToUnacquire'),)))
    win32more.System.WinRT.IInspectable
    return IHolographicQuadLayerInterop
def _define_IHolographicQuadLayerUpdateParametersInterop_head():
    class IHolographicQuadLayerUpdateParametersInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('e5f549cd-c909-444f-8809-7cc18a9c8920')
    return IHolographicQuadLayerUpdateParametersInterop
def _define_IHolographicQuadLayerUpdateParametersInterop():
    IHolographicQuadLayerUpdateParametersInterop = win32more.System.WinRT.Holographic.IHolographicQuadLayerUpdateParametersInterop_head
    IHolographicQuadLayerUpdateParametersInterop.CommitDirect3D12Resource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,win32more.Graphics.Direct3D12.ID3D12Fence_head,UInt64, use_last_error=False)(6, 'CommitDirect3D12Resource', ((1, 'pColorResourceToCommit'),(1, 'pColorResourceFence'),(1, 'colorResourceFenceSignalValue'),)))
    win32more.System.WinRT.IInspectable
    return IHolographicQuadLayerUpdateParametersInterop
__all__ = [
    "IHolographicCameraInterop",
    "IHolographicCameraRenderingParametersInterop",
    "IHolographicQuadLayerInterop",
    "IHolographicQuadLayerUpdateParametersInterop",
]
