from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Win32.System.WinRT
class Direct3DBindings(Enum, UInt32):
    VertexBuffer = 1
    IndexBuffer = 2
    ConstantBuffer = 4
    ShaderResource = 8
    StreamOutput = 16
    RenderTarget = 32
    DepthStencil = 64
    UnorderedAccess = 128
    Decoder = 512
    VideoEncoder = 1024
class Direct3DMultisampleDescription(Structure):
    Count: Int32
    Quality: Int32
class Direct3DSurfaceDescription(Structure):
    Width: Int32
    Height: Int32
    Format: win32more.Windows.Graphics.DirectX.DirectXPixelFormat
    MultisampleDescription: win32more.Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription
class Direct3DUsage(Enum, Int32):
    Default = 0
    Immutable = 1
    Dynamic = 2
    Staging = 3
class IDirect3DDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice'
    _iid_ = Guid('{a37624ab-8d5f-4650-9d3e-9eae3d9bc670}')
    @winrt_commethod(6)
    def Trim(self) -> Void: ...
class IDirect3DSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface'
    _iid_ = Guid('{0bf4a146-13c1-4694-bee3-7abf15eaf586}')
    @winrt_commethod(6)
    def get_Description(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.Direct3DSurfaceDescription: ...
    Description = property(get_Description, None)


make_ready(__name__)
