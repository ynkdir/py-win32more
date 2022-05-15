from win32more import *
import win32more.System.SetupAndMigration
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.SetupAndMigration, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.SetupAndMigration, name)
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
