from win32more.base import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Composition
import win32more.UI.Input.Pointer

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_ICompositionDrawingSurfaceInterop_head():
    class ICompositionDrawingSurfaceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd04e6e3-fe0c-4c3c-ab19-a07601a576ee')
    return ICompositionDrawingSurfaceInterop
def _define_ICompositionDrawingSurfaceInterop():
    ICompositionDrawingSurfaceInterop = win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop_head
    ICompositionDrawingSurfaceInterop.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.POINT_head), use_last_error=False)(3, 'BeginDraw', ((1, 'updateRect'),(1, 'iid'),(1, 'updateObject'),(1, 'updateOffset'),)))
    ICompositionDrawingSurfaceInterop.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'EndDraw', ()))
    ICompositionDrawingSurfaceInterop.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.SIZE, use_last_error=False)(5, 'Resize', ((1, 'sizePixels'),)))
    ICompositionDrawingSurfaceInterop.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),Int32,Int32, use_last_error=False)(6, 'Scroll', ((1, 'scrollRect'),(1, 'clipRect'),(1, 'offsetX'),(1, 'offsetY'),)))
    ICompositionDrawingSurfaceInterop.ResumeDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'ResumeDraw', ()))
    ICompositionDrawingSurfaceInterop.SuspendDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'SuspendDraw', ()))
    win32more.System.Com.IUnknown
    return ICompositionDrawingSurfaceInterop
def _define_ICompositionDrawingSurfaceInterop2_head():
    class ICompositionDrawingSurfaceInterop2(win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop_head):
        Guid = Guid('41e64aae-98c0-4239-8e95-a330dd6aa18b')
    return ICompositionDrawingSurfaceInterop2
def _define_ICompositionDrawingSurfaceInterop2():
    ICompositionDrawingSurfaceInterop2 = win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop2_head
    ICompositionDrawingSurfaceInterop2.CopySurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,Int32,Int32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(9, 'CopySurface', ((1, 'destinationResource'),(1, 'destinationOffsetX'),(1, 'destinationOffsetY'),(1, 'sourceRectangle'),)))
    win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop
    return ICompositionDrawingSurfaceInterop2
def _define_ICompositionGraphicsDeviceInterop_head():
    class ICompositionGraphicsDeviceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('a116ff71-f8bf-4c8a-9c98-70779a32a9c8')
    return ICompositionGraphicsDeviceInterop
def _define_ICompositionGraphicsDeviceInterop():
    ICompositionGraphicsDeviceInterop = win32more.System.WinRT.Composition.ICompositionGraphicsDeviceInterop_head
    ICompositionGraphicsDeviceInterop.GetRenderingDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'GetRenderingDevice', ((1, 'value'),)))
    ICompositionGraphicsDeviceInterop.SetRenderingDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'SetRenderingDevice', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return ICompositionGraphicsDeviceInterop
def _define_ICompositorInterop_head():
    class ICompositorInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('25297d5c-3ad4-4c9c-b5cf-e36a38512330')
    return ICompositorInterop
def _define_ICompositorInterop():
    ICompositorInterop = win32more.System.WinRT.Composition.ICompositorInterop_head
    ICompositorInterop.CreateCompositionSurfaceForHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,c_void_p, use_last_error=False)(3, 'CreateCompositionSurfaceForHandle', ((1, 'swapChain'),(1, 'result'),)))
    ICompositorInterop.CreateCompositionSurfaceForSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,c_void_p, use_last_error=False)(4, 'CreateCompositionSurfaceForSwapChain', ((1, 'swapChain'),(1, 'result'),)))
    ICompositorInterop.CreateGraphicsDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,c_void_p, use_last_error=False)(5, 'CreateGraphicsDevice', ((1, 'renderingDevice'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return ICompositorInterop
def _define_ISwapChainInterop_head():
    class ISwapChainInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('26f496a0-7f38-45fb-88f7-faaabe67dd59')
    return ISwapChainInterop
def _define_ISwapChainInterop():
    ISwapChainInterop = win32more.System.WinRT.Composition.ISwapChainInterop_head
    ISwapChainInterop.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetSwapChain', ((1, 'swapChain'),)))
    win32more.System.Com.IUnknown
    return ISwapChainInterop
def _define_IVisualInteractionSourceInterop_head():
    class IVisualInteractionSourceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('11f62cd1-2f9d-42d3-b05f-d6790d9e9f8e')
    return IVisualInteractionSourceInterop
def _define_IVisualInteractionSourceInterop():
    IVisualInteractionSourceInterop = win32more.System.WinRT.Composition.IVisualInteractionSourceInterop_head
    IVisualInteractionSourceInterop.TryRedirectForManipulation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head), use_last_error=False)(3, 'TryRedirectForManipulation', ((1, 'pointerInfo'),)))
    win32more.System.Com.IUnknown
    return IVisualInteractionSourceInterop
def _define_ICompositionCapabilitiesInteropFactory_head():
    class ICompositionCapabilitiesInteropFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('2c9db356-e70d-4642-8298-bc4aa5b4865c')
    return ICompositionCapabilitiesInteropFactory
def _define_ICompositionCapabilitiesInteropFactory():
    ICompositionCapabilitiesInteropFactory = win32more.System.WinRT.Composition.ICompositionCapabilitiesInteropFactory_head
    ICompositionCapabilitiesInteropFactory.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,c_void_p, use_last_error=False)(6, 'GetForWindow', ((1, 'hwnd'),(1, 'result'),)))
    win32more.System.WinRT.IInspectable
    return ICompositionCapabilitiesInteropFactory
def _define_ICompositorDesktopInterop_head():
    class ICompositorDesktopInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('29e691fa-4567-4dca-b319-d0f207eb6807')
    return ICompositorDesktopInterop
def _define_ICompositorDesktopInterop():
    ICompositorDesktopInterop = win32more.System.WinRT.Composition.ICompositorDesktopInterop_head
    ICompositorDesktopInterop.CreateDesktopWindowTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BOOL,c_void_p, use_last_error=False)(3, 'CreateDesktopWindowTarget', ((1, 'hwndTarget'),(1, 'isTopmost'),(1, 'result'),)))
    ICompositorDesktopInterop.EnsureOnThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'EnsureOnThread', ((1, 'threadId'),)))
    win32more.System.Com.IUnknown
    return ICompositorDesktopInterop
def _define_IDesktopWindowTargetInterop_head():
    class IDesktopWindowTargetInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('35dbf59e-e3f9-45b0-81e7-fe75f4145dc9')
    return IDesktopWindowTargetInterop
def _define_IDesktopWindowTargetInterop():
    IDesktopWindowTargetInterop = win32more.System.WinRT.Composition.IDesktopWindowTargetInterop_head
    IDesktopWindowTargetInterop.get_Hwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'get_Hwnd', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IDesktopWindowTargetInterop
__all__ = [
    "ICompositionDrawingSurfaceInterop",
    "ICompositionDrawingSurfaceInterop2",
    "ICompositionGraphicsDeviceInterop",
    "ICompositorInterop",
    "ISwapChainInterop",
    "IVisualInteractionSourceInterop",
    "ICompositionCapabilitiesInteropFactory",
    "ICompositorDesktopInterop",
    "IDesktopWindowTargetInterop",
]
