from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Graphics.DirectX
import Windows.Graphics.DirectX.Direct3D11
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    Format: Windows.Graphics.DirectX.DirectXPixelFormat
    MultisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription
Direct3DUsage = Int32
Direct3DUsage_Default: Direct3DUsage = 0
Direct3DUsage_Immutable: Direct3DUsage = 1
Direct3DUsage_Dynamic: Direct3DUsage = 2
Direct3DUsage_Staging: Direct3DUsage = 3
class IDirect3DDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a37624ab-8d5f-4650-9d-3e-9e-ae-3d-9b-c6-70')
    @winrt_commethod(6)
    def Trim(self) -> Void: ...
class IDirect3DSurface(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0bf4a146-13c1-4694-be-e3-7a-bf-15-ea-f5-86')
    @winrt_commethod(6)
    def get_Description(self) -> Windows.Graphics.DirectX.Direct3D11.Direct3DSurfaceDescription: ...
    Description = property(get_Description, None)
make_head(_module, 'Direct3DMultisampleDescription')
make_head(_module, 'Direct3DSurfaceDescription')
make_head(_module, 'IDirect3DDevice')
make_head(_module, 'IDirect3DSurface')
