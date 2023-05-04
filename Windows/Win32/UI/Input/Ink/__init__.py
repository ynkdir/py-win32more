from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.UI.Input.Ink
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IInkCommitRequestHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fabea3fc-b108-45b6-a9fc-8d08fa9f85cf}')
    @commethod(3)
    def OnCommitRequested(self) -> Windows.Win32.Foundation.HRESULT: ...
class IInkD2DRenderer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{407fb1de-f85a-4150-97cf-b7fb274fb4f8}')
    @commethod(3)
    def Draw(self, pD2D1DeviceContext: Windows.Win32.System.Com.IUnknown_head, pInkStrokeIterable: Windows.Win32.System.Com.IUnknown_head, fHighContrast: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IInkD2DRenderer2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a95dcd9-4578-4b71-b20b-bf664d4bfeee}')
    @commethod(3)
    def Draw(self, pD2D1DeviceContext: Windows.Win32.System.Com.IUnknown_head, pInkStrokeIterable: Windows.Win32.System.Com.IUnknown_head, highContrastAdjustment: Windows.Win32.UI.Input.Ink.INK_HIGH_CONTRAST_ADJUSTMENT) -> Windows.Win32.Foundation.HRESULT: ...
class IInkDesktopHost(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ce7d875-a981-4140-a1ff-ad93258e8d59}')
    @commethod(3)
    def QueueWorkItem(self, workItem: Windows.Win32.UI.Input.Ink.IInkHostWorkItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInkPresenter(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAndInitializeInkPresenter(self, rootVisual: Windows.Win32.System.Com.IUnknown_head, width: Single, height: Single, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IInkHostWorkItem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ccda0a9a-1b78-4632-bb96-97800662e26c}')
    @commethod(3)
    def Invoke(self) -> Windows.Win32.Foundation.HRESULT: ...
class IInkPresenterDesktop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73f3c0d9-2e8b-48f3-895e-20cbd27b723b}')
    @commethod(3)
    def SetRootVisual(self, rootVisual: Windows.Win32.System.Com.IUnknown_head, device: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCommitRequestHandler(self, handler: Windows.Win32.UI.Input.Ink.IInkCommitRequestHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSize(self, width: POINTER(Single), height: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(self, width: Single, height: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnHighContrastChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
INK_HIGH_CONTRAST_ADJUSTMENT = Int32
USE_SYSTEM_COLORS_WHEN_NECESSARY: INK_HIGH_CONTRAST_ADJUSTMENT = 0
USE_SYSTEM_COLORS: INK_HIGH_CONTRAST_ADJUSTMENT = 1
USE_ORIGINAL_COLORS: INK_HIGH_CONTRAST_ADJUSTMENT = 2
InkD2DRenderer = Guid('{4044e60c-7b01-4671-a97c-04e0210a07a5}')
InkDesktopHost = Guid('{062584a6-f830-4bdc-a4d2-0a10ab062b1d}')
make_head(_module, 'IInkCommitRequestHandler')
make_head(_module, 'IInkD2DRenderer')
make_head(_module, 'IInkD2DRenderer2')
make_head(_module, 'IInkDesktopHost')
make_head(_module, 'IInkHostWorkItem')
make_head(_module, 'IInkPresenterDesktop')
