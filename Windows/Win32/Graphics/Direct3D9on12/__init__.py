from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D12
import Windows.Win32.Graphics.Direct3D9
import Windows.Win32.Graphics.Direct3D9on12
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
MAX_D3D9ON12_QUEUES: UInt32 = 2
@winfunctype('d3d9.dll')
def Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d9.dll')
def Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> Windows.Win32.Graphics.Direct3D9.IDirect3D9_head: ...
class D3D9ON12_ARGS(EasyCastStructure):
    Enable9On12: Windows.Win32.Foundation.BOOL
    pD3D12Device: Windows.Win32.System.Com.IUnknown_head
    ppD3D12Queues: Windows.Win32.System.Com.IUnknown_head * 2
    NumQueues: UInt32
    NodeMask: UInt32
class IDirect3DDevice9On12(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7fda234-b589-4049-940d-8878977531c8}')
    @commethod(3)
    def GetD3D12Device(self, riid: POINTER(Guid), ppvDevice: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnwrapUnderlyingResource(self, pResource: Windows.Win32.Graphics.Direct3D9.IDirect3DResource9_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, riid: POINTER(Guid), ppvResource12: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReturnUnderlyingResource(self, pResource: Windows.Win32.Graphics.Direct3D9.IDirect3DResource9_head, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> Windows.Win32.Graphics.Direct3D9.IDirect3D9_head: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'D3D9ON12_ARGS')
make_head(_module, 'IDirect3DDevice9On12')
make_head(_module, 'PFN_Direct3DCreate9On12')
make_head(_module, 'PFN_Direct3DCreate9On12Ex')
