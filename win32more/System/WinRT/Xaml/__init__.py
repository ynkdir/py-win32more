from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.System.WinRT.Xaml
import win32more.UI.WindowsAndMessaging
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
E_SURFACE_CONTENTS_LOST = 2150301728
def _define_IDesktopWindowXamlSourceNative_head():
    class IDesktopWindowXamlSourceNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('3cbcf1bf-2f76-4e9c-96-ab-e8-4b-37-97-25-54')
    return IDesktopWindowXamlSourceNative
def _define_IDesktopWindowXamlSourceNative():
    IDesktopWindowXamlSourceNative = win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative_head
    IDesktopWindowXamlSourceNative.AttachToWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(3, 'AttachToWindow', ((1, 'parentWnd'),)))
    IDesktopWindowXamlSourceNative.get_WindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(4, 'get_WindowHandle', ((1, 'hWnd'),)))
    win32more.System.Com.IUnknown
    return IDesktopWindowXamlSourceNative
def _define_IDesktopWindowXamlSourceNative2_head():
    class IDesktopWindowXamlSourceNative2(win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative_head):
        Guid = Guid('e3dcd8c7-3057-4692-99-c3-7b-77-20-af-da-31')
    return IDesktopWindowXamlSourceNative2
def _define_IDesktopWindowXamlSourceNative2():
    IDesktopWindowXamlSourceNative2 = win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative2_head
    IDesktopWindowXamlSourceNative2.PreTranslateMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),POINTER(win32more.Foundation.BOOL))(5, 'PreTranslateMessage', ((1, 'message'),(1, 'result'),)))
    win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative
    return IDesktopWindowXamlSourceNative2
def _define_IFindReferenceTargetsCallback_head():
    class IFindReferenceTargetsCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('04b3486c-4687-4229-8d-14-50-5a-b5-84-dd-88')
    return IFindReferenceTargetsCallback
def _define_IFindReferenceTargetsCallback():
    IFindReferenceTargetsCallback = win32more.System.WinRT.Xaml.IFindReferenceTargetsCallback_head
    IFindReferenceTargetsCallback.FoundTrackerTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IReferenceTrackerTarget_head)(3, 'FoundTrackerTarget', ((1, 'target'),)))
    win32more.System.Com.IUnknown
    return IFindReferenceTargetsCallback
def _define_IReferenceTracker_head():
    class IReferenceTracker(win32more.System.Com.IUnknown_head):
        Guid = Guid('11d3b13a-180e-4789-a8-be-77-12-88-28-93-e6')
    return IReferenceTracker
def _define_IReferenceTracker():
    IReferenceTracker = win32more.System.WinRT.Xaml.IReferenceTracker_head
    IReferenceTracker.ConnectFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'ConnectFromTrackerSource', ()))
    IReferenceTracker.DisconnectFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'DisconnectFromTrackerSource', ()))
    IReferenceTracker.FindTrackerTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IFindReferenceTargetsCallback_head)(5, 'FindTrackerTargets', ((1, 'callback'),)))
    IReferenceTracker.GetReferenceTrackerManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.Xaml.IReferenceTrackerManager_head))(6, 'GetReferenceTrackerManager', ((1, 'value'),)))
    IReferenceTracker.AddRefFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'AddRefFromTrackerSource', ()))
    IReferenceTracker.ReleaseFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'ReleaseFromTrackerSource', ()))
    IReferenceTracker.PegFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'PegFromTrackerSource', ()))
    win32more.System.Com.IUnknown
    return IReferenceTracker
def _define_IReferenceTrackerExtension_head():
    class IReferenceTrackerExtension(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e897caa-59d5-4613-8f-8c-f7-eb-d1-f3-99-b0')
    return IReferenceTrackerExtension
def _define_IReferenceTrackerExtension():
    IReferenceTrackerExtension = win32more.System.WinRT.Xaml.IReferenceTrackerExtension_head
    win32more.System.Com.IUnknown
    return IReferenceTrackerExtension
def _define_IReferenceTrackerHost_head():
    class IReferenceTrackerHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('29a71c6a-3c42-4416-a3-9d-e2-82-5a-07-a7-73')
    return IReferenceTrackerHost
def _define_IReferenceTrackerHost():
    IReferenceTrackerHost = win32more.System.WinRT.Xaml.IReferenceTrackerHost_head
    IReferenceTrackerHost.DisconnectUnusedReferenceSources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.XAML_REFERENCETRACKER_DISCONNECT)(3, 'DisconnectUnusedReferenceSources', ((1, 'options'),)))
    IReferenceTrackerHost.ReleaseDisconnectedReferenceSources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'ReleaseDisconnectedReferenceSources', ()))
    IReferenceTrackerHost.NotifyEndOfReferenceTrackingOnThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'NotifyEndOfReferenceTrackingOnThread', ()))
    IReferenceTrackerHost.GetTrackerTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.WinRT.Xaml.IReferenceTrackerTarget_head))(6, 'GetTrackerTarget', ((1, 'unknown'),(1, 'newReference'),)))
    IReferenceTrackerHost.AddMemoryPressure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64)(7, 'AddMemoryPressure', ((1, 'bytesAllocated'),)))
    IReferenceTrackerHost.RemoveMemoryPressure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64)(8, 'RemoveMemoryPressure', ((1, 'bytesAllocated'),)))
    win32more.System.Com.IUnknown
    return IReferenceTrackerHost
def _define_IReferenceTrackerManager_head():
    class IReferenceTrackerManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('3cf184b4-7ccb-4dda-84-55-7e-6c-e9-9a-32-98')
    return IReferenceTrackerManager
def _define_IReferenceTrackerManager():
    IReferenceTrackerManager = win32more.System.WinRT.Xaml.IReferenceTrackerManager_head
    IReferenceTrackerManager.ReferenceTrackingStarted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'ReferenceTrackingStarted', ()))
    IReferenceTrackerManager.FindTrackerTargetsCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte)(4, 'FindTrackerTargetsCompleted', ((1, 'findFailed'),)))
    IReferenceTrackerManager.ReferenceTrackingCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'ReferenceTrackingCompleted', ()))
    IReferenceTrackerManager.SetReferenceTrackerHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IReferenceTrackerHost_head)(6, 'SetReferenceTrackerHost', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IReferenceTrackerManager
def _define_IReferenceTrackerTarget_head():
    class IReferenceTrackerTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('64bd43f8-bfee-4ec4-b7-eb-29-35-15-8d-ae-21')
    return IReferenceTrackerTarget
def _define_IReferenceTrackerTarget():
    IReferenceTrackerTarget = win32more.System.WinRT.Xaml.IReferenceTrackerTarget_head
    IReferenceTrackerTarget.AddRefFromReferenceTracker = COMMETHOD(WINFUNCTYPE(UInt32,)(3, 'AddRefFromReferenceTracker', ()))
    IReferenceTrackerTarget.ReleaseFromReferenceTracker = COMMETHOD(WINFUNCTYPE(UInt32,)(4, 'ReleaseFromReferenceTracker', ()))
    IReferenceTrackerTarget.Peg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Peg', ()))
    IReferenceTrackerTarget.Unpeg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Unpeg', ()))
    win32more.System.Com.IUnknown
    return IReferenceTrackerTarget
def _define_ISurfaceImageSourceManagerNative_head():
    class ISurfaceImageSourceManagerNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c8798b7-1d88-4a0f-b5-9b-b9-3f-60-0d-e8-c8')
    return ISurfaceImageSourceManagerNative
def _define_ISurfaceImageSourceManagerNative():
    ISurfaceImageSourceManagerNative = win32more.System.WinRT.Xaml.ISurfaceImageSourceManagerNative_head
    ISurfaceImageSourceManagerNative.FlushAllSurfacesWithDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'FlushAllSurfacesWithDevice', ((1, 'device'),)))
    win32more.System.Com.IUnknown
    return ISurfaceImageSourceManagerNative
def _define_ISurfaceImageSourceNative_head():
    class ISurfaceImageSourceNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('f2e9edc1-d307-4525-98-86-0f-af-aa-44-16-3c')
    return ISurfaceImageSourceNative
def _define_ISurfaceImageSourceNative():
    ISurfaceImageSourceNative = win32more.System.WinRT.Xaml.ISurfaceImageSourceNative_head
    ISurfaceImageSourceNative.SetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head)(3, 'SetDevice', ((1, 'device'),)))
    ISurfaceImageSourceNative.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,POINTER(win32more.Graphics.Dxgi.IDXGISurface_head),POINTER(win32more.Foundation.POINT_head))(4, 'BeginDraw', ((1, 'updateRect'),(1, 'surface'),(1, 'offset'),)))
    ISurfaceImageSourceNative.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'EndDraw', ()))
    win32more.System.Com.IUnknown
    return ISurfaceImageSourceNative
def _define_ISurfaceImageSourceNativeWithD2D_head():
    class ISurfaceImageSourceNativeWithD2D(win32more.System.Com.IUnknown_head):
        Guid = Guid('54298223-41e1-4a41-9c-08-02-e8-25-68-64-a1')
    return ISurfaceImageSourceNativeWithD2D
def _define_ISurfaceImageSourceNativeWithD2D():
    ISurfaceImageSourceNativeWithD2D = win32more.System.WinRT.Xaml.ISurfaceImageSourceNativeWithD2D_head
    ISurfaceImageSourceNativeWithD2D.SetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetDevice', ((1, 'device'),)))
    ISurfaceImageSourceNativeWithD2D.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.POINT_head))(4, 'BeginDraw', ((1, 'updateRect'),(1, 'iid'),(1, 'updateObject'),(1, 'offset'),)))
    ISurfaceImageSourceNativeWithD2D.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'EndDraw', ()))
    ISurfaceImageSourceNativeWithD2D.SuspendDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'SuspendDraw', ()))
    ISurfaceImageSourceNativeWithD2D.ResumeDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'ResumeDraw', ()))
    win32more.System.Com.IUnknown
    return ISurfaceImageSourceNativeWithD2D
def _define_ISwapChainBackgroundPanelNative_head():
    class ISwapChainBackgroundPanelNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('43bebd4e-add5-4035-8f-85-56-08-d0-8e-9d-c9')
    return ISwapChainBackgroundPanelNative
def _define_ISwapChainBackgroundPanelNative():
    ISwapChainBackgroundPanelNative = win32more.System.WinRT.Xaml.ISwapChainBackgroundPanelNative_head
    ISwapChainBackgroundPanelNative.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISwapChain_head)(3, 'SetSwapChain', ((1, 'swapChain'),)))
    win32more.System.Com.IUnknown
    return ISwapChainBackgroundPanelNative
def _define_ISwapChainPanelNative_head():
    class ISwapChainPanelNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('f92f19d2-3ade-45a6-a2-0c-f6-f1-ea-90-55-4b')
    return ISwapChainPanelNative
def _define_ISwapChainPanelNative():
    ISwapChainPanelNative = win32more.System.WinRT.Xaml.ISwapChainPanelNative_head
    ISwapChainPanelNative.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISwapChain_head)(3, 'SetSwapChain', ((1, 'swapChain'),)))
    win32more.System.Com.IUnknown
    return ISwapChainPanelNative
def _define_ISwapChainPanelNative2_head():
    class ISwapChainPanelNative2(win32more.System.WinRT.Xaml.ISwapChainPanelNative_head):
        Guid = Guid('d5a2f60c-37b2-44a2-93-7b-8d-8e-b9-72-68-21')
    return ISwapChainPanelNative2
def _define_ISwapChainPanelNative2():
    ISwapChainPanelNative2 = win32more.System.WinRT.Xaml.ISwapChainPanelNative2_head
    ISwapChainPanelNative2.SetSwapChainHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(4, 'SetSwapChainHandle', ((1, 'swapChainHandle'),)))
    win32more.System.WinRT.Xaml.ISwapChainPanelNative
    return ISwapChainPanelNative2
def _define_ITrackerOwner_head():
    class ITrackerOwner(win32more.System.Com.IUnknown_head):
        Guid = Guid('eb24c20b-9816-4ac7-8c-ff-36-f6-7a-11-8f-4e')
    return ITrackerOwner
def _define_ITrackerOwner():
    ITrackerOwner = win32more.System.WinRT.Xaml.ITrackerOwner_head
    ITrackerOwner.CreateTrackerHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head)))(3, 'CreateTrackerHandle', ((1, 'returnValue'),)))
    ITrackerOwner.DeleteTrackerHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head))(4, 'DeleteTrackerHandle', ((1, 'handle'),)))
    ITrackerOwner.SetTrackerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head),win32more.System.Com.IUnknown_head)(5, 'SetTrackerValue', ((1, 'handle'),(1, 'value'),)))
    ITrackerOwner.TryGetSafeTrackerValue = COMMETHOD(WINFUNCTYPE(Byte,POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head),POINTER(win32more.System.Com.IUnknown_head))(6, 'TryGetSafeTrackerValue', ((1, 'handle'),(1, 'returnValue'),)))
    win32more.System.Com.IUnknown
    return ITrackerOwner
def _define_IVirtualSurfaceImageSourceNative_head():
    class IVirtualSurfaceImageSourceNative(win32more.System.WinRT.Xaml.ISurfaceImageSourceNative_head):
        Guid = Guid('e9550983-360b-4f53-b3-91-af-d6-95-07-86-91')
    return IVirtualSurfaceImageSourceNative
def _define_IVirtualSurfaceImageSourceNative():
    IVirtualSurfaceImageSourceNative = win32more.System.WinRT.Xaml.IVirtualSurfaceImageSourceNative_head
    IVirtualSurfaceImageSourceNative.Invalidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT)(6, 'Invalidate', ((1, 'updateRect'),)))
    IVirtualSurfaceImageSourceNative.GetUpdateRectCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetUpdateRectCount', ((1, 'count'),)))
    IVirtualSurfaceImageSourceNative.GetUpdateRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),UInt32)(8, 'GetUpdateRects', ((1, 'updates'),(1, 'count'),)))
    IVirtualSurfaceImageSourceNative.GetVisibleBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(9, 'GetVisibleBounds', ((1, 'bounds'),)))
    IVirtualSurfaceImageSourceNative.RegisterForUpdatesNeeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IVirtualSurfaceUpdatesCallbackNative_head)(10, 'RegisterForUpdatesNeeded', ((1, 'callback'),)))
    IVirtualSurfaceImageSourceNative.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(11, 'Resize', ((1, 'newWidth'),(1, 'newHeight'),)))
    win32more.System.WinRT.Xaml.ISurfaceImageSourceNative
    return IVirtualSurfaceImageSourceNative
def _define_IVirtualSurfaceUpdatesCallbackNative_head():
    class IVirtualSurfaceUpdatesCallbackNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('dbf2e947-8e6c-4254-9e-ee-77-38-f7-13-86-c9')
    return IVirtualSurfaceUpdatesCallbackNative
def _define_IVirtualSurfaceUpdatesCallbackNative():
    IVirtualSurfaceUpdatesCallbackNative = win32more.System.WinRT.Xaml.IVirtualSurfaceUpdatesCallbackNative_head
    IVirtualSurfaceUpdatesCallbackNative.UpdatesNeeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'UpdatesNeeded', ()))
    win32more.System.Com.IUnknown
    return IVirtualSurfaceUpdatesCallbackNative
def _define_TrackerHandle___head():
    class TrackerHandle__(Structure):
        pass
    return TrackerHandle__
def _define_TrackerHandle__():
    TrackerHandle__ = win32more.System.WinRT.Xaml.TrackerHandle___head
    TrackerHandle__._fields_ = [
        ('unused', Int32),
    ]
    return TrackerHandle__
XAML_REFERENCETRACKER_DISCONNECT = Int32
XAML_REFERENCETRACKER_DISCONNECT_DEFAULT = 0
XAML_REFERENCETRACKER_DISCONNECT_SUSPEND = 1
__all__ = [
    "E_SURFACE_CONTENTS_LOST",
    "IDesktopWindowXamlSourceNative",
    "IDesktopWindowXamlSourceNative2",
    "IFindReferenceTargetsCallback",
    "IReferenceTracker",
    "IReferenceTrackerExtension",
    "IReferenceTrackerHost",
    "IReferenceTrackerManager",
    "IReferenceTrackerTarget",
    "ISurfaceImageSourceManagerNative",
    "ISurfaceImageSourceNative",
    "ISurfaceImageSourceNativeWithD2D",
    "ISwapChainBackgroundPanelNative",
    "ISwapChainPanelNative",
    "ISwapChainPanelNative2",
    "ITrackerOwner",
    "IVirtualSurfaceImageSourceNative",
    "IVirtualSurfaceUpdatesCallbackNative",
    "TrackerHandle__",
    "XAML_REFERENCETRACKER_DISCONNECT",
    "XAML_REFERENCETRACKER_DISCONNECT_DEFAULT",
    "XAML_REFERENCETRACKER_DISCONNECT_SUSPEND",
]
