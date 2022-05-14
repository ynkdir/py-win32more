from win32more import *
import win32more.System.WinRT.Xaml
import win32more.Foundation
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.WinRT.Xaml, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.WinRT.Xaml, name)
E_SURFACE_CONTENTS_LOST = 2150301728
def _define_ISurfaceImageSourceNative_head():
    class ISurfaceImageSourceNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('f2e9edc1-d307-4525-9886-0fafaa44163c')
    return ISurfaceImageSourceNative
def _define_ISurfaceImageSourceNative():
    ISurfaceImageSourceNative = win32more.System.WinRT.Xaml.ISurfaceImageSourceNative_head
    ISurfaceImageSourceNative.SetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head, use_last_error=False)(3, 'SetDevice', ((1, 'device'),)))
    ISurfaceImageSourceNative.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,POINTER(win32more.Graphics.Dxgi.IDXGISurface_head),POINTER(win32more.Foundation.POINT_head), use_last_error=False)(4, 'BeginDraw', ((1, 'updateRect'),(1, 'surface'),(1, 'offset'),)))
    ISurfaceImageSourceNative.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'EndDraw', ()))
    return ISurfaceImageSourceNative
def _define_IVirtualSurfaceUpdatesCallbackNative_head():
    class IVirtualSurfaceUpdatesCallbackNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('dbf2e947-8e6c-4254-9eee-7738f71386c9')
    return IVirtualSurfaceUpdatesCallbackNative
def _define_IVirtualSurfaceUpdatesCallbackNative():
    IVirtualSurfaceUpdatesCallbackNative = win32more.System.WinRT.Xaml.IVirtualSurfaceUpdatesCallbackNative_head
    IVirtualSurfaceUpdatesCallbackNative.UpdatesNeeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'UpdatesNeeded', ()))
    return IVirtualSurfaceUpdatesCallbackNative
def _define_IVirtualSurfaceImageSourceNative_head():
    class IVirtualSurfaceImageSourceNative(win32more.System.WinRT.Xaml.ISurfaceImageSourceNative_head):
        Guid = Guid('e9550983-360b-4f53-b391-afd695078691')
    return IVirtualSurfaceImageSourceNative
def _define_IVirtualSurfaceImageSourceNative():
    IVirtualSurfaceImageSourceNative = win32more.System.WinRT.Xaml.IVirtualSurfaceImageSourceNative_head
    IVirtualSurfaceImageSourceNative.Invalidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT, use_last_error=False)(6, 'Invalidate', ((1, 'updateRect'),)))
    IVirtualSurfaceImageSourceNative.GetUpdateRectCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetUpdateRectCount', ((1, 'count'),)))
    IVirtualSurfaceImageSourceNative.GetUpdateRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT),UInt32, use_last_error=False)(8, 'GetUpdateRects', ((1, 'updates'),(1, 'count'),)))
    IVirtualSurfaceImageSourceNative.GetVisibleBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(9, 'GetVisibleBounds', ((1, 'bounds'),)))
    IVirtualSurfaceImageSourceNative.RegisterForUpdatesNeeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IVirtualSurfaceUpdatesCallbackNative_head, use_last_error=False)(10, 'RegisterForUpdatesNeeded', ((1, 'callback'),)))
    IVirtualSurfaceImageSourceNative.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(11, 'Resize', ((1, 'newWidth'),(1, 'newHeight'),)))
    return IVirtualSurfaceImageSourceNative
def _define_ISwapChainBackgroundPanelNative_head():
    class ISwapChainBackgroundPanelNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('43bebd4e-add5-4035-8f85-5608d08e9dc9')
    return ISwapChainBackgroundPanelNative
def _define_ISwapChainBackgroundPanelNative():
    ISwapChainBackgroundPanelNative = win32more.System.WinRT.Xaml.ISwapChainBackgroundPanelNative_head
    ISwapChainBackgroundPanelNative.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISwapChain_head, use_last_error=False)(3, 'SetSwapChain', ((1, 'swapChain'),)))
    return ISwapChainBackgroundPanelNative
def _define_ISurfaceImageSourceManagerNative_head():
    class ISurfaceImageSourceManagerNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c8798b7-1d88-4a0f-b59b-b93f600de8c8')
    return ISurfaceImageSourceManagerNative
def _define_ISurfaceImageSourceManagerNative():
    ISurfaceImageSourceManagerNative = win32more.System.WinRT.Xaml.ISurfaceImageSourceManagerNative_head
    ISurfaceImageSourceManagerNative.FlushAllSurfacesWithDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'FlushAllSurfacesWithDevice', ((1, 'device'),)))
    return ISurfaceImageSourceManagerNative
def _define_ISurfaceImageSourceNativeWithD2D_head():
    class ISurfaceImageSourceNativeWithD2D(win32more.System.Com.IUnknown_head):
        Guid = Guid('54298223-41e1-4a41-9c08-02e8256864a1')
    return ISurfaceImageSourceNativeWithD2D
def _define_ISurfaceImageSourceNativeWithD2D():
    ISurfaceImageSourceNativeWithD2D = win32more.System.WinRT.Xaml.ISurfaceImageSourceNativeWithD2D_head
    ISurfaceImageSourceNativeWithD2D.SetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetDevice', ((1, 'device'),)))
    ISurfaceImageSourceNativeWithD2D.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.POINT_head), use_last_error=False)(4, 'BeginDraw', ((1, 'updateRect'),(1, 'iid'),(1, 'updateObject'),(1, 'offset'),)))
    ISurfaceImageSourceNativeWithD2D.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'EndDraw', ()))
    ISurfaceImageSourceNativeWithD2D.SuspendDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'SuspendDraw', ()))
    ISurfaceImageSourceNativeWithD2D.ResumeDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'ResumeDraw', ()))
    return ISurfaceImageSourceNativeWithD2D
def _define_ISwapChainPanelNative_head():
    class ISwapChainPanelNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('f92f19d2-3ade-45a6-a20c-f6f1ea90554b')
    return ISwapChainPanelNative
def _define_ISwapChainPanelNative():
    ISwapChainPanelNative = win32more.System.WinRT.Xaml.ISwapChainPanelNative_head
    ISwapChainPanelNative.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISwapChain_head, use_last_error=False)(3, 'SetSwapChain', ((1, 'swapChain'),)))
    return ISwapChainPanelNative
def _define_ISwapChainPanelNative2_head():
    class ISwapChainPanelNative2(win32more.System.WinRT.Xaml.ISwapChainPanelNative_head):
        Guid = Guid('d5a2f60c-37b2-44a2-937b-8d8eb9726821')
    return ISwapChainPanelNative2
def _define_ISwapChainPanelNative2():
    ISwapChainPanelNative2 = win32more.System.WinRT.Xaml.ISwapChainPanelNative2_head
    ISwapChainPanelNative2.SetSwapChainHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(4, 'SetSwapChainHandle', ((1, 'swapChainHandle'),)))
    return ISwapChainPanelNative2
def _define_IDesktopWindowXamlSourceNative_head():
    class IDesktopWindowXamlSourceNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('3cbcf1bf-2f76-4e9c-96ab-e84b37972554')
    return IDesktopWindowXamlSourceNative
def _define_IDesktopWindowXamlSourceNative():
    IDesktopWindowXamlSourceNative = win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative_head
    IDesktopWindowXamlSourceNative.AttachToWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(3, 'AttachToWindow', ((1, 'parentWnd'),)))
    IDesktopWindowXamlSourceNative.get_WindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(4, 'get_WindowHandle', ((1, 'hWnd'),)))
    return IDesktopWindowXamlSourceNative
def _define_IDesktopWindowXamlSourceNative2_head():
    class IDesktopWindowXamlSourceNative2(win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative_head):
        Guid = Guid('e3dcd8c7-3057-4692-99c3-7b7720afda31')
    return IDesktopWindowXamlSourceNative2
def _define_IDesktopWindowXamlSourceNative2():
    IDesktopWindowXamlSourceNative2 = win32more.System.WinRT.Xaml.IDesktopWindowXamlSourceNative2_head
    IDesktopWindowXamlSourceNative2.PreTranslateMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'PreTranslateMessage', ((1, 'message'),(1, 'result'),)))
    return IDesktopWindowXamlSourceNative2
def _define_IReferenceTrackerTarget_head():
    class IReferenceTrackerTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('64bd43f8-bfee-4ec4-b7eb-2935158dae21')
    return IReferenceTrackerTarget
def _define_IReferenceTrackerTarget():
    IReferenceTrackerTarget = win32more.System.WinRT.Xaml.IReferenceTrackerTarget_head
    IReferenceTrackerTarget.AddRefFromReferenceTracker = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'AddRefFromReferenceTracker', ()))
    IReferenceTrackerTarget.ReleaseFromReferenceTracker = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'ReleaseFromReferenceTracker', ()))
    IReferenceTrackerTarget.Peg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Peg', ()))
    IReferenceTrackerTarget.Unpeg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Unpeg', ()))
    return IReferenceTrackerTarget
def _define_IReferenceTracker_head():
    class IReferenceTracker(win32more.System.Com.IUnknown_head):
        Guid = Guid('11d3b13a-180e-4789-a8be-7712882893e6')
    return IReferenceTracker
def _define_IReferenceTracker():
    IReferenceTracker = win32more.System.WinRT.Xaml.IReferenceTracker_head
    IReferenceTracker.ConnectFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'ConnectFromTrackerSource', ()))
    IReferenceTracker.DisconnectFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DisconnectFromTrackerSource', ()))
    IReferenceTracker.FindTrackerTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IFindReferenceTargetsCallback_head, use_last_error=False)(5, 'FindTrackerTargets', ((1, 'callback'),)))
    IReferenceTracker.GetReferenceTrackerManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.Xaml.IReferenceTrackerManager_head), use_last_error=False)(6, 'GetReferenceTrackerManager', ((1, 'value'),)))
    IReferenceTracker.AddRefFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'AddRefFromTrackerSource', ()))
    IReferenceTracker.ReleaseFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'ReleaseFromTrackerSource', ()))
    IReferenceTracker.PegFromTrackerSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'PegFromTrackerSource', ()))
    return IReferenceTracker
def _define_IReferenceTrackerManager_head():
    class IReferenceTrackerManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('3cf184b4-7ccb-4dda-8455-7e6ce99a3298')
    return IReferenceTrackerManager
def _define_IReferenceTrackerManager():
    IReferenceTrackerManager = win32more.System.WinRT.Xaml.IReferenceTrackerManager_head
    IReferenceTrackerManager.ReferenceTrackingStarted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'ReferenceTrackingStarted', ()))
    IReferenceTrackerManager.FindTrackerTargetsCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte, use_last_error=False)(4, 'FindTrackerTargetsCompleted', ((1, 'findFailed'),)))
    IReferenceTrackerManager.ReferenceTrackingCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'ReferenceTrackingCompleted', ()))
    IReferenceTrackerManager.SetReferenceTrackerHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IReferenceTrackerHost_head, use_last_error=False)(6, 'SetReferenceTrackerHost', ((1, 'value'),)))
    return IReferenceTrackerManager
def _define_IFindReferenceTargetsCallback_head():
    class IFindReferenceTargetsCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('04b3486c-4687-4229-8d14-505ab584dd88')
    return IFindReferenceTargetsCallback
def _define_IFindReferenceTargetsCallback():
    IFindReferenceTargetsCallback = win32more.System.WinRT.Xaml.IFindReferenceTargetsCallback_head
    IFindReferenceTargetsCallback.FoundTrackerTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.IReferenceTrackerTarget_head, use_last_error=False)(3, 'FoundTrackerTarget', ((1, 'target'),)))
    return IFindReferenceTargetsCallback
XAML_REFERENCETRACKER_DISCONNECT = Int32
XAML_REFERENCETRACKER_DISCONNECT_DEFAULT = 0
XAML_REFERENCETRACKER_DISCONNECT_SUSPEND = 1
def _define_IReferenceTrackerHost_head():
    class IReferenceTrackerHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('29a71c6a-3c42-4416-a39d-e2825a07a773')
    return IReferenceTrackerHost
def _define_IReferenceTrackerHost():
    IReferenceTrackerHost = win32more.System.WinRT.Xaml.IReferenceTrackerHost_head
    IReferenceTrackerHost.DisconnectUnusedReferenceSources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Xaml.XAML_REFERENCETRACKER_DISCONNECT, use_last_error=False)(3, 'DisconnectUnusedReferenceSources', ((1, 'options'),)))
    IReferenceTrackerHost.ReleaseDisconnectedReferenceSources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'ReleaseDisconnectedReferenceSources', ()))
    IReferenceTrackerHost.NotifyEndOfReferenceTrackingOnThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'NotifyEndOfReferenceTrackingOnThread', ()))
    IReferenceTrackerHost.GetTrackerTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.WinRT.Xaml.IReferenceTrackerTarget_head), use_last_error=False)(6, 'GetTrackerTarget', ((1, 'unknown'),(1, 'newReference'),)))
    IReferenceTrackerHost.AddMemoryPressure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(7, 'AddMemoryPressure', ((1, 'bytesAllocated'),)))
    IReferenceTrackerHost.RemoveMemoryPressure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(8, 'RemoveMemoryPressure', ((1, 'bytesAllocated'),)))
    return IReferenceTrackerHost
def _define_IReferenceTrackerExtension_head():
    class IReferenceTrackerExtension(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e897caa-59d5-4613-8f8c-f7ebd1f399b0')
    return IReferenceTrackerExtension
def _define_IReferenceTrackerExtension():
    IReferenceTrackerExtension = win32more.System.WinRT.Xaml.IReferenceTrackerExtension_head
    return IReferenceTrackerExtension
def _define_TrackerHandle___head():
    class TrackerHandle__(Structure):
        pass
    return TrackerHandle__
def _define_TrackerHandle__():
    TrackerHandle__ = win32more.System.WinRT.Xaml.TrackerHandle___head
    TrackerHandle__._fields_ = [
        ("unused", Int32),
    ]
    return TrackerHandle__
def _define_ITrackerOwner_head():
    class ITrackerOwner(win32more.System.Com.IUnknown_head):
        Guid = Guid('eb24c20b-9816-4ac7-8cff-36f67a118f4e')
    return ITrackerOwner
def _define_ITrackerOwner():
    ITrackerOwner = win32more.System.WinRT.Xaml.ITrackerOwner_head
    ITrackerOwner.CreateTrackerHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head)), use_last_error=False)(3, 'CreateTrackerHandle', ((1, 'returnValue'),)))
    ITrackerOwner.DeleteTrackerHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head), use_last_error=False)(4, 'DeleteTrackerHandle', ((1, 'handle'),)))
    ITrackerOwner.SetTrackerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head),win32more.System.Com.IUnknown_head, use_last_error=False)(5, 'SetTrackerValue', ((1, 'handle'),(1, 'value'),)))
    ITrackerOwner.TryGetSafeTrackerValue = COMMETHOD(WINFUNCTYPE(Byte,POINTER(win32more.System.WinRT.Xaml.TrackerHandle___head),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'TryGetSafeTrackerValue', ((1, 'handle'),(1, 'returnValue'),)))
    return ITrackerOwner
__all__ = [
    "E_SURFACE_CONTENTS_LOST",
    "ISurfaceImageSourceNative",
    "IVirtualSurfaceUpdatesCallbackNative",
    "IVirtualSurfaceImageSourceNative",
    "ISwapChainBackgroundPanelNative",
    "ISurfaceImageSourceManagerNative",
    "ISurfaceImageSourceNativeWithD2D",
    "ISwapChainPanelNative",
    "ISwapChainPanelNative2",
    "IDesktopWindowXamlSourceNative",
    "IDesktopWindowXamlSourceNative2",
    "IReferenceTrackerTarget",
    "IReferenceTracker",
    "IReferenceTrackerManager",
    "IFindReferenceTargetsCallback",
    "XAML_REFERENCETRACKER_DISCONNECT",
    "XAML_REFERENCETRACKER_DISCONNECT_DEFAULT",
    "XAML_REFERENCETRACKER_DISCONNECT_SUSPEND",
    "IReferenceTrackerHost",
    "IReferenceTrackerExtension",
    "TrackerHandle__",
    "ITrackerOwner",
]
