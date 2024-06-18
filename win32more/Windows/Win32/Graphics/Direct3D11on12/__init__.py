from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D
import win32more.Windows.Win32.Graphics.Direct3D11
import win32more.Windows.Win32.Graphics.Direct3D11on12
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.System.Com
@winfunctype('d3d11.dll')
def D3D11On12CreateDevice(pDevice: win32more.Windows.Win32.System.Com.IUnknown, Flags: UInt32, pFeatureLevels: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL), FeatureLevels: UInt32, ppCommandQueues: POINTER(win32more.Windows.Win32.System.Com.IUnknown), NumQueues: UInt32, NodeMask: UInt32, ppDevice: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Device), ppImmediateContext: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11DeviceContext), pChosenFeatureLevel: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class D3D11_RESOURCE_FLAGS(Structure):
    BindFlags: UInt32
    MiscFlags: UInt32
    CPUAccessFlags: UInt32
    StructureByteStride: UInt32
class ID3D11On12Device(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85611e73-70a9-490e-9614-a9e302777904}')
    @commethod(3)
    def CreateWrappedResource(self, pResource12: win32more.Windows.Win32.System.Com.IUnknown, pFlags11: POINTER(win32more.Windows.Win32.Graphics.Direct3D11on12.D3D11_RESOURCE_FLAGS), InState: win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_STATES, OutState: win32more.Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_STATES, riid: POINTER(Guid), ppResource11: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWrappedResources(self, ppResources: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Resource), NumResources: UInt32) -> Void: ...
    @commethod(5)
    def AcquireWrappedResources(self, ppResources: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Resource), NumResources: UInt32) -> Void: ...
class ID3D11On12Device1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Direct3D11on12.ID3D11On12Device
    _iid_ = Guid('{bdb64df4-ea2f-4c70-b861-aaab1258bb5d}')
    @commethod(6)
    def GetD3D12Device(self, riid: POINTER(Guid), ppvDevice: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ID3D11On12Device2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Direct3D11on12.ID3D11On12Device1
    _iid_ = Guid('{dc90f331-4740-43fa-866e-67f12cb58223}')
    @commethod(7)
    def UnwrapUnderlyingResource(self, pResource11: win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Resource, pCommandQueue: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue, riid: POINTER(Guid), ppvResource12: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReturnUnderlyingResource(self, pResource11: win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Resource, NumSync: UInt32, pSignalValues: POINTER(UInt64), ppFences: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Fence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_D3D11ON12_CREATE_DEVICE(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: UInt32, param2: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL), FeatureLevels: UInt32, param4: POINTER(win32more.Windows.Win32.System.Com.IUnknown), NumQueues: UInt32, param6: UInt32, param7: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Device), param8: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11DeviceContext), param9: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_FEATURE_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
