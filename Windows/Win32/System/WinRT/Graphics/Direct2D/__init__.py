from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct2D
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Graphics.Direct2D
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
GRAPHICS_EFFECT_PROPERTY_MAPPING = Int32
GRAPHICS_EFFECT_PROPERTY_MAPPING_UNKNOWN: GRAPHICS_EFFECT_PROPERTY_MAPPING = 0
GRAPHICS_EFFECT_PROPERTY_MAPPING_DIRECT: GRAPHICS_EFFECT_PROPERTY_MAPPING = 1
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORX: GRAPHICS_EFFECT_PROPERTY_MAPPING = 2
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORY: GRAPHICS_EFFECT_PROPERTY_MAPPING = 3
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORZ: GRAPHICS_EFFECT_PROPERTY_MAPPING = 4
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORW: GRAPHICS_EFFECT_PROPERTY_MAPPING = 5
GRAPHICS_EFFECT_PROPERTY_MAPPING_RECT_TO_VECTOR4: GRAPHICS_EFFECT_PROPERTY_MAPPING = 6
GRAPHICS_EFFECT_PROPERTY_MAPPING_RADIANS_TO_DEGREES: GRAPHICS_EFFECT_PROPERTY_MAPPING = 7
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLORMATRIX_ALPHA_MODE: GRAPHICS_EFFECT_PROPERTY_MAPPING = 8
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR3: GRAPHICS_EFFECT_PROPERTY_MAPPING = 9
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR4: GRAPHICS_EFFECT_PROPERTY_MAPPING = 10
class IGeometrySource2DInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0657af73-53fd-47cf-84-ff-c8-49-2d-2a-80-a3')
    @commethod(3)
    def GetGeometry(self, value: POINTER(Windows.Win32.Graphics.Direct2D.ID2D1Geometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TryGetGeometryUsingFactory(self, factory: Windows.Win32.Graphics.Direct2D.ID2D1Factory_head, value: POINTER(Windows.Win32.Graphics.Direct2D.ID2D1Geometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGraphicsEffectD2D1Interop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2fc57384-a068-44d7-a3-31-30-98-2f-cf-71-77')
    @commethod(3)
    def GetEffectId(self, id: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamedPropertyMapping(self, name: Windows.Win32.Foundation.PWSTR, index: POINTER(UInt32), mapping: POINTER(Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyCount(self, count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProperty(self, index: UInt32, value: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSource(self, index: UInt32, source: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceCount(self, count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IGeometrySource2DInterop')
make_head(_module, 'IGraphicsEffectD2D1Interop')
