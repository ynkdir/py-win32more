from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Recovery
import win32more.System.WindowsProgramming

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
REGISTER_APPLICATION_RESTART_FLAGS = UInt32
RESTART_NO_CRASH = 1
RESTART_NO_HANG = 2
RESTART_NO_PATCH = 4
RESTART_NO_REBOOT = 8
def _define_RegisterApplicationRecoveryCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK,c_void_p,UInt32,UInt32, use_last_error=False)(("RegisterApplicationRecoveryCallback", windll["KERNEL32"]), ((1, 'pRecoveyCallback'),(1, 'pvParameter'),(1, 'dwPingInterval'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterApplicationRecoveryCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("UnregisterApplicationRecoveryCallback", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterApplicationRestart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS, use_last_error=False)(("RegisterApplicationRestart", windll["KERNEL32"]), ((1, 'pwzCommandline'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterApplicationRestart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("UnregisterApplicationRestart", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetApplicationRecoveryCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK),POINTER(c_void_p),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetApplicationRecoveryCallback", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'pRecoveryCallback'),(1, 'ppvParameter'),(1, 'pdwPingInterval'),(1, 'pdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetApplicationRestartSettings():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(Char),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetApplicationRestartSettings", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'pwzCommandline'),(1, 'pcchSize'),(1, 'pdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApplicationRecoveryInProgress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("ApplicationRecoveryInProgress", windll["KERNEL32"]), ((1, 'pbCancelled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ApplicationRecoveryFinished():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(("ApplicationRecoveryFinished", windll["KERNEL32"]), ((1, 'bSuccess'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "REGISTER_APPLICATION_RESTART_FLAGS",
    "RESTART_NO_CRASH",
    "RESTART_NO_HANG",
    "RESTART_NO_PATCH",
    "RESTART_NO_REBOOT",
    "RegisterApplicationRecoveryCallback",
    "UnregisterApplicationRecoveryCallback",
    "RegisterApplicationRestart",
    "UnregisterApplicationRestart",
    "GetApplicationRecoveryCallback",
    "GetApplicationRestartSettings",
    "ApplicationRecoveryInProgress",
    "ApplicationRecoveryFinished",
]
