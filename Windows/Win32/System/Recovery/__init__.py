from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Recovery
import Windows.Win32.System.WindowsProgramming
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('KERNEL32.dll')
def RegisterApplicationRecoveryCallback(pRecoveyCallback: Windows.Win32.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK, pvParameter: VoidPtr, dwPingInterval: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def UnregisterApplicationRecoveryCallback() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def RegisterApplicationRestart(pwzCommandline: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def UnregisterApplicationRestart() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetApplicationRecoveryCallback(hProcess: Windows.Win32.Foundation.HANDLE, pRecoveryCallback: POINTER(Windows.Win32.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK), ppvParameter: POINTER(VoidPtr), pdwPingInterval: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
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
