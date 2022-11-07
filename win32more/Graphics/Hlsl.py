from win32more.base import *
import win32more.Graphics.Hlsl

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
D3DCOMPILER_DLL = 'd3dcompiler_47.dll'
D3DCOMPILE_OPTIMIZATION_LEVEL2 = 49152
D3D_COMPILE_STANDARD_FILE_INCLUDE = 1
__all__ = [
    "D3DCOMPILER_DLL",
    "D3DCOMPILE_OPTIMIZATION_LEVEL2",
    "D3D_COMPILE_STANDARD_FILE_INCLUDE",
]
