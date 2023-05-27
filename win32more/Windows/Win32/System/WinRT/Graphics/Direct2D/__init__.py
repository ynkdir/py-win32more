from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Graphics.Direct2D
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
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0657af73-53fd-47cf-84ff-c8492d2a80a3}')
    @commethod(3)
    def GetGeometry(self, value: POINTER(win32more.Windows.Win32.Graphics.Direct2D.ID2D1Geometry_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TryGetGeometryUsingFactory(self, factory: win32more.Windows.Win32.Graphics.Direct2D.ID2D1Factory_head, value: POINTER(win32more.Windows.Win32.Graphics.Direct2D.ID2D1Geometry_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGraphicsEffectD2D1Interop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2fc57384-a068-44d7-a331-30982fcf7177}')
    @commethod(3)
    def GetEffectId(self, id: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamedPropertyMapping(self, name: win32more.Windows.Win32.Foundation.PWSTR, index: POINTER(UInt32), mapping: POINTER(win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProperty(self, index: UInt32, value: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSource(self, index: UInt32, source: POINTER(MissingType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IGeometrySource2DInterop')
make_head(_module, 'IGraphicsEffectD2D1Interop')
