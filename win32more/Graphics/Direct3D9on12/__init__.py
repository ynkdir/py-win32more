from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.Graphics.Direct3D9
import win32more.Graphics.Direct3D9on12
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
MAX_D3D9ON12_QUEUES = 2
def _define_Direct3DCreate9On12Ex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head),UInt32,POINTER(win32more.Graphics.Direct3D9.IDirect3D9Ex_head))(('Direct3DCreate9On12Ex', windll['d3d9.dll']), ((1, 'SDKVersion'),(1, 'pOverrideList'),(1, 'NumOverrideEntries'),(1, 'ppOutputInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Direct3DCreate9On12():
    try:
        return WINFUNCTYPE(win32more.Graphics.Direct3D9.IDirect3D9_head,UInt32,POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head),UInt32)(('Direct3DCreate9On12', windll['d3d9.dll']), ((1, 'SDKVersion'),(1, 'pOverrideList'),(1, 'NumOverrideEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D9ON12_ARGS_head():
    class D3D9ON12_ARGS(Structure):
        pass
    return D3D9ON12_ARGS
def _define_D3D9ON12_ARGS():
    D3D9ON12_ARGS = win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head
    D3D9ON12_ARGS._fields_ = [
        ('Enable9On12', win32more.Foundation.BOOL),
        ('pD3D12Device', win32more.System.Com.IUnknown_head),
        ('ppD3D12Queues', win32more.System.Com.IUnknown_head * 2),
        ('NumQueues', UInt32),
        ('NodeMask', UInt32),
    ]
    return D3D9ON12_ARGS
def _define_IDirect3DDevice9On12_head():
    class IDirect3DDevice9On12(win32more.System.Com.IUnknown_head):
        Guid = Guid('e7fda234-b589-4049-94-0d-88-78-97-75-31-c8')
    return IDirect3DDevice9On12
def _define_IDirect3DDevice9On12():
    IDirect3DDevice9On12 = win32more.Graphics.Direct3D9on12.IDirect3DDevice9On12_head
    IDirect3DDevice9On12.GetD3D12Device = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'GetD3D12Device', ((1, 'riid'),(1, 'ppvDevice'),)))
    IDirect3DDevice9On12.UnwrapUnderlyingResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D9.IDirect3DResource9_head,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head,POINTER(Guid),POINTER(c_void_p))(4, 'UnwrapUnderlyingResource', ((1, 'pResource'),(1, 'pCommandQueue'),(1, 'riid'),(1, 'ppvResource12'),)))
    IDirect3DDevice9On12.ReturnUnderlyingResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D9.IDirect3DResource9_head,UInt32,POINTER(UInt64),POINTER(win32more.Graphics.Direct3D12.ID3D12Fence_head))(5, 'ReturnUnderlyingResource', ((1, 'pResource'),(1, 'NumSync'),(1, 'pSignalValues'),(1, 'ppFences'),)))
    win32more.System.Com.IUnknown
    return IDirect3DDevice9On12
def _define_PFN_Direct3DCreate9On12():
    return WINFUNCTYPE(win32more.Graphics.Direct3D9.IDirect3D9_head,UInt32,POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head),UInt32)
def _define_PFN_Direct3DCreate9On12Ex():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D9on12.D3D9ON12_ARGS_head),UInt32,POINTER(win32more.Graphics.Direct3D9.IDirect3D9Ex_head))
__all__ = [
    "D3D9ON12_ARGS",
    "Direct3DCreate9On12",
    "Direct3DCreate9On12Ex",
    "IDirect3DDevice9On12",
    "MAX_D3D9ON12_QUEUES",
    "PFN_Direct3DCreate9On12",
    "PFN_Direct3DCreate9On12Ex",
]