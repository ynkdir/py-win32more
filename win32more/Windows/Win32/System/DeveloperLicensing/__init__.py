from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.DeveloperLicensing
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('WSClient.dll')
def CheckDeveloperLicense(pExpiration: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSClient.dll')
def AcquireDeveloperLicense(hwndParent: win32more.Windows.Win32.Foundation.HWND, pExpiration: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSClient.dll')
def RemoveDeveloperLicense(hwndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
