from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
CLSID_SoftwareBitmapNativeFactory: Guid = Guid('{84e65691-8602-4a84-be46-708be9cd4b74}')
class ISoftwareBitmapNative(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{94bc8415-04ea-4b2e-af13-4de95aa898eb}')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class ISoftwareBitmapNativeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c3c181ec-2914-4791-af02-02d224a10b43}')
    @commethod(6)
    def CreateFromWICBitmap(self, data: Windows.Win32.Graphics.Imaging.IWICBitmap_head, forceReadOnly: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateFromMF2DBuffer2(self, data: Windows.Win32.Media.MediaFoundation.IMF2DBuffer2_head, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: Windows.Win32.Foundation.BOOL, minDisplayAperture: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoArea_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'ISoftwareBitmapNative')
make_head(_module, 'ISoftwareBitmapNativeFactory')
