from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Input.Ink
class IInkCommitRequestHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fabea3fc-b108-45b6-a9fc-8d08fa9f85cf}')
    @commethod(3)
    def OnCommitRequested(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkD2DRenderer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{407fb1de-f85a-4150-97cf-b7fb274fb4f8}')
    @commethod(3)
    def Draw(self, pD2D1DeviceContext: win32more.Windows.Win32.System.Com.IUnknown, pInkStrokeIterable: win32more.Windows.Win32.System.Com.IUnknown, fHighContrast: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkD2DRenderer2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a95dcd9-4578-4b71-b20b-bf664d4bfeee}')
    @commethod(3)
    def Draw(self, pD2D1DeviceContext: win32more.Windows.Win32.System.Com.IUnknown, pInkStrokeIterable: win32more.Windows.Win32.System.Com.IUnknown, highContrastAdjustment: win32more.Windows.Win32.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDesktopHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ce7d875-a981-4140-a1ff-ad93258e8d59}')
    @commethod(3)
    def QueueWorkItem(self, workItem: win32more.Windows.Win32.UI.Input.Ink.IInkHostWorkItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInkPresenter(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAndInitializeInkPresenter(self, rootVisual: win32more.Windows.Win32.System.Com.IUnknown, width: Single, height: Single, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkHostWorkItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ccda0a9a-1b78-4632-bb96-97800662e26c}')
    @commethod(3)
    def Invoke(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkPresenterDesktop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73f3c0d9-2e8b-48f3-895e-20cbd27b723b}')
    @commethod(3)
    def SetRootVisual(self, rootVisual: win32more.Windows.Win32.System.Com.IUnknown, device: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCommitRequestHandler(self, handler: win32more.Windows.Win32.UI.Input.Ink.IInkCommitRequestHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSize(self, width: POINTER(Single), height: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(self, width: Single, height: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnHighContrastChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
INK_HIGH_CONTRAST_ADJUSTMENT = Int32
USE_SYSTEM_COLORS_WHEN_NECESSARY: win32more.Windows.Win32.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT = 0
USE_SYSTEM_COLORS: win32more.Windows.Win32.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT = 1
USE_ORIGINAL_COLORS: win32more.Windows.Win32.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT = 2
InkD2DRenderer = Guid('{4044e60c-7b01-4671-a97c-04e0210a07a5}')
InkDesktopHost = Guid('{062584a6-f830-4bdc-a4d2-0a10ab062b1d}')


make_ready(__name__)
