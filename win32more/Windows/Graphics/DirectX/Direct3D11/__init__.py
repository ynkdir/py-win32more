from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Win32.System.WinRT
Direct3DBindings = UInt32
Direct3DBindings_VertexBuffer: Direct3DBindings = 1
Direct3DBindings_IndexBuffer: Direct3DBindings = 2
Direct3DBindings_ConstantBuffer: Direct3DBindings = 4
Direct3DBindings_ShaderResource: Direct3DBindings = 8
Direct3DBindings_StreamOutput: Direct3DBindings = 16
Direct3DBindings_RenderTarget: Direct3DBindings = 32
Direct3DBindings_DepthStencil: Direct3DBindings = 64
Direct3DBindings_UnorderedAccess: Direct3DBindings = 128
Direct3DBindings_Decoder: Direct3DBindings = 512
Direct3DBindings_VideoEncoder: Direct3DBindings = 1024
class Direct3DMultisampleDescription(EasyCastStructure):
    Count: Int32
    Quality: Int32
class Direct3DSurfaceDescription(EasyCastStructure):
    Width: Int32
    Height: Int32
    Format: win32more.Windows.Graphics.DirectX.DirectXPixelFormat
    MultisampleDescription: win32more.Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription
Direct3DUsage = Int32
Direct3DUsage_Default: Direct3DUsage = 0
Direct3DUsage_Immutable: Direct3DUsage = 1
Direct3DUsage_Dynamic: Direct3DUsage = 2
Direct3DUsage_Staging: Direct3DUsage = 3
class IDirect3DDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice'
    _iid_ = Guid('{a37624ab-8d5f-4650-9d3e-9eae3d9bc670}')
    @winrt_commethod(6)
    def Trim(self) -> Void: ...
class IDirect3DSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface'
    _iid_ = Guid('{0bf4a146-13c1-4694-bee3-7abf15eaf586}')
    @winrt_commethod(6)
    def get_Description(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.Direct3DSurfaceDescription: ...
    Description = property(get_Description, None)


make_ready(__name__)
