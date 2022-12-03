from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media.MediaFoundation
import win32more.System.WinRT
import win32more.System.WinRT.Media
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_CLSID_AudioFrameNativeFactory():
    return Guid('16a0a3b9-9f65-4102-93-67-2c-da-3a-4f-37-2a')
def _define_CLSID_VideoFrameNativeFactory():
    return Guid('d194386a-04e3-4814-81-00-b2-b0-ae-6d-78-c7')
def _define_IAudioFrameNative_head():
    class IAudioFrameNative(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('20be1e2e-930f-4746-93-35-3c-33-2f-25-50-93')
    return IAudioFrameNative
def _define_IAudioFrameNative():
    IAudioFrameNative = win32more.System.WinRT.Media.IAudioFrameNative_head
    IAudioFrameNative.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(6, 'GetData', ((1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IAudioFrameNative
def _define_IAudioFrameNativeFactory_head():
    class IAudioFrameNativeFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('7bd67cf8-bf7d-43e6-af-8d-b1-70-ee-0c-01-10')
    return IAudioFrameNativeFactory
def _define_IAudioFrameNativeFactory():
    IAudioFrameNativeFactory = win32more.System.WinRT.Media.IAudioFrameNativeFactory_head
    IAudioFrameNativeFactory.CreateFromMFSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMFSample_head,win32more.Foundation.BOOL,POINTER(Guid),POINTER(c_void_p))(6, 'CreateFromMFSample', ((1, 'data'),(1, 'forceReadOnly'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IAudioFrameNativeFactory
def _define_IVideoFrameNative_head():
    class IVideoFrameNative(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('26ba702b-314a-4620-aa-f6-7a-51-aa-58-fa-18')
    return IVideoFrameNative
def _define_IVideoFrameNative():
    IVideoFrameNative = win32more.System.WinRT.Media.IVideoFrameNative_head
    IVideoFrameNative.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(6, 'GetData', ((1, 'riid'),(1, 'ppv'),)))
    IVideoFrameNative.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(7, 'GetDevice', ((1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IVideoFrameNative
def _define_IVideoFrameNativeFactory_head():
    class IVideoFrameNativeFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('69e3693e-8e1e-4e63-ac-4c-7f-dc-21-d9-73-1d')
    return IVideoFrameNativeFactory
def _define_IVideoFrameNativeFactory():
    IVideoFrameNativeFactory = win32more.System.WinRT.Media.IVideoFrameNativeFactory_head
    IVideoFrameNativeFactory.CreateFromMFSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMFSample_head,POINTER(Guid),UInt32,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Media.MediaFoundation.MFVideoArea_head),win32more.Media.MediaFoundation.IMFDXGIDeviceManager_head,POINTER(Guid),POINTER(c_void_p))(6, 'CreateFromMFSample', ((1, 'data'),(1, 'subtype'),(1, 'width'),(1, 'height'),(1, 'forceReadOnly'),(1, 'minDisplayAperture'),(1, 'device'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IVideoFrameNativeFactory
__all__ = [
    "CLSID_AudioFrameNativeFactory",
    "CLSID_VideoFrameNativeFactory",
    "IAudioFrameNative",
    "IAudioFrameNativeFactory",
    "IVideoFrameNative",
    "IVideoFrameNativeFactory",
]
