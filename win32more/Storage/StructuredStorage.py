from win32more import *

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
JET_HANDLE = UIntPtr
JET_INSTANCE = UIntPtr
JET_SESID = UIntPtr
JET_TABLEID = UIntPtr
JET_API_PTR = UIntPtr
__all__ = [
    "JET_HANDLE",
    "JET_INSTANCE",
    "JET_SESID",
    "JET_TABLEID",
    "JET_API_PTR",
]
