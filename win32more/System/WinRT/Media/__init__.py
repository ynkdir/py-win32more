from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Media.MediaFoundation
import win32more.System.WinRT
import win32more.System.WinRT.Media
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
CLSID_AudioFrameNativeFactory: Guid = Guid('16a0a3b9-9f65-4102-93-67-2c-da-3a-4f-37-2a')
CLSID_VideoFrameNativeFactory: Guid = Guid('d194386a-04e3-4814-81-00-b2-b0-ae-6d-78-c7')
class IAudioFrameNative(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('20be1e2e-930f-4746-93-35-3c-33-2f-25-50-93')
    @commethod(6)
    def GetData(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IAudioFrameNativeFactory(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('7bd67cf8-bf7d-43e6-af-8d-b1-70-ee-0c-01-10')
    @commethod(6)
    def CreateFromMFSample(data: win32more.Media.MediaFoundation.IMFSample_head, forceReadOnly: win32more.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IVideoFrameNative(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('26ba702b-314a-4620-aa-f6-7a-51-aa-58-fa-18')
    @commethod(6)
    def GetData(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevice(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IVideoFrameNativeFactory(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('69e3693e-8e1e-4e63-ac-4c-7f-dc-21-d9-73-1d')
    @commethod(6)
    def CreateFromMFSample(data: win32more.Media.MediaFoundation.IMFSample_head, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: win32more.Foundation.BOOL, minDisplayAperture: POINTER(win32more.Media.MediaFoundation.MFVideoArea_head), device: win32more.Media.MediaFoundation.IMFDXGIDeviceManager_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IAudioFrameNative')
make_head(_module, 'IAudioFrameNativeFactory')
make_head(_module, 'IVideoFrameNative')
make_head(_module, 'IVideoFrameNativeFactory')
__all__ = [
    "CLSID_AudioFrameNativeFactory",
    "CLSID_VideoFrameNativeFactory",
    "IAudioFrameNative",
    "IAudioFrameNativeFactory",
    "IVideoFrameNative",
    "IVideoFrameNativeFactory",
]
