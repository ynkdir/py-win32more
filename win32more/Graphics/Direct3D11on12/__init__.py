from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct3D
import win32more.Graphics.Direct3D11
import win32more.Graphics.Direct3D11on12
import win32more.Graphics.Direct3D12
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('d3d11.dll')
def D3D11On12CreateDevice(pDevice: win32more.System.Com.IUnknown_head, Flags: UInt32, pFeatureLevels: POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL), FeatureLevels: UInt32, ppCommandQueues: POINTER(win32more.System.Com.IUnknown_head), NumQueues: UInt32, NodeMask: UInt32, ppDevice: POINTER(win32more.Graphics.Direct3D11.ID3D11Device_head), ppImmediateContext: POINTER(win32more.Graphics.Direct3D11.ID3D11DeviceContext_head), pChosenFeatureLevel: POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL)) -> win32more.Foundation.HRESULT: ...
class D3D11_RESOURCE_FLAGS(Structure):
    BindFlags: UInt32
    MiscFlags: UInt32
    CPUAccessFlags: UInt32
    StructureByteStride: UInt32
class ID3D11On12Device(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('85611e73-70a9-490e-96-14-a9-e3-02-77-79-04')
    @commethod(3)
    def CreateWrappedResource(pResource12: win32more.System.Com.IUnknown_head, pFlags11: POINTER(win32more.Graphics.Direct3D11on12.D3D11_RESOURCE_FLAGS_head), InState: win32more.Graphics.Direct3D12.D3D12_RESOURCE_STATES, OutState: win32more.Graphics.Direct3D12.D3D12_RESOURCE_STATES, riid: POINTER(Guid), ppResource11: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWrappedResources(ppResources: POINTER(win32more.Graphics.Direct3D11.ID3D11Resource_head), NumResources: UInt32) -> Void: ...
    @commethod(5)
    def AcquireWrappedResources(ppResources: POINTER(win32more.Graphics.Direct3D11.ID3D11Resource_head), NumResources: UInt32) -> Void: ...
class ID3D11On12Device1(c_void_p):
    extends: win32more.Graphics.Direct3D11on12.ID3D11On12Device
    Guid = Guid('bdb64df4-ea2f-4c70-b8-61-aa-ab-12-58-bb-5d')
    @commethod(6)
    def GetD3D12Device(riid: POINTER(Guid), ppvDevice: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ID3D11On12Device2(c_void_p):
    extends: win32more.Graphics.Direct3D11on12.ID3D11On12Device1
    Guid = Guid('dc90f331-4740-43fa-86-6e-67-f1-2c-b5-82-23')
    @commethod(7)
    def UnwrapUnderlyingResource(pResource11: win32more.Graphics.Direct3D11.ID3D11Resource_head, pCommandQueue: win32more.Graphics.Direct3D12.ID3D12CommandQueue_head, riid: POINTER(Guid), ppvResource12: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ReturnUnderlyingResource(pResource11: win32more.Graphics.Direct3D11.ID3D11Resource_head, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(win32more.Graphics.Direct3D12.ID3D12Fence_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_D3D11ON12_CREATE_DEVICE(param0: win32more.System.Com.IUnknown_head, param1: UInt32, param2: POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL), FeatureLevels: UInt32, param4: POINTER(win32more.System.Com.IUnknown_head), NumQueues: UInt32, param6: UInt32, param7: POINTER(win32more.Graphics.Direct3D11.ID3D11Device_head), param8: POINTER(win32more.Graphics.Direct3D11.ID3D11DeviceContext_head), param9: POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'D3D11_RESOURCE_FLAGS')
make_head(_module, 'ID3D11On12Device')
make_head(_module, 'ID3D11On12Device1')
make_head(_module, 'ID3D11On12Device2')
make_head(_module, 'PFN_D3D11ON12_CREATE_DEVICE')
__all__ = [
    "D3D11On12CreateDevice",
    "D3D11_RESOURCE_FLAGS",
    "ID3D11On12Device",
    "ID3D11On12Device1",
    "ID3D11On12Device2",
    "PFN_D3D11ON12_CREATE_DEVICE",
]
