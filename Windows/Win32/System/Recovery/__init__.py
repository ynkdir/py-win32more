from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Recovery
import Windows.Win32.System.WindowsProgramming
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
@winfunctype('KERNEL32.dll')
def RegisterApplicationRecoveryCallback(pRecoveyCallback: Windows.Win32.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK, pvParameter: c_void_p, dwPingInterval: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def UnregisterApplicationRecoveryCallback() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def RegisterApplicationRestart(pwzCommandline: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def UnregisterApplicationRestart() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetApplicationRecoveryCallback(hProcess: Windows.Win32.Foundation.HANDLE, pRecoveryCallback: POINTER(Windows.Win32.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK), ppvParameter: POINTER(c_void_p), pdwPingInterval: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetApplicationRestartSettings(hProcess: Windows.Win32.Foundation.HANDLE, pwzCommandline: Windows.Win32.Foundation.PWSTR, pcchSize: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ApplicationRecoveryInProgress(pbCancelled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ApplicationRecoveryFinished(bSuccess: Windows.Win32.Foundation.BOOL) -> Void: ...
REGISTER_APPLICATION_RESTART_FLAGS = UInt32
RESTART_NO_CRASH: REGISTER_APPLICATION_RESTART_FLAGS = 1
RESTART_NO_HANG: REGISTER_APPLICATION_RESTART_FLAGS = 2
RESTART_NO_PATCH: REGISTER_APPLICATION_RESTART_FLAGS = 4
RESTART_NO_REBOOT: REGISTER_APPLICATION_RESTART_FLAGS = 8
__all__ = [
    "ApplicationRecoveryFinished",
    "ApplicationRecoveryInProgress",
    "GetApplicationRecoveryCallback",
    "GetApplicationRestartSettings",
    "REGISTER_APPLICATION_RESTART_FLAGS",
    "RESTART_NO_CRASH",
    "RESTART_NO_HANG",
    "RESTART_NO_PATCH",
    "RESTART_NO_REBOOT",
    "RegisterApplicationRecoveryCallback",
    "RegisterApplicationRestart",
    "UnregisterApplicationRecoveryCallback",
    "UnregisterApplicationRestart",
]
_arch_optional = [
]
