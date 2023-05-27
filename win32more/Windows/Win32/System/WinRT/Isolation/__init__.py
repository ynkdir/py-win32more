from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Isolation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IIsolatedEnvironmentInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85713c2e-8e62-46c5-8de2-c647e1d54636}')
    @commethod(3)
    def GetHostHwndInterop(self, containerHwnd: win32more.Windows.Win32.Foundation.HWND, hostHwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IIsolatedEnvironmentInterop')
