from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Composition
import win32more.Windows.Win32.UI.Input.Pointer
class ICompositionCapabilitiesInteropFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2c9db356-e70d-4642-8298-bc4aa5b4865c}')
    @commethod(6)
    def GetForWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, result: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICompositionDrawingSurfaceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd04e6e3-fe0c-4c3c-ab19-a07601a576ee}')
    @commethod(3)
    def BeginDraw(self, updateRect: POINTER(win32more.Windows.Win32.Foundation.RECT), iid: POINTER(Guid), updateObject: POINTER(VoidPtr), updateOffset: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndDraw(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Resize(self, sizePixels: win32more.Windows.Win32.Foundation.SIZE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Scroll(self, scrollRect: POINTER(win32more.Windows.Win32.Foundation.RECT), clipRect: POINTER(win32more.Windows.Win32.Foundation.RECT), offsetX: Int32, offsetY: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResumeDraw(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SuspendDraw(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICompositionDrawingSurfaceInterop2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.Composition.ICompositionDrawingSurfaceInterop
    _iid_ = Guid('{41e64aae-98c0-4239-8e95-a330dd6aa18b}')
    @commethod(9)
    def CopySurface(self, destinationResource: win32more.Windows.Win32.System.Com.IUnknown, destinationOffsetX: Int32, destinationOffsetY: Int32, sourceRectangle: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICompositionGraphicsDeviceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a116ff71-f8bf-4c8a-9c98-70779a32a9c8}')
    @commethod(3)
    def GetRenderingDevice(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRenderingDevice(self, value: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICompositorDesktopInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{29e691fa-4567-4dca-b319-d0f207eb6807}')
    @commethod(3)
    def CreateDesktopWindowTarget(self, hwndTarget: win32more.Windows.Win32.Foundation.HWND, isTopmost: win32more.Windows.Win32.Foundation.BOOL, result: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnsureOnThread(self, threadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICompositorInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25297d5c-3ad4-4c9c-b5cf-e36a38512330}')
    @commethod(3)
    def CreateCompositionSurfaceForHandle(self, swapChain: win32more.Windows.Win32.Foundation.HANDLE, result: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateCompositionSurfaceForSwapChain(self, swapChain: win32more.Windows.Win32.System.Com.IUnknown, result: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateGraphicsDevice(self, renderingDevice: win32more.Windows.Win32.System.Com.IUnknown, result: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDesktopWindowTargetInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{35dbf59e-e3f9-45b0-81e7-fe75f4145dc9}')
    @commethod(3)
    def get_Hwnd(self, value: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualInteractionSourceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11f62cd1-2f9d-42d3-b05f-d6790d9e9f8e}')
    @commethod(3)
    def TryRedirectForManipulation(self, pointerInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_ready(__name__)
