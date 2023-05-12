from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Graphics
import Windows.Graphics.Capture
import Windows.Graphics.DirectX
import Windows.Graphics.DirectX.Direct3D11
import Windows.Security.Authorization.AppCapabilityAccess
import Windows.System
import Windows.UI
import Windows.UI.Composition
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Direct3D11CaptureFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Capture.IDirect3D11CaptureFrame
    _classid_ = 'Windows.Graphics.Capture.Direct3D11CaptureFrame'
    @winrt_mixinmethod
    def get_Surface(self: Windows.Graphics.Capture.IDirect3D11CaptureFrame) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: Windows.Graphics.Capture.IDirect3D11CaptureFrame) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ContentSize(self: Windows.Graphics.Capture.IDirect3D11CaptureFrame) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Surface = property(get_Surface, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
    ContentSize = property(get_ContentSize, None)
class Direct3D11CaptureFramePool(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Capture.IDirect3D11CaptureFramePool
    _classid_ = 'Windows.Graphics.Capture.Direct3D11CaptureFramePool'
    @winrt_mixinmethod
    def Recreate(self: Windows.Graphics.Capture.IDirect3D11CaptureFramePool, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_mixinmethod
    def TryGetNextFrame(self: Windows.Graphics.Capture.IDirect3D11CaptureFramePool) -> Windows.Graphics.Capture.Direct3D11CaptureFrame: ...
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Graphics.Capture.IDirect3D11CaptureFramePool, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Capture.Direct3D11CaptureFramePool, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Graphics.Capture.IDirect3D11CaptureFramePool, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateCaptureSession(self: Windows.Graphics.Capture.IDirect3D11CaptureFramePool, item: Windows.Graphics.Capture.GraphicsCaptureItem) -> Windows.Graphics.Capture.GraphicsCaptureSession: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.Graphics.Capture.IDirect3D11CaptureFramePool) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFreeThreaded(cls: Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics2, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: Windows.Graphics.SizeInt32) -> Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
    @winrt_classmethod
    def Create(cls: Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: Windows.Graphics.SizeInt32) -> Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class GraphicsCaptureAccess(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.GraphicsCaptureAccess'
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Graphics.Capture.IGraphicsCaptureAccessStatics, request: Windows.Graphics.Capture.GraphicsCaptureAccessKind) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
GraphicsCaptureAccessKind = Int32
GraphicsCaptureAccessKind_Borderless: GraphicsCaptureAccessKind = 0
GraphicsCaptureAccessKind_Programmatic: GraphicsCaptureAccessKind = 1
class GraphicsCaptureItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Capture.IGraphicsCaptureItem
    _classid_ = 'Windows.Graphics.Capture.GraphicsCaptureItem'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Capture.IGraphicsCaptureItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Graphics.Capture.IGraphicsCaptureItem) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Graphics.Capture.IGraphicsCaptureItem, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Capture.GraphicsCaptureItem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Graphics.Capture.IGraphicsCaptureItem, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryCreateFromWindowId(cls: Windows.Graphics.Capture.IGraphicsCaptureItemStatics2, windowId: Windows.UI.WindowId) -> Windows.Graphics.Capture.GraphicsCaptureItem: ...
    @winrt_classmethod
    def TryCreateFromDisplayId(cls: Windows.Graphics.Capture.IGraphicsCaptureItemStatics2, displayId: Windows.Graphics.DisplayId) -> Windows.Graphics.Capture.GraphicsCaptureItem: ...
    @winrt_classmethod
    def CreateFromVisual(cls: Windows.Graphics.Capture.IGraphicsCaptureItemStatics, visual: Windows.UI.Composition.Visual) -> Windows.Graphics.Capture.GraphicsCaptureItem: ...
    DisplayName = property(get_DisplayName, None)
    Size = property(get_Size, None)
class GraphicsCapturePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Capture.IGraphicsCapturePicker
    _classid_ = 'Windows.Graphics.Capture.GraphicsCapturePicker'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Graphics.Capture.GraphicsCapturePicker: ...
    @winrt_mixinmethod
    def PickSingleItemAsync(self: Windows.Graphics.Capture.IGraphicsCapturePicker) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Capture.GraphicsCaptureItem]: ...
class GraphicsCaptureSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Capture.IGraphicsCaptureSession
    _classid_ = 'Windows.Graphics.Capture.GraphicsCaptureSession'
    @winrt_mixinmethod
    def StartCapture(self: Windows.Graphics.Capture.IGraphicsCaptureSession) -> Void: ...
    @winrt_mixinmethod
    def get_IsCursorCaptureEnabled(self: Windows.Graphics.Capture.IGraphicsCaptureSession2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCursorCaptureEnabled(self: Windows.Graphics.Capture.IGraphicsCaptureSession2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBorderRequired(self: Windows.Graphics.Capture.IGraphicsCaptureSession3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBorderRequired(self: Windows.Graphics.Capture.IGraphicsCaptureSession3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Graphics.Capture.IGraphicsCaptureSessionStatics) -> Boolean: ...
    IsCursorCaptureEnabled = property(get_IsCursorCaptureEnabled, put_IsCursorCaptureEnabled)
    IsBorderRequired = property(get_IsBorderRequired, put_IsBorderRequired)
class IDirect3D11CaptureFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFrame'
    _iid_ = Guid('{fa50c623-38da-4b32-acf3-fa9734ad800e}')
    @winrt_commethod(6)
    def get_Surface(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_commethod(7)
    def get_SystemRelativeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_ContentSize(self) -> Windows.Graphics.SizeInt32: ...
    Surface = property(get_Surface, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
    ContentSize = property(get_ContentSize, None)
class IDirect3D11CaptureFramePool(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFramePool'
    _iid_ = Guid('{24eb6d22-1975-422e-82e7-780dbd8ddf24}')
    @winrt_commethod(6)
    def Recreate(self, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_commethod(7)
    def TryGetNextFrame(self) -> Windows.Graphics.Capture.Direct3D11CaptureFrame: ...
    @winrt_commethod(8)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Capture.Direct3D11CaptureFramePool, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def CreateCaptureSession(self, item: Windows.Graphics.Capture.GraphicsCaptureItem) -> Windows.Graphics.Capture.GraphicsCaptureSession: ...
    @winrt_commethod(11)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IDirect3D11CaptureFramePoolStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics'
    _iid_ = Guid('{7784056a-67aa-4d53-ae54-1088d5a8ca21}')
    @winrt_commethod(6)
    def Create(self, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: Windows.Graphics.SizeInt32) -> Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
class IDirect3D11CaptureFramePoolStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics2'
    _iid_ = Guid('{589b103f-6bbc-5df5-a991-02e28b3b66d5}')
    @winrt_commethod(6)
    def CreateFreeThreaded(self, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: Windows.Graphics.SizeInt32) -> Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
class IGraphicsCaptureAccessStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureAccessStatics'
    _iid_ = Guid('{743ed370-06ec-5040-a58a-901f0f757095}')
    @winrt_commethod(6)
    def RequestAccessAsync(self, request: Windows.Graphics.Capture.GraphicsCaptureAccessKind) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
class IGraphicsCaptureItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureItem'
    _iid_ = Guid('{79c3f95b-31f7-4ec2-a464-632ef5d30760}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Size(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(8)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Capture.GraphicsCaptureItem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayName = property(get_DisplayName, None)
    Size = property(get_Size, None)
class IGraphicsCaptureItemStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureItemStatics'
    _iid_ = Guid('{a87ebea5-457c-5788-ab47-0cf1d3637e74}')
    @winrt_commethod(6)
    def CreateFromVisual(self, visual: Windows.UI.Composition.Visual) -> Windows.Graphics.Capture.GraphicsCaptureItem: ...
class IGraphicsCaptureItemStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureItemStatics2'
    _iid_ = Guid('{3b92acc9-e584-5862-bf5c-9c316c6d2dbb}')
    @winrt_commethod(6)
    def TryCreateFromWindowId(self, windowId: Windows.UI.WindowId) -> Windows.Graphics.Capture.GraphicsCaptureItem: ...
    @winrt_commethod(7)
    def TryCreateFromDisplayId(self, displayId: Windows.Graphics.DisplayId) -> Windows.Graphics.Capture.GraphicsCaptureItem: ...
class IGraphicsCapturePicker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCapturePicker'
    _iid_ = Guid('{5a1711b3-ad79-4b4a-9336-1318fdde3539}')
    @winrt_commethod(6)
    def PickSingleItemAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Capture.GraphicsCaptureItem]: ...
class IGraphicsCaptureSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession'
    _iid_ = Guid('{814e42a9-f70f-4ad7-939b-fddcc6eb880d}')
    @winrt_commethod(6)
    def StartCapture(self) -> Void: ...
class IGraphicsCaptureSession2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession2'
    _iid_ = Guid('{2c39ae40-7d2e-5044-804e-8b6799d4cf9e}')
    @winrt_commethod(6)
    def get_IsCursorCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsCursorCaptureEnabled(self, value: Boolean) -> Void: ...
    IsCursorCaptureEnabled = property(get_IsCursorCaptureEnabled, put_IsCursorCaptureEnabled)
class IGraphicsCaptureSession3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession3'
    _iid_ = Guid('{f2cdd966-22ae-5ea1-9596-3a289344c3be}')
    @winrt_commethod(6)
    def get_IsBorderRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsBorderRequired(self, value: Boolean) -> Void: ...
    IsBorderRequired = property(get_IsBorderRequired, put_IsBorderRequired)
class IGraphicsCaptureSessionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSessionStatics'
    _iid_ = Guid('{2224a540-5974-49aa-b232-0882536f4cb5}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
make_head(_module, 'Direct3D11CaptureFrame')
make_head(_module, 'Direct3D11CaptureFramePool')
make_head(_module, 'GraphicsCaptureAccess')
make_head(_module, 'GraphicsCaptureItem')
make_head(_module, 'GraphicsCapturePicker')
make_head(_module, 'GraphicsCaptureSession')
make_head(_module, 'IDirect3D11CaptureFrame')
make_head(_module, 'IDirect3D11CaptureFramePool')
make_head(_module, 'IDirect3D11CaptureFramePoolStatics')
make_head(_module, 'IDirect3D11CaptureFramePoolStatics2')
make_head(_module, 'IGraphicsCaptureAccessStatics')
make_head(_module, 'IGraphicsCaptureItem')
make_head(_module, 'IGraphicsCaptureItemStatics')
make_head(_module, 'IGraphicsCaptureItemStatics2')
make_head(_module, 'IGraphicsCapturePicker')
make_head(_module, 'IGraphicsCaptureSession')
make_head(_module, 'IGraphicsCaptureSession2')
make_head(_module, 'IGraphicsCaptureSession3')
make_head(_module, 'IGraphicsCaptureSessionStatics')
