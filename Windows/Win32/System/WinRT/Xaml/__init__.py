from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
class IDesktopWindowXamlSourceNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3cbcf1bf-2f76-4e9c-96ab-e84b37972554}')
    @commethod(3)
    def AttachToWindow(self, parentWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_WindowHandle(self, hWnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class IDesktopWindowXamlSourceNative2(ComPtr):
    extends: Windows.Win32.System.WinRT.Xaml.IDesktopWindowXamlSourceNative
    _iid_ = Guid('{e3dcd8c7-3057-4692-99c3-7b7720afda31}')
    @commethod(5)
    def PreTranslateMessage(self, message: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), result: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IFindReferenceTargetsCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04b3486c-4687-4229-8d14-505ab584dd88}')
    @commethod(3)
    def FoundTrackerTarget(self, target: Windows.Win32.System.WinRT.Xaml.IReferenceTrackerTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceTracker(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11d3b13a-180e-4789-a8be-7712882893e6}')
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
class IReferenceTrackerExtension(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e897caa-59d5-4613-8f8c-f7ebd1f399b0}')
class IReferenceTrackerHost(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{29a71c6a-3c42-4416-a39d-e2825a07a773}')
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
class IReferenceTrackerManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3cf184b4-7ccb-4dda-8455-7e6ce99a3298}')
    @commethod(3)
    def ReferenceTrackingStarted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindTrackerTargetsCompleted(self, findFailed: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReferenceTrackingCompleted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetReferenceTrackerHost(self, value: Windows.Win32.System.WinRT.Xaml.IReferenceTrackerHost_head) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceTrackerTarget(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64bd43f8-bfee-4ec4-b7eb-2935158dae21}')
    @commethod(3)
    def AddRefFromReferenceTracker(self) -> UInt32: ...
    @commethod(4)
    def ReleaseFromReferenceTracker(self) -> UInt32: ...
    @commethod(5)
    def Peg(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unpeg(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfaceImageSourceManagerNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c8798b7-1d88-4a0f-b59b-b93f600de8c8}')
    @commethod(3)
    def FlushAllSurfacesWithDevice(self, device: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfaceImageSourceNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f2e9edc1-d307-4525-9886-0fafaa44163c}')
    @commethod(3)
    def SetDevice(self, device: Windows.Win32.Graphics.Dxgi.IDXGIDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginDraw(self, updateRect: Windows.Win32.Foundation.RECT, surface: POINTER(Windows.Win32.Graphics.Dxgi.IDXGISurface_head), offset: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfaceImageSourceNativeWithD2D(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54298223-41e1-4a41-9c08-02e8256864a1}')
    @commethod(3)
    def SetDevice(self, device: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginDraw(self, updateRect: POINTER(Windows.Win32.Foundation.RECT_head), iid: POINTER(Guid), updateObject: POINTER(VoidPtr), offset: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SuspendDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResumeDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainBackgroundPanelNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{43bebd4e-add5-4035-8f85-5608d08e9dc9}')
    @commethod(3)
    def SetSwapChain(self, swapChain: Windows.Win32.Graphics.Dxgi.IDXGISwapChain_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainPanelNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f92f19d2-3ade-45a6-a20c-f6f1ea90554b}')
    @commethod(3)
    def SetSwapChain(self, swapChain: Windows.Win32.Graphics.Dxgi.IDXGISwapChain_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainPanelNative2(ComPtr):
    extends: Windows.Win32.System.WinRT.Xaml.ISwapChainPanelNative
    _iid_ = Guid('{d5a2f60c-37b2-44a2-937b-8d8eb9726821}')
    @commethod(4)
    def SetSwapChainHandle(self, swapChainHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
class ITrackerOwner(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eb24c20b-9816-4ac7-8cff-36f67a118f4e}')
    @commethod(3)
    def CreateTrackerHandle(self, returnValue: POINTER(Windows.Win32.System.WinRT.Xaml.TrackerHandle)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteTrackerHandle(self, handle: Windows.Win32.System.WinRT.Xaml.TrackerHandle) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTrackerValue(self, handle: Windows.Win32.System.WinRT.Xaml.TrackerHandle, value: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TryGetSafeTrackerValue(self, handle: Windows.Win32.System.WinRT.Xaml.TrackerHandle, returnValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Byte: ...
class IVirtualSurfaceImageSourceNative(ComPtr):
    extends: Windows.Win32.System.WinRT.Xaml.ISurfaceImageSourceNative
    _iid_ = Guid('{e9550983-360b-4f53-b391-afd695078691}')
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
class IVirtualSurfaceUpdatesCallbackNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dbf2e947-8e6c-4254-9eee-7738f71386c9}')
    @commethod(3)
    def UpdatesNeeded(self) -> Windows.Win32.Foundation.HRESULT: ...
TrackerHandle = IntPtr
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
