from win32more import *
import win32more.System.HostCompute

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.HostCompute, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.HostCompute, name)
HCS_CALLBACK = IntPtr
__all__ = [
    "HCS_CALLBACK",
]
