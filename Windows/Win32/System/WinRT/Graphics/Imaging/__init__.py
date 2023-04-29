from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Imaging
import Windows.Win32.Media.MediaFoundation
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Graphics.Imaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CLSID_SoftwareBitmapNativeFactory: Guid = Guid('84e65691-8602-4a84-be-46-70-8b-e9-cd-4b-74')
class ISoftwareBitmapNative(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('94bc8415-04ea-4b2e-af-13-4d-e9-5a-a8-98-eb')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISoftwareBitmapNativeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c3c181ec-2914-4791-af-02-02-d2-24-a1-0b-43')
    @commethod(6)
    def CreateFromWICBitmap(self, data: Windows.Win32.Graphics.Imaging.IWICBitmap_head, forceReadOnly: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateFromMF2DBuffer2(self, data: Windows.Win32.Media.MediaFoundation.IMF2DBuffer2_head, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: Windows.Win32.Foundation.BOOL, minDisplayAperture: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoArea_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'ISoftwareBitmapNative')
make_head(_module, 'ISoftwareBitmapNativeFactory')
