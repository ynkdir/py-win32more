from win32more import *
import win32more.System.HostCompute

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.HostCompute, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.HostCompute, name)
def __dir__():
    return __all__
HCS_CALLBACK = IntPtr
__all__ = [
    "HCS_CALLBACK",
]
