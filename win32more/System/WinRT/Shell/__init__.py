from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT.Shell
import win32more.UI.Shell

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
CreateProcessMethod = Int32
CreateProcessMethod_CpCreateProcess = 0
CreateProcessMethod_CpCreateProcessAsUser = 1
CreateProcessMethod_CpAicLaunchAdminProcess = 2
def _define_IDDEInitializer_head():
    class IDDEInitializer(win32more.System.Com.IUnknown_head):
        Guid = Guid('30dc931f-33fc-4ffd-a168-942258cf3ca4')
    return IDDEInitializer
def _define_IDDEInitializer():
    IDDEInitializer = win32more.System.WinRT.Shell.IDDEInitializer_head
    IDDEInitializer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.WinRT.Shell.CreateProcessMethod,win32more.Foundation.PWSTR,win32more.UI.Shell.IShellItem_head,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Initialize', ((1, 'fileExtensionOrProtocol'),(1, 'method'),(1, 'currentDirectory'),(1, 'execTarget'),(1, 'site'),(1, 'application'),(1, 'targetFile'),(1, 'arguments'),(1, 'verb'),)))
    win32more.System.Com.IUnknown
    return IDDEInitializer
__all__ = [
    "CreateProcessMethod",
    "CreateProcessMethod_CpCreateProcess",
    "CreateProcessMethod_CpCreateProcessAsUser",
    "CreateProcessMethod_CpAicLaunchAdminProcess",
    "IDDEInitializer",
]
