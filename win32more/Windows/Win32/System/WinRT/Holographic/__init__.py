from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Holographic
class IHolographicCameraInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7cc1f9c5-6d02-41fa-9500-e1809eb48eec}')
    @commethod(6)
    def CreateDirect3D12BackBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC), ppCreatedTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDirect3D12HardwareProtectedBackBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC), pProtectedResourceSession: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession, ppCreatedTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AcquireDirect3D12BufferResource(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireDirect3D12BufferResourceWithTimeout(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue, duration: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnacquireDirect3D12BufferResource(self, pResourceToUnacquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicCameraRenderingParametersInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f75b68d6-d1fd-4707-aafd-fa6f4c0e3bf4}')
    @commethod(6)
    def CommitDirect3D12Resource(self, pColorResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pColorResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence, colorResourceFenceSignalValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CommitDirect3D12ResourceWithDepthData(self, pColorResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pColorResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence, colorResourceFenceSignalValue: UInt64, pDepthResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pDepthResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence, depthResourceFenceSignalValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicQuadLayerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cfa688f0-639e-4a47-83d7-6b7f5ebf7fed}')
    @commethod(6)
    def CreateDirect3D12ContentBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC), ppTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDirect3D12HardwareProtectedContentBufferResource(self, pDevice: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, pTexture2DDesc: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC), pProtectedResourceSession: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession, ppCreatedTexture2DResource: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AcquireDirect3D12BufferResource(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireDirect3D12BufferResourceWithTimeout(self, pResourceToAcquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue, duration: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnacquireDirect3D12BufferResource(self, pResourceToUnacquire: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicQuadLayerUpdateParametersInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e5f549cd-c909-444f-8809-7cc18a9c8920}')
    @commethod(6)
    def CommitDirect3D12Resource(self, pColorResourceToCommit: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, pColorResourceFence: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence, colorResourceFenceSignalValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
