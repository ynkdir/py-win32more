from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
MAX_D3D9ON12_QUEUES: UInt32 = 2
@winfunctype('d3d9.dll')
def Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d9.dll')
def Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> Windows.Win32.Graphics.Direct3D9.IDirect3D9_head: ...
class D3D9ON12_ARGS(Structure):
    Enable9On12: Windows.Win32.Foundation.BOOL
    pD3D12Device: Windows.Win32.System.Com.IUnknown_head
    ppD3D12Queues: Windows.Win32.System.Com.IUnknown_head * 2
    NumQueues: UInt32
    NodeMask: UInt32
class IDirect3DDevice9On12(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e7fda234-b589-4049-94-0d-88-78-97-75-31-c8')
    @commethod(3)
    def GetD3D12Device(riid: POINTER(Guid), ppvDevice: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnwrapUnderlyingResource(pResource: Windows.Win32.Graphics.Direct3D9.IDirect3DResource9_head, pCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, riid: POINTER(Guid), ppvResource12: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReturnUnderlyingResource(pResource: Windows.Win32.Graphics.Direct3D9.IDirect3DResource9_head, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> Windows.Win32.Graphics.Direct3D9.IDirect3D9_head: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'D3D9ON12_ARGS')
make_head(_module, 'IDirect3DDevice9On12')
make_head(_module, 'PFN_Direct3DCreate9On12')
make_head(_module, 'PFN_Direct3DCreate9On12Ex')
__all__ = [
    "D3D9ON12_ARGS",
    "Direct3DCreate9On12",
    "Direct3DCreate9On12Ex",
    "IDirect3DDevice9On12",
    "MAX_D3D9ON12_QUEUES",
    "PFN_Direct3DCreate9On12",
    "PFN_Direct3DCreate9On12Ex",
]
_arch_optional = [
]
