from win32more import *
import win32more.Graphics.Hlsl

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Graphics.Hlsl, name, eval(f"_define_{name}()"))
    return getattr(win32more.Graphics.Hlsl, name)
D3DCOMPILER_DLL = 'd3dcompiler_47.dll'
D3DCOMPILE_OPTIMIZATION_LEVEL2 = 49152
D3D_COMPILE_STANDARD_FILE_INCLUDE = 1
__all__ = [
    "D3DCOMPILER_DLL",
    "D3DCOMPILE_OPTIMIZATION_LEVEL2",
    "D3D_COMPILE_STANDARD_FILE_INCLUDE",
]
