from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Graphics.Direct2D
GRAPHICS_EFFECT_PROPERTY_MAPPING = Int32
GRAPHICS_EFFECT_PROPERTY_MAPPING_UNKNOWN: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 0
GRAPHICS_EFFECT_PROPERTY_MAPPING_DIRECT: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 1
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORX: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 2
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORY: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 3
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORZ: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 4
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORW: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 5
GRAPHICS_EFFECT_PROPERTY_MAPPING_RECT_TO_VECTOR4: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 6
GRAPHICS_EFFECT_PROPERTY_MAPPING_RADIANS_TO_DEGREES: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 7
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLORMATRIX_ALPHA_MODE: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 8
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR3: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 9
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR4: win32more.Windows.Win32.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING = 10
class IGeometrySource2DInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0657af73-53fd-47cf-84ff-c8492d2a80a3}')
    @commethod(3)
    def GetGeometry(self, value: POINTER(win32more.Windows.Win32.Graphics.Direct2D.ID2D1Geometry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TryGetGeometryUsingFactory(self, factory: win32more.Windows.Win32.Graphics.Direct2D.ID2D1Factory, value: POINTER(win32more.Windows.Win32.Graphics.Direct2D.ID2D1Geometry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetProperty(self, index: UInt32, value: POINTER(win32more.Windows.Foundation.IPropertyValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSource(self, index: UInt32, source: POINTER(win32more.Windows.Graphics.Effects.IGraphicsEffectSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
