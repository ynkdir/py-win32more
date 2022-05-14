from win32more import *
import win32more.System.WinRT.Graphics.Direct2D
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.WinRT.Graphics.Direct2D, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.WinRT.Graphics.Direct2D, name)
GRAPHICS_EFFECT_PROPERTY_MAPPING = Int32
GRAPHICS_EFFECT_PROPERTY_MAPPING_UNKNOWN = 0
GRAPHICS_EFFECT_PROPERTY_MAPPING_DIRECT = 1
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORX = 2
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORY = 3
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORZ = 4
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORW = 5
GRAPHICS_EFFECT_PROPERTY_MAPPING_RECT_TO_VECTOR4 = 6
GRAPHICS_EFFECT_PROPERTY_MAPPING_RADIANS_TO_DEGREES = 7
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLORMATRIX_ALPHA_MODE = 8
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR3 = 9
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR4 = 10
def _define_IGraphicsEffectD2D1Interop_head():
    class IGraphicsEffectD2D1Interop(win32more.System.Com.IUnknown_head):
        Guid = Guid('2fc57384-a068-44d7-a331-30982fcf7177')
    return IGraphicsEffectD2D1Interop
def _define_IGraphicsEffectD2D1Interop():
    IGraphicsEffectD2D1Interop = win32more.System.WinRT.Graphics.Direct2D.IGraphicsEffectD2D1Interop_head
    IGraphicsEffectD2D1Interop.GetEffectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetEffectId', ((1, 'id'),)))
    IGraphicsEffectD2D1Interop.GetNamedPropertyMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING), use_last_error=False)(4, 'GetNamedPropertyMapping', ((1, 'name'),(1, 'index'),(1, 'mapping'),)))
    IGraphicsEffectD2D1Interop.GetPropertyCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetPropertyCount', ((1, 'count'),)))
    IGraphicsEffectD2D1Interop.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p, use_last_error=False)(6, 'GetProperty', ((1, 'index'),(1, 'value'),)))
    IGraphicsEffectD2D1Interop.GetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p, use_last_error=False)(7, 'GetSource', ((1, 'index'),(1, 'source'),)))
    IGraphicsEffectD2D1Interop.GetSourceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetSourceCount', ((1, 'count'),)))
    return IGraphicsEffectD2D1Interop
def _define_IGeometrySource2DInterop_head():
    class IGeometrySource2DInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('0657af73-53fd-47cf-84ff-c8492d2a80a3')
    return IGeometrySource2DInterop
def _define_IGeometrySource2DInterop():
    IGeometrySource2DInterop = win32more.System.WinRT.Graphics.Direct2D.IGeometrySource2DInterop_head
    IGeometrySource2DInterop.GetGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head), use_last_error=False)(3, 'GetGeometry', ((1, 'value'),)))
    IGeometrySource2DInterop.TryGetGeometryUsingFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Factory_head,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head), use_last_error=False)(4, 'TryGetGeometryUsingFactory', ((1, 'factory'),(1, 'value'),)))
    return IGeometrySource2DInterop
__all__ = [
    "GRAPHICS_EFFECT_PROPERTY_MAPPING",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_UNKNOWN",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_DIRECT",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORX",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORY",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORZ",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORW",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_RECT_TO_VECTOR4",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_RADIANS_TO_DEGREES",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_COLORMATRIX_ALPHA_MODE",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR3",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR4",
    "IGraphicsEffectD2D1Interop",
    "IGeometrySource2DInterop",
]
