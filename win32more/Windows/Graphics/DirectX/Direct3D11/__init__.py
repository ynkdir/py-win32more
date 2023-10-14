from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Graphics.DirectX.Direct3D11
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
