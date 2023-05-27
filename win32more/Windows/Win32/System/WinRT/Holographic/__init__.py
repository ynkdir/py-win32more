from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Holographic
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IHolographicCameraInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7cc1f9c5-6d02-41fa-9500-e1809eb48eec}')
    @commethod(6)
    def CreateDirect3D12BackBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), ppCreatedTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDirect3D12HardwareProtectedBackBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), pProtectedResourceSession: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, ppCreatedTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AcquireDirect3D12BufferResource(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireDirect3D12BufferResourceWithTimeout(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, duration: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnacquireDirect3D12BufferResource(self, pResourceToUnacquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicCameraRenderingParametersInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f75b68d6-d1fd-4707-aafd-fa6f4c0e3bf4}')
    @commethod(6)
    def CommitDirect3D12Resource(self, pColorResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pColorResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, colorResourceFenceSignalValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CommitDirect3D12ResourceWithDepthData(self, pColorResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pColorResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, colorResourceFenceSignalValue: UInt64, pDepthResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pDepthResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, depthResourceFenceSignalValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicQuadLayerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cfa688f0-639e-4a47-83d7-6b7f5ebf7fed}')
    @commethod(6)
    def CreateDirect3D12ContentBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), ppTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDirect3D12HardwareProtectedContentBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), pProtectedResourceSession: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, ppCreatedTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AcquireDirect3D12BufferResource(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireDirect3D12BufferResourceWithTimeout(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, duration: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnacquireDirect3D12BufferResource(self, pResourceToUnacquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicQuadLayerUpdateParametersInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e5f549cd-c909-444f-8809-7cc18a9c8920}')
    @commethod(6)
    def CommitDirect3D12Resource(self, pColorResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pColorResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, colorResourceFenceSignalValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IHolographicCameraInterop')
make_head(_module, 'IHolographicCameraRenderingParametersInterop')
make_head(_module, 'IHolographicQuadLayerInterop')
make_head(_module, 'IHolographicQuadLayerUpdateParametersInterop')
