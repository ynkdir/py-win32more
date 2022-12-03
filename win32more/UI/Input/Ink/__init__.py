from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Input.Ink
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
def _define_IInkCommitRequestHandler_head():
    class IInkCommitRequestHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('fabea3fc-b108-45b6-a9-fc-8d-08-fa-9f-85-cf')
    return IInkCommitRequestHandler
def _define_IInkCommitRequestHandler():
    IInkCommitRequestHandler = win32more.UI.Input.Ink.IInkCommitRequestHandler_head
    IInkCommitRequestHandler.OnCommitRequested = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnCommitRequested', ()))
    win32more.System.Com.IUnknown
    return IInkCommitRequestHandler
def _define_IInkD2DRenderer_head():
    class IInkD2DRenderer(win32more.System.Com.IUnknown_head):
        Guid = Guid('407fb1de-f85a-4150-97-cf-b7-fb-27-4f-b4-f8')
    return IInkD2DRenderer
def _define_IInkD2DRenderer():
    IInkD2DRenderer = win32more.UI.Input.Ink.IInkD2DRenderer_head
    IInkD2DRenderer.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL)(3, 'Draw', ((1, 'pD2D1DeviceContext'),(1, 'pInkStrokeIterable'),(1, 'fHighContrast'),)))
    win32more.System.Com.IUnknown
    return IInkD2DRenderer
def _define_IInkD2DRenderer2_head():
    class IInkD2DRenderer2(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a95dcd9-4578-4b71-b2-0b-bf-66-4d-4b-fe-ee')
    return IInkD2DRenderer2
def _define_IInkD2DRenderer2():
    IInkD2DRenderer2 = win32more.UI.Input.Ink.IInkD2DRenderer2_head
    IInkD2DRenderer2.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT)(3, 'Draw', ((1, 'pD2D1DeviceContext'),(1, 'pInkStrokeIterable'),(1, 'highContrastAdjustment'),)))
    win32more.System.Com.IUnknown
    return IInkD2DRenderer2
def _define_IInkDesktopHost_head():
    class IInkDesktopHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ce7d875-a981-4140-a1-ff-ad-93-25-8e-8d-59')
    return IInkDesktopHost
def _define_IInkDesktopHost():
    IInkDesktopHost = win32more.UI.Input.Ink.IInkDesktopHost_head
    IInkDesktopHost.QueueWorkItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ink.IInkHostWorkItem_head)(3, 'QueueWorkItem', ((1, 'workItem'),)))
    IInkDesktopHost.CreateInkPresenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(4, 'CreateInkPresenter', ((1, 'riid'),(1, 'ppv'),)))
    IInkDesktopHost.CreateAndInitializeInkPresenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,Single,Single,POINTER(Guid),POINTER(c_void_p))(5, 'CreateAndInitializeInkPresenter', ((1, 'rootVisual'),(1, 'width'),(1, 'height'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IInkDesktopHost
def _define_IInkHostWorkItem_head():
    class IInkHostWorkItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('ccda0a9a-1b78-4632-bb-96-97-80-06-62-e2-6c')
    return IInkHostWorkItem
def _define_IInkHostWorkItem():
    IInkHostWorkItem = win32more.UI.Input.Ink.IInkHostWorkItem_head
    IInkHostWorkItem.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IInkHostWorkItem
def _define_IInkPresenterDesktop_head():
    class IInkPresenterDesktop(win32more.System.Com.IUnknown_head):
        Guid = Guid('73f3c0d9-2e8b-48f3-89-5e-20-cb-d2-7b-72-3b')
    return IInkPresenterDesktop
def _define_IInkPresenterDesktop():
    IInkPresenterDesktop = win32more.UI.Input.Ink.IInkPresenterDesktop_head
    IInkPresenterDesktop.SetRootVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head)(3, 'SetRootVisual', ((1, 'rootVisual'),(1, 'device'),)))
    IInkPresenterDesktop.SetCommitRequestHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ink.IInkCommitRequestHandler_head)(4, 'SetCommitRequestHandler', ((1, 'handler'),)))
    IInkPresenterDesktop.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),POINTER(Single))(5, 'GetSize', ((1, 'width'),(1, 'height'),)))
    IInkPresenterDesktop.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(6, 'SetSize', ((1, 'width'),(1, 'height'),)))
    IInkPresenterDesktop.OnHighContrastChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'OnHighContrastChanged', ()))
    win32more.System.Com.IUnknown
    return IInkPresenterDesktop
INK_HIGH_CONTRAST_ADJUSTMENT = Int32
USE_SYSTEM_COLORS_WHEN_NECESSARY = 0
USE_SYSTEM_COLORS = 1
USE_ORIGINAL_COLORS = 2
InkD2DRenderer = Guid('4044e60c-7b01-4671-a9-7c-04-e0-21-0a-07-a5')
InkDesktopHost = Guid('062584a6-f830-4bdc-a4-d2-0a-10-ab-06-2b-1d')
__all__ = [
    "IInkCommitRequestHandler",
    "IInkD2DRenderer",
    "IInkD2DRenderer2",
    "IInkDesktopHost",
    "IInkHostWorkItem",
    "IInkPresenterDesktop",
    "INK_HIGH_CONTRAST_ADJUSTMENT",
    "InkD2DRenderer",
    "InkDesktopHost",
    "USE_ORIGINAL_COLORS",
    "USE_SYSTEM_COLORS",
    "USE_SYSTEM_COLORS_WHEN_NECESSARY",
]
