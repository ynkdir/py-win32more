from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D12
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Holographic
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IHolographicCameraInterop(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7cc1f9c5-6d02-41fa-95-00-e1-80-9e-b4-8e-ec')
    @commethod(6)
    def CreateDirect3D12BackBufferResource(self, pDevice: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), ppCreatedTexture2DResource: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDirect3D12HardwareProtectedBackBufferResource(self, pDevice: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, ppCreatedTexture2DResource: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AcquireDirect3D12BufferResource(self, pResourceToAcquire: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireDirect3D12BufferResourceWithTimeout(self, pResourceToAcquire: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, duration: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnacquireDirect3D12BufferResource(self, pResourceToUnacquire: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head) -> Windows.Win32.Foundation.HRESULT: ...
class IHolographicCameraRenderingParametersInterop(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f75b68d6-d1fd-4707-aa-fd-fa-6f-4c-0e-3b-f4')
    @commethod(6)
    def CommitDirect3D12Resource(self, pColorResourceToCommit: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pColorResourceFence: Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, colorResourceFenceSignalValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CommitDirect3D12ResourceWithDepthData(self, pColorResourceToCommit: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pColorResourceFence: Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, colorResourceFenceSignalValue: UInt64, pDepthResourceToCommit: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pDepthResourceFence: Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, depthResourceFenceSignalValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IHolographicQuadLayerInterop(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cfa688f0-639e-4a47-83-d7-6b-7f-5e-bf-7f-ed')
    @commethod(6)
    def CreateDirect3D12ContentBufferResource(self, pDevice: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), ppTexture2DResource: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDirect3D12HardwareProtectedContentBufferResource(self, pDevice: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, pTexture2DDesc: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, ppCreatedTexture2DResource: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AcquireDirect3D12BufferResource(self, pResourceToAcquire: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireDirect3D12BufferResourceWithTimeout(self, pResourceToAcquire: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, duration: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnacquireDirect3D12BufferResource(self, pResourceToUnacquire: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head) -> Windows.Win32.Foundation.HRESULT: ...
class IHolographicQuadLayerUpdateParametersInterop(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5f549cd-c909-444f-88-09-7c-c1-8a-9c-89-20')
    @commethod(6)
    def CommitDirect3D12Resource(self, pColorResourceToCommit: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pColorResourceFence: Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head, colorResourceFenceSignalValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IHolographicCameraInterop')
make_head(_module, 'IHolographicCameraRenderingParametersInterop')
make_head(_module, 'IHolographicQuadLayerInterop')
make_head(_module, 'IHolographicQuadLayerUpdateParametersInterop')
