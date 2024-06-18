from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.Graphics.Direct3D9
import win32more.Windows.Win32.Graphics.Direct3D9on12
import win32more.Windows.Win32.System.Com
MAX_D3D9ON12_QUEUES: UInt32 = 2
@winfunctype('d3d9.dll')
def Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d9.dll')
def Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS), NumOverrideEntries: UInt32) -> win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9: ...
class D3D9ON12_ARGS(Structure):
    Enable9On12: win32more.Windows.Win32.Foundation.BOOL
    pD3D12Device: win32more.Windows.Win32.System.Com.IUnknown
    ppD3D12Queues: win32more.Windows.Win32.System.Com.IUnknown * 2
    NumQueues: UInt32
    NodeMask: UInt32
class IDirect3DDevice9On12(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7fda234-b589-4049-940d-8878977531c8}')
    @commethod(3)
    def GetD3D12Device(self, riid: POINTER(Guid), ppvDevice: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnwrapUnderlyingResource(self, pResource: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DResource9, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue, riid: POINTER(Guid), ppvResource12: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReturnUnderlyingResource(self, pResource: win32more.Windows.Win32.Graphics.Direct3D9.IDirect3DResource9, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS), NumOverrideEntries: UInt32) -> win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9: ...
@winfunctype_pointer
def PFN_Direct3DCreate9On12Ex(SDKVersion: UInt32, pOverrideList: POINTER(win32more.Windows.Win32.Graphics.Direct3D9on12.D3D9ON12_ARGS), NumOverrideEntries: UInt32, ppOutputInterface: POINTER(win32more.Windows.Win32.Graphics.Direct3D9.IDirect3D9Ex)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
