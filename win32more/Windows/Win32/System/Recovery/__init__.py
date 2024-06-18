from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Recovery
import win32more.Windows.Win32.System.WindowsProgramming
@winfunctype('KERNEL32.dll')
def RegisterApplicationRecoveryCallback(pRecoveyCallback: win32more.Windows.Win32.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK, pvParameter: VoidPtr, dwPingInterval: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def UnregisterApplicationRecoveryCallback() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def RegisterApplicationRestart(pwzCommandline: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def UnregisterApplicationRestart() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetApplicationRecoveryCallback(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pRecoveryCallback: POINTER(win32more.Windows.Win32.System.WindowsProgramming.APPLICATION_RECOVERY_CALLBACK), ppvParameter: POINTER(VoidPtr), pdwPingInterval: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def GetApplicationRestartSettings(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pwzCommandline: win32more.Windows.Win32.Foundation.PWSTR, pcchSize: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ApplicationRecoveryInProgress(pbCancelled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ApplicationRecoveryFinished(bSuccess: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
REGISTER_APPLICATION_RESTART_FLAGS = UInt32
RESTART_NO_CRASH: win32more.Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS = 1
RESTART_NO_HANG: win32more.Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS = 2
RESTART_NO_PATCH: win32more.Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS = 4
RESTART_NO_REBOOT: win32more.Windows.Win32.System.Recovery.REGISTER_APPLICATION_RESTART_FLAGS = 8


make_ready(__name__)
