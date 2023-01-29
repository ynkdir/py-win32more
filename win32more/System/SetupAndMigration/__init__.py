from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.SetupAndMigration
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
def OOBEComplete(isOOBEComplete: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterWaitUntilOOBECompleted(OOBECompletedCallback: win32more.System.SetupAndMigration.OOBE_COMPLETED_CALLBACK, CallbackContext: c_void_p, WaitHandle: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWaitUntilOOBECompleted(WaitHandle: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def OOBE_COMPLETED_CALLBACK(CallbackContext: c_void_p) -> Void: ...
make_head(_module, 'OOBE_COMPLETED_CALLBACK')
__all__ = [
    "OOBEComplete",
    "OOBE_COMPLETED_CALLBACK",
    "RegisterWaitUntilOOBECompleted",
    "UnregisterWaitUntilOOBECompleted",
]
_arch_optional = [
]
