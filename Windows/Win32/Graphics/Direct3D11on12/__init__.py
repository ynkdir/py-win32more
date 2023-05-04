from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D
import Windows.Win32.Graphics.Direct3D11
import Windows.Win32.Graphics.Direct3D11on12
import Windows.Win32.Graphics.Direct3D12
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('d3d11.dll')
def D3D11On12CreateDevice(pDevice: Windows.Win32.System.Com.IUnknown_head, Flags: UInt32, pFeatureLevels: POINTER(Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL), FeatureLevels: UInt32, ppCommandQueues: POINTER(Windows.Win32.System.Com.IUnknown_head), NumQueues: UInt32, NodeMask: UInt32, ppDevice: POINTER(Windows.Win32.Graphics.Direct3D11.ID3D11Device_head), ppImmediateContext: POINTER(Windows.Win32.Graphics.Direct3D11.ID3D11DeviceContext_head), pChosenFeatureLevel: POINTER(Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
class D3D11_RESOURCE_FLAGS(EasyCastStructure):
    BindFlags: UInt32
    MiscFlags: UInt32
    CPUAccessFlags: UInt32
    StructureByteStride: UInt32
class ID3D11On12Device(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85611e73-70a9-490e-9614-a9e302777904}')
    @commethod(3)
    def CreateWrappedResource(self, pResource12: Windows.Win32.System.Com.IUnknown_head, pFlags11: POINTER(Windows.Win32.Graphics.Direct3D11on12.D3D11_RESOURCE_FLAGS_head), InState: Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_STATES, OutState: Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_STATES, riid: POINTER(Guid), ppResource11: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWrappedResources(self, ppResources: POINTER(Windows.Win32.Graphics.Direct3D11.ID3D11Resource_head), NumResources: UInt32) -> Void: ...
    @commethod(5)
    def AcquireWrappedResources(self, ppResources: POINTER(Windows.Win32.Graphics.Direct3D11.ID3D11Resource_head), NumResources: UInt32) -> Void: ...
class ID3D11On12Device1(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D11on12.ID3D11On12Device
    _iid_ = Guid('{bdb64df4-ea2f-4c70-b861-aaab1258bb5d}')
    @commethod(6)
    def GetD3D12Device(self, riid: POINTER(Guid), ppvDevice: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D11On12Device2(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D11on12.ID3D11On12Device1
    _iid_ = Guid('{dc90f331-4740-43fa-866e-67f12cb58223}')
    @commethod(7)
    def UnwrapUnderlyingResource(self, pResource11: Windows.Win32.Graphics.Direct3D11.ID3D11Resource_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, riid: POINTER(Guid), ppvResource12: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReturnUnderlyingResource(self, pResource11: Windows.Win32.Graphics.Direct3D11.ID3D11Resource_head, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_D3D11ON12_CREATE_DEVICE(param0: Windows.Win32.System.Com.IUnknown_head, param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL), FeatureLevels: UInt32, param4: POINTER(Windows.Win32.System.Com.IUnknown_head), NumQueues: UInt32, param6: UInt32, param7: POINTER(Windows.Win32.Graphics.Direct3D11.ID3D11Device_head), param8: POINTER(Windows.Win32.Graphics.Direct3D11.ID3D11DeviceContext_head), param9: POINTER(Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'D3D11_RESOURCE_FLAGS')
make_head(_module, 'ID3D11On12Device')
make_head(_module, 'ID3D11On12Device1')
make_head(_module, 'ID3D11On12Device2')
make_head(_module, 'PFN_D3D11ON12_CREATE_DEVICE')
