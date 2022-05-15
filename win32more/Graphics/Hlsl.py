from win32more import *
import win32more.Graphics.Hlsl

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Graphics.Hlsl, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Graphics.Hlsl, name)
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
