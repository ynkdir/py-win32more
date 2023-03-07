from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Shell
import Windows.Win32.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
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
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30dc931f-33fc-4ffd-a1-68-94-22-58-cf-3c-a4')
    @commethod(3)
    def Initialize(fileExtensionOrProtocol: Windows.Win32.Foundation.PWSTR, method: Windows.Win32.System.WinRT.Shell.CreateProcessMethod, currentDirectory: Windows.Win32.Foundation.PWSTR, execTarget: Windows.Win32.UI.Shell.IShellItem_head, site: Windows.Win32.System.Com.IUnknown_head, application: Windows.Win32.Foundation.PWSTR, targetFile: Windows.Win32.Foundation.PWSTR, arguments: Windows.Win32.Foundation.PWSTR, verb: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDDEInitializer')
__all__ = [
    "CreateProcessMethod",
    "CreateProcessMethod_CpAicLaunchAdminProcess",
    "CreateProcessMethod_CpCreateProcess",
    "CreateProcessMethod_CpCreateProcessAsUser",
    "IDDEInitializer",
]
_arch_optional = [
]