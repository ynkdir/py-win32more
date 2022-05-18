from win32more import *
import win32more.System.HostCompute

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
HCS_CALLBACK = IntPtr
__all__ = [
    "HCS_CALLBACK",
]
