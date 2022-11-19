from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.SetupAndMigration

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
def _define_OOBE_COMPLETED_CALLBACK():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_OOBEComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("OOBEComplete", windll["KERNEL32"]), ((1, 'isOOBEComplete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterWaitUntilOOBECompleted():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.SetupAndMigration.OOBE_COMPLETED_CALLBACK,c_void_p,POINTER(c_void_p), use_last_error=True)(("RegisterWaitUntilOOBECompleted", windll["KERNEL32"]), ((1, 'OOBECompletedCallback'),(1, 'CallbackContext'),(1, 'WaitHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterWaitUntilOOBECompleted():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=True)(("UnregisterWaitUntilOOBECompleted", windll["KERNEL32"]), ((1, 'WaitHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "OOBE_COMPLETED_CALLBACK",
    "OOBEComplete",
    "RegisterWaitUntilOOBECompleted",
    "UnregisterWaitUntilOOBECompleted",
]
