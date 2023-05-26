from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Media.MediaFoundation
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Media
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CLSID_AudioFrameNativeFactory: Guid = Guid('{16a0a3b9-9f65-4102-9367-2cda3a4f372a}')
CLSID_VideoFrameNativeFactory: Guid = Guid('{d194386a-04e3-4814-8100-b2b0ae6d78c7}')
class IAudioFrameNative(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{20be1e2e-930f-4746-9335-3c332f255093}')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioFrameNativeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7bd67cf8-bf7d-43e6-af8d-b170ee0c0110}')
    @commethod(6)
    def CreateFromMFSample(self, data: Windows.Win32.Media.MediaFoundation.IMFSample_head, forceReadOnly: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IVideoFrameNative(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{26ba702b-314a-4620-aaf6-7a51aa58fa18}')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevice(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IVideoFrameNativeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{69e3693e-8e1e-4e63-ac4c-7fdc21d9731d}')
    @commethod(6)
    def CreateFromMFSample(self, data: Windows.Win32.Media.MediaFoundation.IMFSample_head, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: Windows.Win32.Foundation.BOOL, minDisplayAperture: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoArea_head), device: Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IAudioFrameNative')
make_head(_module, 'IAudioFrameNativeFactory')
make_head(_module, 'IVideoFrameNative')
make_head(_module, 'IVideoFrameNativeFactory')
