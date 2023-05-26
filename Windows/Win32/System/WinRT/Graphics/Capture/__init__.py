from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Graphics.Capture
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IGraphicsCaptureItemInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3628e81b-3cac-4c60-b7f4-23ce0e0c3356}')
    @commethod(3)
    def CreateForWindow(self, window: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), result: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateForMonitor(self, monitor: Windows.Win32.Graphics.Gdi.HMONITOR, riid: POINTER(Guid), result: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IGraphicsCaptureItemInterop')
