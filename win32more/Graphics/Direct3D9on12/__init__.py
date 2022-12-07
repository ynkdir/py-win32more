from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.Graphics.Direct3D9
import win32more.Graphics.Direct3D9on12
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
MAX_D3D9ON12_QUEUES: UInt32 = 2
@winfunctype('d3d9.dll')
def Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(win32more.Graphics.Direct3D9.IDirect3D9Ex_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('d3d9.dll')
def Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> win32more.Graphics.Direct3D9.IDirect3D9_head: ...
class D3D9ON12_ARGS(Structure):
    Enable9On12: win32more.Foundation.BOOL
    pD3D12Device: win32more.System.Com.IUnknown_head
    ppD3D12Queues: win32more.System.Com.IUnknown_head * 2
    NumQueues: UInt32
    NodeMask: UInt32
class IDirect3DDevice9On12(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e7fda234-b589-4049-94-0d-88-78-97-75-31-c8')
    @commethod(3)
    def GetD3D12Device(riid: POINTER(Guid), ppvDevice: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnwrapUnderlyingResource(pResource: win32more.Graphics.Direct3D9.IDirect3DResource9_head, pCommandQueue: win32more.Graphics.Direct3D12.ID3D12CommandQueue_head, riid: POINTER(Guid), ppvResource12: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ReturnUnderlyingResource(pResource: win32more.Graphics.Direct3D9.IDirect3DResource9_head, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(win32more.Graphics.Direct3D12.ID3D12Fence_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> win32more.Graphics.Direct3D9.IDirect3D9_head: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(win32more.Graphics.Direct3D9.IDirect3D9Ex_head)) -> win32more.Foundation.HRESULT: ...
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
