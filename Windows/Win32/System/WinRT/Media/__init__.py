from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
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
CLSID_AudioFrameNativeFactory: Guid = Guid('16a0a3b9-9f65-4102-93-67-2c-da-3a-4f-37-2a')
CLSID_VideoFrameNativeFactory: Guid = Guid('d194386a-04e3-4814-81-00-b2-b0-ae-6d-78-c7')
class IAudioFrameNative(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('20be1e2e-930f-4746-93-35-3c-33-2f-25-50-93')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioFrameNativeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7bd67cf8-bf7d-43e6-af-8d-b1-70-ee-0c-01-10')
    @commethod(6)
    def CreateFromMFSample(self, data: Windows.Win32.Media.MediaFoundation.IMFSample_head, forceReadOnly: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IVideoFrameNative(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('26ba702b-314a-4620-aa-f6-7a-51-aa-58-fa-18')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevice(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IVideoFrameNativeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('69e3693e-8e1e-4e63-ac-4c-7f-dc-21-d9-73-1d')
    @commethod(6)
    def CreateFromMFSample(self, data: Windows.Win32.Media.MediaFoundation.IMFSample_head, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: Windows.Win32.Foundation.BOOL, minDisplayAperture: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoArea_head), device: Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IAudioFrameNative')
make_head(_module, 'IAudioFrameNativeFactory')
make_head(_module, 'IVideoFrameNative')
make_head(_module, 'IVideoFrameNativeFactory')
