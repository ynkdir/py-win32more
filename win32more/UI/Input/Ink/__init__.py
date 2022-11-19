from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Input.Ink

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
InkDesktopHost = Guid('062584a6-f830-4bdc-a4d2-0a10ab062b1d')
def _define_IInkCommitRequestHandler_head():
    class IInkCommitRequestHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('fabea3fc-b108-45b6-a9fc-8d08fa9f85cf')
    return IInkCommitRequestHandler
def _define_IInkCommitRequestHandler():
    IInkCommitRequestHandler = win32more.UI.Input.Ink.IInkCommitRequestHandler_head
    IInkCommitRequestHandler.OnCommitRequested = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnCommitRequested', ()))
    win32more.System.Com.IUnknown
    return IInkCommitRequestHandler
def _define_IInkPresenterDesktop_head():
    class IInkPresenterDesktop(win32more.System.Com.IUnknown_head):
        Guid = Guid('73f3c0d9-2e8b-48f3-895e-20cbd27b723b')
    return IInkPresenterDesktop
def _define_IInkPresenterDesktop():
    IInkPresenterDesktop = win32more.UI.Input.Ink.IInkPresenterDesktop_head
    IInkPresenterDesktop.SetRootVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetRootVisual', ((1, 'rootVisual'),(1, 'device'),)))
    IInkPresenterDesktop.SetCommitRequestHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ink.IInkCommitRequestHandler_head, use_last_error=False)(4, 'SetCommitRequestHandler', ((1, 'handler'),)))
    IInkPresenterDesktop.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),POINTER(Single), use_last_error=False)(5, 'GetSize', ((1, 'width'),(1, 'height'),)))
    IInkPresenterDesktop.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single, use_last_error=False)(6, 'SetSize', ((1, 'width'),(1, 'height'),)))
    IInkPresenterDesktop.OnHighContrastChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'OnHighContrastChanged', ()))
    win32more.System.Com.IUnknown
    return IInkPresenterDesktop
def _define_IInkHostWorkItem_head():
    class IInkHostWorkItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('ccda0a9a-1b78-4632-bb96-97800662e26c')
    return IInkHostWorkItem
def _define_IInkHostWorkItem():
    IInkHostWorkItem = win32more.UI.Input.Ink.IInkHostWorkItem_head
    IInkHostWorkItem.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IInkHostWorkItem
def _define_IInkDesktopHost_head():
    class IInkDesktopHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ce7d875-a981-4140-a1ff-ad93258e8d59')
    return IInkDesktopHost
def _define_IInkDesktopHost():
    IInkDesktopHost = win32more.UI.Input.Ink.IInkDesktopHost_head
    IInkDesktopHost.QueueWorkItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ink.IInkHostWorkItem_head, use_last_error=False)(3, 'QueueWorkItem', ((1, 'workItem'),)))
    IInkDesktopHost.CreateInkPresenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'CreateInkPresenter', ((1, 'riid'),(1, 'ppv'),)))
    IInkDesktopHost.CreateAndInitializeInkPresenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,Single,Single,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'CreateAndInitializeInkPresenter', ((1, 'rootVisual'),(1, 'width'),(1, 'height'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IInkDesktopHost
InkD2DRenderer = Guid('4044e60c-7b01-4671-a97c-04e0210a07a5')
INK_HIGH_CONTRAST_ADJUSTMENT = Int32
USE_SYSTEM_COLORS_WHEN_NECESSARY = 0
USE_SYSTEM_COLORS = 1
USE_ORIGINAL_COLORS = 2
def _define_IInkD2DRenderer_head():
    class IInkD2DRenderer(win32more.System.Com.IUnknown_head):
        Guid = Guid('407fb1de-f85a-4150-97cf-b7fb274fb4f8')
    return IInkD2DRenderer
def _define_IInkD2DRenderer():
    IInkD2DRenderer = win32more.UI.Input.Ink.IInkD2DRenderer_head
    IInkD2DRenderer.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL, use_last_error=False)(3, 'Draw', ((1, 'pD2D1DeviceContext'),(1, 'pInkStrokeIterable'),(1, 'fHighContrast'),)))
    win32more.System.Com.IUnknown
    return IInkD2DRenderer
def _define_IInkD2DRenderer2_head():
    class IInkD2DRenderer2(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a95dcd9-4578-4b71-b20b-bf664d4bfeee')
    return IInkD2DRenderer2
def _define_IInkD2DRenderer2():
    IInkD2DRenderer2 = win32more.UI.Input.Ink.IInkD2DRenderer2_head
    IInkD2DRenderer2.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT, use_last_error=False)(3, 'Draw', ((1, 'pD2D1DeviceContext'),(1, 'pInkStrokeIterable'),(1, 'highContrastAdjustment'),)))
    win32more.System.Com.IUnknown
    return IInkD2DRenderer2
__all__ = [
    "InkDesktopHost",
    "IInkCommitRequestHandler",
    "IInkPresenterDesktop",
    "IInkHostWorkItem",
    "IInkDesktopHost",
    "InkD2DRenderer",
    "INK_HIGH_CONTRAST_ADJUSTMENT",
    "USE_SYSTEM_COLORS_WHEN_NECESSARY",
    "USE_SYSTEM_COLORS",
    "USE_ORIGINAL_COLORS",
    "IInkD2DRenderer",
    "IInkD2DRenderer2",
]
