from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT.Shell
import win32more.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
CreateProcessMethod = Int32
CreateProcessMethod_CpCreateProcess: CreateProcessMethod = 0
CreateProcessMethod_CpCreateProcessAsUser: CreateProcessMethod = 1
CreateProcessMethod_CpAicLaunchAdminProcess: CreateProcessMethod = 2
class IDDEInitializer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('30dc931f-33fc-4ffd-a1-68-94-22-58-cf-3c-a4')
    @commethod(3)
    def Initialize(fileExtensionOrProtocol: win32more.Foundation.PWSTR, method: win32more.System.WinRT.Shell.CreateProcessMethod, currentDirectory: win32more.Foundation.PWSTR, execTarget: win32more.UI.Shell.IShellItem_head, site: win32more.System.Com.IUnknown_head, application: win32more.Foundation.PWSTR, targetFile: win32more.Foundation.PWSTR, arguments: win32more.Foundation.PWSTR, verb: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IDDEInitializer')
__all__ = [
    "CreateProcessMethod",
    "CreateProcessMethod_CpAicLaunchAdminProcess",
    "CreateProcessMethod_CpCreateProcess",
    "CreateProcessMethod_CpCreateProcessAsUser",
    "IDDEInitializer",
]
