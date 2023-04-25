from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Dxgi
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Xaml
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
E_SURFACE_CONTENTS_LOST: UInt32 = 2150301728
class IDesktopWindowXamlSourceNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3cbcf1bf-2f76-4e9c-96-ab-e8-4b-37-97-25-54')
    @commethod(3)
    def AttachToWindow(self, parentWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_WindowHandle(self, hWnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class IDesktopWindowXamlSourceNative2(c_void_p):
    extends: Windows.Win32.System.WinRT.Xaml.IDesktopWindowXamlSourceNative
    Guid = Guid('e3dcd8c7-3057-4692-99-c3-7b-77-20-af-da-31')
    @commethod(5)
    def PreTranslateMessage(self, message: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), result: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IFindReferenceTargetsCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('04b3486c-4687-4229-8d-14-50-5a-b5-84-dd-88')
    @commethod(3)
    def FoundTrackerTarget(self, target: Windows.Win32.System.WinRT.Xaml.IReferenceTrackerTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceTracker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11d3b13a-180e-4789-a8-be-77-12-88-28-93-e6')
    @commethod(3)
    def ConnectFromTrackerSource(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisconnectFromTrackerSource(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindTrackerTargets(self, callback: Windows.Win32.System.WinRT.Xaml.IFindReferenceTargetsCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReferenceTrackerManager(self, value: POINTER(Windows.Win32.System.WinRT.Xaml.IReferenceTrackerManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddRefFromTrackerSource(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReleaseFromTrackerSource(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PegFromTrackerSource(self) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceTrackerExtension(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4e897caa-59d5-4613-8f-8c-f7-eb-d1-f3-99-b0')
class IReferenceTrackerHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('29a71c6a-3c42-4416-a3-9d-e2-82-5a-07-a7-73')
    @commethod(3)
    def DisconnectUnusedReferenceSources(self, options: Windows.Win32.System.WinRT.Xaml.XAML_REFERENCETRACKER_DISCONNECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseDisconnectedReferenceSources(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyEndOfReferenceTrackingOnThread(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTrackerTarget(self, unknown: Windows.Win32.System.Com.IUnknown_head, newReference: POINTER(Windows.Win32.System.WinRT.Xaml.IReferenceTrackerTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddMemoryPressure(self, bytesAllocated: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveMemoryPressure(self, bytesAllocated: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceTrackerManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3cf184b4-7ccb-4dda-84-55-7e-6c-e9-9a-32-98')
    @commethod(3)
    def ReferenceTrackingStarted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindTrackerTargetsCompleted(self, findFailed: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReferenceTrackingCompleted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetReferenceTrackerHost(self, value: Windows.Win32.System.WinRT.Xaml.IReferenceTrackerHost_head) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceTrackerTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('64bd43f8-bfee-4ec4-b7-eb-29-35-15-8d-ae-21')
    @commethod(3)
    def AddRefFromReferenceTracker(self) -> UInt32: ...
    @commethod(4)
    def ReleaseFromReferenceTracker(self) -> UInt32: ...
    @commethod(5)
    def Peg(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unpeg(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfaceImageSourceManagerNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4c8798b7-1d88-4a0f-b5-9b-b9-3f-60-0d-e8-c8')
    @commethod(3)
    def FlushAllSurfacesWithDevice(self, device: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfaceImageSourceNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f2e9edc1-d307-4525-98-86-0f-af-aa-44-16-3c')
    @commethod(3)
    def SetDevice(self, device: Windows.Win32.Graphics.Dxgi.IDXGIDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginDraw(self, updateRect: Windows.Win32.Foundation.RECT, surface: POINTER(Windows.Win32.Graphics.Dxgi.IDXGISurface_head), offset: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfaceImageSourceNativeWithD2D(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('54298223-41e1-4a41-9c-08-02-e8-25-68-64-a1')
    @commethod(3)
    def SetDevice(self, device: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginDraw(self, updateRect: POINTER(Windows.Win32.Foundation.RECT_head), iid: POINTER(Guid), updateObject: POINTER(c_void_p), offset: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SuspendDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResumeDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainBackgroundPanelNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43bebd4e-add5-4035-8f-85-56-08-d0-8e-9d-c9')
    @commethod(3)
    def SetSwapChain(self, swapChain: Windows.Win32.Graphics.Dxgi.IDXGISwapChain_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainPanelNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f92f19d2-3ade-45a6-a2-0c-f6-f1-ea-90-55-4b')
    @commethod(3)
    def SetSwapChain(self, swapChain: Windows.Win32.Graphics.Dxgi.IDXGISwapChain_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainPanelNative2(c_void_p):
    extends: Windows.Win32.System.WinRT.Xaml.ISwapChainPanelNative
    Guid = Guid('d5a2f60c-37b2-44a2-93-7b-8d-8e-b9-72-68-21')
    @commethod(4)
    def SetSwapChainHandle(self, swapChainHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
class ITrackerOwner(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eb24c20b-9816-4ac7-8c-ff-36-f6-7a-11-8f-4e')
    @commethod(3)
    def CreateTrackerHandle(self, returnValue: POINTER(POINTER(Windows.Win32.System.WinRT.Xaml.TrackerHandle___head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteTrackerHandle(self, handle: POINTER(Windows.Win32.System.WinRT.Xaml.TrackerHandle___head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTrackerValue(self, handle: POINTER(Windows.Win32.System.WinRT.Xaml.TrackerHandle___head), value: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TryGetSafeTrackerValue(self, handle: POINTER(Windows.Win32.System.WinRT.Xaml.TrackerHandle___head), returnValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Byte: ...
class IVirtualSurfaceImageSourceNative(c_void_p):
    extends: Windows.Win32.System.WinRT.Xaml.ISurfaceImageSourceNative
    Guid = Guid('e9550983-360b-4f53-b3-91-af-d6-95-07-86-91')
    @commethod(6)
    def Invalidate(self, updateRect: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUpdateRectCount(self, count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetUpdateRects(self, updates: POINTER(Windows.Win32.Foundation.RECT_head), count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetVisibleBounds(self, bounds: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForUpdatesNeeded(self, callback: Windows.Win32.System.WinRT.Xaml.IVirtualSurfaceUpdatesCallbackNative_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Resize(self, newWidth: Int32, newHeight: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IVirtualSurfaceUpdatesCallbackNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dbf2e947-8e6c-4254-9e-ee-77-38-f7-13-86-c9')
    @commethod(3)
    def UpdatesNeeded(self) -> Windows.Win32.Foundation.HRESULT: ...
class TrackerHandle__(EasyCastStructure):
    unused: Int32
XAML_REFERENCETRACKER_DISCONNECT = Int32
XAML_REFERENCETRACKER_DISCONNECT_DEFAULT: XAML_REFERENCETRACKER_DISCONNECT = 0
XAML_REFERENCETRACKER_DISCONNECT_SUSPEND: XAML_REFERENCETRACKER_DISCONNECT = 1
make_head(_module, 'IDesktopWindowXamlSourceNative')
make_head(_module, 'IDesktopWindowXamlSourceNative2')
make_head(_module, 'IFindReferenceTargetsCallback')
make_head(_module, 'IReferenceTracker')
make_head(_module, 'IReferenceTrackerExtension')
make_head(_module, 'IReferenceTrackerHost')
make_head(_module, 'IReferenceTrackerManager')
make_head(_module, 'IReferenceTrackerTarget')
make_head(_module, 'ISurfaceImageSourceManagerNative')
make_head(_module, 'ISurfaceImageSourceNative')
make_head(_module, 'ISurfaceImageSourceNativeWithD2D')
make_head(_module, 'ISwapChainBackgroundPanelNative')
make_head(_module, 'ISwapChainPanelNative')
make_head(_module, 'ISwapChainPanelNative2')
make_head(_module, 'ITrackerOwner')
make_head(_module, 'IVirtualSurfaceImageSourceNative')
make_head(_module, 'IVirtualSurfaceUpdatesCallbackNative')
make_head(_module, 'TrackerHandle__')
