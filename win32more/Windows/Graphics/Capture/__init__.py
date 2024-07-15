from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Graphics.Capture
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Security.Authorization.AppCapabilityAccess
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Composition
import win32more.Windows.Win32.System.WinRT
class Direct3D11CaptureFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFrame
    _classid_ = 'Windows.Graphics.Capture.Direct3D11CaptureFrame'
    @winrt_mixinmethod
    def get_Surface(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFrame) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFrame) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ContentSize(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFrame) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_DirtyRegions(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFrame2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.RectInt32]: ...
    @winrt_mixinmethod
    def get_DirtyRegionMode(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFrame2) -> win32more.Windows.Graphics.Capture.GraphicsCaptureDirtyRegionMode: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ContentSize = property(get_ContentSize, None)
    DirtyRegionMode = property(get_DirtyRegionMode, None)
    DirtyRegions = property(get_DirtyRegions, None)
    Surface = property(get_Surface, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
class Direct3D11CaptureFramePool(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool
    _classid_ = 'Windows.Graphics.Capture.Direct3D11CaptureFramePool'
    @winrt_mixinmethod
    def Recreate(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_mixinmethod
    def TryGetNextFrame(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool) -> win32more.Windows.Graphics.Capture.Direct3D11CaptureFrame: ...
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Capture.Direct3D11CaptureFramePool, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateCaptureSession(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool, item: win32more.Windows.Graphics.Capture.GraphicsCaptureItem) -> win32more.Windows.Graphics.Capture.GraphicsCaptureSession: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePool) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFreeThreaded(cls: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics2, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: win32more.Windows.Graphics.SizeInt32) -> win32more.Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: win32more.Windows.Graphics.SizeInt32) -> win32more.Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    FrameArrived = event()
class GraphicsCaptureAccess(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.GraphicsCaptureAccess'
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Graphics.Capture.IGraphicsCaptureAccessStatics, request: win32more.Windows.Graphics.Capture.GraphicsCaptureAccessKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
class GraphicsCaptureAccessKind(Enum, Int32):
    Borderless = 0
    Programmatic = 1
class GraphicsCaptureDirtyRegionMode(Enum, Int32):
    ReportOnly = 0
    ReportAndRender = 1
class GraphicsCaptureItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Capture.IGraphicsCaptureItem
    _classid_ = 'Windows.Graphics.Capture.GraphicsCaptureItem'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureItem) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureItem, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Capture.GraphicsCaptureItem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureItem, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryCreateFromWindowId(cls: win32more.Windows.Graphics.Capture.IGraphicsCaptureItemStatics2, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.Graphics.Capture.GraphicsCaptureItem: ...
    @winrt_classmethod
    def TryCreateFromDisplayId(cls: win32more.Windows.Graphics.Capture.IGraphicsCaptureItemStatics2, displayId: win32more.Windows.Graphics.DisplayId) -> win32more.Windows.Graphics.Capture.GraphicsCaptureItem: ...
    @winrt_classmethod
    def CreateFromVisual(cls: win32more.Windows.Graphics.Capture.IGraphicsCaptureItemStatics, visual: win32more.Windows.UI.Composition.Visual) -> win32more.Windows.Graphics.Capture.GraphicsCaptureItem: ...
    DisplayName = property(get_DisplayName, None)
    Size = property(get_Size, None)
    Closed = event()
class GraphicsCapturePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Capture.IGraphicsCapturePicker
    _classid_ = 'Windows.Graphics.Capture.GraphicsCapturePicker'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Capture.GraphicsCapturePicker.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Capture.GraphicsCapturePicker: ...
    @winrt_mixinmethod
    def PickSingleItemAsync(self: win32more.Windows.Graphics.Capture.IGraphicsCapturePicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Capture.GraphicsCaptureItem]: ...
class GraphicsCaptureSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession
    _classid_ = 'Windows.Graphics.Capture.GraphicsCaptureSession'
    @winrt_mixinmethod
    def StartCapture(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession) -> Void: ...
    @winrt_mixinmethod
    def get_IsCursorCaptureEnabled(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCursorCaptureEnabled(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBorderRequired(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBorderRequired(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DirtyRegionMode(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession4) -> win32more.Windows.Graphics.Capture.GraphicsCaptureDirtyRegionMode: ...
    @winrt_mixinmethod
    def put_DirtyRegionMode(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession4, value: win32more.Windows.Graphics.Capture.GraphicsCaptureDirtyRegionMode) -> Void: ...
    @winrt_mixinmethod
    def get_MinUpdateInterval(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession5) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_MinUpdateInterval(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession5, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeSecondaryWindows(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession6) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeSecondaryWindows(self: win32more.Windows.Graphics.Capture.IGraphicsCaptureSession6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Graphics.Capture.IGraphicsCaptureSessionStatics) -> Boolean: ...
    DirtyRegionMode = property(get_DirtyRegionMode, put_DirtyRegionMode)
    IncludeSecondaryWindows = property(get_IncludeSecondaryWindows, put_IncludeSecondaryWindows)
    IsBorderRequired = property(get_IsBorderRequired, put_IsBorderRequired)
    IsCursorCaptureEnabled = property(get_IsCursorCaptureEnabled, put_IsCursorCaptureEnabled)
    MinUpdateInterval = property(get_MinUpdateInterval, put_MinUpdateInterval)
class IDirect3D11CaptureFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFrame'
    _iid_ = Guid('{fa50c623-38da-4b32-acf3-fa9734ad800e}')
    @winrt_commethod(6)
    def get_Surface(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_commethod(7)
    def get_SystemRelativeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_ContentSize(self) -> win32more.Windows.Graphics.SizeInt32: ...
    ContentSize = property(get_ContentSize, None)
    Surface = property(get_Surface, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
class IDirect3D11CaptureFrame2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFrame2'
    _iid_ = Guid('{37869cfa-2b48-5ebf-9afb-dffd805defdb}')
    @winrt_commethod(6)
    def get_DirtyRegions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.RectInt32]: ...
    @winrt_commethod(7)
    def get_DirtyRegionMode(self) -> win32more.Windows.Graphics.Capture.GraphicsCaptureDirtyRegionMode: ...
    DirtyRegionMode = property(get_DirtyRegionMode, None)
    DirtyRegions = property(get_DirtyRegions, None)
class IDirect3D11CaptureFramePool(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFramePool'
    _iid_ = Guid('{24eb6d22-1975-422e-82e7-780dbd8ddf24}')
    @winrt_commethod(6)
    def Recreate(self, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_commethod(7)
    def TryGetNextFrame(self) -> win32more.Windows.Graphics.Capture.Direct3D11CaptureFrame: ...
    @winrt_commethod(8)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Capture.Direct3D11CaptureFramePool, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def CreateCaptureSession(self, item: win32more.Windows.Graphics.Capture.GraphicsCaptureItem) -> win32more.Windows.Graphics.Capture.GraphicsCaptureSession: ...
    @winrt_commethod(11)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    FrameArrived = event()
class IDirect3D11CaptureFramePoolStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics'
    _iid_ = Guid('{7784056a-67aa-4d53-ae54-1088d5a8ca21}')
    @winrt_commethod(6)
    def Create(self, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: win32more.Windows.Graphics.SizeInt32) -> win32more.Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
class IDirect3D11CaptureFramePoolStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IDirect3D11CaptureFramePoolStatics2'
    _iid_ = Guid('{589b103f-6bbc-5df5-a991-02e28b3b66d5}')
    @winrt_commethod(6)
    def CreateFreeThreaded(self, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, numberOfBuffers: Int32, size: win32more.Windows.Graphics.SizeInt32) -> win32more.Windows.Graphics.Capture.Direct3D11CaptureFramePool: ...
class IGraphicsCaptureAccessStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureAccessStatics'
    _iid_ = Guid('{743ed370-06ec-5040-a58a-901f0f757095}')
    @winrt_commethod(6)
    def RequestAccessAsync(self, request: win32more.Windows.Graphics.Capture.GraphicsCaptureAccessKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
class IGraphicsCaptureItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureItem'
    _iid_ = Guid('{79c3f95b-31f7-4ec2-a464-632ef5d30760}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Size(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(8)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Capture.GraphicsCaptureItem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayName = property(get_DisplayName, None)
    Size = property(get_Size, None)
    Closed = event()
class IGraphicsCaptureItemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureItemStatics'
    _iid_ = Guid('{a87ebea5-457c-5788-ab47-0cf1d3637e74}')
    @winrt_commethod(6)
    def CreateFromVisual(self, visual: win32more.Windows.UI.Composition.Visual) -> win32more.Windows.Graphics.Capture.GraphicsCaptureItem: ...
class IGraphicsCaptureItemStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureItemStatics2'
    _iid_ = Guid('{3b92acc9-e584-5862-bf5c-9c316c6d2dbb}')
    @winrt_commethod(6)
    def TryCreateFromWindowId(self, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.Graphics.Capture.GraphicsCaptureItem: ...
    @winrt_commethod(7)
    def TryCreateFromDisplayId(self, displayId: win32more.Windows.Graphics.DisplayId) -> win32more.Windows.Graphics.Capture.GraphicsCaptureItem: ...
class IGraphicsCapturePicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCapturePicker'
    _iid_ = Guid('{5a1711b3-ad79-4b4a-9336-1318fdde3539}')
    @winrt_commethod(6)
    def PickSingleItemAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Capture.GraphicsCaptureItem]: ...
class IGraphicsCaptureSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession'
    _iid_ = Guid('{814e42a9-f70f-4ad7-939b-fddcc6eb880d}')
    @winrt_commethod(6)
    def StartCapture(self) -> Void: ...
class IGraphicsCaptureSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession2'
    _iid_ = Guid('{2c39ae40-7d2e-5044-804e-8b6799d4cf9e}')
    @winrt_commethod(6)
    def get_IsCursorCaptureEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsCursorCaptureEnabled(self, value: Boolean) -> Void: ...
    IsCursorCaptureEnabled = property(get_IsCursorCaptureEnabled, put_IsCursorCaptureEnabled)
class IGraphicsCaptureSession3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession3'
    _iid_ = Guid('{f2cdd966-22ae-5ea1-9596-3a289344c3be}')
    @winrt_commethod(6)
    def get_IsBorderRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsBorderRequired(self, value: Boolean) -> Void: ...
    IsBorderRequired = property(get_IsBorderRequired, put_IsBorderRequired)
class IGraphicsCaptureSession4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession4'
    _iid_ = Guid('{ae99813c-c257-5759-8ed0-668c9b557ed4}')
    @winrt_commethod(6)
    def get_DirtyRegionMode(self) -> win32more.Windows.Graphics.Capture.GraphicsCaptureDirtyRegionMode: ...
    @winrt_commethod(7)
    def put_DirtyRegionMode(self, value: win32more.Windows.Graphics.Capture.GraphicsCaptureDirtyRegionMode) -> Void: ...
    DirtyRegionMode = property(get_DirtyRegionMode, put_DirtyRegionMode)
class IGraphicsCaptureSession5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession5'
    _iid_ = Guid('{67c0ea62-1f85-5061-925a-239be0ac09cb}')
    @winrt_commethod(6)
    def get_MinUpdateInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_MinUpdateInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    MinUpdateInterval = property(get_MinUpdateInterval, put_MinUpdateInterval)
class IGraphicsCaptureSession6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSession6'
    _iid_ = Guid('{d7419236-be20-5e9f-bcd6-c4e98fd6afdc}')
    @winrt_commethod(6)
    def get_IncludeSecondaryWindows(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IncludeSecondaryWindows(self, value: Boolean) -> Void: ...
    IncludeSecondaryWindows = property(get_IncludeSecondaryWindows, put_IncludeSecondaryWindows)
class IGraphicsCaptureSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Capture.IGraphicsCaptureSessionStatics'
    _iid_ = Guid('{2224a540-5974-49aa-b232-0882536f4cb5}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...


make_ready(__name__)
