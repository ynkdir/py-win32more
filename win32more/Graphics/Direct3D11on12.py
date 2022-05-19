from win32more import *
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
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_PFN_D3D11ON12_CREATE_DEVICE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL),UInt32,POINTER(win32more.System.Com.IUnknown_head),UInt32,UInt32,POINTER(win32more.Graphics.Direct3D11.ID3D11Device_head),POINTER(win32more.Graphics.Direct3D11.ID3D11DeviceContext_head),POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL), use_last_error=False)
def _define_D3D11_RESOURCE_FLAGS_head():
    class D3D11_RESOURCE_FLAGS(Structure):
        pass
    return D3D11_RESOURCE_FLAGS
def _define_D3D11_RESOURCE_FLAGS():
    D3D11_RESOURCE_FLAGS = win32more.Graphics.Direct3D11on12.D3D11_RESOURCE_FLAGS_head
    D3D11_RESOURCE_FLAGS._fields_ = [
        ("BindFlags", UInt32),
        ("MiscFlags", UInt32),
        ("CPUAccessFlags", UInt32),
        ("StructureByteStride", UInt32),
    ]
    return D3D11_RESOURCE_FLAGS
def _define_ID3D11On12Device_head():
    class ID3D11On12Device(win32more.System.Com.IUnknown_head):
        Guid = Guid('85611e73-70a9-490e-9614-a9e302777904')
    return ID3D11On12Device
def _define_ID3D11On12Device():
    ID3D11On12Device = win32more.Graphics.Direct3D11on12.ID3D11On12Device_head
    ID3D11On12Device.CreateWrappedResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.Direct3D11on12.D3D11_RESOURCE_FLAGS_head),win32more.Graphics.Direct3D12.D3D12_RESOURCE_STATES,win32more.Graphics.Direct3D12.D3D12_RESOURCE_STATES,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateWrappedResource', ((1, 'pResource12'),(1, 'pFlags11'),(1, 'InState'),(1, 'OutState'),(1, 'riid'),(1, 'ppResource11'),)))
    ID3D11On12Device.ReleaseWrappedResources = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D11.ID3D11Resource_head),UInt32, use_last_error=False)(4, 'ReleaseWrappedResources', ((1, 'ppResources'),(1, 'NumResources'),)))
    ID3D11On12Device.AcquireWrappedResources = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D11.ID3D11Resource_head),UInt32, use_last_error=False)(5, 'AcquireWrappedResources', ((1, 'ppResources'),(1, 'NumResources'),)))
    return ID3D11On12Device
def _define_ID3D11On12Device1_head():
    class ID3D11On12Device1(win32more.Graphics.Direct3D11on12.ID3D11On12Device_head):
        Guid = Guid('bdb64df4-ea2f-4c70-b861-aaab1258bb5d')
    return ID3D11On12Device1
def _define_ID3D11On12Device1():
    ID3D11On12Device1 = win32more.Graphics.Direct3D11on12.ID3D11On12Device1_head
    ID3D11On12Device1.GetD3D12Device = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetD3D12Device', ((1, 'riid'),(1, 'ppvDevice'),)))
    return ID3D11On12Device1
def _define_ID3D11On12Device2_head():
    class ID3D11On12Device2(win32more.Graphics.Direct3D11on12.ID3D11On12Device1_head):
        Guid = Guid('dc90f331-4740-43fa-866e-67f12cb58223')
    return ID3D11On12Device2
def _define_ID3D11On12Device2():
    ID3D11On12Device2 = win32more.Graphics.Direct3D11on12.ID3D11On12Device2_head
    ID3D11On12Device2.UnwrapUnderlyingResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D11.ID3D11Resource_head,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'UnwrapUnderlyingResource', ((1, 'pResource11'),(1, 'pCommandQueue'),(1, 'riid'),(1, 'ppvResource12'),)))
    ID3D11On12Device2.ReturnUnderlyingResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D11.ID3D11Resource_head,UInt32,POINTER(UInt64),POINTER(win32more.Graphics.Direct3D12.ID3D12Fence_head), use_last_error=False)(8, 'ReturnUnderlyingResource', ((1, 'pResource11'),(1, 'NumSync'),(1, 'pSignalValues'),(1, 'ppFences'),)))
    return ID3D11On12Device2
def _define_D3D11On12CreateDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL),UInt32,POINTER(win32more.System.Com.IUnknown_head),UInt32,UInt32,POINTER(win32more.Graphics.Direct3D11.ID3D11Device_head),POINTER(win32more.Graphics.Direct3D11.ID3D11DeviceContext_head),POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL), use_last_error=False)(("D3D11On12CreateDevice", windll["d3d11"]), ((1, 'pDevice'),(1, 'Flags'),(1, 'pFeatureLevels'),(1, 'FeatureLevels'),(1, 'ppCommandQueues'),(1, 'NumQueues'),(1, 'NodeMask'),(1, 'ppDevice'),(1, 'ppImmediateContext'),(1, 'pChosenFeatureLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PFN_D3D11ON12_CREATE_DEVICE",
    "D3D11_RESOURCE_FLAGS",
    "ID3D11On12Device",
    "ID3D11On12Device1",
    "ID3D11On12Device2",
    "D3D11On12CreateDevice",
]
