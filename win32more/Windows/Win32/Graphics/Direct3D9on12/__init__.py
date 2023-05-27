from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.Graphics.Direct3D9
import win32more.Windows.Win32.Graphics.Direct3D9on12
import win32more.Windows.Win32.System.Com
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
def Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d9.dll')
def Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9_head: ...
class D3D9ON12_ARGS(EasyCastStructure):
    Enable9On12: win32more.Windows.Win32.Foundation.BOOL
    pD3D12Device: win32more.Windows.Win32.System.Com.IUnknown_head
    ppD3D12Queues: win32more.Windows.Win32.System.Com.IUnknown_head * 2
    NumQueues: UInt32
    NodeMask: UInt32
class IDirect3DDevice9On12(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7fda234-b589-4049-940d-8878977531c8}')
    @commethod(3)
    def GetD3D12Device(self, riid: POINTER(Guid), ppvDevice: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnwrapUnderlyingResource(self, pResource: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DResource9_head, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, riid: POINTER(Guid), ppvResource12: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReturnUnderlyingResource(self, pResource: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DResource9_head, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32) -> win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9_head: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS_head), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'D3D9ON12_ARGS')
make_head(_module, 'IDirect3DDevice9On12')
make_head(_module, 'PFN_Direct3DCreate9On12')
make_head(_module, 'PFN_Direct3DCreate9On12Ex')
