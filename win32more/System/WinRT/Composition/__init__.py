from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Composition
import win32more.UI.Input.Pointer
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_ICompositionCapabilitiesInteropFactory_head():
    class ICompositionCapabilitiesInteropFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('2c9db356-e70d-4642-82-98-bc-4a-a5-b4-86-5c')
    return ICompositionCapabilitiesInteropFactory
def _define_ICompositionCapabilitiesInteropFactory():
    ICompositionCapabilitiesInteropFactory = win32more.System.WinRT.Composition.ICompositionCapabilitiesInteropFactory_head
    ICompositionCapabilitiesInteropFactory.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(MissingType))(6, 'GetForWindow', ((1, 'hwnd'),(1, 'result'),)))
    win32more.System.WinRT.IInspectable
    return ICompositionCapabilitiesInteropFactory
def _define_ICompositionDrawingSurfaceInterop_head():
    class ICompositionDrawingSurfaceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd04e6e3-fe0c-4c3c-ab-19-a0-76-01-a5-76-ee')
    return ICompositionDrawingSurfaceInterop
def _define_ICompositionDrawingSurfaceInterop():
    ICompositionDrawingSurfaceInterop = win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop_head
    ICompositionDrawingSurfaceInterop.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.POINT_head))(3, 'BeginDraw', ((1, 'updateRect'),(1, 'iid'),(1, 'updateObject'),(1, 'updateOffset'),)))
    ICompositionDrawingSurfaceInterop.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'EndDraw', ()))
    ICompositionDrawingSurfaceInterop.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.SIZE)(5, 'Resize', ((1, 'sizePixels'),)))
    ICompositionDrawingSurfaceInterop.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),Int32,Int32)(6, 'Scroll', ((1, 'scrollRect'),(1, 'clipRect'),(1, 'offsetX'),(1, 'offsetY'),)))
    ICompositionDrawingSurfaceInterop.ResumeDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'ResumeDraw', ()))
    ICompositionDrawingSurfaceInterop.SuspendDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'SuspendDraw', ()))
    win32more.System.Com.IUnknown
    return ICompositionDrawingSurfaceInterop
def _define_ICompositionDrawingSurfaceInterop2_head():
    class ICompositionDrawingSurfaceInterop2(win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop_head):
        Guid = Guid('41e64aae-98c0-4239-8e-95-a3-30-dd-6a-a1-8b')
    return ICompositionDrawingSurfaceInterop2
def _define_ICompositionDrawingSurfaceInterop2():
    ICompositionDrawingSurfaceInterop2 = win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop2_head
    ICompositionDrawingSurfaceInterop2.CopySurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,Int32,Int32,POINTER(win32more.Foundation.RECT_head))(9, 'CopySurface', ((1, 'destinationResource'),(1, 'destinationOffsetX'),(1, 'destinationOffsetY'),(1, 'sourceRectangle'),)))
    win32more.System.WinRT.Composition.ICompositionDrawingSurfaceInterop
    return ICompositionDrawingSurfaceInterop2
def _define_ICompositionGraphicsDeviceInterop_head():
    class ICompositionGraphicsDeviceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('a116ff71-f8bf-4c8a-9c-98-70-77-9a-32-a9-c8')
    return ICompositionGraphicsDeviceInterop
def _define_ICompositionGraphicsDeviceInterop():
    ICompositionGraphicsDeviceInterop = win32more.System.WinRT.Composition.ICompositionGraphicsDeviceInterop_head
    ICompositionGraphicsDeviceInterop.GetRenderingDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetRenderingDevice', ((1, 'value'),)))
    ICompositionGraphicsDeviceInterop.SetRenderingDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'SetRenderingDevice', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return ICompositionGraphicsDeviceInterop
def _define_ICompositorDesktopInterop_head():
    class ICompositorDesktopInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('29e691fa-4567-4dca-b3-19-d0-f2-07-eb-68-07')
    return ICompositorDesktopInterop
def _define_ICompositorDesktopInterop():
    ICompositorDesktopInterop = win32more.System.WinRT.Composition.ICompositorDesktopInterop_head
    ICompositorDesktopInterop.CreateDesktopWindowTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BOOL,POINTER(MissingType))(3, 'CreateDesktopWindowTarget', ((1, 'hwndTarget'),(1, 'isTopmost'),(1, 'result'),)))
    ICompositorDesktopInterop.EnsureOnThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'EnsureOnThread', ((1, 'threadId'),)))
    win32more.System.Com.IUnknown
    return ICompositorDesktopInterop
def _define_ICompositorInterop_head():
    class ICompositorInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('25297d5c-3ad4-4c9c-b5-cf-e3-6a-38-51-23-30')
    return ICompositorInterop
def _define_ICompositorInterop():
    ICompositorInterop = win32more.System.WinRT.Composition.ICompositorInterop_head
    ICompositorInterop.CreateCompositionSurfaceForHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(MissingType))(3, 'CreateCompositionSurfaceForHandle', ((1, 'swapChain'),(1, 'result'),)))
    ICompositorInterop.CreateCompositionSurfaceForSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(MissingType))(4, 'CreateCompositionSurfaceForSwapChain', ((1, 'swapChain'),(1, 'result'),)))
    ICompositorInterop.CreateGraphicsDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(MissingType))(5, 'CreateGraphicsDevice', ((1, 'renderingDevice'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return ICompositorInterop
def _define_IDesktopWindowTargetInterop_head():
    class IDesktopWindowTargetInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('35dbf59e-e3f9-45b0-81-e7-fe-75-f4-14-5d-c9')
    return IDesktopWindowTargetInterop
def _define_IDesktopWindowTargetInterop():
    IDesktopWindowTargetInterop = win32more.System.WinRT.Composition.IDesktopWindowTargetInterop_head
    IDesktopWindowTargetInterop.get_Hwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(3, 'get_Hwnd', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IDesktopWindowTargetInterop
def _define_ISwapChainInterop_head():
    class ISwapChainInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('26f496a0-7f38-45fb-88-f7-fa-aa-be-67-dd-59')
    return ISwapChainInterop
def _define_ISwapChainInterop():
    ISwapChainInterop = win32more.System.WinRT.Composition.ISwapChainInterop_head
    ISwapChainInterop.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetSwapChain', ((1, 'swapChain'),)))
    win32more.System.Com.IUnknown
    return ISwapChainInterop
def _define_IVisualInteractionSourceInterop_head():
    class IVisualInteractionSourceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('11f62cd1-2f9d-42d3-b0-5f-d6-79-0d-9e-9f-8e')
    return IVisualInteractionSourceInterop
def _define_IVisualInteractionSourceInterop():
    IVisualInteractionSourceInterop = win32more.System.WinRT.Composition.IVisualInteractionSourceInterop_head
    IVisualInteractionSourceInterop.TryRedirectForManipulation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head))(3, 'TryRedirectForManipulation', ((1, 'pointerInfo'),)))
    win32more.System.Com.IUnknown
    return IVisualInteractionSourceInterop
__all__ = [
    "ICompositionCapabilitiesInteropFactory",
    "ICompositionDrawingSurfaceInterop",
    "ICompositionDrawingSurfaceInterop2",
    "ICompositionGraphicsDeviceInterop",
    "ICompositorDesktopInterop",
    "ICompositorInterop",
    "IDesktopWindowTargetInterop",
    "ISwapChainInterop",
    "IVisualInteractionSourceInterop",
]
